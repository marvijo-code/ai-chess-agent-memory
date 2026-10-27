import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload['fen'])
me = board.turn
them = not me


def units(b):
    return [(sq, p) for sq, p in b.piece_map().items()
            if p.color == me and p.piece_type != chess.KING]


base = {sq: len(board.attackers(me, sq)) for sq, _ in units(board)}
bad = []
for move in list(board.legal_moves):
    san = board.san(move)
    mover = board.piece_at(move.from_square)
    capture = board.is_capture(move)
    board.push(move)
    to = move.to_square
    if mover is not None and mover.piece_type != chess.KING and not capture:
        if board.attackers(them, to) and not board.attackers(me, to):
            bad.append(move.uci())
            print(san + ' lands your ' + chess.piece_name(mover.piece_type) + ' on ' + chess.square_name(to) + ' unguarded and attacked')
    for sq, p in units(board):
        if sq == to or sq not in base:
            continue
        d0 = base[sq]
        d1 = len(board.attackers(me, sq))
        a1 = len(board.attackers(them, sq))
        if a1 and d1 < d0 and d1 < a1:
            bad.append(move.uci())
            print(san + ' cuts a guard of your ' + chess.piece_name(p.piece_type) + ' on ' + chess.square_name(sq) + ': guards ' + str(d0) + ' -> ' + str(d1) + ', his attackers ' + str(a1))
    board.pop()

if bad:
    print('AVOID: ' + ' '.join(sorted(set(bad))))
else:
    print('no guard cut, no quiet piece landing loose')
