import json, sys, chess
p = json.load(sys.stdin)
board = chess.Board(p["fen"])
mine = board.turn
found = False
for m in list(board.legal_moves):
    if not board.is_capture(m):
        continue
    board.push(m)
    sq = m.to_square
    attackers = board.attackers(not mine, sq)
    if attackers:
        names = " ".join(board.piece_at(a).symbol() + chess.square_name(a) for a in attackers if board.piece_at(a))
        recaps = [r for r in board.legal_moves if r.to_square == sq]
        if recaps:
            print(f"{m.uci()}: recaptured by {names}; you have {len(recaps)} legal recapture(s) - full chain, not a gift")
        else:
            print(f"{m.uci()}: recaptured by {names}; NO legal recapture for you - free for him")
            found = True
    board.pop()
if not found:
    print("no unguarded capture found")