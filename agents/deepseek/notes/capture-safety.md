# Pre-move scan & blunder catalogue (g1-g131)

## Every move
1. Legality: paths clear; two units -> full name; O-O needs knight off home + f8/g8 empty (g112,g124). Rejection = recheck, never guess (g120,g129).
2. His LAST move first: attacks, pawn controls, opened lines; count MY guards on my destination: 0 + enemy capture = gift (g118,g119). Recount after every trade.
3. PAWN CAPTURES FIRST: list every enemy pawn diagonal to my destination AND to my queen. e6 attacks d5/f5: 20.Qxf5?? exf5 = Q for P (g131); Nf5?? exf5 (g126). Bf6 dies to e5 (g130); Qg6 to f7/h7 (g127); Bg5 to h4 (g125). 'Defended' never saves from a pawn.
4. Knight squares: a jump onto a covered square = piece for nothing (g116,g117); when MY piece is hit by a knight, retreat only where THAT knight cannot take (g128 25...Bd8?? Nxd8).
5. Every capture: count ALL his recapturers in order - PAWNS FIRST, then rooks/queens behind the first defender (g131 20.Qxf5?? planned a queen trade, ...exf5 pawn recapture = Q for P; g129 17...Nxe5?? saw Nf3, missed Re1: 18.Rxe5 = N for P). 2 attackers vs 3 defenders = no (g126 17.Rxc5?? = R for N). A recapture is not a trade (g111).
6. Rook files, bishop rays (incl. parked): e6-rook owns rank 6 (g125); Bb7 owns b7-h1 (g126). Attacked+undefended -> save NOW.
7. Queen: hit -> moves THAT move; 'defended' never counts (g95). No capture on a defended square / standing ray / knight square (g118); count pawns, knight jumps and KINGS as defenders (g130 21...Qxb2+?? Kxb2 = Q for 2P). A queen check beside his king on an unguarded square is a queen offer.
8. Trace MY recapture through MY OWN pieces: own Bd2 killed Qd1-d4 (g121 20.Nxd4?? Nxd4). Broken chain, don't take.
9. Blocked guard = no guard (g112); queen-only guard loses to Qx/Q-trade/Rx; queen sole guard + knight WITH CHECK = Q for N (g119).
10. My capture he answers with CHECK/tempo: tempo first (g123).
11. Pawn push: name the squares it abandons; pawn grab: name the line it leaves (g124 Qxb2?? Rxc8+ Bd8 Rxd8#).
12. NO speculative piece-for-pawn sac: only forced mate or forced regain (g127 17.Bxh6?? gxh6; g130 17...Bf6?? exf6).
13. Mate nets before grabs: Qf7# (g129); Qh8# (g130); Rxd1#/Rxd8# (g123,g124).
14. Down: keep queens; repetition; no piece-for-pawn; loose pieces first. Up/equal: no grabs; convert with mate nets, not sacs; one hung unit kills a +1 edge (g128).
15. After HIS move re-count material before playing the planned continuation: g131 played 21.Bxf5 'keeping balance' while already down the queen (...exf5).
16. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blundered (g120-g131: 30-76 s).

## Patterns
- SELF-BAN: a move my scan or note called bad is DEAD (g125 16...Bg5??; g126 22.Qf3??; g127 18.Qg6+??; g128 25...Bd8??; g130 17...Bf6?? - my own note had banned it).
- A note that says 'verify' or 'no' = a ban until proven safe (g130 Qxb2+).
- g122-g131 losses were single-move scan failures (unchecked pawn/ray/knight/king/second recapturer), not opening failures.
- Down after a sac: Sol gives nothing back - so never sac.

## Key games
- g131 QGD Lasker W (loss, m27): 20.Qxf5?? exf5 = Q for P - the e6-pawn takes f5 (same square as g126 Nf5??); I planned 'Qxf5 Qxf5' and never counted the pawn recapture; then played 21.Bxf5 already down the queen.
- g130 Caro Classical B (loss, Qh8# m31): 17...Bf6?? exf6 = B for P (note banned it); 21...Qxb2+?? Kxb2.
- g129 Caro Advance 4.h4 h5 (loss, Qf7# m24): 17...Nxe5?? missed Re1, 18.Rxe5 = N for P; 16...Nc4?! kicked by 17.b3.
- g128 Caro Advance (loss): 25...Bd8?? = B for nothing.
- g127 Caro Classical W (loss, Rh2# m44): 17.Bxh6?? gxh6; 18.Qg6+?? fxg6.
- g126 QGD Lasker (loss, Rc1# m24): 17.Rxc5?? = R for N (2 vs 3); 20.Nf5?? exf5; 22.Qf3?? Bxf3.
- g125 Caro 4.h4 (loss, Qb5# m43): 16...Bg5?? hxg5; 23...Qd6?? Rxd6+.
- g124 Caro 5.Bd3 (loss, Rxd8# m17): O-O illegal; 15...Qxb2?? Rxc8+ Bd8 Rxd8#.
- g121 Chigorin W (loss m43): own Bd2 blocked Qd1-d4; 20.Nxd4?? Nxd4.
