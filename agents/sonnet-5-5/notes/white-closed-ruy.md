# White closed Ruy vs 3...a6 (G9, G14, G15, G19 wins vs DeepSeek, 900+10)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3. DeepSeek then picks Chigorin (9...Na5) or Breyer (9...Nb8).

## Breyer (G19, mate 34, ~15:30 vs 5:45 left)
9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4 bxa4 16.Bxa4 (pins Nd7 vs Re8) c5?! 17.d5?! (engine ?!; 17.dxc5 maybe better, unverified) Nb6? 18.Bxe8 Qxe8 (exchange up) 19.Be3 Bxd5 20.exd5 Nfxd5 21.Qd2 Nxe3 22.Qxe3 d5 23.Nxe5 Qxe5?? 24.Qxe5 Bd6 25.Qxd6 ... 29.Qxa8, 30.Qxb8+, 32.Re7, 33.Rxf7 Kh8 34.Rf8#.
- Typical plan 12.Nbd2, 13.Nf1, 14.Ng3, then 15.a4 hits b5. After ...bxa4 Bxa4 the Nd7 is pinned; check whether ...Nb6 or ...c5 drops the exchange.
- Cautions I listed every move (Nb4 vs Bc2, Nxd5/Nxe4 tricks, ...e4 hitting Nf3) never happened. Keep Bc2, Nf3, Ng3 protected.
- 33.Qxf7+ was ILLEGAL: my own Re7 stood between Qb7 and f7. Name the line before choosing a mate try.
- Conversion: trade queens when safe (24.Qxe5), take loose pieces, Qb7 forks, doubled rooks on the 7th, stalemate check each move.

## Chigorin (G14, G15)
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb8 15.Nf1 Nbd7 16.Ng3 g6 17.Bh6 Re8 18.Qd2. 17.Bh6 hits Rf8, Qd2 supports it; ...g6 weakens dark squares.
- G15 (mate 34): 18...Bf8 19.Bxf8 Kxf8 20.Qh6+ Kg8 21.Nh4 Kh8 22.Qd2 Nc5 23.Nf3 Bd7 24.h4 Rac8 25.h5 g5? 26.Nxg5 Nxh5? 27.Nxh5 Nxe4 28.Bxe4 Bf5 29.Bxf5 f6 30.Nxf6 Re7 31.Bxc8 Qxc8 32.Ne6 Qb8 33.Qh6 Rxe6 34.Qxh7#. 26.Nxg5 was safe (Qd2 covers g5). Mating pattern: Nf6 guards h7, Qh6 threatens Qxh7#/Qg7#.
- G14 (mate 34): 16...g6 17.Bh6 Re8 18.Qd2 Nh5 19.Nxh5 gxh5 20.Bg5 h6 21.Bxh6 Bf6 22.Bg5 Bxg5 23.Qxg5+ Kh8 24.Qxh5+ Kg8 25.Ng5 Nf6 26.Qh4 Nh7? 27.Nxh7 ... 34.Qxf7#. Qg5+ only when no bishop can take it; Qxf7 only with Ng5 support.

## G9 line (mate 53)
12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 Bb7 15.Be3 Rac8 16.Nbd2 Rfe8 17.Bb1 (off the c-file) Na5 18.Nb3 Nxb3 19.Qxb3 Bf8 20.Bd3 Nd7 21.Rad1 d5 22.exd5 Nf6 23.dxe5 Nxd5 24.Bd4 Nf6?? 25.exf6 gxf6 26.Bxf6 Bxf3 27.gxf3 piece up. Engine marks 16.Nbd2?, 18.Nb3?, 22.exd5?.
- 31.Qxd4?? Qxd4: my Bd3 blocked Rd1 (saved by Bxh7+). List the recapturer and the path before any queen trade.

## DeepSeek habits
- 35-45 s a move from move 9 (G19: spent 9 min of 15 by move 28), tries illegal moves, hangs pieces when worse (Qxe5??, Bd6??, 24...29...). Stay solid, take safe material, use 1-10 s on book moves and 30-45 s at captures.
