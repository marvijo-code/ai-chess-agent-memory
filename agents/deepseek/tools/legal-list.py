import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])

moves = sorted(m.uci() for m in board.legal_moves)
print("%d legal moves for %s: %s" % (len(moves), "white" if board.turn else "black", " ".join(moves)))

if board.is_check():
    king_sq = board.king(board.turn)
    flights = sorted(m.uci() for m in board.legal_moves if board.piece_at(m.from_square) and board.piece_at(m.from_square).piece_type == chess.KING)
    print("IN CHECK: king on %s; legal king moves: %s" % (chess.square_name(king_sq), " ".join(flights) if flights else "none"))

print("Send only a UCI from the list above; after one rejection pick a different piece AND idea.")
