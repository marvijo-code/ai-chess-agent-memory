# Pre-move scan & blunder catalogue (g1-g12)

## Scan (EVERY move, not only captures)
1. Destination: list enemy PAWNS and KNIGHTS attacking it; attacked + undefended -> reject. Pawn magnets: e5/d6/f6, d5/c6/e6, c3/b4/d4. Knight magnets: g3->f5 h5 e4 e2 f1 h1; c5->b3 d3 e4 a4; b4->c2 d3 a2; e4->d2 f2 c3 g3 c5 f6; d4->b3 c2 e2 f3 f5 b5 c6 e6. d5-knight reaches c7 e7 b6 f6 b4 f4 c3 e3 only - never d2.
2. Queen captures: list defenders of the target INCLUDING pawns. g12 29...Qxd5?? exd5 = Q for P (e4-pawn defends d5) - I thought it was a queen trade; the e4-pawn is the only recapturer and it takes MY queen. g11 26...Qxb4?? cxb4 (c3-pawn). g9 23.Qxc3?? Qxc3. Rule: no queen capture unless every defender is equal or absent.
3. Open file/line: never my queen or rook on a square an enemy rook/queen attacks along that line, even if defended - Q for R loses (g10 24.Qc2?? Rxc2; g9 24.Rc1?? Qxc1+). No quiet trade onto a square an extra enemy piece attacks (g8 20...Bf5?? Nxf5).
4. Mate net: king c1 + d2 blocked -> ...Qa1# (free d2/guard a1 NOW; g6). Enemy Ng5 + Qf6 vs my king on f8 -> Qxf7# (f7 defended only by the king; g12 m34; defense Re7). King g1/h2 + enemy rook on rank 1 -> ...Qf2# (g10).
5. After checks: re-scan; the threat may remain (g6 14.Nxe7+ Bxe7 - f6-bishop recaptures).
6. Loose-piece scan: my undefended pieces + enemy lines to them (g8 26...Qd7?? Qxb6; g5 Qd2?? Nb3 fork).
7. Never put a piece - above all the queen - on a square an enemy knight attacks (g5, g8 Qf5/Bf5 vs Ng3/Nd4).
8. Piece en prise and hard to save: no queen counterattack that ignores it (g8 28...Qf5??). A knight on the edge 'defended by the king' is NOT defended when the enemy queen covers that square: g12 25...Nh7?? attacked defended Ng5 (Qh4 guards it); 26.Nxh7 wins, Kxh7 illegal. If a trade is declined, take it or retreat to a safe square (g11 25...Bf5?? Nxf5).
9. Pawn kicks: never push an undefended pawn to hit a defended piece (g12 19...h6?? Bxh6, Qd2 defended the bishop) - it just loses the pawn.
10. Attacking the queen: verify she cannot capture my attacker (g9 24.Rc1?? Qxc1+).
11. Legality: path clear (Bc8-e6 needs d7 empty), knight geometry, piece exists. g11 9...Nf6: 3 tries, illegal Nxd2 + Be6; g10 illegal f4 try. Never 60-90s on one move.

## Blunder catalogue (every loss ended here)
- g1 12...Nxb2?? Bxb2 | g2 16.a3?? ...Nxc2 | g3 14...Bxd4??, 15...Ne4??, 19...Qxe4?? | g4 8...Bxd2??, 10...Nf4??, 12...Qxe5??, 13...Re8?? Qxe8# | g5 26.Qd2?? Nb3 fork | g6 15.e5?? Qa1# | g7 22...Nf6?? exf6, 35...Rxb2?? | g8 20...Bf5??, 26...Qd7??, 28...Qf5?? | g9 23.Qxc3??, 24.Rc1?? | g10 24.Qc2?? Rxc2 | g11 10...Bxc3?? B for P, 25...Bf5??, 26...Qxb4?? | g12 19...h6??, 25...Nh7??, 29...Qxd5?? Q for P, m34.

## Sibling patterns
- Open-file blindness: scan from the target square to the enemy back rank for rooks/queens (g9 c3, g10 c2) - a defender BEHIND is easiest to miss.
- Queen pawn-grabs: g9 c3, g10 c2, g11 b4, g12 d5 - check PAWN defenders of the target FIRST.
- Piece 'defended by the king' means nothing if an enemy queen/rook/knight covers the square (g12 h7).
- f5 magnet for enemy Ng3/Nd4; d2 vs Nb3; f6 vs e5-pawn; h6/h7 targets vs Qd2 + Bh6/Bg5 battery.
- Long thinks never prevented a blunder; the 5s scan is the fix.
- After a blunder: defend loose pieces, trade down, no panic captures, play fast.
