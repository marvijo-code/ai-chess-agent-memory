import json
import sys
import chess

VALUES = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}


def material(board, color):
    total = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None and piece.color == color:
            total += VALUES[piece.piece_type]
    return total


def worst_loss(board, move):
    """Approximate the biggest material swing against me after this move."""
    board.push(move)
    worst = 0
    for reply in board.legal_moves:
        victim = board.piece_at(reply.to_square)
        if victim is None:
            continue
        gain = VALUES[victim.piece_type]
        board.push(reply)
        recapture = 0
        for back in board.legal_moves:
            if back.to_square == reply.to_square:
                piece = board.piece_at(back.to_square)
                if piece is not None:
                    recapture = max(recapture, VALUES[piece.piece_type])
        board.pop()
        worst = max(worst, gain - recapture)
    board.pop()
    return worst


def main():
    payload = json.load(sys.stdin)
    board = chess.Board(payload["fen"])
    if board.turn == chess.WHITE:
        me, them, myname = chess.WHITE, chess.BLACK, "White"
    else:
        me, them, myname = chess.BLACK, chess.WHITE, "Black"
    my_mat = material(board, me)
    their_mat = material(board, them)
    moves = list(board.legal_moves)
    scored = []
    for move in moves:
        san = board.san(move)
        scored.append((worst_loss(board, move), san, move.uci()))
    scored.sort(key=lambda item: item[0])
    print("material %s %d v %d (diff %+d)" % (myname, my_mat, their_mat, my_mat - their_mat))
    best = scored[:3]
    print("least-loss moves: " + ", ".join("%s(%d)" % (san, loss) for loss, san, uci in best))
    # flag only big losses, and always keep at least three legal moves unflagged
    big = [item for item in scored if item[0] >= 5]
    big.sort(key=lambda item: -item[0])
    allowed = max(0, len(scored) - 3)
    big = big[:allowed]
    if not big:
        print("no move loses an exchange or more")
    for loss, san, uci in big[:6]:
        print("AVOID: %s - %s loses material worth %d (exchange or more)" % (uci, san, loss))


if __name__ == "__main__":
    main()
