import json, sys, chess
payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
mine = board.turn
opp = not mine
bad = []
notes = []
for my_move in list(board.legal_moves):
    board.push(my_move)
    to_sq = my_move.to_square
    found = False
    for oq in list(board.legal_moves):
        p = board.piece_at(oq.from_square)
        if p is None or p.piece_type != chess.QUEEN or p.color != board.turn:
            continue
        cap = (oq.to_square == to_sq)
        board.push(oq)
        chk = board.is_check()
        if chk and (cap or board.is_attacked_by(opp, to_sq)):
            if not board.is_attacked_by(mine, to_sq) or cap:
                found = True
                board.pop()
                break
        board.pop()
    board.pop()
    if found:
        bad.append(my_move.uci())
        notes.append(f"{my_move.uci()} allows queen check winning {chess.square_name(to_sq)}")
for n in notes[:3]:
    print(n)
if bad:
    print("AVOID: " + " ".join(sorted(set(bad))))
else:
    print("no qa4 queen-check trap")
