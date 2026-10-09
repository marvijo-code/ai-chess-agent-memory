# White closed Ruy vs 3...a6 (wins: DeepSeek G9,G14,G15,G19,G20,T5R3,T10R3,T10SF1G1; Sol SF2G1, T8R2; LOSS Sol T6R3, T13R2)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3. Black: Chigorin (9...Na5) or Breyer (9...Nb8). (7...O-O: white-anti-marshall-d3.md.)

## T13R2 vs Sol: LOSS (mate 39, 900+10), one blunder
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb8 15.Nf1 Nbd7 16.Ng3 Bb7 17.Be3 Rfe8 18.a4 b4 19.Bd2?! a5 20.Nh2 Nc5 21.Ng4 Rac8 22.Nxf6+ Bxf6 23.Bd3?? Nxd3 24.Re2 Nxb2 25.Qb1 Nc4 26.Bxb4 axb4 27.Qxb4 ... 28.Qc3 Qd4 29.Qb3?? Qxa1+ ... 39...Qxh4#.
- 23.Bd3?? Nxd3: my Bd2 stood between Qd1 and d3, so no recapture. My ply-45 note said 'after Nxd3 Qxd3' and was never traced. Nd3 also forked Re1/b2/f2. Piece down at once.
- 29.Qb3?? left Ra1 to Qd4 (queen on c3 had covered the diagonal). Ask what the queen guards.
- Root: 19.Bd2 left e3, so ...Nc5 was safe. Keep Be3: answer ...Nc5 with Bxc5 dxc5 (or Bxc5). Don't play Nh2-g4 plans while c5 is available to a knight. Untested: 18.Bd3/18.Qd2/18.Nh4 ideas; with Bc2 + Qd1 free on d-file, Bd3 is OK only without Bd2.
- Sol: replies 5-47 s, converted by Nxb2, Qxa1+, Bxe2, Qxh4# on h-file with Rg1 blocked by own rook.

## T10 SF1G1 vs DeepSeek: WIN (mate 24)
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Bb7 14.Nb3 Rac8 15.Nxa5 Qxa5 16.Bd2 Rfd8?? 17.Bxa5 ... 24.Qe8#.
- 14.Nb3 vs Rac8+Qc7: 15.Nxa5 removes the battery on Bc2. Check ...Bxe4/...Nxe4/Rxc2 tricks.

## T10R3 vs DeepSeek: WIN (mate 23)
...11.d4 Qc7 12.Nbd2 Bb7 13.Nf1 Rac8 14.Ng3 Nd7 15.d5 c4 16.Nf5 Nc5 17.Bg5 Bxg5 18.Nxg5 b4 19.cxb4 Nxe4? 20.Bxe4 ... 23.Qxh7#.
- 15.d5 closes the c-file; Nf5 outpost; Bg5xg5 gives Ng5 + Nf5 -> Qh5/Qxh7#.

## T8R2 vs Sol: WIN (mate 52)
13...Nc6 14.d5 Nd8 15.Nf1 Bd7 16.Ng3 Nb7 17.Bd2 Nc5 18.Qe2 Rac8 19.Rac1 g6 ... 26...Na4? 27.Bxa4 bxa4 28.Rxc7.
- Plan vs d5: Nf1-g3, Bd2, Qe2, Rac1 behind Bc2. Bd2 must keep guarding Rc1. Trade rooks when ahead.

## T6R3 vs Sol: LOSS from a won position (mate 38)
13...Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.Rc1 Rac8 18.Qe2 Qb6?? 19.dxe5! ... 26.Ne5?? dxe5 ... 37.Rb5?? Qh2+ 38.Kf1 Qh1#. MATE-THREAT CHECK first; king left bare.

## Chigorin with 14.Nb3 Bb7 15.Bd3! Rac8 16.Be3
- 15.Bd3 (not Nbd2) leaves the c-file. T5R3: 16...a5 17.Nbd2?! b4 18.d5! Nd7 19.dxc6.
- SF2G1 vs Sol: 16...Rfe8 17.Qd2?? d5. Before Qd2 check ...d5/...Nxe4.
- G20: Vs Rac8+Qc7 hitting Bc2 play 15.Bb1 or Nb3/Rc1. G9: 31.Qxd4?? Qxd4 (Bd3 blocked Rd1).

## Breyer (G19, mate 34)
9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4 bxa4 16.Bxa4 c5?! 17.d5 ... 34.Rf8#. 33.Qxf7+ was ILLEGAL (own Re7 in the way).

## Habits
- DeepSeek: 35-60 s a move, hangs pieces when worse. Sol: 3-55 s, finds raids when my king is thin.
- Me: 1-10 s on book moves, 30-120 s at captures/trades/queen moves; trace recaptures even in 'standard' positions.
