# Chess memory

Notes (read at start):
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g45
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Dragon/Rauzer as Black
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- It is my turn: move only BLACK pieces; never echo his last move. g45 tried 'Qxb7' though my Qd8 has no line to b7 (his queen stood there).
- Geometry: does this piece move that way? Is every path square empty (own pieces block)? Destination empty, or enemy-held ('x' only then)?
- After one rejected attempt do NOT resend it: play a different, trivially legal move and trace it twice.
- g34/g44/g45: games lost to 3 invalid replies. This check comes first.

## Rule 1 - pre-move scan (5 s, FINAL position)
1. Destination: which enemy PAWN, knight, bishop, rook (rank/file), queen, king attacks it? Attacked+undefended -> reject. Moving a piece vacates squares it guarded (g30).
2. My attacked or loose piece: save/trade/defend NOW, before any other move. g45: 13.Qxb5 attacked Bb7; 13...Ra5?? hit her queen but b7 fell to 14.Qxb7. Defend b7 (...Qd7/...Rb8) or retreat ...Bc8 first.
3. Queen: never on a square his pawn/slider/rook attacks. Every queen capture/trade: count ALL recapturers incl. rooks on the destination rank/file and PAWNS.
4. Knight: never undefended or on a pawn/bishop-attacked square, esp. down material.
5. Rook: undefended rook facing his rook loses; his rook to an open file at my loose piece = emergency.
6. Pawn pushes/captures: never onto a defended piece, a pawn's attack, where a queen gains tempo, or while it guards my piece; never down material.
7. Attacking his queen excuses nothing: first list my loose pieces (g45).
8. Lost: defend/trade; no 'active' piece to an undefended square; 5-15 s.
9. Time: routine <=15 s; from m10 no move >25 s. Long thinks never fixed anything; flag/forfeit risk is real (g36,g42,g43,g44,g45).

## Openings
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, ...Na5 ...c5 ...Qc7 ...Bb7 ...Rac8. After 9.h3 no ...Bg4. Resolve the centre BEFORE his d5; no knight where his d5-pawn kicks it (g44 15...Nc6?); Qc7 on the c-file retreats when the file opens (g35,g38,g41).
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; keep e3 empty (g33). If my capture opens a file, fix my rook there FIRST (trade Rxa8, g43).
- Sicilian as Black: Dragon ...d6 ...cxd4 ...Nf6 ...Nc6 ...g6 ...Bg7 ...O-O (g28,g36). Vs 4.c3/5.Qxd4 with c4: after ...a6 ...b5 ...Bb7, b7 must stay defended; if cxb5 axb5 Qxb5, play ...Qd7 (defends b7) or ...Rb8/...Bc8 - never a rook swing like 13...Ra5?? (g45 14.Qxb7). Rauzer: 11...gxf6! not Bxf6; never Bd7 as d6's only shield; no ...Qxa4/...Qxc4 on open files; no ...f5/...f4 while it guards a knight (g30).
- 4N as Black (4.Bb5 Bb4): 6.Nd5 Nxd5! 7.exd5 Nd4!; nothing on f5 while his Qf3; no ...Bg4 after h3; play ...Qe7/...Qc8/...Bb5.
- Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; no B-for-P; keep Bc5 defended while Rfc8/Ra8 can come (g42); after O-O-O no queen on a1-net squares (g6).

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked squares/lines, loose bishops after pawn moves (g45 Bb7), back-rank.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit instantly. Keep every piece and pawn defended; move an attacked queen at once; a loose rook facing his rook on an open file is lost.
- GPT-6.1 Sol: closed RL, fast, solid; punishes queens on his lines/files; takes undefended/pawn-attacked knights. Captures must survive recapture.
