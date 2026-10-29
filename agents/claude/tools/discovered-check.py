import json, sys, chess

VAL = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}


def disc_replies(board):
    # board: side to move is the one who wants to give a discovered check
    res = []
    for r in list(board.legal_moves):
        if not board.gives_check(r):
            continue
        board.push(r)
        ch = list(board.checkers())
        board.pop()
        if any(sq != r.to_square for sq in ch):
            res.append(r)
    return res


def hanging(board, color):
    # my pieces (value>=3) attacked by the enemy and unguarded or hit by a cheaper piece
    out = []
    for sq, p in board.piece_map().items():
        if p.color != color or p.piece_type == chess.KING or p.piece_type == chess.PAWN:
            continue
        atk = board.attackers(not color, sq)
        if not atk:
            continue
        guarded = bool(board.attackers(color, sq))
        cheaper = any(VAL.get(board.piece_at(a).piece_type, 99) < VAL[p.piece_type] for a in atk)
        if (not guarded) or cheaper:
            out.append(chess.square_name(sq))
    return out


def main():
    payload = json.load(sys.stdin)
    board = chess.Board(payload["fen"])
    me = board.turn
    bad = []
    # current resources of the opponent
    if not board.is_check():
        b2 = board.copy()
        b2.push(chess.Move.null())
        d0 = disc_replies(b2)
        if d0:
            print("He has discovered-check moves now: " + " ".join(m.uci() for m in d0[:6]))
    for m in list(board.legal_moves):
        san = board.san(m)
        board.push(m)
        if board.is_checkmate():
            board.pop()
            continue
        d = disc_replies(board)
        h = hanging(board, me)
        if d and h:
            bad.append(m.uci())
            print(f"{san} allows discovered check {d[0].uci()} while my {','.join(h)} hangs")
        board.pop()
    if bad:
        print("AVOID: " + " ".join(sorted(set(bad))))
    else:
        print("no move allows a discovered check while a piece of mine hangs (verified 2-ply)")


main()
