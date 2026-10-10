# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue (g1-g99)
- notes/qgd-white.md - QGD W: Lasker g98, Tartakower g96
- notes/ruy-lopez-black.md - Chigorin/Breyer Black
- notes/ruy-lopez-white.md - Ruy White
- notes/sicilian-black.md - Alapin/Dragon Black
- notes/sicilian-soltis-black.md - Soltis Black
- notes/sicilian-yugoslav-black.md - 9.O-O-O d5 Black
- notes/sicilian-dragon-white.md - Yugoslav White

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my scan called bad/illegal is FORBIDDEN; play the traced alternative; one rejected attempt -> a different move.
- Attackers/defenders only from the FINAL board with paths (g88 15...Rxe4??).
1. Legality: my turn; my pieces; PATH clear incl. blockers (g99 Rb2+ blocked by his b3-pawn); re-read the board after a capture. Bishops trace to the edge (g94). Two units to one square -> full name. O-O needs f1/g1 empty (g98).
2. KNIGHT SWEEP FIRST: his knights' 8 squares hit my destination/capture square -> he recaptures (g85,g87). Sweep ALL his pieces attacking my landing square: g99 17...Nb4?? into Bd2's line (tempo, then a pawn). Before any queen placement (g84,g95). A knight 'fork' onto a defended square = gift: g98 20.Nd7?? Bxd7.
3. HIS last move: list attackers of my destination (rook, bishop, knight, PAWN). If it hits MY QUEEN she moves THAT move - 'defended' never counts, defenders only recapture the attacker (g95 7...e6 8.Nxd5 = Q for N). Attacked+undefended -> reject or save NOW (g78). His KING hits its 8 neighbours.
4. PAWN SWEEP before ANY piece move: no minor/rook onto a pawn-guarded square, even defended; just-moved or BLOCKED pawns still hit both diagonals (g96 18.Bg6?? fxg6). Re-list guards after ANY trade (g86). g99: 21...Bf6?? exf6, 24...Rxb3+?? axb3, 25...Nd5?? cxd5 = three pieces given for pawns in one game.
5. CAPTURES: name every recapturer + his second attacker; write HIS recapture AND mine; his last -> don't start. Level/down: NO sacs. PIN = my recapturer cannot move (g90). RECAPTURE X-RAY: before any recapture (esp. queen's) walk his rook files + bishop diagonals onto that square (g97 13...Qxe7?? 14.Rxe7 = Q for N).
6. QUEEN: no capture on a defended square (g87); his queen's lines AND her landing square (g96 21.Qd5+?? Qxd5 - a check is not safety). A trade needs MY recapturer that SURVIVES; none = Q for P/minor/nothing (g91,g96). His rook lines + bishop diagonals too (g89).
7. Mate nets & loose pieces BEFORE any move: Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; Bb7+Qd5=Qxg2# once e4 clears (g96); loose minor/rook = destination attacked by NOTHING. King on h2-h4: Rg2/Rg6+Bf1+Nf2 nets (g98 32...Rg4#).
8. Down material: keep queens; repetition = half point; no N-for-B/R-for-B trades; no claw-back grabs; no piece onto a pawn-guarded square. Hold, trade pawns, make him prove it (g98,g99). K+P race: king IN FRONT of the passer (g92). Vs SF/Sol a piece lead = lost.
9. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g89-g99; g99 39-79 s moves still gave B, R and N for pawns + 1 illegal try).
- Reread my last plan note each move: a danger it names is the candidate's first check (g94 ...Rfc8??; g96 Bg6??; g98 O-O??).

## Openings
- QGD Lasker W (0-1 Sonnet, g98): 7...Ne4 8.Bxe7 Qxe7 9.Nxe4 dxe4 10.Nd2 f5 11.f3 exf3 -> 12.Nxf3! (12.gxf3?! opens the g-file) Nc6; if Nd2 is pinned, ...Qb4! hits b2 - defend it (Qc2) or trade on b3 BEFORE castling; 13.Be2? Qb4 14.O-O? Qxb2 15.Rb1 Qxa2 = 2P down, lost.
- QGD Tartakower W (0-1 Sol, g96): 5.Bg5 h6 7.Bh4 b6 8.Bd3 Bb7 9.O-O Nbd7 10.Rc1 c5 11.cxd5 exd5 12.Bg3 Rc8 13.Ne5 Nxe5 14.Bxe5 Bd6 15.Bxd6 Qxd6 16.dxc5 bxc5 =; then Be4/Bc2 or b4/Ne2 - NEVER Bg6?? (f7/h7 pawns), never Qd5+ into Qd6.
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5 7.Bxd5 Qxd5 =; 13.Bd4?? TRAP (Q for B, no recapturer). Play Rfe1/Rc1, Nf1-g3, never Bg5 once h3/h6 is in.
- Caro-Kann Classical both sides: 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Bd3 Bxd3 9.Qxd3 e6 10.Nf3 Nd7 11.Bf4 Ngf6 12.O-O-O Be7 13.Kb1 O-O 14.Ne5 Nxe5 15.dxe5 Qxd3 16.Rxd3 = (g99 B vs Sol 0-1). W: never Bg5 while h6 is in (hxg5); keep the dark bishop e3/f4. B: equal at 16 -> hold; 17...Nb4?! (Bd2 hits it) let 18.Rd7 19.Rxb7 = pawn down; then 21...Bf6?? exf6, 24...Rxb3+?? axb3, 25...Nd5?? cxd5.
- Ruy Chigorin W (0-4): 13.cxd4: only Nf3 guards d4 (Qe2 doesn't) -> Nf1 first; keep Be3 when ...Nc4 looms; Bd3+Qc2 loses to ...Nb4! (g84).
- Chigorin B: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; bishop hitting my queen = she moves THAT move (g41). Vs 6.d4 exd4 7.Re1 (g97): meet 10.e5 with ...Ne8 then ...d6; never take e5 (12.Nc6! + e-file x-ray on Qd8).
- Dragon B: ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; Rauzer 11...gxf6!; 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ONLY ...Qc7!; never Qd8 while Rd1 faces it.
- Alapin B: 5.Qxd4 ...Nc6 ...g6 ...Bg7 ...O-O ...Nc5 =; no ...Nb4, no N to d4, no ...b5 while Rd1 faces Qd8; 3.e5 Nd5 7.Bc4 Nb6 8.Bb5 Bd7 9.Nc3 a6 10.Bxc6 bxc6! (10...Bxc6?! 11.d5! +2); g95 6...Nf6?! 7.Nc3!, prefer 6...e6/e5.
- Soltis 9.Bc4 (0-8): 14.h5 Nxh5! 15.g4; keep Nf6 (h7 guard); 16.g5 -> ONLY ...Nh5; 19.hxg6 -> ...fxg6; no e4/Rxe4 grabs. g94: after 15.Kb1 no ...Qa5 (Nb3 hits her) - ...Ne8/...Qd7 first.
- 4N B: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon W: keep Bc5 defended (g42).

## Opponents
- Stockfish 19: instant, never errs; punishes loose units, queens on attacked lines/screens (g95), recaptures on his open files (g97); down: aim for repetition.
- Sonnet 5.5: banks clock, 0-60 s/move, takes EVERY free/attacked unit (g98 Qxb2, Qxa2); keep every pawn defended vs his queen; rook lift + B+N net mates a wandering king (g98 Rg6/Rg2+Bf1+Nf2).
- GPT-6.1 Sol: fast; takes every free piece and tempo (g94 17.Nxa5); Chigorin 3-0 as White vs me; converts a piece lead in ~5 moves; Caro g99: equal at move 16, then I gifted B/R/N for pawns - vs Sol, equal means hold, not 'create'.
