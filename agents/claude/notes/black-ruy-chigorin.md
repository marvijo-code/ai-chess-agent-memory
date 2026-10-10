# Black Closed Ruy / Chigorin (DeepSeek 9 W 1 D; Sol W T9SF2G1,T5R1,T6SF2G1; L T7R1,G3,T14R3,T14SF2G1,T15SF2G1G1; D G4,T15R3)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 then 14.d5 Nb4 15.Bb1 a5 (a3 Na6, ...Nc5) / 14.Nb3 / 14.Nf1 Bd7 / 14.Bb3 Bd7.

## T15R5.2 vs DeepSeek: WON (mate 34, 900+10)
14.d5 Nb4 15.Bb1 a5! 16.Nf1 Bd7 17.Ng3 Rac8 18.Be3 Rfe8 19.Qd2 h6 20.Rd1 Bf8 21.Bxh6?? gxh6! 22.Qxh6 Bxh6 23.Nh5 Nxh5 24.Rd2 Bxd2 ... 31.Ne3 Qxa1 ... 34...Rc2#.
- Quiet setup (Rfe8, h6, Bf8 guarding h6/g7, Nb4 held by a5) was enough; DeepSeek sacked a bishop for a pawn, then gave up Q+R.
- TIME ERROR: 21...gxh6 took 9:06 (12:46 -> 3:50) for a plain recapture. For a hanging piece check his checks/follow-ups (Qxh6 Bxh6, Nh5) in <60 s, then take.
- Conversion went fine: Nf4 hit h3/g2, Qc1+ (Ra1 blocked by Bb1), Qxb2/Qxa1, Rc2#. Stalemate/mate checks each ply.

## T15SF2G1G1 vs Sol: LOST (mate 61) after winning a pawn
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rac8 18.a3 Na6 19.Ba2 Nc5 20.Be3?! Ncxe4! 21.Nxe4 Nxe4 22.Bb1 Nf6 23.Bg5 Nxd5?? 24.Qxd5 Bxg5 25.Nxg5 h6 ... 61.Qd5#.
- 20...Ncxe4: e4 attacked once (Ng3), defended twice; Be3 blocks Re1. Repeat vs Be3.
- 23...Nxd5??: d5 hit by Qd1 down the open d-file, knight had NO defender. I checked only Bxe7 Nxe7. Better: 23...Bxg5 24.Nxg5 h6, 23...Nd7, 23...Be8. Pawn up and equal: do not grab a second pawn.

## T15R3 vs Sol: DRAW by repetition THREE PAWNS UP (ply 105)
14.Nf1 Bd7 15.Be3 Rac8 16.d5 Nb4 17.Bb1 a5 18.a3 Nc2! 19.Bxc2 Qxc2 20.Qxc2 Rxc2 ... 37.a4? bxa4 ... 48.Nc4 Nb4+ 49.Kc7 Nxd5+ 50.Kc6 Nb4+ 51.Kc7 Nd5+ 52.Kc6 Nb4+ 53.Kc7 threefold.
- 18...Nc2 equalizes (queens and rooks off). Sol self-destructed.
- THE MISS: N+5P v N+2P; 50.Kc6 hit Nd5 and I repeated checks. Even losing d6 leaves +2 with a passed e-pawn. Better: ...gxf5 / ...Ke6 / ...e4; trade knights into K+P. Vary BEFORE the 2nd repetition.

## T14SF2G1 vs Sol: LOST (mate 45): Q for R+B at move 25
...20.Be3 Rfc8 21.Rc1 h6 22.Nd2 Rab8 23.b4 axb3 e.p. 24.Nxb3 Nxb3 25.Bxb3 Qxc1?? 26.Bxc1 Rxc1 27.Qxc1. 24...Nxb3 uncovered Rc1 on Qc7. Queen off the c-file at 21-23; Qxc1 only if c1 has ONE defender.

## T14R3 vs Sol: LOST (mate 52)
...19.Be3 Rac8 20.Nf5 Bxf5 21.exf5 Rfe8 22.Ba2 h6 23.Rc1 Kh8?? 24.Qe2 Bd8?? 25.Qxb5. 20...Bxf5 removed the ONLY guard of b5. Fix: 20...Bf8 or ...Qb7/...b4.

## DeepSeek wins/draw
T14R5.2: 15...a5! 16.Nb3 a4 17.Nbd2 Bd7 18.Nxe5?? dxe5! 19.d6 Bxd6; ...a5/...a4 kicks Nb3, Rac8 behind Qc7. T14R1: 14.Bb3 Bd7 15.dxe5 dxe5 16.Nc4? bxc4! ... Qh2#. T13R1 DRAW (B+B+N vs pawns): walk K, push h-pawn, never allow 2nd repetition. T12R5.2: 19.Bxc5 Qxc5, Ra8 guards a5. T12R2: 18.a3 Na6! (Nc6?? dxc6). T11R2: 16.a3 Na6 17.b4 axb4 18.axb4 Bd7! (not Nxb4: Rxa8). T6R2: 19.Ng3?? Nb3! forks.

## Sol wins/losses
T9SF2G1 WON: 14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 ... trade outpost knight, ...Bf6 vs g5, queen off c-file, ...Nh7. T7R1 LOST after winning a piece: 19...Qc4?? 20.Rxc4. G3: pawn up, thrown away by 42...Qe6??. G4: 28.f4 exf4?? opened e5/b1-h7.

## Endgame
Q vs b-pawn is lost. No Rxh3 when gxh3. Stalemate check every ply.
