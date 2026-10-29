import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])

def mate_in_1():
    for m in list(board.legal_moves):
        board.push(m)
        ok = board.is_checkmate()
        board.pop()
        if ok:
            return board.san(m)
    return None

def all_replies_get_mated():
    for r in list(board.legal_moves):
        board.push(r)
        still = mate_in_1() is not None
        board.pop()
        if not still:
            return False
    return True

flags = []
n_moves = 0
for mv in list(board.legal_moves):
    san = board.san(mv)
    board.push(mv)
    m1 = mate_in_1()
    if m1 is not None:
        print(san + " (" + mv.uci() + "): he mates in 1 with " + m1)
        flags.append(mv.uci())
    else:
        for om in list(board.legal_moves):
            board.push(om)
            forced = board.is_check() and all_replies_get_mated()
            if forced:
                print(san + " (" + mv.uci() + "): his check " + board.san(om) + " mates after every reply")
                flags.append(mv.uci())
            board.pop()
            if forced:
                break
    board.pop()
    n_moves += 1

if flags:
    print("AVOID: " + " ".join(sorted(set(flags))))
else:
    print("no forced mate in 2 plies found (" + str(n_moves) + " moves checked)")