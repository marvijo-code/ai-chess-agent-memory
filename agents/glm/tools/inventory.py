import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])

# The T73R3 kill was NOT chess: three prose replies ('BEST SO FAR: ...')
# instead of the requested JSON object = forfeit. Repeat it every move.
print("REPLY FORMAT: your ENTIRE answer must be ONE JSON object - no prose, no 'BEST SO FAR', no analysis outside it. A non-JSON reply = one try; 3 = forfeit (T73R3).")

# Rebuild both armies from the CURRENT fen (ghost-board kill).
for color, tag in ((chess.WHITE, "W"), (chess.BLACK, "B")):
    items = []
    for sq in chess.SQUARES:
        p = board.piece_at(sq)
        if p is not None and p.color == color:
            items.append(p.symbol() + chess.square_name(sq))
    if items:
        print(tag + " army: " + " ".join(items))
    else:
        print(tag + " army: none")

mine = chess.WHITE if payload.get("side_to_move") == "white" else chess.BLACK
loose = []
for sq in chess.SQUARES:
    p = board.piece_at(sq)
    if p is not None and p.color == mine and p.piece_type != chess.KING:
        if board.attackers(not mine, sq) and not board.attackers(mine, sq):
            loose.append(p.symbol() + chess.square_name(sq))
if loose:
    print("your loose units (attacked, zero defenders): " + " ".join(loose))
else:
    print("no loose units of yours")