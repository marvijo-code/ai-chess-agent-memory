# Sicilian as Black - Dragon/Alapin/Rauzer (g28-g64)

## Alapin 4.c3, 5.Qxd4 (g58, g63, g64)
- g58: ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5, ...Bd7/...Rc8 = equal (-0.3..0.0). No knight to d4: 12...Nd4?? 13.Rxd4! Bxd4 14.Nxd4 = N+B for R+N and Bg7 gone; list enemy attackers incl. rooks on file/rank, then value the chain.
- g63 vs SF19 (mate m46): 6.Qd3 7.Be2 8.O-O 9.Rd1 10.a4 11.Na3 Qa5 12.Nc4 Qd8 equal. Then 13...b5?? 14.axb5 Nb4?? 15.cxb4 Bxb5 16.b3 Qa5?? 17.Rxa5.
- 13...b5?? dropped a pawn: after 14.axb5 NOTHING recaptures (a7 takes only b6; Bd7 blocked by Nc6; no Rb8). Before any pawn push, list every recapturer of the pushed pawn.
- 14...Nb4?? cxb4: the SAME blunder as g47 15...Nb4??; b4 is c3-pawn-attacked and undefended. No knight jump to a pawn-attacked square, ever.
- 16...Qa5?? Rxa5: Qa5 was safe at m11 only while the a4-pawn blocked the a-file; 14.axb5 opened it (a2/a3/a4 empty) so Ra1 takes first. After a capture opens a line, re-check every "safe" square.
- g64 vs SF19 (mate m25): 6.Qd3 7.Be2 8.O-O 9.Rd1 10.Be3 11.Qc2 b5?? 12.Bxc5! dxc5 13.Rxd8 Rxd8 = Q for R. The d6-pawn was BOTH Rd1's screen in front of my Qd8 AND the sole guard of Nc5 (Be3 attacks it); while his Qd3 blocked d3 the trade was even, but once 11.Qc2 vacated d3, Bxc5 won a piece or, after the forced dxc5, opened Rd1 to my queen. Fix: 11...Qc7! (defends c5 AND leaves the d-file) or any queen move off d8; never ...b5 there.
- 22...Qxd5?? cxd5 (g58), 22...Qxb5?? Nxb5 (g59): count PAWNS/KNIGHTS on the target before any queen capture.

## Alapin 4.c3, 5.cxd4 (g59)
5...Nc6 6.d5 Nb8 7.Be3 g6 8.Be2 Bg7 9.Nc3 O-O 10.Nd4 Nbd7 11.O-O Nc5 12.f3 Bd7 13.b4 (SF +1.7; 4...Nc6?!; 4...Nf6 order avoids 6.d5 with tempo). 13...Na4?? 14.Nxa4! Bxa4 15.Qxa4 = piece down. After ...b4 the c5-knight has only a6 (b7 own pawn, d7 bishop, e6 hit by d5-pawn, e4 by f3-pawn).

## g50 (delayed Alapin, Qa3# m21)
9.Bxd6 Bxd6 10.Qxd6 Qc7?? 11.Qxc7!: nothing covers c7 (a8-rook, b8-knight, d7-bishop, f6-knight, b7/e6 pawns miss). Before any queen move: can his Q/B/R/PAWN take it, what recaptures? Attacking his queen excuses nothing. Rxc7 illegal (1 try); trace the path first. 37-99 s thinks m5-12 did not help.

## g47 (delayed Alapin, flag m24)
11...Nxe4?? e4 is defended by Qf3 - a grab wins only with no recapture, esp. his QUEEN. 15...Nb4?? 16.cxb4 (repeated in g63!) - c3-pawn. Qxb4 illegal twice; never resend a rejected move. Down vs SF: defend, trade, 5-15 s.

## g45 (forfeit m14)
With b5 gone Bb7 is loose: ...Qd7/...Rb8 defend, ...Bc8 retreats; never a rook swing ignoring a hanging bishop. Setup fine to 12...axb5.

## Older - condensed
- g36: fine to 13...Qa5; 14...Qxa4?? Ra1 takes on the open a-file (Qc2 also guards a4); never Qx a flank pawn on a rook's file.
- g30/g28: 5...Nh5?! offside; 9...f5?? 10.Nxc5; 20...f4?? moved f5, sole guard of Ne4; 18...Qxc4?? Bxc4.
- g32/g29 Rauzer: 11...gxf6! (Be7 guards d6); Bxf6?? leaves d6 loose (12.Qxd6!); no B-for-P; guard the back rank (19...Rd8?? Rxd8#).
- g49 Soltis: see notes/sicilian-soltis-black.md.

## Recurring
- Queen: never where his Q/R/B/PAWN/KNIGHT takes with no recapture; his piece aiming at my queen = move it THAT move (g45,g46,g50,g58,g59,g63,g64).
- Lines his captures open: his rook enters first; squares safe before can be fatal after (g61 21.b4?, g63 16...Qa5??).
- Knight: check enemy PAWNS/KNIGHTS on the destination, rooks on its file, recaptures; the retreat square must be attacked by nothing (g47,g58,g59; g63 Nb4 twice).
- Pawn push: sole guard of my piece? recapturers of the pushed pawn? (g63 13...b5??).
- Overloaded guard: a pawn that is both a file screen in front of my queen and the only guard of an attacked piece is a tactic magnet; move the queen off the file or add a second defender before developing (g64).
- d6/d7 weak: never Bd7 as d6's only shield; recapture Bxf6 with ...gxf6. b7 loose once b5 leaves: ...Qd7/...Rb8 or ...Bc8.
- Time: routine <=15 s; long thinks never fixed anything (g50,g59,g63,g64); when down play 1-5 s (g59 flag).
