import json, sys, chess
payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
mine = board.turn
target = chess.F2 if mine == chess.WHITE else chess.F7
home = chess.G1 if mine == chess.WHITE else chess.G8
rook_home = chess.F1 if mine == chess.WHITE else chess.F8
king = board.piece_at(home)
if not king or king.piece_type != chess.KING or king.color != mine:
    print("king not tucked short, no Rxf2 pattern")
else:
    foe = not mine
    has_f_rook = any(board.piece_at(sq) and board.piece_at(sq).piece_type == chess.ROOK and board.piece_at(sq).color == foe for sq in chess.SQUARES if chess.square_file(sq) == 5)
    bad = []
    for move in board.legal_moves:
        san = board.san(move)
        is_f_block = move.to_square == target
        is_f_abandon = move.from_square == rook_home
        if not (is_f_block or is_f_abandon):
            continue
        board.push(move)
        atk = len(board.attackers(foe, target))
        defe = len(board.attackers(mine, target))
        foe_rook_still = any(board.piece_at(sq) and board.piece_at(sq).piece_type == chess.ROOK and board.piece_at(sq).color == foe for sq in chess.SQUARES if chess.square_file(sq) == 5)
        if has_f_rook and foe_rook_still and atk > 0 and atk >= defe:
            bad.append(san)
            print(f"{san} leaves f-square loose vs rook on f-file")
        board.pop()
    if bad:
        print("AVOID: " + " ".join(sorted(set(bad))))
    else:
        print("no f2 weakness")
