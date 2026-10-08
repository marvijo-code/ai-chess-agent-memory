# White closed Ruy vs 3...a6 (G9, G14, G15, G19, G20 wins vs DeepSeek, 900+10)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3. DeepSeek then picks Chigorin (9...Na5) or Breyer (9...Nb8).

## Breyer (G19, mate 34)
9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4 bxa4 16.Bxa4 (pins Nd7 vs Re8) c5?! 17.d5?! Nb6? 18.Bxe8 Qxe8 (exchange up) 19.Be3 Bxd5 20.exd5 Nfxd5 21.Qd2 Nxe3 22.Qxe3 d5 23.Nxe5 Qxe5?? 24.Qxe5 Bd6 25.Qxd6 ... 33.Rxf7 Kh8 34.Rf8#.
- Plan 12.Nbd2, 13.Nf1, 14.Ng3, 15.a4 hits b5. After ...bxa4 Bxa4 the Nd7 is pinned.
- 33.Qxf7+ was ILLEGAL: my own Re7 stood between. Name the line before a mate try.

## Chigorin (G14, G15, G20)
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 (or Bb7 in G20) 14.d5 Nb8 15.Nf1 Nbd7 16.Ng3 g6 17.Bh6 Re8 18.Qd2. 17.Bh6 hits Rf8, Qd2 supports it.
- G20 (mate 41): 13...Bb7 14.Nf1 Rac8 15.Ng3?? (engine) Rfe8 16.d5?? Nc4 17.b3 Nb6 18.Bd3 Nc4? 19.bxc4 bxc4 20.Bf1 Nd7 21.Be3 f5 22.Nxf5 g6 23.Nxe7+ Rxe7 24.Nd2 c3 25.Nb3 Nf6 26.Bc1 Nxe4 27.Rxe4 Bxd5 28.Qxd5+ Rf7 29.Qc4 Qxc4 30.Bxc4 Rxc4 31.Rxc4 Rxf2 32.Kxf2 c2 33.Rxc2 ... 40.Re7+ Kg8 41.Rd8#. Engine: 13.Bb3! 25.cxd4!, but 15.Ng3?? and 16.d5?? (Black's Rac8+Qc7 hit Bc2 on the c-file, Nc4 comes with tempo). Next time vs ...Bb7/...Rac8 setup: 15.Bb1 (as G9) or 15.Nb3/Rc1 idea, keep d4 tension, don't close with d5.
- Why it worked anyway: after ...Nc4 b3 kicked it; 18...Nc4? bxc4 won a piece; I avoided Bxc4 (undefended to Qxc4) and Qxc2 (queen trade trap), retreated Bd3-f1, Be3, then Bc1 to blockade c3. Watched ...c2 for ten moves (never Qxc2).
- G15 (mate 34): 18...Bf8 19.Bxf8 Kxf8 20.Qh6+ Kg8 21.Nh4 Kh8 22.Qd2 Nc5 23.Nf3 Bd7 24.h4 Rac8 25.h5 g5? 26.Nxg5 Nxh5? 27.Nxh5 Nxe4 28.Bxe4 Bf5 29.Bxf5 f6 30.Nxf6 Re7 31.Bxc8 Qxc8 32.Ne6 Qb8 33.Qh6 Rxe6 34.Qxh7#. Mating pattern: Nf6 guards h7, Qh6 threatens Qxh7#/Qg7#.
- G14 (mate 34): 16...g6 17.Bh6 Re8 18.Qd2 Nh5 19.Nxh5 gxh5 20.Bg5 h6 21.Bxh6 Bf6 22.Bg5 Bxg5 23.Qxg5+ Kh8 24.Qxh5+ Kg8 25.Ng5 Nf6 26.Qh4 Nh7? 27.Nxh7 ... 34.Qxf7#.

## G9 line (mate 53)
12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 Bb7 15.Be3 Rac8 16.Nbd2 Rfe8 17.Bb1 (off the c-file) Na5 18.Nb3 Nxb3 19.Qxb3 Bf8 20.Bd3 Nd7 21.Rad1 d5 22.exd5 Nf6 23.dxe5 Nxd5 24.Bd4 Nf6?? 25.exf6 ... piece up.
- 31.Qxd4?? Qxd4: my Bd3 blocked Rd1. List the recapturer and the path before any queen trade.

## DeepSeek habits
- 35-60 s a move from move 9 (G20: 13 of 15 min used by move 33; I used ~1 min), tries illegal moves, hangs pieces when worse. Stay solid, take safe material, 1-10 s on book moves, 30-45 s at captures.
- Down material it just grabs pawns and trades into lost endings; convert by trading and checking stalemate.
