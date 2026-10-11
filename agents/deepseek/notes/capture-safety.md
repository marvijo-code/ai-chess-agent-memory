# Pre-move scan & blunder catalogue (g1-g144)

## Every move
1. Legality: paths clear; two units -> full name; O-O needs knight off home + f8/g8 empty. A rejection = recheck the board, never guess (g120,g129,g134,g141,g143). After ONE rejection NEVER resend: g144 20...Qxg6 tried twice (a queen on e7 has no line to g6) = 1:43 lost, 2 of 3 strikes.
2. His LAST move first, then MY destination: 0 of my guards + his capture = gift (g118,g119). Hitting two of his units is no safety (g136,g142). List enemy PAWNS on the target square first: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7.
3. PAWN CAPTURES FIRST: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6; 'defended' never saves (g133,g143). A pawn recapture kills trades: g144 24...Qxe5?? fxe5 (Q+R for R+P) even though my own note banned it 2 plies earlier.
4. Knight retreats only where THAT knight cannot take (g128); a pawn kick chases it (g129); a5 hunts a b6-knight (g137). A pawn taking a 'forking' knight is not a trade (g142).
5. Captures: count ALL recapturers - PAWNS FIRST, then pieces behind the first defender (g129,g131); 2 attackers vs 3 defenders = no (g126); recapture != trade (g141). A 'trade' needs MY defender on the destination. RECAPTURE CHOICE: keep the recapturer's OTHER guards - g144 15...Bxf6? left e7, the c5-knight's only guard -> 16.Bxc5!; ...Qxf6/...gxf6 keeps e7. g143 15.Qxf3?? left Bc4's only guard -> 15...Rxc4; 15.gxf3!.
6. Rook files and bishop rays own whole lines: attacked+undefended -> save NOW; mate net before any grab (g123,g129,g141).
7. QUEEN hit: she moves THAT move, OFF every attacker ray - a retreat along the same line is still en prise (g134). Pawns, knights, KINGS defend for him (g130). My attacker must be defended (g133).
8. A piece he 'guards' on a file his rook owns is not guarded (g139).
9. Blocked guard = no guard; a grab opens lines (g124). No piece-for-pawn sac (g127,g130).
10. Down: keep queens; repetition; loose pieces first; NO claw-back grabs (g132,g136,g141,g142,g143,g144). Up: trade pieces not pawns (g128). Equal R-ending = HOLD (g111).
11. Re-count material FROM THE BOARD after every capture (g131,g138,g141).
12. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g134-g144: 30-81 s routine thinks blundered anyway (g144: 33-39 s on moves 6-15 incl. f6?!, Bxf6?, h6??, plus 1:43 on the illegal Qxg6).
13. MATE FIRST: after EVERY his move ask 'what mates if I pass?' (g138,g141,g143). Back rank: Kg1 + f2/g2/h2 and no rank-1 blocker = mate (g141,g143).
14. PAWN PUSHES that were guards: before ...h6/...f6 name what the pawn still guards - g144 19...h6?? removed h7, the g6-knight's ONLY guard -> 20.Bxg6; g135 9...f6 removed f7, g6's only pawn guard -> Nf4-g6 fork. An attacked g6 piece: move the piece.

## Patterns
- SELF-BAN: a move my scan called bad is DEAD (g141 Rc1); g144 played 24...Qxe5 after my own note wrote 'Qxe5?? loses Q to fxe5' 2 plies earlier.
- A fork is no excuse to skip the destination scan (g142).
- A forced recapture is a decision too (g143); so is the choice of recapturer (g144).
- g122-g144 losses = one-move scan misses + plan drift; openings were fine.

## Key games
- g144 Caro Advance 4.Be2 B vs SF19 (0-1, Qe8# m28): 9...Nxg6?!; 14...f6?! 15.exf6! 15...Bxf6? 16.Bxc5 won the Nc5; 19...h6?? 20.Bxg6; 24...Qxe5?? fxe5. 2 illegal Qxg6 tries.
- g143 QGD Bf4-IQP W vs Sol (0-1, Qe1# m23): 15.Qxf3?? Rxc4 = piece; 19.Bd6?? hung; 20.Qxe6?? fxe6; 23.Rd2?? Qe1#.
- g142 QGD Lasker W vs Sonnet (0-1, Qb7# m50): equal to 15; 16.Ng6?? fxg6 = N for P.
- g141 QGD Lasker W vs Sonnet (0-1, Rxe1# m24): 22.Rxc6?? = R for P; 23.Rc1?? Rxc1+.
- g139 Caro Classical (0-1, Bf6# m35): 15...Nd7??; g138 Qxg2# m21; g137 clamp 10...c4?! (12.f5!); g135 9...f6?; g136 27.Qd5?? exd5.
