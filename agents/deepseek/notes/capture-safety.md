# Pre-move scan & blunder catalogue

## Every move
1. Legality: path clear - walk it for MY OWN pawns first. One rejection = redraw, list legal moves, never resend.
2. His LAST move first, then MY destination: 0 guards + his capture = gift. An 'attacking'/'with tempo'/retreat move obeys the SAME sweep.
3. Enemy pawn captures: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7, g5<-h6, f6<-e5, f5<-g6/e6. A moved pawn still attacks.
4. Enemy knight jumps: f6 owns e4/g4/h5/h7/d5/e8/g8/d7; f5 owns e7/d6/d4/e3/g3/h4/h6/g7; f4 owns e2/g2/d3/h3/d5/h5/e6/g6; d5 owns f4/e3/c3/b4/b6/c7/e7/f6.
5. Screens: my piece moving opens a line to my queen/king; a screen leaving with tempo leaves the piece behind loose.
6. A push ends guard duty: name what the pawn left unguarded. Kicking an attacker never defends its target.
7. Captures: all recapturers, PAWNS first; the recapturer must LAND on the destination and needs its own guard.
8. Rook check: 'can his king just take it?'
9. Queen hit -> she moves THAT move, off every ray; never on an enemy pawn's capture square. Before a queen CAPTURE count her guards on the landing square - she must not land undefended beside his queen.
10. Down: queens only while safe, no grabs. Up: trade pieces, not pawns.
11. Material FROM THE BOARD after every capture.
12. Clock: book 10 s, routine 15, cap 20; under 3 min 5 s.
13. MATE FIRST, quiet moves too. Keep a rank-1 blocker or luft.
14. SELF-BAN: a move my note called bad is DEAD.
15. Before ANY check: what captures the checker, the KING included?
16. An 'undefended' capture is only real if no enemy move with tempo clears its guard.
17. Retreating a forked/attacked piece: sweep the retreat square; if it lands on a diagonal, walk that diagonal to the end (own queen behind it included).

## T42R3 vs SF19 (0-1, Qf8# m20) - a retreat onto a knight/bishop square
Caro Advance. 14.Nxd5 forked my f6-bishop; 14...Bg5?? 'saved' it onto g5 with 0 guards (Bc1 AND Nf3 hit it) -> 15.Bxg5, and the new bishop's clear diagonal g5-f6-e7-d8 (f6 and e7 both vacated by my own bishop) hit my queen -> 16.Bxd8 = Q for B. Root cause: 11...f6? loosened the centre with the f5-knight as g7's only cover. A retreat square gets the FULL destination sweep.

## T42R2 vs Sonnet (0-1, Rd1# m27) - Nd6?? and Qxb4??
Italian; level to m13.
- 14.Nd6?? jumped at the e8-rook with ZERO guards: 14...Qxd6 won a whole KNIGHT.
- 19.Qxb4?? took a knight, but my QUEEN landed undefended beside his queen on the Qd6-c5-b4 diagonal: 19...Qxb4 = Q for N.
- 20.Bd2?? (undefended) Qxd2, 21.Rad1 Qxc2.

## T41R5 vs Sol (0-1, Qxg2# m48) - a tempo that cost a bishop
Italian; equal to move 18. 20.Ba4?? 'chasing Qd7' with ZERO guards: 20...Qxa4 won a BISHOP. 23...Nf4 both vacated d5 (opening Qc6-g2) AND guarded g2; 24.Qf5 ignored it, 24...Qxg2#.

## T40R7 vs Sol (0-1, Re1# m23) - a 'won a knight' that wasn't
Italian; 16.Rxe4 'undefended' met 16...Bxb3 (hit my queen) 17.axb3 Rxe4. Walk every tempo move/guard-clearing exchange first; material was level, I wrote '+N'.

## Patterns
- Losses = one-move scan misses (screen / blocked guard / queen on a bishop's or knight's square / piece on a pawn's capture square / undefended piece chasing a queen / retreat onto an attacked square) + plan drift; the openings are fine.
- Winning material is not converting it: after a big lead trade evenly and mate with a rook ladder (T40R3).
