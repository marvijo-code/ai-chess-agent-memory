# White vs 1.e4 c5 (Stockfish G2 loss)

## What happened
1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.O-O Nc7 6.Bc4? b5! 7.Bb3?? c4 (bishop trapped; Ba4 bxa4, Bxc4 bxc4). Eval jumped to about +6 for Black and never recovered.
- 6.Bc4 was the real error: after ...Nc7 the bishop is chased by ...b5. 6.Bxc6 dxc6 (or bxc6) was safe, 6.Bf1 or 6.Re1 also fine.
- 7.Bf1 (instead of Bb3) would have been OK: after ...b5 and ...b4 nothing is trapped.

## Safer plans
- 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4: Open Sicilian, known structure, bishops not exposed.
- Or 2.c3 (Alapin) with d4: solid, no early bishop adventures.
- If 3.Bb5: vs ...g6 play 4.O-O Bg7 5.Re1 e5 6.c3; vs ...Nf6 play 4.Nc3 (not 4.e5) or 4.Bxc6 dxc6 5.d3/Nc3 and develop calmly. If 4.e5 Nd5 is played, follow with 5.Nc3 Nxc3 6.dxc3 (Black's queen side is fine, but nothing hangs) instead of castling with the bishop loose.

## Checklist for any bishop retreat
1. List squares the bishop can reach after the opponent's best pawn push.
2. If only one retreat square exists and a pawn push can take it, trade the bishop now or retreat elsewhere.
3. Prefer main-line theory moves over invented ones; a 1-2 s book move is fine, long thought belongs where a piece can be lost.
