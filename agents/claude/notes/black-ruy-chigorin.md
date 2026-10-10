# Black Closed Ruy / Chigorin (DeepSeek 13 W 1 D; Sol W T9SF2G1,T5R1,T6SF2G1; L T7R1,G3,T14R3,T14SF2G1,T15SF2G1G1,T17SF2G1; D G4,T15R3)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 (or 12...Bd7), then 14.d5 Nb4 15.Bb1 a5 / 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 / 14.Nf1 Bd7 / 14.Bb3 Bd7.

## T17 5.2 vs DeepSeek: WON (mate 40, 900+10, 11:08 left)
12...Bd7 13.d5 Rac8 14.Nf1 c4 15.Ng3 Rfe8 16.Nh2 g6 17.f4 exf4 18.Bxf4 Nb7 19.Be3 Nc5 20.Bxc5 Qxc5+ 21.Kh1 Kg7 22.Qd2 a5 23.Ngf1 b4 24.Ne3 Bb5 25.Nf5+ gxf5 26.exf5 Nxd5 27.f6+ Bxf6 28.Qh6+?? Kxh6 29.Ng4+ Kg7 ... Rxe1+ trades ... 33...Ne3 34.Be4 bxc3 35...Nd5 (Qf2 illegal: own Ne3) 36.Ng5 Bxg5 37.Bxd5 Qxd5 38.Kh2 Bf4+ 39.g3 Bc6 40.gxf4 Qg2#.
- Plan vs 13.d5: ...Rac8, ...c4 clamp, ...Rfe8, ...g6 (kills Nf5), ...Nb7-c5 to trade his Be3 for the knight. 22...a5/23...b4 worked (Be7 cannot take b4: d6 blocks; Qc5 guards it).
- SF marks: 17...exf4?!, 21...Kg7?!, 24...Bb5?!, 25...gxf5!, 26...Nxd5? (unclear better), 27...Bxf6?!. Nf5+ was an unsound sac; after it I won a piece, took d5 after counting f6+/Rxe7.
- DeepSeek used ~45 s a move and still dropped the queen. Conversion: trade rooks, keep pieces guarded, mate with Q+B on g2.

## T17SF2G1 vs Sol: LOST (mate 44, 900+10)
14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.d5 Nb4 18.Bb1 Rfc8 19.a3 Nc2 20.Bxc2 Qxc2 21.Qxc2 Rxc2 22.Rab1 b4 23.axb4 a3?! (23...Bxb4 ILLEGAL: own d6) 24.bxa3 Rxa3 ... 31.Kf2 Ra7?? 32.Bxa7 ... 44.Qd8#.
- Equal to move 21. 22...b4 had no follow-up; 31...Ra7: Be3 hits a7 via d4-c5-b6. Walk his bishop's diagonals.
- Next time (unverified): 22...Rac8/Rc7 keeping rooks and ...Bf8, keep tension; or 18...Na6 19.a3 Nc5 (T15 line).

## DeepSeek wins (short)
- T16R5.2: 14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ne3 a4 18.a3 Na6 19.Nf5 Bxf5 20.exf5 Nc5 21.Bg5 h6 22.Bxf6 Bxf6 ... Nd3 outpost + Qxf4/Qxg3+, Nf2#.
- T16R2: 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.Nf1 Rfe8 18.Ng3 h6 19.d5 Nb4 20.Bb1 Rac8 21.Nf5 Bxf5 22.exf5 Nbxd5; Re2 + Qxf2+/Qxg2#.
- T15R5.2: 14.d5 Nb4 15.Bb1 a5! 16.Nf1 Bd7 17.Ng3 Rac8 18.Be3 Rfe8 ... 21.Bxh6?? gxh6. T14R5.2: 18.Nxe5?? dxe5. T14R1: 16.Nc4? bxc4!. T12R2: 18.a3 Na6!. T6R2: 19.Ng3?? Nb3! forks.

## Sol games (L/D)
- T15SF2G1G1 (L 61, after winning a pawn): 18.a3 Na6 19.Ba2 Nc5 20.Be3?! Ncxe4! 21.Nxe4 Nxe4 22.Bb1 Nf6 23.Bg5 Nxd5?? 24.Qxd5. Be3 blocks Re1; pawn up: don't grab a second.
- T15R3 DRAW, THREE PAWNS UP (ply 105): 14.Nf1 Bd7 15.Be3 Rac8 16.d5 Nb4 17.Bb1 a5 18.a3 Nc2! ... Nb4+/Nxd5+ shuffle. Vary BEFORE the 2nd repetition (...gxf5/...Ke6/...e4); trade into K+P.
- T14SF2G1: 23.b4 axb3 e.p. 24.Nxb3 Nxb3 25.Bxb3 Qxc1?? Qxc1 only if c1 has ONE defender. T14R3: 20.Nf5 Bxf5 21.exf5 ... Bxf5 removed b5's only guard (use 20...Bf8/Qb7/b4). T7R1: 19...Qc4?? 20.Rxc4. G3: pawn up, thrown away by 42...Qe6??. G4: 28.f4 exf4?? opened e5/b1-h7. T13R1 DRAW (B+B+N vs pawns): walk K, push h-pawn, never allow a 2nd repetition. T9SF2G1: trade outpost knight, ...Bf6 vs g5, queen off c-file.

## Endgame
Q vs b-pawn is lost. No Rxh3 when gxh3. Stalemate check every ply.
