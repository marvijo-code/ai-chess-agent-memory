import json, sys, chess
payload = json.load(sys.stdin)
board = chess.Board(payload['fen'])
mine = board.turn
opp = not mine
free_moves = []
free_sans = {}
for move in list(board.legal_moves):
    if not board.is_capture(move):
        continue
    san = board.san(move)
    to_sq = move.to_square
    board.push(move)
    if board.is_attacked_by(opp, to_sq):
        board.pop()
        continue
    loose = False
    for sq in chess.SQUARES:
        p = board.piece_at(sq)
        if p and p.color == mine and p.piece_type != chess.KING and sq != to_sq:
            if board.is_attacked_by(opp, sq) and not board.is_attacked_by(mine, sq):
                loose = True
                break
    board.pop()
    if not loose:
        free_moves.append(move)
        free_sans[move.uci()] = san
if free_moves:
    for m in free_moves:
        print(f'free capture {free_sans[m.uci()]} wins material and stays safe')
    all_uci = [m.uci() for m in board.legal_moves]
    free_uci = set([m.uci() for m in free_moves])
    avoid = sorted([u for u in all_uci if u not in free_uci])
    print('AVOID: ' + ' '.join(avoid))
else:
    print('no free capture')
