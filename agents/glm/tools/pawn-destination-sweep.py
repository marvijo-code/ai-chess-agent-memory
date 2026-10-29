import json, sys
import chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
side = payload.get("side_to_move") or ("white" if board.turn == chess.WHITE else "black")
me = chess.WHITE if side == "white" else chess.BLACK
if board.turn != me:
    # mirror to my turn anyway: analyse moves for the side to move
    me = board.turn
them = not me

def pawn_captures(b):
    """my non-king pieces the enemy can capture with a PAWN (both diagonals)"""
    hits = {}
    for sq in chess.SQUARES:
        p = b.piece_at(sq)
        if p is not None and p.color == me and p.piece_type != chess.KING:
            if any(b.piece_type_at(a) == chess.PAWN for a in b.attackers(them, sq)):
                hits[sq] = p.symbol()
    return hits

before = set(pawn_captures(board))
avoid = set()
shown = 0
for move in list(board.legal_moves):
    san = board.san(move)
    board.push(move)
    now = pawn_captures(board)
    fresh = [(sq, sym) for sq, sym in now.items() if sq not in before]
    for sq, sym in fresh:
        kind = "LANDS" if sq == move.to_square else "EXPOSES"
        if shown < 8:
            print(f"{san} {kind}: {sym} on {chess.square_name(sq)} capturable by a pawn (pawns eat BOTH diagonals)")
            shown += 1
        if sym == "Q":
            avoid.add(move.uci())
    board.pop()
if avoid:
    print("AVOID: " + " ".join(sorted(avoid)))
else:
    print("no fresh pawn captures")
