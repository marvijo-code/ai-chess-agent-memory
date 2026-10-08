# Pre-move scan & blunder catalogue (g1-g18)

## Scan (EVERY move, 5s)
1. Destination: do enemy PAWNS, KNIGHTS or the KING attack it now? Attacked + undefended -> reject. Pawn magnets: e5->d6/f6; d5->c6/e6; c3->b4/d4; b3->a4/c4 (g16 18...Nc4?? bxc4 = N for P); a2->b3. Knight magnets: see MEMORY.md.
2. Queen/rook moves: list ALL attackers of the destination - pawns, knights, KING, rooks/queens on lines, BISHOPS/queens on diagonals. Defended is not enough: reject if the trade is Q for B/N/P (g18 23.Qd5?? Bb7xd5 = Q for B; g10 24.Qc2?? Rxc2; g9 24.Rc1?? Qxc1+; g13 26.Qh8+?? Kxh8; g14 17...Qe1+?? Rxe1).
3. Queen captures: list defenders INCLUDING pawns (g12 29...Qxd5??; g11 26...Qxb4??; g15 23...Qxe5??; g17 13...Qxd5?? mate ignored). No grab unless the trade is favorable AND no enemy mate/battery exists.
4. Queen leaves a duty: name the squares it covered (g13 25.Qxh6?? left Bc2; g17 12...Qd6?? left d4 -> 13.Qxd4! + Qxg7#). Enemy moves can restore a defense - recheck after every enemy move (g16 26...Nxe4?? Re1 re-covered e4).
5. Pinned knight (Ba4-d7-e8): moving it loses the exchange (g15 17...Nb6? 18.Bxe8!). Unpin with ...Rb8.
6. Mate nets: king c1 + d2 blocked -> ...Qa1# (g6). Ng5+Qf6 vs king f8 -> Qxf7# (g12). King g1/h2 + enemy rook rank 1 -> ...Qf2# (g10); Qg2 backed by Bb7 -> ...Qxg2# (g13). Back rank king g8, f8/h8 uncovered -> Re8#/Rd8# (g14, g16). Battery Qd4+Bb2 vs king g8, e5/f6 empty -> Qxg7# (g17).
7. After checks re-scan; the threat may remain (g6).
8. Loose pieces: my undefended pieces + enemy queen/rook/knight lines (g8 26...Qd7?? Qxb6). King-only defense fails vs a queen (g12 25...Nh7??).
9. Piece en prise: no counterattack that ignores it (g8 28...Qf5??; g15 25...Nc4). If a trade is declined, take it or retreat to a safe square (g11 25...Bf5?? Nxf5).
10. Pawn kicks: never push an undefended pawn to hit a defended piece (g12 19...h6?? Bxh6); never push onto a square an enemy knight attacks (g16 21...f5?? Nxf5).
11. No major-piece grab of a pawn a rook/queen recaptures (g18 25.Rxe5 Rxe5 = R for P).
12. Legality: path, knight geometry, own piece blocks (g16 20...f5 with Nf6). Illegal tries waste clock (g18: 4 tries).
13. Closed RL: keep the dark bishop - Bxf6/Bxc5 gives Black the bishop pair (g13, g18).

## Blunder catalogue (every loss ended here)
g1 12...Nxb2?? Bxb2 | g2 16.a3?? ...Nxc2 | g3 14...Bxd4??, 15...Ne4??, 19...Qxe4?? | g4 8...Bxd2??, 10...Nf4??, 12...Qxe5??, 13...Re8?? Qxe8# | g5 26.Qd2?? Nb3 | g6 15.e5?? Qa1# | g7 22...Nf6?? exf6, 35...Rxb2?? | g8 20...Bf5??, 26...Qd7??, 28...Qf5?? | g9 23.Qxc3??, 24.Rc1?? | g10 24.Qc2?? Rxc2 | g11 10...Bxc3??, 25...Bf5??, 26...Qxb4?? | g12 19...h6??, 25...Nh7??, 29...Qxd5?? | g13 21.Bxf6?!, 25.Qxh6??, 26.Qh8+?? | g14 17...Qe1+?? Rxe1, 19.Re8# | g15 16...c5?! 17...Nb6? 18.Bxe8, 19...Bxd5??, 23...Qxe5?? | g16 18...Nc4??, 26...Nxe4??, 27...Bxd5??, 41.Rd8# | g17 12...Qd6?? 13.Qxd4!, 13...Qxd5?? Qxg7# | g18 21.Bxc5?!, 23.Qd5?? Bxd5 = Q for B, 25.Rxe5 Rxe5 = R for P.

## Sibling patterns
- Queen safety: g9 c3, g10 c2, g11 b4, g12 d5, g15 e5, g17 d5, g18 d5 (bishop!). List attackers first: PAWNS, KING, rooks/queens on lines, BISHOPS/queens on diagonals.
- Queen leaves a duty (g13 c2, g17 d4). Battery mate Bb2+Qd4 vs king g8: keep e5/f6 occupied or g7 defended (g17).
- Pinned knight behind a bishop drops the exchange (g15). King-only defense loses to Q/R/N (g12, g17).
- Long thinks never prevented a blunder; the 5s scan is the fix. After a blunder: defend loose pieces, trade down, no panic captures, play fast.
