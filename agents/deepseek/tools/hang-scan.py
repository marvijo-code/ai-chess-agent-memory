import json
import sys

import chess

VAL = {chess.PAWN: 100, chess.KNIGHT: 320, chess.BISHOP: 330,
       chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 20000}


def see_reply(board, sq, depth):
    """Best net gain for the side to move by capturing on sq; 0 = decline."""
    if depth <= 0:
        return 0
    caps = [m for m in board.legal_moves if m.to_square == sq]
    if not caps:
        return 0
    caps.sort(key=lambda m: VAL[board.piece_at(m.from_square).piece_type])
    move = caps[0]
    victim = board.piece_at(sq)
    gain = VAL[victim.piece_type] if victim else 0
    board.push(move)
    rec = see_reply(board, sq, depth - 1)
    board.pop()
    return max(0, gain - rec)


def see_capture(board, move):
    victim = board.piece_at(move.to_square)
    gain = VAL[victim.piece_type] if victim else 0
    board.push(move)
    rec = see_reply(board, move.to_square, 6)
    board.pop()
    return gain - rec


def main():
    payload = json.load(sys.stdin)
    board = chess.Board(payload["fen"])
    rows = []
    for move in list(board.legal_moves):
        san = board.san(move)
        board.push(move)
        worst = 0
        wsan = "-"
        for cap in list(board.legal_moves):
            if board.is_capture(cap):
                value = see_capture(board, cap)
                if value > worst:
                    worst = value
                    wsan = board.san(cap)
        board.pop()
        rows.append((worst, move.uci(), san, wsan))
    if not rows:
        print("hang-scan: no legal moves")
        return
    base = min(r[0] for r in rows)
    bad = [r for r in rows if r[0] >= 250 and r[0] >= base + 200]
    bad.sort(key=lambda r: -r[0])
    for worst, uci, san, wsan in bad[:6]:
        print("%s: his %s wins about %.1f pawns net on a static exchange"
              % (san, wsan, worst / 100.0))
    if base >= 250:
        print("note: every legal move allows a capture worth about %.1f"
              % (base / 100.0))
    if bad:
        print("AVOID: " + " ".join(r[1] for r in bad[:6]))
    else:
        print("hang-scan: no move hands over 2.5 pawns to a capture")


main()
