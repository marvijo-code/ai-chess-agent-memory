import json, sys, chess
payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
mine = board.turn
opp = not mine
clocks = payload.get("clocks", {})
you = clocks.get("you_ms", 0)
if you and you < 180000:
    print(f"low time {int(you//1000)}s use 5-10s waits only")
else:
    print("clock shell 5-10s routine 10-20s")
out_sq = chess.F4 if mine == chess.WHITE else chess.F5
p = board.piece_at(out_sq)
if p and p.color == opp and p.piece_type == chess.KNIGHT:
    print(f"opp N on {chess.square_name(out_sq)} guarded kick g3 only after Qe3 holds f3")
else:
    print(f"no opp N on {chess.square_name(out_sq)}")
chain = (chess.E4, chess.D5, chess.C4) if mine == chess.WHITE else (chess.E5, chess.D5, chess.C5)
bad = []
for move in board.legal_moves:
    board.push(move)
    for sq in chain:
        q = board.piece_at(sq)
        if q and q.color == mine and board.attackers(opp, sq) and not board.attackers(mine, sq):
            bad.append(move.uci())
            break
    board.pop()
if bad:
    print(f"chain loose after {len(bad)} moves e.g. {' '.join(sorted(set(bad))[:3])}")
    print("AVOID: " + " ".join(sorted(set(bad))))
else:
    print("e-chain held no loose e4/d5/c4")
