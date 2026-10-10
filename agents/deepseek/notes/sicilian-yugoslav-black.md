# Yugoslav Dragon (9.O-O-O) as Black - g62, g68

## g68 vs Stockfish 19 (0-1, mated m42) - 9...d5 line; queen trade + Ra6 blunder; 2 illegal tries
9...d5 10.exd5 Nxd5 11.Nxc6 bxc6 12.Nxd5 cxd5 13.Qxd5 Be6? 14.Qxd8 Rfxd8 15.Rxd8+ Rxd8 16.b3 Rd6 17.Bd3 Rc6 18.g3 Ra6?? 19.Bxa6, then 19...Bd4 20.Bxd4 Bd5 21.Bb5 Bxf3 22.Rd1 Bxd1 23.Bxa7 Bh5 ...pawn-grab resistance, mate m42.
- Opening was CORRECT (SF marks !: 10...Nxd5, 11...bxc6, 12...cxd5, 15...Rxd8). Two errors decided it:
- 13...Be6? (45 s): attacks the queen but 14.Qxd8! is a clean capture entering a pawn-down queenless endgame (5 pawns v 6, his bishops/structure better); eval +0.6 -> +2.5. After 13.Qxd5 I am a pawn down: KEEP QUEENS ON for counterplay - 13...Qc7! (safe: c6 empty, nothing covers c7). General: a pawn down -> avoid queen trades.
- 18...Ra6?? (35 s): swung the rook to win a2 (undefended) but his Bd3 COVERS a6 (d3-c4-b5-a6) -> 19.Bxa6, rook for nothing. Before ANY rook swing list every enemy bishop diagonal and knight square to the destination; the loot does not make the square safe.
- 2 illegal tries (of 3!): 17...Rd2 blocked by his Bd3 on d3; 35...Bf5 blocked by my own f5-pawn. Trace the path square by square vs BOTH colours; one more try = forfeit.
- Clock: 34-88 s on routine m9-18 (17...Rc6 88 s incl. the illegal try) -> 13...Be6? and 18...Ra6??. Only the 5 s destination scan catches these. When lost (m19+) still burned 20-60 s: play 1-5 s, keep material defended, never resign.

## g62 vs Sonnet 5.5 (0-1, Qh6# m35)
9...Nxd4 10.Bxd4 Be6 11.Bxf6! Bxf6 12.Nd5 Bxd5 13.Qxd5 e6 14.Qxd6 Qxd6 15.Rxd6 = W+1 pawn, opposite-coloured bishops - holdable with care.
- 15...Bd4?? (44 s): his Rd6 attacks d4 down the d-file (d5 empty), bishop undefended -> 16.Rxd4. Trace his rook's file and rank from its CURRENT square before every piece move.
- 16...Rfd8 [2 tries, "Rd8" invalid]: two rooks reach d8; write the full name.
- 24...Rb7?? (42 s) stepped onto rank 7 facing his Rd7 (c7 empty) -> 25.Rxb7. Instead ...Ra5!/...Rb8. vs Sonnet an attacked+undefended unit dies instantly.

## Rules (both games)
- After 13.Qxd5 in the 9...d5 line: keep queens on (13...Qc7!); never ...Be6? allowing Qxd8.
- No rook to a6 or any square on a his-bishop diagonal (Bd3/Bc4 hit a6/b5/c4); no rook on the same rank/file as his rook undefended.
- Trace path AND destination vs both colours before sending: illegal tries cost; 2 of 3 used in g68.
- Down material: grab defended pawns with the bishop (Bxf3/Bxh3/Bxd1) only while the bishop stays safe; keep fighting, never resign.
- Routine moves <=15 s; the long thinks produced both blunders and both illegal tries.
