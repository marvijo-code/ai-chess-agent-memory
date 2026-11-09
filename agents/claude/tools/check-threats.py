import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
me = board.turn


def has_mate1(b):
    for m in list(b.legal_moves):
        b.push(m)
        r = b.is_checkmate()
        b.pop()
        if r:
            return m
    return None


def forced_mate2(b):
    # b: opponent to move. Returns (first check, mate reply) if every defence loses.
    for chk in list(b.legal_moves):
        if not b.gives_check(chk):
            continue
        b.push(chk)
        replies = list(b.legal_moves)
        ok = bool(replies)
        last = None
        for r in replies:
            b.push(r)
            mm = has_mate1(b)
            b.pop()
            if mm is None:
                ok = False
                break
            last = mm
        b.pop()
        if ok:
            return chk, last
    return None


found = False
for move in list(board.legal_moves):
    san = board.san(move)
    board.push(move)
    if board.is_checkmate():
        board.pop()
        continue
    m1 = has_mate1(board)
    if m1 is not None:
        found = True
        print(f"AVOID: {move.uci()} - {san} allows mate in 1 by {board.san(m1)}")
    else:
        r = forced_mate2(board)
        if r:
            found = True
            print(f"AVOID: {move.uci()} - {san} allows forced mate in 2: {board.san(r[0])} then mate")
    board.pop()
if not found:
    print("no mate in 1 or forced check-mate in 2 after any of my moves")
