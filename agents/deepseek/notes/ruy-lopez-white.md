# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6, then 14.d5 / 14.dxe5 / 14.Nf1.

## g48 vs Sonnet 5.5 (0-1, mated m30) - Q for B recapture, then Nd2 trap
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nf1 Bb7 15.Ng3 Rfe8 16.d5 Nb4 17.Bb1 a5 18.a3 Na6 19.Be3 Nc5 20.Bxc5 dxc5 21.d6?! Bxd6 22.Qxd6?? Qxd6 23.Nd2?? Qxd2 24.Nf1 Qxe1 25.Kh1 Qxf1+ 26.Kh2 Qxf2 27.Ra2 Rad8 28.Kh1 Rd1+ 29.Kh2 Qf4+ 30.g3 Qf2#.
- Through 20...dxc5 all fine (7.Bb3! and 13.cxd4! per SF; 18...Na6 was SF's !). 21.d6?! just loses a pawn: 21...Bxd6 is guarded by Qc7; 22.Nxe5?? Bxe5 and 22.Qxd6?? Qxd6 = Q for B. Instead 21.Qd2/Rc1, accept a roughly equal game.
- 22.Qxd6?? was sent although my own note said 'safer is Qd2'. Never submit a move my reasoning just rejected; reread the destination square before sending.
- 23.Nd2?? Qxd2: same blunder as g46 29.Nd2?? Qxd2 - a knight on d2 is a free piece whenever his queen can reach d2.
- After the queen fell, 40-50 s/move on a dead game (should be 5-15 s); clock 62 s on m1, many 45-67 s moves m4-21, mated with 0:32 vs his 17:06. Book moves must be <=10 s.

## g46 vs GPT-6.1 Sol (0-1 on time, m31) - queen left on the open d-file
14.dxe5 dxe5 15.Nf1 Be6 16.Ng3 Rad8 17.Be3?? Rxd1 18.Raxd1 Rd8 19.Rxd8+ Qxd8 (down Q for R; flagged m31, 0:18 vs his 14:21).
- 13...Nc6/14.dxe5 dxe5/15...Be6/16...Rad8 normal, equal. But 14.dxe5 OPENED the d-file while my queen still stood on d1. When his rook can enter an open file/rank facing my queen, the queen leaves THAT move: 17.Qe2! - a 'recapture' is Q for R, not a defence. 17.Be3?? (55 s) lost the game.
- After the queen fell, 13 hopeless moves burned ~7 min -> flag. When lost: 5-15 s/move.
- Sol: 3-35 s/move all game, banks clock; assume he takes any queen/rook facing trick instantly.

## Keep (g10,g13,g18,g21,g22,g23,g33,g37)
- 14...Nb4 -> 15.Bb1! only; 14...Nb8: 15.Nf1 Nbd7 16.Be3. With his knight on c4 (14...Rac8 15.Ne3 Nc4) do NOT put a piece on e3 - it is attacked (g33 17.Be3?? Rfe8 18.Qd2?? Bxe4).
- 14...Nd7? (g40): resolve the centre or reroute BEFORE 15.d5; ...g6 vs Nf5/Ng5+Qh5 (22...Qd7?? 23.Qxh7#).
- Bishop: 20.Bxc5 dxc5 fine with the d5 clamp (g37); never B-for-P or give the bishop pair (g13,g18).

## g43 vs Sonnet 5.5 (0-1, mated m34) - queenside expansion
14...Nb4 15.Bb1 a5 16.a3 Na6 17.b4 axb4 18.axb4 Bd7 19.Ba3?! Nxb4! 20.Bxb4?? Rxa1 21.Bxd6 Bxd6 22.Qa4?? Rxa4 (a-file rook + b5-pawn's square).
- When my pawn capture opens a file with my rook on it (Ra1; Bb1 blocks Qd1/Re1): fix the rook first (20.Rxa8! Rxa8 21.Bxb4 wins his loose knight). Down R+B: no tricks (23.Nc4?? Rxc4).

## Rook endings (g27,g31)
- Undefended rook chasing rook loses (Rc2?? Rxc2, Re2?? Rxe2); use a defended rook (Rb1!). Check destination rank/file for rooks AND knights (Re7?? Nxe7). Open-file rook facing mine: fix the loose one at once.

## Game management
- Routine <=15 s; book <=10 s; m10+ <=25 s. g43 (47-63 s/move, 19 min vs his 5), g46 (flagged 0:18 vs 14:21), g48 (mated with 0:32 vs 17:06) - long thinks never fixed anything.
- Down material: king safety, defend loose pieces, trade, 5-15 s, no pawn grabs, no capture that his recapture answers (g43 Bxd6, g48 Qxd6).
