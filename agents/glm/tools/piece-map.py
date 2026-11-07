import json, sys, chess
p = json.load(sys.stdin)
b = chess.Board(p["fen"])
mine = b.turn
val = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}
mat = {chess.WHITE: 0, chess.BLACK: 0}
for c in (chess.WHITE, chess.BLACK):
    for pt in val:
        mat[c] += val[pt] * len(b.pieces(pt, c))
mename = "WHITE" if mine == chess.WHITE else "BLACK"
wk = b.king(chess.WHITE)
bk = b.king(chess.BLACK)
print("TO MOVE: %s | YOUR king: %s | his king: %s | material W%d v B%d | legal moves: %d" % (
    mename,
    chess.square_name(wk) if wk is not None else "-",
    chess.square_name(bk) if bk is not None else "-",
    mat[chess.WHITE], mat[chess.BLACK], b.legal_moves.count()))
mineparts = [b.piece_at(s).symbol() + chess.square_name(s) for s in chess.SQUARES
             if b.piece_at(s) and b.piece_at(s).color == mine]
hisparts = [b.piece_at(s).symbol() + chess.square_name(s) for s in chess.SQUARES
            if b.piece_at(s) and b.piece_at(s).color != mine]
print("MY pieces: " + " ".join(mineparts))
print("HIS pieces: " + " ".join(hisparts))
print("Pick every king/rook/queen keeper FROM this map - no remembered squares.")