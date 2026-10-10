# Sicilian as Black - Alapin/Dragon/Taimanov (g28-g103)

## g103 vs Sol (0-1, Rf8# m33) - Taimanov: two free pieces
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 d6 9.f4 Nxd4 10.Bxd4 e5 11.fxe5 dxe5 12.Bxe5 Bd6?? 13.Qxd6 Qxd6 14.Bxd6 Nxe4 15.Nxe4 Be6 16.Bxf8 Rxf8 17.Bd3 Bf5?? 18.Rxf5: White R+R+B+N vs R+B, mate m33.
- After 12.Bxe5 (hits Nf6, White +1 pawn) Black must free the knight: 12...Nxe4! 13.Nxe4 (pawns level) then ...f6/...Bd7 and hold. 12...Bd6?? loses B+Q for Q: 13.Qxd6 Qxd6 14.Bxd6 - a piece defended ONLY by my queen dies to Qx then his 2nd attacker (the e5-bishop). Write Qx + Bx before moving a piece onto a square his queen's line covers.
- 17...Bf5?? Rxf5: quiet piece onto the open f-file (f2-f5 empty, Rf1; f7 blocks recapture) with no defender; it attacked only a Bd3-defended knight. Already down, every move passes the destination sweep (his rook files + bishop diagonals) FIRST.
- Clock: 28-38 s opening moves, ended 9:37 vs 14:52; both blunders took 36-38 s. Book <=10 s even in a 'solid' line.

## g95 vs Stockfish19 (0-1, Qe8# m28) - queen 'defended' on attacked d5
1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.Nf3 Nc6 5.d4 cxd4 6.cxd4 Nf6?! 7.Nc3! e6?? 8.Nxd5! exd5 9.Bb5 +8.85.
- 6...Nf6?! (SF: 7.Nc3! only, +1.58). Before ...Nf6 be sure Nc3 cannot come with tempo. Better 6...e6 (or 5...e6: 6.dxc5 Qxd1+ 7.Kxd1 Bxc5 =) or 6...e5.
- 7...e6?? 'defended' d5 with the e6-pawn; 8.Nxd5 exd5 = QUEEN for a knight. Defenders never save an attacked queen - she MOVES that move: ...Qd6/Qd8/Qa5. Same mistake g41/g91/g94 - 5th time.
- Clock: 31-43 s routine blunders (the fatal move took 8 s), ended 9:44 vs 19:29.

## g91 vs Stockfish19 (0-1, Qf7# m22) - bad recaptures, then Qxd6?? on his file
1.e4 c5 2.c3 Nf6 3.e5 Nd5 4.d4 cxd4 5.Nf3 Nc6 6.cxd4 d6 7.Bc4 Nb6 8.Bb5 Bd7 9.Nc3 a6 10.Bxc6 Bxc6?! 11.d5! Bd7 12.O-O e6 13.Bg5 Be7 14.dxe6 fxe6?! 15.Bxe7 Kxe7 16.exd6+ Kf8 ... 19...Qxd6?? 20.Qxd6+ = Q for P.
- 10...bxc6! not ...Bxc6?! (11.d5! kicks it); 14...Bxe6! not ...fxe6?! (16.exd6+ makes a passer behind my king).
- 19...Qxd6??: his Qd1 and my Qd8 shared the open d-file; the d6-pawn was the last screen. Before any queen capture list Q/R on the destination's file/rank/diagonal, screens counted.
- Clock 30-40 s per move, every error had a long think.

## g90 vs Stockfish19 (0-1, Qd7# m18) - pinned recapturer
3.e5 Nd5 4.d4 cxd4 5.Nf3 Nc6 6.cxd4 d6 7.Bc4 Nb6 8.Bb5 dxe5 9.Nxe5 Bd7 10.Nxd7 Qxd7 11.Nc3 Qxd4?? 12.Qxd4! (Nxd4 ILLEGAL: Bb5 pins Nc6 to Ke8) 13.Qxd5.
- Before a capture that relies on a recapturer, trace its line to my king: pinned = illegal = Q for a pawn. 11...e6/...Be7/...O-O =.
- Down a queen vs SF: defend everything, 1-5 s/move.

## Alapin 4.c3 plans
- 5.Qxd4 (g58,g63,g64): ...Nc6 ...g6 ...Bg7 ...O-O ...Nc5 =; no ...Nb4, no knight to d4 (12...Nd4?? 13.Rxd4), no ...b5 while Rd1 faces Qd8 (g64: 11...b5?? 12.Bxc5! dxc5 13.Rxd8 - d6-pawn was last screen AND Nc5's guard).
- g59: 4...Nf6 order avoids 6.d5 with tempo; then ...Nc6/...g6/...Bg7/...O-O/...Nc5.
- Pawn push: list recapturers first; a square safe before a capture may not be after (g63).

## Recurring
- PIN (g90): verify a recapturer is not pinned before sending.
- SCREEN (g91,g64,g79): a capture on the last screen of his queen's file = Q for P.
- Queen: hit by anything -> she moves that move; 'defended' never counts (g95). Never Qx a flank pawn on a rook file.
- His captures open lines: his rook enters first; recheck after every capture.
- Time: routine <=15 s; long thinks never fixed anything (g50,g59,g63,g64,g90,g91,g95); down 1-5 s.
