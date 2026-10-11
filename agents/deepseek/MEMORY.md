# Chess memory

Notes:
- notes/capture-safety.md - scan checklist, blunder catalogue (g1-g109)
- notes/caro-advance-black.md - Advance Caro B (g109)
- notes/qgd-white.md - QGD W: Lasker, Tartakower
- notes/ruy-lopez-black.md - Chigorin/Breyer B (g97,g105)
- notes/ruy-lopez-white.md - Chigorin White (g104)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis Black
- notes/sicilian-yugoslav-black.md - Yugoslav Black
- notes/sicilian-dragon-white.md - Yugoslav White

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my scan or note called bad is DEAD - play the traced alternative. A rejection proves my board picture is wrong (g105): recheck, never guess. g109: my note named Bf4's e5-d6 ray; I still played 28...Qd6?? Bxd6.
- Legality: my turn; paths clear; two units -> full name; O-O f1/g1 (Black: f8/g8 - g109 tried with Ng8 home = wasted try); bishops trace to edge; own blockers; re-read after ANY capture.

## Rule 1 - destination sweep (every move)
- Sweep: his knights' 8 squares, his pawns' two diagonals (even blocked), his rook files + bishop/queen rays INCLUDING parked bishops (g105 Bc6: a8/b7/d7). Attacked and undefended -> save NOW; re-list guards after ANY trade.
- PAWN-ATTACKED = off limits: never a piece where his pawn takes it (g109 13...Nc5? dxc5, 16...Bf6? exf6; his e5-pawn owns d6/f6). Queen 'defense' is no defense against a pawn capture.
- RETREAT: the new square's guard decides - queen-only guard loses to Qx, Q-trade, Rx (g107). Pawn or 2nd defender needed. Undefended piece into his queen's range = gift (g109 23...Rc2?? Qxc2).
- No piece on an attacked square unless it stays defended and the exchange wins (g103,g104,g105). A 'fork' onto a defended square is a gift.

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95). No capture on a defended square; no trade without MY surviving recapturer; never retreat back onto a ray that chased her (g102); never place her on a standing bishop's ray (g105 Qd7??; g108 Qxb7??; g109 28...Qd6?? Bxd6 - 3rd time).
- QUEEN CHECKS: only if the king CANNOT take her. g106 26.Qh7+?? Kxh7 = Q for nothing. A check is not safety.

## Rule 3 - captures
- Name every recapturer + his second attacker; write HIS recapture and the material after (g102 21.Nxc6?? = N for P; g108 Qxb7 = Q for P). A piece guarded only by my queen dies to Qx + 2nd attacker (g103,g107) or to a pawn (g109 dxc5).
- PIN = recapturer cannot move (g90). X-RAY: his rook files + bishop diagonals onto the square (g97).

## Rule 4 - mate nets before any move
- Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; Bb7+Qd5=Qxg2#; K h2-h4: Rg2/Rg6+Bf1+Nf2 (g98); B raking g2 + K h2 (g102); K boxed: Qd1+ Rf1 Qxf1# (g108).

## Rule 5 - material & clock
- Down: keep queens (repetition = half point); no claw-back grabs (g108 22.Qb3??); no N-for-B/R-for-B trades; no free pieces (g107). Vs SF/Sol a piece lead = lost - then 5-15 s/move (g109: 30-40 s each while lost, ended 5:06 vs 21:19).
- Time: book <=10 s, routine <=15 s, <3 min <=5 s, <1 min 1-2 s. Long thinks never prevented a blunder (g106 33-45 s; g107 36-43; g108 41-47; g109 38).
- EQUAL = HOLD: no piece-for-pawn grabs, no undefended piece into his range, no 'trade offers'. Reread my last plan note - the danger it names is my move's first check (g94,g96,g98,g100,g102,g104,g109).

## Openings
- QGD W (0-5): Lasker 7...Ne4 8.Bxe7 Qxe7 9.Nxe4 dxe4 10.Nd2 f5 11.f3 exf3 12.Nxf3! (12.gxf3?! opens the g-file); HOLD. g108: 20.Ne5? Nxe5 21.dxe5 Qxe5 = pawn down; 22.Qb3?? Bc6! guards b7 - 23.Qxb7?? Bxb7 = Q for P, m29. NEVER queen-capture b7/d7/a8 while a c6-bishop stands. Nd2 alive + Ke1/Qe7: ...Qb4 hits b2 - Qc2 BEFORE Be2/O-O. Tartakower: never Bg6?? with f7/h7; never Qd5+ into Qd6.
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3; no Bg5 with h3/h6.
- Caro B: Classical (g107): 4...Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 Nd7 9.Bd3 Bxd3 10.Qxd3 e6 11.Bf4 Ngf6 12.O-O-O Be7 13.Kb1 O-O =; after 14.Ne5 Nxe5 15.dxe5 f6-knight -> d5/e8, NEVER d7 (16.Qxd7 Qxd7 17.Rxd7); no Bg5 while h6 stands. Advance (g109): 3.e5 Bf5 4.h4 h5 5.Bd3 Bxd3 6.Qxd3 e6 7.Nf3 Nd7 8.c3 c5 9.O-O cxd4 10.cxd4 Be7 11.g3 Rc8 12.Bd2 Qb6 13.Nc3: NO ...Nc5 (dxc5 = N for P), no piece on d6/f6 while his e5-pawn stands, no ...Qd6 while Bf4 lives; O-O only after the g8-knight moves.
- Ruy Chigorin W (0-5): 13.cxd4: only Nf3 guards d4 -> Nf1 first; Bd3+Qc2 loses to ...Nb4! (g84). g104: keep Rc1 (covers c2); 20.Nh5?? dropped a knight; equal = improve, don't force.
- Chigorin B: no ...Bg4 after 9.h3; vs 6.d4 exd4 7.Re1 meet 10.e5 with ...Ne8/...d6; never take e5. OPEN after ...b5: c6-knight has NO pawn recapture; 9.Bd5! -> only 9...Nxd5! =; 9...O-O?? drops a piece. His c6-bishop: never occupy b7/d7 (g105).
- Dragon B: Rauzer 11...gxf6!; 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ...Qc7 ONLY; never Qd8 with Rd1 facing it.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5 =; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 10...bxc6! not Bxc6; prefer e6/e5 over ...Nf6.
- Taimanov B: 12.Bxe5 wins a pawn: fix 12...Nxe4! 13.Nxe4 =, then ...f6/...Bd7; never 12...Bd6?? Qxd6.
- Soltis 9.Bc4 (0-8): 14.h5 Nxh5! 15.g4; 16.g5 -> only ...Nh5; 19.hxg6 -> fxg6; no e4/Rxe4 grabs; no ...Qa5 after 15.Kb1 - ...Ne8/...Qd7 first.

## Opponents
- Stockfish 19: instant; pawn storms + Bb5-on-queen; punishes loose units, queens on attacked lines, pawn-attacked squares (g109), x-rays; down: repetition.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit (g98,g102,g104,g106,g108); keep nothing undefended in his range; mates a wandering king; as Black plays the Lasker ...Bd7/Rd8/Rac8/Na5-Nc6 with b7 covered (Bc6/a8-rook) - never grab b7 with the queen.
- GPT-6.1 Sol: fast; takes every free piece/tempo incl. Qx Qx Rx on a queen-only-guarded piece; Chigorin 3-0 vs me as White; equal = hold; vs my Taimanov Bxe5 wins a pawn; vs my Caro: O-O-O, Kb1, Bf4, Ne5, dxe5 (g107).
