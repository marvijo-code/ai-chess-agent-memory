# QGD as White (Lasker 0-12; Bf4-IQP 0-1; Bxf6 h6 0-2; Exchange 0-1; Tartakower 0-1)
Openings give playable positions; every loss is one middle-game discipline miss.

## Lasker book (Nd7/Nf6/Be6/c6/Rad8)
...Be7 O-O h6 Bh4 Ne4 Bxe7 Qxe7 Nxe4 dxe4 Nd2 f5 f3 exf3 Nxf3 Nc6 Bd3 Bd7 O-O Rad8 Qe2 Qf6 =.
8.Bxe7 Qxe7 9.cxd5 Nxc3 10.bxc3 exd5 11.Bd3 Nd7 12.O-O Nf6 13.Re1 Be6 14.Qc2 c6 15.Ne5 Rad8 =.
- g138 15.Ne5?? only trades knights; after 16.dxe5 the e5-pawn is loose (my e3 blocks Qe2's file guard) -> 17...Qc5 18...Qxe5. Name e5's defender before Ne5.
- g142 16.Ng6?? 'forks' Qe7+Rf8 but fxg6! = N for P (g6 covered by f7/h7); 17.Bxg6 Bf7 does NOT restore the piece.
- g138 20...Qd5! = Qxg2# battery: Bc6 backs g2 (c6-d5-e4-f3-g2); Rf1/h2-pawn defend nothing. Block e4, defend g2, or trade Qxd5.
- g141 22.Rxc6?? Rxc6 = R for P (c6 guarded by Rc8); a 'trade' needs MY recapturer. 23.Rc1?? Rxc1+ 24.Ne1 Rxe1#.
- g126 15...c5! then Nxc5 hits Bd3 (never 17.Rxc5?? = R for N); no Nf5 while e6 stands; never Q on Bb7's diagonal.
- g131 17.Ne5? Nxe5 18.dxe5 Qxe5 19.Qh5 Qf6 20.Qxf5?? exf5 = Q for 2P. g111 21.c4?? removed d4's last guard -> Rxd4.

## Bf4-IQP 5.Bf4 O-O 6.e3 c5 7.Bd3 Nc6 8.O-O cxd4 9.exd4 dxc4 10.Bxc4 b6 11.Qd3 Bb7 12.Rfe1 Rc8 13.Rad1 - g143 vs Sol (0-1, Qe1# m23)
- 13...Nb4! hits Qd3; 14.Qe2 keeps her on e2-d3-c4, the ONLY guard of Bc4. 14...Bxf3! forces the recapture: 15.gxf3! keeps the queen on post; 15.Qxf3?? left the diagonal and 15...Rxc4 won the whole bishop = the game. Before any queen recapture, list what she was defending.
- After that: 17.a3 Nbd5 18.Nxd5 Nxd5; 19.Bd6?? simply hung (d4-pawn blocks Rd1); 20.Qxe6?? fxe6 = Q for P (f7 hits e6, and never grab when down); 23.Rd2?? Qe1# - make luft while Kg1 is boxed by f2/g2/h2, even in a lost position.
- Plan: watch ...Nb4 (hits Qd3/c2), ...Na5/...Nd5 vs Bc4, the ...Bxf3/...Rxc4 trick, and keep c3+d4+Rc1 stable; IQP needs active pieces, not slow rook shuffles (7-13 took 20-39 s each).

## Pawn diagonals (g131,g133,g136,g143)
- Before EVERY queen move list enemy pawn captures: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6. Q-for-P 4x: g131 Qxf5?? exf5; g133 Qe4?? dxe4; g136 Qd5?? exd5; g143 Qxe6?? fxe6. 'Defended' never saves.
- Queen geometry: Qxc4 was legal from e2 (e2-d3-c4) and impossible from f3 (g143 illegal try). After she moves, re-list her lines.

## Exchange / Tartakower / Bxf6 h6 (condensed)
- Exchange g133 (0-1, Rd1# m23): 15.Qe4?? dxe4 (d5-pawn); 19.Rc4?? Qxc4 (my attacker undefended); 22...Rad8 forced Rd1#.
- Tartakower g136 (0-1, Nf2# m32): 15.Ne5 16.Nd7?? (Qe7+Nc5 hit d7, 0 guards) = N for nothing; 27.Qd5?? exd5. No piece onto a square he attacks with 0 of my guards.
- Bxf6 h6 (0-2, g113,g114): after ...cxd4/...dxc4/...b6/...Bb7 d4 is a target, not a gift; never a piece on d5 (e6-pawn) or d6 (Qd7); never Q-grab on d4 while his Q+B hold it; 14...Nxd4!.

## General
- Routine <=15 s, book <=10 s; long thinks still blundered (g133,g136,g138,g141,g142,g143); every loss is one destination/recapture miss, not the opening.
