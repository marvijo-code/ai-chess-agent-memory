# White closed Ruy vs 3...a6 (wins: DeepSeek G9,G14,G15,G19,G20,T5R3,T10R3,T10SF1G1; Sol SF2G1, T8R2; LOSS Sol T6R3, T13R2, T16R3, T17R1)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3. Black: Chigorin (9...Na5) or Breyer (9...Nb8). (7...O-O: white-anti-marshall-d3.md.)

## T17R1 vs Sol: LOSS (mate 40, 900+10), clock 6:31 vs 11:14 at the end
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.d5?! Nb4 18.Bb1 Na6 19.a3 Nc5 20.Bxc5 dxc5 21.Nf1 c4 22.Qd2 Bd6 23.Ne3 g6 24.Rc1 Rfc8 25.Qe2 Qb6 26.Qd2 h5 27.Kh2? Nd7 28.Qe2 f5 29.exf5?? e4+ 30.g3 exf3 31.Qxf3 Ne5 32.Qe2 Nd3 33.Bxd3 cxd3 34.Rxc8+ Rxc8 35.Qxd3 Rc2 36.Nxc2?? Qxf2+ 37.Kh1 Bxg3 38.Qxg3 Qxg3 39.Ne1 Bxd5+ 40.Nf3 Bxf3#.
- Opening was fine (18.Bb1, 20.Bxc5 approved). 17.d5?! closed the centre: protected ...c4 clamp + ...Bd6 blockade. Try (unverified) 17.Rc1 / 17.Qd2 / 17.Qb1 keeping d4-e5 tension.
- 22-28: five queen/king shuffles, no plan. My in-game notes repeated 'watch ...c3, ...b4, ...Nxe4' and never named ...f5/...e4+.
- 27.Kh2 stood on Bd6's b8-h2 diagonal behind only the e5 pawn; 28...f5 then 29.exf5? e4+ (discovered check, hits Nf3) lost a piece. Unverified fixes: Kh1/Kg1, 29.Nxc4 or 29.Neg5 (do not open e4 for ...e4+).
- 35.Qxd3 left f2 guarded by nothing but the Ne3 shield; 35...Rc2 was bait. 36.Nxc2?? unmasked Qb6-f2. 36.Qxc2 (Qxe3 fxe3) or 36.Nxc2 only after checking f2. I was a rook up and lost it all.

## T16R3 vs Sol: LOSS (mate 40)
...14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.d5 Nb4 18.Bb1 Rfc8 19.a3 Na6 20.Bc2?? Nc5 21.b4? axb3 e.p. 22.Bxb3 Ncxe4! 23.Nxe4 Nxe4 24.Qd3 (Rxe4 illegal x2: Be3 on e3) ... 27...e4 forks Qd3+Nf3 29.Nd2 Bxa1 ... 40...Qxg2#.
- Be3 blocks Re1, so e4 had Nd2+Bc2 vs Nc5+Nf6. Fixes: 20.Bb1 stay; 21.Bxc5; never b4. Move Ra1 before ...Bf6.

## T13R2 vs Sol: LOSS (mate 39)
...13...Nc6 14.d5 Nb8 15.Nf1 Nbd7 16.Ng3 Bb7 17.Be3 Rfe8 18.a4 b4 19.Bd2?! a5 20.Nh2 Nc5 21.Ng4 Rac8 22.Nxf6+ Bxf6 23.Bd3?? Nxd3 (Bd2 blocked Qd1) ... 29.Qb3?? Qxa1+. Keep Be3, answer ...Nc5 with Bxc5.

## Wins
- T10 SF1G1 (DeepSeek, mate 24): 14.Nb3 Rac8 15.Nxa5 Qxa5 16.Bd2 Rfd8?? 17.Bxa5. T10R3 (mate 23): 11.d4 Qc7 12.Nbd2 Bb7 13.Nf1 Rac8 14.Ng3 Nd7 15.d5 c4 16.Nf5 Nc5 17.Bg5 ... 23.Qxh7#.
- T8R2 vs Sol (mate 52): 14.d5 Nd8 15.Nf1 Bd7 16.Ng3 Nb7 17.Bd2 Nc5 18.Qe2 Rac8 19.Rac1: Bd2 guards Rc1.
- Breyer G19 (mate 34): 9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4.
- 14.Nb3 Bb7 15.Bd3! Rac8 16.Be3 (T5R3, G20: vs Rac8+Qc7 hitting Bc2 play Bb1 or Nb3/Rc1).

## T6R3 vs Sol: LOSS from a won position
18.Qe2 Qb6?? 19.dxe5! ... 37.Rb5?? Qh2+ 38.Kf1 Qh1#. Mate-threat check first; king left bare.

## Habits
- Sol 3-55 s, finds raids when my king is thin and breaks (...f5, ...e4) that open diagonals to my king. DeepSeek hangs pieces when worse.
- Me: 1-10 s on book, then 30-120 s at captures/trades/queen moves; trace recaptures and screens even in standard positions.
