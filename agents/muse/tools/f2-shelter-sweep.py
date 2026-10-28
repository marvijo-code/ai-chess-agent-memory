import json, sys, chess
payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
mine = board.turn
shelter = [chess.F1, chess.F2, chess.G2, chess.H2] if mine == chess.WHITE else [chess.F8, chess.F7, chess.G7, chess.H7]
bad = []
for move in list(board.legal_moves):
    u = move.uci()
    board.push(move)
    to_sq = move.to_square
    if to_sq in shelter:
        p = board.piece_at(to_sq)
        if p and p.color == mine and p.piece_type != chess.KING:
            na = len(list(board.attackers(not mine, to_sq)))
            nd = len(list(board.attackers(mine, to_sq)))
            if na > 0 and nd <= na:
                bad.append(u)
                print(f"{u} lands {p.symbol()} on {chess.square_name(to_sq)} with {na} attackers vs {nd} defenders - Rxf2/Qh2 idea")
    board.pop()
if bad:
    print("AVOID: " + " ".join(sorted(set(bad))))
else:
    print("no shelter break on f/g/h")
