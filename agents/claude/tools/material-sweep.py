import json, sys, chess

V = {1: 1, 2: 3, 3: 3, 4: 5, 5: 9, 6: 0}


def mat(b):
    s = 0
    for sq, p in b.piece_map().items():
        if p.piece_type != chess.KING:
            s += V[p.piece_type] * (1 if p.color == chess.WHITE else -1)
    return s


def best_gain(b):
    best = 0
    bm = None
    for m in b.legal_moves:
        if not b.is_capture(m):
            continue
        if b.is_en_passant(m):
            victim = 1
        else:
            victim = V[b.piece_at(m.to_square).piece_type]
        att = V[b.piece_at(m.from_square).piece_type]
        b.push(m)
        defended = bool(b.attackers(b.turn, m.to_square))
        b.pop()
        g = victim - (att if defended else 0)
        if g > best:
            best = g
            bm = m
    return best, bm


def main():
    p = json.load(sys.stdin)
    b = chess.Board(p["fen"])
    me = b.turn
    d = mat(b) * (1 if me == chess.WHITE else -1)
    print("Material for side to move: %+d (P1 minor3 R5 Q9)" % d)
    base = 0
    if not b.is_check():
        b.push(chess.Move.null())
        base = best_gain(b)[0]
        b.pop()
    lines = []
    for m in list(b.legal_moves):
        san = b.san(m)
        mg = 0
        if b.is_capture(m):
            mg = 1 if b.is_en_passant(m) else V[b.piece_at(m.to_square).piece_type]
        b.push(m)
        if b.is_checkmate():
            b.pop()
            continue
        mated = False
        for om in list(b.legal_moves):
            b.push(om)
            if b.is_checkmate():
                mated = True
            b.pop()
            if mated:
                break
        if mated:
            lines.append("AVOID: %s - %s allows mate in 1" % (m.uci(), san))
        else:
            g, om = best_gain(b)
            if om is not None and g > base and g - mg >= 2:
                lines.append("AVOID: %s - %s lets %s win about %d points (new loss; already-attacked units are NOT flagged)" % (m.uci(), san, om.uci(), g - mg))
        b.pop()
    if base >= 2:
        print("Note: a unit of mine is already attacked (about %d points); moves that do not fix it are not flagged." % base)
    for l in lines[:8]:
        print(l)
    if not lines:
        print("no new material loss found")


main()
