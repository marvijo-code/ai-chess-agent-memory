# Chess memory

Notes (read at start):
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g48
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Dragon/Alapin/Rauzer as Black
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- It is my turn: move only my own pieces; never echo his last move. Geometry: does this piece move that way? Every path square empty (own pieces block)? Destination empty, or enemy-held ('x' only then)?
- After ONE rejected attempt do NOT resend it - it will be rejected again. Play a different, trivially legal move, traced twice (g47 wasted ~2 min retrying Qxb4).
- g34/g44/g45: games lost to 3 invalid replies. This check comes first.
- g48: never send a move my own reasoning just rejected - my note read 'safer is Qd2' and 22.Qxd6?? went out anyway (Q for B). Re-read the destination square right before submitting.

## Rule 1 - pre-move scan (5 s, FINAL position)
1. HIS last move first: what does the moved piece attack now? g46 16...Rad8 hit my Qd1 - I answered 17.Be3?? and lost the queen. Then my destination: which enemy PAWN, knight, bishop, rook (rank/file), queen, king attacks it? Attacked+undefended -> reject. Moving vacates guards (g30).
2. My attacked/loose piece: save it NOW, before any other move. A queen attacked by a rook must MOVE - a recapture is Q for R (g42,g46).
3. Queen: never on an open file/rank or a square his rook/pawn/slider covers; never rely on being 'defended' vs a rook.
4. Every capture/trade: count ALL recapturers incl. rooks on the destination rank/file, PAWNS and QUEENS (g36,g42,g47). g48 22.Qxd6?? Qxd6 = Q for B; a pawn/bishop that is simply lost stays lost - accept it, don't grab back.
5. Knight: never undefended or on a pawn/bishop/queen-attacked square, esp. down material (g44,g46,g47). Nd2 trap: g46 29.Nd2?? Qxd2, g48 23.Nd2?? Qxd2 - never Nd2 while his queen can reach d2.
6. Rook: loose rook facing his rook loses; his rook to an open file/rank at my loose piece = emergency (g42,g46).
7. Pawn pushes/captures: never onto a defended piece, a pawn's attack, where a queen gains tempo, or while it guards my piece; never down material. g48 21.d6?! Bxd6 lost a pawn for nothing.
8. Attacking his queen excuses nothing: first list my loose pieces (g45).
9. Lost: defend/trade; no 'active' piece to an undefended square; 5-15 s (g48 spent 40-50 s/move on a dead game).
10. Time: routine <=15 s; book moves <=10 s; m1-12 hard cap 20 s/move. g46 flagged 0:18 vs 14:21; g47 flagged 0:36; g48: 62 s m1, many 45-67 s moves m4-21, mated with 0:32 vs 17:06. Long thinks never prevented one blunder.

## Openings
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, ...Na5 ...c5 ...Qc7 ...Bb7 ...Rac8. After 9.h3 no ...Bg4. Resolve the centre BEFORE his d5; no knight where his d5-pawn kicks it (g44); Qc7 retreats when the c-file opens (g35,g38,g41).
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; keep e3 empty (g33). If my capture opens a file, fix my rook there FIRST (trade Rxa8, g43). g46: 14.dxe5 opened the d-file with my Qd1 - move the queen off early (15.Qe2); after 16...Rad8, 17.Be3?? lost her to Rxd1. g48: 14.Nf1 Bb7 15.Ng3 Rfe8 16.d5 Nb4 17.Bb1 a5 18.a3 Na6 19.Be3 Nc5 20.Bxc5 dxc5 was fine; 21.d6?! only loses a pawn (Bxd6, guarded by Qc7) - play Qd2/Rc1.
- Sicilian as Black: Dragon ...d6 ...cxd4 ...Nf6 ...Nc6 ...g6 ...Bg7 ...O-O (g28,g36,g47). Vs 4.c3/5.Qxd4 (g36,g45,g47): after ...Bg4 ...Bxf3 his Qxf3 covers e4 - never ...Nxe4; b7 is loose once the b-pawn leaves - defend (Qd7/Rb8) or retreat (Bc8), never a rook swing (g45 13...Ra5?? 14.Qxb7). Rauzer: 11...gxf6! not Bxf6; never Bd7 as d6's only shield; no ...Qxa4/...Qxc4 on open files; no ...f5/...f4 while it guards a knight (g30).
- 4N as Black (4.Bb5 Bb4): 6.Nd5 Nxd5! 7.exd5 Nd4!; nothing on f5 while his Qf3; no ...Bg4 after h3; play ...Qe7/...Qc8/...Bb5.
- Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; no B-for-P; keep Bc5 defended while Rfc8/Ra8 can come (g42); after O-O-O no queen on a1-net squares (g6).

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked squares/lines, loose bishops after pawn moves (g45 Bb7), back-rank. g47: took free knights instantly (Qxe4, cxb4) and converted while I flagged.
- Sonnet 5.5: banks clock (1-14 s/move; 17:06 left when he mated me). Takes EVERY free/attacked unit instantly (g48: Qxd6, Qxd2, Qxe1, Qxf1+, Qxf2). Keep every piece and pawn defended; move an attacked queen at once; a loose rook facing his rook is lost. As Black vs my Chigorin: 14...Bb7 15...Rfe8 16...Nb4 17...a5 18...Na6 (SF !) 19...Nc5, then mops up with the queen once ahead.
- GPT-6.1 Sol: fast (3-35 s/move), banks clock, closed RL, solid; instantly takes queen-for-rook on open files (g46 17...Rxd1) and undefended knights (g46 29...Qxd2); punishes queens on his lines/files. Captures must survive recapture; match his speed, keep everything defended.
