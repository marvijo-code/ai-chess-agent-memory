import json, sys, chess

PV = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
me = board.turn

def mat(b):
    d = 0
    for pc in b.piece_map().values():
        v = PV[pc.piece_type]
        d += v if pc.color == me else -v
    return d

start = mat(board)

def side_best(b, maximizer):
    cur = mat(b)
    top = None
    for m in list(b.legal_moves):
        if not b.is_capture(m):
            continue
        nxt = b.copy()
        nxt.push(m)
        v = mat(nxt)
        good = v >= cur if maximizer else v <= cur
        if good and (top is None or (maximizer and v > top[1]) or (not maximizer and v < top[1])):
            top = (m, v)
    return (cur if top is None else top[1]), (None if top is None else top[0])

flags = []
lines = []
for move in list(board.legal_moves):
    name = board.san(move)
    nxt = board.copy()
    nxt.push(move)
    tgt = move.to_square
    v0, _ = side_best(nxt, False)
    if v0 > start - 2:
        continue
    recs = [r for r in list(nxt.legal_moves) if r.to_square == tgt and nxt.is_capture(r)]
    vals = [v0]
    for rec in recs:
        two = nxt.copy()
        two.push(rec)
        v2, _ = side_best(two, True)
        vals.append(v2)
    if max(vals) > start - 2:
        continue
    flags.append(move.uci())
    if len(lines) < 6:
        hs = "nothing (another capture elsewhere)"
        if recs:
            worst = vals.index(min(vals))
            hs = nxt.san(recs[worst - 1]) if worst else hs
        lines.append(f"{name}: {hs}! and I stay down {start - min(vals)} on every branch (in-kind / survivor check)")

if lines:
    for L in lines:
        print(L)
    print("AVOID: " + " ".join(flags))
else:
    print("no move loses material on all branches (greedy capture sweep)")
    print("AVOID:")