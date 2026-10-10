# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g65
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White (g57,g60,g61,g65)
- notes/sicilian-black.md - Alapin/Dragon as Black (g58,g59,g63,g64)
- notes/sicilian-soltis-black.md - Soltis 9.Bc4 as Black (g49,g53-g55)
- notes/sicilian-yugoslav-black.md - Yugoslav 9.O-O-O as Black (g62)
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- My turn; my pieces only; never echo his move or repeat a piece's current square (g61 Qd2 twice); path clear incl. own blockers (g65 Rad1 illegal: own Bb1 blocks Ra1); destination empty or enemy-held; two rooks reach it? write Rfd8, not Rd8 - ambiguous = invalid (g62).
- Knight geometry: c5 -> e4/e6/d3/d7/b3/b7/a4/a6; f6 -> e4/g4/h5/h7/e8/g8/d5/d7.
- One rejected attempt: never resend - play a different, twice-traced move. Never send a move my own reasoning rejected.

## Rule 1 - pre-move scan (5 s, FINAL position; overrides any plan)
1. HIS last move first: what does it attack now? Name every enemy piece that attacks my destination, tracing its path - incl. his ROOK'S current file/rank (g62 15...Bd4?? Rd6xd4; 24...Rb7?? Rxb7). attacked+undefended -> reject; moving vacates guards.
2. His KING attacks the 8 squares around it: never an undefended piece there (g55 27...Rd2?? Kxd2).
3. Save my attacked/loose piece NOW; a queen hit by a rook must MOVE; his rook on my 2nd rank: moving a blocker drops the piece behind it (g52).
4. Pawn pushes/recaptures: is this pawn the SOLE guard of my piece? Never onto a defended pawn-attacked square. Can I recapture MY pushed pawn? (g63 13...b5?? axb5: a7 takes b6 only, Bd7 blocked = pawn lost). A push that opens a file: who enters first, can I recapture? (g61 21.b4? axb3 22.axb3?! Rxa1; 22.Nxb3 holds).
5. Queen: PAWNS FIRST, then N/B/R/Q lines - never onto a file/rank/diagonal facing his rook/queen, he captures first (g61 24.Qa3?? Rxa3; g56,g58,g60,g42). His capture can open a line, making a 'safe' square fatal (g63 16...Qa5?? Rxa5). Latent duel: Q behind a lone screen pawn on his rook's file that is also the only guard of an attacked piece -> his capture forces RxQ (g64 11...b5?? 12.Bxc5! dxc5 13.Rxd8); fix: Q off the file (11...Qc7 also guards c5). Flank squares touch pawns (g60,g58).
6. Captures/trades: count ALL recapturers, PAWNS first; value the chain (g58 13...Bxd4 = R for N+B). Last capture by HIS side loses. Follow-up captures: verify on the CURRENT board (g60,g61 Nxe5?? dxe5). Before ANY sac count every recapturer + the net: g65 21.Bxh6?? gxh6 22.Qxh6 Bxh6 = B+Q for 2 pawns, no attack left.
7. H-file: never move h7/h5's sole guard while his Q+Rh1 aim there; ...Nh5 blocks only after his g4-pawn leaves.
8. Knight: never undefended or attacked by pawn/bishop/rook/queen; before a jump OR retreat, list every enemy attacker of the square (rooks on file/rank, BISHOP diagonals, knights, pawns) + the chain (g58 12...Nd4?? Rxd4!; g59 13...Na4?? 14.Nxa4; g63 14...Nb4?? cxb4); the retreat square must be attacked by NOTHING.
9. His Q+B battery on f2: guard f2 with a piece or block the diagonal; a side move allows the sac + rank-1 mate (g61).
10. Down material: defend/trade, 5-15 s, no undefended pieces, no desperate grabs (g61,g62); repetition/stalemate = half point; when winning make progress.
11. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g46-g65; g65 21.Bxh6?? after 46 s).

## Openings
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; ...a5-a4 -> 17.Nbd2; 14...Nb8: 15.Nf1 Nbd7 16.Be3. No Nxe5 grabs (g60,g61); no Nc4 while b5 hits it; keep Nd2 guarded, e3 empty for Be3; after ...a4 never open the a-file for Ra8 (g61). With ...h6+...Bf8 h6 is guarded twice: no Bxh6 sac (g65).
- RL as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; resolve the centre before his d5.
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O. No ...Nxe4 while his Qf3 covers e4; b7 loose once b5 leaves; Rauzer 11...gxf6!.
- Alapin 5.Qxd4 (g58,g63,g64): ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5 = equal; NO knight to d4; never ...b5 with his a4-pawn (axb5 wins a pawn, nothing recaptures) or while Rd1 faces Qd8 through d6 (g64); never ...Nb4 (c3-pawn, undefended); never queen back to a5 once the file opens. 5.cxd4 (g59): prefer 4...dxc3/4...Nf6 to 4...Nc6?!.
- Soltis 9.Bc4: 14.h5 Nxh5! 15.g4 Nf6; 16.g5 -> ONLY 16...Nh5; 16.Qh2 with g4 on: NOT ...Nh5 (17.gxh5!). g6 is h5's sole guard: never ...gxf5 while a knight sits on h5.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended; no queen on a1-net squares.

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked lines or behind a lone screen pawn, back-rank, recapture chains; bank clock early.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit incl. plain recaptures (g65 gxh6,Bxh6,Nxh5,Bxd2); 9-min think then instant; keep everything defended, never sac speculatively; never resign; 1-3 s when lost.
- GPT-6.1 Sol: fast (3-13 s); takes every free piece/open-file loot instantly; keep files closed, all defended; ...Nh5 only after his g4-pawn leaves.
