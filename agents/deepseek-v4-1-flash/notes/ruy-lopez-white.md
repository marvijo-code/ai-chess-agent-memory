# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5.

## g37 vs GPT-6.1 Sol (0-1, m31) - 14...Nb8 main line
14...Nb8 15.Bb1 Nbd7 16.Nf1 Bb7 17.Ng3 Nc5 18.Be3 Rfe8 19.Qd2 Bf8 20.Bxc5 dxc5 21.Ne2 c4 22.d6 Bxd6 23.Nc3 b4 24.Nd5 Nxd5 25.exd5 e4 26.Rxe4 Rxe4 27.Bxe4.
- Through 27.Bxe4 this was fine (Stockfish marks Bb3!, cxd4!): Bb7 is blocked by my d5 pawn, so the rook trade wins a pawn; material then equal.
- 27...c3 hit my Qd2. 28.Qxc3?? bxc3!: c3 was attacked by the b4-PAWN and by Qc7 down the open c-file (c4-pawn had moved on). Retreat (Qd3/Qe2), giving up cxb2. Never Qx a square an enemy pawn attacks.
- Clock: 38-56s on moves 2-28, 5:27 left at m29; long thinks did not prevent the blunder.

## Keep (g10,g13,g18,g21,g22,g23,g33)
- 14...Nb4 -> 15.Bb1! only (g21 15.Bd3?? Nxd3/Nxe1). 15...a5 16.a3 Na6 17.Qe2 Bd7 18.Nf1 Nc5: 19.Nd2! covers e4+b3; 19.Ng3?? Nb3! forks Ra1+Bc1 (g23).
- 14...Nb8 standard: 15.Nf1 Nbd7 16.Be3 Bb7 17.Qd2 Nc5 18.Ng3; no Nf5 tour - after ...g6 f5 is pawn-attacked (g22 23.Nef5?? gxf5).
- 14...Rac8 15.Ne3 Nc4: keep e3 EMPTY - it is e4's rescuer (g33 17.Be3?? Rfe8 18.Qd2?? Bxe4!).
- Bishop: 20.Bxc5 dxc5 is fine with the d5 clamp (g37); other lines 21.Bxf6?! (g13), 21.Bxc5?! dxc5 (g18) hand Black the bishop pair; keep the dark bishop, plan f4/Nf5/Rae1. Never Bxf7+?? Rxf7 or Bxb5?? axb5 = B for P.

## g33 (0-1, m27)
14.Nf1 Rac8 15.Ne3 Nc4 16.Nxc4 Qxc4 17.Be3?? Rfe8 18.Qd2?? Bxe4! 19.Bxe4 Nxe4 20.dxe5?? Nxd2 -> Q for N, mated.
- With Be3 played, Re1's e-file and Qd2-e3-e4 are blocked, so e4 has no rescuer (20.Qxe4/Nd2 illegal tries). Keep e3 empty while his Qc4+...Bb7 aim at e4.
- 19...Nxe4 hit Qd2: save the queen first. 23.Nxe5?? Qxe5 = N for P; 24.Bd4?? Qxd4 (no defender).

## Queen safety (g9,g10,g13,g18,g21,g22,g31,g37)
- Never my Q/R on a square any enemy slider/rook/PAWN attacks: g10 24.Qc2?? Rxc2; g18 23.Qd5?? Bxd5; g22 31.Qxc4?? Rc8xc4; g31 28.Qd6?? Qxd6; g37 28.Qxc3?? bxc3.
- Every queen CAPTURE: list all defenders incl. pawns and rooks on files (g22,g37).
- Name the squares the queen leaves (g13 25.Qxh6??); never move the queen where any piece or the KING can capture (g13 26.Qh8+?? Kxh8); 21.b4? Na4! (g9).

## Rook endings (g27,g31)
- An undefended rook chasing an enemy rook loses (23.Rc2?? Rxc2 24.Re2?? Rxe2); use a DEFENDED rook (23.Rb1!). Check the destination's rank/file for enemy rooks AND knights (g31 32.Re7?? Nxe7).
- 28.Nxb5?? Bxb5; 29.Bxh6?? gxh6 (never grab a pawn a pawn/bishop recaptures).

## Game management
- Routine <=15s; from move 10 no move >30s. The 5s scan of the FINAL move is the fix. g22 used 37-61s/move and flagged.
- Down material (g10,g13,g18,g22,g23,g27,g31,g33): king safety first, defend loose pieces, trade, 5-15s, no pawn grabs, no capture his piece recaptures.
