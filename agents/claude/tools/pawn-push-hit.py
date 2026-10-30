import json, sys, chess

V = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}


def cap_value(b, mv):
    if b.is_en_passant(mv):
        return 1
    p = b.piece_at(mv.to_square)
    return V[p.piece_type] if p else 0


def opp_gain(b):
    # best simple capture for the side to move (value won minus value lost on recapture)
    me = not b.turn
    best = 0
    for c in b.legal_moves:
        if not b.is_capture(c):
            continue
        cap = cap_value(b, c)
        mover = V[b.piece_at(c.from_square).piece_type]
        b.push(c)
        rec = b.is_attacked_by(me, c.to_square)
        b.pop()
        g = cap - (mover if rec else 0)
        if g > best:
            best = g
    return best


def main():
    payload = json.load(sys.stdin)
    board = chess.Board(payload["fen"])
    me = board.turn
    opp = not me
    flagged = []
    for m in list(board.legal_moves):
        san = board.san(m)
        # my pieces already hit by an enemy pawn before the move: not new
        pre = set()
        for sq in chess.SQUARES:
            pc = board.piece_at(sq)
            if pc and pc.color == me and V[pc.piece_type] >= 3:
                for a in board.attackers(opp, sq):
                    if board.piece_at(a).piece_type == chess.PAWN:
                        pre.add(sq)
        board.push(m)
        if board.is_game_over():
            board.pop()
            continue
        base = opp_gain(board)
        found = None
        for p in list(board.legal_moves):
            pc = board.piece_at(p.from_square)
            if pc.piece_type != chess.PAWN or board.is_capture(p) or p.promotion:
                continue
            board.push(p)
            targets = []
            for sq in board.attacks(p.to_square):
                pp = board.piece_at(sq)
                if pp and pp.color == me and V[pp.piece_type] >= 3 and sq not in pre:
                    targets.append(sq)
            if targets:
                minloss = 99
                for r in list(board.legal_moves):
                    g_me = 0
                    if board.is_capture(r):
                        cap = cap_value(board, r)
                        mover = V[board.piece_at(r.from_square).piece_type]
                        board.push(r)
                        rec = board.is_attacked_by(opp, r.to_square)
                        loss = opp_gain(board)
                        board.pop()
                        g_me = max(0, cap - (mover if rec else 0))
                    else:
                        board.push(r)
                        loss = opp_gain(board)
                        board.pop()
                    loss -= g_me
                    if loss < minloss:
                        minloss = loss
                    if minloss < 2:
                        break
                if minloss != 99 and minloss >= 2 and minloss > base + 1:
                    found = (p, targets[0], minloss)
            board.pop()
            if found:
                break
        board.pop()
        if found:
            p, sq, loss = found
            flagged.append((m.uci(), san, p.uci(), chess.square_name(sq), loss))
    if flagged:
        print("pawn-push-hit: %d moves allow a pawn push that wins a piece" % len(flagged))
        for u, san, pu, sqn, loss in flagged[:12]:
            print("AVOID: %s - %s allows %s and the pawn hits my piece on %s with no good reply (about -%d)" % (u, san, pu, sqn, loss))
    else:
        print("pawn-push-hit: no move allows a winning pawn push (one-ply check)")


main()
