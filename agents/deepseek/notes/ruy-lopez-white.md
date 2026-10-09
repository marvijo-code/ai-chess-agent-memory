# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6, then 14.d5 / 14.dxe5 / 14.Nf1.

## g51 vs Sonnet (0-1, m34) - queen for knight on d5
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.a3 Na6 18.Be3 Nc5 19.Bxc5 Qxc5 20.Qd2 Rfc8 21.Ng3 h6 22.Nf5 Bxf5 23.exf5 Nxd5?? 24.Qxd5?? Qxd5 25.Rxe5?? dxe5.
- Good to 23.exf5 (SF: Bb3!, cxd4!, Bb1!, exf5!); his Qc5 guards d5. 24.Qxd5?? takes a knight his QUEEN defends: Q for N, not a queen trade (my queen undefended, f5-pawn blocks Bb1). Name the recapturer and its value before capturing.
- 25.Rxe5?? his d6-PAWN recaptures; list enemy PAWNS as recapturers.
- Down Q for N: defend, trade, 5-15 s; clock ended 3:28 vs his 17:18, mated m34.

## g48 vs Sonnet (0-1, m30) - Q for B recapture, Nd2 trap
14.Nf1 Bb7 15.Ng3 Rfe8 16.d5 Nb4 17.Bb1 a5 18.a3 Na6 19.Be3 Nc5 20.Bxc5 dxc5 21.d6?! Bxd6 22.Qxd6?? Qxd6 23.Nd2?? Qxd2 24.Nf1 Qxe1 25.Kh1 Qxf1+ 26.Kh2 Qxf2 27.Ra2 Rad8 28.Kh1 Rd1+ 29.Kh2 Qf4+ 30.g3 Qf2#.
- Through 20...dxc5 all fine. 21.d6?! just loses a pawn (21...Bxd6, guarded by Qc7); instead 21.Qd2/Rc1, equal.
- 22.Qxd6?? I had already rejected it in my own reasoning, then sent it. Never send a rejected move; reread the destination.
- 23.Nd2?? Qxd2 (also g46): a knight on d2 is free once his queen reaches d2. After the queen fell I burned 40-50 s/move; mated with 0:32 vs his 17:06.

## g46 vs GPT-6.1 Sol (0-1 on time, m31) - queen left on the open d-file
14.dxe5 dxe5 15.Nf1 Be6 16.Ng3 Rad8 17.Be3?? Rxd1 18.Raxd1 Rd8 19.Rxd8+ Qxd8 (down Q for R; flagged m31, 0:18 vs 14:21).
- 14.dxe5 OPENED the d-file while my queen stood on d1. When his rook enters an open file facing my queen, the queen leaves THAT move: 17.Qe2! (a 'recapture' would be Q for R, not a defence). 17.Be3?? (55 s) lost.
- Once lost: 5-15 s/move, not 13 hopeless moves in ~7 min -> flag.

## Keep (g10,g13,g18,g21,g22,g23,g33,g37)
- 14...Nb4 -> 15.Bb1! only; 14...Nb8: 15.Nf1 Nbd7 16.Be3. With his knight on c4 (14...Rac8 15.Ne3 Nc4) do NOT play Be3 - it is attacked (g33 17.Be3?? Rfe8 18.Qd2?? Bxe4).
- 14...Nd7? (g40): resolve the centre or reroute BEFORE 15.d5; ...g6 vs Nf5/Ng5+Qh5 (22...Qd7?? 23.Qxh7#).
- Bishop: 20.Bxc5 dxc5 fine with the d5 clamp (g37); never B-for-P or give the bishop pair (g13,g18).

## g43 vs Sonnet (0-1, m34) - queenside expansion
14...Nb4 15.Bb1 a5 16.a3 Na6 17.b4 axb4 18.axb4 Bd7 19.Ba3?! Nxb4! 20.Bxb4?? Rxa1 21.Bxd6 Bxd6 22.Qa4?? Rxa4 (a-file rook + b5-pawn's square).
- When my capture opens a file with my rook on it (Ra1, Bb1 blocking Qd1/Re1): fix the rook first (20.Rxa8! Rxa8 21.Bxb4 wins his loose knight). Down R+B: no tricks (23.Nc4?? Rxc4).

## Rook endings (g27,g31)
- Undefended rook chasing rook loses (Rc2?? Rxc2, Re2?? Rxe2); use a defended rook. Check destination rank/file for rooks AND knights (Re7?? Nxe7). His rook to an open file at my loose rook: fix it at once.

## Game management
- Routine <=15 s; book <=10 s; m10+ <=25 s. g43 (47-63 s/move, 19 min vs his 5), g46 (flagged 0:18 vs 14:21), g48 (mated with 0:32 vs 17:06) - long thinks never fixed anything.
- Down material: king safety, defend loose pieces, trade, 5-15 s, no pawn grabs, no capture his recapture answers (g43 Bxd6, g48 Qxd6, g51 Qxd5).
