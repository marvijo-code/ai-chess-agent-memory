# White closed Ruy vs 3...a6 (wins: DeepSeek G9,G14,G15,G19,G20,T5R3,T10R3,T10SF1G1; Sol SF2G1, T8R2; LOSS Sol T6R3, T13R2, T16R3)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3. Black: Chigorin (9...Na5) or Breyer (9...Nb8). (7...O-O: white-anti-marshall-d3.md.)

## T16R3 vs Sol: LOSS (mate 40, 900+10), clock 3:35 vs 11:00 at the end
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.d5 Nb4 18.Bb1 Rfc8 19.a3 Na6 20.Bc2?? (SF) Nc5 21.b4? axb3 e.p. 22.Bxb3 Ncxe4! 23.Nxe4 Nxe4 24.Qd3 (Rxe4 illegal x2: Be3 on e3; 2:50 lost) Nc5 25.Bxc5 Qxc5 26.Nd2 f5 27.Nf3 e4 28.Qe2 Bf6 29.Nd2 Bxa1 30.Rxa1 Qc3 31.Ra2 Qc1+ 32.Kh2 Rxa3 ... 40...Qxg2#.
- Root: Be3 blocks Re1, so e4 had Nd2 + Bc2 only vs Nc5 + Nf6. 21.b4 axb3 e.p. made Bxb3 and removed Bc2's guard. My game note said 'Nxe4 Nxe4 Rxe4 wins a piece' without tracing e1-e4.
- Fixes (unverified): 20.Bb1 stay (or Ba2); 21.Bxc5 dxc5 22.Qd3/Bb3 keeps e4 guarded twice; avoid b4 entirely (it also opened a1-h8: Bf6xa1 later). Vs ...Na6-c5 the Be3 is a liability; consider Bd2 only if Nc5 can be taken by Bxc5.
- Later: 27...e4 forked Qd3+Nf3 (Q should leave d3 earlier); 28.Qe2 Bf6 hit Nf3+Ra1: move Ra1 BEFORE. 32.Kh2 Rxa3: a3 defended only by Ra2.
- Time: Sol banked 11 min; my 20-35 moves took 40-70 s each with false justifications. Spend the time listing my blocked lines and loose rooks.

## T13R2 vs Sol: LOSS (mate 39)
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb8 15.Nf1 Nbd7 16.Ng3 Bb7 17.Be3 Rfe8 18.a4 b4 19.Bd2?! a5 20.Nh2 Nc5 21.Ng4 Rac8 22.Nxf6+ Bxf6 23.Bd3?? Nxd3 24.Re2 Nxb2 ... 29.Qb3?? Qxa1+ ... 39...Qxh4#.
- 23.Bd3?? Nxd3: my Bd2 sat between Qd1 and d3, no recapture. Qb3?? left Ra1. 19.Bd2 left e3 so ...Nc5 was safe: keep Be3 and answer ...Nc5 with Bxc5.

## T10 SF1G1 vs DeepSeek: WIN (mate 24)
13...Bb7 14.Nb3 Rac8 15.Nxa5 Qxa5 16.Bd2 Rfd8?? 17.Bxa5. 15.Nxa5 removes the battery on Bc2; check ...Bxe4/...Nxe4/Rxc2 tricks.

## T10R3 vs DeepSeek: WIN (mate 23)
11.d4 Qc7 12.Nbd2 Bb7 13.Nf1 Rac8 14.Ng3 Nd7 15.d5 c4 16.Nf5 Nc5 17.Bg5 Bxg5 18.Nxg5 b4 19.cxb4 Nxe4? 20.Bxe4 ... 23.Qxh7#. d5 closes c-file; Nf5 outpost; Ng5+Nf5 -> Qh5/Qxh7#.

## T8R2 vs Sol: WIN (mate 52)
13...Nc6 14.d5 Nd8 15.Nf1 Bd7 16.Ng3 Nb7 17.Bd2 Nc5 18.Qe2 Rac8 19.Rac1 g6 ... 26...Na4? 27.Bxa4 bxa4 28.Rxc7. Plan vs d5: Nf1-g3, Bd2, Qe2, Rac1 behind Bc2; Bd2 guards Rc1.

## T6R3 vs Sol: LOSS from a won position (mate 38)
13...Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.Rc1 Rac8 18.Qe2 Qb6?? 19.dxe5! ... 37.Rb5?? Qh2+ 38.Kf1 Qh1#. MATE-THREAT CHECK first; king left bare.

## 14.Nb3 Bb7 15.Bd3! Rac8 16.Be3
- 15.Bd3 (not Nbd2) leaves the c-file. T5R3: 16...a5 17.Nbd2?! b4 18.d5! SF2G1: 16...Rfe8 17.Qd2?? d5. G20: vs Rac8+Qc7 hitting Bc2 play 15.Bb1 or Nb3/Rc1.

## Breyer (G19, mate 34)
9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4 bxa4 16.Bxa4 c5?! 17.d5 ... 34.Rf8#.

## Habits
- DeepSeek: 35-60 s a move, hangs pieces when worse. Sol: 3-55 s, finds raids when my king is thin.
- Me: 1-10 s on book, 30-120 s at captures/trades/queen moves; trace recaptures (own pieces block rooks!) even in 'standard' positions.
