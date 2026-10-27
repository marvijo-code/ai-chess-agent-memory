import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
val = {chess.QUEEN: 9, chess.ROOK: 5, chess.BISHOP: 3, chess.KNIGHT: 3, chess.PAWN: 1}

def material(color):
    total = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.color == color and piece.piece_type != chess.KING:
            total += val[piece.piece_type]
    return total

mine = material(board.turn)
theirs = material(not board.turn)
diff = mine - theirs

clocks = payload.get("clocks", {})
you_ms = clocks.get("you_ms")
opp_ms = clocks.get("opponent_ms")

def fmt(ms):
    return "?" if ms is None else f"{ms/1000:.0f}s"

print(f"Material: you {mine}, opponent {theirs}, diff {diff:+d}.")
print(f"Clock: you {fmt(you_ms)}, opponent {fmt(opp_ms)}.")
if diff > 0:
    print("UP MATERIAL: play 5-10 s, trade pieces not pawns, avoid repetition, keep every unit guarded.")
elif diff < 0:
    print("DOWN MATERIAL: 5-10 s defensive moves, no grabs, keep units guarded.")
else:
    print("Material level: no grabs; every unit guarded.")

for square in chess.SQUARES:
    piece = board.piece_at(square)
    if piece and piece.color == board.turn and piece.piece_type != chess.KING:
        if board.attackers(not board.turn, square) and not board.attackers(board.turn, square):
            print(f"LOOSE: your {piece.symbol()} on {chess.square_name(square)}")

print("AVOID:")
