# Black vs 3.Bc4 (Sol: T9R1 L mate 47, T12SF2G1 L mate 50; DeepSeek: T19R5.2 W, T20R5.2 W)

## T20R5.2 vs DeepSeek (WON mate 73, 900+10, 4:34 left at end)
1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d3 Be7 5.c3 O-O 6.O-O d6 7.Nbd2 Be6 8.Bb3 Bxb3 9.Qxb3 Na5 10.Qc2 c5 11.Re1 Qc7 12.Nf1 Rfd8 13.Ng3 Nc6 14.Be3 h6 15.d4 cxd4 16.cxd4 Rac8 17.dxe5 dxe5 18.Rad1 Rxd1 19.Rxd1 Rd8 20.Rxd8+ Qxd8 21.Nf5 Bf8 22.h3 Qd7 23.Kh2 Be7 24.Nxe7+ Qxe7 25.Qd3 Nd7 26.Bg5?? hxg5 27.Nxg5 Qxg5 28.Qxd7 Qe7 29.Qxe7 Nxe7 (N for P up).
- Equal to move 25. Setup: Be6, trade on b3, Na5 hits Qb3, ...c5, ...Qc7, ...Rfd8, ...Nc6 back, ...h6. Before cxd4 I noted 'Qc2 unguarded: after cxd4 the c-file opens'. Good habit: write what an opened file does to his queen.
- Ending (N+P up, 30-73): 30...Nc6 31.a3 Nd4 32.f4 exf4+ 33.Kxf4 Ne6+ ... 40.Kxe5 Nc5 41.b4 Ne6 42.Kd6 Kf6 43.Kd7 b6 44.Kc6 Kf5 45.Kb7 a5?? 46.Kxb6 axb4 47.axb4 Kg4 48.b5 Kxh4?? 49.Kb7 ... 52.b7 Nxb7 53.Kxb7 Kg3 54.Kc6 Kxg2: won the K+g vs K race only because DeepSeek's K went the wrong way (SF: 95.b5??, 101.Ka7??, 103.b7??).
- My errors (SF: 70 f6?!, 90 a5??, 96 Kxh4??, 102 Nd8??): king walked f8-e7-f7-f6-f5 away from the queenside, so Kd6-d7-c6-b7 forked a7/b6. Better: Ke7 stays (his Kd6 is impossible), ...Nc5/...Nd4 vs the b-pawn, trade pawns on the queenside first, h4 can wait. Idea (unverified): keep a7+b6 pawns on a6/b6 chain, knight on d6/c5.
- Queen-vs-king mate (ply 142-146): Qc3 box, king approach, Qb4 then Qb6+/Qb7#; checked stalemate each ply.

## T19R5.2 vs DeepSeek (WON mate 31)
1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d3 Be7 5.O-O O-O 6.c3 d6 7.Nbd2 Be6 8.Bb3 a5 9.Re1 a4?! 10.Bxa4! Bd7 11.Bb3 Na5 12.Bc2 b5 13.h3 c5 14.Nf1 c4 15.dxc4 bxc4 16.Qxd6?? Bxd6 17.Rd1 Be7 18.Rxd7 Nxd7 19.Bd3 cxd3 ... e1=Q 31.Kg2 Qh1#.
- 9...a4?! lost a pawn (Bxa4; Rxa4 Qxa4 loses the exchange). Better 9...h6/...Re8/...Qd7 or take on b3 first.
- Recovery: ...Bd7, ...Na5 hits Bb3, ...b5/...c5/...c4 with tempo. After 16...Bxd6 17.Rd1 the Bd6 was loose: ...Be7 was right.

## T12SF2G1 vs Sol: equal 29 moves, then Qf5?? hung the queen
1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d3 Be7 5.O-O d6 6.c3 O-O 7.Re1 a6 8.Bb3 h6 9.Nbd2 Be6 10.Bc2 Re8 11.Nf1 Bf8 12.Ng3 Qd7 13.h3 Rad8 14.d4 exd4 15.cxd4 d5! 16.e5 Ne4! 17.Nxe4 dxe4! 18.Bxe4 Bf5! 19.Bxf5 Qxf5! 20.Be3 Rd5 21.Rc1 Qe6 22.Qe2 Be7 ... 30.Qe4 Qf5?? 31.Qxf5 g6 ... 50.Qh7#.
- Setup (Be7, d6, a6, h6, Be6, Re8, Bf8, Qd7, Rad8, ...exd4, ...d5 vs isolated d4) equalised easily. Moves 20-29 were shuffling with no plan.
- BLUNDER: Qf5 'defended' by Rd5 only on paper: his e5 pawn sat between. Trace the path through his pawns.
- Better 30th moves (unverified): 30...Qd7 / 30...Ne7 / 30...Rd7.

## T9R1 vs Sol (LOST mate 47): 3...Bc5 line
3...Bc5 4.c3 Nf6 5.d3 d6 6.O-O O-O 7.Re1 h6 8.Nbd2 a6 9.a4 Ba7 10.Nf1 Re8 11.h3 Be6 12.Bb3 Qd7 13.Ng3 Kh7 14.Be3 Bxe3 15.Rxe3 Bxb3 16.Qxb3 Rab8 17.d4 exd4 18.cxd4 d5 19.e5 Ng8 ... 26.e6 fxe6 27.Nxe6 ... 29.g5 hxg5?? 30.Nfxg5 ... 47.Nf7#.
- Traded both bishops; 19.e5 kicked Nf6; ...hxg5 opened the h-file. Prefer Be7/d6, keep a bishop, after d4 exd4 cxd4 play ...d5 and meet e5 with ...Ne4.
