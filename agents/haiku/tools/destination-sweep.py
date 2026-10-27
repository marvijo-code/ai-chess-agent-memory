import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
me = board.turn
VAL = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 100}


def loose(b):
    found = set()
    for sq in chess.SQUARES:
        p = b.piece_at(sq)
        if p is None or p.color != me or p.piece_type == chess.KING:
            continue
        attackers = b.attackers(not me, sq)
        if not attackers:
            continue
        defenders = b.attackers(me, sq)
        cheapest = min(VAL[b.piece_type_at(a)] for a in attackers)
        if not defenders or cheapest < VAL[p.piece_type]:
            found.add(chess.square_name(sq))
    return found


before = loose(board)
bad, lines = [], []
for move in list(board.legal_moves):
    mover = board.piece_at(move.from_square)
    captured = board.piece_at(move.to_square)
    cap_val = VAL[captured.piece_type] if captured else 0
    if board.is_en_passant(move):
        cap_val = 1
    san = board.san(move)
    board.push(move)
    new = loose(board) - before
    board.pop()
    dest = chess.square_name(move.to_square)
    if dest in new and cap_val >= VAL[mover.piece_type]:
        new.discard(dest)
    if new:
        bad.append(move.uci())
        if len(lines) < 6:
            lines.append(san + " leaves " + ", ".join(sorted(new)) + " loose")

for line in lines:
    print(line)
if bad:
    print("AVOID: " + " ".join(sorted(set(bad))))
else:
    print("no legal move leaves a new loose piece")
