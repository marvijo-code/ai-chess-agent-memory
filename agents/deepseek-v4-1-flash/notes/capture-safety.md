# Pre-move scan & blunder catalogue (g1-g11)

## Scan (EVERY move, not only captures)
1. Destination: list enemy PAWNS and KNIGHTS attacking it; attacked + undefended -> reject. Pawn magnets: e5/d6/f6, d5/c6/e6, c3/b4/d4. Knight magnets: g3->f5 h5 e4 e2 f1 h1; c5->b3 d3 e4 a4; b4->c2 d3 a2; e4->d2 f2 c3 g3 c5 f6; d4->b3 c2 e2 f3 f5 b5 c6 e6 (g11 25...Bf5?? Nxf5). d5-knight reaches c7 e7 b6 f6 b4 f4 c3 e3 only - never d2.
2. Enemy rook/queen on an open file/rank/diagonal: never put my queen or rook on a square it attacks along that line, even if defended - Q for R loses. g10 24.Qc2?? Rxc2 (Rc8 on the open c-file; Bxc2 recapture). g9 24.Rc1?? Qxc1+. No quiet trade onto a square an extra enemy piece attacks (g8 20...Bf5?? Nxf5).
3. Captures/grabs: list EVERY recapturer - pawns AND pieces on open lines to the target. g9 23.Qxc3?? Qxc3 (Q for N; Qc7 on the open c-file). g11 10...Bxc3?? dxc3 = B for P: c3 is defended by b2+d2, and Bxc3 bxc3 wins a pawn is WRONG - bxc3 takes the bishop. g11 26...Qxb4?? cxb4 = Q for P (b4 defended by the c3-pawn). Never piece for pawn, never Q for N/B/P. b2/c2/b4 grabs chronic (g1, g2, g7).
4. Mate net: king c1 + d2 blocked -> ...Qa1#; free d2 (Qe3/Qd3) or guard a1 (Qc1) NOW, no quiet move (g6). King g1/h2 + enemy rook on rank 1 -> ...Qf2# (g10 32).
5. After checks: re-scan; the threat may remain (g6 14.Nxe7+ Bxe7 - the f6-bishop recaptures).
6. Loose-piece scan: my undefended pieces + enemy lines to them (g8 26...Qd7?? Qxb6; 28...Qf5?? left Rc7).
7. Never put a piece - above all the queen - on a square an enemy knight attacks (g5 Qd2?? Nb3 fork; g8/g11 Qf5/Bf5 vs Ng3/Nd4).
8. Piece en prise and hard to save: no queen counterattack that ignores it (g8 28...Qf5??). If my attacked piece's trade is declined, take it myself or retreat to a square no pawn/knight attacks (g11 24...Bd3 25.Bf1 25...Bf5?? Nxf5).
9. Attacking the queen: verify she cannot capture my attacker (g9 24.Rc1?? Qxc1+; my own Bb1 blocked the a1-rook).
10. Legality: path clear (Bc8-e6 needs d7 empty - play ...d6 first), knight geometry, enemy target, piece exists. g11 9...Nf6: 3 tries, illegal Nxd2 + Be6; g10 illegal f4 try. Never 60-90s on one move.

## Blunder catalogue (every loss ended here)
- g1 12...Nxb2?? Bxb2 | g2 16.a3?? ...Nxc2 (Q for N) | g3 14...Bxd4??, 15...Ne4??, 19...Qxe4?? | g4 8...Bxd2??, 10...Nf4??, 12...Qxe5??, 13...Re8?? Qxe8# | g5 26.Qd2?? Nb3 fork; 27.Qxa5?? | g6 14.Nxe7+?!/15.e5?? Qa1# | g7 22...Nf6?? exf6, 35...Rxb2?? | g8 20...Bf5??, 26...Qd7??, 28...Qf5?? | g9 23.Qxc3??, 24.Rc1?? | g10 24.Qc2?? Rxc2 (m32) | g11 10...Bxc3?? B for P (+0.1->+7.4), 25...Bf5??, 26...Qxb4?? (m36).

## Sibling patterns
- Open-file blindness: scan from the target square to the enemy back rank for rooks/queens (g9 c3, g10 c2); a defender BEHIND is easiest to miss.
- Pawn-grab blindness: check the square's pawn defenders first (g4 Bxd2 vs Qd1; g11 Qxb4 vs c3-pawn).
- f5 is a magnet for an enemy Ng3/Nd4; d2 vs Nb3; f6 vs an e5-pawn.
- Long thinks never prevented the blunder; the 5s scan is the fix.
- After a blunder: defend loose pieces, trade down, no panic captures (not Qxb4-style grabs), play fast.
