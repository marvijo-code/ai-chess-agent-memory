# Pre-move scan & blunder catalogue (g1-g21)

## Scan (EVERY move, 5s) - apply to the FINAL move, not the plan (g21: wrote "Nb4 attacks d3", played 15.Bd3??)
1. Destination: do enemy PAWNS, KNIGHTS or the KING attack it? Attacked + undefended -> reject. Pawn magnets (enemy pawn position -> squares it attacks): e5->d6/f6; d5->c6/e6; c3->b4/d4; a2->b3; b3->a4/c4; b5->a4/c4 (g21 18.Nc4?? bxc4); c4->b3/d3 (g21 22.Qb3?? cxb3 = Q for P). Knight magnets: b4->a2/c2/d3/d5 (g21 15.Bd3?? Nxd3 = B+R for N); full lists in MEMORY.md.
2. Queen/rook moves: list ALL attackers - pawns, knights, KING, rooks/queens on lines, bishops/queens on diagonals. Defended is not enough: reject Q for B/N/P (g18 23.Qd5?? Bxd5; g19 28...Qxd5?? Bxd5; g10 24.Qc2?? Rxc2; g13 26.Qh8+?? Kxh8; g14 17...Qe1+?? Rxe1). Never take/place a queen on d5 while any P/N/B/R recaptures (g12, g17, g18, g19). Queen captures: defenders include pawns (g12 29...Qxd5??; g11 26...Qxb4??). Queen leaves a duty: name the squares it covered (g13 c2; g17 d4 -> 13.Qxd4!); recheck after enemy moves (g16 26...Nxe4?? Re1 re-covered e4).
3. Pinned knight (Ba4-d7-e8): moving it loses the exchange (g15 17...Nb6? 18.Bxe8!). Unpin ...Rb8.
4. Mate nets: king c1+d2 blocked -> ...Qa1# (g6). Ng5+Qf6 vs king f8 -> Qxf7# (g12). King g1/h2 + enemy rook rank 1 -> ...Qf2# (g10); Qg2+Bb7 -> ...Qxg2# (g13). King g8/h8, f7/g7/h7, 8th rank open -> ...Re8#/...Qc8# (g14, g16; g19 33...Rc8?? 34.Qxc8#). King h1, own g2 pawn, enemy rook rank 1 + queen covers h2 -> ...Rb1# (g21). After checks re-scan (g6).
5. Loose pieces: my undefended units + enemy Q/R/N lines (g8 26...Qd7?? Qxb6). King-only defense fails vs a queen (g12 25...Nh7??). Piece en prise: no counterattack that ignores it (g8 28...Qf5??; g15 25...Nc4); declined trade -> take or retreat safe (g11 25...Bf5?? Nxf5).
6. Pawn pushes: never undefended onto a defended piece (g12 19...h6?? Bxh6), onto a knight-attacked square (g16 21...f5?? Nxf5), or where the queen takes with tempo (g19 24...b3?? Qxb3+). No rook grabs a pawn a rook/queen recaptures (g18 25.Rxe5 Rxe5).
7. Enemy pawn attacks a knight -> MOVE it (g19 18...Nd7?! 19.dxc6 = N for P).
8. Legality: path, knight geometry (c6-knight cannot reach d7), own piece blocks (g21 Qd3 blocked by Nd2). Illegal tries waste clock (g18: 4, g19: 2, g21: 1).
9. Closed RL: keep the dark bishop (g13, g18).

## Blunder catalogue (all losses)
g1 12...Nxb2?? | g2 16.a3?? Nxc2 | g3 14...Bxd4??, 15...Ne4??, 19...Qxe4?? | g4 8...Bxd2??, 10...Nf4??, 12...Qxe5??, 13...Re8?? Qxe8# | g5 26.Qd2?? Nb3 | g6 15.e5?? Qa1# | g7 22...Nf6?? exf6, 35...Rxb2?? | g8 20...Bf5??, 26...Qd7??, 28...Qf5?? | g9 23.Qxc3??, 24.Rc1?? | g10 24.Qc2?? Rxc2 | g11 10...Bxc3??, 25...Bf5??, 26...Qxb4?? | g12 19...h6??, 25...Nh7??, 29...Qxd5?? | g13 21.Bxf6?!, 25.Qxh6??, 26.Qh8+?? | g14 17...Qe1+?? Rxe1, 19.Re8# | g15 17...Nb6? 18.Bxe8, 19...Bxd5??, 23...Qxe5?? | g16 18...Nc4??, 26...Nxe4??, 27...Bxd5??, 41.Rd8# | g17 12...Qd6?? 13.Qxd4!, 13...Qxd5?? Qxg7# | g18 21.Bxc5?!, 23.Qd5?? Bxd5, 25.Rxe5 Rxe5 | g19 18...Nd7?!, 24...b3?? Qxb3+, 28...Qxd5?? Bxd5, 33...Rc8?? Qxc8# | g21 15.Bd3?? Nxd3/Nxe1 = B+R for N, 18.Nc4?? bxc4 = N for P, 22.Qb3?? cxb3 = Q for P, 29...Rb1#.

## Patterns
- Queen safety on d5 (g12/g17/g18/g19); queen leaving a duty (g13 c2, g17 d4).
- Magnet squares ignored: piece/queen onto a square an enemy N/P attacks (g16 c4, g21 d3/c4/b3).
- Pinned knight drops the exchange (g15). King-only defense loses to Q/R/N (g12, g17).
- King on the back rank with no luft: enemy Q/R reaching it mates (g14, g16, g19, g21 h1).
- Long thinks never prevented a blunder; the 5s scan is the fix. After a blunder: defend loose pieces, trade down, play fast.
