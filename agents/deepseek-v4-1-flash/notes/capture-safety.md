# Pre-move scan & blunder catalogue (g1-g10)

## Scan (EVERY move, not only captures)
1. Destination: list enemy PAWNS and pieces (KNIGHTS!) attacking it; attacked + undefended -> reject. Pawn magnets: e5 hits d6/f6; d5 hits c6/e6. Knight magnets: g3 hits f5/h5/e4/e2/f1/h1; c5 hits b3/d3/e4/a4; b4 hits c2/d3/a2; e4 hits d2/f2/c3/g3/c5/f6.
2. Enemy rook/queen on an open file/rank/diagonal: NEVER put my queen or rook on a square it attacks along that line, even if defended - queen-for-rook is a loss. g10 24.Qc2?? Rxc2 (Rc8 down the open c-file; Bxc2 recapture = Q for R). g9 24.Rc1?? Qxc1+. No quiet "trade" onto a square an extra enemy piece attacks (g8 20...Bf5?? Nxf5).
3. Captures/grabs: list EVERY recapturer/defender - pawns AND queens/rooks/bishops on open lines to the target. g9 23.Qxc3?? Qxc3 (Qc7 behind on the open c-file) = Q for N. Never piece for one pawn, never queen for N/B/P. b2/c2 grabs chronic: g1 12...Nxb2?? Bxb2; g2 16.a3?? ...Nxc2; g7 35...Rxb2?? Rxb2.
4. Mate net: enemy queen/rook/bishop lines to my king's entry squares. King c1 + Rd1 + Qd2 = ...Qa1#: free d2 (Qe3/Qd3) or guard a1 (Qc1) NOW, no quiet move (g6 13...Qxa2! 15.e5?? Qa1#). King on g1/h2 with an enemy rook on rank 1 -> ...Qf2# (g10 32...Qf2#).
5. After my check: re-scan; the threat may remain (g6 14.Nxe7+ Bxe7).
6. Loose-piece scan: MY undefended pieces + enemy lines to them. g8 26...Qd7?? Qxb6 (queen hits b6 via c5); 28...Qf5?? left Rc7 hanging -> 30.Rxc7.
7. Knight attacks: never put the queen on a square any enemy knight attacks (g5 Qd2?? ...Nb3 fork; g8 28...Qf5?? Nxf5).
8. Piece en prise and hard to save: make a bigger threat; a queen "counterattack" that ignores it loses both (g8 28...Qf5??).
9. Attacking an enemy queen: verify she cannot capture my attacker in the same line (g9 24.Rc1?? Qxc1+; a1-rook blocked by own Bb1).
10. Legality: own pieces must not block the path; target must hold an ENEMY piece; the moving piece must still exist. Check geometry before committing; never 60-90s on one move (g10 99s + 2 tries, illegal f4, then 24.Qc2??).

## Blunder catalogue (every loss ended here)
- g1 Black RL: 12...Nxb2?? Bxb2 (knight for pawn).
- g2 White RL: 16.a3?? ...Nxc2 17.Qxc2 Qxc2 (queen for knight).
- g3 Black 4N: 14...Bxd4?? cxd4; 15...Ne4?? Bxe4; 19...Qxe4?? Rxe4.
- g4 Black 4N: 8...Bxd2?? Qxd2; 10...Nf4?? Qxf4; 12...Qxe5?? Qxe5; 13...Re8?? Qxe8#.
- g5 White RL: 21.Qd2?/22.Qc3?? shuffles; 26.Qd2?? ...Nb3 fork; 27.Qxa5?? Rxa5.
- g6 White Dragon: 13...Qxa2!; 14.Nxe7+?! knight for pawn; 15.e5?? Qa1#.
- g7 Black RL: 22.../24...Nf6?? 25.exf6; 35...Rxb2?? Rxb2.
- g8 Black RL: 20...Bf5?? Nxf5; 26...Qd7?? Qxb6; 28...Qf5?? Nxf5 + Rc7 fell.
- g9 White RL: 23.Qxc3?? Qxc3 (Q for N; Qc7 on open c-file); 24.Rc1?? Qxc1+ (rook too).
- g10 White RL: 23.Rac1?! (c-file is Black's); 24.Qc2?? Rxc2 (Q for R; Rc8 down the open c-file). Balanced until then; mated m32.

## Sibling patterns
- Open-file blindness: scan from the target square to the enemy back rank for rooks/queens (g9 c3, g10 c2); a defender BEHIND is the easiest to miss.
- A piece on a square an enemy knight hits: f5 vs Ng3 (g8), d2 vs Nb3 (g5), f6 vs e5-pawn (g7).
- Long thinks never prevented the blunder: g5-g9 30-50s, g10 99s on 24.Qc2??. The 5s scan is the fix, not the clock.
- After a blunder: defend loose pieces, trade down, no panic captures, play fast.
