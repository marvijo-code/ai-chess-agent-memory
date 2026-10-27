import json, sys, chess

p = json.load(sys.stdin)
board = chess.Board(p["fen"])

avoid = []
for move in list(board.legal_moves):
    san_mv = board.san(move)
    board.push(move)
    finds = []
    replies = [r for r in board.legal_moves if board.gives_check(r)]
    for reply in replies:
        san_r = board.san(reply)
        board.push(reply)
        if board.is_checkmate():
            finds.append(san_r)
        board.pop()
    board.pop()
    if finds:
        avoid.append(move.uci())
        print(f"{san_mv} ({move.uci()}) allows opponent mate-in-1: {', '.join(finds[:4])}")

if avoid:
    print("AVOID: " + " ".join(avoid))
else:
    print("no move of mine allows an opponent mate-in-1")
