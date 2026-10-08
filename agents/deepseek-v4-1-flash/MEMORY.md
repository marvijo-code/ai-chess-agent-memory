# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan, blunder + mate catalogue)
- notes/sicilian-dragon-white.md (g6: Yugoslav, Qa1# in 15)
- notes/four-knights-black.md
- notes/ruy-lopez-black.md
- notes/ruy-lopez-white.md (games 2, 5)

## Rule 1 - pre-move scan (ALL losses, g1-g6)
Before EVERY move:
1. Destination: which enemy pawns/pieces attack it? Attacked + undefended -> reject unless a forcing follow-up.
2. Captures: list EVERY recapturer (pawns count, queen behind); count material after the full exchange. Piece-for-pawn = -2; never queen for N/B/P. This includes my checks: g6 14.Nxe7+ was knight-for-pawn because the f6-bishop recaptured.
3. Mate net: every enemy queen/rook/bishop line to my king's entry squares. With king c1, Rd1, Qd2, b2/c2 pawns: ...Qa1# (b1 free, d2 self-blocked). A Black queen on a1/a2/b2 near my castled king = mate alert: free d2 (Qe3/Qd3) or guard a1 (Qc1) NOW, no quiet pawn move (g6: 13...Qxa2! ... 15.e5?? Qa1#).
4. After a check/forced sequence: re-scan. My check does not remove their pending mate (g6: 14.Nxe7+ Bxe7, mate still there).
5. Knight-fork scan: enemy knight jumps attacking 2 of my pieces (Nb3 hits a1+d2, Nc2 hits Ra1+Re1, c5->b3). Never queen on such a square.
6. Legality/paths: own pieces must not block the route; pick the right rook (g5: 'Rad1' illegal, my Bb1 blocked the a1-rook).
Blunder shapes: piece-for-pawn, queen for lesser, piece onto an attacked square, Nb3 fork vs Qd2, mate: Re8?? Qxe8#, e5?? Qa1#.

## Rule 2 - time (900+10)
Opening/book <=10s, routine <=15s, max 3 thinks of 30-45s. Long thinks never prevented a blunder (g5: eight 30-45s thinks, then Nb3 fork; g6: 40-48s on moves 9-13, mated move 15). Dead-lost: 5s moves, nothing more lost.

## Openings
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O solid; ...dxe4/fxe4/Nxd4/Bxd4 fine. But the long-castled king's only escape is d2; watch ...Qxa2/...Qa1 ideas, and don't spend 40s on these book moves. notes/sicilian-dragon-white.md.
- RL as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, Chigorin/Breyer; keep f7 covered; ...Nxb2 only if a rook already covers b2. notes/ruy-lopez-black.md.
- RL as White: Chigorin 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5! Nb4 15.Bb1 16.a3 Na6 17.Nf1 Bd7 18.Ng3 Nc5, then Bg5, Red1, Qe2/e3 (not d2 while Nb3 possible), f4. If ...Nb4 with only the queen on c2: 16.Rac1/Bb1, never 16.a3?? (g2 ...Nxc2). notes/ruy-lopez-white.md.
- Four Knights 4.Bb5 Bb4: 6.Nd5 Nxd5 7.exd5 Ne7, 8.Nxe5 ~+0.5, answer 8...Nxd5/d6/c6; never 8...Bxd2??. Nc4 hits b6 -> ...b5. notes/four-knights-black.md.

## Opponents
- Stockfish 19 (ladder): ~0s/move, banks clock, punishes every loose piece and every pawn grab that carries a mate threat (g6 ...Qxa2!). Never blunders back. Full Rule 1 scan every move.
- Sonnet 5.5: fast, sound; stay ahead on clock.
- GPT-6.1 Sol: solid closed Ruy Lopez; punishes loose pieces/queen placement, finds ...Nb3 forks; keep all defended, queen off fork squares; punish his blunders (g5 21...Nh7??) calmly with Rd1/Qe2/f4.

## Principles
- Material first: no piece for a pawn, no queen for N/B/P, no capture on a defended square unless equal-or-better.
- Scan mate nets + loose pieces before every quiet move, and again after every check.
- After a blunder: defend loose pieces, trade down, no panic captures.
