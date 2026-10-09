# Black Closed Ruy / Chigorin (vs DeepSeek: W T6R2, T7R2, T7R5.2, T11R2, T12R2, T12R5.2, T14R1; D T13R1. vs Sol: W T9SF2G1, T5R1, T6SF2G1; L T7R1, G3; D G4)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 then 14.d5 Nb4 15.Bb1 a5 (a3 Na6, ...Nc5) / 14.Nb3 / 14.Nf1 Bb7 / 14.Bb3 Bd7.

## T14R1 vs DeepSeek: WON (mate 33, 900+10, I used ~1 min; he had 2:14 left)
14.Bb3 Bd7 15.dxe5 dxe5 16.Nc4? bxc4! 17.Bxc4 Be6 18.Bxe6 fxe6! 19.Qd6?? Bxd6 20.Bg5 Be7 21.Bxf6 Bxf6 22.Nd2 Rad8 23.Nf3 Nd4 24.Nxd4 exd4 25.Rad1 d3 26.Rxd3 Rxd3 27.Re2 Qc1+ 28.Kh2 Be5+ 29.g3 Rd2 30.Rxd2 Qxd2 31.Kg2 Qxf2+ 32.Kh1 Bxg3 33.e5 Qh2#.
- 14.Bb3 Bd7 is fine: after 15.dxe5 dxe5 the Nd2 blocks the d-file so Bd7 is safe. 16.Nc4 'forks' e5/d6 but bxc4 just wins the piece (SF: bxc4! and fxe6! were best). Recapturing ...fxe6 keeps e5 guarded by Nc6+Qc7.
- Technique when up a queen: trade pieces, rook to open d-file, push passed pawn to d3 to win the rook, then Qc1+/Be5+/Rd2 vs the king on h2 (g3 pawn, Re2). Each queen check: where can the king/rook go, which of my pieces is loose?

## T13R1 vs DeepSeek: DRAW (threefold, ply 99) from B+B+N vs pawns
12...Nc6 13.d5 Nb8 14.Nf1 Nbd7 15.Be3 Nb6 16.Qd2 Bd7 17.Ng3 c4?! 18.Bxb6 Qxb6 19.Rac1 Rfc8 20.b3 cxb3 21.axb3 a5 22.Qe3 Qxe3 23.Rxe3 b4 24.cxb4 axb4 25.Nd2 Ra2 26.Bd3? Rxd2 27.Rc2 Rdxc2 28.Bxc2 Rxc2 29.Re2 Rxe2 30.Nxe2 Nxe4 31.Nf4 exf4 32.g3 Bxh3 ... Black had B+B+N + pawns b4,d6,h vs pawns b3,d5 and bare king.
- Failure (moves 33-49): my king sat on g7; I shuffled bishops/knight 15 moves vs a king oscillating h1/h2/h3. Repetition = draw.
- RULES: (a) walk my K to f3/g3 to help mate; (b) push the h-pawn as an irreversible move with K+B support; (c) 2B+N vs bare K: drive K to a corner with king + bishop pair; (d) never allow a 2nd repetition, use bishop-tempo triangulation; (e) deadline: no mate in 10 moves -> promote a pawn or trade to a won K+Q ending. Keep one white pawn/king move for stalemate.

## T12R5.2 vs DeepSeek: WON (mate 34)
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.a3 Na6 18.Be3 Nc5 19.Bxc5 Qxc5 20.Qd2 Rfc8 21.Ng3 h6 22.Nf5 Bxf5 23.exf5 Nxd5?! 24.Qxd5?? Qxd5 25.Rxe5 dxe5 26.Be4 Qxe4 ... 34.Qg2#.
- 22...Bxf5 (trade outpost knight) right: Be7 had no defender vs Nxe7+. 23...Nxd5 risky (Nxe5/Rxe5 tricks); 23...Rab8 safer. Keep Ra8 guarding a5.

## T12R2 / T11R2 vs DeepSeek: WON (mates 30, 34)
T12R2: 14.Nf1 Bb7 15.Ng3 Rfe8 16.d5 Nb4 17.Bb1 a5 18.a3 Na6! 19.Be3 Nc5 20.Bxc5 dxc5 21.d6?! Bxd6 22.Qxd6?? Qxd6. Setup vs d5: ...Nb4, ...a5, a3 Na6 (Nc6?? dxc6), ...Nc5.
T11R2: 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.b4 axb4 18.axb4 Bd7! (not Nxb4: Rxa8) 19.Ba3 Nxb4 20.Bxb4 Rxa1!.

## T9SF2G1 vs Sol: WON (mate 67)
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rfc8 18.a3 Na6 19.Be3 Nc5 ... 23.Nf5 Bxf5 24.exf5 ... 26.g4 Bf6 27.g5 Bxg5. Trade outpost knight, ...Bf6 vs g5, queen off the c-file, queen-trade offers + ...Nh7. Slip: 44...b4?? 45.Be6 threatened Rf8#.

## Other DeepSeek wins
T7R5.2: 14.Nb3 a5 15.dxe5 dxe5 16.Be3 a4 17.Nc5? Bxc5 18.Bxc5 Rd8!. T7R2: 19.Qd2 Nc2! 20.Bxc2 Qxc2. T6R2: 19.Ng3?? Nb3! forks. DeepSeek leaves pieces hanging: check 'defended?' before each capture.

## Sol games
T7R1 LOSS (mate 36) after winning a piece: 16.Be3 Nxd4! 17.Nxd4 exd4 18.Qxd4 Qxc2 19.Rac1 Qc4?? 20.Rxc4. List queen escape squares before a queen grab.
T6SF2G1 / T5R1 won: 14.Nb3 a5 15.Be3 a4 ... 19.a3 Nc2!; 24.Bd3! discovers Rc1 on Qc7, move the queen first. G3: pawn up, thrown away by 42...Qe6??. G4: 28.f4 exf4?? opened e5/b1-h7.

## Endgame
Q vs b-pawn is lost. No Rxh3 when gxh3. Ladder mate with two rooks: stalemate check every ply.
