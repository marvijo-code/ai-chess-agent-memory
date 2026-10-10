# Pre-move scan & blunder catalogue (g1-g82)

## SELF-BAN
- A move my own note/scan called bad, illegal or 'not on' is FORBIDDEN; send the traced alternative (g67; g70 23.Rxe5??; g74 15...Nxh5??; g77 25.Nf5+). Reread my last note before every move.

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my turn; my pieces; PATH clear of EVERYTHING incl. my own; never echo his move or repeat a piece's square; two to one square -> full name; 3 invalid = forfeit. QUEEN LINES: trace square by square - e2-d4 is no queen move (g82 Qxd4 rejected). After a capture re-read the board (g78 Kxe1 legal).
2. KNIGHT SWEEP FIRST: his knights' 8 squares each; if my destination or my capture's landing square is one, assume he recaptures. g82: 18.Nxd4?? Nxd4 (c6-d4; I had no recapturer on d4 - c-pawn gone, Qe2 cannot reach it) = piece for pawn; 22.Rxe7?? Nxe7 (c6-e7); 23.Qxd5?? Nexd5 (e7-d5 AND f6-d5).
3. HIS last move: every attacker of my destination - rook file/rank, BISHOP diagonals (g82 20.Nf5?? Bd7xf5), knights, PAWNS (g68 Ra6??; g73 dxe5). Attacked+undefended -> reject. Save my hit piece NOW (g78 18.Nh5?? left Be3 to ...Nxe3!). His KING hits its 8 neighbours (g77 28.Qh6+?? Kxh6).
4. Pawns: never onto a pawn-attacked square even if defended; is this pawn my piece's sole guard? Recapture MY push (g63 b5??)? Push opens a file - who enters first (g61; g81 17...dxe5)?
5. QUEEN: enemy PAWNS'/KNIGHTS' capture squares FIRST, then N/B/R/Q lines; Qd4 vs his e5-pawn = Q for P (g67,g70). No queen facing his rook/queen on an open line (g61 Qa3?? Rxa3); a file his capture opens -> leave the line (g73). SCREEN: my Q and his Q/R on one rank/file - count blockers; never move the last pawn/knight one, move my queen off first (g79 20...gxh5??; g81 17...dxe5??).
6. Trades/sacs: count ALL recapturers (PAWNS, bishops, knights) + his second attacker after my recapture; write HIS recapture and MINE; his last => don't start (g70 Rxe5 dxe5; g75 18...Rb5?!). Sacs need every recapturer + net; a pawn recapture beats a check-sac (g77 25.Nf5+?, 20.Bxc5?? Qxc5+). Level or down: NO sacs and no N-for-B/R-for-B 'trades' while down (g82 20.Nf5, 22.Rxe7).
7. Loose minors/rooks: before a jump, retreat or rook swing list every enemy attacker of the destination + chain (g58 Nd4??; g68 Ra6??; g78 23.Re2??).
8. Mate nets before ANY move: Qh2+Rh1 open h-file (Nf6 = h7's only guard, g66); Qh6+rook h4/h5 = Qxh7# (g69,g74); Q+B on f2 (g61); Q+Bc6 long diagonal = Qxg2# (g77 40.gxf4??); O-O-O Qa1/a2/b2 (g6).
9. Down material: defend/trade, 5-15 s, no undefended pieces; keep queens (g75); pawn-down same-colour-B endings vs SF are lost - keep every pawn defended (g76); repetition/stalemate = half point; never resign. A pawn that falls to ...exd4/Nc6 with no second recapturer stays lost - no piece sac to regain it (g82 18.Nxd4??).
10. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s; lost 1-5 s. Long thinks never prevented a blunder (g50-g82; g82 moves 14-25 40-61 s, then 3 blunders).

## Patterns
- Knight geometry (worst recurring miss): unseen recaptures on e7/d5/d4 (g82); a queen on e2 'defending' d4 (impossible); knight = 2+1 file/rank - count it, never assume.
- Screen: my Q and his Q/R on one rank/file - moving the last pawn/knight between them loses the queen (g79 gxh5??; g81 dxe5??).
- Queen: onto a pawn-attacked/covered square, in front of his rook on an open line, or with no recapturer (g48-g73).
- Checks with an undefended piece next to his king (g77 28.Qh6+??); desperate sacs level/down (g77 25.Nf5+).
- 'Active' piece onto a pawn's capture square (g73 Be5?? dxe5); B-for-N giving a check-recapture (g77 20.Bxc5?? Qxc5+).
- Covered-unit grabs; captures whose follow-up is blocked; sacs with 2+ recapturers (g65).
- Rook/knight/bishop onto a pawn-attacked or B/N/R-covered square (g68, g70/g73, g78 Re2, g82 Nf5).
- Self-banned move sent (g67,g70,g74); illegal tries - trace path twice; e2-d4 no queen line (g82).
- vs Sonnet/Sol, level or winning: no speculative sacs; keep every unit defended.
