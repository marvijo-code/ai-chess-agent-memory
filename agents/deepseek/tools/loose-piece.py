import json
import sys
import chess

VALUES = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3,
          chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 100}


def main():
    payload = json.load(sys.stdin)
    board = chess.Board(payload["fen"])
    me = board.turn
    legal = list(board.legal_moves)
    bad = []
    for move in legal:
        board.push(move)
        hit = None
        for reply in board.legal_moves:
            victim = board.piece_at(reply.to_square)
            if victim is None or victim.color != me:
                continue
            if VALUES[victim.piece_type] < 3:
                continue
            if board.attackers(me, reply.to_square):
                continue
            hit = (reply, victim)
            break
        board.pop()
        if hit:
            bad.append(move.uci())
            print("%s leaves your %s on %s with no guard; %s wins it"
                  % (move.uci(), hit[1].symbol(),
                     chess.square_name(hit[0].to_square), hit[0].uci()))
    if not bad:
        print("no move leaves a piece of value 3+ undefended")
    elif len(bad) == len(legal):
        print("every legal move leaves something loose - keep the best-guarded piece")
    else:
        print("AVOID: " + " ".join(bad))


main()
