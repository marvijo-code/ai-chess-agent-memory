# QGD as White (Lasker 0-13; Bf4-IQP 0-2; Bxf6 h6 0-2; Exchange 0-1; Tartakower 0-1)

Every loss = one destination/recapture/retreat miss, not the opening.

## Lasker book (Nd7/Nf6/Be6/c6/Rad8)
A: ...Be7 O-O h6 Bh4 Ne4 Bxe7 Qxe7 Nxe4 dxe4 Nd2 f5 f3 exf3 Nxf3 Nc6 Bd3 = level.
B: 8.Bxe7 Qxe7 9.cxd5 Nxc3 10.bxc3 exd5 11.Bd3 Nd7 12.O-O Nf6 13.Re1 Be6 14.Qc2 c6 15.Ne5 Rad8 = level.
- g138 15.Ne5?? only trades knights; after dxe5 the e5-pawn hangs (my e3 blocks Qe2's file guard) -> ...Qc5/...Qxe5. Name e5's defender before Ne5.
- g142 16.Ng6?? fxg6 = N for P (g6 covered by f7/h7); Bxg6 Bf7 does NOT restore the piece.
- g138 20...Qd5! = Qxg2# battery (Bc6 backs g2: c6-d5-e4-f3-g2); block e4, defend g2, or trade Qxd5.
- g141 22.Rxc6?? Rxc6 = R for P (c6 guarded by Rc8); 23.Rc1?? Rxc1+ 24.Ne1 Rxe1#.
- g126 15...c5!; then ...Nxc5 hits Bd3 (never Rxc5); no Nf5 while e6 stands; never a queen on Bb7's diagonal.
- g131 20.Qxf5?? exf5; g111 21.c4?? removed d4's last guard -> Rxd4.
- g145: 14.O-O Nb6 15.Bd3 Nd5 16.Ne5 Qc7 17.Rac1 Be6 - the d5-knight SCREENS Be6-b3; 18.e4?? Nf4! = Q for B; move the queen off b3 first (Qc2).

## Bf4-IQP (0-2, g143,g146)
Book: 6.e3 c5 7.Bd3 Nc6 8.O-O cxd4 9.exd4 dxc4 10.Bxc4 b6 11.Qd3 Bb7 12.Rfe1 Rc8 13.Rad1 (15 plies).
- Then 13...Nb4! hits Qd3; 14.Qe2 keeps her on e2-d3-c4, the ONLY guard of Bc4; 14...Bxf3! 15.gxf3! (15.Qxf3?? left that diagonal -> 15...Rxc4 = bishop).
- g143: 19.Bd6?? hung (d4 blocks Rd1); 20.Qxe6?? fxe6; 23.Rd2?? Qe1# - make luft while Kg1 is boxed by f2/g2/h2.
- g146: 13.Bxf6 Nxf6 14.Ne5 Nd5 15.Nxd5 Bxd5 16.Bxd5 Qxd5 17.Nc4?? (9 plies) - the queen on d5 hits e5 (rank) AND c4/f3 (diagonals), so the knight's retreat square was still on her lines; 17...Qxc4 won the knight. Before retreating an attacked piece, list EVERY square the attacker still hits; the retreat must leave all of them and be defended.
- g146: 20.b3?? cleared b2 from the a1-h8 diagonal, so the f6-bishop took the a1-rook. Before a pawn push, name the line it opens and the piece at its end.
- Plan: IQP needs active pieces; watch ...Na5/...Nd5 vs Bc4 and the ...Bxf3/...Rxc4 trick; no slow shuffles (g146 moves 7-17 took 32-41 s each).

## Exchange / Tartakower / Bxf6 h6 (condensed)
- Exchange g133 (Rd1# m23): 15.Qe4?? dxe4 (d5-pawn); 19.Rc4?? Qxc4 (my attacker undefended); 22...Rad8 forced Rd1#.
- Tartakower g136 (Nf2# m32): 15.Ne5 16.Nd7?? (Qe7 and Nc5 both hit d7, 0 guards) = N for nothing; 27.Qd5?? exd5. No piece onto a square he attacks with 0 of my guards.
- Bxf6 h6 g113/g114: after ...cxd4/...dxc4/...b6/...Bb7, d4 is a target; never a piece on d5 (e6-pawn) or d6 (Qd7); never a queen grab on d4 while his Q+B hold it; 14...Nxd4!.

## Pawn diagonals / queen geometry
- Before EVERY queen move list enemy pawn captures: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6. Q-for-P 3x: g131 Qxf5?? exf5; g136 Qd5?? exd5; g143 Qxe6?? fxe6. 'Defended' never saves.
- Qxc4 was legal from e2 (e2-d3-c4) and impossible from f3 (g143 illegal try). After she lands, re-list her lines.

## General
- Routine <=15 s, book <=10 s; long thinks still blundered (g138-g146; g146 moves 7-17 were 32-41 s each).
- Down material: no grabs, keep queens, defend loose pieces first (g133-g146 all).
