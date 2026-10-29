import json, sys, chess

VAL = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}

payload = json.load(sys.stdin)
board = chess.Board(payload['fen'])
mine = board.turn
opp = not mine
bad = []
for move in board.legal_moves:
    san = board.san(move)
    board.push(move)
    if board.is_check():
        board.pop()
        continue
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if piece is None or piece.color != mine or piece.piece_type == chess.KING:
            continue
        attackers = board.attackers(opp, sq)
        if not attackers:
            continue
        cheapest = min(VAL[board.piece_type_at(a)] for a in attackers)
        guards = [g for g in board.attackers(mine, sq) if board.piece_type_at(g) != chess.KING]
        if not guards and VAL[piece.piece_type] > cheapest:
            print(f"{san} leaves your {piece.symbol()} on {chess.square_name(sq)}: a cheaper piece hits it and only your king could recapture - he sacs and trades down")
            bad.append(move.uci())
    board.pop()
if bad:
    print('AVOID: ' + ' '.join(sorted(set(bad))))
else:
    print('no king-only-guard sac risk found')