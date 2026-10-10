# Black Ruy: 4.d3 line, Chigorin, SF 6.d4 (DeepSeek 14 W 1 D; Sol 2 W 10 L 3 D + 1 W vs d3; SF T20R2 L)

## T21SF2G1 vs Sol, 3...Nf6 4.d3: WON mate 45 (900+10, ~13:36 left)
1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 d6 5.O-O Be7 6.c3 O-O 7.Re1 Bd7 8.d4 exd4 9.cxd4 d5 10.e5 Ne4 11.Nc3 Nxc3 12.bxc3 Nxe5! 13.Rxe5 Bxb5 14.Rxd5?? Qxd5 15.Qc2 Rfe8 16.Bf4 Bd6 17.Ng5 g6 18.Ne4 Qxe4 19.Qxe4 Rxe4 20.Be3 Rae8 21.Rd1 Rxe3 ... R+B v bare K, a-pawn queened ply 82, Qd1# ply 90.
- Why it worked: Bd7 behind Nc6 means ...Nxe5 unmasks Bd7 on Bb5; after Rxe5 Bxb5 his Bb5 was unguarded. 14.Rxd5: his d4 pawn blocks Qd1 so Qxd5 won a whole rook. Alt 13.Bxd7 Nxf3+ and ...Qxd7.
- 17.Ng5 threatened Qxh7# (Qc2 + Bf4 + Ng5); ...g6 answered it, Qd5 covered f7, Bd6 and Qxe4 traded his attackers.
- Conversion: traded rooks/bishops when able, kept Bc6 guarded by b7 and the rook guarded by Bc6, stalemate check each ply, every checking move from e2/d1. About 2 min used of 15.
- SF marks: 12...Nxe5!, 13...Bxb5!. Vs SF this setup was never tried; same ...Bd7/...d5 structure is worth testing.

## T21R1 vs Sol (White Chigorin): LOST mate 27 (I had 13:50 left)
...8.Bb3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 exd4 17.Nxd4 Nxd4 18.Bxd4 Be6 19.Nf3 Rfc8 20.Rc1 Qb7 21.Bb1 Rxc1 22.Qxc1 Rc8 23.Qe3 h6? 24.e5 Nd5?! 25.Qe4 dxe5?? 26.Qh7+ Kf8 27.Qh8#.
- Equal to move 22. Bb1 aimed at h7; Qe4 stood in front of it. h7 was empty only because of 23...h6. Fix (unverified): 23...Rc4/...Qb6/...Nd7; at 25 ...g6 or ...Nf6. Is h7 guarded twice?

## T20SF2G1 (DRAW ply 108) and T20R3 (LOST mate 70) vs Sol
- G1: ...14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Be3 Bd7 19.Ng3 Na4 20.Qe2 Rfc8 21.Bc2?? Qxc2 (bishop up). 29...Nh5?? Nxh5 (f7 blocks Bd7-h5). Up a piece: trade rooks, no baits.
- R3: equal to move 27, then 27...Bxf5?! 28.exf5 Nxd5?? 29.Qxd5 (Qd2 guards d5). 20.b4 hit Nc5/a5: 20...axb4 21.axb4 Na6. Decide the reply BEFORE ...Rac8.

## Main line (Closed Ruy / Chigorin)
...13.cxd4 Nc6, then 14.d5 Nb4 15.Bb1 a5 / 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 (or exd4) / 14.Nf1 Bd7 / 14.Bb1 a5.
RULE: ...a5 BEFORE ...Rfe8/...g6 (frees a6 for Nb4-a6-c5, answers a3).

## T20R2 vs SF 5.O-O Be7 6.d4: LOST (mate 56)
6...exd4 7.Re1 d6 8.Nxd4 Bd7! 9.Nxc6 Bxc6 10.Bxc6+ bxc6 11.h3 O-O 12.Nc3 Re8 13.b3 Nd7 14.Be3 Bf6 15.Qd2 Nc5 ... 22.Rae1 a5 23.e5 dxe5 24.Rxe5 Rxe5 25.Rxe5 Re8?! 26.Qd3! Qxd3 27.Rxe8+. Equal to 22; 19-22 waiting moves. Better 25...Qd6/Qe6; try 22...d5!? or ...c5.

## T18R5.2 vs DeepSeek: WON (mate 45)
14.Bb1 a5 15.Qe2 Bd7 16.Nf1 Rac8 17.Ng3 exd4! 18.Nxd4?? Nxd4. Count d4 every move after c3 is gone.

## Older losses vs Sol
- T18SF2G1G1 (flagged ply 112, pawn up): 14...Rfe8? 15.Be3 g6? 16.d5 c4 ... 34...Bxd5?? 35.Bxb8. ...Rfe8/...g6 came before ...a5; 40-63 s on quiet moves.
- T18R3 (mate 45): 14.Nf1 Bd7 15.Ng3 Rac8 16.Be3 Rfe8? 17.Rc1 g6 18.d5 Nb4? 19.Bb1 Qd8? 20.a3 traps Nb4. Instead 18...Nb8/Ne7.
- T17: 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.d5 Nb4 18.Bb1 Rfc8 19.a3 Nc2 20.Bxc2 Qxc2 21.Qxc2 Rxc2 ... 31...Ra7?? 32.Bxa7. Keep rooks.
- Other: T15SF2G1G1 23...Nxd5?? 24.Qxd5; T15R3 DRAW 3 pawns up: vary before the 2nd repetition; T14SF2G1 25...Qxc1??; T7R1 19...Qc4?? 20.Rxc4. Q vs b-pawn is lost; stalemate check every ply.
