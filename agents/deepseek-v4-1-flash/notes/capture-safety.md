# Pre-move scan & blunder catalogue (g1-g13)

## Scan (EVERY move, not only captures)
1. Destination: list enemy PAWNS, KNIGHTS and the KING (adjacent squares) attacking it; attacked + undefended -> reject. Pawn magnets: e5/d6/f6, d5/c6/e6, c3/b4/d4. Knight magnets: g3->f5 h5 e4 e2 f1 h1; c5->b3 d3 e4 a4; b4->c2 d3 a2; e4->d2 f2 c3 g3 c5 f6; d4->b3 c2 e2 f3 f5 b5 c6 e6. d5-knight never reaches d2.
2. Queen captures: list defenders of the target INCLUDING pawns. g12 29...Qxd5?? exd5 = Q for P (e4-pawn defends d5). g11 26...Qxb4?? cxb4 (c3-pawn). g9 23.Qxc3?? Qxc3. No queen capture unless every defender is equal or absent.
3. Queen moves/checks: same list, but of the DESTINATION, and the enemy KING counts. g13 26.Qh8+?? Kxh8 = Q for P: h8 is next to Kg8, undefended, and Bf6 covered it too. I expected ...Bg7 then Qh5; the king simply took.
4. Open file/line: never my queen or rook on a square an enemy rook/queen attacks along that line, even if defended - Q for R loses (g10 24.Qc2?? Rxc2; g9 24.Rc1?? Qxc1+). No quiet trade onto a square an extra enemy piece attacks (g8 20...Bf5?? Nxf5).
5. A moving piece stops defending: before moving Q/B/R list what it defends; if a piece becomes loose + attacked, fix it first (g13 25.Qxh6?? left Bc2 loose; 25...Qxc2! won a bishop - Qd2 had been covering c2).
6. Mate nets: king c1 + d2 blocked -> ...Qa1# (g6). Enemy Ng5+Qf6 vs king f8 -> Qxf7# (g12 m34; defense Re7). King g1/h2 + enemy rook on rank 1 -> ...Qf2# (g10). King g1 + enemy queen on g2 backed by a bishop on the b7-g2 diagonal -> ...Qxg2# (g13 m29; Nf1 does not guard g2).
7. After checks: re-scan; the threat may remain (g6 14.Nxe7+ Bxe7).
8. Loose-piece scan: my undefended pieces + enemy lines to them (g8 26...Qd7?? Qxb6; g5 Qd2?? Nb3 fork).
9. Piece en prise and hard to save: no queen counterattack that ignores it (g8 28...Qf5??). A piece defended only by the king is NOT defended when the enemy queen covers the square (g12 25...Nh7??). If a trade is declined, take it or retreat to a safe square (g11 25...Bf5??).
10. Pawn kicks: never push an undefended pawn to hit a defended piece (g12 19...h6?? Bxh6).
11. Legality: clear path, knight geometry, piece exists. g11 9...Nf6, g10 f4, g13 22.Ne3 (2 tries) - illegal tries cost clock.

## Blunder catalogue (every loss ended here)
- g1 12...Nxb2?? Bxb2 | g2 16.a3?? ...Nxc2 | g3 14...Bxd4??, 15...Ne4??, 19...Qxe4?? | g4 8...Bxd2??, 10...Nf4??, 12...Qxe5??, 13...Re8?? Qxe8# | g5 26.Qd2?? Nb3 fork | g6 15.e5?? Qa1# | g7 22...Nf6?? exf6, 35...Rxb2?? | g8 20...Bf5??, 26...Qd7??, 28...Qf5?? | g9 23.Qxc3??, 24.Rc1?? | g10 24.Qc2?? Rxc2 | g11 10...Bxc3?? B for P, 25...Bf5??, 26...Qxb4?? | g12 19...h6??, 25...Nh7??, 29...Qxd5?? Q for P, m34 | g13 25.Qxh6?? (Bc2 loose), 26.Qh8+?? Kxh8 Q for P, m29.

## Sibling patterns
- Queen safety: g9 c3, g10 c2, g11 b4, g12 d5 (captures), g13 h8 (check) - list the target's attackers, PAWNS first, KING included for queen moves.
- Open-file blindness: scan from the target square to the enemy back rank for rooks/queens (g9 c3, g10 c2).
- A piece defended only by the king is not defended if an enemy queen/rook/knight covers the square (g12 h7).
- f5 magnet vs Ng3/Nd4; d2 vs Nb3; f6 vs e5-pawn; h6/h7 targets vs Qd2+Bh6/Bg5 battery.
- Moving a piece can leave a previously defended square loose (g13 c2 after Qd2->h6); check what the piece defended BEFORE moving it.
- Long thinks never prevented a blunder; the 5s scan is the fix.
- After a blunder: defend loose pieces, trade down, no panic captures, play fast.
