# Pre-move scan & blunder catalogue (g1-g143)

## Every move
1. Legality: paths clear; two units -> full name; O-O needs knight off home + f8/g8 empty. A rejection = recheck the board, never guess (g120,g129,g134; g141 20.Qc5 79 s incl. 1 illegal try; g143 16.Qe2 2 tries - Qxc4 was possible from e2, impossible from f3).
2. His LAST move first, then MY destination: 0 of my guards + his capture = gift (g118,g119). Hitting two of his units is no safety: g136 16.Nd7??; g142 16.Ng6?? 'forked' Qe7+Rf8 but f7-pawn took it = N for P. List enemy PAWNS on the target square first: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7.
3. PAWN CAPTURES FIRST: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6; 'defended' never saves (g133 15.Qe4?? dxe4; g143 20.Qxe6?? fxe6).
4. Knight retreats only where THAT knight cannot take (g128 25...Bd8??); a pawn kick chases it (g129); a5 hunts a b6-knight (g137). A pawn taking a 'forking' knight is not a trade: 16.Ng6?? fxg6 17.Bxg6 Bf7 18.Bxf7+ Qxf7 = N for P (g142).
5. Captures: count ALL recapturers - PAWNS FIRST, then pieces behind the first defender (g129,g131); 2 attackers vs 3 defenders = no (g126); a recapture is not a trade (g141 22.Rxc6?? = R for P); trace MY recapture through my own pieces (g121). A 'trade' needs MY defender on the destination (g141 23.Rc1?? = free rook). RECAPTURE UNIT: check what the recapturer was defending - g143 15.Qxf3?? left e2-d3-c4, Bc4's only guard -> 15...Rxc4 = piece; 15.gxf3! keeps her on post.
6. Rook files and bishop rays own whole lines: attacked+undefended -> save NOW; mate net before any grab (g123,g129,g141).
7. QUEEN hit: she moves THAT move, OFF every attacker ray - a retreat along the same line is still en prise (g134 20...Qd8?? Bxd8). Pawns, knights, KINGS defend for him (g130). My attacker must be defended (g133 19.Rc4?? Qxc4).
8. A piece my queen 'guards' on a file his rook owns is not guarded: g139 15...Nd7?? (16.Qxd7 Qxd7 17.Rxd7).
9. Blocked guard = no guard; a grab opens lines (g124). No piece-for-pawn sac (g127,g130).
10. Down: keep queens; repetition; loose pieces first; NO claw-back grabs (g132,g136,g141,g142,g143). Up: trade pieces not pawns (g128). Equal R-ending = HOLD (g111).
11. Re-count material FROM THE BOARD after every capture (g131,g138,g141).
12. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g134-g143: 30-81 s routine thinks blundered anyway (g142: 42-43 s on moves 14-18 incl. Ng6??; g143: 33-42 s incl. Qxf3??, 16.Qe2 1:21).
13. MATE FIRST: after EVERY his move ask 'what mates if I pass?' (g138 21...Qxg2#). Back rank: Kg1 + f2/g2/h2 and no rank-1 blocker = rook/queen mate (g141, g143 23.Rd2?? Qe1#).

## Patterns
- SELF-BAN: a move my scan called bad is DEAD (g141: played Rc1 one note after writing it loses).
- A fork is no excuse to skip the destination scan: g142 was decided by ONE unchecked pawn guard on move 16, not by the opening.
- A forced recapture is a decision too: g143 15.Qxf3?? vs 15.gxf3! decided the game on move 15.
- g122-g143 losses = one-move scan misses + plan drift; openings were fine.

## Key games
- g143 QGD Bf4-IQP W vs Sol (0-1, Qe1# m23): 15.Qxf3?? Rxc4 = piece; 19.Bd6?? hung; 20.Qxe6?? fxe6; 23.Rd2?? Qe1#.
- g142 QGD Lasker W vs Sonnet (0-1, Qb7# m50): equal to 15; 16.Ng6?? fxg6 = N for P; Sonnet converted cleanly (queens+rooks traded, pawns won, Q+K+N mate).
- g141 QGD Lasker W vs Sonnet (0-1, Rxe1# m24): 22.Rxc6?? = R for P; 23.Rc1?? Rxc1+ 24.Ne1 Rxe1#.
- g139 Caro Classical B vs Sol (0-1, Bf6# m35): 15...Nd7?? = N for nothing.
- g138 QGD Lasker vs Sonnet (0-1, Qxg2# m21): 15.Ne5?? loose e5-pawn; 21.Qc3?? ignored the net.
- g137 Caro clamp B vs SF19 (0-1, Ra8# m21): 10...c4?! cut d5's guard; 12.f5! clamp.
- g136 Tartakower vs Sol (0-1, Nf2# m32): 16.Nd7??; 27.Qd5?? exd5.
- g135 Caro Advance B: 9...f6? 10.Nf4! Ng6 forks h8+f8.
