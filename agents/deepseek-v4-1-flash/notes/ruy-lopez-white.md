# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5. Then 14...Nb4 (15.Bb1!) or 14...Nb8 (15.Nf1 Nbd7 16.Be3 Bb7 17.Qd2 Nc5 18.Ng3 Rfe8).

## Keep
- 11.d4/13.cxd4/14.d5 good. 14...Nb4 -> 15.Bb1! is the only safe square (b4-knight attacks a2/c2/d3/d5; g21 15.Bd3?? Nxd3/Nxe1). 15...a5 16.a3 Na6 17.Qe2 Bd7 18.Nf1 Nc5: play 19.Nd2! (covers e4 AND b3); 19.Ng3?? allowed 19...Nb3! forking Ra1+Bc1 (g23).
- Keep the dark bishop: 21.Bxf6?! (g13), 21.Bxc5?! dxc5 (g18) hand Black the bishop pair; slow plan f4/Nf5/Rae1.
- Never Bxf7+?? Rxf7 or Bxb5?? axb5 = B for P.
- 14...Nb8 lines (g10,g13,g18,g22) stay equal: no Nf5 tour wins anything, and after ...g6 f5 is pawn-attacked - g22 23.Nef5?? gxf5 = N for P.
- g27 plan was fine: 16.Nf1 Bd7 17.Ng3 Rfc8 18.Be3 h6 19.Qd2.

## Rook endings (g27 - new)
- After queens come off, an enemy rook that lands on the 2nd rank kills you: it eats b2 and then your rooks.
- 19...Nc2 forks Ra1+Re1 (knight fork, same idea as g23 Nb3). c2 was attacked by Bb1+Qd2 but covered by Qc7+Rc8 (2v2): the capturer's LAST recapture lands on c2 - his ROOK. My 20.Bxc2?? Qxc2 21.Qxc2 Rxc2 gave that position.
- 22.Rac1? Rxb2! 23.Rc2?? Rxc2 24.Re2?? Rxe2: his ONE rook took b2-pawn + my two rooks. Do NOT chase an enemy rook with an undefended rook; do NOT put a rook on a square his rook attacks.
- Correct: 23.Rb1! (defended by Re1) - 23...Rxb1+ 24.Rxb1 trades rooks and I lose only the b2-pawn.
- Rule: before any rook move check the destination's rank/file for enemy rooks AND whether my rook has a defender.

## Queen safety (g9,g10,g13,g18,g21,g22)
- Open c-file/d5: never my Q/R on a square any enemy slider attacks: g10 24.Qc2?? Rxc2; g9 23.Qxc3?? Qxc3; g18 23.Qd5?? Bxd5.
- Any queen CAPTURE: list all defenders incl. rooks on the file: g22 31.Qxc4?? Rc8xc4 = Q for R.
- Qd2 covers c2/f2: name the squares the queen leaves (g13 25.Qxh6?? left c2). Never move the queen where any piece or the KING can capture (g13 26.Qh8+?? Kxh8).
- 21.b4? Na4! (g9).

## g27 vs Sonnet 5.5 (0-1, mated m41) - Chigorin
Same line to 15.Bb1/16.Nf1/17.Ng3/18.Be3/19.Qd2 - equal. 19...Nc2?? 20.Bxc2?? Qxc2 21.Qxc2 Rxc2 22.Rac1? Rxb2! 23.Rc2?? Rxc2 24.Re2 Rxe2 25.Nxe2 25...Nxe4 26.Nfd4 exd4 27.Nxd4 Rc8 28.Nxb5?? Bxb5 (knight grabs a pawn a bishop recaptures: N for P) 29.Bxh6?? gxh6 30.f4 Rc1+ 31.Kh2 Bh4 32.g3 Rc2+ ... Rh2#.
- Material was LEVEL after 21...Rxc2; everything lost from 22-25 (rook play) plus 28.Nxb5??/29.Bxh6?? (piece grabs of pawns that recapture).
- Down material after that: only legal moves, play instantly; clock 48s vs 16min.

## g23 vs Sonnet 5.5 (0-1, mated m52) - Chigorin
9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Qe2 Bd7 18.Nf1 Nc5 19.Ng3?? Nb3! 20.Bd2?? Nxa1! 21.Bxa5?? Rxa5 22.Qe3 Nc2 23.Bxc2 Qxc2 24.Qe2 Qxe2 25.Rxe2 Rfa8, Black converts.
- 19.Nd2 covers b3 and e4. Fork defense: never step onto a forker's square (20.Bd2??). 21.Bxa5?? Rxa5 = B for P.
- 38.Nxe5?? dxe5 = N for P - count recapturers before EVERY knight capture.

## g22 vs GPT-6.1 Sol (0-1, flagged m42)
14.d5 Nb8 15.Nf1 Nbd7 16.Be3 Bb7 17.Qd2 Nc5 18.Ng3 Rfe8 19.Nf5 Bf8 20.Bxc5 Qxc5 21.Ne3 g6 22.Nh4 Bg7 23.Nef5?? gxf5 24.Nxf5.
- 23.Nef5?? = N for P; 26.Nxd6?? Qxd6; 31.Qxc4?? Rc8xc4 = Q for R.
- Clock: 37-61s/move 12-31; flagged at m42.

## g21 vs GPT-6.1 Sol (0-1, mated m29)
14...Nb4 15.Bd3?? Nxd3 16.Qe2 Nxe1; 18.Nc4?? bxc4; 22.Qb3?? cxb3; mate 29...Rb1#.

## Game management
- Routine moves <=15s; the 5s scan on the FINAL move is the fix.
- Down material (g10,g13,g18,g22,g23,g27): king safety first, defend loose pieces, trade, 5-15s moves, no pawn grabs.
