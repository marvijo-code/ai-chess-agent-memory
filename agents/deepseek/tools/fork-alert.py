import json, sys, chess

def main():
    payload = json.load(sys.stdin)
    board = chess.Board(payload["fen"])
    mine = board.turn
    opp = not mine
    count = 0
    for move in board.legal_moves:
        if count >= 5:
            break
        san = board.san(move)
        board.push(move)
        fork = None
        for opp_move in board.legal_moves:
            piece = board.piece_at(opp_move.from_square)
            if not piece or piece.piece_type != chess.KNIGHT or piece.color != opp:
                continue
            board.push(opp_move)
            my_queen = None
            my_king = None
            for sq in chess.SQUARES:
                p = board.piece_at(sq)
                if p and p.color == mine:
                    if p.piece_type == chess.QUEEN:
                        my_queen = sq
                    elif p.piece_type == chess.KING:
                        my_king = sq
            if my_queen is not None and my_king is not None:
                attacks = board.attacks(opp_move.to_square)
                if my_queen in attacks and my_king in attacks:
                    fork = (opp_move, my_queen, my_king)
            board.pop()
            if fork:
                break
        if fork:
            opp_san = board.san(fork[0])
            print(f"AVOID: {move.uci()} - allows ...{opp_san} forking your Q on {chess.square_name(fork[1])} and K on {chess.square_name(fork[2])}")
            count += 1
        board.pop()
    if count == 0:
        print("no queen+king knight fork after your legal moves")

if __name__ == "__main__":
    main()
