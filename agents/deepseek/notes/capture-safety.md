# Pre-move scan & blunder catalogue

## Every move
1. Legality: walk the path for MY OWN pawns first. One rejection = redraw, list legal moves, never resend.
2. His LAST move first, then MY destination: 0 guards + his capture = gift. Quiet/'tempo'/retreat moves obey the SAME sweep.
3. Enemy pawn captures: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, e6<-f7, g5<-h6, f6<-e5, f5<-g6/e6. A moved pawn still attacks.
4. Enemy knight jumps: f6 owns e4/g4/h5/h7/d5/e8/g8/d7; f5 owns e7/d6/d4/e3/g3/h4/h6/g7; f4 owns e2/g2/d3/h3/d5/h5/e6/g6; d5 owns f4/e3/c3/b4/b6/c7/e7/f6.
5. Screens: a piece moving opens the line to my queen/king (T42R4 ...dxe5 opened d7-d2, Qxd2).
6. A push ends guard duty: name what the pawn left unguarded.
7. Captures: all recapturers, PAWNS first; the recapturer must LAND on the destination, needs its own guard, and must not itself be the piece he is attacking (T42R4 21.Rxe1?? left Qd2 to ...Qxd2; 21.Qxe1! took with the queen).
8. Rook check: 'can his king just take it?'
9. Queen hit -> she moves THAT move; never on an enemy pawn's capture square.
10. Down: queens while safe, no grabs. Up: trade pieces, not pawns.
11. Material FROM THE BOARD after every capture. A won piece must be RE-GUARDED on its new square (T42R4 16.Nxe4! then ...Bxb3 vacated e6 and ...Rxe4; d3 had left e4).
12. Clock: book 10 s, routine 15, cap 20; under 3 min 5 s.
13. MATE FIRST, quiet moves too. Keep a rank-1 blocker or luft.
14. SELF-BAN: a move my note called bad is DEAD.
15. Before ANY check: what captures the checker, the KING included?
16. An 'undefended' capture is real only if no enemy move with tempo clears its guard.
17. A retreat/recapture landing on a diagonal: walk that diagonal to the end (own queen behind it included).

## T42R4 vs Sol (0-1, Rh2# m32) - won a knight, gave it back, hung the queen
Italian Pianissimo, level to m13. Sol blundered 14...Nxe4??; 16.Nxe4! won the knight.
- 17.axb3??: his 16...Bxb3 VACATED e6 (the e-file's only blocker) so 17...Rxe4 took my knight; its pawn guard (d3) had advanced to d4 at move 14.
- 18.Ne5?? dxe5: the d6-pawn owns e5, and that capture opened the d-file onto Qd2.
- 21.Rxe1?? left Qd2 on the open d-file -> 21...Qxd2 = Q for R. 21.Qxe1! recaptures WITH the attacked queen and dodges the file.
- Clock: 15:00 at move 14 -> 12:45; 38 s on d4, 40 s on Nxe4, 62 s on Ne5??. Long thinks were the blunders.

## T42R3 vs SF19 (0-1, Qf8# m20) - retreat onto an attacked square
Caro Advance: 14.Nxd5 forked my f6-bishop; 14...Bg5?? landed on g5 with 0 guards (Bc1+Nf3 hit it) -> 15.Bxg5, and the g5-f6-e7-d8 diagonal then hit my queen -> 16.Bxd8.

## T42R2 vs Sonnet (0-1, Rd1# m27) - two grabs
- 14.Nd6?? at the e8-rook with ZERO guards: 14...Qxd6.
- 19.Qxb4?? put my QUEEN undefended beside his on the d6-c5-b4 diagonal: 19...Qxb4 = Q for N.

## Patterns
- Losses = one-move scan misses (screen / blocked guard / queen on a bishop or knight square / piece on a pawn's capture square / wrong recapturer) + plan drift; the openings are fine.
- Winning material is not converting it: re-guard the new piece, trade evenly, mate with a rook ladder (T40R3).
