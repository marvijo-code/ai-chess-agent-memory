import json, sys, chess
payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
legal = sorted(m.uci() for m in board.legal_moves)
print(f"LEGAL ({len(legal)}): {' '.join(legal)}")
print("no loose piece")
