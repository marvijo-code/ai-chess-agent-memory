import json
import sys
from collections import Counter

import chess


def poskey(board):
    """Position identity: pieces, side to move, castling rights, en-passant."""
    parts = board.fen().split()
    return " ".join(parts[:4])


def main():
    payload = json.load(sys.stdin)
    fen = payload.get("fen") or chess.STARTING_FEN
    moves = [m for m in (payload.get("moves") or []) if isinstance(m, str)]
    cur = chess.Board(fen)

    replay = chess.Board(chess.STARTING_FEN)
    counts = Counter([poskey(replay)])
    bad = ""
    for i, uci in enumerate(moves):
        try:
            replay.push_uci(uci)
        except Exception:
            bad = f"history unusable at move {i + 1} ('{uci}'); counts partial"
            break
        counts[poskey(replay)] += 1
    if bad:
        print(bad)
    if poskey(replay) != poskey(cur) and not bad:
        print("note: replayed position differs from the given fen")

    vals = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3,
            chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}
    mine = his = 0
    for sq in chess.SQUARES:
        p = cur.piece_at(sq)
        if p is None or p.piece_type == chess.KING:
            continue
        if p.color == cur.turn:
            mine += vals[p.piece_type]
        else:
            his += vals[p.piece_type]
    diff = mine - his
    if diff >= 5:
        print(f"mover is up {diff}; a threefold NOW = lost win, walking into rep = disaster; treat 'even'don't' = low value")
    else:
        print(f"mover material balance {diff:+d}; repetition here is a real option for{'the mover' if diff <= 0 else 'defender side'}")

    third = []
    second = []
    for move in cur.legal_moves:
        cur.push(move)
        before = counts.get(poskey(cur), 0)
        cur.pop()
        if before >= 2:
            third.append(move.uci())
        elif before == 1:
            second.append(move.uci())
    if third:
        print("3RD occurrence right now (opponent can claim a draw): " + " ".join(third))
    if second:
        print("2ND occurrence now (one more later = threefold; track these): " + " ".join(second))
    if not third and not second:
        print("no move this ply creates a 2nd or 3rd repetition")
    if third and diff >= 5:
        print("AVOID: " + " ".join(sorted(set(third))))
    elif not third:
        print("AVOID: none")


main()
