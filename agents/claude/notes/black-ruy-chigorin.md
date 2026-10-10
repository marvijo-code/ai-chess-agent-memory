# Black Closed Ruy / Chigorin (DeepSeek 12 W 1 D; Sol W T9SF2G1,T5R1,T6SF2G1; L T7R1,G3,T14R3,T14SF2G1,T15SF2G1G1,T17SF2G1; D G4,T15R3)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6, then 14.d5 Nb4 15.Bb1 a5 / 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 / 14.Nf1 Bd7 / 14.Bb3 Bd7.

## T17SF2G1 vs Sol: LOST (mate 44, 900+10)
14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.d5 Nb4 18.Bb1 Rfc8 19.a3 Nc2 20.Bxc2 Qxc2 21.Qxc2 Rxc2 22.Rab1 b4 23.axb4 a3?! (23...Bxb4 ILLEGAL: own d6 blocks e7-b4, cost 1:26) 24.bxa3 Rxa3?! 25.Rec1 Rxc1+ 26.Rxc1 Bd8 27.Nc4 Ra6 28.Nfd2 Bb5 29.f3 Bxc4 30.Rxc4 Be7 31.Kf2 Ra7?? 32.Bxa7 ... 41.Rxd7+ 42.b8=Q 44.Qd8#.
- Equal to move 21 (Nc2 and the queen trade were not marked). 22...b4 had no follow-up: Bxb4 blocked by d6, axb4 simply lost a pawn and made him a passed b-pawn; ...a3/Rxa3 only reduced the damage.
- 31...Ra7: Be3 hits a7 via d4-c5-b6; I checked rooks/knights only. Walk his bishop's diagonals.
- Next time (unverified): 22...Rac8/Rc7 keeping rooks and ...Bf8, keep tension; or 18...Na6 19.a3 Nc5 (T15 line).

## T16R5.2 vs DeepSeek WON (mate 31)
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ne3 a4 18.a3 Na6 19.Nf5 Bxf5 20.exf5 Nc5 21.Bg5 h6 22.Bxf6 Bxf6 23.Rxe5?? dxe5 24.Qd4 exd4 25.Bd3 Nxd3 26.Ne5 Nxe5 27.d6 Qxd6 28.f4 Nd3 29.h4 Qxf4 30.g3 Qxg3+ 31.Kh1 Nf2#.
- SF marked 15...a5, 19...Na6!, 22...Bxf6!. 18.a3 Na6 then ...Nc5 hits d3/e4; Bb1 guards e4. 21...h6: ...Nxd5 loses to Qxd5. After Bxf6 Bxf6, e5 has 3 guards. Nd3 outpost + Qxf4/Qxg3+ = mate.

## T16R2 vs DeepSeek WON (mate 34)
14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.Nf1 Rfe8 18.Ng3 h6 19.d5 Nb4 20.Bb1 Rac8 21.Nf5 Bxf5! 22.exf5 Nbxd5 (d5 hit twice, Qd1 only guard) 23.Qd4?? exd4 ... 33.a3 Qxf2+ 34.Kh3 Qxg2#.
- Conversion: Re2 (Qxf2+/Qxg2# threat); no Rc1+ without a recapture.

## T15R5.2 vs DeepSeek WON (mate 34)
14.d5 Nb4 15.Bb1 a5! 16.Nf1 Bd7 17.Ng3 Rac8 18.Be3 Rfe8 19.Qd2 h6 20.Rd1 Bf8 21.Bxh6?? gxh6! ... Rc2#. Time error: 9:06 on a plain recapture.

## T15SF2G1G1 vs Sol: LOST (mate 61) after winning a pawn
...17.Ng3 Rac8 18.a3 Na6 19.Ba2 Nc5 20.Be3?! Ncxe4! 21.Nxe4 Nxe4 22.Bb1 Nf6 23.Bg5 Nxd5?? 24.Qxd5 ... 61.Qd5#. Be3 blocks Re1 so e4 was weak; 23...Nxd5: Qd1 hit d5 on the open file, knight undefended. Pawn up: don't grab a second.

## T15R3 vs Sol: DRAW threefold THREE PAWNS UP (ply 105)
14.Nf1 Bd7 15.Be3 Rac8 16.d5 Nb4 17.Bb1 a5 18.a3 Nc2! ... 48.Nc4 Nb4+ 49.Kc7 Nxd5+ 50.Kc6 Nb4+. Vary BEFORE the 2nd repetition: ...gxf5/...Ke6/...e4; trade knights into K+P.

## Other Sol losses
- T14SF2G1: ...23.b4 axb3 e.p. 24.Nxb3 Nxb3 25.Bxb3 Qxc1?? 26.Bxc1 Rxc1 27.Qxc1. Qxc1 only if c1 has ONE defender.
- T14R3: ...19.Be3 Rac8 20.Nf5 Bxf5 21.exf5 Rfe8 22.Ba2 h6 23.Rc1 Kh8?? 24.Qe2 Bd8?? 25.Qxb5. Bxf5 removed b5's only guard; use 20...Bf8/Qb7/b4.
- T7R1: 19...Qc4?? 20.Rxc4. G3: pawn up, thrown away by 42...Qe6??. G4: 28.f4 exf4?? opened e5/b1-h7.

## Wins/draw vs DeepSeek and Sol
T14R5.2: 15...a5! 16.Nb3 a4 17.Nbd2 Bd7 18.Nxe5?? dxe5! T14R1: 16.Nc4? bxc4! T13R1 DRAW (B+B+N vs pawns): walk K, push h-pawn, never allow a 2nd repetition. T12R2: 18.a3 Na6! (Nc6?? dxc6). T11R2: 16.a3 Na6 17.b4 axb4 18.axb4 Bd7!. T6R2: 19.Ng3?? Nb3! forks. T9SF2G1 vs Sol: 14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7, trade outpost knight, ...Bf6 vs g5, queen off c-file.

## Endgame
Q vs b-pawn is lost. No Rxh3 when gxh3. Stalemate check every ply.
