import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
mine = board.turn
VALUES = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}

def material(color):
    total = 0
    for piece in board.piece_map().values():
        if piece.color == color:
            total += VALUES[piece.piece_type]
    return total

diff = material(mine) - material(not mine)
checks = []
captures = []
for move in board.legal_moves:
    san = board.san(move)
    if board.is_capture(move):
        captures.append(san)
    board.push(move)
    if board.is_check():
        checks.append(san)
    board.pop()

print("material (pawn units) mine-minus-his: %+d" % diff)
print("my checks: " + (", ".join(checks) if checks else "none"))
print("my captures: " + (", ".join(captures) if captures else "none"))
if diff >= 5:
    print("UP BIG: a big lead is a mate problem. Play a check, a capture, or a rook lift toward his king; do NOT shuffle and do NOT repeat the position.")
