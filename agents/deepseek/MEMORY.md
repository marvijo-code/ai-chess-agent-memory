# Chess memory

Notes (read at start):
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g62
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White (g57,g60,g61)
- notes/sicilian-black.md - Alapin/Dragon as Black (g58,g59)
- notes/sicilian-soltis-black.md - Soltis 9.Bc4 as Black (g49,g53-g55)
- notes/sicilian-yugoslav-black.md - Yugoslav 9.O-O-O as Black (g62)
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- My turn; my pieces only; never echo his move or repeat a piece's current square (g61 Qd2 twice = 92 s); path clear incl. own blockers; destination empty or enemy-held; two rooks reach it? write Rfd8, not Rd8 - ambiguous = invalid (g62).
- Knight geometry: c5 -> e4/e6/d3/d7/b3/b7/a4/a6; f6 -> e4/g4/h5/h7/e8/g8/d5/d7.
- One rejected attempt: never resend - play a different, twice-traced move. Never send a move my own reasoning rejected.

## Rule 1 - pre-move scan (5 s, FINAL position; overrides any plan)
1. HIS last move first: what does it attack now? Name every enemy piece that attacks my destination, tracing its path - incl. his ROOK'S current file/rank (g62 15...Bd4?? Rd6xd4; 24...Rb7?? Rxb7, c7 empty); attacked+undefended -> reject; moving vacates guards.
2. His KING attacks the 8 squares around it: never an undefended piece there (g55 27...Rd2?? Kxd2).
3. Save my attacked/loose piece NOW; a queen hit by a rook must MOVE; his rook on my 2nd rank: moving a blocker drops the piece behind it (g52).
4. Pawn pushes/recaptures: is this pawn the SOLE guard of my piece? Never onto a defended pawn-attacked square. A push that opens a file: who enters first, can I recapture? (g61 21.b4? axb3 e.p. 22.axb3?! Rxa1; 22.Nxb3 holds a1).
5. Queen: PAWNS FIRST, then N/B/R/Q lines - never onto a file/rank/diagonal facing his rook/queen, he captures first (g61 24.Qa3?? Rxa3; g56,g58,g60,g42). Flank squares touch pawns (g60 21.Qxa4?? bxa4; g58 22...Qxd5?? cxd5; g59 22...Qxb5?? Nxb5).
6. Captures/trades: count ALL recapturers, PAWNS first, and value the chain: R for N+B = -1 (g58 13...Bxd4). If HIS side makes the last capture, it loses. A capture needing a follow-up: verify it on the CURRENT board (g60,g61 Nxe5?? dxe5).
7. H-file: never move h7/h5's sole guard while his Q+Rh1 aim there; ...Nh5 blocks only after his g4-pawn leaves.
8. Knight: never undefended or attacked by pawn/bishop/rook/queen; before a jump OR a retreat, list every enemy attacker of the square (rooks on file/rank, BISHOP diagonals, knights, pawns) + the chain (g58 12...Nd4?? Rxd4!; g59 13...Na4?? 14.Nxa4); the retreat square must be attacked by NOTHING.
9. His Q+B battery on f2 (Qb6+Bc5): guard f2 with a piece or block the diagonal; a side move allows the sac + rank-1 mate (g61 30...Bxf2+ 31.Kh2 Bg3+ 32.Nxg3 Qe3 33...Qxg3+ 34.Kg1 Rb1+ 35.Rc1 Rxc1#; Qg3 covers f2/g2/h2).
10. Down material: defend/trade, 5-15 s, no undefended pieces, no desperate grabs (g61,g62); repetition/stalemate = half point; when winning make progress.
11. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g46-g62; g62: 35-55 s on routine m9-24, two blunders, still 8 min left). Sol's 3-13 s.

## Openings
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; ...a5-a4 -> step Nb3 away (17.Nbd2); 14...Nb8: 15.Nf1 Nbd7 16.Be3. No Nxe5 grabs (g60,g61); no Nc4 while b5 hits c4; keep Nd2 guarded, e3 empty for Be3; after ...a4 do not open the a-file for his Ra8 (g61: b4 only with 22.Nxb3 recapture).
- RL as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; resolve the centre before his d5.
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O. No ...Nxe4 while his Qf3 covers e4; b7 loose once b5 leaves; Rauzer 11...gxf6!.
- Yugoslav 9.O-O-O (g62): 9...Nxd4 10.Bxd4 Be6 11.Bxf6 Bxf6 12.Nd5 Bxd5 13.Qxd5 e6 14.Qxd6 Qxd6 15.Rxd6 = W+1 pawn, holdable: ...Rfc8/...Kf8/...Be7, keep Bf6 safe, hit b2/e4; no piece on a square his rook covers.
- Delayed Alapin 4.c3: 5.Qxd4 (g58) ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5 + ...Bd7/...Rc8/...Qa5 = equal; NO knight to d4. 5.cxd4 (g59): prefer 4...dxc3/4...Nf6 to 4...Nc6?!.
- Soltis 9.Bc4: 14.h5 Nxh5! 15.g4 Nf6; 16.g5 -> ONLY 16...Nh5; 16.Qh2 with g4 on: NOT ...Nh5 (17.gxh5!). g6 is h5's sole guard: never ...gxf5 while a knight sits on h5.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended; no queen on a1-net squares.

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked lines, back-rank; wins recapture chains. Bank clock early.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit (g60 Nc2/Nxe4/Qxb2; g62 Rxd4/Rxb7); keep everything defended; never resign vs him; 1-3 s when lost.
- GPT-6.1 Sol: fast (3-13 s); takes every free piece; open-file loot 22...Rxa1/24...Rxa3 instantly; keep files closed, everything defended; ...Nh5 only once his g4-pawn left; match his speed.
