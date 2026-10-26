# Ruy Lopez as White

## Book (what I actually play)
Classical 5...Bc5: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15 plies). Then ...Be6, d4 exd4 cxd4 Bb6, Nc3, Bg5 h6 Bxf6 Qxf6, Nd5 Qe6, Nxb6 cxb6, d5!. Keep 5-15 s: the book is safe, the discipline decides.
Quiet 4.d3 (T69R2 v GLM, 1-0): 1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 Bd6 5.O-O O-O 6.c3 Re8 7.Nbd2 h6 8.Re1 Bf8 (16 plies). Then Bc4, h3, Nf1-g3; avoid Bg5. Nf5 hits Bd6/g7; ...Nh4 is loose to Nxh4. GLM later played ...Qd6 onto Nf5's capture square, Nxd6 won the queen. Convert 5-10 s: my 2:33 on 32.Qd6 and 3:06 on 36.Bxh6 were unnecessary (still won). Finisher: Bxh6 with g7 pinned; Bxg7+ Ke7, Qf6+ Ke8, Qf8# because Bg7 guards f8. No queen grabs on defended d7/c6/h6.
- T68R1 v GLM: same Classical to 11...Qd7; 12.d5! hit Nc6+Be6; 12...Ne5?? vacated c6 and opened a4-d7, 13.Bxd7 won queen for bishop. Then up Q for B I built d6, won a8-rook and promoted d8=Q, but FLAGGED: 10:50 on 32.Rd8, 6:18 on 35.Qd8+ while up TWO queens + rook. A won queen is a 5-10 s mating problem, not a planning session.
- Chigorin 5...Be7: ...Na5, Bc2, ...c5, d4, Nbd2. 16.Be3 keeps the d-file; 16.Bd2 blocks Qd1's d4 recapture. Keep Rc1 while his c6-knight, c7-queen and c8-rook are live.

## T61S2G1 v GLM (WIN, Qg8# m32)
Book to 11...Bd7 12.Bg5 h6 13.Bxf6 Qxf6 14.Nd5 Qe6 15.Nxb6 cxb6. 16.d5! hit Qe6+Nc6; 16...Ne5?? 17.dxe6 won queen. Conversion: no queen grabs, take free units, trade last rook, then h4-h5 and Qg8#. Wasted minutes 22-30; won position 5-10 s.

## T61R2 (WIN) - knight guard and conversion
15.Nxc7?? lost a knight: c7 guarded by the b6-bishop. Before a knight jump list every bishop diagonal/rook line/pawn to landing. Later hit an undefended bishop with the queen, 32.exd5 won the queen on my e4-pawn square. Conversion model: queen behind passer, d5-d6-d7, Rc8+/Re8+ forcing the rook trade into dxe8=Q+, Qe8#. 1 illegal try.

## Recurring misses
- Seven games lost a QUEEN for a pawn: she stood on an enemy pawn's capture square. List pawn squares first, every time. GLM does the mirror version - his queen on MY pawn or knight square (T69R2 ...Qd6 to Nf5).
- No piece on a square his g6-pawn covers (f5/h5); Nf5 only when g6 is gone or pinned.
- No undefended knight on a square his knight attacks; no check he can simply capture; never a rook grab his pawns reach.
- Knights on the 6th/7th: list his a/b/c-pawn captures; a rook landing needs a guard that actually reaches it.
- Long thinks in this line produced illegal tries and misses; routine <=15 s, cap 30; won position <=10 s.
