import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload['fen'])
mine = board.turn

if board.is_check():
    replies = list(board.legal_moves)
    print('IN CHECK: %d legal replies: %s' % (len(replies), ' '.join(m.uci() for m in replies)))
    if len(replies) == 1:
        print('FORCED: %s is the sole legal reply. If a refusal cites a DIFFERENT move that citation is a ghost - resend this move once (accepted 10x in T73R5). NEVER resend when 2+ replies exist.' % replies[0].uci())
    sys.exit(0)

loose_before = set()
for sq in chess.SQUARES:
    pc = board.piece_at(sq)
    if pc and pc.color == mine and pc.piece_type == chess.PAWN:
        if board.attackers(not mine, sq) and not board.attackers(mine, sq):
            loose_before.add(sq)

bad = set()
for move in list(board.legal_moves):
    board.push(move)
    for sq in chess.SQUARES:
        if sq in loose_before:
            continue
        pc = board.piece_at(sq)
        if pc and pc.color == mine and pc.piece_type == chess.PAWN:
            if board.attackers(not mine, sq) and not board.attackers(mine, sq):
                bad.add(move.uci())
                print('%s leaves my pawn on %s newly capturable' % (move.uci(), chess.square_name(sq)))
                break
    board.pop()

if bad:
    print('AVOID: ' + ' '.join(sorted(bad)))
else:
    print('no newly loose pawns; when in check this tool lists all legal replies')
