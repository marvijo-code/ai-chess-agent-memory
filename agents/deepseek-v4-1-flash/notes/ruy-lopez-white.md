# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5.

## Keep
- 11.d4/13.cxd4/14.d5 good. 14...Nb4 -> 15.Bb1! only (b4-knight hits a2/c2/d3/d5; g21 15.Bd3?? Nxd3/Nxe1). 15...a5 16.a3 Na6 17.Qe2 Bd7 18.Nf1 Nc5: play 19.Nd2! (covers e4 AND b3); 19.Ng3?? Nb3! forks Ra1+Bc1 (g23).
- 14...Nb8 15.Nf1 Nbd7 16.Be3 Bb7 17.Qd2 Nc5 18.Ng3 (g10,g13,g18,g22). No Nf5 tour: after ...g6 f5 is pawn-attacked (g22 23.Nef5?? gxf5).
- Keep the dark bishop: 21.Bxf6?! (g13) and 21.Bxc5?! dxc5 (g18) hand Black the bishop pair; slow plan f4/Nf5/Rae1.
- Never Bxf7+?? Rxf7 or Bxb5?? axb5 = B for P.

## g33 vs GPT-6.1 Sol (0-1, m27)
14.Nf1 Rac8 15.Ne3 Nc4 16.Nxc4 Qxc4 17.Be3?? Rfe8 18.Qd2?? Bxe4 19.Bxe4 Nxe4 20.dxe5?? Nxd2 21.Nxd2 Qd5 -> Q for N, mated 27...Qxg2#.
- 14...Rac8 15.Ne3 Nc4: Black offers this exchange; 16.Nxc4 Qxc4 (QUEEN recapture) gives him an active queen hitting Bc2. Equal through 16...Qxc4.
- 17.Be3?? Rfe8 18.Qd2?? Bxe4!: with a piece on e3, Re1's e-file is blocked AND Qd2-e3-e4 is blocked, so e4 has no rescuer. Keep e3 EMPTY while his Qc4+...Bb7 aim at e4: 17.Qd2 (or Bd2) first, or block with d5. General: my own piece must not block my rescuer (also g33 20.Qxe4/Nd2 illegal tries).
- 19...Nxe4: the knight hits d2/f2/g3/g5/c3/c5/d6/f6 - my QUEEN on d2 was attacked. 20.dxe5?? ignored it -> 20...Nxd2. Save the queen first (Qe2/Qe3); 2:35 and 3 tries on this move.
- 23.Nxe5?? Qxe5 = N for P (knight grab of a queen-defended pawn). 24.Bd4?? Qxd4: no rook actually defended d4 - an 'offer' only his queen can accept just loses it.
- Down material: king safety first; 27...Qxg2# with Rc2 guarding the queen.

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
- Down material (g10,g13,g18,g22,g23,g27,g31,g33): king safety first, defend loose pieces, trade, 5-15s, no pawn grabs, no capture his piece recaptures.
