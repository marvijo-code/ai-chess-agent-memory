# Chess memory

Notes (read at start):
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g49
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Dragon/Alapin/Rauzer as Black
- notes/sicilian-soltis-black.md - 9.Bc4 Soltis Dragon as Black
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- It is my turn; move only my own pieces; never echo his last move. Geometry: does this piece move that way? Path squares empty (own pieces block)? Destination empty or enemy-held ('x' only then)?
- After ONE rejected attempt do NOT resend it - play a different, trivially legal move, traced twice (g47 retried Qxb4 ~2 min; g34/g44/g45 lost to 3 invalid replies).
- g48: never send a move my own reasoning just rejected (note said 'safer is Qd2'; 22.Qxd6?? = Q for B). Re-read the destination right before submitting.

## Rule 1 - pre-move scan (5 s, FINAL position)
1. HIS last move first: what does it attack now? (g46 16...Rad8 hit Qd1; 17.Be3?? lost her.) Then my destination: which enemy PAWN/knight/bishop/rook(rank-file)/queen/king attacks it? Attacked+undefended -> reject; a move vacates guards (g30).
2. Save my attacked/loose piece NOW, before anything else. A queen attacked by a rook must MOVE - 'defended' still loses Q for R (g42,g46).
3. Queen: never on an open file/rank or a square his rook/pawn/slider covers.
4. Captures/trades: count ALL recapturers - rooks on the rank/file, PAWNS, QUEENS (g36,g42,g47). g48 22.Qxd6?? Qxd6 = Q for B; a simply lost pawn/bishop stays lost - no grab-back.
5. Knight: never undefended or pawn/bishop/queen-attacked, esp. down material (g44,g46,g47). Nd2 trap: g46/g48 Nd2?? Qxd2.
6. Rook: loose rook facing his rook loses; his rook to an open file/rank at my loose piece = emergency (g42,g46).
7. Pawn pushes/captures: never onto a defended piece or pawn attack, where a queen gains tempo, or while it guards my piece (g48 21.d6?! Bxd6).
8. Attacking his queen excuses nothing: list my loose pieces first (g45).
9. Never remove the sole guard of a pawn/piece to grab a side pawn: g49 16...Nxe4?? (f6-knight alone guarded h5) 17.Rxh5! Qxh7#. Guard h5/h7 whenever his Q+rook aim at my castled king.
10. Lost: defend/trade; no 'active' piece to an undefended square; 5-15 s (g48 40-50 s on a dead game).
11. Time: routine <=15 s, book <=10 s, m1-12 <=20 s. g46 flagged 0:18 vs 14:21; g47 0:36; g48 mated 0:32 vs 17:06; g49 7:09 vs 15:13. Long thinks never prevented a blunder (g36-g49).

## Openings
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, ...Na5 ...c5 ...Qc7 ...Bb7 ...Rac8. After 9.h3 no ...Bg4. Resolve the centre BEFORE his d5; no knight where his d5-pawn kicks it (g44); Qc7 retreats when the c-file opens (g35,g38,g41).
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; keep e3 empty (g33). If my capture opens a file, fix my rook there FIRST (Rxa8, g43). g46: 14.dxe5 opened the d-file under Qd1 - move the queen off early (15.Qe2); 17.Be3?? lost her to Rxd1. g48: 20.Bxc5 dxc5 fine; 21.d6?! only loses a pawn - play Qd2/Rc1.
- Sicilian as Black: Dragon ...d6 ...cxd4 ...Nf6 ...Nc6 ...g6 ...Bg7 ...O-O (g28,g36,g47,g49). Vs 4.c3/5.Qxd4 (g36,g45,g47): after ...Bg4 ...Bxf3 his Qxf3 covers e4 - never ...Nxe4; b7 loose once the b-pawn leaves - defend (Qd7/Rb8) or retreat (Bc8), never a rook swing (13...Ra5?? 14.Qxb7, g45). Rauzer: 11...gxf6! not Bxf6; never Bd7 as d6's only shield; no ...Qxa4/...Qxc4 on open files; no ...f5/...f4 while it guards a knight (g30).
- Soltis 9.Bc4 (g49): 11...Ne5 12.h4 Nc4 13.Bxc4 Rxc4 equal; 14.h5 -> 14...Nxh5! (g6 then guards h5; 14...gxh5?! opens the h-file and makes Nf6 h5's only guard). After 15.Bh6 do NOT take (15...Bxh6?? 16.Qxh6) - keep the g7-bishop or defend/counter. 16...Nxe4?? left h5: 17.Rxh5! Qxh7#.
- 4N as Black (4.Bb5 Bb4): 6.Nd5 Nxd5! 7.exd5 Nd4!; nothing on f5 while his Qf3; no ...Bg4 after h3; play ...Qe7/...Qc8/...Bb5.
- Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; no B-for-P; keep Bc5 defended while Rfc8/Ra8 can come (g42); after O-O-O no queen on a1-net squares (g6). With his Q on h6 and my rook ready to reach h5, Rxh5 wins only once his f6-knight has left h5's guard (g49).

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked squares/lines, loose bishops after pawn moves (g45 Bb7), back-rank. g47: took free knights instantly (Qxe4, cxb4) and converted while I flagged.
- Sonnet 5.5: banks clock (1-14 s/move; 17:06 left when he mated me). Takes EVERY free/attacked unit instantly (g48: Qxd6, Qxd2, Qxe1, Qxf1+, Qxf2). Keep every piece and pawn defended; move an attacked queen at once; a loose rook facing his rook is lost. As Black vs my Chigorin: 14...Bb7 15...Rfe8 16...Nb4 17...a5 18...Na6 (SF !) 19...Nc5.
- GPT-6.1 Sol: fast, banks clock; takes Q-for-R on open files (g46 17...Rxd1) and free knights (g46/g48 Qxd2); punishes queens on his lines/files. g49 as White: Soltis 9.Bc4, h4-h5 storm, Qxh6 after the h6 trade, mate with Q+R on the h-file - never leave h5/h7 loose vs him. Match his speed; keep everything defended.
