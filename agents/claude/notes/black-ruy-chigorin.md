# Black Closed Ruy / Chigorin (DeepSeek: W T6R2,T7R2,T7R5.2,T11R2,T12R2,T12R5.2,T14R1,T14R5.2; D T13R1. Sol: W T9SF2G1,T5R1,T6SF2G1; L T7R1,G3,T14R3,T14SF2G1; D G4)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 then 14.d5 Nb4 15.Bb1 a5 (a3 Na6, ...Nc5) / 14.Nb3 / 14.Nf1 Bb7 / 14.Bb3 Bd7.

## T14R5.2 vs DeepSeek: WON (mate 30, 900+10, used ~2 of 15 min)
14.d5 Nb4 15.Bb1 a5! 16.Nb3 a4 17.Nbd2 Bd7 18.Nxe5?? dxe5! 19.d6 Bxd6 (d6 unguarded, hit Qc7+Be7) 20.Nf3 Rac8 21.Qxa4?? bxa4 22.Be3 Nc2 23.Bxc2 Qxc2 24.Nd4 exd4 25.Bxd4 Nxe4 26.Be3 Qxb2 27.f3 Nc3 28.Re2 Nxe2+ 29.Kh1 Qxa1+ 30.Bg1 Qxg1#.
- ...a5/...a4 kicks Nb3, ...Bd7, Rac8 behind Qc7. Before 18...dxe5 I checked Qxa4, Ba3, Qg4: do that for every 'free' piece.
- Conversion: each capture removed an attacker or forked (Nc2 hit Be3+rooks, Nxe2+ then Qxa1+); Bd4 guarded by nothing so Qxb2 not Qxd4. Always list his checks.

## T14SF2G1 vs Sol: LOST (mate 45): Q for R+B at move 25
14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Ng3 Bd7 19.Ba2 a4 20.Be3 Rfc8 21.Rc1 h6 22.Nd2 Rab8 23.b4 axb3 e.p. 24.Nxb3 Nxb3 25.Bxb3 Qxc1?? 26.Bxc1 Rxc1 27.Qxc1 (-6) ... 32.Nh5 Nxh5 33.Qxd7 ... 43...f6 44.Bd3 Kh8 45.Qh7#.
- Equal to move 24. Problem: c-file line Rc1 / Nc5 (front) / Qc7 / Rc8. 24...Nxb3 uncovered Rc1 on Qc7; Qxc1 Bxc1 (Be3 + Qd1 guard c1). SF marks BOTH 24...Nxb3?? and 25.Bxb3??; I never listed my options after 25.Bxb3.
- Fix: at 21-23 move the queen off the c-file (...Qb6/...Qd8) or settle Nc5. After 25.Bxb3: 25...Qd8/Qb6; Qxc1 only if c1 has ONE defender.
- Down Q: keep a defender for h7 (Bg7/Rh8), not ...f6. 28...Bc5 illegal: own pawn d6 blocked.

## T14R3 vs Sol: LOST (mate 52): b5 pawn, d6, fork
...17.Nf1 Nc5 18.Ng3 Bd7 19.Be3 Rac8 20.Nf5 Bxf5 21.exf5 Rfe8 22.Ba2 h6 23.Rc1 Kh8?? 24.Qe2 Bd8?? 25.Qxb5 Qb6 26.Qxb6 Bxb6 27.Red1 Rc7? 28.Nd2 Rec8 29.Nc4 Ba7 30.Nxd6 Rd8 31.Nb5 forks Rc7+Ba7.
- 20...Bxf5 removed Bd7, the ONLY guard of b5; 21-24 were waiting moves. Fix: 21...Qb7/...Rb8/...b4 or 20...Bf8. List knight forks before placing two pieces on c7/a7/d6.

## T14R1 vs DeepSeek: WON (mate 33)
14.Bb3 Bd7 15.dxe5 dxe5 16.Nc4? bxc4! 17.Bxc4 Be6 18.Bxe6 fxe6! 19.Qd6?? Bxd6 20.Bg5 Be7 ... Qh2#.

## T13R1 vs DeepSeek: DRAW (threefold) with B+B+N vs pawns
I shuffled 15 moves. Walk K to f3/g3; push h-pawn with K+B support; never allow a 2nd repetition; promote or trade to won K+Q. Keep a spare move for stalemate.

## DeepSeek wins
T12R5.2: 14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.a3 Na6 18.Be3 Nc5 19.Bxc5 Qxc5 20.Qd2 Rfc8: keep Ra8 guarding a5.
T12R2: 14.Nf1 Bb7 15.Ng3 Rfe8 16.d5 Nb4 17.Bb1 a5 18.a3 Na6! (Nc6?? dxc6) 19.Be3 Nc5.
T11R2: 16.a3 Na6 17.b4 axb4 18.axb4 Bd7! (not Nxb4: Rxa8) 19.Ba3 Nxb4 20.Bxb4 Rxa1!.
T7R5.2: 14.Nb3 a5 15.dxe5 dxe5 16.Be3 a4 17.Nc5? Bxc5. T7R2: 19.Qd2 Nc2!. T6R2: 19.Ng3?? Nb3! forks.

## Sol wins/losses
T9SF2G1 WON (mate 67): 14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rfc8 18.a3 Na6 19.Be3 Nc5 ... 23.Nf5 Bxf5 24.exf5 ... 26.g4 Bf6 27.g5 Bxg5. Trade outpost knight, ...Bf6 vs g5, queen off c-file, ...Nh7.
T7R1 LOST after winning a piece: 19...Qc4?? 20.Rxc4. List queen escape squares before a queen grab.
T6SF2G1/T5R1 won: 14.Nb3 a5 15.Be3 a4 ... 19.a3 Nc2!. G3: pawn up, thrown away by 42...Qe6??. G4: 28.f4 exf4?? opened e5/b1-h7.

## Endgame
Q vs b-pawn is lost. No Rxh3 when gxh3. Two-rook ladder mate: stalemate check every ply.
