# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue (g1-g102)
- notes/qgd-white.md - QGD W: Lasker g98/g102, Tartakower g96
- notes/ruy-lopez-black.md - Chigorin/Breyer Black
- notes/ruy-lopez-white.md - Ruy White
- notes/sicilian-black.md - Alapin/Dragon Black
- notes/sicilian-soltis-black.md - Soltis Black
- notes/sicilian-yugoslav-black.md - 9.O-O-O d5 Black
- notes/sicilian-dragon-white.md - Yugoslav White

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my scan called bad/illegal is FORBIDDEN; play the traced alternative; one rejected attempt -> a different move.
- Legality: my turn; paths clear; two units -> full name; O-O f1/g1 empty (g98); bishops to the edge (g94); re-read board after ANY capture; only FINAL-board attackers count (g88,g99).
1. KNIGHT SWEEP FIRST: his knights' 8 squares hit my destination/capture -> he recaptures (g85,g87); sweep ALL attackers of my landing square (g99); before any queen placement (g84,g95,g102). 'Fork' onto a defended square = gift (g98).
2. HIS last move: list attackers of my destination (rook, bishop, knight, PAWN). Hit queen moves THAT move - 'defended' never counts (g95 7...e6 8.Nxd5 = Q for N). Attacked+undefended -> save NOW; re-list guards after ANY trade (g86).
3. PAWN SWEEP before ANY piece move: no minor/rook onto a pawn-guarded square, even defended; just-moved or BLOCKED pawns still hit both diagonals (g96 18.Bg6?? fxg6). g99: 21...Bf6?? exf6, 24...Rxb3+?? axb3, 25...Nd5?? cxd5.
4. QUEEN: no capture on a defended square; no trade without MY recapturer that SURVIVES (g91,g96). Hit by a bishop/queen line: leave the ENTIRE line; never retreat along/onto it, never RETURN to a square it chased her from (g100 Qc6??; g102 26.Qd3?? back onto e4-d3-c2-b1 = Q for B). Before ANY queen move trace all enemy B/Q lines through the destination; a check is not safety (g96).
5. CAPTURES: name every recapturer + second attacker; write HIS recapture AND the material after (g102 21.Nxc6?? Bxc6 = N for ONE pawn - b7 was guarded by the recapturer); his last -> don't start; level/down NO sacs. PIN = my recapturer cannot move (g90). RECAPTURE X-RAY: walk his rook files + bishop diagonals onto the square (g97 13...Qxe7?? 14.Rxe7 = Q for N).
6. Mate nets BEFORE any move: Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; Bb7+Qd5=Qxg2#; K h2-h4: Rg2/Rg6+Bf1+Nf2 (g98); bishop raking g2 + K h2 (g102 33...Qxg2#).
7. Down material: keep queens; repetition = half point; no N-for-B/R-for-B trades; no claw-back grabs; no piece onto a pawn-guarded square. Hold, trade pawns, make him prove it (g98-g102). K+P race: king IN FRONT (g92). Vs SF/Sol a piece lead = lost.
8. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g89-g102; g102 42-48 s/move with Qc2?!, Bd3?!, Nxc6??, Qd3??; ended 7:56 vs 15:42).
9. EQUAL = HOLD, don't create: no piece-for-pawn grabs, no line-opening grabs; trade pawns, improve (g99,g102). Reread my last plan note each move: a danger it names is the candidate's first check (g94 Rfc8??, g96 Bg6??, g98 O-O??, g100 Qc6??, g102 Qd3??).

## Openings
- QGD Lasker W (0-2 Sonnet): 7...Ne4 8.Bxe7 Qxe7 9.Nxe4 dxe4 10.Nd2 f5 11.f3 exf3 12.Nxf3! (12.gxf3?! opens g-file) Nc6 13.Qc2?! Bd7 14.Bd3?! Rad8 15...Nb4 (Qc3 Nxd3 Qxd3 =) 19...Be4! hits Qd3; = to ...c6: HOLD. g98: Nd2 pinned + ...Qb4 hits b2 - Qc2/Qb3-trade BEFORE Be2/O-O.
- QGD Tartakower W (0-1 Sol): NEVER Bg6?? (f7/h7 pawns); never Qd5+ into Qd6.
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5; Nf1-g3, no Bg5 with h3/h6; 13.Bd4?? Qxd4 (no recapturer).
- Caro-Kann Classical W (g99 Sol 0-1): Bxd3 Qxd3 e6 Nd7/Ngf6/Be7 =; hold; no Bg5 while h6 stands.
- Caro Advance/Tal B (g100 SF): 13.Qa4+ when a4-e8 (b5/c6/d7/e8) is open: block with a PIECE; never Q there (13...Qd7?! 14.Bb5 Qc6?? 15.Bxc6+ = Q for B).
- Ruy Chigorin W (0-4): 13.cxd4: only Nf3 guards d4 (Qe2 doesn't) -> Nf1 first; Bd3+Qc2 loses to ...Nb4! (g84).
- Chigorin B: no ...Bg4 after 9.h3; vs 6.d4 exd4 7.Re1 (g97) meet 10.e5 with ...Ne8 then ...d6; never take e5 (12.Nc6! + e-file x-ray on Qd8).
- Dragon B: Rauzer 11...gxf6!; 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ...Qc7 ONLY; never Qd8 while Rd1 faces it.
- Alapin B: 5.Qxd4 ...Nc6/g6/Bg7/O-O/Nc5 =; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 10...bxc6! not Bxc6 (g91); prefer 6...e6/e5 over ...Nf6 (g95).
- Soltis 9.Bc4 (0-8): 14.h5 Nxh5! 15.g4; 16.g5 -> only ...Nh5; 19.hxg6 -> ...fxg6; no e4/Rxe4 grabs; g94: no ...Qa5 after 15.Kb1 (Nb3 hits) - ...Ne8/...Qd7 first.
- 4N B: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon W: keep Bc5 defended (g42).

## Opponents
- Stockfish 19: instant, never errs; pawn storms + Bb5-on-queen (g100); punishes loose units, queens on attacked lines/screens, recaptures on open files (g95,g97); down: repetition.
- Sonnet 5.5: banks clock (g102 15:42 left vs my 7:56); takes EVERY free/attacked unit (g98 Qxb2/Qxa2; g102 Bxd3/Bxc4/Rxc8); defend pawns and queen lines; mates (Qxg2#) on a wandering king.
- GPT-6.1 Sol: fast; takes every free piece and tempo (g94); Chigorin 3-0 vs me as White; equal means hold, not create (g99).
