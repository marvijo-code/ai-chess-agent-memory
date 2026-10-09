# White closed Ruy vs 3...a6 (wins: DeepSeek G9,G14,G15,G19,G20,T5R3,T10R3,T10SF1G1; Sol SF2G1, T8R2; LOSS Sol T6R3)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3. Black picks Chigorin (9...Na5) or Breyer (9...Nb8). (7...O-O: see white-anti-marshall-d3.md.)

## T10 SF1G1 vs DeepSeek: WIN (mate 24, 900+10, used ~1 min)
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Bb7 14.Nb3 Rac8 15.Nxa5 Qxa5 16.Bd2 Rfd8?? 17.Bxa5 Bxe4 18.Bxe4 Nxe4 19.Rxe4 Bf6 20.Bxd8 Bxd8 21.dxe5 dxe5 22.Nxe5 Bf6 23.Qd7 Rc7 24.Qe8#.
- 14.Nb3 vs Rac8+Qc7: 15.Nxa5 removes the Qc7/Rc8 battery on Bc2. After 15...Qxa5 the queen is undefended and 16.Bd2 hits it (Bd2 guarded by Qd1; ...Qxa2 Rxa2). Check each move: ...Bxe4/...Nxe4 tricks and Rc8xc2.
- Won queen for a pawn; then kept Qd1/Ra1 on the back rank, traded, finished Qd7/Qe8# on the open back rank (pawns f7,g7,h7 boxed K).

## T10R3 vs DeepSeek: WIN (mate 23)
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 Bb7 13.Nf1 Rac8 14.Ng3 Nd7 15.d5 c4 16.Nf5 Nc5 17.Bg5 Bxg5 18.Nxg5 b4 19.cxb4 Nxe4? 20.Bxe4 Nc6 21.dxc6 Bxc6 22.Qh5 Qd7 23.Qxh7#.
- 15.d5 closes the c-file (Bc2 safe), Nf5 outpost supported by e4. 17.Bg5 forces ...Bxg5 Nxg5: Ng5 guards h7, Nf5 guards g7 -> Qh5 threatens Qxh7#.
- 19.cxb4 forked Na5+Nc5; 19...Nxe4 lost a piece (d5 blocked Bb7). Ng5 undefended (...h6 hits it).

## T8R2 vs Sol: WIN (mate 52)
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nd8 15.Nf1 Bd7 16.Ng3 Nb7 17.Bd2 Nc5 18.Qe2 Rac8 19.Rac1 g6 20.Nh2 Rfe8 21.Ng4 Nxg4 22.hxg4 Bf8 23.g5 Bg7 24.a3 a5 25.b4 axb4 26.axb4 Na4? 27.Bxa4 bxa4 28.Rxc7 Rxc7 (Q for R)
- Plan vs d5: Nf1-g3, Bd2, Qe2, Rac1 puts Rc1 behind Bc2. Any Black knight move off c5 opens the c-file: Rxc7. Bd2 must keep guarding Rc1.
- Conversion: trade rooks when ahead, list forks (...Rc2, ...Ra2, ...Bb5, ...Ra1+) each move.

## T6R3 vs Sol: LOSS from a won position (mate 38)
13...Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.Rc1 Rac8 18.Qe2 Qb6?? 19.dxe5! ... 25...Bf6 (pawn+ up) 26.Ne5?? dxe5 ... 30.a3? Nd4 31.Nxd4 exd4 ... 37.Rb5?? Qh2+ 38.Kf1 Qh1#.
- 26.Ne5 bad queen-attack try; 31.Nxd4 removed guard of h2/g1; I left the king bare. MATE-THREAT CHECK first; needed 37.g3 or a queen trade.

## Chigorin with 14.Nb3 Bb7 15.Bd3! Rac8 16.Be3
- 15.Bd3 (not Nbd2, which blocks Qd1 and lets ...exd4 win a piece) leaves the c-file.
- T5R3 (mate 34): 16...a5 17.Nbd2?! b4 18.d5! Nd7 19.dxc6 won a piece.
- SF2G1 vs Sol: 16...Rfe8 17.Qd2?? d5 18.exd5 Nxd5 ... Before Qd2 check ...d5/...Nxe4; untested 17.Rc1/17.Qe2/17.a4.
- G20: 13...Bb7 14.Nf1 Rac8 15.Ng3?? Rfe8 16.d5?? Nc4. Vs Rac8+Qc7 hitting Bc2 play 15.Bb1 or Nb3/Rc1.
- G15/G14: 16.Ng3 g6 17.Bh6 Re8 18.Qd2 ... Qh6 threatens Qxh7#/Qg7#.
- G9: 31.Qxd4?? Qxd4 because my Bd3 blocked Rd1.

## Breyer (G19, mate 34)
9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4 bxa4 16.Bxa4 c5?! 17.d5?! Nb6? 18.Bxe8 ... 34.Rf8#. 33.Qxf7+ was ILLEGAL (own Re7 in the way).

## Habits
- DeepSeek: 35-60 s a move from move 9, hangs pieces/queen when worse. Sol: 3-55 s, finds queen+bishop raids when my king is thin.
- Me: 1-10 s on book moves, 20-60 s at captures/queen moves; same care when ahead. Trace paths.
