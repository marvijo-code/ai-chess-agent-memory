# Pre-move scan & blunder catalogue (g1-g77)

## SELF-BAN (g67, g70, g74, g77)
- A move my own note/scan called bad, illegal or 'not on' is FORBIDDEN; send the traced alternative (g67 26.Rxe7??; g70 23.Rxe5??; g74 15...Nxh5??; g77 25.Nf5+ even though my ply-49 note called it a sac with no follow-up). Reread my last note before every move.

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my turn; my pieces; geometry; PATH clear of EVERYTHING incl. my own pieces (g70 Be3 blocked by own Nd2); never echo his move or repeat a piece's square; two pieces to one square -> full name; one rejected attempt -> different move; 3 invalid = forfeit.
2. HIS last move FIRST: every enemy attacker of my destination - rook file/rank, BISHOP DIAGONALS, knights, PAWNS (g68 Ra6??; g73 23.Be5?? dxe5). Attacked+undefended -> reject. His KING hits its 8 neighbours - never move/check onto a king-adjacent square unless defended (g55 Rd2?? Kxd2; g77 28.Qh6+?? Kxh6).
3. Pawns: never onto a pawn-attacked square even if defended; is this pawn my piece's sole guard? Recapture MY push (g63 b5??)? Push opens a file - who enters first (g61)?
4. QUEEN: enemy PAWNS'/KNIGHTS' capture squares FIRST, then N/B/R/Q lines; no queen facing his rook/queen on an open line (g61 Qa3?? Rxa3; g63 Qa5?? Rxa5); Qd4 vs his e5-pawn = Q for P (g67, g70). His capture can open a line - after 23...dxe5 (g73) his Rd8 hit my Qd1: leave the FILE that move (Qe2/Qc2), never along it (24.Qd2?? Rxd2).
5. Trades/sacs: count ALL recapturers (PAWNS, bishops, knights); write HIS recapture and MINE; if his side makes the last capture, don't start (g70 Rxe5 dxe5; g75 18...Rb5?! 19.Rxb5 Bxb5 20.Bxb5). Value the chain (g58 Bxd4 = R for N+B); sacs need every recapturer + net (g65 Bxh6 = B+Q for 2P). Level or DOWN: no sacs (g77 25.Nf5+? gxf5, 27.f6+?); checks don't make a sac sound and a pawn recapture beats it. A recapture that arrives with check is not a trade to seek (g77 20.Bxc5?? Qxc5+).
6. Loose minors/rooks: before a jump, retreat or rook swing list every enemy attacker of the destination + chain (g58 Nd4??; g63 Nb4?? cxb4; g68 Ra6??; g70/g73 Bd3??).
7. Mate nets before ANY move: Qh2+Rh1 open h-file (Nf6 = h7's only guard, g66); Qh6+rook h4/h5 = Qxh7# (g69, g74); Q+B on f2 (g61); Q+Bc6 long diagonal vs my castled king = Qxg2# - take the bishop or block (g77 40.gxf4?? Qg2#); O-O-O Qa1/a2/b2 (g6); rank-1 Qxf2/Qxg2#.
8. Down material: defend/trade, 5-15 s, no undefended pieces; pawn down -> keep queens (g68 Be6? Qxd8); repetition/stalemate = half point; when winning make progress; never resign (<1 min: 1-2 s).
9. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s; lost 1-5 s. 30-90 s thinks never prevented a blunder or an illegal try (g50-g77; g77: 43-46 s routine m13-17 -> 5:35 vs 11:01).

## Patterns
- Queen: onto a pawn-attacked/covered square, in front of his rook on an open line, or with no recapturer (g48-g73).
- Checks with an undefended piece onto a square adjacent to his king (g77 28.Qh6+?? Kxh6, the game); desperate sacs when level or down (g77 25.Nf5+, 27.f6+).
- 'Active/centralizing' piece onto a pawn's capture square (g73 Be5?? dxe5); a B-for-N that gives him a check-recapture with centralization (g77 20.Bxc5?? Qxc5+).
- Covered-unit grabs; captures whose follow-up is blocked; sacs with 2+ recapturers (g65); f2-battery (g61); h7 nets (g66, g69); g2 nets via Bc6 long diagonal (g77).
- Rook/knight/bishop onto a pawn-attacked or bishop/knight-covered square (g68 Ra6, g70/g73 Bd3).
- Sending a self-banned move (g67, g70, g74); 2-3 illegal tries in complex middlegames (g68, g70) - trace path and destination twice.
- vs Sonnet, level or winning: no speculative sacs; keep every unit defended.
