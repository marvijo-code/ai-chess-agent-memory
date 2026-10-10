# Black Ruy: SF 6.d4 and Chigorin (DeepSeek 14 W 1 D; Sol 2 W 10 L 3 D; SF T20R2 L)

## T21R1 vs Sol (White): LOST mate 27 (900+10, I had 13:50 left)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 d6 7.c3 b5 8.Bb3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 exd4 17.Nxd4 Nxd4 18.Bxd4 Be6 19.Nf3 Rfc8 20.Rc1 Qb7 21.Bb1 Rxc1 22.Qxc1 Rc8 23.Qe3 h6? 24.e5 Nd5?! 25.Qe4 dxe5?? 26.Qh7+ Kf8 27.Qh8#.
- Equal to move 22 (SF: 25.cxd4!, 35.Bxd4!). 21.Bb1 aimed at h7; 25.Qe4 put the queen in front of Bb1: threat Qh7+ Kf8 Qh8#. Be7 (e7) and Rc8 boxed the king; h7 was empty only because of 23...h6. Nd5 blocked Qb7, so ...Qxe4 was impossible. My in-game notes covered Qxe4/Bxe4 and Qxb7 but never 'Qh7+'.
- Fix (unverified): 23...Rc4/...Qb6/...Nd7 instead of h6 (h7 pawn home = battery harmless); at 25 stop Qh7 with 25...g6 or 25...Nf6 (g6 guards h7; Nd5 still guarded by Be6+Qb7). With his Bb1/Bc2 + Q on that diagonal: is h7 guarded twice?

## T20SF2G1 vs Sol (White): DRAW (threefold ply 108; 900+10)
...9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Be3 Bd7 19.Ng3 Na4 20.Qe2 Rfc8 21.Bc2?? Qxc2 22.Qxc2 Rxc2 (bishop up) 23.b3 Nb2 ... 29.Rb1 Nh5?? 30.Nxh5 -> R+B v R+N locked, Bd7/Be8 shuffle, Ke7 holds d6, b5 guarded.
- Setup works: ...a5 first, ...Na6-c5, ...Bd7, ...Na4, ...Rfc8 vs Bc2. SF: 13.Bb3!, 25.cxd4!, 32...Na6!.
- 29...Nh5??: Bd7 does not reach h5 (f7 blocks e8-h5). Up a piece: trade rooks, no baits. Ending dead equal; I varied once at the first repeat, then took the draw.

## T20R3 vs Sol (White): LOST (mate 70). Equal to move 27, then 28...Nxd5??
...14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Ng3 Bd7 19.Be3 Rac8 20.b4 Nb7? 21.Qd2 axb4?! 22.axb4 Ra8 ... 27.Nhf5 Bxf5?! 28.exf5 Nxd5?? 29.Qxd5.
- Qd2 guards d5 down the d-file. 20.b4 hit Nc5 and a5; try 20...axb4 21.axb4 Na6 or 21...Na4. Decide the reply BEFORE ...Rac8. 24-27 passive vs h4-h5 + Nh4-f5: answer with ...Ra4/...f6.

## Main line (Closed Ruy / Chigorin)
...13.cxd4 Nc6, then 14.d5 Nb4 15.Bb1 a5 / 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 (or exd4 as T21R1) / 14.Nf1 Bd7 / 14.Bb1 a5.
RULE: ...a5 BEFORE ...Rfe8/...g6 (frees a6 for Nb4-a6-c5, answers a3).

## T20R2 vs SF 5.O-O Be7 6.d4: LOST (mate 56)
6...exd4 7.Re1 d6 8.Nxd4 Bd7! 9.Nxc6 Bxc6 10.Bxc6+ bxc6 11.h3 O-O 12.Nc3 Re8 13.b3 Nd7 14.Be3 Bf6 15.Qd2 Nc5 ... 22.Rae1 a5 23.e5 dxe5 24.Rxe5 Rxe5 25.Rxe5 Re8?! 26.Qd3! Qxd3 27.Rxe8+.
- Equal to move 22; 19-22 waiting moves, then 23.e5. Better 25...Qd6/Qe6. Try 22...d5!? or ...c5.

## T18R5.2 vs DeepSeek: WON (mate 45)
14.Bb1 a5 15.Qe2 Bd7 16.Nf1 Rac8 17.Ng3 exd4! 18.Nxd4?? Nxd4. d4 had one defender; count d4 every move after c3 is gone.

## Older losses vs Sol
- T18SF2G1G1 (flagged ply 112, pawn up): 14...Rfe8? 15.Be3 g6? 16.d5 c4 ... 34...Bxd5?? 35.Bxb8. ...Rfe8/...g6 came before ...a5; 40-63 s on quiet moves.
- T18R3 (mate 45): 14.Nf1 Bd7 15.Ng3 Rac8 16.Be3 Rfe8? 17.Rc1 g6 18.d5 Nb4? 19.Bb1 Qd8? 20.a3: Nb4 trapped. Instead 18...Nb8/Ne7.
- T17: 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.d5 Nb4 18.Bb1 Rfc8 19.a3 Nc2 20.Bxc2 Qxc2 21.Qxc2 Rxc2 ... 31...Ra7?? 32.Bxa7. Keep rooks.
- Other: T15SF2G1G1 23...Nxd5?? 24.Qxd5; T15R3 DRAW 3 pawns up: vary before the 2nd repetition; T14SF2G1 25...Qxc1??; T7R1 19...Qc4?? 20.Rxc4. Endgame: Q vs b-pawn is lost; stalemate check every ply.
