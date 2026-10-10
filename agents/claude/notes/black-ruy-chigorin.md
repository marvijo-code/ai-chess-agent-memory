# Black Closed Ruy / Chigorin (DeepSeek 11 W 1 D; Sol W T9SF2G1,T5R1,T6SF2G1; L T7R1,G3,T14R3,T14SF2G1,T15SF2G1G1; D G4,T15R3)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 then 14.d5 Nb4 15.Bb1 a5 (a3 Na6, ...Nc5) / 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 / 14.Nf1 Bd7 / 14.Bb3 Bd7.

## T16R5.2 vs DeepSeek: WON (mate 31, 900+10, 7:50 left of 15:00)
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ne3 a4 18.a3 Na6 19.Nf5 Bxf5 20.exf5 Nc5 21.Bg5 h6 22.Bxf6 Bxf6 23.Rxe5?? dxe5 24.Qd4 exd4 25.Bd3 Nxd3 26.Ne5 Nxe5 27.d6 Qxd6 28.f4 Nd3 29.h4 Qxf4 30.g3 Qxg3+ 31.Kh1 Nf2#.
- SF marked 15...a5, 19...Na6!, 22...Bxf6! (my moves). 18.a3 Na6 (knight b4 attacked, a6 safe) then ...Nc5 hits d3/e4; Bb1 guards e4 so no ...Nxe4.
- 21...h6: ...Nxd5 loses to Qxd5 (d5 guarded by Qd1). After Bxf6 Bxf6, e5 is guarded by Bf6+Qc7+d6, so 23.Rxe5 just lost the rook.
- Conversion: after each odd move list captures (Qd4 en prise to e5, Bd3 hanging, Ne5 trade), keep the Nd3 outpost, then Qxf4/Qxg3+ with Nd3 covering f2 = mate. Check his checks before Qxf4 (none: only Rook-less Qd1 gone).
- Time: 21...h6 took 3:23, other moves 4-90 s. Fine; ~1 min for the Bxf5 decision is the right size.

## T16R2 vs DeepSeek: WON (mate 34, 900+10)
14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.Nf1 Rfe8 18.Ng3 h6 19.d5 Nb4 20.Bb1 Rac8 21.Nf5 Bxf5! 22.exf5 Nbxd5 23.Qd4?? exd4 24.Nxd4 Nxe3 25.Rxe3 Qb6 26.Rxe7 Rxe7 27.Nf3 Re2 28.Ne1 Rxe1+ 29.Kh2 Rcc1 30.Kg3 Rxb1 31.Rxb1 Rxb1 32.h4 Rxb2 33.a3 Qxf2+ 34.Kh3 Qxg2#.
- 21.Nf5 Bxf5 22.exf5: d5 attacked by Nb4 + Nf6, guarded by Qd1 only -> Nbxd5. Checked Bxh6 gxh6 and Qxd5 Nxd5 first.
- Conversion: Re2 (Qxf2+/Qxg2# threat), Rcc1 doubles on Bb1, Qxf2+ protected by Rb2. Do not Rc1+ when no recapture follows.

## T15R5.2 vs DeepSeek: WON (mate 34)
14.d5 Nb4 15.Bb1 a5! 16.Nf1 Bd7 17.Ng3 Rac8 18.Be3 Rfe8 19.Qd2 h6 20.Rd1 Bf8 21.Bxh6?? gxh6! 22.Qxh6 Bxh6 23.Nh5 Nxh5 ... 34...Rc2#. TIME ERROR: 21...gxh6 took 9:06 for a plain recapture.

## T15SF2G1G1 vs Sol: LOST (mate 61) after winning a pawn
...17.Ng3 Rac8 18.a3 Na6 19.Ba2 Nc5 20.Be3?! Ncxe4! 21.Nxe4 Nxe4 22.Bb1 Nf6 23.Bg5 Nxd5?? 24.Qxd5 Bxg5 25.Nxg5 h6 ... 61.Qd5#.
- 20...Ncxe4: e4 attacked once, defended twice; Be3 blocks Re1. 23...Nxd5??: d5 hit by Qd1 down the open d-file, knight had NO defender. Better 23...Bxg5/Nd7/Be8. Pawn up: do not grab a second.

## T15R3 vs Sol: DRAW by repetition THREE PAWNS UP (ply 105)
14.Nf1 Bd7 15.Be3 Rac8 16.d5 Nb4 17.Bb1 a5 18.a3 Nc2! 19.Bxc2 Qxc2 ... 48.Nc4 Nb4+ 49.Kc7 Nxd5+ 50.Kc6 Nb4+ ... threefold.
- N+5P v N+2P; I repeated checks. Better ...gxf5 / ...Ke6 / ...e4; trade knights into K+P. Vary BEFORE the 2nd repetition.

## T14SF2G1 vs Sol: LOST (mate 45): Q for R+B at move 25
...23.b4 axb3 e.p. 24.Nxb3 Nxb3 25.Bxb3 Qxc1?? 26.Bxc1 Rxc1 27.Qxc1. Qxc1 only if c1 has ONE defender.

## T14R3 vs Sol: LOST (mate 52)
...19.Be3 Rac8 20.Nf5 Bxf5 21.exf5 Rfe8 22.Ba2 h6 23.Rc1 Kh8?? 24.Qe2 Bd8?? 25.Qxb5. 20...Bxf5 removed the ONLY guard of b5 (no Nb4 trick here). Fix: 20...Bf8 or ...Qb7/...b4.

## DeepSeek wins/draw
T14R5.2: 15...a5! 16.Nb3 a4 17.Nbd2 Bd7 18.Nxe5?? dxe5! 19.d6 Bxd6. T14R1: 14.Bb3 Bd7 15.dxe5 dxe5 16.Nc4? bxc4! ... Qh2#. T13R1 DRAW (B+B+N vs pawns): walk K, push h-pawn, never allow 2nd repetition. T12R2: 18.a3 Na6! (Nc6?? dxc6). T11R2: 16.a3 Na6 17.b4 axb4 18.axb4 Bd7! T6R2: 19.Ng3?? Nb3! forks.

## Sol wins/losses
T9SF2G1 WON: 14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 ... trade outpost knight, ...Bf6 vs g5, queen off c-file. T7R1 LOST after winning a piece: 19...Qc4?? 20.Rxc4. G3: pawn up, thrown away by 42...Qe6??. G4: 28.f4 exf4?? opened e5/b1-h7.

## Endgame
Q vs b-pawn is lost. No Rxh3 when gxh3. Stalemate check every ply.
