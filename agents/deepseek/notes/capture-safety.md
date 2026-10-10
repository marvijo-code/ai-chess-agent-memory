# Pre-move scan & blunder catalogue (g1-g93)

## SELF-BAN
A move my note/scan called bad or illegal is FORBIDDEN; send the traced alternative (g77; g88 15...Rxe4??; g89 13.Bg5??; g91 19...Qxd6??); never resend a rejected move. Reread my last plan note every move.

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my pieces; PATH clear of EVERYTHING; never echo his move; two of my pieces reach one square -> full name. BISHOPS: trace to the edge. PIN: a piece between his B/R/Q and my K/Q cannot move or recapture (g90 Nxd4 illegal). Queen e2-d4 is no line (g82). After a capture re-read the board.
2. KNIGHT SWEEP FIRST: his knights' 8 squares; if my destination or capture landing square is hit, he recaptures (g87 18.Rxd7??; g85 15.Qxd4??).
3. HIS last move: every attacker of my destination - rook lines, bishops, knights, PAWNS (g89 13.Bg5?? hxg5!). Attacked+undefended -> reject; save my hit piece NOW (g78). His KING hits its 8 neighbours.
4. Pawns: never onto a pawn-attacked square even if defended; blocked pawns still hit both diagonals (g87 19.Bd3?? cxd3); a pawn's capture squares follow it (g89 h6xg5). Sole guard of a piece? After any trade re-list pawn guards (g86).
5. QUEEN: her pawn/knight/bishop lines first; NEVER a queen capture on a defended square (g87 16.Qxd6?? Bxd6). His QUEEN defends down files/diagonals - count it (g91 Qd1 guarded d6). A 'trade' needs MY recapturer that SURVIVES: his taking my queen with no legal unit of mine hitting the square = Q for P/B (g91 19...Qxd6?? 20.Qxd6+; g93 13.Bd4?? Bxd4 14.Qxd4?? Qxd4 - Nc3/Nd2 miss d4 and my queen was the d-file's last screen). Recapture with the PAWN, never the queen, where his knight sweeps (g85). List enemy ROOK files/ranks to the destination: zero screens = he takes first (g89 16.Qh3?? Rxh3).
6. Trades/sacs: count ALL recapturers + his second attacker after my recapture; write HIS recapture AND MINE; his last -> don't start (g70). Level/down: NO sacs. A rook taking a defended PAWN = R for P (g88 15...Rxe4?? 16.fxe4). My recapturer must exist and not be pinned (g86,g90).
7. Loose minor/rook (jump, retreat, swing): destination attacked by NOTHING; walk his bishop diagonals to the edge (g86 23...Rb8??; g78 23.Re2??). A check is not safety.
8. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+Ng5 = Qxh7# (g88); Q+Bc6 = Qxg2# (g77); Qa1# after my O-O-O.
9. Down material: keep queens (g75); repetition = half point; no N-for-B/R-for-B 'trades'; no claw-back grabs (g87-g91). Every capture still passes the scan.
10. Time: routine <=15 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g86-g93, all errors).

## Patterns
- Pinned recapturer / last-screen queen recapture (g90,g93): 11...Qxd4?? 12.Qxd4 and Nxd4 illegal (Bb5 pins Nc6 to Ke8) = Q for P; 13.Bd4?? Bxd4 14.Qxd4?? Qxd4 with my queen the only unit between his Qd8 and d4 = Q for B (Nc3/Nd2 never cover d4).
- Knight geometry (worst): recaptures on d4/e7/d7/e5 missed (g82,g85,g87); Qe2 does not defend d4; Nc3 does not defend d4.
- Queen on an enemy line: g89 Qh3?? Rxh3; g84 Qc2?? ...Nb4; g79/g81/g83 screens; g91 open d-file.
- Recapture discipline: list attackers AND defenders from the board; cheapest piece; PAWNS count (g88 fxe4).
- Undefended piece onto a pawn-hit square = pawn wins it (g87 19.Bd3??; g89 13.Bg5??): never develop to a square a pawn guards.
- Rook/knight/bishop to covered squares or an open bishop diagonal (g68-g86); a rook grabbing a pawn is R for P if a pawn recaptures (g88).
- Self-banned/illegal move sent (g67-g90): trace the path twice.
