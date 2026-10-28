import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
legal = list(board.legal_moves)
head = "IN CHECK. " if board.is_check() else ""
king = [m.uci() for m in legal if board.piece_type_at(m.from_square) == chess.KING]
print(head + str(len(legal)) + " legal moves. KING moves: " + (" ".join(king) if king else "none"))
others = [m.uci() for m in legal if board.piece_type_at(m.from_square) != chess.KING]
if others:
    print("Other legal UCI: " + " ".join(others))
bad = []
for m in legal:
    board.push(m)
    if board.is_stalemate():
        print(board.san(m) if False else m.uci() + " stalemates the opponent (only fine if I am worse)")
    mated = False
    for r in list(board.legal_moves):
        board.push(r)
        if board.is_checkmate():
            mated = True
        board.pop()
        if mated:
            break
    board.pop()
    if mated:
        bad.append(m.uci())
if bad:
    print("These moves allow mate in 1: " + " ".join(bad))
    if len(bad) < len(legal):
        print("AVOID: " + " ".join(bad))
else:
    print("no move allows mate in 1")
