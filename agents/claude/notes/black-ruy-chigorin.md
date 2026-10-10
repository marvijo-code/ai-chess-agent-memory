# Black Closed Ruy / Chigorin (DeepSeek 13 W 1 D; Sol W T9SF2G1,T5R1,T6SF2G1; L T7R1,G3,T14R3,T14SF2G1,T15SF2G1G1,T17SF2G1,T18R3,T18SF2G1G1(flag); D G4,T15R3)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 (or 12...Bd7), then 14.d5 Nb4 15.Bb1 a5 / 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 / 14.Nf1 Bd7 / 14.Bb3 Bd7.
RULE: ...a5 BEFORE ...Rfe8/...g6. It frees a6 for Nb4-a6-c5 and answers a3.

## T18SF2G1G1 vs Sol: LOST ON TIME (ply 112, 900+10), pawn up
12...Bd7 13.Nf1 Rac8 14.Ng3 Rfe8? 15.Be3 g6? 16.d5 c4 17.a4 bxa4 18.Bxa4 Bb5 19.Bc2 Rb8 20.Ra2 Nb7 21.b3 cxb3 22.Bxb3 Qxc3 23.Bc2 Nc5 24.Qd2 Qxd2 25.Bxd2 Rbc8 26.Nh2 h6?! 27.f4 exf4 28.Bxf4 Kg7 29.Nf3 Bc4 30.Rb2 Rb8 31.Rxb8 Rxb8 32.Nd4 Bf8 33.e5 dxe5? 34.Bxe5 Bxd5?? 35.Bxb8 (exchange) ... 56.Kf4, I had 10 s.
- Opening fine: 17.a4 bxa4, 21...cxb3, 24...Qxd2, 31...Rxb8 marked best (pawn up at move 22). Still ...Rfe8?/...g6? came before ...a5.
- 33.e5: ...dxe5 let Be5 hit Rb8 along f4-e5-d6-c7-b8 (d6 had screened it) and Nd4. 34...Bxd5 ignored it although my own reasoning said 'with tempo against the b8 rook'. Instead (unverified): 33...Ne8/...Nfd7, or 34...Rb7/...Rd8 first, THEN take d5.
- Clock: 13:00 at move 23 vs his 14:00; then 40-63 s on quiet moves 25-34 (...Rbc8, ...h6, ...exf4, ...Bf8) -> 5:37 at move 35, 1:00 at move 50. Four extra pawns were useless without time. Follow the budget in MEMORY.md.

## T18R3 vs Sol: LOST (mate 45): Nb4 trapped
14.Nf1 Bd7 15.Ng3 Rac8 16.Be3 Rfe8? 17.Rc1 g6 18.d5 Nb4? 19.Bb1 Qd8? 20.a3 Nbxd5 21.exd5 Nxd5 22.Bd2 Rxc1 23.Bxc1 Bf6 24.Qxd5 ... 38...Qc6?? 39.Ne7+ forked K+Q+R.
- After a3 Nb4 had no square: a6 (my own pawn), c6 (dxc6), c2/d3 (Bb1), a2. Instead: 18...Nb8 (...Nbd7) or 18...Ne7. List ALL knight checks (e7 f6 c7 b6 f4 e3) before K/Q moves.

## T17 5.2 vs DeepSeek: WON (mate 40)
12...Bd7 13.d5 Rac8 14.Nf1 c4 15.Ng3 Rfe8 16.Nh2 g6 17.f4 exf4 18.Bxf4 Nb7 19.Be3 Nc5 20.Bxc5 Qxc5+ 21.Kh1 Kg7 22.Qd2 a5 23.Ngf1 b4 ... 28.Qh6+?? Kxh6 ... 40.gxf4 Qg2#. Plan vs 13.d5: ...Rac8, ...c4, ...Rfe8, ...g6, ...Nb7-c5.

## T17SF2G1 vs Sol: LOST (mate 44)
14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.d5 Nb4 18.Bb1 Rfc8 19.a3 Nc2 20.Bxc2 Qxc2 21.Qxc2 Rxc2 22.Rab1 b4 23.axb4 a3?! (23...Bxb4 illegal: own d6) ... 31...Ra7?? 32.Bxa7. Equal to move 21; next: keep rooks (22...Rac8/Rc7).

## DeepSeek wins (short)
- T16R5.2/T16R2/T15R5.2: 14.d5 Nb4 15.Bb1 a5! 16.Nf1 Bd7; or 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7, then Nd3 outposts, Nbxd5, Qxf2+. T14R5.2 18.Nxe5?? dxe5. T14R1 16.Nc4? bxc4. T12R2 18.a3 Na6!. T6R2 19.Ng3?? Nb3!

## Sol games (L/D)
- T15SF2G1G1 (L 61, pawn up): 18.a3 Na6 19.Ba2 Nc5 20.Be3?! Ncxe4! 21.Nxe4 Nxe4 22.Bb1 Nf6 23.Bg5 Nxd5?? 24.Qxd5. Don't grab a second pawn.
- T15R3 DRAW, THREE PAWNS UP (ply 105): Nb4+/Nxd5+ shuffle. Vary BEFORE the 2nd repetition; trade into K+P.
- T14SF2G1: 23.b4 axb3 e.p. 24.Nxb3 Nxb3 25.Bxb3 Qxc1?? T14R3: 20.Nf5 Bxf5 21.exf5 removed b5's only guard. T7R1: 19...Qc4?? 20.Rxc4. G3: pawn up, lost by 42...Qe6??. G4: 28.f4 exf4?? opened e5/b1-h7. T9SF2G1: trade outpost knight, ...Bf6 vs g5.

## Endgame
Q vs b-pawn is lost. No Rxh3 when gxh3. Stalemate check every ply.
