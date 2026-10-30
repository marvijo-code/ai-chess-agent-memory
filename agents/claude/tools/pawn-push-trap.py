import json, sys, chess

V = {1: 1, 2: 3, 3: 3, 4: 5, 5: 9, 6: 99}


def minatt(b, color, sq):
    vals = [V[b.piece_type_at(s)] for s in b.attackers(color, sq)]
    return min(vals) if vals else None


def has_safe(b, sq):
    me = b.turn
    val = V[b.piece_type_at(sq)]
    for m in list(b.legal_moves):
        if m.from_square != sq:
            continue
        b.push(m)
        a = minatt(b, not me, m.to_square)
        ok = a is None or (a >= val and b.is_attacked_by(me, m.to_square))
        b.pop()
        if ok:
            return True
    return False


def trapped(b, p):
    me = b.turn
    out = []
    for sq in b.attacks(p):
        pc = b.piece_at(sq)
        if pc and pc.color == me and pc.piece_type not in (chess.PAWN, chess.KING):
            if not has_safe(b, sq):
                out.append(sq)
    return out


def escape(b, p):
    me = b.turn
    for m in list(b.legal_moves):
        if m.to_square != p:
            continue
        if b.piece_type_at(m.from_square) != chess.PAWN:
            if not b.is_attacked_by(not me, p):
                return True
            continue
        b.push(m)
        ok = True
        for r in list(b.legal_moves):
            if r.to_square == p and b.piece_type_at(r.from_square) == chess.PAWN:
                b.push(r)
                if trapped(b, p):
                    ok = False
                b.pop()
        b.pop()
        if ok:
            return True
    return False


def threats(b):
    res = {}
    for m in list(b.legal_moves):
        if b.piece_type_at(m.from_square) != chess.PAWN:
            continue
        b.push(m)
        p = m.to_square
        tr = trapped(b, p)
        if tr and not escape(b, p):
            for sq in tr:
                res[sq] = m.uci()
        b.pop()
    return res


def main():
    payload = json.load(sys.stdin)
    board = chess.Board(payload["fen"])
    base = {}
    if not board.is_check():
        board.push(chess.Move.null())
        base = threats(board)
        board.pop()
    lines = []
    for sq, mv in base.items():
        lines.append("EXISTING: his pawn push %s would trap my piece on %s (no safe square)" % (mv, chess.square_name(sq)))
    for m in list(board.legal_moves):
        board.push(m)
        th = {} if board.is_game_over() else threats(board)
        board.pop()
        for sq, mv in th.items():
            if sq in base and sq != m.to_square:
                continue
            lines.append("AVOID: %s - then his pawn push %s hits my piece on %s which has no safe square (trapped, lost for a pawn)" % (m.uci(), mv, chess.square_name(sq)))
            break
    if not lines:
        print("no pawn-push trap found")
    else:
        for l in lines[:10]:
            print(l)


main()
