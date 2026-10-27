import json, sys, chess

V = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 99}


def threats(b, color):
    out = {}
    for sq in chess.SQUARES:
        p = b.piece_at(sq)
        if not p or p.color != color or p.piece_type == chess.KING:
            continue
        att = b.attackers(not color, sq)
        if not att:
            continue
        dfn = b.attackers(color, sq)
        low = min(V[b.piece_at(a).piece_type] for a in att)
        if (not dfn) or low < V[p.piece_type]:
            out[sq] = p
    return out


def main():
    payload = json.load(sys.stdin)
    board = chess.Board(payload["fen"])
    me = board.turn
    before = threats(board, me)
    bad = []
    notes = []
    pawn_notes = []
    for move in list(board.legal_moves):
        san = board.san(move)
        gain = 0
        if board.is_en_passant(move):
            gain = 1
        else:
            cp = board.piece_at(move.to_square)
            if cp:
                gain = V[cp.piece_type]
        board.push(move)
        mate = False
        for r in list(board.legal_moves):
            board.push(r)
            if board.is_checkmate():
                mate = True
            board.pop()
            if mate:
                break
        after = threats(board, me)
        flagged = []
        newpawns = []
        for sq, p in after.items():
            moved = (sq == move.to_square)
            was = before.get(sq)
            if was is not None and was.piece_type == p.piece_type and not moved:
                continue
            if p.piece_type == chess.PAWN:
                if not moved:
                    newpawns.append(chess.square_name(sq))
                continue
            loss = V[p.piece_type]
            if moved and loss <= gain:
                continue
            flagged.append(p.symbol().upper() + chess.square_name(sq))
        board.pop()
        if mate:
            bad.append(move.uci())
            notes.append(san + " allows mate in 1")
        elif flagged:
            bad.append(move.uci())
            notes.append(san + " leaves loose/under-guarded: " + ",".join(flagged))
        if newpawns:
            pawn_notes.append(san + ":" + ",".join(newpawns))
    for n in notes[:6]:
        print(n)
    if pawn_notes:
        print("new loose pawns after (info): " + "; ".join(pawn_notes[:5]))
    if not notes:
        print("no new loose piece and no opponent mate in 1 after any move (pins not modelled)")
    print("AVOID: " + " ".join(sorted(set(bad))))


main()
