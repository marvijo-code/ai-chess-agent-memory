import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
me = board.turn
opp = not me
lines = []
bad = []

# A) my pieces pinned by an enemy slider facing my king
for sq in chess.SQUARES:
    pc = board.piece_at(sq)
    if pc and pc.color == me and pc.piece_type != chess.KING and board.is_pinned(me, sq):
        for a in board.attackers(opp, sq):
            ap = board.piece_at(a)
            if ap and ap.piece_type in (chess.QUEEN, chess.ROOK, chess.BISHOP, chess.PAWN):
                lines.append("PINNED: your %s on %s pinned by the %s on %s; any move off that line is illegal" % (
                    pc.symbol(), chess.square_name(sq), ap.symbol(), chess.square_name(a)))
                break

# B) my pawn pushes that attack a knight/bishop which can escape with capture-check
for mv in list(board.legal_moves):
    if board.piece_type_at(mv.from_square) != chess.PAWN:
        continue
    san = board.san(mv)
    board.push(mv)
    for t in list(board.attacks(mv.to_square)):
        tp = board.piece_at(t)
        if not tp or tp.color != opp or tp.piece_type not in (chess.KNIGHT, chess.BISHOP):
            continue
        escapes = []
        for om in list(board.legal_moves):
            if om.from_square == t and board.gives_check(om) and board.is_capture(om):
                escapes.append(board.san(om))
        if escapes:
            lines.append("KICK: %s attacks the %s on %s, which escapes with CAPTURE-CHECK (%s) - the pawn push loses material" % (
                san, tp.symbol(), chess.square_name(t), ", ".join(escapes[:3])))
            bad.append(mv.uci())
    board.pop()

if lines:
    for l in lines[:8]:
        print(l)
if bad:
    print("AVOID: " + " ".join(sorted(set(bad))))
else:
    print("no pin and no kick-escape finding on pawn moves")
