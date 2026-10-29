import json, sys
import chess

VAL = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}

payload = json.load(sys.stdin)
board = chess.Board(payload['fen'])
me = board.turn
you = not me

kingsq = board.king(me)
if kingsq is None:
    kfile, krank = -9, -9
else:
    kfile = chess.square_file(kingsq)
    krank = chess.square_rank(kingsq)

def hangs(b):
    free, konly = set(), set()
    for sq in chess.SQUARES:
        pc = b.piece_at(sq)
        if pc is None or pc.color != me or pc.piece_type == chess.KING:
            continue
        if not b.attackers(you, sq):
            continue
        guards = b.attackers(me, sq)
        if not guards:
            free.add(sq)
        elif all(b.piece_type_at(d) == chess.KING for d in guards):
            konly.add(sq)
    return free, konly

pre_free, pre_ko = hangs(board)
avoid = []
shown = 0
for mv in list(board.legal_moves):
    san = board.san(mv)
    board.push(mv)
    free, konly = hangs(board)
    msgs = []
    bad = False
    for sq in sorted(free - pre_free, key=lambda s: -VAL[board.piece_type_at(s)]):
        pc = board.piece_at(sq)
        v = VAL[pc.piece_type]
        atks = [a for a in board.attackers(you, sq) if board.piece_type_at(a) != chess.KING]
        if not atks:
            continue
        cheapest = min(VAL[board.piece_type_at(a)] for a in atks)
        who = ','.join(sorted(chess.square_name(a) for a in atks))
        shell_pawn = (pc.piece_type == chess.PAWN and abs(chess.square_file(sq) - kfile) <= 1
                      and abs(chess.square_rank(sq) - krank) <= 2)
        tag = 'SHELL PAWN FREE' if shell_pawn else ('FREE LOSS' if v - cheapest >= 2 else 'loose (equal trade risk)')
        msgs.append('%s%s -> free to %s (%s)' % (pc.symbol(), chess.square_name(sq), who, tag))
        if v - cheapest >= 2 or shell_pawn:
            bad = True
    for sq in sorted(konly - pre_ko, key=lambda s: -VAL[board.piece_type_at(s)]):
        pc = board.piece_at(sq)
        atks = [a for a in board.attackers(you, sq) if board.piece_type_at(a) != chess.KING]
        if not atks:
            continue
        who = ','.join(sorted(chess.square_name(a) for a in atks))
        msgs.append('%s%s -> king-only recapture vs %s' % (pc.symbol(), chess.square_name(sq), who))
    board.pop()
    if msgs and shown < 8:
        print(san + ': ' + '; '.join(msgs[:2]) + (' (+more)' if len(msgs) > 2 else ''))
        shown += 1
    if bad:
        avoid.append(mv.uci())

if shown == 0:
    print('no move hands him a new free capture or a king-only recapture')
if avoid:
    print('AVOID: ' + ' '.join(sorted(set(avoid))))
else:
    print('AVOID: (none)')