# Sicilian as Black - Dragon/Alapin/Rauzer (g28-g91)

## g91 vs Stockfish19 (0-1, Qf7# m22) - Alapin 3.e5: both recaptures wrong, then Qxd6?? hung the queen
1.e4 c5 2.c3 Nf6 3.e5 Nd5 4.d4 cxd4 5.Nf3 Nc6 6.cxd4 d6 7.Bc4 Nb6 8.Bb5 Bd7 9.Nc3 a6 10.Bxc6 Bxc6?! 11.d5! Bd7 12.O-O e6 13.Bg5 Be7 14.dxe6 fxe6?! 15.Bxe7 Kxe7 16.exd6+ Kf8 17.Re1 Rc8 18.Ne5 Bc6 19.h3 Qxd6?? 20.Qxd6+ Kg8 21.Qxe6+ Kf8 22.Qf7#.
- 10...Bxc6?! (SF ?; +0.38 -> +1.31): puts the bishop on the square White's d-pawn kicks with tempo. Recapture 10...bxc6! - the d7-bishop stays home, doubled c-pawns are harmless, 11.d5 cxd5 and Black holds.
- 14...fxe6?! (worse than 14...Bxe6): taking with the f-pawn removes f7 (king shelter) and lets 16.exd6+ create a passed pawn on the d-file behind my king; eval +3.7 -> +6.1. 14...Bxe6! keeps the pawn wall, no passer, and 15.Bxe7 Qxe7 (queen recapture) = level.
- 19...Qxd6?? = Q for P: his Qd1 and my Qd8 were on the same d-file with only his pawn on d6 between (d2-d5 empty). Capturing the screen put my queen on the file he owned; 20.Qxd6+ (also check - my e7-bishop was gone) and I could not recapture (nothing defends d6). BEFORE a queen capture: list enemy Q/R on the destination's file/rank/DIAGONAL, with screens; the target itself may be the last screen.
- 21...Kf8 22.Qf7#: Ne5 covers f7, h7/g7/h8 all blocked or covered.
- Clock: 30-40 s on routine moves (6...d6 30, 7...Nb6 36, 9...a6 33, 11...Bd7 39, 13...Be7 39, 14...fxe6 38, 15...Kxe7 39, 17...Rc8 39, 18...Bc6 40); every error came with a long think. Ended 9:20 vs 18:30. Routine <=15 s.

## g90 vs Stockfish19 (0-1, Qd7# m18) - PINNED RECAPTURER: queen lost for a pawn
1.e4 c5 2.c3 Nf6 3.e5 Nd5 4.d4 cxd4 5.Nf3 Nc6 6.cxd4 d6 7.Bc4 Nb6 8.Bb5 dxe5 9.Nxe5 Bd7 10.Nxd7 Qxd7 11.Nc3 Qxd4?? 12.Qxd4! (Nxd4 ILLEGAL: Bb5 pins Nc6 to Ke8) 13.Qxd5 ... 18.Qd7#.
- 11...Qxd4?? assumed Nc6 recaptures; Bb5 pins Nc6 to Ke8 (b5-c6-d7-e8), so no recapture. BEFORE any capture relying on a recapture, trace the recapturer's line to my king: pinned = illegal = queen for a pawn.
- 11...e6/...a6/...Be7/...O-O keeps the line equal.
- Queen down vs Stockfish: defend everything, 1-5 s/move.

## Alapin 4.c3, 5.Qxd4 (g58, g63, g64)
- g58: ...Nc6 ...g6 ...Bg7 ...O-O ...Nc5, ...Bd7/...Rc8 = equal. No knight to d4: 12...Nd4?? 13.Rxd4! = N+B for R+N.
- g63: 6.Qd3 7.Be2 8.O-O 9.Rd1 10.a4 11.Na3 Qa5 12.Nc4 Qd8 equal. 13...b5?? 14.axb5 (NOTHING recaptures); 14...Nb4?? 15.cxb4; 16.b3 Qa5?? 17.Rxa5. Pawn push: list recapturers first; a square 'safe' before a capture opens a file may not be after.
- g64 (mate m25): 6.Qd3 7.Be2 8.O-O 9.Rd1 10.Be3 11.Qc2 b5?? 12.Bxc5! dxc5 13.Rxd8 = Q for R. The d6-pawn was BOTH Rd1's screen in front of Qd8 AND Nc5's sole guard; 11...Qc7! fixes it.

## Alapin 4.c3, 5.cxd4 (g59)
5...Nc6 6.d5 Nb8 7.Be3 g6 8.Be2 Bg7 9.Nc3 O-O 10.Nd4 Nbd7 11.O-O Nc5 12.f3 Bd7 13.b4 (SF +1.7). 13...Na4?? 14.Nxa4! Bxa4 15.Qxa4 = a piece down: after ...b4 the c5-knight has only a6. 4...Nf6 order avoids 6.d5 with tempo.

## Recurring
- PIN (g90): a recapture by a pinned unit is ILLEGAL - verify before sending. Trace the recapturer's line to my king first.
- SCREEN GRAB (g91): a queen capture on the square that is the only screen on his queen's/rook's file = Q for P. Also true of the d6-pawn in g64 and the g6-pawn in g79.
- Queen: never where his Q/R/B/PAWN/KNIGHT takes with no recapture; his piece attacking my queen = move it THAT move (g45-g64). Never Qx a flank pawn on his rook's file.
- Lines his captures open: his rook enters first; safe-before can be fatal after (g61, g63 16...Qa5??).
- Knight: check enemy PAWNS/KNIGHTS on the destination, rooks on its file, retreat square attacked by nothing.
- Pawn push: sole guard of my piece? recapturers of the pushed pawn? (g63).
- d6/d7 weak: never Bd7 as d6's only shield; recapture Bxf6 with ...gxf6. b7 loose once b5 leaves.
- Time: routine <=15 s; long thinks never fixed anything (g50,g59,g63,g64,g90,g91); when down 1-5 s.
