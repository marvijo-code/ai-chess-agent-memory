import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload['fen'])
me = board.turn
them = not me
out = []
avoid = []

for f in range(8):
    for r in range(8):
        sq = chess.square(f, r)
        pc = board.piece_at(sq)
        if pc is None or pc.color != me or pc.piece_type != chess.PAWN:
            continue
        d = 8 if me == chess.WHITE else -8
        one = sq + d
        if not (0 <= one < 64):
            continue
        name1 = chess.square_name(one)
        block = board.piece_at(one)
        if block is not None:
            who = 'OWN' if block.color == me else 'HIS'
            out.append('push ' + chess.square_name(sq) + name1 + ' BLOCKED by ' + who + ' ' + block.symbol() + ' on ' + name1)
            continue
        move = chess.Move(sq, one)
        if move in board.legal_moves:
            board.push(move)
            cap = [a for a in board.attackers(them, one) if board.piece_type_at(a) == chess.PAWN]
            guards = board.attackers(me, one)
            board.pop()
            if cap and not guards:
                out.append('push ' + chess.square_name(sq) + name1 + ' HANGS: his pawn on ' + chess.square_name(cap[0]) + ' takes it, zero defenders')
                avoid.append(move.uci())
        if chess.square_rank(sq) == (1 if me == chess.WHITE else 6):
            two = sq + 2 * d
            if 0 <= two < 64:
                name2 = chess.square_name(two)
                block2 = board.piece_at(two)
                if block2 is not None:
                    who2 = 'OWN' if block2.color == me else 'HIS'
                    out.append('two-step ' + chess.square_name(sq) + name2 + ' BLOCKED by ' + who2 + ' ' + block2.symbol() + ' on ' + name1 + '/' + name2)
                else:
                    move2 = chess.Move(sq, two)
                    if move2 in board.legal_moves:
                        board.push(move2)
                        cap2 = [a for a in board.attackers(them, two) if board.piece_type_at(a) == chess.PAWN]
                        guard2 = board.attackers(me, two)
                        board.pop()
                        note = 'two-step ' + chess.square_name(sq) + name2 + ' open'
                        if cap2 and not guard2:
                            note += ' but HANGS to his pawn on ' + chess.square_name(cap2[0]) + ' (zero defenders)'
                            avoid.append(move2.uci())
                        out.append(note)

print(' | '.join(out) if out else 'no pawn pushes available')
if avoid:
    print('AVOID: ' + ' '.join(avoid))
