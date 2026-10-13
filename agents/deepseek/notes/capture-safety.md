# Pre-move scan & blunder catalogue

## Every move
1. Legality: path clear - walk it for MY OWN pawns first. One rejection = redraw, list legal moves, never resend. O-O-O leaves Kc8, so ...Rc8 illegal.
2. His LAST move first, then MY destination: 0 guards + his capture = gift.
3. Enemy pawn captures: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7, g5<-h6, f6<-e5, f5<-g6/e6. A moved pawn still attacks.
4. Enemy KNIGHT jumps on EVERY destination: d5 owns f4/e3/c3/b4/b6/c7/e7/f6; f6 owns e4/g4/h5/h7/d5/e8/g8/d7; f5 owns e7/d6/d4/e3/g3/h4/h6/g7.
5. Screens: my piece moving opens a line to my queen/king. A screen leaving with tempo makes the piece behind loose.
6. A push ends guard duty: name what the pawn left unguarded. Kicking an attacker never defends its target.
7. Captures: all recapturers, PAWNS first; the defender must LAND on the destination, and needs its own guard.
8. Rook check: 'can his king just take it?'
9. Queen hit -> she moves THAT move, off every ray; never on an enemy pawn's capture square.
10. Down: queens only while safe, no grabs. Up: trade pieces, not pawns.
11. Material FROM THE BOARD after every capture.
12. Clock: book 10 s, routine 15, cap 20; under 3 min 5 s.
13. MATE FIRST, quiet moves too. Keep a rank-1 blocker or luft.
14. SELF-BAN: a move my note called bad is DEAD.
15. Before ANY check: what captures the checker, the KING included?
16. An 'undefended' capture is only real if no enemy move with tempo clears its guard.

## T40R7 vs Sol (0-1, Re1# m23) - a 'won a knight' that wasn't
Italian Giuoco Pianissimo; level to move 13. 14.cxd4?? (engine) - over-trusted my recapture chain.
- 16.Rxe4 'his e4-knight is undefended, I win a piece': 16...Bxb3 hit my QUEEN, 17.axb3 Rxe4 took my rook - the bishop exchange cleared the e-file for his rook. Walk every tempo move and guard-clearing exchange before taking a 'loose' piece.
- 18.Rxa6?? R for P - NEVER trade a ROOK for a PAWN; I had written '+N' but material was level.
- Lesson: count material from the board; trace a capture chain to the end before calling it a gain.

## T40R3 vs GLM (1-0, Ra8# m44) - rook-ladder conversion
Open Sicilian 3...Nxd4 4...e5; Nd5/...Nxd5/exd5 space edge; 22.Ne3?? left my c4-bishop to 22...bxc4. Then Nxf5/Nxe7+ won the QUEEN for a bishop; +Q for B+P converted by guarding every unit, trading rooks evenly, two-rook ladder Rd7+/Rd8+, Ra8#.
- Illegal tries 41.Rb7+/43.Rb8# BOTH blocked by my own b3/b4 pawns.

## T40R2 vs SF19 (0-1, Qxh2# m18) - three pawn-square gifts
Accelerated Dragon: 9.Bf4?? took Be3 off d4 (Nd4's only guard) -> Bxd4; 11.Nf6+ on the e7-pawn's grab square -> exf6; 14.Qf4?? on the g5-pawn's square -> gxf4 = Q for P.

## T40R1 vs Sol (0-1, Re8# m28) - gave back a won queen
21.fxe6 Rxf3 22.Rxf3 won Q for R; 24...Qe7 vacated d7, the only blocker on f5-c8 -> Bxc8 won my loose Rac8; 25...Qe1+?? Rxe1 = Q for R.

## Patterns
- Losses = one-move scan misses (screen / blocked guard / queen on a bishop's or knight's square / piece on a pawn's capture square) + plan drift; the openings are fine.
- A note that NAMES a danger is a self-ban.
- Winning material is not converting it: after Q-for-R defend every rook and queen, keep his bishop's diagonal blocked; after a big lead trade evenly and mate with a rook ladder (T40R3).
