import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
me = board.turn
opp = not me
legal = list(board.legal_moves)
bad = {}

for mv in legal:
    board.push(mv)
    for r in list(board.legal_moves):
        pc = board.piece_at(r.from_square)
        if pc is None or pc.piece_type != chess.PAWN or r.promotion:
            continue
        board.push(r)
        sq = r.to_square
        targets = []
        for s in board.attacks(sq):
            q = board.piece_at(s)
            if q and q.color == me and q.piece_type in (2, 3, 4, 5):
                targets.append(s)
        if targets:
            can_take_with_pawn = False
            for m2 in board.legal_moves:
                p2 = board.piece_at(m2.from_square)
                if m2.to_square == sq and p2 and p2.piece_type == chess.PAWN:
                    can_take_with_pawn = True
            guarded = bool(board.attackers(opp, sq))
            if not can_take_with_pawn and guarded:
                trapped = []
                for s in targets:
                    safe = False
                    for m2 in board.legal_moves:
                        if m2.from_square == s and not board.is_attacked_by(opp, m2.to_square):
                            safe = True
                    if not safe:
                        trapped.append(s)
                if len(targets) >= 2 or trapped:
                    names = ",".join(chess.square_name(s) for s in targets)
                    bad.setdefault(mv.uci(), []).append(
                        "%s hits %s" % (r.uci(), names))
        board.pop()
    board.pop()

if len(bad) >= len(legal):
    print("Pawn-push threat exists against every move (already on the board): no AVOID.")
else:
    for u, why in sorted(bad.items()):
        print("%s allows pawn push %s (guarded pawn, no pawn capture; fork or no safe retreat)" % (u, why[0]))
    if bad:
        print("AVOID: " + " ".join(sorted(bad)))
    else:
        print("no guarded pawn push forks two pieces or traps a piece (2-ply check only)")
