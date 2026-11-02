import json, sys, chess
payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
mine = board.turn
found = False
for move in board.legal_moves:
    san = board.san(move)
    board.push(move)
    for sq in chess.SQUARES:
        p = board.piece_at(sq)
        if p and p.color == mine and p.piece_type == chess.ROOK:
            if board.is_attacked_by(not mine, sq) and not board.is_attacked_by(mine, sq):
                print(f"AVOID: {move.uci()} - {san} leaves your rook on {chess.square_name(sq)} loose")
                found = True
                break
    board.pop()
if not found:
    print("no rook left loose")
