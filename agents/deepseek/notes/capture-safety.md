# Pre-move scan & blunder catalogue (g1-g134)

## Every move
1. Legality: paths clear; two units -> full name; O-O needs knight off home + f8/g8 empty (g112,g124). Rejection = recheck the board, never guess (g120,g129,g134 - 2 illegal tries).
2. His LAST move first: attacks, pawn controls, opened lines; count MY guards on my destination: 0 + enemy capture = gift (g118,g119). Recount after every trade.
3. PAWN CAPTURES FIRST - from the ACTUAL pawn placement: e6 hits d5/f5, d5 hits c4/e4, e5 hits d6/f6. 15.Qe4?? dxe4 = Q for P (g133); 16...Qd6?? exd6 (g132); 20.Qxf5?? exf5 (g131). A blocking pawn still attacks; 'defended' never saves.
4. KNIGHT squares: list his knight's jump set before my queen/piece moves: Nd4 hits b3 c2 e2 e6 f3 f5 (g133: e2/e4 pawn-mined; safe Qd1/Qd3/Qe3). Jump onto a covered square = piece for nothing; retreat only where THAT knight cannot take (g128).
5. Every capture: count ALL his recapturers in order - PAWNS FIRST, then rooks/queens behind the first defender (g129,g131). 2 attackers vs 3 defenders = no (g126). A recapture is not a trade (g111).
6. Rook files, bishop rays (incl. parked), own whole lines: e6-rook owns rank 6 (g125); Bb7 owns b7-h1 (g126). Attacked+undefended -> save NOW.
7. Queen: hit -> moves THAT move, and OFF EVERY RAY of the attacker - a retreat along the same line is still en prise (g134 20...Qd8?? on a5-b6-c7-d8: 21.Bxd8 Q for B; safe ...Qa6/...Qb4). List ranks/files/diagonals + every enemy pawn diagonal + every knight jump. Defenders never save (g95); pawns, knights and KINGS count as his defenders (g130 21...Qxb2+?? Kxb2).
8. Queen attack: my attacker must be defended or she just captures it (g133 19.Rc4?? Qxc4 = R for nothing).
9. Trace MY recapture through MY OWN pieces: own Bd2 killed Qd1-d4 (g121). Broken chain, don't take.
10. Blocked guard = no guard (g112); queen-only guard loses to Qx/Q-trade/Rx; queen sole guard + knight WITH CHECK = Q for N (g119).
11. My capture he answers with CHECK/tempo: tempo first (g123).
12. Pawn push: name squares it abandons; pawn grab: name the line it leaves (g124 Qxb2?? Rxc8+ Bd8 Rxd8#).
13. NO speculative piece-for-pawn sac: only forced mate or forced regain (g127 17.Bxh6?? gxh6; g130 17...Bf6?? exf6).
14. Mate nets before grabs: Qf7# (g129); Qh8# (g130); Rd1# (g133); Rxd5# (g134).
15. Down: keep queens; repetition; no piece-for-pawn; loose pieces first. Up/equal: no grabs; one hung unit kills a +1 edge (g128).
16. After HIS move re-count material before the planned continuation (g131).
17. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g134: 30-40 s routine moves, 1:14/1:03 + 2 illegal tries, ended 5:57 vs 20:39 - long thinks blunder anyway.

## Patterns
- SELF-BAN: a move my scan or note called bad is DEAD (g125-g130).
- A note that says 'verify' or 'no' = a ban until proven safe (g130 Qxb2+).
- g122-g134 losses: single-move scan failures (unchecked pawn/ray/knight/king/second recapturer/own-line retreat), not opening failures.
- Down after a sac: Sol gives nothing back - never sac.

## Key games
- g134 Caro Advance B (loss, Rxd5# m34): 20...Qd8?? stepped the attacked queen along the attacking bishop's diagonal (a5-b6-c7-d8) - 21.Bxd8 = Q for B; safe ...Qa6/...Qb4. Rest of game: clamping h5/g4/f4 + no castling for me, queen shuffled to the wall. 30-40 s routine moves.
- g133 QGD Exchange W (loss, Rd1# m23): 15.Qe4?? dxe4 = Q for P - I checked the d4-knight was undefended but never the d5-pawn's diagonals; 16.Bxe4 Ne2+ forked K+R; then I grabbed (20.Bxb7, 23.Ba8) while 22...Rad8 set Rd1#. Safe queen squares were d1/d3/e3. 12.Rc1 took 70 s + 1 illegal try.
- g131 QGD Lasker W: 20.Qxf5?? exf5; played on already down the queen.
- g130 Caro Classical B: 17...Bf6?? exf6 = B for P; 21...Qxb2+?? Kxb2.
- g129 Caro Advance: 17...Nxe5?? missed Re1, 18.Rxe5 = N for P; 16...Nc4?! kicked by b3.
- g128 Caro Advance: 25...Bd8?? = B for nothing. g127: 17.Bxh6?? gxh6; 18.Qg6+?? fxg6.
- g126 QGD: 17.Rxc5?? = R for N (2 vs 3); 22.Qf3?? Bxf3. g125: 16...Bg5?? hxg5; 23...Qd6?? Rxd6+.
- g124: O-O illegal; 15...Qxb2?? Rxc8+ Bd8 Rxd8#.
