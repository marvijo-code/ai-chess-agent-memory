# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Alapin/Dragon as Black
- notes/sicilian-soltis-black.md - Soltis 9.Bc4 as Black
- notes/sicilian-yugoslav-black.md - Yugoslav 9.O-O-O as Black
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- My turn; my pieces only; never echo his move or repeat a piece's current square; PATH clear of ALL pieces, own AND his (g68 Rd6-d2 blocked by his Bd3; Bg4-f5 blocked by own f5-pawn); destination empty or enemy-held; two pieces reach one square -> full name (Rfd8); ambiguous = invalid (g62).
- Knight geometry: c5->e4/e6/d3/d7/b3/b7/a4/a6; f6->e4/g4/h5/h7/e8/g8/d5/d7.
- One rejected attempt: never resend; play a different, twice-traced move. Never send a move my own scan/note called bad (g67: Rxe7).

## Rule 1 - pre-move scan (5 s, FINAL position)
1. HIS last move first: what does it attack now? Name every enemy piece attacking my destination incl. his ROOK's file/rank and BISHOP's diagonals (g68 18...Ra6?? Bd3 covers a6 - the loot a2 was free but a6 hung). attacked+undefended -> reject; moving vacates guards.
2. His KING attacks its 8 neighbour squares: no undefended piece there (g55 27...Rd2?? Kxd2). Save my attacked/loose piece NOW; a queen hit by a rook must MOVE; his rook on my 2nd rank: moving a blocker drops the piece behind it.
3. Pawn push: sole guard of my piece? Never onto a defended pawn-attacked square. Recapture MY pushed pawn? (g63 13...b5?? axb5). Push that opens a file: who enters first? (g61 21.b4? axb3 22.axb3?! Rxa1; 22.Nxb3 holds).
4. Queen: list enemy PAWNS' capture squares FIRST, then N/B/R/Q lines - never onto a file/rank/diagonal facing his rook/queen (g61 Qa3?? Rxa3; g67 23.Qd4?? e5-PAWN+Nc6). His capture can open a line: 'safe' squares turn fatal (g63 Qa5?? Rxa5). Screen pawn on his rook's file + sole guard of an attacked piece: his capture forces RxQ (g64 11...b5?? 12.Bxc5!).
5. Trades: count ALL recapturers, PAWNS first; value the chain (g58 Bxd4 = R for N+B). Recount attackers vs defenders of my advanced pawn before a trade near it (g67 d5). Last capture by HIS side loses. Sac: count every recapturer + net (g65 21.Bxh6?? = B+Q for 2 pawns).
6. H-file storm: his Qh2 + Rh1 (h-file open): Nf6 is h7's ONLY guard - ANY knight move = Qxh7# (g66). His Qh6 + rook on h4/h5: Qxh7# is mate (rook covers h7 through the empty h6); a free piece never matters - make LUFT (...Re8, f8 escape) or cover/block h7 FIRST, no grabs/side moves until h7 is safe (g69 22...Rxd4?? Qxh7#).
7. Knight/rook/bishop: before a jump, retreat OR rook swing list every enemy attacker of the destination (rook lines, bishop diagonals, knights, pawns) + chain; destination/retreat square attacked by NOTHING (g58 Nd4??; g63 Nb4?? cxb4; g68 Ra6?? Bd3 covers a6).
8. His Q+B battery on f2: guard f2 or block the diagonal; side moves allow the sac + rank-1 mate (g61).
9. Down material: defend/trade, no undefended pieces, no desperate grabs; a pawn down -> AVOID queen trades, keep counterplay (g68 13...Be6? 14.Qxd8); repetition/stalemate = half point; when winning make progress.
10. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder or an illegal try (g46-g69; g69 m11-22 34-46 s -> Bxh6?, Qd8?, Rxd4??).

## Openings
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; ...a5-a4 -> 17.Nbd2; 14...Nb8: 15.Nf1 Nbd7 16.Be3. No Nxe5 grabs; no Nc4 while b5 hits it; keep Nd2 guarded, e3 free for Be3; no Bxh6 sac when ...h6+...Bf8 guard h6 twice (g65); g67: no Nf5 vs e4+Q, no Qd4 (e5-pawn+Nc6).
- RL as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; resolve the centre before his d5.
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O. No ...Nxe4 while his Qf3 covers e4; b7 loose once b5 leaves; Rauzer 11...gxf6!.
- Yugoslav 9.O-O-O, 9...d5: 10.exd5 Nxd5! 11.Nxc6 bxc6! 12.Nxd5 cxd5! 13.Qxd5 - KEEP QUEENS ON: 13...Qc7! (13...Be6? 14.Qxd8!). No rook to a6 vs Bd3; no rook on a rank/file facing his rook.
- Alapin 5.Qxd4: ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5 = equal; NO knight to d4; never ...b5 with his a4-pawn or while Rd1 faces Qd8 through d6; never ...Nb4; never Qa5 once the a-file opens. 5.cxd4: prefer 4...dxc3/4...Nf6.
- Soltis 9.Bc4 (0-5 vs Sol: g49,g53,g54,g66,g69): 14.h5 Nxh5! 15.g4 Nf6. 16.g5 -> ONLY 16...Nh5. 16.Qh2 (g4 on): NO ...Nh5, NO knight move - keep Nf6, try ...Qa5. 16.Bh6: do NOT recapture (17.Qxh6 + g5/Rxh5 storm; g49+g69 both lost) - ...Qe8/...Qa5 + ...Re8/...f5 luft first. After 18.g5 Nh5! 19.Rxh5 gxh5: play ...Re8 (f8 luft) AT ONCE; g6 is h5's sole guard while the knight sits there.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended; no queen on a1-net squares.

## Opponents
- Stockfish 19: ~0 s/move, never errs tactically; punishes loose units, queens on attacked lines or behind a lone screen pawn, back-rank, loose rooks (Bd3xa6); bank clock early; when lost play 1-5 s, never resign.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit incl. recaptures and pawns on attacked squares; 9-min think then instant; keep all defended, never sac speculatively; never resign; 1-3 s when lost.
- GPT-6.1 Sol: fast (3-13 s); takes every free piece/open-file loot instantly; vs the Soltis he plays Bh6, then the g5+Rxh5 exchange sac with Qh6+rook on the h-file - make f8 luft early and never grab with Qxh7# pending (g69); in g66 he waited for a guard to leave, then mated.
