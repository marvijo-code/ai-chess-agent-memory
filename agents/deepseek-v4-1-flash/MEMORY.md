# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan, blunder catalogue g1-g10)
- notes/sicilian-dragon-white.md
- notes/four-knights-black.md
- notes/ruy-lopez-black.md
- notes/ruy-lopez-white.md (games 2, 5, 9, 10)

## Rule 1 - pre-move scan (ALL losses, g1-g10)
Before EVERY move:
1. Destination: list enemy PAWNS and KNIGHTS that attack it. Attacked + undefended -> reject unless a forcing follow-up. Pawn magnets: e5 hits d6/f6; d5 hits c6/e6. Knight magnets: g3 hits f5/h5/e4/e2/f1/h1; c5 hits b3/d3/e4/a4; b4 hits c2/d3/a2; e4 hits d2/f2/c3/g3/c5/f6.
2. Enemy rook/queen on an open file: never put my queen or rook on that file, even if defended - queen-for-rook loses. g10 24.Qc2?? Rxc2 (Rc8 down the open c-file). g9 24.Rc1?? Qxc1+. No quiet "trade" onto a square an extra enemy piece attacks (g8 20...Bf5?? Nxf5).
3. Captures/grabs: list EVERY recapturer/defender, including queen/rook/bishop lines along open files/ranks/diagonals. g9 23.Qxc3?? Qxc3 (Qc7 behind on the open c-file) = queen for knight. Never piece for pawn, never queen for N/B/P or rook; b2/c2 grabs only if no enemy piece attacks and I recapture (g1, g2, g7).
4. Mate net: enemy queen/rook/bishop lines to my king's entry squares. King c1 + Rd1 + Qd2 (d2 self-blocked) = ...Qa1#: free d2 (Qe3/Qd3) or guard a1 (Qc1) NOW, no quiet move (g6 13...Qxa2! 15.e5?? Qa1#). King on g1/h2/g2 with an enemy rook on rank 1: ...Qf2# (g10 m32).
5. After a check/forced sequence: re-scan; the threat may remain (g6 14.Nxe7+ Bxe7).
6. Loose-piece scan: my undefended pieces + enemy queen/bishop/rook/knight lines to them (g8 26...Qd7?? left Nb6 -> Qxb6). Never a queen on a square any enemy knight attacks (g8 28...Qf5?? Nxf5; g5 Qd2?? ...Nb3 fork).
7. My piece en prise and hard to save: make a bigger threat; a queen move that ignores it loses both (g8 Rc7 attacked; 28...Qf5??, 30.Rxc7).
8. Attacking a queen: check she cannot capture my attacker in the same line, else it just loses material (g9 24.Rc1?? Qxc1+, a1-rook blocked by my own Bb1).
9. Legality: clear rank/file/diagonal path; target must be enemy; moving piece must still exist. Never 60-90s on one move (g10 99s + illegal f4 try on 24.Qc2??).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s. g10: 30-51s on moves 14-24, 99s+2 tries on 24.Qc2??, ended 6:37 vs 14:09 while Sol stayed ~14-15 min. g5-g9 same pattern. Long thinks never prevented the blunder; the 5s scan is the fix. Down material or dead-lost: 5-15s, defend, trade, no grabs.

## Openings
- RL as White: 14.d5!/15.Bb1! good. Then Nf1/Ng3/Bg5/Nd2/Nb3, f4; keep c2 covered by Qd1. vs 14...Nb8: 15.Nf1 Nbd7 16.Ng3 Nc5 17.Bg5 h6 18.Bxf6 Bxf6 19.Nd2 Bd7 20.Nb3 fine (~equal). After ...Rac8 + ...Qb6 (f2 pinned) keep the queen OFF the c-file: 24.Qc2?? Rxc2 = Q for R; unpin with Kh2 then f4, Re1-d1, not Rac1. 16.a3 safe only when Qd1 AND Bb1 cover c2 (g2 16.a3?? ...Nxc2). 21.b4? Na4! if a5-pawn supports a4. notes/ruy-lopez-white.md.
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8/...Rfe8. Keep f7 covered. After 14.Nb3, ...Bb7 > ...Be6. ...d5 backed by Bb7 is thematic; after ...d5 exd5 the d5-knight is immune (Qxd5?? Bxd5); never ...Nf6 in front of a White e5 pawn. notes/ruy-lopez-black.md.
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; after O-O-O watch ...Qxa2/...Qa1. notes/sicilian-dragon-white.md.
- Four Knights 4.Bb5 Bb4: 6.Nd5 Nxd5 7.exd5 Ne7, 8.Nxe5 ~+0.5; answers ...Nxd5/d6/c6; never 8...Bxd2??. Nc4 hits b6 -> ...b5. notes/four-knights-black.md.

## Opponents
- GPT-6.1 Sol: solid closed RL as both colors; fast, banks clock (kept ~14-15 min; I was 8 min behind by move 32). Punishes loose pieces, queen/rook placement on lines his pieces cover (g9 23.Qxc3?? Qxc3; g10 24.Qc2?? Rxc2). Never take or place a piece on a square his queen/rook covers along an open line.
- Sonnet 5.5: fast, sound; instantly punishes hanging pieces; rare errors but recovers. Keep every piece defended, no pawn grabs, stay ahead on clock; when he shuffles in a balanced closed position, stay solid and wait.
- Stockfish 19 (ladder): ~0s/move, banks clock; punishes every loose piece and pawn grab with a mate threat.

## Principles
- Material first: no piece for pawn, no queen for N/B/P or for a rook; no capture on a defended square unless equal-or-better; b2/c2 grabs losing by default.
- Every move: pawn attack-squares + knight attack-squares + enemy queen/rook lines to the destination + mate net + loose pieces; re-scan after checks.
- R ending down one pawn holdable: keep the rook, defend pawns, no panic grabs.
- After a blunder: defend loose pieces, trade down, no panic captures, play fast; king safety first (back-rank + queen mates).
