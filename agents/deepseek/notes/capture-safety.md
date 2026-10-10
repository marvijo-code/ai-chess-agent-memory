# Pre-move scan & blunder catalogue (g1-g85)

## SELF-BAN
- A move my note/scan called bad, illegal or 'not on' is FORBIDDEN; send the traced alternative (g67, g70 23.Rxe5??, g74 15...Nxh5??, g77 25.Nf5+). Reread my last note before every move.

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my turn; my pieces; PATH clear of EVERYTHING incl. my own; never echo his move or repeat a piece's square; two of my pieces reach one square -> full name; 3 invalid = forfeit. QUEEN LINES: trace square by square - e2-d4 is no queen move (g82). After a capture re-read the board (g78 Kxe1 legal).
2. KNIGHT SWEEP FIRST: his knights' 8 squares each; if my destination or my capture's landing square is one, assume he recaptures. g85: 15.Qxd4?? Nxd4 = Q for N (c6-knight and Rd8 both hit d4). g82: 18.Nxd4?? Nxd4, 22.Rxe7?? Nxe7, 23.Qxd5?? Nexd5.
3. HIS last move: every attacker of my destination - rook file/rank, BISHOP diagonals (g82 20.Nf5?? Bd7xf5), knights, PAWNS (g68 Ra6??). Attacked+undefended -> reject. Save my hit piece NOW (g78). His KING hits its 8 neighbours (g77 28.Qh6+??).
4. Pawns: never onto a pawn-attacked square even if defended; is this pawn my piece's sole guard? Recapture MY push (g63 b5??)? Push opens a file - who enters first (g61; g81 17...dxe5)?
5. QUEEN: enemy PAWNS'/KNIGHTS' capture squares FIRST (g67,g70), then N/B/R/Q lines. Recapture with the PAWN, never the queen, on a square his knight sweeps (g85). No queen facing his rook on an open line (g61); a capture that opens a file -> leave the line (g73). SCREEN: count blockers between my Q and his Q/R; never move the last; his capture of the last IS an attack - step off or trade THAT move (g79,g81,g83). Queen attacked: MOVE it, never grab (g84 20.Qxc8?? Rxc8).
6. Trades/sacs: count ALL recapturers (PAWNS, bishops, knights) + his second attacker after my recapture; write HIS recapture and MINE; his last => don't start (g70 Rxe5 dxe5). A pawn recapture beats a check-sac (g77 25.Nf5+?). Level or down: NO sacs, no N-for-B/R-for-B 'trades' (g82 20.Nf5, 22.Rxe7).
7. Loose minors/rooks: before a jump, retreat or rook swing list every enemy attacker of the destination + chain (g58 Nd4??; g68 Ra6??; g78 23.Re2??).
8. Mate nets before ANY move: Qh2+Rh1 open h-file (Nf6 = h7's only guard, g66); Qh6+rook = Qxh7# (g69,g74); Q+B on f2 (g61); Q+Bc6 long diagonal = Qxg2# (g77); O-O-O Qa1/a2/b2 (g6).
9. Down material: defend/trade, 5-15 s, no undefended pieces; keep queens (g75); repetition/stalemate = half point; never resign. A pawn that falls to ...exd4/Nc6 with no second recapturer stays lost - no piece sac (g82).
10. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s; lost 1-5 s. Long thinks never prevented a blunder (g50-g85; g85 15.Qxd4?? after 49 s).

## Patterns
- Knight geometry (worst recurring miss): recaptures on d4/e7/d5 missed (g82); 'queen defends d4' impossible via e2; g85 queen recapture on c6's d4 with Rd8 behind = Q for N. Knight = 2+1 file/rank - count it, never assume.
- Recapture discipline: list attackers AND defenders of the recapture square; take back with the cheapest piece - pawn first, queen never on a knight's square (g85).
- Screen: my Q and his Q/R on one rank/file - moving the last pawn/knight between them loses the queen (g79 gxh5??; g81 dxe5??).
- Checks with an undefended piece next to his king (g77 28.Qh6+??); desperate sacs level/down (g77 25.Nf5+).
- 'Active' piece onto a pawn's capture square (g73 Be5?? dxe5); B-for-N giving a check-recapture (g77 20.Bxc5?? Qxc5+).
- Rook/knight/bishop onto a pawn-attacked or B/N/R-covered square (g68, g70/g73, g78 Re2, g82 Nf5).
- Self-banned move sent (g67,g70,g74); illegal tries - trace path twice (g82 e2-d4).
- vs Sonnet/Sol, level or winning: no speculative sacs; keep every unit defended - he takes every free unit (g85 Rxd4, Rxe2).
