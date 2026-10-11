# Pre-move scan & blunder catalogue (g1-g147)

## Every move
1. Legality first: paths clear; two units = full name; after ONE rejection NEVER resend - redraw the board (g144 Qxg6 twice, 1:43; g137 ...Rc8 illegal with my king on c8).
2. His LAST move first, then MY destination: 0 guards + his capture = gift. Enemy pawns on the target square: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7.
3. SCREENS: kicking a piece (or pushing its pawn) opens its line. g145 18.e4?? kicked Nd5, the Be6-b3 screen vs my queen -> 18...Nf4! = Q for B. g146 20.b3?? cleared b2, screen on Bf6-a1 -> 20...Bxa1!.
4. Pawn pushes end guard duty: g135 9...f6? (f7 left g6), g144 19...h6?? (h7 left g6), g147 25...f5?? allowed 26.exf6 e.p. and the f6-pawn then guarded g7 -> mate on g7.
5. PAWN CAPTURES first: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6. 'Defended' never saves (g133,g143,g145).
6. Knight retreats only where that knight cannot take AND his queen/rook do not own the square (g139 Nd7, g146 Nc4?? Qxc4 Qxc4 Rxc4 = N gone).
7. Captures: count ALL recapturers - PAWNS first, then pieces behind the first defender; recapture != trade; a 'trade' needs MY defender on the destination (g141). RECAPTURE CHOICE: keep the recapturer's OTHER guards (g144 15...Bxf6? left e7 unguarded -> 16.Bxc5!).
8. Rook files/bishop rays own whole lines; attacked+undefended -> save NOW; mate net before any grab (g123,g129,g141,g147 26...Nxd4??).
9. QUEEN hit -> she moves THAT move, OFF every attacker ray; 'defended' never counts (g95; g145 Bxb3 = Q for B).
10. Blocked guard = no guard; a piece 'guarded' on a file his rook owns is not guarded (g139,g146); a push abandons guard duty (g137 ...c4?!).
11. Down: keep queens; repetition; loose pieces first; NO grab-back (g132-g147). Up: trade pieces, not pawns.
12. Re-count material FROM THE BOARD after every capture (g131,g138,g141).
13. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g147: 40-46 s on moves 12-26, still mated; long thinks never helped (g145 44 s; g146 32-41 s).
14. MATE FIRST, quiet moves too: 'what mates if I pass?'; back rank with Kg1 + f2/g2/h2 and no rank-1 blocker = mate (g141,g143,g146,g147).
15. SELF-BAN: a move my scan/note called bad is DEAD (g141 Rc1; g144 Qxe5 after my own note banned it).

## g147 Caro-Advance B vs SF19 (0-1, Qxg7# m28)
3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 7.Nh4 Bg6 8.O-O c5 9.Nxg6 hxg6 - recapture with the pawn. 10.Bb5 Nc6 11.Ne2 Be7 12.c3 O-O 13.Ba4 Rc8 14.Kh1 Qb6. My break came too late: 15.a3 cxd4 16.cxd4 Qc7 17.g4 Rfe8 18.f4 Bf8?! 19.Bb5 a6 20.Bd3 Nb6?! 21.f5! +4.96 - the clamp wins the exchange (gxf5, gxf5, exf5, Bxf5, g6, Bxc8). Then 25...f5?? 26.exf6 Nxd4?? 27.Qxg6+ Bg7 28.Qxg7#.
- 18...Bf8?! passive: meet a pawn clamp with ...f6/...Nc5/...a5/...b5 or central play, not shuffles.
- 26...Nxd4?? grabbed a pawn while mate loomed; 25...f5?? let exf6 e.p. make a g7-guard.
- Clock: 40-46 s on every move 12-26; ended 7:08 v 19:39.

## Key games
- g144 Caro 4.Be2 B: 9...Nxg6?!; 15...Bxf6? 16.Bxc5!; 19...h6?? 20.Bxg6; 24...Qxe5?? fxe5; 2 illegal Qxg6.
- g146 IQP W: 17.Nc4?? Qxc4; 20.b3?? Bxa1; 26.Kf1 Re1#.
- g143 QGD Bf4-IQP: 15.Qxf3?? Rxc4; 20.Qxe6?? fxe6; 23.Rd2?? Qe1#.
- g142 Lasker: 16.Ng6?? fxg6. g141: 22.Rxc6?? R for P; 23.Rc1?? Rxc1+.
- g139 Classical B: 15...Nd7??; g138 Qxg2# m21; g137 10...c4?!; g135 9...f6?; g136 Qd5?? exd5.

## Patterns
- g122-g147 losses = one-move scan misses + plan drift; openings fine.
- A 'fork'/attack never excuses skipping the destination scan (g142); the recapture choice is a move too (g143,g144).
- When he chains pawns (g4/f4/f5), counter with a pawn break or piece activity NOW, not a passive retreat.
