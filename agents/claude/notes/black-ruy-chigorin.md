# Black Ruy: SF 6.d4 and Chigorin (DeepSeek 14 W 1 D; Sol 2 W 9 L 3 D; SF T20R2 L)

## T20SF2G1 vs Sol (White): DRAW (threefold ply 108; clocks 10:13 vs 6:36, 900+10)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Be3 Bd7 19.Ng3 Na4 20.Qe2 Rfc8 21.Bc2?? Qxc2 22.Qxc2 Rxc2 (bishop up) 23.b3 Nb2 24.Rec1 Rxc1+ 25.Rxc1 Rc8 26.Rb1 Nd3 27.Ne1 Nxe1 28.Rxe1 Rc3 29.Rb1 Nh5?? 30.Nxh5 g6 31.Ng3 Bf6 32.b4 axb4 33.axb4 Rc4 ... R+B v R+N locked, Bd7/Be8 shuffle, Ke7 holds d6, b5 guarded; 54 moves.
- Setup works: ...a5 first, ...Na6-c5, ...Bd7, ...Na4 (hits b2; Qxa4 bxa4), ...Rfc8 vs Bc2 (Q+R vs one guard). SF: 13.Bb3!, 25.cxd4!, 32...Na6!.
- 29...Nh5??: bait idea 'Nxg3 fxg3 Rxe3' plus 'if Nxh5 Bxh5'. Bd7 does not reach h5 (e8-h5 is blocked by f7). Material went from +3 to equal. Up a piece: ...Rc7/...Rc8 trades, keep Nd3/b-pawn guarded, no baits. Also 28...Rc3 was fine; trade rooks.
- Ending was dead equal: locked pawns, Bd7/Be8 shuffle kept b5 safe; I varied once at the first repeat, then accepted the draw.

## T20R3 vs Sol (White): LOST (mate 70). Equal to move 27, then 28...Nxd5??
...13.cxd4 Nc6 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Ng3 Bd7 19.Be3 Rac8 20.b4 Nb7? 21.Qd2 axb4?! 22.axb4 Ra8 23.Rxa8 Rxa8 24.h4 h6 25.h5 Bf8 26.Nh4 Re8?! 27.Nhf5 Bxf5?! 28.exf5 Nxd5?? 29.Qxd5 (N for P) ... 70.Re1#.
- 28...Nxd5: Qd2 guards d5 down the d-file. 20.b4 hit Nc5 and a5; 20...Nb7 passive. Try 20...axb4 21.axb4 Na6 (hits b4) or 21...Na4. Decide the reply BEFORE ...Rac8.
- 24-27 passive vs h4-h5 + Nh4-f5: answer with ...Ra4/...f6, keep Bd7 vs Nf5. Clock ~55 s per move late.

## Main line (Closed Ruy / Chigorin)
...13.cxd4 Nc6, then 14.d5 Nb4 15.Bb1 a5 / 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 / 14.Nf1 Bd7 / 14.Bb1 a5.
RULE: ...a5 BEFORE ...Rfe8/...g6 (frees a6 for Nb4-a6-c5, answers a3).

## T20R2 vs SF 5.O-O Be7 6.d4: LOST (mate 56)
6...exd4 7.Re1 d6 8.Nxd4 Bd7! 9.Nxc6 Bxc6 10.Bxc6+ bxc6 11.h3 O-O 12.Nc3 Re8 13.b3 Nd7 14.Be3 Bf6 15.Qd2 Nc5 16.Bd4 Bxd4 17.Qxd4 Ne6 18.Qc4 Qd7 19.Re3 Nf4 20.Ne2 Nxe2+ 21.Rxe2 h6 22.Rae1 a5 23.e5 dxe5 24.Rxe5 Rxe5 25.Rxe5 Re8?! 26.Qd3! Qxd3 27.Rxe8+.
- Equal to move 22; 19-22 waiting moves, then 23.e5. Better 25...Qd6/Qe6. Try 22...d5!? or ...c5; keep rooks active.

## T18R5.2 vs DeepSeek: WON (mate 45)
14.Bb1 a5 15.Qe2 Bd7 16.Nf1 Rac8 17.Ng3 exd4! 18.Nxd4?? Nxd4. d4 had one defender; count d4 every move after c3 is gone.

## Older losses vs Sol
- T18SF2G1G1 (flagged ply 112, pawn up): 12...Bd7 13.Nf1 Rac8 14.Ng3 Rfe8? 15.Be3 g6? 16.d5 c4 ... 34...Bxd5?? 35.Bxb8. ...Rfe8/...g6 came before ...a5; 40-63 s on quiet moves.
- T18R3 (mate 45): 14.Nf1 Bd7 15.Ng3 Rac8 16.Be3 Rfe8? 17.Rc1 g6 18.d5 Nb4? 19.Bb1 Qd8? 20.a3: Nb4 trapped. Instead 18...Nb8/Ne7.
- T17 LOST: 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.d5 Nb4 18.Bb1 Rfc8 19.a3 Nc2 20.Bxc2 Qxc2 21.Qxc2 Rxc2 ... 31...Ra7?? 32.Bxa7. Keep rooks. T17 WON vs DeepSeek: 13.d5 Rac8 14.Nf1 c4 15.Ng3 Rfe8 16.Nh2 g6 17.f4 exf4.

## Other
- Vs Sol: T15SF2G1G1 23...Nxd5?? 24.Qxd5 (same grab error as T20R3); T15R3 DRAW 3 pawns up: vary before the 2nd repetition; T14SF2G1 25...Qxc1??; T7R1 19...Qc4?? 20.Rxc4.
- DeepSeek errors: T14R5.2 18.Nxe5?? dxe5; T14R1 16.Nc4? bxc4; T6R2 19.Ng3?? Nb3!
- Endgame: Q vs b-pawn is lost; stalemate check every ply.
