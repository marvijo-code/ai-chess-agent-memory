# White closed Ruy vs 3...a6 (G9, G14, G15, G19, G20, T5R3 wins vs DeepSeek, 900+10)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3. DeepSeek then picks Chigorin (9...Na5) or Breyer (9...Nb8).

## Chigorin: 9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4
- T5R3 (mate 34, used ~1 min of 15): 13...Nc6 14.Nb3 Bb7 15.Bd3! (avoids Nbd2 which blocks Qd1 and lets ...exd4 win a piece; Nb3+Nf3 guard d4) Rac8 16.Be3 a5 17.Nbd2?! (engine) b4 18.d5! Nd7 19.dxc6 (piece up) Bxc6 20.Qc2 Rfd8 21.Rac1 Nc5 22.Bxc5 dxc5 23.Nc4 f6 24.Ne3 b3 25.Qxb3+ Kh8 26.Nd5 Bxd5 27.exd5 Qd7 28.Bc4 Qxd5 29.Bxd5 Rxd5 30.Qxd5 ... 33.Qxc7 Rc8 34.Qxc8#.
  Pattern: ...a5/...b4 allowed d5 hitting Nc6 with the knight having no good square. Keep Bd3 guarded by Qc2/Qb3, trade pieces, check ...Bxe4/...Rxd3 each move.
- G20 (mate 41): 13...Bb7 14.Nf1 Rac8 15.Ng3?? Rfe8 16.d5?? Nc4 17.b3 Nb6 18.Bd3 Nc4? 19.bxc4 won a piece. Black's Rac8+Qc7 hit Bc2 on the c-file; vs that setup play 15.Bb1 (as G9) or Nb3/Rc1, keep d4 tension, don't close with d5 unless a knight is hit (T5R3).
- G15 (mate 34): 16.Ng3 g6 17.Bh6 Re8 18.Qd2 Bf8 19.Bxf8 Kxf8 20.Qh6+ ... Nf6 guards h7, Qh6 threatens Qxh7#/Qg7#; 34.Qxh7#.
- G14 (mate 34): 16...g6 17.Bh6 Re8 18.Qd2 Nh5 19.Nxh5 gxh5 20.Bg5 h6 21.Bxh6 Bf6 ... 34.Qxf7#.
- G9 (mate 53): 12...cxd4 13.cxd4 Nc6 14.Nb3 Bb7 15.Be3 Rac8 16.Nbd2 Rfe8 17.Bb1 (off the c-file) Na5 18.Nb3 Nxb3 19.Qxb3 Bf8 ... 31.Qxd4?? Qxd4: my Bd3 blocked Rd1. Name the recapturer and its path before a queen trade.

## Breyer (G19, mate 34)
9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4 bxa4 16.Bxa4 (pins Nd7 vs Re8) c5?! 17.d5?! Nb6? 18.Bxe8 Qxe8 19.Be3 ... 33.Rxf7 Kh8 34.Rf8#. 33.Qxf7+ was ILLEGAL (own Re7 in the way): name the line before a mate try.

## DeepSeek habits
- 35-60 s a move from move 9 (T5R3: 9 min used by move 28, ended with 1:30; tried illegal recaptures Nxc6/Rxd5), hangs pieces when worse, grabs pawns, trades into lost endings. Stay solid, 1-10 s on book moves, 20-45 s at captures, check stalemate when mating.
