import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
mine = board.turn
his = not mine
findings = []
avoid = []

# my pieces ALREADY attacked by his pawns: pawn-takes-piece = piece for pawn
for sq in chess.SQUARES:
    p = board.piece_at(sq)
    if p and p.color == mine and p.piece_type in (chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN):
        pa = [s for s in board.attackers(his, sq) if board.piece_type_at(s) == chess.PAWN]
        if pa:
            names = ", ".join(chess.square_name(s) for s in sorted(pa))
            findings.append("your %s on %s is eaten by his pawn on %s: move it now (piece-for-pawn)" % (p.symbol(), chess.square_name(sq), names))
            if len(findings) >= 3:
                break

# landings his pawns capture with no guard of mine
for move in list(board.legal_moves):
    piece = board.piece_at(move.from_square)
    if piece is None or piece.piece_type == chess.PAWN:
        continue
    board.push(move)
    sq = move.to_square
    pa = [s for s in board.attackers(his, sq) if board.piece_type_at(s) == chess.PAWN]
    defs = board.attackers(mine, sq)
    board.pop()
    if pa and not defs:
        names = ", ".join(chess.square_name(s) for s in sorted(pa))
        findings.append("%s lands your %s on %s where his pawn on %s takes it undefended" % (move.uci(), piece.symbol(), chess.square_name(sq), names))
        avoid.append(move.uci())
        if len(avoid) >= 6:
            break

if not findings:
    print("no pawn-capturer findings")
for f in findings:
    print(f)
if avoid:
    print("AVOID: " + " ".join(avoid))