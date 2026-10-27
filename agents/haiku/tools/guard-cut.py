import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload['fen'])
mine = board.turn
enemy = not mine


def state(b):
    info = {}
    for sq, piece in b.piece_map().items():
        if piece.color == mine and piece.piece_type != chess.KING:
            info[sq] = (len(b.attackers(enemy, sq)), len(b.attackers(mine, sq)))
    return info


before = state(board)
cuts = []
for move in list(board.legal_moves):
    san = board.san(move)
    board.push(move)
    after = state(board)
    board.pop()
    lost = []
    for sq in before:
        if sq in (move.from_square, move.to_square) or sq not in after:
            continue
        _, def_before = before[sq]
        att_after, def_after = after[sq]
        if def_before > 0 and def_after == 0 and att_after > 0:
            lost.append(chess.square_name(sq))
    if lost:
        cuts.append((move.uci(), san, ', '.join(lost)))

if cuts:
    for uci, san, where in cuts:
        print(f'{san} leaves your last guard gone from {where}, which his piece attacks')
    print('AVOID: ' + ' '.join(sorted(set(uci for uci, _, _ in cuts))))
else:
    print('no move cuts the last guard of an attacked piece of yours')
