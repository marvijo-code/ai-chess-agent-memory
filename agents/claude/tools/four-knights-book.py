import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
W, B = chess.WHITE, chess.BLACK


def has(sq, pt, color):
    p = board.piece_at(chess.parse_square(sq))
    return bool(p) and p.piece_type == pt and p.color == color


base = (board.turn == B and has("b5", chess.BISHOP, W) and has("b4", chess.BISHOP, B)
        and has("c6", chess.KNIGHT, B) and has("f6", chess.KNIGHT, B)
        and has("c3", chess.KNIGHT, W) is not None)
if board.turn == B and has("d5", chess.KNIGHT, W) and has("b5", chess.BISHOP, W) \
        and has("b4", chess.BISHOP, B) and has("c6", chess.KNIGHT, B) \
        and has("f6", chess.KNIGHT, B) and has("e4", chess.PAWN, W):
    print("BOOK: f6d5 (Nxd5, then exd5 e4). Play it; my note says Nxd5 ONLY.")
    print("AVOID: f6e4 - 5...Nxe4? 6.Qe2 hits Ne4, Bxc6 then Nxb4 wins the b4 bishop: a piece lost (SF +6.5 by move 8).")
elif board.turn == B and has("b5", chess.BISHOP, W) and has("b4", chess.BISHOP, B) \
        and has("c6", chess.KNIGHT, B) and has("f6", chess.KNIGHT, B) \
        and has("c3", chess.KNIGHT, W) and has("g1", chess.KING, W) \
        and not has("g8", chess.KING, B):
    print("BOOK: e8g8 (5.O-O O-O). Then 6.Nd5 Nxd5 7.exd5 e4.")
else:
    print("four-knights-book: not a Four Knights book position")
