import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
mine = chess.WHITE if payload["side_to_move"] == "white" else chess.BLACK
opp = not mine
vals = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}
probe = board.copy(stack=False)
probe.turn = opp
items = []
for mv in list(probe.generate_pseudo_legal_moves()):
    pt = probe.piece_type_at(mv.from_square)
    if pt not in (chess.PAWN, chess.KNIGHT):
        continue
    b2 = probe.copy(stack=False)
    if not b2.is_legal(mv):
        continue
    b2.push(mv)
    tags = []
    worst = 0
    if b2.is_check():
        tags.append("CHECK on my king (discovered or direct)")
        worst = 9
    for t in chess.SQUARES:
        q = b2.piece_at(t)
        if q and q.color == mine and q.piece_type != chess.KING:
            if b2.attackers(opp, t) and not b2.attackers(mine, t):
                tags.append(chess.piece_name(q.piece_type).capitalize() + " on " + chess.square_name(t) + " loose")
                worst = max(worst, vals[q.piece_type])
    if tags:
        items.append((0 if b2.is_check() else 1, -worst, "HIS " + probe.san(mv) + ": " + "; ".join(tags)))
items.sort()
lines = [it[2] for it in items]
if lines:
    print("top pawn/knight threats against me:")
    for line in lines[:15]:
        print(line)
else:
    print("no his pawn push/knight jump leaves a loose piece of mine or gives check")
