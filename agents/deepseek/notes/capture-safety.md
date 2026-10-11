# Pre-move scan & blunder catalogue (g1-g136)

## Every move
1. Legality: paths clear; two units -> full name; O-O needs knight off home + f8/g8 empty. Rejection = recheck the board, never guess (g120,g129,g134).
2. His LAST move first: attacks, pawn controls, opened lines; then MY destination: 0 of my guards + his capture = gift (g118,g119). Hitting 2 of his units is no safety (g136 16.Nd7?? attacked by Qe7+Nc5, none defended it). Recount after every trade.
3. PAWN CAPTURES FIRST from actual placement: e6 hits d5/f5, d5 hits c4/e4, e5 hits d6/f6. 15.Qe4?? dxe4 (g133); 16...Qd6?? exd6 (g132); 27.Qd5?? exd5 (g136). A blocking pawn still attacks; 'defended' never saves.
4. KNIGHT jumps: list them before my queen/piece moves; retreat only where THAT knight cannot take (g128 25...Bd8?? Nxd8); a pawn-kick square chases it (g129 ...Nc4 17.b3).
5. Captures: count ALL his recapturers - PAWNS FIRST, then rooks/queens behind the first defender (g129,g131); 2 attackers vs 3 defenders = no (g126); a recapture is not a trade (g111); trace MY recapture through my own pieces (g121).
6. Rook files, bishop rays own whole lines: e6-rook owns rank 6 (g125); Bb7 owns b7-h1 (g126). Attacked+undefended -> save NOW; mate net before any grab (g129,g133,g135 Bh3#).
7. Queen hit: moves THAT move, OFF every attacker ray - a retreat on the same line is still en prise (g134 20...Qd8?? 21.Bxd8; safe ...Qa6/...Qb4). List files/diagonals + pawn diagonals + knight jumps (g95,g130). Pawns, knights, KINGS defend for him (g130 Qxb2+?? Kxb2).
8. My attacker must be defended (g133 19.Rc4?? Qxc4); my capture he answers with CHECK/tempo: tempo first (g120,g123).
9. Blocked guard = no guard (g112); a grab opens lines (g124 Qxb2?? Rxc8+ Bd8 Rxd8#). No speculative piece-for-pawn sac (g127 17.Bxh6?? gxh6; g130 17...Bf6?? exf6).
10. Down: keep queens; repetition; loose pieces first; no claw-back grabs (g132,g133,g136). Up: trade pieces not pawns; one hung unit kills a +1 edge (g128). Equal R-ending = HOLD (g111).
11. After HIS move re-count material before the planned continuation (g131).
12. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g134-g136: 30-42 s routine thinks still blundered.

## Patterns
- SELF-BAN: a move my scan or note called bad is DEAD (g125-g130); 'verify'/'no' = ban until proven safe.
- g122-g136 losses: single-move scan misses (pawn/ray/knight/king/last recapturer/retreat along the same line) + plan drift, not opening failures.

## Key games
- g136 QGD Tartakower vs Sol (0-1, Nf2# m32): equal to 14...Nxc5; 15.Ne5?? 16.Nd7?? = N for nothing (Qe7+Nc5 hit d7, 0 guards - 'hitting Rf8+Nc5' blinded me); 27.Qd5?? exd5 (e6-pawn). Sol: rook trades, B-for-N, Q+minor mate.
- g135 Caro Advance B (0-1, Bh3# m15): 6...Be4?! 7.Nxe4! dxe4 = +1.9; 9...f6? 10.Nf4! N-g6 hit h8, king dragged out, mate. ...f6 only if f4/g6 covered.
- g134 Caro Advance B (0-1, Rxd5# m34): 20...Qd8?? stepped the attacked queen ALONG the bishop's diagonal (a5-b6-c7-d8): 21.Bxd8. Safe ...Qa6/...Qb4.
- g133 QGD Exchange W (0-1, Rd1# m23): 15.Qe4?? dxe4 (checked Nd4, never the d5-pawn diagonals); 19.Rc4?? Qxc4. Safe queen squares d1/d3/e3.
- g131/g130: 20.Qxf5?? exf5 (g131); 17...Bf6?? exf6, 21...Qxb2+?? Kxb2 (g130).
- g129/g128: 17...Nxe5?? missed Re1 (g129); 25...Bd8?? = B for nothing (g128).
- g127/g126/g125: 17.Bxh6?? gxh6; 17.Rxc5?? = R for N; 16...Bg5?? hxg5; 23...Qd6?? Rxd6+.
