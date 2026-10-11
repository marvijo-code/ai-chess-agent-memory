# Pre-move scan & blunder catalogue (g1-g135)

## Every move
1. Legality: paths clear; two units -> full name; O-O needs knight off home + f8/g8 empty. Rejection = recheck the board, never guess (g120,g129,g134).
2. His LAST move first: attacks, pawn controls, opened lines; count MY guards on my destination: 0 + enemy capture = gift (g118,g119). Recount after every trade.
3. PAWN CAPTURES FIRST from actual placement: e6 hits d5/f5, d5 hits c4/e4, e5 hits d6/f6. 15.Qe4?? dxe4 = Q for P (g133); 16...Qd6?? exd6 (g132). A blocking pawn still attacks.
4. KNIGHT jumps: list them before my queen/piece moves; retreat only where THAT knight cannot take (g128 25...Bd8?? Nxd8); a pawn-kick square chases it (g129 ...Nc4 17.b3).
5. Captures: count ALL his recapturers - PAWNS FIRST, then rooks/queens behind the first defender (g129,g131); 2 attackers vs 3 defenders = no (g126); a recapture is not a trade (g111); trace MY recapture through my own pieces (g121 own Bd2).
6. Rook files, bishop rays own whole lines: e6-rook owns rank 6 (g125); Bb7 owns b7-h1 (g126). Attacked+undefended -> save NOW; mate net before any grab (g129,g133,g135 Bh3#).
7. Queen hit: moves THAT move, OFF every attacker ray - a retreat on the same line is still en prise (g134 20...Qd8?? 21.Bxd8; safe ...Qa6/...Qb4). List files/diagonals + pawn diagonals + knight jumps (g95,g130). Pawns, knights, KINGS defend for him (g130 Qxb2+?? Kxb2); queen sole guard + knight WITH CHECK = Q for N (g119).
8. My attacker must be defended (g133 19.Rc4?? Qxc4); my capture he answers with CHECK/tempo: tempo first (g120,g123).
9. Blocked guard = no guard (g112); a pushed pawn abandons squares; a grab opens lines (g124 Qxb2?? Rxc8+ Bd8 Rxd8#). No speculative piece-for-pawn sac (g127 17.Bxh6?? gxh6; g130 17...Bf6?? exf6).
10. Down: keep queens (Sol gives nothing back after a sac); repetition; loose pieces first; no claw-back grabs (g132,g133). Up: trade pieces not pawns; one hung unit kills a +1 edge (g128). Equal R-ending = HOLD (g111).
11. After HIS move re-count material before the planned continuation (g131).
12. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g134: 30-40 s routine, ended 5:57 vs 20:39.

## Patterns
- SELF-BAN: a move my scan or note called bad is DEAD (g125-g130); 'verify'/'no' = ban until proven safe.
- g122-g135 losses: single-move scan misses (pawn/ray/knight/king/last recapturer/retreat on the same line) + plan drift, not opening failures.

## Key games
- g135 Caro Advance B (loss, Bh3# m15): 6...Be4?! 7.Nxe4! dxe4 = +1.9 White; 9...f6? 10.Nf4! Nf4-g6 hit h8 (exchange gone), my king dragged out, mate. Play ...f6 only if f4/g6 are covered.
- g134 Caro Advance B (loss, Rxd5# m34): 20...Qd8?? stepped the attacked queen ALONG the attacking bishop's diagonal (a5-b6-c7-d8) - 21.Bxd8 = Q for B; safe ...Qa6/...Qb4. Clamp 4.h4/6.g4 = no castling for me; queen shuffled to the wall.
- g133 QGD Exchange W (loss, Rd1# m23): 15.Qe4?? dxe4 = Q for P (checked the d4-knight, never the d5-pawn diagonals); 16.Bxe4 Ne2+; grabs ignored 22...Rad8 Rd1#. Safe queen squares: d1/d3/e3.
- g131 QGD Lasker W: 20.Qxf5?? exf5. g130 Caro Classical B: 17...Bf6?? exf6; 21...Qxb2+?? Kxb2.
- g129 Caro Advance: 17...Nxe5?? missed Re1 (18.Rxe5); 16...Nc4?! b3. g128: 25...Bd8?? = B for nothing.
- g127: 17.Bxh6?? gxh6; 18.Qg6+?? fxg6. g126: 17.Rxc5?? = R for N (2 vs 3); 22.Qf3?? Bxf3. g125: 16...Bg5?? hxg5; 23...Qd6?? Rxd6+.
