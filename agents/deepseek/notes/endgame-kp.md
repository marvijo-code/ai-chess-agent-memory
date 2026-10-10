# Endgames: K+P vs K and piece-up conversion (g92)

## g92 vs Sonnet (0-1, Qb7# m73) - lost the N+1P vs 3P ending
Line: 26.Bg5?? hxg5 (B for 2P, then Nxg5 Qxg5) -> down N for P -> 53.Kxb7 reached K+1P vs K+1P... actually K vs K+P(g6)+g2 raced.

### The race (after 53.Kxb7 Kg3 54.Kc6 Kxg2)
Position: White Kb7, Black Kg2 + pawn g6 (White g2 pawn gone). White must catch the g-pawn or blockade.
- Game: 55.Kd5 g5 56.Ke4 g4 57.Kf4 Kh3 58.Kg5 g3 59.Kf4 g2 60.Kf3 g1=Q.
- Key: White king needs 4 moves (b7-c6-d5-e4-f5) to reach f5/g5; Black king takes g2 (1 move) then runs the pawn (5 moves) = pawn promotes before White arrives. LOST unless White gets IN FRONT with a tempo to spare.
- Rule: with the black king right beside (defending) the pawn, a g-pawn (or any pawn) on the 5th-6th rank RUNS HOME; the defender must get to the square in front (f5/g5) BEFORE the pawn reaches the 3rd rank, or win the pawn outright.
- So the whole ending hinged on tempos much earlier: do NOT let a lone far-away king face a king-supported passer; keep the pawn trade option open, or keep my own pawn (g2) longer so Black spends a move grabbing it.

### Concrete GTB-style checks I got wrong
- 55.Ke5!? was the move (not Kd5): from e5 White threatens Kf5 winning g6 while the black king is still on g2 (too far to defend). Even then Black escorts it home if the king is closer.
- Knight sacrifice by the stronger side (...Nxb7 giving N for the last pawn) still WINS if their king+passer race beats my king. Do not 'win' the b7-pawn-for-knight trade unless my king is close enough to stop the passer.

## Rules
- K+P vs K: the defender draws iff he gets his king IN FRONT of the pawn (or captures it). A king behind/beside with the pawn supported = loss. Do not calculate 'it's a pawn ending, probably draw' without counting moves to the square in front.
- Race arithmetic: count BOTH kings' distances to the critical squares every ply; one tempo decides.
- Piece-up conversion (his side): he traded the knight for my passed pawn at the right moment; his king was already on the pawn's file. When I am the stronger side, do the same: take the last defender's pawn only when my king escorts the passer.
- When down a piece, keep MY pawns (g2) to buy tempi and seek pawn trades; do not walk the king so far queenside that the kingside pawn falls for free.
