# Pre-move scan & blunder catalogue (g1-g9)

## Scan (EVERY move, not only captures)
1. Destination: list enemy PAWNS and pieces (KNIGHTS!) attacking it; attacked + undefended -> reject. Pawn magnets: e5 hits d6/f6; d5 hits c6/e6. Knight magnets: g3 hits f5/h5/e4/e2/f1/h1; c5 hits b3/d3/e4/a4; b4 hits c2/d3/a2; e4 hits d2/f2/c3/g3/c5/f6.
2. "Trade" offers: a quiet move like ...Bf5 hoping Bxf5 is a gift if the destination is attacked by another enemy piece and is undefended. g8 20...Bf5?? Nxf5; g8 28...Qf5?? Nxf5 = queen for knight.
3. Captures/grabs: list EVERY recapturer/defender - pawns AND queens/rooks/bishops on open files/ranks/diagonals to the target square. g9 23.Qxc3?? Qxc3: the c3-knight was defended by Qc7 down the wide-open c-file (c-pawn traded on 13.cxd4) -> queen for knight. Never piece for one pawn or queen for N/B/P. b2/c2 grabs are a chronic killer: g1 12...Nxb2?? Bxb2; g2 16.a3?? ...Nxc2; g7 35...Rxb2?? Rxb2. My checks: g6 14.Nxe7+ was knight-for-pawn.
4. Mate net: enemy queen/rook/bishop lines to my king's entry squares. King c1 + Rd1 + Qd2 + b2/c2 pawns = ...Qa1#. Black queen on a1/a2/b2 -> free d2 or guard a1 (Qc1) NOW; no quiet move first (g6 13...Qxa2! 15.e5?? Qa1#).
5. After my check: re-scan; the threat may still be there (g6 14.Nxe7+ Bxe7).
6. Loose-piece scan: list MY undefended pieces and enemy queen/bishop/rook/knight lines to them. g8 26...Qd7?? Qxb6 (queen hits b6 via c5). g8 28...Qf5?? left Rc7 (attacked by Qb6+Rc1) hanging -> 30.Rxc7.
7. Knight-fork/attack scan: never move the queen onto a square any enemy knight attacks (g5 Qd2?? ...Nb3 fork Qd2+Ra1; g8 28...Qf5?? Nxf5. Nb3 hits a1+d2; Nc2 hits a1+e1; Ng3 hits f5).
8. My piece en prise and hard to save: make a bigger threat; a queen "counterattack" that ignores it loses both (g8 28...Qf5??).
9. Attacking an enemy queen: verify she cannot capture my attacker in the same line. g9 24.Rc1?? Qxc1+ took the rook with check, and the a1-rook could not recapture (own Bb1 on b1).
10. Legality: own pieces must not block the path; target must hold an ENEMY piece; the moving piece must still exist (g9 tried Rc1 after that rook was captured). g8 illegal tries Bf6xe3, Qd7xb6; verify geometry before committing.

## Blunder catalogue (every loss ended here)
- g1 Black RL: 12...Nxb2?? Bxb2 (knight for pawn).
- g2 White RL: 16.a3?? ...Nxc2 17.Qxc2 Qxc2 (queen for knight).
- g3 Black 4N: 14...Bxd4?? cxd4; 15...Ne4?? Bxe4; 19...Qxe4?? Rxe4.
- g4 Black 4N: 8...Bxd2?? Qxd2; 10...Nf4?? Qxf4; 12...Qxe5?? Qxe5; 13...Re8?? Qxe8#.
- g5 White RL: 21.Qd2?/22.Qc3?? shuffles; 26.Qd2?? ...Nb3 fork; 27.Qxa5?? Rxa5.
- g6 White Dragon: 13.Nd5?! ...Qxa2!; 14.Nxe7+?! knight for pawn; 15.e5?? Qa1#.
- g7 Black RL: 22...Nf6??/24...Nf6?? 25.exf6; 29...Qb6??; 35...Rxb2?? Rxb2.
- g8 Black RL: 20...Bf5?? Nxf5; 26...Qd7?? Qxb6; 28...Qf5?? Nxf5 + Rc7 fell.
- g9 White RL: 23.Qxc3?? Qxc3 (queen for knight; Qc7 behind on the open c-file); 24.Rc1?? Qxc1+ (rook too).

## Sibling patterns
- A piece on a square an enemy knight hits is a recurring killer: f5 vs Ng3 (g8), d2 vs Nb3 (g5), f6 vs e5-pawn (g7).
- A defender BEHIND on the same open file is the easiest to miss: Qc7 defends c3 (g9). Scan file/rank/diagonal from the target to the enemy back rank, not just neighbours.
- Long thinks never prevented the blunder: g5-g8 30-50s, g9 38-50s. The 5s scan is the fix, not the clock.
- After a blunder: defend loose pieces, trade down, no panic captures, play fast.
