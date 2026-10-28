import json, sys, chess
payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
mine = board.turn
bad = []
for move in list(board.legal_moves):
    board.push(move)
    found = None
    for sq in chess.SQUARES:
        p = board.piece_at(sq)
        if p and p.color == mine and p.piece_type != chess.KING:
            if board.attackers(not mine, sq) and not board.attackers(mine, sq):
                found = (sq, p.symbol())
                break
    if found:
        sq, sym = found
        bad.append(move.uci())
        print(f"{move.uci()} leaves {sym} on {chess.square_name(sq)} loose")
    board.pop()
if bad:
    print("AVOID: " + " ".join(sorted(set(bad))))
else:
    print("no loose piece")
