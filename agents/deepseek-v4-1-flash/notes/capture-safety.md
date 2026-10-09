# Pre-move scan & blunder catalogue (g1-g26)

## Scan (EVERY move, 5s) - on the FINAL move, not the plan
1. Destination: which enemy PAWN, KNIGHT, BISHOP, KING, QUEEN attacks it? Attacked+undefended -> reject. Pawn magnets: h3->g4 (g24), f3->g4/e4, e5->d6/f6, d5->c6/e6, c3->b4/d4, b3->a4/c4, b5->a4/c4, c4->b3/d3, g6->f5/h5. Knight magnets: b4->a2/c2/d3/d5; b3->a1/c1/d2/d4/a5/c5 (g23 20.Bd2?? Nxa1); d4->b3/c2/e2/f3/f5/c6/e6; e4->d2/f2/c3/g3/c5/f6; c6->a5/a7/b4/b8/d4/d8/e5/e7 (NOT d7). Lines: d3/c2-bishop hits g6+h7 (g25 14...Qg6?? Bxg6); his Qf5 hits d7 (g26 16...Qd7?? Qxd7); his Qf3 hits f5 up the file - no undefended piece there (g26 15...Bf5?? Qxf5).
2. Knight captures: never take a defended pawn/square with a knight - count recapturers (g19,g22,g23).
3. Queen/rook moves: list ALL attackers incl. rooks on the file (g22 31.Qxc4?? Rc8xc4). Defended is not enough: reject Q for B/N/P (g18 23.Qd5?? Bxd5; g25 14...Qg6?? Bxg6). d5 is a queen trap (g12,g17,g18,g19). Name the squares it leaves (g17 12...Qd6?? left d4).
4. A moving piece stops defending its old squares: fix them; re-scan after checks/forced moves and every enemy move (g16 26...Nxe4?? Re1 re-covered e4).
5. Knight forks: cover BOTH targets or vacate one (g23 19...Nb3 forked Ra1+Bc1); never step onto a forker's square (20.Bd2?? Nxa1).
6. Pinned knight (Ba4-d7-e8): moving it loses the exchange (g15); unpin ...Rb8.
7. Mate nets: c1 king + d2 blocked -> ...Qa1# (g6); his Qh5 + Bd3 covering h7 -> Qxh7+ wins (Kxh7 illegal), defend ...g6 not ...Qf6?? (g25); f8 king -> Qxf7# (g12); enemy rook rank 1 -> ...Qf2# (g10), ...Rb1# (g21); c8 king + Rf7 -> ...Qg8# (g24); king on the 8th with no luft -> Re8#/Qc8#/Qd8#/Qxe8# (g14,g16,g19,g20,g25,g26).
8. Pawn pushes: never undefended onto a defended piece (g12 ...h6??), onto a knight-attacked square (g16 ...f5??), onto an enemy pawn's attack (g24), onto a bishop's capture square (g25 10...d3?!), or where a queen takes with tempo (g19 ...b3??).
9. Pawn grabs: no rook grab of a pawn a rook/queen recaptures (g18); no bishop grab of a twice-defended pawn (g23); down material, no pawn grabs.
10. Enemy pawn attacks a knight -> MOVE it (g19 18...Nd7?! 19.dxc6).
11. 'Standard/thematic' is not a scan: check every plan move against actual pawns/queens (g24, g25, g26 ...Bf5).
12. Legality: path clear, own pieces block (c8-bishop behind d7-pawn: Be6/Bf5/Bg4 illegal before ...d6, g25), knight geometry.

## Blunder catalogue (all losses)
g1 12...Nxb2 | g2 16.a3 Nxc2 | g3 14...Bxd4, 19...Qxe4 | g4 8...Bxd2, 13...Re8 Qxe8# | g5 26.Qd2 Nb3 | g6 15.e5 Qa1# | g8 20...Bf5, 26...Qd7 | g10 24.Qc2 Rxc2 | g11 25...Bf5, 26...Qxb4 | g12 19...h6, 25...Nh7, 29...Qxd5 | g13 25.Qxh6, 26.Qh8+ | g14 17...Qe1+ Rxe1 | g15 17...Nb6, 19...Bxd5 | g16 18...Nc4, 26...Nxe4 | g17 12...Qd6 | g18 23.Qd5 Bxd5, 25.Rxe5 Rxe5 | g19 18...Nd7, 24...b3, 28...Qxd5, 33...Rc8 | g20 11...Nd7 | g21 15.Bd3, 18.Nc4, 22.Qb3, 29...Rb1# | g22 23.Nef5, 26.Nxd6, 31.Qxc4 | g23 19.Ng3, 20.Bd2 Nxa1, 21.Bxa5, 38.Nxe5 | g24 10...Bg4 hxg4 | g25 10...d3?!, 12...Qf6??, 14...Qg6?? | g26 15...Bf5?? Qxf5, 16...Qd7?? Qxd7.

## Patterns
- Queen: d5 trap; leaving a duty; rooks/bishops/queens on the capture line; my queen on a square his queen covers (g26 d7).
- Magnet squares: piece/queen onto an enemy N/P/B/Q attack (g16 c4, g21 d3, g22 f5, g23 d2, g24 g4, g25 g6, g26 f5/d7).
- Knight forks: b3/b4 forker - cover both targets; never step onto its square (g23).
- Back rank: king without luft, enemy Q/R arrives (g14,g16,g19,g20,g24,g25,g26).
- Long thinks never prevented a blunder; the 5s destination scan is the fix. Down material: trade, defend loose pieces, 5-15s moves.
