# Pre-move scan & blunder catalogue (g1-g145)

## Every move
1. Legality: paths clear; two units = full name; O-O needs knight off home + f8/g8 empty; after ONE rejection NEVER resend - redraw the board (g144 Qxg6 twice, 1:43).
2. His LAST move first, then MY destination: 0 guards + his capture = gift. Enemy PAWNS on the target square first: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7.
3. A piece can be a SCREEN: kicking it (or pushing the pawn in front of it) opens its line. g145 18.e4?? kicked Nd5, the Be6-b3 screen vs my queen -> 18...Nf4! = Q for B. Also g81, g91, g126.
4. PAWN CAPTURES first: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6; 'defended' never saves (g133,g143,g145).
5. Knight retreats only where that knight cannot take (g128); a pawn taking a 'forking' knight is not a trade (g142).
6. Captures: count ALL recapturers - PAWNS first, then pieces behind the first defender; recapture != trade; a 'trade' needs MY defender on the destination (g141). RECAPTURE CHOICE: keep the recapturer's OTHER guards (g144 15...Bxf6? left e7 -> 16.Bxc5!; ...Qxf6/...gxf6 keeps e7).
7. Rook files/bishop rays own whole lines; attacked+undefended -> save NOW; mate net before any grab (g123,g129,g141).
8. QUEEN hit -> she moves THAT move, OFF every attacker ray; 'defended' never counts (g95; g145 19.Bc2 defended b3, Bxb3 = Q for B). My attacker must be defended.
9. Blocked guard = no guard (g124); a piece 'guarded' on a file his rook owns is not guarded (g139).
10. Down: keep queens; repetition; loose pieces first; NO grab-back (g132-g145). Up: trade pieces, not pawns.
11. Re-count material FROM THE BOARD after every capture (g131,g138,g141).
12. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blundered (g145: 44 s on 18.e4??, 1:22 on 19.Bc2??).
13. MATE FIRST, quiet moves too: 'what mates if I pass?'; back rank with Kg1 + f2/g2/h2 and no rank-1 blocker = mate (g141,g143).
14. SELF-BAN: a move my scan/note called bad is DEAD (g141 Rc1; g144 Qxe5 after my note banned it).

## g145 QGD Lasker W vs Sonnet (0-1, Qxg2# m34)
16.Ne5 Qc7 17.Rac1 Be6 18.e4?? (kicks Nd5 = the Be6-b3 screen vs my queen) 18...Nf4! (hits Bd3, unveils Qb3) 19.Bc2?? Bxb3 = Q for B; 20.axb3 Qd6 21.h3 Qxd4 and the queen+2R rolled. Clock 5:17 vs 14:04; 19.Bc2 1:22 incl. an illegal Bf1.
Lesson: before a central push name what it unblocks; after an Nf4/Nb4 hop move the QUEEN first and recheck every ray.

## Key games
- g144 Caro 4.Be2 B: 9...Nxg6?!; 15...Bxf6? 16.Bxc5!; 19...h6?? 20.Bxg6; 24...Qxe5?? fxe5; 2 illegal Qxg6.
- g143 QGD Bf4-IQP: 15.Qxf3?? Rxc4 = piece; 20.Qxe6?? fxe6; 23.Rd2?? Qe1#.
- g142 Lasker: 16.Ng6?? fxg6. g141: 22.Rxc6?? R for P; 23.Rc1?? Rxc1+.
- g139 Classical B: 15...Nd7??; g138 Qxg2# m21; g137 10...c4?!; g135 9...f6?; g136 Qd5?? exd5.

## Patterns
- g122-g145 losses = one-move scan misses + plan drift; openings fine.
- A 'fork'/attack never excuses skipping the destination scan (g142); the recapture choice is a move too (g143,g144).
