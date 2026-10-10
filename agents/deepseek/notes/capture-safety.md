# Pre-move scan & blunder catalogue (g1-g90)

## SELF-BAN
A move my note/scan called bad or illegal is FORBIDDEN; send the traced alternative (g67,g70,g74,g77; g88 15...Rxe4??; g89 13.Bg5?? - my plan note only said 'watch' the pawn attack). 3 invalid = forfeit; never resend a rejected move. Reread my last plan note every move.

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my pieces; PATH clear of EVERYTHING; never echo his move; two of my pieces reach one square -> full name (g87 N3xd2); one rejected try -> different move. BISHOPS: trace to the edge (g86). PIN: a piece between his B/R/Q and my K/Q cannot move or recapture (g90 Nxd4 illegal, Bb5 x-ray b5-c6-d7-e8). Queen e2-d4 is no line (g82). After a capture re-read the board.
2. KNIGHT SWEEP FIRST: his knights' 8 squares; if my destination or capture landing square is hit, he recaptures (g87 18.Rxd7??; g85 15.Qxd4??; g82 18.Nxd4??).
3. HIS last move: every attacker of my destination - rook lines, BISHOPS (g82), knights, PAWNS (g89 13.Bg5?? hxg5!). Attacked+undefended -> reject; save my hit piece NOW (g78). His KING hits its 8 neighbours (g77).
4. Pawns: never onto a pawn-attacked square even if defended; blocked pawns still hit both diagonals (g87 19.Bd3?? cxd3); an unmoved or just-advanced pawn still hits its capture squares (g89 h6xg5). Is this pawn a piece's sole guard? After any trade re-list pawn guards (g86).
5. QUEEN: her pawn/knight/bishop lines first; NEVER a queen capture on a defended square (g87 16.Qxd6?? Bxd6). Recapture with the PAWN, never the queen, on a square his knight sweeps (g85). Always list enemy ROOKS' files/ranks to the destination: zero screens = he takes first (g89 16.Qh3?? Rxh3 = Q for R; g79/g81/g83 screens).
6. Trades/sacs: count ALL recapturers + his second attacker after my recapture; write HIS recapture AND MINE; his last -> don't start (g70). Level/down: NO sacs. A rook taking a defended PAWN = R for P (g88 15...Rxe4?? 16.fxe4). My recapturer must still exist and not be pinned (g86; g90).
7. Loose minor/rook (jump, retreat, swing): destination attacked by NOTHING; walk his bishop diagonals to the edge (g86 23...Rb8??; g78 23.Re2??). A check is not safety.
8. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+Ng5 = Qxh7# (g88 20...Qd7??); Q+Bc6 = Qxg2# (g77); Qa1# after my O-O-O.
9. Down material: keep queens (g75); repetition = half point; no N-for-B/R-for-B 'trades'; no claw-back grabs (g87 x3; g88; g89 16.Qh3??). Every capture still passes the scan.
10. Time: routine <=15 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g86 43 s; g87 51 s; g88 38 s; g89-g90 long thinks, all errors).

## Patterns
- Pinned recapturer (g90): Bb5 pinned Nc6 to Ke8; ...Qxd4?? 12.Qxd4 and Nxd4 illegal = Q for P. Check every x-ray before a capture/trade.
- Knight geometry (worst): recaptures on d4/e7/d7/e5 missed (g82,g85,g87); queen cannot defend d4 via e2.
- Queen on an enemy line: g89 Qh3?? Rxh3 (open rook file, 0 screens); g84 Qc2?? ...Nb4; g82 Qe2/d4; g79/g81/g83 screens. Walk enemy rooks, bishops, pawns before any queen move.
- Recapture discipline: list attackers AND defenders from the board; cheapest piece; PAWNS count (g88 fxe4); my recapturer must exist (g86).
- Undefended piece onto a pawn-hit square = pawn wins it (g87 19.Bd3?? cxd3; g89 13.Bg5?? hxg5): never develop to a square a pawn guards, even 'to watch it'.
- Rook/knight/bishop to covered squares or an open bishop diagonal (g68,g70,g73,g78,g80,g86); a rook grabbing a pawn is R for P if a pawn recaptures (g88).
- Self-banned/illegal move sent (g67,g70,g74,g82,g86 x2; g87 Nxd2; g90 Nxd4 pinned): trace the path twice.
