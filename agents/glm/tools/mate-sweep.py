import json, sys, chess

p = json.load(sys.stdin)
b = chess.Board(p["fen"])
print("turn:", "white" if b.turn else "black", "| legal moves:", b.legal_moves.count())
if b.is_check():
    k = b.king(b.turn)
    flights = [chess.square_name(k) + chess.square_name(m.to_square)
               for m in b.legal_moves
               if b.piece_type_at(m.from_square) == chess.KING]
    if flights:
        print("IN CHECK - king step FIRST, legal: " + " ".join(flights))
    else:
        print("IN CHECK - no king move legal; find a block or capture from the FEN")
bad = []
for mv in list(b.legal_moves):
    b.push(mv)
    for r in list(b.legal_moves):
        b.push(r)
        if b.is_checkmate():
            bad.append(mv.uci())
            print(b.san(mv) + " allows mate-in-1 by " + b.san(r))
        b.pop()
    b.pop()
if bad:
    print("AVOID: " + " ".join(sorted(set(bad))))
else:
    print("no mate-in-1 after any of my moves")
