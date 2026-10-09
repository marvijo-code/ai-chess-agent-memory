# Pre-move scan & blunder catalogue (g1-g23)

## Scan (EVERY move, 5s) - on the FINAL move, not the plan (g21: noted Nb4 attacks d3, then played 15.Bd3??)
1. Destination: which enemy PAWNS, KNIGHTS, KING attack it? Attacked+undefended -> reject. Pawn magnets: e5->d6/f6; d5->c6/e6; c3->b4/d4; b3->a4/c4; b5->a4/c4; c4->b3/d3; g6->f5/h5. Knight magnets: b4->a2/c2/d3/d5; b3->a1/c1/d2/d4/a5/c5 (g23 20.Bd2?? Nxa1); d4->b3/c2/e2/f3/f5/b5/c6/e6; e4->d2/f2/c3/g3/c5/f6; c6->a5/a7/b4/b8/d4/d8/e5/e7 (NOT d7); b8->a6/c6/d7 only if no enemy Q/B (g20 11...Nd7?? Qxd7).
2. Knight captures: a knight taking a defended pawn/square is N for P - count recapturers (g19 18...Nd7?! dxc6; g22 26.Nxd6?? Qxd6; g23 38.Nxe5?? dxe5). Never.
3. Queen/rook moves: list ALL attackers - pawns, knights, KING, sliders incl. rooks on the target's FILE (g22 31.Qxc4?? Rc8xc4). Defended is not enough: reject Q for B/N/P (g18 23.Qd5?? Bxd5). d5 is a queen trap (g12/g17/g18/g19). Queen leaves a duty: name the squares it covered (g17 12...Qd6?? left d4 -> 13.Qxd4!).
4. Knight forks: cover BOTH attacked units or vacate one (g23 19...Nb3 forked Ra1+Bc1, both loose - save the rook). Never move a piece onto a forker's square: g23 20.Bd2?? (b3-knight attacks d2) and 20...Nxa1 won a rook.
5. Pinned knight (Ba4-d7-e8): moving it loses the exchange (g15); unpin ...Rb8.
6. Mate nets: king c1+d2 blocked -> ...Qa1# (g6); king f8 vs Ng5+Qf6 -> Qxf7# (g12); king g1/h2 + enemy rook rank 1 -> ...Qf2# (g10); king g8/h8, f7/g7/h7, 8th rank open -> ...Re8#/...Qc8# (g14,g16,g19,g20); king h1, own g2, rook rank 1 + queen on h2 -> ...Rb1# (g21).
7. Loose pieces: my undefended units + enemy Q/R/N lines (g8 26...Qd7?? Qxb6); declined trade -> take or retreat safe (g11 25...Bf5?? Nxf5).
8. Pawn pushes: never undefended onto a defended piece (g12 19...h6?? Bxh6), onto a knight-attacked square (g16 21...f5?? Nxf5), or where the queen takes with tempo (g19 24...b3?? Qxb3+).
9. Pawn grabs: no rook grab of a pawn a rook/queen recaptures (g18 25.Rxe5 Rxe5); no bishop grab of a twice-defended pawn (g23 21.Bxa5?? Rxa5 = B for P); while down material, no pawn grabs at all.
10. Enemy pawn attacks a knight -> MOVE it (g19 18...Nd7?! 19.dxc6 = N for P).
11. Legality: path, knight geometry (c6 not d7), own piece blocks (g23 Be3 blocked by Nd2). Illegal tries waste clock.
12. Closed RL: keep the dark bishop (g13,g18).

## Blunder catalogue (all losses)
g1 12...Nxb2?? | g2 16.a3?? Nxc2 | g3 14...Bxd4??, 19...Qxe4?? | g4 8...Bxd2??, 13...Re8?? Qxe8# | g5 26.Qd2?? Nb3 | g6 15.e5?? Qa1# | g8 20...Bf5??, 26...Qd7?? | g10 24.Qc2?? Rxc2 | g11 25...Bf5??, 26...Qxb4?? | g12 19...h6??, 25...Nh7??, 29...Qxd5?? | g13 25.Qxh6??, 26.Qh8+?? | g14 17...Qe1+?? Rxe1 | g15 17...Nb6?, 19...Bxd5?? | g16 18...Nc4??, 26...Nxe4?? | g17 12...Qd6?? | g18 23.Qd5?? Bxd5, 25.Rxe5 Rxe5 | g19 18...Nd7?!, 24...b3??, 28...Qxd5??, 33...Rc8?? | g20 11...Nd7?? | g21 15.Bd3??, 18.Nc4??, 22.Qb3??, 29...Rb1# | g22 23.Nef5??, 26.Nxd6??, 31.Qxc4?? | g23 19.Ng3??/...Nb3!, 20.Bd2?? Nxa1, 21.Bxa5?? Rxa5, 38.Nxe5?? dxe5.

## Patterns
- Queen: d5 trap; leaving a duty; rooks on the capture file.
- Magnet squares: piece/queen onto enemy N/P attack (g16 c4, g21 d3/c4/b3, g22 f5, g23 d2).
- Knight N-for-P: g19, g22 x2, g23 x2.
- Knight forks b3/b4: cover both targets; never step onto the forker's square (g23).
- Back rank: king with no luft, enemy Q/R reaches it (g14,g16,g19,g21).
- Long thinks never prevented a blunder; the 5s scan is the fix (g22 40-60s/move, 3 blunders; g23 43-68s, 2 blunders). After a blunder: defend loose pieces, trade down, play fast.
