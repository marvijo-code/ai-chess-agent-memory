# Sicilian as Black - Alapin/Dragon (g28-g95)

## g95 vs Stockfish19 (0-1, Qe8# m28) - Q stays on attacked d5 because 'defended'
1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.Nf3 Nc6 5.d4 cxd4 6.cxd4 Nf6?! 7.Nc3! e6?? 8.Nxd5! exd5 9.Bb5 +8.85; 24.Rxe8+ Bf8 25.Qe1 Bg6 26.Rxf8+ Kxf8 27.Bb4+ Kg8 28.Qe8#.
- 6...Nf6?! (SF: 7.Nc3! the only good move, +1.58): the c3-knight hits Qd5 and 8.d5! follows (hits Nc6, e-pawn loose/pinned). Before ...Nf6 be sure Nc3 cannot come with tempo. Better 6...e6 (5...e6 too: 6.dxc5 Qxd1+ 7.Kxd1 Bxc5 =) or 6...e5.
- 7...e6?? was played to 'defend' d5 with the e6-pawn; 8.Nxd5 exd5 = QUEEN for a knight. Defenders never save an attacked queen - they only recapture the attacker. She MOVES that move: 7...Qd6/Qd8/Qa5. Same mistake g41/g91/g94 - the 5th time.
- Clock: 6...Nf6 31s, 8...exd5 39s, 13...Bf5 43s, 16...Ne5 42s, 17...Nd6 42s, 21...Bd3 41s; ended 9:44 vs 19:29. The fatal move took only 8 s: the queen-safety check must be automatic, not a product of think time.

## g91 vs Stockfish19 (0-1, Qf7# m22) - bad recaptures, then Qxd6?? on his file
1.e4 c5 2.c3 Nf6 3.e5 Nd5 4.d4 cxd4 5.Nf3 Nc6 6.cxd4 d6 7.Bc4 Nb6 8.Bb5 Bd7 9.Nc3 a6 10.Bxc6 Bxc6?! 11.d5! Bd7 12.O-O e6 13.Bg5 Be7 14.dxe6 fxe6?! 15.Bxe7 Kxe7 16.exd6+ Kf8 17.Re1 Rc8 18.Ne5 Bc6 19.h3 Qxd6?? 20.Qxd6+ = Q for P.
- 10...bxc6! not ...Bxc6?! (11.d5! kicks it); 14...Bxe6! not ...fxe6?! (16.exd6+ makes a passer behind my king).
- 19...Qxd6??: his Qd1 and my Qd8 shared the d-file with only his d6-pawn between; taking the last screen = Q for P. List enemy Q/R on the destination's file/rank/diagonal, screens counted, before any queen capture.
- Clock 30-40 s on every move; every error had a long think.

## g90 vs Stockfish19 (0-1, Qd7# m18) - pinned recapturer
3.e5 Nd5 4.d4 cxd4 5.Nf3 Nc6 6.cxd4 d6 7.Bc4 Nb6 8.Bb5 dxe5 9.Nxe5 Bd7 10.Nxd7 Qxd7 11.Nc3 Qxd4?? 12.Qxd4! (Nxd4 ILLEGAL: Bb5 pins Nc6 to Ke8) 13.Qxd5.
- Before a capture that relies on a recapturer, trace the recapturer's line to my king: pinned = illegal = Q for a pawn. 11...e6/...a6/...Be7/...O-O =.
- Down a queen vs SF: defend everything, 1-5 s/move.

## Alapin 4.c3 plans
- 5.Qxd4 (g58,g63,g64): ...Nc6 ...g6 ...Bg7 ...O-O ...Nc5 =; no ...Nb4, no knight to d4 (12...Nd4?? 13.Rxd4), no ...b5 while Rd1 faces Qd8 (g64: 11...b5?? 12.Bxc5! dxc5 13.Rxd8 = Q for R - the d6-pawn was Rd1's last screen AND Nc5's guard).
- g59: 5...Nc6 6.d5 Nb8 7.Be3 g6 8.Be2 Bg7 9.Nc3 O-O 10.Nd4 Nbd7 11.O-O Nc5 12.f3 Bd7 13.b4 (SF +1.7) - the 4...Nf6 order avoids 6.d5 with tempo.
- Pawn push: list recapturers first; a square safe before a capture may not be after (g63).

## Recurring
- PIN (g90): verify a recapturer is not pinned before sending.
- SCREEN (g91,g64,g79): a queen/pawn capture on the last screen of his queen's file = Q for P.
- Queen: hit by anything -> she moves that move; 'defended' never counts (g95). Never Qx a flank pawn on a rook file.
- His captures open lines: his rook enters first; recheck after every capture.
- Time: routine <=15 s; long thinks never fixed anything (g50,g59,g63,g64,g90,g91,g95); down 1-5 s.
