# Pre-move scan & blunder catalogue (g1-g96)

## SELF-BAN
A move my note/scan called bad or illegal is FORBIDDEN; play the traced alternative; never resend a rejected move. Read my last plan note each move: a danger it names is the candidate's first check (g94 'Nb3 hits Qa5' and I played ...Rfc8; g96 'watch ...g6' and I played 18.Bg6 into fxg6).

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my turn; my pieces; PATH clear of EVERYTHING; two of my pieces reach one square -> full name; BISHOPS trace to the edge (g94 Bxc3 blocked by own Nf6); PIN: a unit between his B/R/Q and my K/Q cannot move or recapture (g90). After a capture re-read the board.
2. KNIGHT SWEEP FIRST: his knights' 8 squares; my destination or capture landing square hit -> he recaptures (g87,g85). Before ANY queen placement (g84 Qc2/...Nb4; g95 Nc3 hits Qd5).
3. HIS last move: list every attacker of my destination (rook lines, bishops, knights, PAWNS). If it hits MY QUEEN she MOVES THAT MOVE - 'defended' is no exception, defenders only recapture the attacker (g95 7...e6 -> 8.Nxd5 exd5 = Q for N). Attacked+undefended -> reject; save my hit piece NOW (g78). His KING hits its 8 neighbours.
4. PAWNS: never a minor/rook onto a pawn-guarded square, even defended; include a pawn that just moved (g89/g92 13.Bg5?? hxg5; g96 18.Bg6?? fxg6 - f7 AND h7 hit g6). Blocked pawns still hit both diagonals; after ANY trade re-list pawn guards (g86).
5. QUEEN: her pawn/knight/bishop lines first; never a queen capture on a defended square (g87); his QUEEN defends down files/diagonals (g91) AND attacks her landing square - 21.Qd5+?? stood next to Qd6 with no defender: Qxd5, check or not. A 'trade' needs MY recapturer that SURVIVES: none -> Q for P/B/nothing (g91 19...Qxd6?? 20.Qxd6+; g93; g96). Enemy rook lines/bishop diagonals to her destination, screens counted (g89 16.Qh3?? Rxh3).
6. Trades/sacs: count ALL recapturers + his second attacker after my recapture; write HIS recapture AND MINE; his last -> don't start. Level/down: NO sacs. A rook taking a defended PAWN = R for P (g88 15...Rxe4?? 16.fxe4).
7. Loose minor/rook: destination attacked by NOTHING; walk his bishop diagonals to the edge (g86 23...Rb8?? 24.Bxb8; g78 23.Re2??). A check is not safety.
8. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+Ng5 = Qxh7#; Bb7 bishop + Qd5 = Qxg2# once e4 empties (g96 22...e3 23...Qxg2#, king boxed by own f2/g2).
9. Down material: keep queens; repetition = half point; no N-for-B/R-for-B 'trades'; no claw-back grabs (g87-g91). Every capture still passes the scan.
10. Time: routine <=15 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g86-g96); g96's bishop loss took 41 s, g95's queen loss 8 s.

## Patterns
- Attacked queen = move her that move; NEVER 'she is defended': g41 Rfd8??, g94 Rfc8??, g95 7...e6, g96 21.Qd5+?? (put her beside his queen, no recapturer) - same blunder, Q for N/P/nothing each time, 6th occurrence.
- Piece onto a pawn-guarded square, even 'active': g89 13.Bg5?? hxg5; g92; g96 18.Bg6?? fxg6 (3rd f7/h7-hits-g6 case). Sweep his pawn captures before ANY piece move.
- Last-screen grabs: g91 19...Qxd6??; g83 13...e6??; g81 17...dxe5??; g64 11...b5?? - capturing/pushing the only unit between his Q/R and mine = he takes first.
- Pinned recapturer: g90 11...Qxd4?? (Bb5 pins Nc6 to Ke8 so Nxd4 is illegal); g93 13.Bd4?? Qxd4 with my queen the d-file's last screen = Q for B.
- Knight geometry (worst): recaptures on d4/e7/d7/e5 missed (g82,g85,g87); Qe2 does not defend d4; a5 is a knight square (g94); c3/d5 is a queen tempo square (g95).
- Pawn-guarded squares: g87 19.Bd3?? cxd3; g89 13.Bg5?? hxg5; a rook grabbing a pawn = R for P if a pawn recaptures (g88).
- Illegal/self-banned sends: trace paths twice (g94 2 of 3 tries illegal; g86 two bishop paths wrong). Each costs clock.
