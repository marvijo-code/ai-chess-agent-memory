# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5.

## Keep
- 11.d4/13.cxd4/14.d5 good. 14...Nb4 -> 15.Bb1! only (b4-knight hits a2/c2/d3/d5; g21 15.Bd3?? Nxd3/Nxe1). 15...a5 16.a3 Na6 17.Qe2 Bd7 18.Nf1 Nc5: play 19.Nd2! (covers e4 AND b3); 19.Ng3?? Nb3! forks Ra1+Bc1 (g23).
- 14...Nb8 15.Nf1 Nbd7 16.Be3 Bb7 17.Qd2 Nc5 18.Ng3 (g10,g13,g18,g22). No Nf5 tour: after ...g6 f5 is pawn-attacked (g22 23.Nef5?? gxf5).
- Keep the dark bishop: 21.Bxf6?! (g13) and 21.Bxc5?! dxc5 (g18) hand Black the bishop pair; slow plan f4/Nf5/Rae1.
- Never Bxf7+?? Rxf7 or Bxb5?? axb5 = B for P.

## g31 vs GPT-6.1 Sol (0-1, m33)
14.d5 Nb8 15.b3 Nbd7 16.Bb2 Bb7 17.Rc1 Rac8 18.Nf1 Nc5 19.a4 b4 20.Ne3 g6 21.a5?! Qxa5 22.Nc4 Qc7 23.Nxd6?? Bxd6 24.Nxe5?? Bxe5 25.Bxe5 Qxe5 -> N+N for P, lost.
- Equal through 20...g6; b3/Bb2/Rc1 and Nf1-e3 are fine.
- 19.a4?! ...b4 then 21.a5?! drops a pawn: a5 undefended, his queen grabs it. Keep the pawn back; play Nd2/Bb1/f4 first.
- 23.Nxd6??: d6 is DEFENDED by Be7 (and Qc7). 24.Nxe5??: after ...Bxd6 the bishop also covers e5. Before ANY knight capture list enemy BISHOPS and check both diagonals of the target; d6/e5 sit on Be7/Bd6.
- 28.Qd6?? Qxd6 (undefended queen on his queen's diagonal - 'offering a trade' is no defense). 32.Re7?? Nxe7 (undefended rook where a knight attacks).
- Clock 1:28 vs 13:54; 39-69s on moves 14-32, incl. 49s on the Nxd6 blunder.

## Rook endings (g27)
- An enemy rook on the 2nd rank eats b2 then my rooks; 19...Nc2 forked Ra1+Re1 and c2 was 2v2 -> his LAST recapturer is a ROOK.
- Do NOT chase an enemy rook with an undefended rook (23.Rc2?? Rxc2 24.Re2?? Rxe2); use a DEFENDED rook (23.Rb1!).
- Before any rook move check the destination's rank/file for enemy rooks AND knights (g31 32.Re7?? Nxe7), and whether my rook has a defender.
- 28.Nxb5?? Bxb5; 29.Bxh6?? gxh6 (never grab a pawn a bishop/pawn recaptures).

## Queen safety (g9,g10,g13,g18,g21,g22,g31)
- Open c-file/d5: never my Q/R on a square any enemy slider attacks: g10 24.Qc2?? Rxc2; g18 23.Qd5?? Bxd5; g22 31.Qxc4?? Rc8xc4 = Q for R; g31 28.Qd6?? Qxd6.
- Every queen CAPTURE: list all defenders incl. rooks on the file (g22).
- Name the squares the queen leaves (g13 25.Qxh6?? left c2). Never move the queen where any piece or the KING can capture (g13 26.Qh8+?? Kxh8); 21.b4? Na4! (g9).

## Other losses
- g23: 19.Ng3?? Nb3! 20.Bd2?? Nxa1! 21.Bxa5?? Rxa5; 38.Nxe5?? dxe5 = N for P.
- g22: 37-61s/move 12-31, flagged m42; 26.Nxd6?? Qxd6.
- g21: 15.Bd3?? Nxd3; 18.Nc4?? bxc4; 22.Qb3?? cxb3; mate 29...Rb1#.
- g27: 22.Rac1? Rxb2! then one enemy rook took b2 + both my rooks.

## Game management
- Routine <=15s; the 5s scan of the FINAL move is the fix.
- Down material (g10,g13,g18,g22,g23,g27,g31): king safety first, defend loose pieces, trade, 5-15s, no pawn grabs, no capture his piece recaptures.
