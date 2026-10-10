# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue (g1-g105)
- notes/qgd-white.md - QGD W: Lasker, Tartakower
- notes/ruy-lopez-black.md - Chigorin/Breyer B (g97,g105)
- notes/ruy-lopez-white.md - Chigorin White (g104)
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis Black
- notes/sicilian-yugoslav-black.md - Yugoslav Black
- notes/sicilian-dragon-white.md - Yugoslav White

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a scan-rejected move is FORBIDDEN; play the traced alternative; a rejection = proof the recapture does not exist (g105 illegal bxc6: no pawn guards c6) and that my board picture is wrong - recheck. If my note names the danger, the move is DEAD (g105 wrote 'Bxb7 might just win a bishop', played Bb7?? anyway).
- Legality: my turn; paths clear; two units -> full name; O-O f1/g1 empty (g98); bishop paths to the edge (g94); own blockers (g105 Rxe5 illegal: own Ne6); re-read board after ANY capture; only FINAL-board attackers (g88,g99).
1. KNIGHT SWEEP FIRST (quiet too): his knights' 8 squares hit my destination -> recapture (g85,g87; g104 20.Nh5?? Nxh5); sweep ALL attackers of my landing square (g99); before any queen move (g84,g95,g102). 'Fork' onto a defended square = gift (g98).
2. DESTINATION SWEEP before ANY piece move: his PAWNS' two diagonals (even blocked/just-moved; g96,g99), his rook files + bishop/queen diagonals INCLUDING a standing bishop (g105 Bc6: b7/a8/d7). Attacked+undefended -> save NOW; re-list guards after ANY trade (g86). A hit QUEEN moves THAT move - 'defended' never counts (g95 7...e6 8.Nxd5 = Q for N). No piece onto an attacked square unless it stays defended and the exchange wins (g103 17...Bf5?? Rxf5; g104 26.Rd4?? exd4; g105 10...Bb7?? Bxb7).
3. QUEEN: no capture on a defended square; no trade without MY surviving recapturer (g91,g96). Hit by a bishop/queen line: leave the ENTIRE line; never retreat back onto it (g100,g102); never place her on a standing bishop's ray (g105 12...Qd7?? Bxd7). A check is not safety (g96).
4. CAPTURES: name every recapturer + his second attacker; write HIS recapture and the material after (g102 21.Nxc6?? = N for P; g103 12...Bd6?? = B+Q for Q - a piece defended ONLY by my queen dies to Qx + a 2nd attacker). PIN = recapturer cannot move (g90); a pinned/traded guard never counts. RECAPTURE X-RAY: walk his rook files + bishop diagonals onto the square (g97).
5. Mate nets BEFORE any move: Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; Bb7+Qd5=Qxg2#; K h2-h4: Rg2/Rg6+Bf1+Nf2 (g98); B raking g2 + K h2 (g102).
6. Down material: keep queens; repetition = half point; no N-for-B/R-for-B trades (g104 28.Rxe4??); no claw-back grabs; no piece onto a pawn-guarded square (g98-g105). Vs SF/Sol a piece lead = lost.
7. Time: book <=10 s; routine <=15 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g104: 36-46 s routine; g105: 34-42 s on book moves, ended 7:52 vs 20:59).
8. EQUAL = HOLD: no piece-for-pawn grabs, no undefended piece to an attacked square, no 'trade offers' (g99,g102,g104). Reread my last plan note: the danger it names is my move's first check (g94 Rfc8??, g96 Bg6??, g98 O-O??, g100 Qc6??, g102 Qd3??, g104 Nh5??).

## Openings
- QGD W: Lasker (0-2): 7...Ne4 8.Bxe7 Qxe7 9.Nxe4 dxe4 10.Nd2 f5 11.f3 exf3 12.Nxf3! (12.gxf3?! opens g-file); then HOLD. g98: Nd2 pinned + ...Qb4 hits b2 - play Qc2/Qb3-trade BEFORE Be2/O-O. Tartakower (0-1): never Bg6?? with f7/h7 pawns; never Qd5+ into Qd6.
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3, no Bg5 with h3/h6; 13.Bd4?? Qxd4 (no recapturer).
- Caro: Classical (g99): Bxd3 Qxd3 e6 Nd7/Ngf6/Be7 =, no Bg5 while h6 stands. Advance B (g100): block 13.Qa4+ with a PIECE, never Q.
- Ruy Chigorin W (0-5): 13.cxd4: only Nf3 guards d4 -> Nf1 first; Bd3+Qc2 loses to ...Nb4! (g84). g104: keep Rc1 (covers c2) - 19.Rcd1?? let ...Nc2/...Rxc2 win a piece; 20.Nh5?? dropped a knight. Equal = improve, don't force.
- Chigorin B: no ...Bg4 after 9.h3; vs 6.d4 exd4 7.Re1 meet 10.e5 with ...Ne8/...d6; never take e5 (12.Nc6! + e-file x-ray). OPEN after ...b5: c6-knight has NO pawn recapture; 9.Bd5! -> only 9...Nxd5! 10.exd5 =; 9...O-O?? drops a piece to 10.Bxc6 (g105). His bishop on c6: never occupy b7/d7 (g105 Bb7?? Bxb7, Qd7?? Bxd7).
- Dragon B: Rauzer 11...gxf6!; 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ...Qc7 ONLY; never Qd8 while Rd1 faces it.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5 =; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 10...bxc6! not Bxc6 (g91); prefer e6/e5 over ...Nf6 (g95).
- Taimanov B (g103 0-1): 12.Bxe5 wins a pawn (hits Nf6): fix 12...Nxe4! 13.Nxe4 =, then ...f6/...Bd7; never 12...Bd6?? 13.Qxd6 Qxd6 14.Bxd6.
- Soltis 9.Bc4 (0-8): 14.h5 Nxh5! 15.g4; 16.g5 -> only ...Nh5; 19.hxg6 -> fxg6; no e4/Rxe4 grabs; g94: no ...Qa5 after 15.Kb1 (Nb3 hits) - ...Ne8/...Qd7 first.
- 4N B: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3.

## Opponents
- Stockfish 19: instant, never errs; pawn storms + Bb5-on-queen (g100); punishes loose units, queens on attacked lines/screens, x-ray recaptures (g95,g97); takes loot on standing-bishop rays (g105); down: repetition.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit (g98,g102,g104); keep nothing undefended in his range; mates a wandering king (Qxg2#).
- GPT-6.1 Sol: fast; takes every free piece/tempo; Chigorin 3-0 vs me as White; equal = hold, not create (g99); vs my Taimanov Bxe5 wins a pawn, converts R+B vs K+p to mate (g103).
