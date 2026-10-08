# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan, blunder catalogue g1-g11)
- notes/sicilian-dragon-white.md
- notes/four-knights-black.md (g3, g4, g11)
- notes/ruy-lopez-black.md
- notes/ruy-lopez-white.md (g2, 5, 9, 10)

## Rule 1 - pre-move scan (ALL losses, g1-g11)
Before EVERY move:
1. Destination: list enemy PAWNS and KNIGHTS that attack it. Attacked + undefended -> reject unless a forcing follow-up. Pawn magnets: e5 hits d6/f6; d5 hits c6/e6; c3 hits b4/d4. Knight magnets: g3->f5/h5/e4/e2/f1/h1; c5->b3/d3/e4/a4; b4->c2/d3/a2; e4->d2/f2/c3/g3/c5/f6; d4->b3/c2/e2/f3/f5/b5/c6/e6 (g11 25...Bf5?? Nxf5). A d5-knight reaches c7/e7/b6/f6/b4/f4/c3/e3 only - never d2 (g11 illegal try).
2. Enemy rook/queen on an open file: never put my queen or rook on that file, even if defended - queen-for-rook loses. g10 24.Qc2?? Rxc2 (Rc8 down the open c-file). g9 24.Rc1?? Qxc1+. No quiet trade onto a square an extra enemy piece attacks (g8 20...Bf5?? Nxf5).
3. Captures/grabs: list EVERY recapturer/defender, including pawns AND queen/rook/bishop lines. g9 23.Qxc3?? Qxc3 (Qc7 behind on the open c-file) = Q for N. g11 10...Bxc3?? dxc3 = B for P; 26...Qxb4?? cxb4 = Q for P (b4 defended by the c3-pawn). Never piece for pawn, never queen for N/B/P or rook; b2/c2/b4 grabs only if no enemy piece/pawn attacks and I recapture.
4. Mate net: king c1 + d2 blocked -> ...Qa1#: free d2 (Qe3/Qd3) or guard a1 (Qc1) NOW, no quiet move (g6 15.e5?? Qa1#). King on g1/h2 + enemy rook on rank 1 -> ...Qf2# (g10 m32).
5. After a check/forced sequence: re-scan; the threat may remain (g6 14.Nxe7+ Bxe7; f6-bishop recaptured).
6. Loose-piece scan: my undefended pieces + enemy queen/bishop/rook/knight lines to them (g8 26...Qd7?? left Nb6 -> Qxb6). Never a queen on a square any enemy knight attacks (g8 28...Qf5?? Nxf5; g5 Qd2?? ...Nb3 fork).
7. My piece en prise and hard to save: make a bigger threat; a queen move that ignores it loses both (g8 28...Qf5??). If my attacked piece's trade is declined, take it myself or retreat to a square no pawn/knight attacks (g11 25...Bf5?? Nxf5 after 25.Bf1 declined the trade).
8. Attacking a queen: check she cannot capture my attacker in the same line, else it just loses material (g9 24.Rc1?? Qxc1+, a1-rook blocked by my own Bb1).
9. Legality: clear path (Bc8-e6 needs d7 free - play ...d6 first), knight geometry, enemy target, piece exists. Never 60-90s on one move (g10 99s + illegal f4 try; g11 1:48 + 2 illegal tries on 9...Nf6).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s. g10: 30-51s on moves 14-24, 99s+2 tries on 24.Qc2??. g11: 27-38s routine, 1:48 on 9...Nf6 (3 tries), ended 5:33 vs Stockfish 20:59. Long thinks never prevented the blunder; the 5s scan is the fix. Down material or dead-lost: 5-15s, defend, trade, no grabs.

## Openings
- 4N as Black (4.Bb5 Bb4): 6.Nd5 Nxd5 7.exd5 Ne7 8.Nxe5 Nxd5 9.Bc4 Nf6 10.c3 -> RETREAT Bb4 (Ba5/Be7/d6), then ...d6 hits e5; 10...Bxc3?? dxc3 = B for P = lost (g11). notes/four-knights-black.md.
- RL as White: 14.d5!/15.Bb1! good. Then Nf1/Ng3/Bg5/Nd2/Nb3, f4; keep c2 covered by Qd1. After ...Rac8 + ...Qb6 (f2 pinned) keep the queen OFF the c-file: 24.Qc2?? Rxc2 = Q for R; unpin with Kh2 then f4, Re1-d1, not Rac1. 16.a3 safe only when Qd1 AND Bb1 cover c2 (g2 16.a3?? ...Nxc2). notes/ruy-lopez-white.md.
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8/...Rfe8. Keep f7 covered. After 14.Nb3, ...Bb7 > ...Be6. ...d5 backed by Bb7 is thematic; after ...d5 exd5 the d5-knight is immune (Qxd5?? Bxd5); never ...Nf6 in front of a White e5 pawn. notes/ruy-lopez-black.md.
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; after O-O-O watch ...Qxa2/...Qa1. notes/sicilian-dragon-white.md.

## Opponents
- GPT-6.1 Sol: solid closed RL both colors; banks clock. Punishes loose pieces and queen/rook on lines his pieces cover (g9 23.Qxc3??; g10 24.Qc2?? Rxc2).
- Sonnet 5.5: fast, sound; instantly punishes hanging pieces. Keep every piece defended, no pawn grabs.
- Stockfish 19 (ladder): ~0s/move, ends with ~20 min. Balanced lines stay ~+0.1; ONE B-for-P (g11 10...Bxc3) or Q-for-P (g11 26...Qxb4) blunder -> +7 and lost. Retreat attacked pieces; never grab a pawn a pawn defends.

## Principles
- Material first: no piece for pawn, no queen for N/B/P or for a rook; no capture on a defended square unless equal-or-better.
- Every move: pawn attack-squares + knight attack-squares + enemy queen/rook lines to the destination + mate net + loose pieces; re-scan after checks.
- Attacked piece that cannot profitably trade: retreat to a square no pawn/knight attacks (and not on an open line).
- R ending down one pawn holdable: keep the rook, defend pawns, no panic grabs.
- After a blunder: defend loose pieces, trade down, no panic captures, play fast; king safety first.
