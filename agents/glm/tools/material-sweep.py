import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
vals = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}
names = {chess.WHITE: [], chess.BLACK: []}
tot = {chess.WHITE: 0, chess.BLACK: 0}
for sq in chess.SQUARES:
    p = board.piece_at(sq)
    if not p:
        continue
    names[p.color].append(p.symbol().upper() + chess.square_name(sq))
    tot[p.color] += vals.get(p.piece_type, 0)
w, b = tot[chess.WHITE], tot[chess.BLACK]
if w == b:
    print(f"W {w} v B {b} LEVEL - any '+' claim in my notes is a GHOST")
else:
    who = "W" if w > b else "B"
    print(f"W {w} v B {b} - {who} +{abs(w - b)}")
print("W pieces: " + " ".join(names[chess.WHITE]))
print("B pieces: " + " ".join(names[chess.BLACK]))
