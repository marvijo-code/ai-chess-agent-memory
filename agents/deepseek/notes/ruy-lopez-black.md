# Ruy Lopez Closed - Black (Chigorin/Breyer)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3. Also 6.d4 exd4 7.Re1 (open centre, g97).

## Setup
...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then Chigorin ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8; Breyer ...Nb8/...Nbd7/...Re8/...Bf8/...g6. After 9.h3 no ...Bg4 pin.

## g97 vs SF19 (0-1, Qxe8# m19) - Ruy 6.d4 exd4 7.Re1
9.a4 b4 10.e5! Nxe5? 11.Nxe5 d6?! 12.Nc6! Qd7?? 13.Nxe7+! Qxe7?? 14.Rxe7 (Q for N, his Re1 owns the open e-file).
- 10...Nxe5? (c6-knight) vacates c6 and opens the e-file: his knight lands on e5 with Re1 support; 11...d6? 12.Nc6! hits Qd8+Be7. Meet 10.e5 with ...Ne8/...Nd5 (keep f6) then ...d6. NEVER take on e5.
- 12...Qd7?? (also Qe8) loses the QUEEN to the e-file x-ray; 12...Qc8 only loses B+B for N. So 11...d6?! was already the losing step.
- Clock: 28-41 s routine, Qd7 39 s; ended 10:44 vs 18:09. Routine <=15 s.

## g41 vs Sonnet 5.5 (0-1, m24) - Chigorin; queen-tempo blunder
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Bb7 14.Nb3 Rac8 15.Nxa5 Qxa5 16.Bd2 Rfd8?? 17.Bxa5 Bxe4 18.Bxe4 Nxe4 19.Rxe4 Bf6 20.Bxd8 Bxd8 21.dxe5 dxe5 22.Nxe5 Bf6 23.Qd7 Rc7 24.Qe8#.
- Through 15...Qxa5 EQUAL (SF's only Black mark: 16...Rfd8??). 16.Bd2 ATTACKS Qa5 (d2-c3-b4-a5). Queen must retreat FIRST: ...Qd8/...Qc7/...Qb6/...Qa6 (a4 is covered by Bc2, b4 by Bd2). 16...Rfd8?? ignored the tempo; 17.Bxa5 won the queen (Sonnet took in 8s).
- Lesson: whenever any of his pieces moves onto a line to my queen, move the queen THAT move - no rook/developing move first.
- Clock (g41): 22-59 s thinks, blunder on a 43 s move; ended 7:45 vs 16:16.

## Qc7 safety (recurring: g35, g38)
His Be3+Rc1 on the c-file: Qc7 is a tempo target; 'defended' by Rc8 is still Rxc7 = R for Q. RETREAT ...Qb8/...Qd8 the move the file opens or earlier. Never a piece move that leaves the queen on c7 (g38 18...Nc4?? 19.Bb3! Nb6?? 20.Rxc7). ...Nc4 only when Bb3 cannot come with tempo on the knight (never ...Nc4 once White has b3, g16). Count ALL recapturers incl. bishops (g35 18.Rc1! Qxc1?? 19.Bxc1).

## g40 vs Sonnet 5.5 (0-1, Qxh7# m23)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 Bb7 13.Nf1 Rac8 14.Ng3 Nd7? 15.d5 c4 16.Nf5 Nc5 17.Bg5 Bxg5! 18.Nxg5 b4? 19.cxb4 Nxe4?? 20.Bxe4 Nc6?? 21.dxc6 Bxc6 22.Qh5 Qd7?? 23.Qxh7#.
- Normal to 13...Rac8. 14...Nd7? (SF ?): his Ng3 heads to f5 and 15.d5 locks the centre - Bb7 dead, knights no squares. Resolve the centre (...cxd4) or reroute ...Nc6/...Nb6 + ...Rfd8 BEFORE d5.
- 18...b4? 19.cxb4 hit BOTH Na5 and Nc5; play ...g6 (guards h7, hits Nf5) or ...Rcd8/...Qd8 first.
- 19...Nxe4?? e4 was undefended = N for nothing; 20...Nc6?? 21.dxc6. When down: defend, trade, no knight to an undefended/pawn-attacked square.
- 22.Qh5 threatened Qxh7# (Ng5 guards h7); needed ...g6 earlier. 22...Qd7?? 23.Qxh7#.

## Plans/traps
- ...c5 hits d4; dxc5 dxc5 may trade queens on d8. Na5-c4 hits e3/d2; ...Nxb2?? with Bc1 loses a knight.
- Keep f7 covered; NEVER a piece on a square a White knight attacks (g8 20...Bf5?? Nxf5).
- White's d5 break: c6-knight hit -> ...Ne7/...Nb8/...Na5; Bb7 then dead behind d5, ...Bc8 blocks ...Rac8 (g38).
- His Nf5/Ng5 + Qh5 hit h7: play ...g6 early.

## Older - condensed
- g35: 18.Rc1! Qxc1?? 19.Bxc1 = Q for R+B; 15...Rfe8?! flagged.
- g19: 18.d5 hit Nc6; 28...Qxd5?? Bxd5; 33...Rc8?? Qxc8#.
- g15 Breyer: Ba4 pins Nd7/Re8; ...Nb6? Bxe8 (unpin ...Rb8); 19...Bxd5?? exd5; 23...Qxe5?? = Q for N.
- g12: 19...h6?? 20.Bxh6; 25...Nh7??; 33...Kf8?? Qxf7#.
- g7/g8: 24...Nf6?? exf6; 20...Bf5?? Nxf5; 36-90s thinks did not help.
