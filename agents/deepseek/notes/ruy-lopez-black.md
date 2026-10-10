# Ruy Lopez Closed - Black (Chigorin/Breyer)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 (Closed). Also 6.d4 exd4 7.Re1 (open centre: g97, g105).

## g105 vs SF19 (0-1, Qe5# m36) - OPEN Chigorin 9.Bd5! and two one-move hangs
6.d4 exd4 7.Re1 b5 8.Bb3 d6 9.Bd5! O-O?? 10.Bxc6 Bb7?? 11.Bxb7 Rb8 12.Bc6 Qd7?? 13.Bxd7.
- 9.Bd5 attacks the c6-knight AND a8 through b7 (b7 empty). Only 9...Nxd5! 10.exd5 =; any knight retreat loses Ra8 to Bxa8; 9...O-O?? just drops the knight (no pawn recaptures c6: b5 covers a4/c4, d6 covers c5/e5).
- 10...Bb7?? and 12...Qd7?? both land on the c6-bishop's rays (b7/a8, d7/e8): B then Q for nothing. My note wrote 'Bxb7 might just win a bishop - reconsider'. A named danger = self-ban.
- 2 illegal tries (bxc6 impossible; Rxe5 blocked by own Ne6): a rejection means recheck the board, don't guess the next move.
- Clock: 34-42 s on 6-12 book moves, ended 7:52 vs 20:59. Open Chigorin book <=10 s.

## g97 vs SF19 (0-1, Qxe8# m19) - Ruy 6.d4 exd4 7.Re1
9.a4 b4 10.e5! Nxe5? 11.Nxe5 d6?! 12.Nc6! Qd7? 13.Nxe7+! Qxe7?? 14.Rxe7 (Q for N, Re1 owns the open e-file).
- Meet 10.e5 with ...Ne8/...Nd5 (keep f6), then ...d6. NEVER take on e5: 10...Nxe5? vacates c6 and opens the e-file.
- 12...Qd7??/Qe8 lose the QUEEN to the e-file x-ray; 12...Qc8 only loses B+B for N. So 11...d6?! was the losing step.
- Clock: 28-41 s routine moves; routine <=15 s.

## g41 vs Sonnet (0-1, m24) - Chigorin; queen-tempo blunder
...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O ...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Bb7 14.Nb3 Rac8 15.Nxa5 Qxa5: EQUAL.
- 16.Bd2! hits Qa5 (d2-c3-b4-a5). 16...Rfd8?? 17.Bxa5 Bxe4 18.Bxe4 Nxe4 19.Rxe4 Bf6 20.Bxd8 Bxd8 21.dxe5 dxe5 22.Nxe5 Bf6 23.Qd7 Rc7 24.Qe8#.
- Whenever one of his moves lands on a line to my queen, she moves THAT move - no rook/developing move first.

## Qc7 safety (g35, g38)
His Be3+Rc1 on the c-file: Qc7 is a tempo target; 'defended' by Rc8 is still Rxc7 = R for Q. RETREAT ...Qb8/...Qd8 the move the file opens or earlier. Never a piece move leaving the queen on c7 (g38 18...Nc4?? 19.Bb3! Nb6?? 20.Rxc7). ...Nc4 only when Bb3 cannot come with tempo on the knight (never ...Nc4 once White has b3). Count ALL recapturers incl. bishops (g35 18.Rc1! Qxc1?? 19.Bxc1).

## g40 vs Sonnet (0-1, Qxh7# m23)
9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 Bb7 13.Nf1 Rac8 14.Ng3 Nd7? 15.d5 c4 16.Nf5 Nc5 17.Bg5 Bxg5! 18.Nxg5 b4? 19.cxb4 Nxe4?? 20.Bxe4 Nc6?? 21.dxc6 Bxc6 22.Qh5 Qd7?? 23.Qxh7#.
- 14...Nd7? ignores 15.d5 locking the centre (Bb7 dead, knights homeless): resolve the centre (...cxd4) or reroute ...Nc6/...Nb6 + ...Rfd8 first.
- 18...b4? 19.cxb4 hit Na5 and Nc5; play ...g6 or ...Rcd8/...Qd8 first. 19...Nxe4?? = N for nothing. 22.Qh5 threatened Qxh7# (Ng5 guards h7): needed ...g6 earlier.

## Plans/traps
- ...c5 hits d4; dxc5 dxc5 may trade queens on d8. Na5-c4 hits e3/d2; ...Nxb2?? with Bc1 loses a knight.
- Keep f7 covered; NEVER a piece on a square a White knight attacks (g8 20...Bf5?? Nxf5).
- White's d5 break: c6-knight hit -> ...Ne7/...Nb8/...Na5; Bb7 then dead behind d5, ...Bc8 blocks ...Rac8 (g38). His Nf5/Ng5 + Qh5 hit h7: play ...g6 early.

## Older - condensed
- g35: 18.Rc1! Qxc1?? 19.Bxc1 = Q for R+B.
- g19: 28...Qxd5?? Bxd5; 33...Rc8?? Qxc8#.
- g15 Breyer: Ba4 pins Nd7/Re8; ...Nb6? Bxe8 (unpin ...Rb8); 23...Qxe5?? = Q for N.
- g12: 19...h6?? 20.Bxh6; 33...Kf8?? Qxf7#.
- g7/g8: 24...Nf6?? exf6; 20...Bf5?? Nxf5.
