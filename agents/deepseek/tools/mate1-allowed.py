import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
bad = []
safe = 0
for move in board.legal_moves:
    board.push(move)
    mated = False
    for reply in board.legal_moves:
        if not board.gives_check(reply):
            continue
        board.push(reply)
        if board.is_checkmate():
            mated = True
        board.pop()
        if mated:
            break
    board.pop()
    if mated:
        bad.append(move.uci())
    else:
        safe += 1
if bad and safe > 0:
    print("these moves allow a mate in 1 (check first, then mate): " + " ".join(sorted(bad)))
    print("AVOID: " + " ".join(sorted(bad)))
elif bad:
    print("every legal move here allows a mate in 1 - position already lost, play the most stubborn move")
else:
    print("no mate in 1 allowed")
