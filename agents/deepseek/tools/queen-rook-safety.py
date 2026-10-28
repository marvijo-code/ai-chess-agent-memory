import json, sys, chess
payload = json.load(sys.stdin)
board = chess.Board(payload['fen'])
mine = board.turn
bad = []
for move in board.legal_moves:
    piece = board.piece_at(move.from_square)
    if piece is None or piece.piece_type not in (chess.QUEEN, chess.ROOK):
        continue
    captured = board.piece_at(move.to_square)
    if captured is not None and captured.piece_type == chess.QUEEN:
        continue
    san = board.san(move)
    board.push(move)
    if board.is_checkmate():
        board.pop()
        continue
    dest = move.to_square
    pawns = board.attackers(not mine, dest) & board.pieces(chess.PAWN, not mine)
    knights = board.attackers(not mine, dest) & board.pieces(chess.KNIGHT, not mine)
    reasons = []
    if pawns:
        reasons.append('pawn')
    if knights:
        reasons.append('knight')
    if reasons:
        reason = '/'.join(reasons)
        bad.append(move.uci())
        print(f'{san} puts your {piece.symbol()} on a {reason}-attacked square')
    board.pop()
if bad:
    print('AVOID: ' + ' '.join(sorted(set(bad))))
else:
    print('no queen/rook move onto a pawn/knight attack square')
