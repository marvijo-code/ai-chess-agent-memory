# Chess memory

Notes (read at start):
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g50
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Dragon/Alapin/Rauzer as Black
- notes/sicilian-soltis-black.md - 9.Bc4 Soltis Dragon as Black
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- My turn; my pieces only; never echo his move. Geometry: moves that way? path clear incl. own blockers? destination empty or enemy-held ('x' only then)?
- After ONE rejected attempt do NOT resend it - play a different, trivially legal move, traced twice (g47 retried Qxb4; g34/g44/g45 lost to 3 invalid replies; g50 Rxc7 illegal -> Nd8 = correct recovery).
- Never send a move my own reasoning just rejected (g48 22.Qxd6??). Re-read the destination right before submitting.

## Rule 1 - pre-move scan (5 s, FINAL position)
1. HIS last move first: what does it attack now? (g46 16...Rad8 hit Qd1; 17.Be3?? lost her.) Then my destination: which enemy PAWN/knight/bishop/rook(rank-file)/queen attacks it? Attacked+undefended -> reject; a move vacates guards (g30).
2. Save my attacked/loose piece NOW, before anything else. A queen attacked by a rook must MOVE - 'defended' still loses Q for R (g42,g46).
3. Queen: never on an open file/rank or a square his rook/pawn/slider/queen covers. Queen-vs-queen: check MY square first - attacked+undefended and he captures first (g50 10...Qc7?? undefended, hit by Qd6: 11.Qxc7 = free queen). A trade needs a legal recapture.
4. Captures/trades: count ALL recapturers - rooks on rank/file, PAWNS, QUEENS (g36,g42,g47). g48 22.Qxd6?? Qxd6 = Q for B; a simply lost pawn/bishop stays lost - no grab-back.
5. Knight: never undefended or pawn/bishop/queen-attacked, esp. down material (g44,g46,g47). Nd2?? Qxd2 (g46,g48).
6. Rook: loose rook facing his rook loses; his rook to an open file/rank at my loose piece = emergency (g42,g46).
7. Pawn pushes/captures: never onto a defended piece or pawn attack, where a queen gains tempo, or while it guards my piece (g48 21.d6?! Bxd6).
8. Attacking his queen excuses nothing: list my loose pieces and my queen's square first (g45,g50).
9. Never remove the sole guard of a pawn/piece to grab a side pawn: g49 16...Nxe4?? (f6-N alone guarded h5) 17.Rxh5! Qxh7#; guard h5/h7 when his Q+rook aim at my king.
10. Lost: defend/trade; no 'active' piece to an undefended square; 5-15 s (g48 40-50 s on a dead game).
11. Time: routine <=15 s, book <=10 s, m1-12 <=20 s. Long thinks never prevented a blunder: g46 0:18, g47 0:36, g48 0:32, g49 7:09; g50 ~11 min at m21, queen fell m10.

## Openings
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5 ...c5 ...Qc7 ...Bb7 ...Rac8; no ...Bg4 after 9.h3. Resolve the centre BEFORE his d5; no knight where his d5-pawn kicks it (g44); Qc7 leaves when the c-file opens (g35,g38,g41).
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; keep e3 empty (g33). If my capture opens a file, fix my rook there FIRST (Rxa8, g43). g46: 14.dxe5 opened the d-file under Qd1; 17.Be3?? lost her to Rxd1 (Qe2!). g48: 21.d6?! just loses a pawn - play Qd2/Rc1.
- Sicilian as Black: Dragon ...d6 ...cxd4 ...Nf6 ...Nc6 ...g6 ...Bg7 ...O-O (g28,g36,g47,g49). Vs 4.c3/5.Qxd4 (g36,g45,g47): after ...Bg4 ...Bxf3 his Qxf3 covers e4 - never ...Nxe4; b7 loose once the b-pawn leaves - defend (Qd7/Rb8) or retreat (Bc8), never a rook swing (13...Ra5?? 14.Qxb7, g45). Vs 4.c3 dxc3 (g50): ...Nc6 ...Bd7 ...Nf6 ...e6 fine; after 9.Bxd6 Bxd6 10.Qxd6 play ...Qb6/...Qc8, never ...Qc7??. Rauzer: 11...gxf6! not Bxf6; Bd7 never d6's only shield; no ...Qxa4/...Qxc4; no ...f5/...f4 while it guards a knight (g30).
- Soltis 9.Bc4 (g49): 11...Ne5 12.h4 Nc4 13.Bxc4 Rxc4 equal; 14.h5 -> 14...Nxh5! (g6 keeps h5; 14...gxh5?! opens the h-file, Nf6 the only guard). After 15.Bh6 do NOT take - keep the g7-bishop or defend. 16...Nxe4?? left h5: 17.Rxh5! Qxh7#.
- 4N as Black (4.Bb5 Bb4): 6.Nd5 Nxd5! 7.exd5 Nd4!; nothing on f5 while his Qf3; no ...Bg4 after h3; play ...Qe7/...Qc8/...Bb5.
- Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; no B-for-P; keep Bc5 defended while Rfc8/Ra8 can come (g42); after O-O-O no queen on a1-net squares (g6); Rxh5 (Qh6 + rook) wins once his f6-knight leaves h5's guard (g49).

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked squares/lines, loose bishops after pawn moves (g45 Bb7), back-rank. g47: took free knights instantly (Qxe4, cxb4) and converted while I flagged. g50: 10...Qc7?? on a square his queen attacked = 11.Qxc7, mate m21.
- Sonnet 5.5: banks clock (1-14 s/move; 17:06 left at mate). Takes EVERY free/attacked unit instantly (g48: Qxd6, Qxd2, Qxe1, Qxf1+, Qxf2). Keep everything defended; move an attacked queen at once; a loose rook facing his rook is lost. As Black vs my Chigorin: ...Bb7 ...Rfe8 ...Nb4 ...a5 ...Na6 ...Nc5.
- GPT-6.1 Sol: fast, banks clock; takes Q-for-R on open files (g46) and free knights (g46/g48 Qxd2); punishes queens on his lines. g49 as White: Soltis 9.Bc4, h4-h5 storm, Qxh6 after the h6 trade, mate with Q+R on the h-file - never leave h5/h7 loose vs him. Match his speed; keep everything defended.
