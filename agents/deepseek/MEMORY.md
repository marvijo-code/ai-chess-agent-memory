# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Alapin/Dragon as Black
- notes/sicilian-soltis-black.md - Soltis 9.Bc4 as Black (g66 Qxh7#)
- notes/sicilian-yugoslav-black.md - Yugoslav 9.O-O-O as Black
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- My turn; my pieces only; never echo his move or repeat a piece's current square; path clear incl. own blockers (g65 'Rad1' illegal: Bb1 blocks Ra1); destination empty or enemy-held; two pieces reach one square -> full name (Rfd8); ambiguous = invalid (g62).
- Knight geometry: c5->e4/e6/d3/d7/b3/b7/a4/a6; f6->e4/g4/h5/h7/e8/g8/d5/d7.
- One rejected attempt: never resend; play a different, twice-traced move. Never send a move my own reasoning rejected.

## Rule 1 - pre-move scan (5 s, FINAL position)
1. HIS last move first: what does it attack now? Name every enemy piece attacking my destination incl. his ROOK's file/rank (g62 Bd4?? Rd6xd4; Rb7?? Rxb7). attacked+undefended -> reject; moving vacates guards.
2. His KING attacks its 8 neighbour squares: no undefended piece there (g55 27...Rd2?? Kxd2).
3. Save my attacked/loose piece NOW; a queen hit by a rook must MOVE; his rook on my 2nd rank: moving a blocker drops the piece behind it.
4. Pawn push: sole guard of my piece? Never onto a defended pawn-attacked square. Recapture MY pushed pawn? (g63 13...b5?? axb5: a7 takes b6 only, Bd7 blocked). Push that opens a file: who enters first? (g61 21.b4? axb3 22.axb3?! Rxa1; 22.Nxb3 holds).
5. Queen: PAWNS FIRST, then N/B/R/Q lines - never onto a file/rank/diagonal facing his rook/queen (g61 Qa3?? Rxa3; g56,g58,g60). His capture can open a line: 'safe' squares turn fatal (g63 Qa5?? Rxa5). Screen pawn on his rook's file that is also the sole guard of an attacked piece: his capture forces RxQ (g64 11...b5?? 12.Bxc5!); fix: Q off the file.
6. Trades: count ALL recapturers, PAWNS first; value the chain (g58 Bxd4 = R for N+B). Last capture by HIS side loses. Follow-ups: verify on the CURRENT board (g60,g61 Nxe5?? dxe5). Sac: count every recapturer + net (g65 21.Bxh6?? gxh6 22.Qxh6 Bxh6 = B+Q for 2 pawns).
7. H-file storm: never move h7/h5's sole guard while his Q+Rh1 aim there; ...Nh5 blocks only after his g4-pawn leaves. His Q on h2, h-file open, g4 still on g4: Nf6 is the ONLY h7 guard (it captures Qh7; Rh1 defends, so Kg8 can't) - ANY knight move = Qxh7# (g66 17...Nxe4?? 18.Qxh7#; 16...Rc8?? bad). After 17.g5 (g4 vacated) ONLY ...Nh5.
8. Knight: never undefended or pawn/bishop/rook/queen-attacked; before a jump OR retreat list every enemy attacker of the square (rooks file/rank, bishop diagonals, knights, pawns) + chain (g58 Nd4?? Rxd4!; g59 Na4??; g63 Nb4?? cxb4); retreat square attacked by NOTHING.
9. His Q+B battery on f2: guard f2 with a piece or block the diagonal; side moves allow the sac + rank-1 mate (g61).
10. Down material: defend/trade, no undefended pieces, no desperate grabs; repetition/stalemate = half point; when winning make progress.
11. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (40-60 s thinks all blundered, g46-g66).

## Openings
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; ...a5-a4 -> 17.Nbd2; 14...Nb8: 15.Nf1 Nbd7 16.Be3. No Nxe5 grabs; no Nc4 while b5 hits it; keep Nd2 guarded, e3 free for Be3; after ...a4 never open the a-file; ...h6+...Bf8 guards h6 twice: no Bxh6 sac (g65).
- RL as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; resolve the centre before his d5.
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O. No ...Nxe4 while his Qf3 covers e4; b7 loose once b5 leaves; Rauzer 11...gxf6!.
- Alapin 5.Qxd4: ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5 = equal; NO knight to d4; never ...b5 with his a4-pawn (axb5 wins a pawn) or while Rd1 faces Qd8 through d6; never ...Nb4; never Qa5 once the a-file opens. 5.cxd4: prefer 4...dxc3/4...Nf6.
- Soltis 9.Bc4: 14.h5 Nxh5! 15.g4 Nf6; 16.g5 -> ONLY 16...Nh5; 16.Qh2 (g4 on): NO ...Nh5 (17.gxh5) and NO knight move (Rule 7) - keep Nf6, try ...Qa5; after 17.g5 ONLY 17...Nh5. g6 is h5's sole guard: never ...gxf5 while a knight sits on h5.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended; no queen on a1-net squares.

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked lines or behind a lone screen pawn, back-rank, chains; bank clock early.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit incl. plain recaptures; 9-min think then instant; keep all defended, never sac speculatively; never resign; 1-3 s when lost.
- GPT-6.1 Sol: fast (3-13 s); takes every free piece/open-file loot instantly; keep files closed, all defended; in the Soltis attack it waits for a guard to leave, then mates (g66).
