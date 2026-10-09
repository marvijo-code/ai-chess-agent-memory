# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5. Then 14...Nb4 (15.Bb1!) or 14...Nb8 (15.Nf1 Nbd7 16.Be3 Bb7 17.Qd2 Nc5 18.Ng3 Rfe8).

## Keep
- 11.d4/13.cxd4/14.d5 good. 14...Nb4 -> 15.Bb1! is the only safe square (b4-knight attacks a2/c2/d3/d5; g21 15.Bd3?? Nxd3/Nxe1 = B+R for N). 15.Bb1 a5 16.a3 (only if Qd1+Bb1 cover c2) Na6 17.Nf1 Bd7 18.Ng3 Nc5.
- Keep the dark bishop: 21.Bxf6?! (g13), 21.Bxc5?! dxc5 (g18) hand Black the bishop pair; slow plan f4/Nf5/Rae1.
- Never Bxf7+?? Rxf7 or Bxb5?? axb5 = B for P.
- 14...Nb8 lines (g10,g13,g18,g22) stay equal: no Nf5 tour wins anything, and after ...g6 f5 is pawn-attacked - g22 23.Nef5?? gxf5 = N for P.

## Queen safety (g9,g10,g13,g18,g21,g22)
- Open c-file/d5: never my Q/R on a square any enemy slider attacks: g10 24.Qc2?? Rxc2; g9 23.Qxc3?? Qxc3; g18 23.Qd5?? Bxd5; g19 28...Qxd5?? Bxd5.
- Any queen CAPTURE: list all defenders incl. rooks on the file: g22 31.Qxc4?? Rc8xc4 = Q for R.
- Qd2 covers c2/f2: name the squares the queen leaves (g13 25.Qxh6?? left c2). Never move the queen where any piece or the KING can capture (g13 26.Qh8+?? Kxh8).
- 21.b4? Na4! (g9).

## g22 vs GPT-6.1 Sol (0-1, flagged m42)
9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb8 15.Nf1 Nbd7 16.Be3 Bb7 17.Qd2 Nc5 18.Ng3 Rfe8 19.Nf5 Bf8 20.Bxc5 Qxc5 21.Ne3 g6 22.Nh4 Bg7 23.Nef5?? gxf5 24.Nxf5.
- 23.Nef5?? = N for P (g6-pawn attacks f5); 26.Nxd6?? Qxd6 = N for P (d6 defended by Qc5): count recapturers before every knight capture.
- 31.Qxc4?? Rc8xc4 = Q for R (rook c4 defended along the c-file). Sol recaptures everything; every capture must survive his recapture.
- Clock: 37-61s on moves 12-31 (routine moves); 5:43 at m26, 2:47 at m31; flagged at m42. Long thinks found no plan, prevented no blunder.

## g21 vs GPT-6.1 Sol (0-1, mated m29)
14...Nb4 15.Bd3?? Nxd3 16.Qe2 Nxe1 (16.Qe2 was illegal - Nd2 blocks the d-file); 18.Nc4?? bxc4; 22.Qb3?? cxb3; mate 29...Rb1# (king h1, own g2 pawn, rook rank 1, queen covers h2). Magnet squares: d3/c4/b3.

## Game management
- Routine moves <=15s; the 5s scan on the FINAL move is the fix. g21: 43-91s thinks then 15.Bd3??; g22: 40-61s/move then 3 blunders + flag.
- Down material (g10,g13,g18,g22): king safety first, defend loose pieces, trade, 5-15s moves.
