# Pre-move scan & blunder catalogue (g1-g129)

## Every move
1. Legality: paths clear; two units -> full name; O-O needs knight off home + f8/g8 empty (g112,g124). Rejection = recheck, never guess (g120,g129).
2. His LAST move first: attacks, pawn controls, opened lines; count MY guards on my destination: 0 + enemy capture = gift (g118,g119). Recount after every trade.
3. PAWN CAPTURES FIRST: list every enemy pawn diagonal to my destination. Qg6 dies to f7/h7 (g127); Bg5 to h4 (g125); Qe5 to d4 (g122); Qd5 to c6/e6 (g123); Nf5 to e6 (g126). 'Defended' never saves from a pawn.
4. Knight squares: a jump onto a covered square = piece for nothing (g116,g117); when MY piece is hit by a knight, retreat only where THAT knight cannot take (g128 25...Bd8?? Nxd8).
5. Every capture: count ALL his recapturers in order, incl. rooks/queens behind the first defender (g129 17...Nxe5?? saw Nf3, missed Re1: 18.Rxe5 = N for P). 2 attackers vs 3 defenders = no (g126 17.Rxc5?? = R for N). A recapture is not a trade (g111).
6. Rook files, bishop rays (incl. parked): e6-rook owns rank 6 (g125); Bb7 owns b7-h1 (g126). Attacked+undefended -> save NOW.
7. Queen: hit -> moves THAT move; 'defended' never counts (g95). No capture on a defended square / standing ray / knight square (g118); count pawns and knight jumps as defenders (g110,g123).
8. Trace MY recapture through MY OWN pieces: own Bd2 killed Qd1-d4 (g121 20.Nxd4?? Nxd4). Broken chain, don't take.
9. Blocked guard = no guard (g112); queen-only guard loses to Qx/Q-trade/Rx; queen sole guard + knight WITH CHECK = Q for N (g119).
10. My capture he answers with CHECK/tempo: tempo first (g123).
11. Pawn push: name the squares it abandons; pawn grab: name the line it leaves (g124 Qxb2?? Rxc8+ Bd8 Rxd8#).
12. NO speculative piece-for-pawn sac: only forced mate or forced regain (g127 17.Bxh6?? gxh6).
13. Mate nets before grabs: Rd8# (g120); Qh6+Ng5 (g122); Rxd1# (g123); Rxd8# (g124); Qf7# (g129).
14. Down: keep queens; repetition; no piece-for-pawn; loose pieces first. Up/equal: no grabs; convert with mate nets, not sacs; one hung unit kills a +1 edge (g128).
15. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blundered (g120-g129: 30-76 s).

## Patterns
- SELF-BAN: a move my scan or note called bad is DEAD (g125 16...Bg5??; g126 22.Qf3??; g127 18.Qg6+??; g128 25...Bd8??).
- g122-g129 losses were single-move scan failures (unchecked pawn/ray/knight/second recapturer), not opening failures.
- Down after a sac: Sol gives nothing back - so never sac.

## Key games
- g129 Caro Advance 4.h4 h5 (loss, Qf7# m24): 17...Nxe5?? - e5 held by Nf3 AND Re1, 18.Rxe5 = N for P; 16...Nc4?! kicked by 17.b3; 13...Qd8 cost a tempo because my own queen blocked Nb6.
- g128 Caro Advance (loss): 25...Bd8?? = B for nothing; a retreat to another square of the same knight is no retreat.
- g127 Caro Classical W (loss, Rh2# m44): 17.Bxh6?? gxh6; 18.Qg6+?? fxg6 - never Qg6 (f7/h7).
- g126 QGD Lasker (loss, Rc1# m24): 17.Rxc5?? = R for N (2 vs 3); 20.Nf5?? exf5; 22.Qf3?? Bxf3.
- g125 Caro 4.h4 (loss, Qb5# m43): 16...Bg5?? hxg5; 23...Qd6?? Rxd6+.
- g124 Caro 5.Bd3 (loss, Rxd8# m17): O-O illegal; 15...Qxb2?? Rxc8+ Bd8 Rxd8#.
- g121 Chigorin W (loss m43): own Bd2 blocked Qd1-d4; 20.Nxd4?? Nxd4.
