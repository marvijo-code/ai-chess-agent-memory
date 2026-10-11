# Chess memory

Notes:
- notes/capture-safety.md - scan checklist, blunder catalogue (g1-g107)
- notes/qgd-white.md - QGD W: Lasker, Tartakower
- notes/ruy-lopez-black.md - Chigorin/Breyer B (g97,g105)
- notes/ruy-lopez-white.md - Chigorin White (g104)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis Black
- notes/sicilian-yugoslav-black.md - Yugoslav Black
- notes/sicilian-dragon-white.md - Yugoslav White

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my scan or note called bad is DEAD - play the traced alternative. A rejection proves my board picture is wrong (g105 bxc6/Rxe5 illegal): recheck, never guess.
- Legality: my turn; paths clear; two units -> full name; O-O f1/g1 empty; bishops trace to the edge; own blockers; re-read after ANY capture; only FINAL-board attackers count.

## Rule 1 - sweep of my destination (every move)
- His knights' 8 squares (quiet moves too), his PAWNS' two diagonals (even blocked), his rook files and bishop/queen rays INCLUDING a standing bishop (g105 Bc6: b7/a8/d7). Attacked and undefended -> save NOW; re-list guards after ANY trade (g86).
- RETREAT: the new square's guard decides - queen-only guard loses to Qx, Q-trade, Rx (g107 15...Nd7?? 16.Qxd7 Qxd7 17.Rxd7). Pawn or 2nd defender needed.
- No piece on an attacked square unless it stays defended and the exchange wins (g103 17...Bf5?? Rxf5; g104 26.Rd4?? exd4; g105 10...Bb7?? Bxb7). A 'fork' onto a defended square is a gift.

## Rule 2 - the queen
- Hit by anything: she moves THAT move; 'defended' never counts (g95 7...e6?? 8.Nxd5 = Q for N).
- No capture on a defended square; no trade without MY surviving recapturer; never retreat back onto a ray that chased her (g102); never place her on a standing bishop's ray (g105 Qd7?? Bxd7).
- QUEEN CHECKS: only if the king CANNOT take her (square guarded by one of my pieces or blocked). g106 26.Qh7+?? Kxh7 = Q for nothing. A check is not safety.

## Rule 3 - captures
- Name every recapturer + his second attacker; write HIS recapture and the material after (g102 21.Nxc6?? = N for P). A piece guarded only by my queen dies to Qx + a 2nd attacker (g103 12...Bd6??; g107 Nd7: Qx, Qx, Rx).
- PIN = recapturer cannot move; a pinned/traded guard never counts (g90). RECAPTURE X-RAY: walk his rook files + bishop diagonals onto the square (g97).

## Rule 4 - mate nets before any move
- Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; Bb7+Qd5=Qxg2#; K h2-h4: Rg2/Rg6+Bf1+Nf2 (g98); B raking g2 + K h2 (g102).

## Rule 5 - material & clock
- Down: keep queens (repetition = half point); no N-for-B/R-for-B trades; no claw-back grabs; no piece onto a pawn-guarded square; no free pieces (g107 19...Rd1+?? Rxd1). Vs SF/Sol a piece lead = lost.
- Time: book <=10 s, routine <=15 s, <3 min <=5 s, <1 min 1-2 s. Long thinks never prevented a blunder (g106 33-45 s on known Lasker; g107 36-43 s on known Caro; ended 6:55/9:29 vs 14:20/15:39).
- EQUAL = HOLD: no piece-for-pawn grabs, no undefended piece into his range, no 'trade offers'. Reread my last plan note - the danger it names is my move's first check (g94,g96,g98,g100,g102,g104).

## Openings
- QGD W (0-4): Lasker 7...Ne4 8.Bxe7 Qxe7 9.Nxe4 dxe4 10.Nd2 f5 11.f3 exf3 12.Nxf3! (12.gxf3?! opens the g-file); then HOLD - g106 equal until 26.Qh7+??. Nd2 alive + Ke1/Qe7: ...Qb4 hits b2 - Qc2 or offer Qb3 BEFORE Be2/O-O. Tartakower: never Bg6?? with f7/h7; never Qd5+ into Qd6.
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3, no Bg5 with h3/h6; 13.Bd4?? Qxd4.
- Caro B (g107): 4...Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 Nd7 9.Bd3 Bxd3 10.Qxd3 e6 11.Bf4 Ngf6 12.O-O-O Be7 13.Kb1 O-O =; after 14.Ne5 Nxe5 15.dxe5 the kicked f6-knight goes d5 (c6-pawn guard) or e8 - NEVER d7 (16.Qxd7 Qxd7 17.Rxd7). No Bg5 while h6 stands. Advance: block 13.Qa4+ with a PIECE, never Q.
- Ruy Chigorin W (0-5): 13.cxd4: only Nf3 guards d4 -> Nf1 first; Bd3+Qc2 loses to ...Nb4! (g84). g104: keep Rc1 (covers c2); 20.Nh5?? dropped a knight. Equal = improve, don't force.
- Chigorin B: no ...Bg4 after 9.h3; vs 6.d4 exd4 7.Re1 meet 10.e5 with ...Ne8/...d6; never take e5. OPEN after ...b5: c6-knight has NO pawn recapture; 9.Bd5! -> only 9...Nxd5! =; 9...O-O?? drops a piece. His c6-bishop: never occupy b7/d7 (g105).
- Dragon B: Rauzer 11...gxf6!; 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ...Qc7 ONLY; never Qd8 with Rd1 facing it.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5 =; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 10...bxc6! not Bxc6; prefer e6/e5 over ...Nf6.
- Taimanov B: 12.Bxe5 wins a pawn: fix 12...Nxe4! 13.Nxe4 =, then ...f6/...Bd7; never 12...Bd6?? Qxd6.
- Soltis 9.Bc4 (0-8): 14.h5 Nxh5! 15.g4; 16.g5 -> only ...Nh5; 19.hxg6 -> fxg6; no e4/Rxe4 grabs; no ...Qa5 after 15.Kb1 (Nb3 hits) - ...Ne8/...Qd7 first.
- 4N B: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3.

## Opponents
- Stockfish 19: instant; pawn storms + Bb5-on-queen; punishes loose units, queens on attacked lines/screens, x-ray recaptures; takes loot on standing-bishop rays; down: repetition.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit (g98,g102,g104; g106 Kxh7); keep nothing undefended in his range; mates a wandering king.
- GPT-6.1 Sol: fast; takes every free piece/tempo incl. Qx Qx Rx on a queen-only-guarded piece; Chigorin 3-0 vs me as White; equal = hold, not create; vs my Taimanov Bxe5 wins a pawn, converts R+B vs K+p; vs my Caro he plays O-O-O, Kb1, Bf4, Ne5, dxe5 (g107).
