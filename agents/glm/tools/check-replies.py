import json, sys, chess
p = json.load(sys.stdin)
b = chess.Board(p["fen"])
mine = b.turn
VAL = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}

def mat(bd):
    s = 0
    for pc in bd.piece_map().values():
        v = VAL[pc.piece_type]
        s += v if pc.color == mine else -v
    return s

if not b.is_check():
    print("not in check")
else:
    base = mat(b)
    rows = []
    for m in b.legal_moves:
        san = b.san(m)
        uci = m.uci()
        b.push(m)
        worst = 0
        mated = False
        for om in b.legal_moves:
            cap = b.is_capture(om)
            b.push(om)
            if b.is_checkmate():
                mated = True
            if cap:
                loss = base - mat(b)
                if loss > worst:
                    worst = loss
            b.pop()
        b.pop()
        rows.append((mated, worst, uci, san))
    rows.sort(key=lambda r: (r[0], r[1]))
    print("IN CHECK: " + str(len(rows)) + " legal replies - send the TOP uci verbatim, one try, 5 s")
    for mated, worst, uci, san in rows[:12]:
        if mated:
            print("AVOID: " + uci + " " + san + " - MATE-1 NEXT")
        else:
            print(uci + " " + san + " - worst capture reply -" + str(worst))
