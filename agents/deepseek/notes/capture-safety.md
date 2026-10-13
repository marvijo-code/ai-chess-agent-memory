# Pre-move scan & blunder catalogue

## Every move
1. Legality: paths clear; one rejection = redraw, list every legal move, never resend.
2. His LAST move first, then MY destination: 0 guards + his capture = gift. Walk every enemy bishop/rook diagonal to any queen/rook destination (T37R5 17.Qg4?? Bxg4 = Q for B).
3. Enemy pawn captures: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7, g5<-h6, f6<-e5. A pawn that MOVED to attack still attacks (T38R6 9...Nf6?? exf6).
4. Screens: my piece moving opens a line to my queen or king.
5. A push ends guard duty: name what the pawn left unguarded (T38R4 16.d4? left Nc4 loose).
6. Knight retreats only where that knight cannot take and his queen/rook do not own the square.
7. Captures: count ALL recapturers - PAWNS first; my defender must LAND on the destination; recapture choice keeps the recapturer's other guards.
8. Rook check: ask 'can his king just take it?' (T38R2 43...Rf5+?? Kxf5).
9. Queen hit -> she moves THAT move, OFF every ray. Before any queen/rook move list what it guarded where it stood + every enemy knight/pawn hitting the destination (T38R6 19...Qc5?? Nxc5).
10. A piece whose only guard is my queen is lost to his second attacker.
11. Down: keep queens while safe, loose pieces first, no grabs. Up: trade pieces, not pawns.
12. Material FROM THE BOARD after every capture.
13. Clock: book 10 s, routine 15, cap 20; under 3 min 5 s. Long thinks still blunder.
14. MATE FIRST, quiet moves too. Keep a rank-1 blocker or luft. B+N vs K: to the bishop's-colour corner, no shuffling.
15. SELF-BAN: a move my note called bad is DEAD (T37R5 17.Qg4??; T38R7 12.c4?).

## Italian W vs Sol - the c4?/Nf4 trap twice (T37R5 m19, T38R7 m32)
Book: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 O-O 6.O-O d6 7.Nbd2 a6 8.Re1 Ba7 (16 plies).
- 10.d4?! exd4 11.cxd4 Nxd4! wins a pawn (Nbd2 blocks Qd1).
- 12.c4? kicks the d5-knight to f4 hitting d3; 13.Bc2?? does NOT save it: 13...Nxd3 14.Bxd3 Qxd3 = pawn + bishop pair for a knight. Re-guard c4 before d4; after exd5 use Ne4/Nf1-g3/Bd2, NEVER c4.
- T38R7 18...Nd3! forked Re1/Bc1; 19.Bd2 'defended' e1 but Nxe1 still won the exchange. A forked rook must MOVE or the forker must be taken.
- 17.Qg4?? blocked Qxg2# on Be6's diagonal: Q for B. Defend g2, remove Nf4, or trade queens.

## Other catalogue
- T38R6 (Taimanov B): 9...Nf6?? exf6; 12...Rg8?? Qxg8+; 19...Qc5?? Nxc5.
- T38R2 (English B, converted R+B): 25.dxc6?? Qxd3 (Qa6 hit d3 via b5-c4); 43...Rf5+?? Kxf5.
- g148 Caro B: 17...Bg5?? screen to Qd8 -> 19.Bxd8; 21...Rc7??/23...Nb7?? hung.
- g144 Caro B: 15...Bxf6? 16.Bxc5!; 19...h6?? 20.Bxg6; 24...Qxe5?? fxe5.
- g146 IQP W: 20.b3?? Bxa1; 26.Kf1?? Re1#; g143 23.Rd2?? Qe1#.

## Patterns
- Losses = one-move scan misses (screen / blocked guard / queen on a bishop's diagonal / piece on a pawn's capture square) + plan drift; the openings are fine.
- A note that NAMES a danger is a self-ban: T38R7 12.c4? repeated exactly the trap my own Italian note described.
- A fork/attack never excuses skipping the destination scan.
