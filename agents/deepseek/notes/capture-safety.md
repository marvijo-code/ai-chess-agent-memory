# Pre-move scan & blunder catalogue (g1-g98)

## SELF-BAN
A move my scan called bad/illegal is FORBIDDEN; play the traced alternative; never resend it. Reread my last plan note each move: a danger it names is the candidate's first check (g94 'Nb3 hits Qa5' -> ...Rfc8??; g96 'watch g6' -> Bg6??; g98 'watch Qxb2' -> O-O??).

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my turn; my pieces; PATH clear; two units to one square -> full name; BISHOPS trace to the edge (g94 Bxc3 blocked by own Nf6); O-O needs f1/g1 empty (g98 try illegal); PIN: a unit between his B/R/Q and my K/Q cannot move or recapture (g90). Re-read the board after a capture.
2. KNIGHT SWEEP FIRST: his knights' 8 squares; my destination/capture landing square hit -> he recaptures (g85,g87). Before ANY queen placement (g84 ...Nb4; g95). A 'fork' onto a defended square is a gift: g98 20.Nd7?? Bxd7.
3. HIS last move: list every attacker of my destination (rook lines, bishops, knights, PAWNS). If it hits MY QUEEN she MOVES THAT MOVE - 'defended' is no exception (g95 7...e6 -> 8.Nxd5 exd5 = Q for N). Attacked+undefended -> reject; save my hit piece NOW (g78). His KING hits its 8 neighbours.
4. PAWNS: never a minor/rook onto a pawn-guarded square, even defended; include a pawn that just moved or is blocked (g89/g92 13.Bg5?? hxg5; g96 18.Bg6?? fxg6). Re-list pawn guards after ANY trade (g86).
5. QUEEN: her pawn/knight/bishop lines first; no queen capture on a defended square (g87); his QUEEN defends down files/diagonals AND attacks her landing square (g96 21.Qd5+?? Qxd5, check or not). A 'trade' needs MY recapturer that SURVIVES; none -> Q for P/B/nothing (g91 19...Qxd6??; g93). Enemy rook lines/bishop diagonals to her destination, screens counted (g89 Qh3?? Rxh3).
6. Trades: count ALL recapturers + his second attacker after my recapture; write HIS recapture AND MINE; his last -> don't start. Level/down: NO sacs. A rook taking a defended PAWN = R for P (g88 15...Rxe4??).
7. Loose minor/rook: destination attacked by NOTHING; walk his bishop diagonals to the edge (g86 23...Rb8??; g78 23.Re2??). A check is not safety.
8. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's guard); Qh6+Ng5 = Qxh7#; Bb7+Qd5 = Qxg2# once e4 clears (g96). King on h2-h4 + his Rg2/Rg6: count Bf1+Nf2 nets - g98 32...Rg4# (my h5/f4 pawns boxed the king; Kg1 illegal, open g-file).
9. Down material: keep queens; repetition = half point; no N-for-B/R-for-B 'trades'; no claw-back grabs (g87-g91). g98: 2P down, 20.Nd7?? dropped a knight - hold, trade pawns, defend.
10. Time: routine <=15 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g86-g98; g98 30-59 s moves still blundered + 2 illegal tries).

## Patterns
- Attacked queen = move her that move; NEVER 'she is defended': g41 Rfd8??, g94 Rfc8??, g95 7...e6, g96 21.Qd5+?? - Q for N/P/nothing each time.
- Piece onto a pawn-guarded square: g89 13.Bg5?? hxg5; g96 18.Bg6?? fxg6.
- Last-screen grabs: g91 19...Qxd6??; g83 13...e6??; g81 17...dxe5?? - taking/pushing the only unit between his Q/R and mine = he takes first.
- Pinned recapturer: g90 11...Qxd4?? (Bb5 pins Nc6); g93 13.Bd4?? Qxd4 (my queen was the d-file's last screen).
- Queen entry with tempo: g41 16.Bd2 hit Qa5; g98 13...Qb4 pinned Nd2 AND hit undefended b2 -> Qxb2/Qxa2 = 2 pawns.
- Knight geometry (worst): recaptures on d4/e7/d7/e5 missed (g82,g85,g87,g98); Qe2 does not defend d4; d7 is a bishop-defended square.
- Illegal sends: trace paths twice (g94 2 of 3; g98 2 tries). Each costs clock.
