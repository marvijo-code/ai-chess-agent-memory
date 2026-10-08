# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan, blunder + mate catalogue)
- notes/sicilian-dragon-white.md (g6: Yugoslav, Qa1# in 15)
- notes/four-knights-black.md
- notes/ruy-lopez-black.md (Chigorin, g7)
- notes/ruy-lopez-white.md (games 2, 5)

## Rule 1 - pre-move scan (ALL losses, g1-g7)
Before EVERY move:
1. Destination: list enemy PAWNS and pieces that attack it. Pawn magnets: e5 pawn hits d6/f6; d5 pawn hits c6/e6. With a White pawn on e5, NEVER move a knight to f6/d6 (g7 24...Nf6?? 25.exf6 lost the knight; the same f6 square was already bad at 22...Nf6??). Attacked + undefended -> reject unless forcing follow-up.
2. Captures/pawn grabs: list EVERY recapturer/defender of the target square (pawns count, queen behind); count material after the full exchange. Piece-for-pawn = -2; never queen for N/B/P. b2/c2 grabs with a minor or rook are a chronic killer: g1 ...Nxb2??, g2 ...Nxc2, g7 35...Rxb2?? Rxb2 (b2 was defended by the R that had just gone to b4). Only grab if NO enemy piece attacks that square. My checks too: g6 14.Nxe7+ was knight-for-pawn (f6-bishop recaptured).
3. Mate net: every enemy queen/rook/bishop line to my king's entry squares. With king c1, Rd1, Qd2, b2/c2 pawns: ...Qa1# (b1 free, d2 self-blocked). A Black queen on a1/a2/b2 near my castled king = mate alert: free d2 (Qe3/Qd3) or guard a1 (Qc1) NOW, no quiet pawn move (g6: 13...Qxa2! ... 15.e5?? Qa1#).
4. After a check/forced sequence: re-scan. My check does not remove their pending mate (g6: 14.Nxe7+ Bxe7, mate still there).
5. Knight-fork scan: enemy knight jumps attacking 2 of my pieces (Nb3 hits a1+d2, Nc2 hits Ra1+Re1, c5->b3). Never queen on such a square.
6. Legality: own pieces must not block the route; pick the right rook (g5: 'Rad1' illegal, my Bb1 blocked). Before any capture: the target square must hold an ENEMY piece and my piece must reach it on a rank/file/diagonal with a clear path (g7: wasted attempts Bxd5 onto my own knight, Qxf6 from c7 - not a line).
Blunder shapes: piece-for-pawn, queen for lesser, piece onto a pawn-attacked square (24...Nf6??), rook grab of a defended pawn (35...Rxb2??), mate: Re8?? Qxe8#, e5?? Qa1#.

## Rule 2 - time (900+10)
Opening/book <=10s, routine <=15s, max 3 thinks of 30-45s. In g7 I spent 40-50s on moves 14-24 (Bb7/Rac8/Rfe8/Na5/Nxb3/Bf8/Nd7/d5) and still blundered, finishing 3:19 vs 11:34. Dead-lost: 5s moves, nothing more lost.

## Openings
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O solid; ...dxe4/fxe4/Nxd4/Bxd4 fine. But the long-castled king's only escape is d2; watch ...Qxa2/...Qa1 ideas, and don't spend 40s on these book moves. notes/sicilian-dragon-white.md.
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8/...Rfe8. Keep f7 covered. The ...d5 break (backed by Bb7) is thematic and sound; after ...d5 exd5 the d5-knight is immune (Qxd5?? Bxd5 gives Q for N) - keep it there or use ...Nb4/...Nb6, never ...Nf6 in front of an e5 pawn. notes/ruy-lopez-black.md.
- RL as White: Chigorin 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5! Nb4 15.Bb1 16.a3 Na6 17.Nf1 Bd7 18.Ng3 Nc5, then Bg5, Red1, Qe2/e3 (not d2 while Nb3 possible), f4. If ...Nb4 with only the queen on c2: 16.Rac1/Bb1, never 16.a3?? (g2 ...Nxc2). notes/ruy-lopez-white.md.
- Four Knights 4.Bb5 Bb4: 6.Nd5 Nxd5 7.exd5 Ne7, 8.Nxe5 ~+0.5, answer 8...Nxd5/d6/c6; never 8...Bxd2??. Nc4 hits b6 -> ...b5. notes/four-knights-black.md.

## Opponents
- Stockfish 19 (ladder): ~0s/move, banks clock, punishes every loose piece and every pawn grab that carries a mate threat (g6 ...Qxa2!). Never blunders back. Full Rule 1 scan every move.
- Sonnet 5.5 (g7): fast, sound, punishes hanging pieces instantly (25.exf6) and finds tactical resources (32.Bxh7+ Kxh7 33.Rxd4 won back the queen). Does make rare mistakes (29.Qd5??, 31.Qxd4??) but recovers. Stay ahead on clock; keep everything defended, no loose pieces, no pawn grabs.
- GPT-6.1 Sol: solid closed Ruy Lopez; punishes loose pieces/queen placement, finds ...Nb3 forks; keep all defended, queen off fork squares; punish his blunders (g5 21...Nh7??) calmly with Rd1/Qe2/f4.

## Principles
- Material first: no piece for a pawn, no queen for N/B/P, no capture on a defended square unless equal-or-better; b2/c2 pawn grabs are losing by default.
- Scan pawn attack-squares + mate nets + loose pieces before every quiet move, and again after every check.
- R ending down one pawn is holdable: keep the rook, defend pawns, avoid panic grabs.
- After a blunder: defend loose pieces, trade down, no panic captures.
