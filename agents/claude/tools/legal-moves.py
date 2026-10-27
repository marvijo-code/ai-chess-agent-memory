import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
me = board.turn
VAL = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}
king, caps, checks, avoid = [], [], [], []
for move in board.legal_moves:
    piece = board.piece_at(move.from_square)
    san = board.san(move)
    if piece.piece_type == chess.KING and not board.is_castling(move):
        king.append(chess.square_name(move.to_square))
    if board.is_capture(move):
        caps.append(san)
    if board.gives_check(move):
        checks.append(san)
    if piece.piece_type in (chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT):
        target = board.piece_at(move.to_square)
        got = VAL[target.piece_type] if target else 0
        for a in board.attackers(not me, move.to_square):
            ap = board.piece_at(a)
            if ap.piece_type == chess.PAWN and got < VAL[piece.piece_type]:
                avoid.append(move.uci())
                print(f"{san}: lands on a square his pawn on {chess.square_name(a)} captures")
                break
print("Legal king squares (only these are legal): " + (" ".join(king) if king else "none"))
print("Captures: " + (" ".join(caps) if caps else "none"))
print("Checks: " + (" ".join(checks) if checks else "none"))
print("Legal move count: %d" % board.legal_moves.count())
if avoid:
    print("AVOID: " + " ".join(sorted(set(avoid))))
