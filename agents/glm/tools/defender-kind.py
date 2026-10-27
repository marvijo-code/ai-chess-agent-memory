import json, sys, chess

VAL = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}
NAME = {chess.PAWN: 'pawn', chess.KNIGHT: 'knight', chess.BISHOP: 'bishop',
        chess.ROOK: 'rook', chess.QUEEN: 'queen', chess.KING: 'king'}

payload = json.load(sys.stdin)
board = chess.Board(payload['fen'])
me = chess.WHITE if payload.get('side_to_move', 'white') == 'white' else chess.BLACK
avoid = set()
lines = 0

for mv in list(board.legal_moves):
    mover = board.piece_type_at(mv.from_square)
    tgt = board.piece_type_at(mv.to_square)
    san = board.san(mv)
    flag = False
    if tgt is not None and mover in VAL and VAL[mover] > VAL[tgt]:
        # capture of a cheaper unit: is there a recapturer?
        board.push(mv)
        them = board.turn
        us = not them
        land = board.attackers(them, mv.to_square)
        konly = land and all(board.piece_at(a).piece_type == chess.KING for a in land)
        if land and not (konly and board.attackers(us, mv.to_square)):
            flag = True
            avoid.add(mv.uci())
            if lines < 8:
                print(f'{san}: {NAME[mover]} takes {NAME[tgt]} on {chess.square_name(mv.to_square)} but the square is recapturable -> loses material')
                lines += 1
        board.pop()
    else:
        # rule: my piece guarded only by pawns while an enemy pawn attacks it -> piece for pawn
        board.push(mv)
        them = board.turn
        us = not them
        for sq in chess.SQUARES:
            p = board.piece_at(sq)
            if not p or p.color != us or p.piece_type == chess.KING:
                continue
            atk = board.attackers(them, sq)
            if not atk:
                continue
            dguards = board.attackers(us, sq)
            dtypes = set(board.piece_at(d).piece_type for d in dguards)
            if any(t != chess.PAWN for t in dtypes):
                continue
            if any(board.piece_at(a).piece_type == chess.PAWN for a in atk):
                if lines < 8:
                    print(f'{san}: leaves my {NAME[p.piece_type]} on {chess.square_name(sq)} guarded only by pawns while an enemy pawn attacks it (a pawn recaptures only a pawn -> piece for pawn)')
                    lines += 1
                break
        board.pop()

if not lines:
    print('no findings')
print('AVOID: ' + ' '.join(sorted(avoid)))
