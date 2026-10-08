# Pre-move scan & blunder catalogue (g1-g17)

## Scan (EVERY move)
1. Destination: do enemy PAWNS, KNIGHTS or the KING attack it (now, not just before)? Attacked + undefended -> reject. Pawn magnets shift with the pawn: e5->d6/f6; d5->c6/e6; c3->b4/d4; b3->a4/c4 (g16 18...Nc4?? bxc4 = N for P); a2->b3. Knight magnets: see MEMORY.md.
2. Queen captures: list defenders INCLUDING pawns (g12 29...Qxd5?? exd5; g11 26...Qxb4?? cxb4; g15 23...Qxe5?? Qxe5; g17 13...Qxd5?? Qxg7# = mate ignored). No queen grab unless every defender is equal or absent AND no enemy mate/battery exists.
3. Queen moves/checks: same list for the DESTINATION; the enemy KING and rooks/queens on cleared lines count. g13 26.Qh8+?? Kxh8; g14 17...Qe1+?? Rxe1. Never move - even with check - the queen where any enemy piece or the KING can capture.
4. Open file/line: never my queen or rook on a square an enemy rook/queen attacks along that line, even if defended (g10 24.Qc2?? Rxc2; g9 24.Rc1?? Qxc1+). No quiet trade onto a square an extra enemy piece attacks (g8 20...Bf5?? Nxf5).
5. Pinned knight (Ba4-d7-e8): moving it loses the exchange (g15 17...Nb6? 18.Bxe8!). A moving Q/B/R stops defending - check its old squares (g13 25.Qxh6?? left Bc2; g17 12...Qd6?? left d4 -> 13.Qxd4! + Qxg7#).
6. Mate nets: king c1 + d2 blocked -> ...Qa1# (g6). Ng5+Qf6 vs king f8 -> Qxf7# (g12). King g1/h2 + enemy rook rank 1 -> ...Qf2# (g10); Qg2 backed by Bb7 -> ...Qxg2# (g13; Nf1 does not guard g2). Back rank king g8, f8/h8 uncovered -> Re8#/Rd8# (g14, g16 41.Rd8#). Battery: enemy Qd4+Bb2, king g8, e5/f6 empty -> Qxg7# (g17 m14; f7/h7 box the king, g7 guarded only by the king).
7. After checks re-scan; the threat may remain (g6 14.Nxe7+ Bxe7).
8. Loose pieces: my undefended pieces + enemy queen/rook/knight lines (g8 26...Qd7?? Qxb6; g5 Qd2?? Nb3). King-only defense fails vs a queen (g12 25...Nh7??).
9. Piece en prise and hard to save: no queen counterattack that ignores it (g8 28...Qf5??; g15 25...Nc4 had no home). If a trade is declined, take it or retreat to a safe square (g11 25...Bf5?? Nxf5).
10. Pawn kicks: never push an undefended pawn to hit a defended piece (g12 19...h6?? Bxh6); never push onto a square an enemy knight attacks (g16 21...f5?? Nxf5).
11. Legality: clear path, knight geometry, piece exists (g11 9...Nf6; g14 13...Bf5/...Bb7 blocked; g16 20...f5 with Nf6) - illegal tries waste clock.

## Blunder catalogue (every loss ended here)
g1 12...Nxb2?? Bxb2 | g2 16.a3?? ...Nxc2 | g3 14...Bxd4??, 15...Ne4??, 19...Qxe4?? | g4 8...Bxd2??, 10...Nf4??, 12...Qxe5??, 13...Re8?? Qxe8# | g5 26.Qd2?? Nb3 | g6 15.e5?? Qa1# | g7 22...Nf6?? exf6, 35...Rxb2?? | g8 20...Bf5??, 26...Qd7??, 28...Qf5?? | g9 23.Qxc3??, 24.Rc1?? | g10 24.Qc2?? Rxc2 | g11 10...Bxc3??, 25...Bf5??, 26...Qxb4?? | g12 19...h6??, 25...Nh7??, 29...Qxd5??, m34 | g13 25.Qxh6??, 26.Qh8+??, m29 | g14 17...Qe1+?? Rxe1, 19.Re8# | g15 16...c5?!+17...Nb6? 18.Bxe8, 19...Bxd5??, 23...Qxe5??, m34 | g16 18...Nc4??, 26...Nxe4??, 27...Bxd5??, 41.Rd8# | g17 12...Qd6?? (left d4) 13.Qxd4!, 13...Qxd5?? Qxg7#.

## Sibling patterns
- Queen safety: captures g9 c3, g10 c2, g11 b4, g12 d5, g15 e5; g17 d5 (mate ignored); checks g13 h8, g14 e1. List attackers first: PAWNS, KING, rooks/queens on lines.
- Queen leaves a duty: Qf6 defended d4 -> 12...Qd6?? (g17); Qd2 guarded c2 -> 25.Qxh6?? (g13). Name the squares the queen covers before moving it.
- Battery mate: Bb2+Qd4 (queen on the b2-g7 diagonal) vs king g8 with e5/f6 empty -> Qxg7#; keep e5/f6 occupied or g7 defended (g17).
- Pinned knight behind a bishop drops the exchange (g15 d7). Bishop takes a defended pawn = B for P (g4 d2, g11 c3, g15 d5).
- King-only defender loses to Q/R/N (g12 h7, g17 g7).
- Long thinks never prevented a blunder; the 5s scan is the fix. After a blunder: defend loose pieces, trade down, no panic captures, play fast.
