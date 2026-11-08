import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
me = board.turn
avoids = []
mates = []
legal = []
for move in list(board.legal_moves):
    uci = move.uci()
    legal.append(uci)
    board.push(move)
    if board.is_checkmate():
        mates.append(uci)
        board.pop()
        continue
    mated = False
    ep_lost = False
    for reply in list(board.legal_moves):
        board.push(reply)
        if board.is_checkmate():
            mated = True
        board.pop()
        if mated:
            break
    if mated:
        avoids.append(f"AVOID: {uci} - allows a mate in 1 reply")
    if board.has_legal_en_passant():
        for reply in list(board.legal_moves):
            if board.is_en_passant(reply):
                target = reply.to_square
                board.push(reply)
                if not board.attackers(me, target):
                    ep_lost = True
                board.pop()
                if ep_lost:
                    break
    if ep_lost:
        avoids.append(f"AVOID: {uci} - double step lets his pawn capture en passant and I cannot recapture, losing a pawn")
    board.pop()
if mates:
    print("MATE IN 1: " + " ".join(mates))
for line in avoids[:6]:
    print(line)
if board.is_check():
    print("IN CHECK, legal: " + " ".join(legal))
elif not mates and not avoids:
    print("no mate-in-1 or en passant loss found among " + str(len(legal)) + " legal moves")
