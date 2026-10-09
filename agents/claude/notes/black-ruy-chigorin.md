# Black Closed Ruy / Chigorin (vs Sol: W T9SF2G1, T5R1, T6SF2G1; L T7R1, G3; D G4; vs DeepSeek: W T6R2, T7R2, T7R5.2, T11R2, T12R2, T12R5.2; D T13R1)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 then 14.d5 Nb4 15.Bb1 a5 (a3 Na6, ...Nc5) / 14.Nb3 / 14.Nf1 Bb7.

## T13R1 vs DeepSeek: DRAW (threefold, ply 99) from B+B+N vs pawns
12...Nc6 13.d5 Nb8 14.Nf1 Nbd7 15.Be3 Nb6 16.Qd2 Bd7 17.Ng3 c4?! 18.Bxb6 Qxb6 19.Rac1 Rfc8 20.b3 cxb3 21.axb3 a5 22.Qe3 Qxe3 23.Rxe3 b4 24.cxb4 axb4 25.Nd2 Ra2 26.Bd3? Rxd2 27.Rc2 Rdxc2 28.Bxc2 Rxc2 29.Re2 Rxe2 30.Nxe2 Nxe4 31.Nf4 exf4 32.g3 Bxh3 ... Black: B+B+N + pawns b4,d6,h-pawn vs White pawns b3,d5 and bare king.
- Opening/middlegame fine: 13.d5 Nb8 -> Nbd7-b6, ...Bd7, ...c4, ...Rfc8, ...a5/b4 (22...Qxe3 was forced trade: Qb6 hung to Qe3, don't miss it). 25...Ra2 hit Bc2+Nd2.
- THE FAILURE (moves 33-49): my king stayed on g7 all game; I shuffled bishops (Bf2, Be1, Bg4, Bf3) and knight (Nf3, Nh4, Nf5) for 15 moves building a 'mating net' on a king oscillating h1/h2/h3 (his pawns b3/d5 blocked, so only king moves). Repetition on h2/h1 with my Nh4/Bg4 returning = draw. Spent 1 min a move on shuffles, but no plan.
- RULES for such endings: (a) walk my K to f3/g3 area (his king on h-file, my K helps mate); (b) push my h-pawn (h4-h3) as an irreversible move with K+B support, or win b3/d5 with the bishop ONLY when his king still has squares; (c) with 2B+N vs bare K a standard mate exists: drive the K to a corner with king + bishop pair; (d) keep a written list of positions with side to move, never allow a 2nd repetition; use a tempo-losing triangulation (bishop moves along a diagonal) to change who is to move; (e) set a deadline: no mate in 10 moves -> promote the h-/b-pawn or trade down to a won K+Q ending. Stalemate: keep one white pawn move or king move.

## T12R5.2 vs DeepSeek: WON (mate 34, 900+10, ~2 min used)
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.a3 Na6 18.Be3 Nc5 19.Bxc5 Qxc5 20.Qd2 Rfc8 21.Ng3 h6 22.Nf5 Bxf5 23.exf5 Nxd5?! 24.Qxd5?? Qxd5 (f5 pawn blocks Bb1) 25.Rxe5 dxe5 26.Be4 Qxe4 ... 32...Rc2+ 33.Kf1 Qh3+ 34.Kg1 Qg2#.
- 22...Bxf5 (trade outpost knight) was right: Be7 had no defender vs Nxe7+. 23...Nxd5 marked ??: check Nxe5/Rxe5 tricks; alternatives 23...Rab8. Keep Ra8 guarding a5 while Rc8 is out.

## T12R2 vs DeepSeek: WON (mate 30)
14.Nf1 Bb7 15.Ng3 Rfe8 16.d5 Nb4 17.Bb1 a5 18.a3 Na6! 19.Be3 Nc5 20.Bxc5 dxc5 21.d6?! Bxd6 22.Qxd6?? Qxd6 ... Qf2#.
- Setup vs d5: ...Nb4, ...a5, a3 Na6 (Nc6?? dxc6), ...Nc5 guarded by d6/Qc7/Be7. After 22.Qxd6 Qxd6 he has no recapture; check Bb1 blocking Ra1.

## T11R2 vs DeepSeek: WON (mate 34)
14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.b4 axb4 18.axb4 Bd7! 19.Ba3 Nxb4 20.Bxb4 Rxa1! ... 18...Nxb4? allows Rxa8 so 18...Bd7 first.

## T9SF2G1 vs Sol: WON (mate 67)
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rfc8 18.a3 Na6 19.Be3 Nc5 20.Bc2 a4 ... 23.Nf5 Bxf5 24.exf5 ... 26.g4 Bf6 27.g5 Bxg5.
- Good: trade the outpost knight, ...Bf6 vs g5, queen off the c-file, queen-trade offers + ...Nh7 killed the storm. Slip: 44...b4?? 45.Be6 threatened Rf8#; keep Nd7 guarding f8.

## Other DeepSeek wins
T7R5.2: 14.Nb3 a5 15.dxe5 dxe5 16.Be3 a4 17.Nc5? Bxc5 18.Bxc5 Rd8! T7R2: 19.Qd2 Nc2! 20.Bxc2 Qxc2. T6R2: 19.Ng3?? Nb3! forks. DeepSeek leaves pieces hanging: check 'defended?' before each capture.

## T7R1 vs Sol: LOSS (mate 36) after winning a piece
16.Be3 Nxd4! 17.Nxd4 exd4 18.Qxd4 Qxc2 19.Rac1 Qc4?? 20.Rxc4. List queen escape squares before a queen grab.

## T6SF2G1 / T5R1 vs Sol (won); G3 / G4
SF2G1: 14.Nb3 a5 15.Be3 a4 ... 19.a3 Nc2! (31...Bxc5 ILLEGAL: d6 blocks). T5R1: 24.Bd3! discovers Rc1 on Qc7; move the queen first. G3: pawn up, thrown away by 42...Qe6??. G4: 28.f4 exf4?? opened e5/b1-h7.

## Endgame
Q vs b-pawn is lost. No Rxh3 when gxh3. Ladder mate with two rooks: stalemate check every ply.
