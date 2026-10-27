import json, sys, chess

payload = json.load(sys.stdin)
fen = payload.get('fen')
moves = payload.get('moves', [])
side = payload.get('side_to_move', 'white')
my_color = chess.WHITE if side == 'white' else chess.BLACK

board = chess.Board(fen)
hist = chess.Board()
keys = []
ok = True
for uci in moves:
    try:
        mv = chess.Move.from_uci(uci)
        if mv not in hist.legal_moves:
            ok = False
            break
        hist.push(mv)
        keys.append(hist.fen().split(' ')[0:4])
    except Exception:
        ok = False
        break

if ok and hist.fen().split(' ')[0:4] == fen.split(' ')[0:4]:
    board = hist
else:
    keys = []

vals = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}
def material(b, color):
    total = 0
    for sq in chess.SQUARES:
        p = b.piece_at(sq)
        if p and p.color == color and p.piece_type in vals:
            total += vals[p.piece_type]
    return total

diff = material(board, my_color) - material(board, not my_color)
risk = []
for mv in board.legal_moves:
    b2 = board.copy()
    b2.push(mv)
    key = b2.fen().split(' ')[0:4]
    count = 1 + sum(1 for k in keys if k == key)
    if count >= 3:
        risk.append((mv.uci(), count, 'threefold'))
    elif diff >= 1 and count >= 2:
        risk.append((mv.uci(), count, 'repeats while material up'))

if risk:
    for uci, count, why in risk:
        print(uci + ': position occurrence ' + str(count) + ' (' + why + ')')
    print('AVOID: ' + ' '.join(sorted(set(u for u, _, _ in risk))))
else:
    print('repetition guard: no threefold risk (material diff ' + str(diff) + ')')
