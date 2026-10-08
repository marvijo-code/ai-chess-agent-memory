# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan, blunder catalogue g1-g9)
- notes/sicilian-dragon-white.md
- notes/four-knights-black.md
- notes/ruy-lopez-black.md (Chigorin; g7+g8 vs Sonnet)
- notes/ruy-lopez-white.md (games 2, 5, T2 vs Sol)

## Rule 1 - pre-move scan (ALL losses, g1-g9)
Before EVERY move:
1. Destination: list enemy PAWNS and pieces (KNIGHTS too) that attack it. Attacked + undefended -> reject unless a forcing follow-up. Pawn magnets: e5 hits d6/f6; d5 hits c6/e6. Knight magnets: g3 hits f5/h5/e4/e2/f1/h1; c5 hits b3/d3/e4/a4; b4 hits c2/d3/a2. White pawn on e5 -> knight to f6/d6 is a free capture (g7 24...Nf6?? 25.exf6).
2. Trade offers: before ...Bf5/...Bd7 "I trade" moves, check the square is not attacked by an extra enemy piece and that something defends it (g8 20...Bf5?? Nxf5; 28...Qf5?? Nxf5).
3. Captures/grabs: list EVERY recapturer/defender, including enemy QUEEN/ROOK/BISHOP lines along open files/ranks/diagonals. g9 23.Qxc3?? lost the queen: Qc7 defended the c3-knight down the open c-file (pawns gone after ...cxd4). Piece-for-pawn = -2; never queen for N/B/P. b2/c2 grabs only if no enemy piece attacks the square and I can recapture (g1 ...Nxb2??, g2 ...Nxc2, g7 35...Rxb2??).
4. Mate net: enemy queen/rook/bishop lines to my king's entry squares. King c1 + Rd1 + Qd2 (d2 self-blocked) = ...Qa1#. Enemy queen on a1/a2/b2 -> free d2 (Qe3/Qd3) or guard a1 (Qc1) NOW, no quiet move (g6 13...Qxa2! 15.e5?? Qa1#).
5. After a check/forced sequence: re-scan; the threat may remain (g6 14.Nxe7+ Bxe7).
6. Loose-piece scan: my undefended pieces + enemy queen/bishop/rook/knight lines to them (g8 26...Qd7?? left Nb6; 27.Qxb6). Never a queen on a square any enemy knight attacks (g8 28...Qf5?? Nxf5; g5 Qd2?? ...Nb3 fork).
7. My piece en prise and hard to save: make a bigger threat; a queen move that ignores it loses both (g8 Rc7 attacked; 28...Qf5??, 30.Rxc7).
8. Attacking a queen: check she cannot capture my attacker in the same line, else it just loses material (g9 24.Rc1?? Qxc1+, a1-rook blocked by my own Bb1).
9. Legality: clear rank/file/diagonal path; target must be enemy; the moving piece must still be on the board (g9 tried Rc1 after it fell). Verify geometry; never 60-90s on one move.

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s. Persistent: g7/g8 36-50s on routine shuffles; g9 38-50s on moves 14-23, ended 10:48 vs 11:48. The 5s scan is the fix, not the clock. Dead-lost: 5s moves.

## Openings
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; after O-O-O watch ...Qxa2/...Qa1. notes/sicilian-dragon-white.md.
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8/...Rfe8. Keep f7 covered. After 14.Nb3, ...Bb7 > ...Be6. ...d5 backed by Bb7 is thematic; after ...d5 exd5 the d5-knight is immune (Qxd5?? Bxd5); never ...Nf6 in front of a White e5 pawn. notes/ruy-lopez-black.md.
- RL as White: 14.d5! (engine ! in two games), ...Nb4 15.Bb1! (engine !), then a3/Nf1/Ng3/Bg5/Qd2/Rd1/Qe2, f4. 16.a3 safe only when Qd1 AND Bb1 cover c2; else 16.Rac1/Bb1 (g2 16.a3?? ...Nxc2). Don't kick the c5-knight with b4 if it can go a4 (a5-pawn supports) then c3 with Qc7 behind (g9 21.b4? Na4!). notes/ruy-lopez-white.md.
- Four Knights 4.Bb5 Bb4: 6.Nd5 Nxd5 7.exd5 Ne7, 8.Nxe5 ~+0.5; answers ...Nxd5/d6/c6; never 8...Bxd2??. Nc4 hits b6 -> ...b5. notes/four-knights-black.md.

## Opponents
- GPT-6.1 Sol: solid closed RL as both colors; punishes loose pieces, queen placement and captures of defended pieces (g9 23.Qxc3?? Qxc3; 24...Qxc1+). Never take on a square his queen/rook already covers along an open line.
- Sonnet 5.5: fast, sound; instantly punishes hanging pieces; rare errors but recovers. Keep every piece defended, no pawn grabs, stay ahead on clock; when he shuffles in a balanced closed position, stay solid and wait.
- Stockfish 19 (ladder): ~0s/move, banks clock; punishes every loose piece and pawn grab with a mate threat.

## Principles
- Material first: no piece for pawn, no queen for N/B/P, no capture on a defended square unless equal-or-better; b2/c2 grabs losing by default.
- Every move: pawn attack-squares + knight attack-squares + enemy queen/rook lines to the destination + mate net + loose pieces; re-scan after checks.
- R ending down one pawn holdable: keep the rook, defend pawns, no panic grabs.
- After a blunder: defend loose pieces, trade down, no panic captures, play fast (clock is the only asset).
