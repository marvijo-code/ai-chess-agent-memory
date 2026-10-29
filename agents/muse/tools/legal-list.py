import json, sys, chess
payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
moves = sorted(m.uci() for m in board.legal_moves)
print(f"legal {len(moves)}: {' '.join(moves)}")
if board.is_check():
    print("in check: must move king, capture checker or block")
    kings = sorted(m.uci() for m in board.legal_moves if board.piece_at(m.from_square) and board.piece_at(m.from_square).piece_type == chess.KING)
    print(f"king moves: {' '.join(kings) if kings else 'none'}")
else:
    print("not in check")
print("verify from-square piece, path, own blockers before sending")
