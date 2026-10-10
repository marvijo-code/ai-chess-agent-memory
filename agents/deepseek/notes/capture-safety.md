# Pre-move scan & blunder catalogue (g1-g100)

## SELF-BAN
A move my scan called bad/illegal is FORBIDDEN; play the traced alternative; never resend it. Reread my last plan note each move: a danger it names is the candidate's first check (g94 'Nb3 hits Qa5' -> ...Rfc8??; g96 'watch g6' -> Bg6??; g98 'watch Qxb2' -> O-O??; g100 'bishop attacks my queen' -> Qc6?? along the same diagonal).

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my turn; my pieces; PATH clear (g99 Rb2+ blocked by his b3-pawn); two units to one square -> full name; BISHOPS trace to the edge (g94); O-O needs f1/g1 empty (g98); PIN: a unit between his B/R/Q and my K/Q cannot move or recapture (g90). Re-read the board after every capture.
2. KNIGHT SWEEP FIRST: his knights' 8 squares hit my destination -> he recaptures (g85,g87); before ANY queen placement (g84,g95); a 'fork' onto a defended square = gift (g98 20.Nd7?? Bxd7).
3. HIS last move: list every attacker of my destination (rook, bishop, knight, PAWN). Attacked QUEEN moves THAT move - 'defended' never counts, defenders only recapture the attacker (g95 7...e6 8.Nxd5 = Q for N). Attacked+undefended -> save NOW (g78). His KING hits its 8 neighbours.
4. PAWNS: never a minor/rook onto a pawn-guarded square, even defended, even a just-moved/blocked pawn (g89/g92 13.Bg5?? hxg5; g96 18.Bg6?? fxg6). Re-list pawn guards after ANY trade (g86). g99: 21...Bf6?? exf6, 24...Rxb3+?? axb3, 25...Nd5?? cxd5.
5. QUEEN: no capture on a defended square (g87); no trade without MY recapturer that SURVIVES (g91,g96 - none = Q for P/minor/nothing); his queen/rook lines AND her landing square (g89, g96 21.Qd5+?? Qxd5); hit by a BISHOP: retreat OFF that whole diagonal, never along it (g100 b5-c6-d7-e8, Qc6?? Bxc6+ = Q for B).
6. CAPTURES: name every recapturer + his second attacker; write MY recapture; his last -> don't start. Level/down: NO sacs. RECAPTURE X-RAY: before any recapture (esp. queen's) walk his rook files + bishop diagonals onto that square (g97 13...Qxe7?? 14.Rxe7 = Q for N).
7. Loose minor/rook: destination attacked by NOTHING; walk his bishop diagonals to the edge (g86,g78). A check is not safety.
8. Mate nets BEFORE any move: Qh2/Rh1 h-file; Qh6+Ng5 = Qxh7#; Bb7+Qd5 = Qxg2# once e4 clears (g96); King on h2-h4: Rg2/Rg6+Bf1+Nf2 (g98 32...Rg4#).
9. Down material: keep queens; repetition = half point; no N-for-B/R-for-B trades; no claw-back grabs (g87-g91,g98). Hold, trade pawns, make him prove it.
10. Time: routine <=15 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g86-g100; g100 26-39 s routine moves lost the queen).

## Patterns
- Attacked queen = move her that move; NEVER 'she is defended' (g41, g94 Rfc8??, g95 7...e6, g96 21.Qd5+??, g100 Qc6??).
- Queen hit by a line: leave the ENTIRE line, not just the square (g100).
- Pawn-guarded square: g89 13.Bg5?? hxg5; g96 18.Bg6?? fxg6.
- Last-screen grabs: g91 19...Qxd6??; g83 13...e6??; g81 17...dxe5??.
- Pinned recapturer: g90 11...Qxd4??; g93 13.Bd4?? Qxd4.
- Queen with tempo: g41 16.Bd2 hit Qa5; g98 13...Qb4 pinned Nd2 AND hit b2.
- Knight geometry: recaptures on d4/e7/d7/e5 missed (g82,g85,g87,g98).
- Illegal sends: trace paths twice (g94, g98); each costs clock.

## g100 Caro Advance/Tal vs SF (0-1, Qxd8# m18)
3.e5 Bf5 4.h4 h6 5.Nc3 e6 6.g4 Bg6 7.h5 Bh7 8.f4 c5 9.Nf3 cxd4 10.Nxd4 Nc6 11.Be3 Nxd4 12.Qxd4 Be7? -> 13.Qa4+ (+4; b5/c6/d7/e8 ALL empty - block with ...Nd7/...Bd7) Qd7?! 14.Bb5! Qc6?? 15.Bxc6+ bxc6 16.Qxc6+ Kf8 17.Qxa8+ Bd8 18.Qxd8#.
- Root: 12...Be7 left the a4-e8 diagonal open while my c-pawn was gone; my own move note said 'bishop attacks my queen' and I still slid along the same diagonal. Block checks with a PIECE; keep the queen off long diagonals that his bishop or queen can enter.
