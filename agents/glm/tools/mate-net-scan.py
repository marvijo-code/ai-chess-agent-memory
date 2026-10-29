import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
side = payload["side_to_move"]

def mating_move():
    for mv in list(board.legal_moves):
        if not board.gives_check(mv):
            continue
        board.push(mv)
        is_mate = board.is_checkmate()
        board.pop()
        if is_mate:
            return mv
    return None

def forced_net_after(my_move):
    # pushed already: opponent to move. True if opponent has a check such that
    # EVERY legal reply of mine lets opponent mate in one.
    checks = [r for r in list(board.legal_moves) if board.gives_check(r)][:12]
    for r in checks:
        board.push(r)
        dead = True
        for s in list(board.legal_moves):
            board.push(s)
            if mating_move() is None:
                dead = False
                board.pop()
                break
            board.pop()
        board.pop()
        if dead:
            return r
    return None

bad = []
own_mate = mating_move()
for move in list(board.legal_moves):
    san = board.san(move)
    board.push(move)
    if mating_move() is not None:
        bad.append(san)
        board.pop()
        continue
    if forced_net_after(move) is not None:
        bad.append(san)
    board.pop()

if own_mate is not None:
    print("YOU HAVE MATE IN 1: " + board.san(own_mate))
if bad:
    for san in bad:
        print(f"{san}: hands him a forced mate net (uncapturable/unblockable check, then mate next move whatever I play)")
    print("AVOID: " + " ".join(m.uci() for m in board.legal_moves if board.san(m) in set(bad)))
else:
    if own_mate is None:
        print("no mate in 1 found, no forced mate net within 3 plies checked")
