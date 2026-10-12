# Pre-move scan & blunder catalogue (g1-g148)

## Every move
1. Legality first: paths clear; two units = full name; after ONE rejection NEVER resend - redraw the board (g144 Qxg6 twice; g137 ...Rc8 illegal with my king on c8).
2. His LAST move first, then MY destination: 0 guards + his capture = gift. Enemy pawns on the target square: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7.
3. SCREENS: moving/trading my piece opens a line to my QUEEN or KING. g145 18.e4?? kicked Nd5, the Be6-b3 screen vs my Qb3 -> 18...Nf4! = Q for B. g146 20.b3?? cleared b2, screen on Bf6-a1 -> 20...Bxa1!. g148 17...Bg5?? moved my Be7 off the g5-f6-e7-d8 diagonal; after 18.Bxg5 his bishop sat on g5 and 19.Bxd8 won my QUEEN - never move/trade the piece between his bishop and my queen.
4. Pawn pushes end guard duty: g135 9...f6? (f7 left g6), g144 19...h6?? (h7 left g6), g147 25...f5?? allowed 26.exf6 e.p. -> mate on g7.
5. PAWN CAPTURES first: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6. 'Defended' never saves (g133,g143,g145,g148 Qd8).
6. Knight retreats only where that knight cannot take AND his queen/rook do not own the square (g139 Nd7, g146 Nc4?).
7. Captures: count ALL recapturers - PAWNS first, then pieces behind the first defender; recapture != trade; a 'trade' needs MY defender on the destination (g141). RECAPTURE CHOICE: keep the recapturer's OTHER guards (g144 15...Bxf6? left e7 unguarded -> 16.Bxc5!).
8. Rook files/bishop rays own whole lines; attacked+undefended -> save NOW. g148 21...Rc7 hung (Nxd8 did not guard c7) -> 22.Rxc7; then the b7-knight hung. Mate net before any grab (g123,g129,g141,g147 26...Nxd4??).
9. QUEEN hit -> she moves THAT move, OFF every attacker ray; 'defended' never counts (g95). g148: she sat on his bishop's g5-d8 diagonal screened only by my Be7 - the screen moved and she fell.
10. Blocked guard = no guard; a piece 'guarded' on a file his rook owns is not guarded (g139,g146); a push abandons guard duty (g137 ...c4?!).
11. Down: keep queens; repetition; loose pieces first; NO grab-back (g132-g148). Up: trade pieces, not pawns.
12. Re-count material FROM THE BOARD after every capture (g131,g138,g141,g148).
13. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g147-g148: 30-46 s routine thinks still blundered (g148 15...Rc8 37 s, 17...Bg5?? 38 s).
14. MATE FIRST, quiet moves too: back rank with Kg1 + f2/g2/h2 and no rank-1 blocker = mate (g141,g143,g146,g147); king on f8 + his rook on the 7th = Rc8# (g148 35.Rc8#).
15. SELF-BAN: a move my scan/note called bad is DEAD (g141 Rc1; g144 Qxe5).

## g148 Caro-Advance B vs Sonnet (0-1, Rc8# m35)
3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O c5 7.c3 Ne7 8.Nbd2 Bg6 9.Nb3 cxd4 10.cxd4 (15 plies). 11.Bf4 Be7 12.Rc1 O-O 13.Bd3 Re8 14.Bxg6 hxg6 15.Qd2 Rc8 16.a3 b5 17.a4 Bg5?? 18.Bxg5 19.Bxd8 won my queen.
- 17...Bg5??: my Be7 screened g5-f6-e7-d8 to my Qd8; trading it let his bishop land on g5 with a clear ray to d8. Same class as g145 Nf4.
- Then the game was gone but I also hung 21...Rc7 (undefended) and 23...Nb7 (undefended). 25...gxh6 won his queen back (g7-pawn spears h6) - keep fighting, but the screen blunder decided it.
- 35.Rc8#: my king on f8, his Ra7 on the 7th; a king cut on rank 8 with a rook on the 7th is mated.

## Key games
- g144 Caro 4.Be2 B: 9...Nxg6?!; 15...Bxf6? 16.Bxc5!; 19...h6?? 20.Bxg6; 24...Qxe5?? fxe5.
- g146 IQP W: 17.Nc4?? Qxc4; 20.b3?? Bxa1; 26.Kf1 Re1#.
- g143 QGD Bf4-IQP: 15.Qxf3?? Rxc4; 20.Qxe6?? fxe6; 23.Rd2?? Qe1#.
- g142 16.Ng6?? fxg6. g141 22.Rxc6?? R for P; 23.Rc1?? Rxc1+.
- g139 15...Nd7??; g138 Qxg2# m21; g137 10...c4?!; g135 9...f6?; g136 Qd5?? exd5.

## Patterns
- Losses = one-move scan misses (screen/guard/recapture) + plan drift; openings fine.
- A 'fork'/attack never excuses skipping the destination scan; the recapture choice is a move too.
- When he chains pawns (g4/f4/f5), counter with a pawn break or piece activity NOW, not a passive retreat.
