# Pre-move scan & blunder catalogue (g1-g15)

## Scan (EVERY move, not only captures)
1. Destination: enemy PAWNS, KNIGHTS and the adjacent KING attack it? attacked + undefended -> reject. Pawn magnets: e5/d6/f6; d5/c6/e6; d5 is also defended by the e4-pawn (g15 19...Bxd5?? exd5 = B for P); c3/b4/d4. Knight magnets: g3->f5 h5 e4 e2 f1 h1; c5->b3 d3 e4 a4; b4->c2 d3 a2; e4->d2 f2 c3 g3 c5 f6; d4->b3 c2 e2 f3 f5 b5 c6 e6. d5-knight never reaches d2.
2. Queen captures: list defenders INCLUDING pawns. g12 29...Qxd5?? exd5 = Q for P; g11 26...Qxb4?? cxb4; g9 23.Qxc3??; g15 23...Qxe5?? Qxe5 (open e-file, Qe3 covered e5, my Qe8 undefended) = Q for N. No queen capture unless every defender is equal or absent.
3. Queen moves/checks: same list for the DESTINATION; the enemy KING counts, and rooks/queens on cleared lines count. g13 26.Qh8+?? Kxh8 = Q for P (Bf6 covered h8 too). g14 17...Qe1+?? Rxe1 = QUEEN FOR NOTHING (a1-rook took on the cleared rank). Never move - even with check - the queen where any enemy piece or the KING can capture.
4. Open file/line: never my queen or rook on a square an enemy rook/queen attacks along that line, even if defended (g10 24.Qc2?? Rxc2; g9 24.Rc1?? Qxc1+). No quiet trade onto a square an extra enemy piece attacks (g8 20...Bf5?? Nxf5).
5. Pinned knight: bishop pin Ba4-Nd7-Re8 -> moving the knight loses the exchange (g15 17...Nb6? 18.Bxe8!). Unpin with the rook first or keep the knight home. A moving Q/B/R stops defending: check its old squares (g13 25.Qxh6?? left Bc2 loose, 25...Qxc2!).
6. Mate nets: king c1 + d2 blocked -> ...Qa1# (g6). Enemy Ng5+Qf6 vs king f8 -> Qxf7# (g12 m34; defense Re7). King g1/h2 + enemy rook on rank 1 -> ...Qf2# (g10). King g1 + enemy queen g2 backed by Bb7 -> ...Qxg2# (g13 m29; Nf1 does not guard g2). Back rank: king g8, f8/h8 uncovered, enemy rook e8/d8 -> Re8# (g14 m19; own Ra8/Bc8 blocked).
7. After checks re-scan; the threat may remain (g6 14.Nxe7+ Bxe7).
8. Loose pieces: my undefended pieces + enemy queen/rook/knight lines to them (g8 26...Qd7?? Qxb6; g5 Qd2?? Nb3 fork).
9. Piece en prise and hard to save: no queen counterattack that ignores it (g8 28...Qf5??; g15 25...Nc4 chased the queen, then Qxd5/Qb3/Qb7 won the knight). A piece defended only by the king is NOT defended when an enemy queen covers the square (g12 25...Nh7??). If a trade is declined, take it or retreat to a safe square (g11 25...Bf5?? Nxf5).
10. Pawn kicks: never push an undefended pawn to hit a defended piece (g12 19...h6?? Bxh6).
11. Legality: clear path, knight geometry, piece exists (g11 9...Nf6, g10 f4, g13 22.Ne3, g14 13...Bf5/18...Bb7 own-pawn blocks) - illegal tries waste clock.

## Blunder catalogue (every loss ended here)
g1 12...Nxb2?? Bxb2 | g2 16.a3?? ...Nxc2 | g3 14...Bxd4??, 15...Ne4??, 19...Qxe4?? | g4 8...Bxd2??, 10...Nf4??, 12...Qxe5??, 13...Re8?? Qxe8# | g5 26.Qd2?? Nb3 | g6 15.e5?? Qa1# | g7 22...Nf6?? exf6, 35...Rxb2?? | g8 20...Bf5??, 26...Qd7??, 28...Qf5?? | g9 23.Qxc3??, 24.Rc1?? | g10 24.Qc2?? Rxc2 | g11 10...Bxc3??, 25...Bf5??, 26...Qxb4?? | g12 19...h6??, 25...Nh7??, 29...Qxd5??, m34 | g13 25.Qxh6??, 26.Qh8+??, m29 | g14 17...Qe1+?? Rxe1, 19.Re8# | g15 16...c5?!+17...Nb6? 18.Bxe8 (exchange), 19...Bxd5?? B for P, 23...Qxe5?? Q for N, m34.

## Sibling patterns
- Queen safety: g9 c3, g10 c2, g11 b4, g12 d5, g15 e5 (captures); g13 h8, g14 e1 (checks). List attackers first: PAWNS, KING, rooks/queens on lines.
- Pinned knight behind a bishop (Ba4-d7-e8): moving it drops the exchange; always check what stands behind a pinned or skewered piece.
- Bishop takes a defended pawn = B for P: g4 Bxd2, g11 Bxc3, g15 Bxd5. Count pawn defenders.
- King-only defender loses to a queen/rook/knight covering the square (g12 h7).
- f5 vs Ng3/Nd4; d2 vs Nb3; h6/h7 vs Qd2+Bh6/Bg5.
- Long thinks never prevented a blunder; the 5s scan is the fix. After a blunder: defend loose pieces, trade down, no panic captures, play fast.
