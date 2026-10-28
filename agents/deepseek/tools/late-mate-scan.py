import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
mine = board.turn
bad = []
for move in board.legal_moves:
    board.push(move)
    if board.is_game_over():
        board.pop()
        continue
    mates = []
    for reply in board.legal_moves:
        uci = reply.uci()
        board.push(reply)
        if board.is_checkmate():
            mates.append(uci)
        board.pop()
    board.pop()
    if mates:
        bad.append(move.uci())
        print(move.uci() + " allows mate in 1: " + ", ".join(sorted(mates)[:3]))
if bad:
    print("AVOID: " + " ".join(sorted(set(bad))))
else:
    print("no mate in 1 after any of my moves")
