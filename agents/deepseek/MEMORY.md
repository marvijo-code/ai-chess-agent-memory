# Chess memory

Notes (read at start):
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g46
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Dragon/Rauzer as Black
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- It is my turn: move only my own pieces; never echo his last move. g45 tried 'Qxb7' though my Qd8 has no line to b7.
- Geometry: does this piece move that way? Every path square empty (own pieces block)? Destination empty, or enemy-held ('x' only then)?
- After one rejected attempt do NOT resend it: play a different, trivially legal move and trace it twice.
- g34/g44/g45: games lost to 3 invalid replies. This check comes first.

## Rule 1 - pre-move scan (5 s, FINAL position)
1. HIS last move first: what does the moved piece attack now? g46 16...Rad8 hit my Qd1 - I answered 17.Be3?? and lost the queen. Then my destination: which enemy PAWN, knight, bishop, rook (rank/file), queen, king attacks it? Attacked+undefended -> reject. Moving vacates guards (g30).
2. My attacked/loose piece: save it NOW, before any other move. A queen attacked by a rook must MOVE - a recapture is Q for R (g46,g42). g45: 13.Qxb5 attacked Bb7, 13...Ra5?? ignored it, 14.Qxb7 fell.
3. Queen: never on an open file/rank or a square his rook/pawn/slider covers; never rely on being 'defended' vs a rook.
4. Every queen capture/trade: count ALL recapturers incl. rooks on the destination rank/file and PAWNS (g36,g42).
5. Knight: never undefended or on a pawn/bishop-attacked square, esp. down material (g44; g46 29.Nd2?? Qxd2 won the last knight).
6. Rook: loose rook facing his rook loses; his rook to an open file/rank at my loose piece = emergency.
7. Pawn pushes/captures: never onto a defended piece, a pawn's attack, where a queen gains tempo, or while it guards my piece; never down material.
8. Attacking his queen excuses nothing: first list my loose pieces (g45).
9. Lost: defend/trade; no 'active' piece to an undefended square; 5-15 s.
10. Time: routine <=15 s; from m10 no move >25 s. g46: 20-55 s/move from move 1, flagged with 0:18 vs his 14:21. Long thinks never prevented one blunder (g36,g42,g43,g44,g45,g46).

## Openings
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, ...Na5 ...c5 ...Qc7 ...Bb7 ...Rac8. After 9.h3 no ...Bg4. Resolve the centre BEFORE his d5; no knight where his d5-pawn kicks it (g44 15...Nc6?); Qc7 on the c-file retreats when the file opens (g35,g38,g41).
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; keep e3 empty (g33). If my capture opens a file, fix my rook there FIRST (trade Rxa8, g43). g46: 14.dxe5 dxe5 opened the d-file with my Qd1; move the queen off early (15.Qe2) - after 16...Rad8, 17.Be3?? lost her to 17...Rxd1.
- Sicilian as Black: Dragon ...d6 ...cxd4 ...Nf6 ...Nc6 ...g6 ...Bg7 ...O-O (g28,g36). Vs 4.c3/5.Qxd4 with c4: after ...a6 ...b5 ...Bb7, b7 must stay defended; if cxb5 axb5 Qxb5, play ...Qd7 (defends b7) or ...Rb8/...Bc8 - never a rook swing like 13...Ra5?? (g45 14.Qxb7). Rauzer: 11...gxf6! not Bxf6; never Bd7 as d6's only shield; no ...Qxa4/...Qxc4 on open files; no ...f5/...f4 while it guards a knight (g30).
- 4N as Black (4.Bb5 Bb4): 6.Nd5 Nxd5! 7.exd5 Nd4!; nothing on f5 while his Qf3; no ...Bg4 after h3; play ...Qe7/...Qc8/...Bb5.
- Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; no B-for-P; keep Bc5 defended while Rfc8/Ra8 can come (g42); after O-O-O no queen on a1-net squares (g6).

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked squares/lines, loose bishops after pawn moves (g45 Bb7), back-rank.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit instantly. Keep every piece and pawn defended; move an attacked queen at once; a loose rook facing his rook on an open file is lost.
- GPT-6.1 Sol: fast (3-35 s/move), banks clock, closed RL, solid; instantly takes queen-for-rook when our units face on an open file (g46 17...Rxd1) and undefended knights (g46 29...Qxd2); punishes queens on his lines/files. Captures must survive recapture; match his speed, keep everything defended.
