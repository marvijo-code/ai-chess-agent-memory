import json, sys, time, chess

V = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 99}


def unsafe(b, me):
    out = []
    for sq, p in b.piece_map().items():
        if p.color != me or p.piece_type in (chess.PAWN, chess.KING):
            continue
        att = b.attackers(not me, sq)
        if not att:
            continue
        low = min(V[b.piece_type_at(a)] for a in att)
        if low < V[p.piece_type] or not b.is_attacked_by(me, sq):
            out.append(sq)
    return out


def fixable(b, me):
    for m in list(b.legal_moves):
        b.push(m)
        ok = not unsafe(b, me)
        b.pop()
        if ok:
            return True
    return False


def main():
    payload = json.load(sys.stdin)
    board = chess.Board(payload["fen"])
    me = board.turn
    base = unsafe(board, me)
    if base:
        print("already attacked now: " + " ".join(chess.square_name(s) for s in base) + " (only mates are flagged below)")
    t0 = time.time()
    bad = []
    lines = 0
    for m in list(board.legal_moves):
        if time.time() - t0 > 6:
            print("time budget hit, check incomplete")
            break
        san = board.san(m)
        board.push(m)
        found = None
        if not board.is_checkmate() and not board.is_stalemate():
            for r in list(board.legal_moves):
                rs = board.san(r)
                board.push(r)
                if board.is_checkmate():
                    found = "%s allows mate" % rs
                elif not base and not board.is_stalemate():
                    u = unsafe(board, me)
                    if u and not fixable(board, me):
                        found = "%s wins a piece on %s (pin/fork, no fix)" % (rs, chess.square_name(u[0]))
                board.pop()
                if found:
                    break
        board.pop()
        if found:
            bad.append(m.uci())
            if lines < 5:
                print("%s: reply %s" % (san, found))
                lines += 1
    if bad:
        print("AVOID: " + " ".join(bad))
    else:
        print("pin-fork-trap: no 2-ply mate or unfixable attack on a piece found")


main()
