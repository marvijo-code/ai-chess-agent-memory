# Pre-move scan & blunder catalogue (g1-g88)

## SELF-BAN
A move my note/scan called bad or illegal is FORBIDDEN; send the traced alternative (g67,g70,g74,g77; g88 15...Rxe4 - my own note flagged it). 3 invalid = forfeit; never resend a rejected move. Reread my last note every move.

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my pieces; PATH clear of EVERYTHING; never echo his move; two of my pieces reach one square -> full name (g87 N3xd2); one rejected try -> different move. BISHOPS: trace to the edge (g86 Bxe7/Bxf3 illegal). Queen e2-d4 is no line (g82). After a capture re-read the board.<div></div>
2. KNIGHT SWEEP FIRST: his knights' 8 squares; if my destination or capture landing square is hit, he recaptures (g87 18.Rxd7?? Nf6xd7; 24.Nxe5?? Nd7xe5; g85 15.Qxd4??; g82 18.Nxd4??, 22.Rxe7??).
3. HIS last move: every attacker of my destination - rook lines, BISHOPS (g82 20.Nf5??), knights, PAWNS. Attacked+undefended -> reject; save my hit piece NOW (g78). His KING hits its 8 neighbours (g77 28.Qh6+??).
4. Pawns: never onto a pawn-attacked square even if defended; a blocked pawn still hits both diagonals (g87 19.Bd3?? cxd3). Is this pawn my piece's sole guard? Recapture MY push? Push opens a file - who enters first (g81)? After any trade re-list pawn guards.
5. QUEEN: his pawn/knight/bishop lines first; NEVER a queen capture on a defended square - 16.Qxd6?? Bxd6 = Q for P (g87). Recapture with the PAWN, never the queen, on a square his knight sweeps (g85). No queen on an open line facing his Q/R; a capture that opens a file -> leave it. SCREEN: count blockers between my Q and his Q/R; never move the last; his capture of it IS an attack - step off or trade THAT move (g79,g81,g83). Queen attacked: MOVE it (g84).
6. Trades/sacs: count ALL recapturers + his second attacker after my recapture; write HIS recapture AND MINE; his last -> don't start (g70). Level/down: NO sacs (g77). A rook taking a defended PAWN = R for P; PAWNS are defenders too (g88 15...Rxe4?? 16.fxe4). My recapturer must still exist (g86 17...Bd3?! 18.Bxd3).
7. Loose minor/rook (jump, retreat, swing): destination attacked by NOTHING; walk his bishop diagonals to the edge (g86 23...Rb8?? 24.Bxb8; g78 23.Re2??). A check is not safety.
8. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6 + Ng5 = Qh7# vs castled king - h7 must be guarded or the knight taken (g88: 20...Qd7?? 21.Qh7#); Q+Bc6 = Qxg2# (g77); Qa1# after my O-O-O.
9. Down material: keep queens (g75); repetition = half point; no N-for-B/R-for-B 'trades'; no claw-back grabs (g87 x3; g88 down R for P - no risky captures). Every capture still passes the scan.
10. Time: routine <=15 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g86 43 s; g87 51 s; g88 38 s).

## Patterns
- Knight geometry (worst): recaptures on d4/e7/d7/e5 missed (g82,g85,g87); queen cannot defend d4 via e2; queen recapture on d4 with Rd8 behind = Q for N (g85).
- Recapture discipline: list attackers AND defenders; cheapest piece; PAWNS count (g88 fxe4); my recapturer must exist (g86).
- Rook grabs a pawn defended by a pawn = R for P (g88 15...Rxe4??); vs Sonnet/Sol no speculative sacs - they take every free/attacked unit (g85 Rxd4/Rxe2; g87 Bxd6/Nxd7; g88 fxe4).
- Rook/knight/bishop onto pawn-attacked or covered squares, or an open bishop diagonal (g68,g70,g73,g78,g80,g86; g87 19.Bd3).
- Self-banned/illegal move sent (g67,g70,g74,g82,g86 x2; g87 Nxd2): trace the path twice.
