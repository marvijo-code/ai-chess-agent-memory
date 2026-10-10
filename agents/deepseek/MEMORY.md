# Chess memory

Notes (read at start):
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g60
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White (g57,g60)
- notes/sicilian-black.md - Alapin/Dragon/Rauzer as Black (g58,g59)
- notes/sicilian-soltis-black.md - 9.Bc4 Soltis (g49,g53-g55)
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- My turn; my pieces only; never echo his move; path clear incl. own blockers; destination empty or enemy-held.
- Knight geometry: c5 -> e4/e6/d3/d7/b3/b7/a4/a6; f6 -> e4/g4/h5/h7/e8/g8/d5/d7.
- One rejected attempt: never resend - play a different, twice-traced move. Never send a move my own reasoning rejected.

## Rule 1 - pre-move scan (5 s, FINAL position; overrides any plan)
1. HIS last move first: what does it attack now? Name every enemy piece that attacks my destination, tracing its path; attacked+undefended -> reject; moving vacates guards.
2. His KING attacks the 8 squares around it: never an undefended piece there (g55 27...Rd2?? Kxd2).
3. Save my attacked/loose piece NOW; a queen attacked by a rook must MOVE; his rook on my 2nd rank: moving a blocker drops the piece behind it (g52).
4. Pawn pushes/recaptures: is this pawn the SOLE guard of my piece? Never onto a defended piece/pawn attack, or while it guards my piece.
5. Queen: name every enemy piece covering the destination - PAWNS FIRST, then knight/bishop/rook/queen lines - and my recapturer if his queen takes mine there. Flank squares touch pawns: g60 21.Qxa4?? bxa4 = Q for P; g58 22...Qxd5?? cxd5; g59 22...Qxb5?? Nxb5.
6. Captures/trades: count ALL recapturers - PAWNS, knights, rooks, queens - and value the chain: R for N+B = -1 (g58 13...Bxd4). If HIS side makes the last capture, it loses. A capture needing a follow-up: verify the follow-up on the CURRENT board (pieces present, paths open, defenders counted): g60 18.Nxe5?? dxe5 planned 19.d6, but d6 had no defender (Nd2 blocked Qd1) and Bxd6 just took it (class g57).
7. H-file mate: never move h7/h5's sole guard while his Q+Rh1 aim there; ...Nh5 blocks only once his g4-pawn has left.
8. Knight: never undefended or attacked by pawn/bishop/rook/queen. Before a jump OR a retreat when hit, list every enemy attacker of the square - rooks on file/rank, BISHOP diagonals, knights, pawns - and the chain (g58 12...Nd4?? Rxd4!; g59 13...Na4?? 14.Nxa4 Bxa4 15.Qxa4). The retreat square must be attacked by NOTHING; attacking something is not safety.
9. Down material: defend/trade, 5-15 s, no undefended pieces, keep playing (repetition/stalemate = half point); when winning make progress.
10. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g46-g60; g60: 40-51 s on m16-22 routine moves, then hung the queen).

## Openings
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; ...a5-a4 -> step Nb3 away (17.Nbd2); 14...Nb8: 15.Nf1 Nbd7 16.Be3. No 18.Nxe5?? grab on e5 (g60); no Nc4 while b5 hits c4; keep Nd2 guarded, e3 empty for Be3.
- RL as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; resolve the centre before his d5.
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O. No ...Nxe4 while his Qf3 covers e4; b7 loose once b5 leaves; Rauzer 11...gxf6!.
- Delayed Alapin 4.c3: 5.Qxd4 (g58) ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5 + ...Bd7/...Rc8/...Qa5 = equal; NO knight to d4. 5.cxd4 (g59): prefer 4...dxc3/4...Nf6 to 4...Nc6?!.
- Soltis 9.Bc4: 14.h5 Nxh5! 15.g4 Nf6; 16.g5 -> ONLY 16...Nh5; 16.Qh2 with g4 on: NOT ...Nh5 (17.gxh5!). g6 is h5's sole guard: never ...gxf5 while a knight sits on h5.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended; no queen on a1-net squares.

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked lines, loose bishops, back-rank; wins recapture chains. Bank clock early.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit (g60: bxa4, Nc2, Nxe4, Qxb2 all free); keep everything defended; never resign vs him; 1-3 s when lost.
- GPT-6.1 Sol: fast; takes every free piece. Soltis storm: ...Nh5 only once his g4-pawn has left. g57 mate net: Qxf2+ then Qxg2# with a rook on rank 2 - keep f2/g2 covered; no greedy grabs under mate threat; match his speed.
