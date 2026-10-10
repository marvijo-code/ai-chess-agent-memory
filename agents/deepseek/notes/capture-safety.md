# Pre-move scan & blunder catalogue (g1-g87)

## SELF-BAN
A move my note/scan called bad or illegal is FORBIDDEN; send the traced alternative (g67,g70,g74,g77). Reread my last note before every move.

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my turn; my pieces; PATH clear of EVERYTHING; never echo his move; two of my pieces reach one square -> full name (g87: both knights reached d2); 3 invalid = forfeit. BISHOPS: trace square by square to the edge (g86: Bxe7 and Bxf3 both illegal). QUEEN: e2-d4 is no queen line (g82). After a capture re-read the board.
2. KNIGHT SWEEP FIRST: his knights' 8 squares; if my destination or my capture's landing square is one, he recaptures (g87 18.Rxd7?? Nf6xd7 = R for B; 24.Nxe5?? Nd7xe5 = N for P; g85 15.Qxd4?? Nxd4; g82 18.Nxd4??, 22.Rxe7??).
3. HIS last move: every attacker of my destination - rook file/rank, BISHOP diagonals (g82 20.Nf5?? Bd7xf5), knights, PAWNS (g68 Ra6??). Attacked+undefended -> reject; save my hit piece NOW (g78). His KING hits its 8 neighbours (g77 28.Qh6+??).
4. Pawns: never onto a pawn-attacked square even if defended; a blocked pawn still attacks both diagonals (g87 19.Bd3?? cxd3, c4 hit b3/d3). Is this pawn my piece's sole guard? Recapture MY push? Push opens a file - who enters first (g61; g81 17...dxe5?? took Rd1-Qd8's last screen).
5. QUEEN: his PAWNS'/KNIGHTS'/BISHOPS' lines FIRST (g67,g70); NEVER a queen capture on a defended square - 16.Qxd6?? Bxd6 = Q for P (d6 defended by Be7; 51 s, g87). Recapture with the PAWN, never the queen, on a square his knight sweeps (g85). No queen facing his rook/queen on an open line; a capture that opens a file -> leave the line (g73). SCREEN: count blockers between my Q and his Q/R; never move the last one; his capture of the last IS an attack - step off or trade THAT move (g79,g81,g83). Queen attacked: MOVE it (g84 20.Qxc8?? Rxc8).
6. Trades/sacs: count ALL recapturers + his second attacker after my recapture; write HIS recapture and MINE; his last -> don't start (g70). Level/down: NO sacs (g77). My recapturing piece must still exist (g86 17...Bd3?! 18.Bxd3). A pawn lost to ...exd4/Nc6 with no second recapturer stays lost (g82).
7. Loose minor/rook (jump, retreat, swing): destination attacked by NOTHING, and walk his bishop diagonals to the edge (g86 23...Rb8?? 24.Bxb8; g78 23.Re2??; g80 21...Rd2+??). A check is not safety.
8. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+rook = Qxh7#; Q+Bc6 long diagonal = Qxg2# (g77); Qa1# after my O-O-O.
9. Down material/endgames: keep queens (g75); repetition = half point; down: no N-for-B or R-for-B 'trades', defend 1-5 s; never resign. NO claw-back grabs: g87's 18.Rxd7, 19.Bd3, 24.Nxe5 each hung more; every capture still passes the scan.
10. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g86 43 s on 17...Bd3; g87 51 s on 16.Qxd6??; g86 ended 4:19 vs 19:49; g87 3:23 vs 15:35).

## Patterns
- Knight geometry (recurring worst): recaptures on d4/e7/d7/e5 missed (g82,g85,g87); 'queen defends d4' impossible via e2; queen recapture on c6's d4 with Rd8 behind = Q for N (g85).
- Queen capture of a defended target = queen loss (g87 16.Qxd6?? Bxd6); a 'free' pawn defended by a bishop is bait.
- Recapture discipline: list attackers AND defenders of the recapture square; cheapest piece; queen never on a knight's square (g85); my recapturer must still exist (g86).
- Screen: my Q and his Q/R on one rank/file - moving the last blocker loses the queen (g79 gxh5??; g81 dxe5??).
- Sac/loss expecting a recapture that is not there: pawn gone (g86 Bd3), no second recapturer (g82 Nxd4).
- Rook/knight/bishop onto a pawn-attacked or B/N/R-covered square, or onto an open bishop diagonal (g68,g70,g73,g78,g80,g86; g87 19.Bd3).
- Self-banned or illegal move sent (g67,g70,g74,g82,g86 x2; g87 Nxd2): trace the path twice; never resend a rejected move.
- vs Sonnet/Sol, level or winning: no speculative sacs; keep every unit defended - they take every free unit (g85 Rxd4/Rxe2; g87 Bxd6, Nxd7, cxd3, Nxe5).
