import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
mine = board.turn
VAL = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}
KN = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


def jumps(square):
    f, r = chess.square_file(square), chess.square_rank(square)
    out = []
    for df, dr in KN:
        nf, nr = f + df, r + dr
        if 0 <= nf < 8 and 0 <= nr < 8:
            out.append(chess.square(nf, nr))
    return out


bad = []
for move in board.legal_moves:
    board.push(move)
    findings = []
    if not (board.is_checkmate() or board.is_stalemate()):
        for sq in chess.SQUARES:
            piece = board.piece_at(sq)
            if not piece or piece.color == mine or piece.piece_type != chess.KNIGHT:
                continue
            for dest in jumps(sq):
                occ = board.piece_at(dest)
                if occ and occ.color != mine:
                    continue
                if board.attackers(mine, dest):
                    continue
                king_hit = False
                loose = []
                for t in jumps(dest):
                    tp = board.piece_at(t)
                    if not tp or tp.color != mine:
                        continue
                    if tp.piece_type == chess.KING:
                        king_hit = True
                    elif not board.attackers(mine, t):
                        loose.append(VAL[tp.piece_type])
                if (king_hit and loose) or len(loose) >= 2 or any(v >= 5 for v in loose):
                    findings.append(chess.square_name(dest))
    board.pop()
    if findings:
        bad.append(move.uci())
        print(move.uci() + " lets his knight land free on " + " ".join(sorted(set(findings))) + " forking my units")

if bad:
    print("AVOID: " + " ".join(sorted(set(bad))))
else:
    print("no free knight-fork square after any legal move")
