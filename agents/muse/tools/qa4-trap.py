import json, sys, chess
payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
mine = board.turn
bad = set()
for move in list(board.legal_moves):
    try:
        san = board.san(move)
    except:
        san = move.uci()
    board.push(move)
    my_queens = []
    for sq in chess.SQUARES:
        pc = board.piece_at(sq)
        if pc is not None and pc.color == mine and pc.piece_type == chess.QUEEN:
            my_queens.append(sq)
    flagged = False
    for om in list(board.legal_moves):
        opc = board.piece_at(om.from_square)
        if opc is None or opc.color == mine:
            continue
        if opc.piece_type == chess.QUEEN and chess.square_name(om.to_square) == "a4" and board.gives_check(om):
            try:
                osan = board.san(om)
            except:
                osan = om.uci()
            print(f"{san} allows {osan} Qa4+ check on king")
            bad.add(move.uci())
            flagged = True
            break
        if opc.piece_type == chess.KNIGHT:
            dest = om.to_square
            df_file = chess.square_file(dest)
            df_rank = chess.square_rank(dest)
            for q in my_queens:
                df = abs(df_file - chess.square_file(q))
                dr = abs(df_rank - chess.square_rank(q))
                if (df == 1 and dr == 2) or (df == 2 and dr == 1):
                    print(f"{san} allows N-{chess.square_name(dest)} forking Q on {chess.square_name(q)}")
                    bad.add(move.uci())
                    flagged = True
                    break
            if flagged:
                break
    board.pop()
if bad:
    print("AVOID: " + " ".join(sorted(bad)))
else:
    print("no Qa4/Nc6 queen hit")
