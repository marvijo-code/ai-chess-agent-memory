# Pre-move scan & blunder catalogue (g1-g141)

## Every move
1. Legality: paths clear; two units -> full name; O-O needs knight off home + f8/g8 empty. A rejection = recheck the board, never guess (g120,g129,g134; g141 20.Qc5 1 illegal try, 79 s).
2. His LAST move first (attacks, pawn controls, opened lines), then MY destination: 0 of my guards + his capture = gift (g118,g119). Hitting two of his units is no safety (g136 16.Nd7?? Qe7+Nc5 hit it, it had 0 guards). Recount after every trade.
3. PAWN CAPTURES FIRST: e6 hits d5/f5, d5 hits c4/e4, e5 hits d6/f6; a blocking pawn still attacks; 'defended' never saves (g133 15.Qe4?? dxe4 - 3rd Q-for-P).
4. Knight retreats only where THAT knight cannot take (g128 25...Bd8?? Nxd8); a pawn kick chases it (g129); a5 hunts a b6-knight (g137).
5. Captures: count ALL recapturers - PAWNS FIRST, then pieces behind the first defender (g129,g131); 2 attackers vs 3 defenders = no (g126); a recapture is not a trade (g111, g141 22.Rxc6?? Rxc6 = R for P - the pawn's guard was the rook behind it); trace MY recapture through my own pieces (g121). A 'trade' move needs MY defender on the destination (g141 23.Rc1?? nothing of mine defended c1 = free rook).
6. Rook files and bishop rays own whole lines: attacked+undefended -> save NOW; mate net before any grab (g123,g129,g133,g141 23.Rc1?? on Rc6's file).
7. QUEEN hit: she moves THAT move, OFF every attacker ray - a retreat along the same line is still en prise (g134 20...Qd8?? Bxd8; safe Qa6/Qb4). Pawns, knights, KINGS defend for him (g130 Qxb2+?? Kxb2). My attacker must be defended (g133 19.Rc4?? Qxc4); his check/tempo first.
8. A piece my queen 'guards' on a file his rook owns is not guarded: g139 15...Nd7?? ('defended' by Qd8; 16.Qxd7 Qxd7 17.Rxd7 = +N, Rd1 stood on the file all game). Name his rook on that file and the whole recapture chain before any retreat.
9. Blocked guard = no guard; a grab opens lines (g124 Qxb2?? Rxc8+ Rxd8#). No speculative piece-for-pawn sac (g127 17.Bxh6??; g130 17...Bf6?? exf6).
10. Down: keep queens; repetition; loose pieces first; NO claw-back grabs (g132,g133,g136,g141). Up: trade pieces not pawns; one hung unit kills a +1 edge (g128). Equal R-ending = HOLD (g111).
11. Re-count material FROM THE BOARD after every his move (g131; g138 called 16.dxe5 a win - it was a recapture; g141 'up a pawn' when down R for P).
12. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g134-g141: 30-79 s routine thinks blundered anyway (g141 22.Rxc6?? 39 s; 20.Qc5 79 s incl. an illegal try).
13. MATE FIRST: after EVERY his move (quiet too) ask 'what mates if I pass?' - g138 21...Qxg2#: his Qd5 backed along c6-d5-e4-f3-g2 by Bc6; Rf1/h2-pawn guarded nothing. Block the diagonal (e4) or trade queens. Back rank: Kg1 + f2/g2/h2 and no rank-1 blocker = his rook checks mate (g141 Rxc1+ Ne1 Rxe1#).

## Patterns
- SELF-BAN: a move my scan or note called bad is DEAD; 'maybe' stays banned until checked off-board (g141: played Rc1 one note after writing it loses).
- g122-g141 losses = one-move scan misses (pawn/ray/knight/king/last recapturer/retreat on the same line/pinned guard/mate net) + plan drift, not opening failures.

## Key games
- g141 QGD Lasker W vs Sonnet (0-1, Rxe1# m24): equal to 21...b6; 22.Rxc6?? Rxc6 = R for P (c6 guarded by Rc8; my 'trade' never existed); 23.Rc1?? Rxc1+ 24.Ne1 Rxe1#. My own note wrote 'Rc1 loses to Rxc1' and I played it anyway.
- g139 Caro Classical B vs Sol (0-1, Bf6# m35): equal to 15; 15...Nd7?? = N for nothing (see 8) - retreat ...Ne8, never onto Rd1's file.
- g138 QGD Lasker vs Sonnet (0-1, Qxg2# m21): 15.Ne5?? only trades, then e5-pawn loose (e3 blocks Qe2's file); 21.Qc3?? ignored the g2 net.
- g137 Caro clamp B vs SF19 (0-1, Ra8# m21): 10...c4?! cut d5's guard; 12.f5! clamp; 20.Nxd5! forks Qc7+Be7, 21.Ra8#.
- g136 Tartakower vs Sol (0-1, Nf2# m32): 16.Nd7?? Qe7+Nc5 hit it, 0 guards; 27.Qd5?? exd5.
- g135 Caro Advance B: 9...f6? 10.Nf4! Ng6 forks h8+f8 (f7 was g6's only pawn guard).
- g134/g133: 20...Qd8?? Bxd8 (g134); 15.Qe4?? dxe4, 19.Rc4?? Qxc4 (g133).
