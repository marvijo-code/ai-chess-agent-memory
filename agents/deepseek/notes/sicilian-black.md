# Sicilian as Black - Dragon/Alapin/Rauzer (g28-g90)

## g90 vs Stockfish19 (0-1, Qd7# m18) - PINNED RECAPTURER: queen lost for a pawn
1.e4 c5 2.c3 Nf6 3.e5 Nd5 4.d4 cxd4 5.Nf3 Nc6 6.cxd4 d6 7.Bc4 Nb6 8.Bb5 dxe5 9.Nxe5 Bd7 10.Nxd7 Qxd7 11.Nc3 Qxd4?? 12.Qxd4! (Nxd4 ILLEGAL: Bb5 pins Nc6 to Ke8) 13.Qxd5 ... 18.Qd7#.
- 11...Qxd4?? assumed Nc6 recaptures; Bb5 pins Nc6 to Ke8 (b5-c6-d7-e8), so no recapture. BEFORE any capture relying on a recapture, trace the recapturer's line to my king: pinned = illegal = queen for a pawn.
- 11...e6/...a6/...Be7/...O-O keeps the line equal.
- 12...Nd5?? (Nxd4 illegal) hung a knight to 13.Qxd5; ...e6/...Kd8/...f6/...Ke7 only delayed mate. Queen down vs Stockfish: defend everything, 1-5 s/move.
- Clock: 30 s m1, 37 s 5...Nc6, 76 s 12...Nd5 - all routine; cap 15 s.

## Alapin 4.c3, 5.Qxd4 (g58, g63, g64)
- g58: ...Nc6 ...g6 ...Bg7 ...O-O ...Nc5, ...Bd7/...Rc8 = equal. No knight to d4: 12...Nd4?? 13.Rxd4! Bxd4 14.Nxd4 = N+B for R+N.
- g63: 6.Qd3 7.Be2 8.O-O 9.Rd1 10.a4 11.Na3 Qa5 12.Nc4 Qd8 equal. 13...b5?? 14.axb5 (NOTHING recaptures: a7 only takes b6, Bd7 blocked by Nc6, no Rb8); 14...Nb4?? 15.cxb4 Bxb5 16.b3 Qa5?? 17.Rxa5.
- Pawn push: list recapturers first. No knight to a pawn-attacked square. After a capture opens a file, re-check "safe" squares (Qa5 safe only while the a4-pawn blocked the a-file).
- g64 (mate m25): 6.Qd3 7.Be2 8.O-O 9.Rd1 10.Be3 11.Qc2 b5?? 12.Bxc5! dxc5 13.Rxd8 = Q for R. The d6-pawn was both Rd1's screen in front of Qd8 AND Nc5's sole guard; 11...Qc7! fixes it.

## Alapin 4.c3, 5.cxd4 (g59)
5...Nc6 6.d5 Nb8 7.Be3 g6 8.Be2 Bg7 9.Nc3 O-O 10.Nd4 Nbd7 11.O-O Nc5 12.f3 Bd7 13.b4 (SF +1.7). 13...Na4?? 14.Nxa4! Bxa4 15.Qxa4 = piece down: after ...b4 the c5-knight has only a6. 4...Nf6 order avoids 6.d5 with tempo.

## g50/g47/g45 - condensed
- g50 (Qa3# m21): 10.Qxd6 Qc7?? 11.Qxc7! (nothing covers c7). Before any queen move: can his Q/B/R/PAWN take it, what recaptures? Rxc7 illegal (1 try).
- g47: 11...Nxe4?? e4 defended by Qf3; 15...Nb4?? 16.cxb4 (c3-pawn). Down vs SF: defend, 5-15 s.
- g45 (forfeit m14): with b5 gone Bb7 is loose: ...Qd7/...Rb8 defend, ...Bc8 retreats.

## Older - condensed
- g36: 14...Qxa4?? Ra1 takes on the open a-file. g30/g28: 9...f5?? 10.Nxc5; 20...f4?? moved Ne4's sole guard.
- g32/g29 Rauzer: 11...gxf6!; Bxf6?? 12.Qxd6!; no B-for-P; back rank (19...Rd8?? Rxd8#).

## Recurring
- PIN (g90): a recapture by a pinned unit is ILLEGAL - verify before sending (Nxd4 cost invalid attempt #1). Trace the recapturer's line to my king first.
- Queen: never where his Q/R/B/PAWN/KNIGHT takes with no recapture; his piece attacking my queen = move it THAT move (g45-g64). Never Qx a flank pawn on his rook's file.
- Lines his captures open: his rook enters first; safe-before can be fatal after (g61, g63 16...Qa5??).
- Knight: check enemy PAWNS/KNIGHTS on the destination, rooks on its file, retreat square attacked by nothing.
- Pawn push: sole guard of my piece? recapturers of the pushed pawn? (g63).
- Overloaded guard: a pawn that is both my queen's file screen and the only guard of an attacked piece = tactic magnet (g64).
- d6/d7 weak: never Bd7 as d6's only shield; recapture Bxf6 with ...gxf6. b7 loose once b5 leaves.
- Time: routine <=15 s; long thinks never fixed anything (g50,g59,g63,g64,g90); when down 1-5 s.
