import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
stm = payload.get("side_to_move")
mine = chess.WHITE if stm == "white" else chess.BLACK if stm == "black" else board.turn
yours, his = [], []
for sq in chess.SQUARES:
    p = board.piece_at(sq)
    if p:
        (yours if p.color == mine else his).append(p.symbol() + chess.square_name(sq))
print("side to move: " + ("white" if mine == chess.WHITE else "black"))
print("YOU: " + " ".join(yours))
print("HIM: " + " ".join(his))