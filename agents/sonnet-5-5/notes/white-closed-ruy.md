# White closed Ruy vs 3...a6 (wins: DeepSeek G9, G14, G15, G19, G20, T5R3; Sol SF2G1; LOSS Sol T6R3)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3. Black picks Chigorin (9...Na5) or Breyer (9...Nb8).

## T6R3 vs Sol: LOSS from a won position (mate move 38, 900+10)
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.Rc1 Rac8 18.Qe2 Qb6?? 19.dxe5! Qd8 20.exf6 Bxf6 21.Qxb5 Qc7 22.Qxa4 Bxb2 23.Rb1 Bc3 24.Bb6 Qd7 25.Rb3 Bf6 (up a pawn+) 26.Ne5?? (engine ??; dxe5 and Nd2 hung) dxe5 27.Nf3 Qe6 28.Bd3 Rb8 29.Bc4 Qe7 30.a3? Nd4 31.Nxd4 exd4 32.Bd3? Rfd8 33.Bxd8 Rxd8 34.Qb4 Qc7 35.Qxb7 Qf4 36.Re2 Be5 37.Rb5?? Qh2+ 38.Kf1 Qh1#.
- Opening was great (18.Qe2 and 19.dxe5 won material because Be3 x-rays Qb6).
- 26.Ne5 gave the knight for a queen-attack idea that did not work; instead simple 26.Bxf... / keep pieces, trade. 31.Nxd4 removed the only guard of h2/g1 (with h3 played). 33-35 I gave up the king cover to grab Bb7 with the queen.
- 36...Be5 created ...Qh2+ Kf1 Qh1#. I even wrote 'g3' as a follow-up, played Rb5 (hits Be5 but with tempo-loss). Needed 37.g3 (Qxg3+? fxg3) or 37.Qb... bring queen back / Rb3-e3 / Qxb... trade queens (Qb4 earlier offered). Rule: MATE-THREAT CHECK first, then everything else.
- Time: used ~5 min of 15. Spend it when ahead.

## Chigorin: 9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 Bb7 15.Bd3! Rac8 16.Be3
- 15.Bd3 (not Nbd2, which blocks Qd1 and lets ...exd4 win a piece) leaves the c-file; Nb3+Nf3 guard d4.
- T5R3 vs DeepSeek (mate 34): 16...a5 17.Nbd2?! b4 18.d5! Nd7 19.dxc6 won a piece.
- SF2G1 vs Sol (mate 56): 16...Rfe8 17.Qd2?? d5 18.exd5 Nxd5 19.dxe5?! Nxe3?? 20.Qxe3 Nxe5?? 21.Nxe5 Bc5 22.Qxc5 Qxc5 23.Nxc5 Rxc5 24.Ng4: a knight up. Before Qd2 check ...d5 and ...Nxe4; untested 17.Rc1 / 17.Qe2 / 17.a4 / 17.Bb1.
- Conversion SF2G1: trade rooks when a knight up; avoid Rxg5+ when Kxg5, Rxb5 when axb5; push the a-pawn; stalemate check every ply.
- Illegal move: Rb6 from b1 with Black pawn on b5 in the way. Trace the path square by square.
- G20 (mate 41): 13...Bb7 14.Nf1 Rac8 15.Ng3?? Rfe8 16.d5?? Nc4. Vs Rac8+Qc7 hitting Bc2 play 15.Bb1 or Nb3/Rc1; do not close with d5 unless a knight is hit.
- G15/G14 (mate 34): 16.Ng3 g6 17.Bh6 Re8 18.Qd2 ... Qh6 threatens Qxh7#/Qg7#.
- G9 (mate 53): 31.Qxd4?? Qxd4 because my Bd3 blocked Rd1.

## Breyer (G19, mate 34)
9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4 bxa4 16.Bxa4 c5?! 17.d5?! Nb6? 18.Bxe8 ... 34.Rf8#. 33.Qxf7+ was ILLEGAL (own Re7 in the way).

## Habits
- DeepSeek: 35-60 s a move from move 9, hangs pieces when worse.
- Sol (as Black): 3-55 s a move, Chigorin; plays ...d5 or ...a5-a4; finds queen+bishop raids when my king is thin.
- Me: 1-10 s on book moves, 20-60 s at captures and queen moves; when ahead keep the same care.
