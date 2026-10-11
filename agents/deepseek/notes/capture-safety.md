# Pre-move scan & blunder catalogue (g1-g127)

## Every move
1. Legality: paths clear; two units -> full name; O-O needs knight off home + f8/g8 empty (g112,g116,g124). Rejection = recheck, never guess (g120,g122,g124).
2. Why did HIS last move come? Attacks, pawn controls, opened lines; then COUNT MY GUARDS on my destination: 0 + enemy capture = gift (g118,g119). Recount guards after every trade.
3. PAWN CAPTURES FIRST: list every enemy pawn diagonal to my destination before ANY move: Qg6 dies to f7/h7 (g127 18.Qg6+?? fxg6); Bg5 to h4 (g125); Qe5 to d4 (g122); Qd5 to c6/e6 (g123); Nf5 to e6 (g126). 'Defended' never saves a piece from a pawn.
4. Knight jump onto a covered square = piece for nothing (g116,g117,g121). Sweep his knights' squares + his king before any queen move.
5. Rook files, bishop rays (incl. parked): rook e6 owns rank 6 (g125 23...Qd6?? Rxd6+); Bb7 owns b7-h1 (g126 22.Qf3?? Bxf3). Attacked+undefended -> save NOW.
6. Queen: hit -> moves THAT move. No capture on a defended square or a standing ray (g118 13.Qxd5?? Nxd5). Count EVERY defender incl. pawns and knight jumps (g110,g123).
7. Captures: name what I win AND what he wins back; attackers vs defenders - 2 vs 3 = no capture (g126 17.Rxc5?? Rxc5 18.Rxc5 Qxc5 = R for N); a recapture is not a trade (g111 Rxc6?? = R for P).
8. Trace MY recapture through MY OWN pieces: own Bd2 killed Qd1-d4 (g121 20.Nxd4?? Nxd4). Broken chain, don't take.
9. Blocked guard = no guard (g112); queen-only guard loses to Qx/Q-trade/Rx; queen sole guard + knight WITH CHECK = Q for N (g119 16...Qd6?? 17.Nxe6+).
10. My capture he answers with CHECK/tempo: tempo first (g123 Qxd5?? Bxg5+ Qd2 Bxd2+).
11. Pawn push: name the squares it abandons; pawn grab: name the line it leaves (g124 15...Qxb2?? 16.Rxc8+ Bd8 17.Rxd8#).
12. NO speculative piece-for-pawn sac: only a forced mate or forced regain (g127 17.Bxh6?? gxh6 = B for P, then Qg6 fxg6 = Q; Sol gives nothing back).
13. Mate nets before grabs: Rd8# (g120); Qh6+Ng5 (g122); Rxd1# (g123); Rxc8+Bd8 Rxd8# (g124); Rc1# (g126); Rh2# (g127).
14. Down: keep queens; repetition; no piece-for-pawn; loose pieces first. Up/equal: no grabs; convert with mate nets, not sacs; stalemate-check.
15. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blundered (g120-g127: 30-72 s).

## Patterns
- SELF-BAN: a move my scan or note called bad is DEAD (g124 O-O; g125 16...Bg5??; g126 22.Qf3??; g127 18.Qg6+??).
- g122-g127 losses were one-move scan failures (an unchecked pawn/ray capture), not opening failures. Equal positions threw away by a single unlisted enemy capture.
- Down after a sac: Sol gives nothing back; resignable at once - so never sac.

## Key games
- g127 Caro Classical W (0-1, Rh2# m44): 15.d5! exd5 16.cxd5 Re8 = space edge; 17.Bxh6?? gxh6 (B for P); 18.Qg6+?? fxg6 (Q for P; f7/h7 pawns); down Q, mate m44. No sac without forced mate; never Qg6.
- g126 QGD Lasker (0-1, Rc1# m24): 17.Rxc5?? = R for N (3 defenders vs 2); 20.Nf5?? exf5 (N for P); 22.Qf3?? Bxf3 (Q for B+P on b7-h1).
- g125 Caro 4.h4 (0-1, Qb5# m43): 16...Bg5?? hxg5; 23...Qd6?? Rxd6+; 35...Rf8?? queen's route. ...Nb6/...Nc4 fine.
- g124 Caro 5.Bd3 (0-1, Rxd8# m17): O-O illegal (Ng8 home); 15...Qxb2?? 16.Rxc8+ Bd8 17.Rxd8#.
- g123 Caro W 3.Nc3 (0-1, Rxd1# m23): 16.Qxd5?? Q for N; 23.Rxf5?? Rxd1# (no luft, K b1).
- g122/g120/g119: Qxe5?? dxe5; Qb6?? Qxd7+; Qd6?? Nxe6+.
- g121 Chigorin W (0-1 m43): own Bd2 blocked Qd1-d4; 20.Nxd4?? Nxd4.
