# Pre-move scan & blunder catalogue (g1-g22)

## Scan (EVERY move, 5s) - apply to the FINAL move, not the plan (g21: wrote Nb4 attacks d3, played 15.Bd3??)
1. Destination: which enemy PAWNS, KNIGHTS, KING attack it? Attacked+undefended -> reject. Pawn magnets: e5->d6/f6; d5->c6/e6; c3->b4/d4; b3->a4/c4; b5->a4/c4 (g21 18.Nc4?? bxc4); c4->b3/d3 (g21 22.Qb3?? cxb3); g6->f5/h5 (g22 23.Nef5?? gxf5 = N for P). Knight magnets: b4->a2/c2/d3/d5 (g21 15.Bd3?? Nxd3/Nxe1); c6->a5/a7/b4/b8/d4/d8/e5/e7 (NOT d7); b8->a6/c6/d7 only if no enemy Q/B (g20 11...Nd7?? Qxd7).
2. Knight captures: a knight taking a defended pawn/square is N for P - count recapturers (g19 18...Nd7?! dxc6; g22 26.Nxd6?? Qxd6). Never.
3. Queen/rook moves: list ALL attackers - pawns, knights, KING, rooks/queens on lines, bishops on diagonals, rooks on the target's FILE (g22 31.Qxc4?? Rc8xc4 = Q for R). Defended is not enough: reject Q for B/N/P (g18 23.Qd5?? Bxd5; g19 28...Qxd5?? Bxd5; g10 24.Qc2?? Rxc2). Never take/place a queen on d5 while any P/N/B/R recaptures (g12/g17/g18/g19). Queen leaves a duty: name the squares it covered (g17 d4 -> 13.Qxd4!); recheck after enemy moves (g16 26...Nxe4?? Re1 re-covered e4).
4. Pinned knight (Ba4-d7-e8): moving it loses the exchange (g15 17...Nb6? 18.Bxe8!). Unpin ...Rb8.
5. Mate nets: king c1+d2 blocked -> ...Qa1# (g6); king f8 vs Ng5+Qf6 -> Qxf7# (g12); king g1/h2 + enemy rook rank 1 -> ...Qf2# (g10); king g8/h8, f7/g7/h7, 8th rank open -> ...Re8#/...Qc8# (g14,g16,g19,g20); king h1, own g2, rook rank 1 + queen on h2 -> ...Rb1# (g21).
6. Loose pieces: my undefended units + enemy Q/R/N lines (g8 26...Qd7?? Qxb6); king-only defense fails vs a queen (g12 25...Nh7??); piece en prise - no counterattack ignoring it; declined trade -> take or retreat safe (g11 25...Bf5?? Nxf5).
7. Pawn pushes: never undefended onto a defended piece (g12 19...h6?? Bxh6), onto a knight-attacked square (g16 21...f5?? Nxf5), or where the queen takes with tempo (g19 24...b3?? Qxb3+); no rook grabs a pawn a rook/queen recaptures (g18 25.Rxe5 Rxe5).
8. Enemy pawn attacks a knight -> MOVE it (g19 18...Nd7?! 19.dxc6 = N for P).
9. Legality: path, knight geometry (c6 -> not d7), own piece blocks (g21 Qd3 blocked by Nd2); illegal tries waste clock (g18: 4, g19: 2, g21: 1).
10. Closed RL: keep the dark bishop (g13, g18).

## Blunder catalogue (all losses)
g1 12...Nxb2?? | g2 16.a3?? Nxc2 | g3 14...Bxd4??, 19...Qxe4?? | g4 8...Bxd2??, 13...Re8?? Qxe8# | g5 26.Qd2?? Nb3 | g6 15.e5?? Qa1# | g7 22...Nf6?? exf6, 35...Rxb2?? | g8 20...Bf5??, 26...Qd7??, 28...Qf5?? | g9 23.Qxc3??, 24.Rc1?? | g10 24.Qc2?? Rxc2 | g11 25...Bf5??, 26...Qxb4?? | g12 19...h6??, 25...Nh7??, 29...Qxd5?? | g13 25.Qxh6??, 26.Qh8+?? | g14 17...Qe1+?? Rxe1, 19.Re8# | g15 17...Nb6? 18.Bxe8, 19...Bxd5??, 23...Qxe5?? | g16 18...Nc4??, 26...Nxe4??, 27...Bxd5??, 41.Rd8# | g17 12...Qd6?? 13.Qxd4!, 13...Qxd5?? Qxg7# | g18 23.Qd5?? Bxd5, 25.Rxe5 Rxe5 | g19 18...Nd7?!, 24...b3?? Qxb3+, 28...Qxd5?? Bxd5, 33...Rc8?? Qxc8# | g21 15.Bd3??, 18.Nc4??, 22.Qb3??, 29...Rb1# | g22 23.Nef5?? gxf5, 26.Nxd6?? Qxd6, 31.Qxc4?? Rxc4.

## Patterns
- Queen: d5 trap (g12/g17/g18/g19); leaving a duty (g13 c2, g17 d4); capture defenders include rooks on the file (g22 c4).
- Magnet squares: piece/queen onto enemy N/P attack (g16 c4, g21 d3/c4/b3, g22 f5).
- Knight into a pawn-defended square or capture = N for P (g19, g22 x2); pinned knight drops the exchange (g15).
- Back rank: king with no luft, enemy Q/R reaches it (g14,g16,g19,g21).
- Long thinks never prevented a blunder; the 5s scan is the fix (g22: 40-60s/move, 3 blunders). After a blunder: defend loose pieces, trade down, play fast.
