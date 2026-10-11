# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue g1-123
- notes/caro-advance-black.md - Caro B lines + W 3.Nc3 (g123)
- notes/qgd-white.md - QGD W Lasker/Bxf6
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W (g104,g121)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O: knight off home, f8/g8 empty, path clear (g112,g116). Two units -> full name. Own piece blocks a line = illegal; rejection = recheck, never guess (g118,g120,g122; g123 Rd7: rook was his check's blocker).
- SELF-BAN: a move my scan or note called bad is DEAD (g109,g116,g118,g122).

## Rule 1 - destination sweep (every move)
- COUNT MY GUARDS on my landing square FIRST: 0 + any enemy capture = gift (g118 11.Bf4??; g119 20...Nxf2?? Kxf2).
- Sweep knight squares, pawn diagonals, rook files, bishop/queen rays; attacked+undefended -> save NOW. CHECK: capturing the checker answers (g115 18...Nc3+?? Qxc3).
- KNIGHT JUMP onto a covered square = piece for nothing (g116,g117): bishop rays, pawns, knights, king first.
- PAWN-ATTACKED = off limits. No piece on f6/d6 while his e5-pawn stands (g115,g117; g122 14...Bf6? exf6, 17...Rfe8?? exf6). A defender his pawn kicks with tempo = no defender (g119 13...Nc5?). Pawn capture w/ check: b6 after dxc5+ (g120 13...Qb6??).
- His QUEEN near: her whole line is attacked (g114 21.Nd6??). A bare pawn in her line = free grab (g116 15.Qxd5). Queen-only guard loses to Qx/Q-trade/Rx; KING-ONLY = no guard.
- MATE NETS first: Qxg2#/Bb7 (g113,g114); Qh2/Rh1 (g118); Rd8# (g120); Qh6+Ng5 (g122); his rook vs my d1-rook, K b1 + a2/c2 pawns = Rxd1# (g123 23.Rxf5??).

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). No capture on a defended square, a standing bishop's ray (g105,g108) or a knight square (g118 13.Qxd5?? Nxd5). Checks only if the king cannot take (g106).
- QUEEN takes a pawn/piece: count EVERY defender incl. PAWNS and knight jumps; his recapture where mine cannot = Q for P/N (g110,g114,g115,g118; g122 16...Qxe5?? dxe5; g123 16.Qxd5?? c6+e6 held d5).
- QUEEN SOLE GUARD + knight capture WITH CHECK = Q for N (g119 16...Qd6?? 17.Nxe6+).
- My capture he answers with a CHECK or tempo capture: tempo first; if my queen must block on the square he takes her, Q lost (g123 Qxd5?? Bxg5+ Qd2 Bxd2+; g120 Qb6?? Qxd7+ then dxc5+).

## Rule 3 - captures
- RECAPTURE is not a TRADE (g111 26.Rxc6?? Rxc6 = R for P): name what I win AND what he wins back. A piece guarded only by my queen dies to Qx + 2nd attacker (g103,g109).
- Trace MY recapture line through MY OWN pieces: own Bd2 on d2 = Qd1 could never retake d4 (g121 20.Nxd4?? Nxd4 = piece for nothing). Broken chain, don't take.
- PIN = recapturer frozen (g90); X-RAY = his rook files/bishop diagonals (g97); blocked recapture -> ...Bxa3! (g112). Removing a screen uncovers the attack behind (g81 d6, g120 d4).

## Rule 4 - material & clock
- Down: keep queens (repetition); NO grabs; move loose pieces first; blockaders home (g117); 5-10 s. Up: trade pieces not pawns; escort passers; promote; stalemate-check.
- Equal R-ending = HOLD; R for P loses (g111). Even up material, check the mate net before any grab (g123 23.Rxf5?? Rxd1#).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blundered (g120 72 s; g121 45 s; g122 40 s; g123 44 s).

## Openings
- Caro B (all lines): Advance: ...Bf5/Bg6 e6 Nd7 c5 Be7 Rc8 Qb6; NEVER ...Qxd4; no ...Nc5 while d4 stands; nothing on d6/f6 or ...Ngf6 while e5 stands; no ...Qd6 vs Bf4; vs b3/Ba3 ...Bxa3! (g109-g122). 4.h4 h5: 10.c4 cxd4?! loses (g119); vs 12.Qb5+ 12...Qd7! not 12...Nd7?! 13.Rd1! (g120). Classical: f6-knight -> d5/e8 only; no ...Nc3+/...Bf6/...Qxf4 (g107,g115,g117). 4.Nf3: ...Nh6?! Bxh6 gxh6 weakens h6 (g122).
- Caro W 3.Nc3 (g123, 0-1): ...Bxd3 Qxd3 e6 Bf4 Ngf6 O-O-O Be7 Ne5 O-O Bg5 Nxe5 dxe5 =; 16.Qxd5?? Q for N; after ...Rad8 vs my Rd1 (K b1): trade rooks or make luft, never grab (23.Rxf5?? Rxd1#).
- QGD W (0-8): Lasker 12.Nxf3!; keep c3+d4+Rc1, no c4 (g111); ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 vs a c6-bishop. Bxf6: ...Nxd4 ...Bxd4 wins d4; no piece on d4/d5/d6.
- Ruy Chigorin W (0-6): 13.cxd4: Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (own Bd2 blocks Qd1-d4: 19...exd4! 20.Nxd4?? Nxd4, g121). B: no ...Bg4 after 9.h3; 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5! =.
- Dragon B: Rauzer 11...gxf6!; 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5; no e4/Rxe4 grabs; no ...Qa5 after 15.Kb1.
- Alapin/Taimanov B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4!, never 12...Bd6??.
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3.

## Opponents
- SF19: instant; punishes loose units, queens on attacked lines, pawn-attacked squares, d-file pins (g120 13.Rd1!). Down: king g8/h7, no self-blocks (g120 20...Ne7?? 21.Rd8#); repetition works (g119).
- Sonnet 5.5 (1W g112, 4L g116,g118,g121,g122): banks clock; takes every free/attacked unit; g121 ...exd4 won a piece (my Bd2 blocked Qd1); g122 traded both bishops then Qxh6 on the weak h-pawn.
- GPT-6.1 Sol (won g114,g115,g117; g123): fast; takes every free piece/piece on a pawn square; queen grabs pawns when unpunished (g123 21...Qxf2??) yet wins any back-rank slip (23.Rxf5?? Rxd1#).
