# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue g1-125
- notes/caro-advance-black.md - Caro B + W 3.Nc3 (g124,g125)
- notes/qgd-white.md - QGD W Lasker/Bxf6
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W (g104,g121)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O needs knight off home + f8/g8 empty (g112,g116,g124); g124 my note said no, I tried it = rejection + clock. Two units -> full name. Blocked line = illegal; rejection = recheck, never guess (g118,g120,g122; g123 Rd7).
- SELF-BAN: a move my scan or note called bad is DEAD (g109,g116,g118,g122,g124; g125 16...Bg5?? hxg5 - the pawn-take class already warned by g122 16...Qxe5?? dxe5).

## Rule 1 - destination sweep (every move)
- COUNT MY GUARDS on my landing square FIRST: 0 + any enemy capture = gift (g118,g119).
- Sweep knight squares, pawn diagonals, rook files, bishop/queen rays; attacked+undefended -> save NOW. CHECK: capturing the checker answers (g115).
- KNIGHT JUMP onto a covered square = piece for nothing (g116,g117).
- PAWN-ATTACKED = off limits: no piece on f6/d6 while his e5-pawn stands (g115,g117,g122); a defender his pawn kicks with tempo = no defender (g119 13...Nc5?). His h4-pawn takes a B on g5 (g125 16...Bg5?? hxg5): before offering a piece list EVERY pawn capture.
- His QUEEN near: her whole line is attacked (g114 21.Nd6??); queen-only guard loses to Qx/Q-trade/Rx; KING-ONLY = no guard.
- MATE NETS first: Qxg2#/Bb7 (g113,g114); Qh2/Rh1 (g118); Rd8# (g120); Qh6+Ng5 (g122); Rxd1# (g123); vs my K e8: Rxc8+ Bd8 Rxd8# (g124).

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). No capture on a defended square, a standing bishop's ray (g105,g108) or a knight square (g118 13.Qxd5?? Nxd5). Checks only if the king cannot take (g106).
- Before ANY queen move list his ranks/files/diagonals: a rook on e6 owns rank 6 (g125 23...Qd6?? Rxd6+ = Q for R).
- QUEEN takes: count EVERY defender incl. PAWNS and knight jumps; his recapture where mine cannot = Q for P/N (g110,g114,g115,g118; g123 16.Qxd5?? c6+e6).
- QUEEN SOLE GUARD + knight capture WITH CHECK = Q for N (g119 16...Qd6?? 17.Nxe6+).
- My capture he answers with CHECK/tempo: tempo first (g120 Qb6?? Qxd7+; g123 Qxd5?? Bxg5+ Qd2 Bxd2+).
- Pawn grab while my king is on an open file deletes my only blocker (g124 15...Qxb2?? 16.Rxc8+ Bd8 17.Rxd8#).

## Rule 3 - captures
- RECAPTURE is not a TRADE (g111 Rxc6?? Rxc6 = R for P): name what I win AND what he wins back. A piece guarded only by my queen dies to Qx + 2nd attacker (g103,g109).
- Trace MY recapture through MY OWN pieces: own Bd2 = Qd1 never retook d4 (g121 20.Nxd4?? Nxd4). Broken chain, don't take.
- PIN = recapturer frozen (g90); X-RAY = rook files/bishop diagonals (g97); blocked recapture -> ...Bxa3! (g112); removing a screen uncovers what's behind (g81 d6, g120 d4).

## Rule 4 - material & clock
- Down: keep queens (repetition); NO grabs; loose pieces first; no piece on his queen's route (g125 35...Rf8?? Qb4+ Qe7+ Qxf8); 5-10 s. Up: trade pieces not pawns; escort passers; promote; stalemate-check.
- Equal R-ending = HOLD; R for P loses (g111). Even material: mate net before any grab (g123 Rxf5?? Rxd1#).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blundered (g120 72 s; g121 45; g122 40; g123 44; g124 32-50; g125 30-41).

## Openings
- Caro B: Advance ...Bf5/Bg6 e6 Nd7 c5 Be7 Rc8 Qb6; NEVER ...Qxd4; no ...Nc5 while d4; nothing on d6/f6 or ...Ngf6 while e5; no ...Qd6 vs Bf4; vs b3/Ba3 ...Bxa3! (g109-g125). 4.h4 h5: 10.c4 cxd4?! loses (g119); vs 12.Qb5+ 12...Qd7! (g120); 5.Bd3 Bxd3 6.Qxd3 (g124,g125): keep Be7 after 12...cxd4 13.cxd4; 14.Bg5+15.Rfc1 wins the c-file; 16...Bg5?? hxg5 = B for P; no ...Qxb2. Classical: f6-knight -> d5/e8; no ...Nc3+/...Bf6/...Qxf4 (g107,g115,g117); 4.Nf3 ...Nh6?! Bxh6 gxh6 (g122).
- Caro W 3.Nc3 (g123): ...Bxd3 Qxd3 e6 Bf4 Ngf6 O-O-O Be7 Ne5 O-O =; 16.Qxd5?? Q for N; K b1 + ...Rad8 vs Rd1: trade rooks/make luft, never grab (23.Rxf5?? Rxd1#).
- QGD W (0-8): Lasker 12.Nxf3!; keep c3+d4+Rc1, no c4; ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 vs c6-bishop. Bxf6: ...Nxd4 ...Bxd4 wins d4; no piece on d4/d5/d6 (g111).
- Ruy Chigorin W (0-6): 13.cxd4: Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (own Bd2 blocks Qd1-d4: g121 19...exd4! 20.Nxd4?? Nxd4). B: no ...Bg4 after 9.h3; 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5 =.
- Dragon B: Rauzer 11...gxf6!; 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5; no e4/Rxe4 grabs; no ...Qa5 after 15.Kb1.
- Alapin/Taimanov B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4!, never 12...Bd6??.
- Italian 4.d3 d5: 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3 (0-3).

## Opponents
- SF19: instant; punishes loose units, queens on his ranks/rays, pawn-attacked squares, d-file pins (g120 13.Rd1!). Down: no self-blocks; repetition works (g119).
- Sonnet 5.5 (g112 1-0; 5L): banks clock; takes every free unit; g121 ...exd4; g122 traded bishops then Qxh6.
- GPT-6.1 Sol (won g114,g115,g117; g123): fast; takes free pieces; wins any back-rank slip.
