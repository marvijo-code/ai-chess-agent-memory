import json, sys, chess
p = json.load(sys.stdin)
b = chess.Board(p["fen"])
vals = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}
scores = {}
for color, name in ((chess.WHITE, "WHITE"), (chess.BLACK, "BLACK")):
    pcs = []
    pawns = minors = 0
    for sq in chess.SQUARES:
        pc = b.piece_at(sq)
        if pc and pc.color == color and pc.piece_type != chess.KING:
            pcs.append(chess.square_name(sq) + pc.symbol())
            if pc.piece_type == chess.PAWN:
                pawns += 1
            elif pc.piece_type in (chess.KNIGHT, chess.BISHOP):
                minors += 1
    scores[name] = vals[pawns and chess.PAWN or chess.PAWN] * 0  # placeholder, replaced below
# compute properly
scores = {}
for color, name in ((chess.WHITE, "WHITE"), (chess.BLACK, "BLACK")):
    s = 0
    pcs = []
    for sq in chess.SQUARES:
        pc = b.piece_at(sq)
        if pc and pc.color == color and pc.piece_type != chess.KING:
            pcs.append(chess.square_name(sq) + pc.symbol())
            s += vals[pc.piece_type]
    scores[name] = s
    print(f"{name} ({s}): {' '.join(pcs) if pcs else 'none'}")
diff = scores["WHITE"] - scores["BLACK"]
print(f"material white-black: {diff:+d}" )
sme = chess.WHITE if p.get("side_to_move", "white") == "white" else chess.BLACK
mine = scores["WHITE"] if sme == chess.WHITE else scores["BLACK"]
other = scores["BLACK"] if sme == chess.WHITE else scores["WHITE"]
print(f"MY total {mine} vs HIS {other}: {'I AM UP' if mine > other else 'I AM DOWN' if mine < other else 'level'}")
