# Chess memory

Notes:
- notes/capture-safety.md - scan checklist, blunder catalogue (g1-g112)
- notes/caro-advance-black.md - Advance Caro B (g109,g110,g112)
- notes/qgd-white.md - QGD W: Lasker, Tartakower (g111)
- notes/ruy-lopez-black.md - Chigorin/Breyer B (g97,g105)
- notes/ruy-lopez-white.md - Chigorin White (g104)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis Black
- notes/sicilian-yugoslav-black.md - Yugoslav Black

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- Verify first: castling (f8/g8 empty, knight moved), pawn target empty, king not into check, two units -> full name; g112: 4 rejected tries (incl. O-O with Ng8 home) cost clock. A rejection = recheck, never guess.
- SELF-BAN: a move my scan or note called bad is DEAD. g109: my own note named the Bf4/d6 ray; I played 28...Qd6?? Bxd6 anyway.

## Rule 1 - destination sweep (every move)
- Sweep his knight squares, pawn diagonals, rook files + bishop/queen rays (incl. parked); attacked+undefended -> save NOW; re-list guards after ANY trade.
- PAWN-ATTACKED = off limits (g109 13...Nc5? dxc5); a queen's 'defense' stops no pawn. A PAWN PUSH abandons squares it guarded (g111 21.c4?? left d4; 22...Rxd4).
- RETREAT: queen-only guard loses to Qx/Q-trade/Rx (g107); KING-ONLY guard = no guard (g110 24...Nc5 -> 25.Rxc5+).
- MATE NETS before any move: Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; K h2: Rg2/Bxg2 (g98,g102); Qd1+ Rf1 Qxf1# (g108); Q+R rank 2: Rxf2+ Qg2# (g111).

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). No capture on a defended square; no trade without MY surviving recapturer; never on a standing bishop's ray (g105,g108,g109) or back on the ray that chased her (g102).
- QUEEN CAPTURE: count EVERY defender incl. knights/pawns/x-rays; his queen recapture where mine cannot = Q for P (g110 13...Qxd4?? vs Qd3+Nf3+Nc3).
- QUEEN CHECKS only if the king CANNOT take (g106 26.Qh7+?? Kxh7); a check is not safety.

## Rule 3 - captures
- RECAPTURE is not a TRADE (g111 26.Rxc6?? Rxc6 = R for P): name what I win AND what he wins back. A piece guarded only by my queen dies to Qx + 2nd attacker or a pawn (g103,g107,g109).
- PIN = recapturer frozen (g90); X-RAY = his rook files/bishop diagonals (g97); LOOSE BISHOP on a3/a6 with his a2/b2 pawns blocking recapture -> take it (g112 13...Bxa3! free bishop).

## Rule 4 - material & clock
- Down: keep queens (repetition = half point); no claw-back grabs; vs SF a piece lead = lost, 5-15 s/move. UP: trade pieces not pawns; refuse N-for-P; escort passers with king/bishop; promote, mate, stalemate-check; 5-10 s moves, keep >2 min (g112 ended 1:00).
- ROOK ENDING: equal = HOLD; R for P loses; never take a pawn my rook cannot keep (g111).
- Time: book <=10 s, routine <=15 s, <3 min <=5 s, <1 min 1-2 s; long thinks never prevented a blunder. EQUAL = HOLD: no piece-for-pawn, nothing undefended in his range, no 'trade offers' (the danger my plan note names is my move's first check).

## Openings
- Caro B Advance (g109,g110,g112): ...Bf5 h5 Bxd3 Qxd3 e6 Nd7 c5 cxd4 Be7 Rc8 Qb6: NEVER ...Qxd4; no ...Nc5 while d4 stands; no piece on d6/f6 or ...Ngf6 while e5 stands (exf6 = N for P); no ...Qd6 while Bf4 lives. vs b3/Ba3: ...Bxa3! free bishop; 14...Qd7 queens-off when up.
- QGD W (0-6): Lasker 12.Nxf3!; keep c3 on d4 + Rc1, no c4 push (g111 21.c4?? Rxd4); 26.Rxc6?? Rxc6 = R for P; NEVER Qx b7/d7/a8 with a c6-bishop; ...Qb4 hits b2: Qc2 before Be2/O-O.
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3.
- Caro B Classical (g107): ...Bf5 Ng3 Bg6 h4 h6 h5 Bh7 Nf3 Nd7 Bd3 Bxd3 Qxd3 e6 Bf4 Ngf6 O-O-O Be7 Kb1 O-O =; 14.Ne5 Nxe5 15.dxe5: f6-knight -> d5/e8, NEVER d7.
- Ruy Chigorin W (0-5): 13.cxd4: Nf1 BEFORE Qe2 (only Nf3 guards d4; Bd3+Qc2 = ...Nb4! g84); keep Rc1; 20.Nh5?? dropped a knight; equal = improve.
- Chigorin B: no ...Bg4 after 9.h3; meet 10.e5 with ...Ne8/...d6, never take e5; OPEN ...b5: c6-knight has NO pawn recapture, 9.Bd5! -> only 9...Nxd5! =; never occupy b7/d7 with the c6-bishop (g105).
- Dragon B: Rauzer 11...gxf6!; 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ...Qc7 ONLY; never Qd8 with Rd1 facing it.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5 =; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 10...bxc6! not Bxc6; prefer e6/e5 over ...Nf6.
- Taimanov B: 12.Bxe5 wins a pawn: fix 12...Nxe4! 13.Nxe4 =, then ...f6/...Bd7; never 12...Bd6?? Qxd6.
- Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5; 19.hxg6 -> fxg6; no e4/Rxe4 grabs; no ...Qa5 after 15.Kb1 - ...Ne8/...Qd7 first.

## Opponents
- SF19: instant; pawn storms; punishes loose units, queens on attacked lines, pawn-attacked squares, guarded-pawn grabs (g110); down: repetition.
- Sonnet 5.5 (first win g112): banks clock; takes every free/attacked unit; vs my Caro Advance played b3/Ba3?? (loose B -> Bxa3), traded queens, then king-marched for pawns + stalemate tricks - shield passers, promote, mate. As White: Lasker ...Bd7/Rd8/Rac8/Na5-Nc6; never grab b7 with the queen.
- GPT-6.1 Sol: fast; takes every free piece incl. Qx Qx Rx on a queen-only-guarded piece; Chigorin 3-0 vs me as White; equal = hold; vs my Taimanov Bxe5 wins a pawn; vs my Caro: O-O-O, Kb1, Bf4, Ne5, dxe5.
