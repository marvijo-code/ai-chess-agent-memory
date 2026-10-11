# Chess memory

Notes:
- notes/capture-safety.md - scan checklist, blunder catalogue (g1-g111)
- notes/caro-advance-black.md - Advance Caro B (g109,g110)
- notes/qgd-white.md - QGD W: Lasker, Tartakower (g111)
- notes/ruy-lopez-black.md - Chigorin/Breyer B (g97,g105)
- notes/ruy-lopez-white.md - Chigorin White (g104)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis Black
- notes/sicilian-yugoslav-black.md - Yugoslav Black
- notes/sicilian-dragon-white.md - Yugoslav White

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my scan or note called bad is DEAD - play the traced alternative. A rejection = wrong board picture: recheck, never guess. g109: my note named the Bf4/d6 ray; I played 28...Qd6?? Bxd6 anyway.
- Legality: paths clear; two units -> full name; O-O f1/g1 (Black f8/g8); bishops trace to edge; own blockers; re-read after ANY capture.

## Rule 1 - destination sweep (every move)
- Sweep: his knights' 8 squares, his pawns' two diagonals, his rook files + bishop/queen rays incl. parked ones. Attacked+undefended -> save NOW; re-list guards after ANY trade.
- PAWN-ATTACKED = off limits: never a piece where his pawn takes it (g109 13...Nc5? dxc5); a queen's 'defense' stops no pawn.
- PUSHING A PAWN abandons squares it guarded: c3 guarded d4; 21.c4?? (g111) left d4 to Rd8 = 22...Rxd4. List them before any push.
- RETREAT: the new square's guard decides - queen-only guard loses to Qx, Q-trade, Rx (g107). Pawn or 2nd defender needed.
- KING-ONLY guard = no guard: blocking a rook check (g110 24...Nc5 -> 25.Rxc5+) or any piece he takes with tempo. Undefended into his queen's range = gift (g109 23...Rc2?? Qxc2).

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). No capture on a defended square; no trade without MY surviving recapturer; never back onto the ray that chased her (g102); never on a standing bishop's ray (g105,g108,g109).
- QUEEN CAPTURE of a pawn/piece: count EVERY defender (queen, knights, pawns, x-rays). His queen recapture where mine cannot = Q for P (g110 13...Qxd4?? - d4 had Qd3+Nf3+Nc3, I listed two).
- QUEEN CHECKS: only if the king CANNOT take her (g106 26.Qh7+?? Kxh7). A check is not safety.

## Rule 3 - captures
- RECAPTURE is not a TRADE: his recapture takes MY unit. My rook taking a pawn his rook defends = R for P (g111 26.Rxc6?? Rxc6; my own note had said 'his rook defends c6'). Name what I win AND what he wins back.
- Name every recapturer + 2nd attacker; write HIS recapture and the material (N/Q for P). A piece guarded only by my queen dies to Qx + 2nd attacker (g103,g107) or a pawn (g109).
- PIN = recapturer cannot move (g90). X-RAY: his rook files + bishop diagonals onto the square (g97).

## Rule 4 - mate nets before any move
- Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; K h2: Rg2/Rg6+Bf1+Nf2 (g98); B raking g2 + K h2 (g102); Qd1+ Rf1 Qxf1# (g108); Q+R rank 2: Rxf2+ (Q guards it), then Qg2/Qh2# vs a cornered king (g111).

## Rule 5 - material & clock
- Down: keep queens (repetition = half point); no claw-back grabs, no bad trades, no free pieces; vs SF a piece lead = lost, then 5-15 s/move.
- ROOK ENDING: equal = HOLD, rooks active; never take a pawn my rook cannot keep (g111). Pawn-down rook endings draw; R for P loses.
- Time: book <=10 s, routine <=15 s, <3 min <=5 s, <1 min 1-2 s. Long thinks never prevented a blunder: g110/g111 spent 40-46 s on book/routine moves and still blundered; g111 ended 8:45 vs 14:24.
- EQUAL = HOLD: no piece-for-pawn grabs, nothing undefended in his range, no 'trade offers'. The danger my last plan note names is my move's first check (g94,g96,g98,g100,g102,g104,g109,g111).

## Openings
- QGD W (0-6): Lasker 12.Nxf3!. g111: ...Bxf3 14.Qxf3 Rad8/Rfe8 Qd6 e4 dxe4 Bxe4 Qf6 Qxf6 gxf6 Bxc6 bxc6 =: keep c3 (guards d4) + Rc1, no c4 push; 26.Rxc6?? Rxc6 = R for P. NEVER Qx b7/d7/a8 with a c6-bishop. ...Qb4 hits b2: Qc2 before Be2/O-O.
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3; no Bg5 with h3/h6.
- Caro B Classical (g107): 4...Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 Nd7 9.Bd3 Bxd3 10.Qxd3 e6 11.Bf4 Ngf6 12.O-O-O Be7 13.Kb1 O-O =; 14.Ne5 Nxe5 15.dxe5: f6-knight -> d5/e8, NEVER d7.
- Caro B Advance (g109,g110): ...Bf5 h5 Bxd3 Qxd3 e6 Nd7 c5 cxd4 Be7 Rc8 Qb6 Nc3: NEVER ...Qxd4 (Qd3+Nf3+Nc3 = Q for P); no ...Nc5 while d4 stands (dxc5); no piece on d6/f6 while e5 stands; no ...Qd6 while Bf4 lives.
- Ruy Chigorin W (0-5): 13.cxd4: Nf1 BEFORE Qe2 (only Nf3 guards d4; Bd3+Qc2 = ...Nb4! g84). Keep Rc1 (covers c2); 20.Nh5?? dropped a knight; equal = improve, don't force.
- Chigorin B: no ...Bg4 after 9.h3; 6.d4 exd4 7.Re1: meet 10.e5 with ...Ne8/...d6, never take e5. OPEN ...b5: c6-knight has NO pawn recapture; 9.Bd5! -> only 9...Nxd5! =; 9...O-O?? drops a piece; never occupy b7/d7 with the c6-bishop (g105).
- Dragon B: Rauzer 11...gxf6!; 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ...Qc7 ONLY; never Qd8 with Rd1 facing it.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5 =; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 10...bxc6! not Bxc6; prefer e6/e5 over ...Nf6.
- Taimanov B: 12.Bxe5 wins a pawn: fix 12...Nxe4! 13.Nxe4 =, then ...f6/...Bd7; never 12...Bd6?? Qxd6.
- Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5; 19.hxg6 -> fxg6; no e4/Rxe4 grabs; no ...Qa5 after 15.Kb1 - ...Ne8/...Qd7 first.

## Opponents
- Stockfish 19: instant; pawn storms; punishes loose units, queens on attacked lines, pawn-attacked squares, guarded-pawn grabs (g110); x-rays; down: repetition.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit incl. my rook (g111); keep nothing undefended; rook endings: grabs pawns my push left unguarded; mates a wandering king; as Black Lasker ...Bd7/Rd8/Rac8/Na5-Nc6 with b7 covered - never grab b7 with the queen.
- GPT-6.1 Sol: fast; takes every free piece/tempo incl. Qx Qx Rx on a queen-only-guarded piece; Chigorin 3-0 vs me as White; equal = hold; vs my Taimanov Bxe5 wins a pawn; vs my Caro: O-O-O, Kb1, Bf4, Ne5, dxe5.
