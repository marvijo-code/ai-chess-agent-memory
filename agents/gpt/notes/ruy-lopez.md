# Ruy Lopez: captures, clearance and guards

## T28 final: White vs Stockfish 19, mate loss
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O b5 6.Bb3! Bc5 7.d3 d6 8.c3 h6 9.d4 Ba7 10.Re1 Bg4 11.h3 Bxf3! 12.Qxf3 exd4! 13.e5?! Nxe5! 14.Qg3 O-O 15.cxd4?! Bxd4!.
- Nc6xe5 captured the advanced pawn AND attacked Qf3. Attacking Nf6 did not force that knight to move. d6 guarded Ne5, so Re1's clear file did not provide a cheap recovery.
- Ba7's ray was a7-b6-c5-d4. cxd4 removed c3's pawn and placed it directly on that ray; Bxd4 captured it. White had lost c/d/e pawns against Black's e-pawn: two pawns down. Opening the c-file was no compensation established by calculation.
- e5 and cxd4 were marked inaccurate; no verified best replacements supplied. Sparse marks do not establish the safety of later moves.
16.Nc3 Nh5 17.Qh2 Re8 18.Be3 Nd3 19.Rf1 Bxc3 20.bxc3! Qf6 21.Bd4 Qg6 22.Rad1 Ndf4 23.Kh1 Ne2 24.g4 Nhf4 25.f3 c5 26.Be3 Rxe3.
- Nh5 attacked Qg3. Nd3 then attacked Re1/f2. Track both knights after each move rather than describing general pressure.
- At 18.Be3, f2 guarded e3; Ne5 also screened Re8's file. Ne5-d3-f4-e2 cleared that screen. f2-f3 removed the bishop's pawn guard, so returning Bd4-e3 allowed Re8xe3 through e7/e6/e5/e4. Re-audit a familiar square after intervening pawn and knight moves.
27.Rd2 Rae8 28.Qg1?? Nxg1 29.Rxg1 Qg5 30.Rd5 Qh4 31.Rd2 Qxh3+ 32.Rh2 Qxf3+ 33.Rhg2 Nxg2 34.Rxg2 Qh3+ 35.Kg1 Re1+ 36.Kf2 Qe3#.
- Ne2 attacked g1 directly. Rf1's protection of g1 merely enabled Rxg1 after losing Q for N. A defended destination is insufficient for a queen beside a cheaper capturer.
- Rg2 screened Qf3-g2-h1. Nf4xg2 removed the interposing rook before Rxg2. Check every available capture of a defensive blocker.
- Final Re1+ drove Kg1 to f2; Qe3# was supported by Re8 down the e-file. Earlier h3 luft had no value against this changed net.
- No invalid attempts; 9:26 remained. e5/cxd4 each took 49 seconds, Qh2 70, Kh1 53, Qg1 42. Long thinks missed direct captures; use the deadline to run the destination and guard scan.

## T28 round 3: White vs Sonnet, mate win
Chigorin: 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nf1 a5 15.Ng3 Bd7 16.Be3 Rac8 17.Rc1 h6 18.d5 Nb4 19.Bb1 Qxc1? 20.Bxc1 Rxc1 21.Qxc1.
- Nf1 cleared d2 for Qd1-d4. Bb1 saved the attacked bishop and cleared c2, uncovering Rc1-c7 against Qc7.
- Qxc1 Bxc1 Rxc1 Qxc1 cost Black Q+R against White R+B: queen for bishop. White's queen stayed on d1 until the final horizontal recapture. No forced opening advantage established.
- Rc1 Rxc1+ Qxc1 removed the last rook. Safe minor trades and queen captures left Q versus B. Escorting a4-a8 created another queen; Black's dark bishop could not control a8.
- Qe6/Bg5/Qag8#: Qe6 guarded g8 through f7 and covered h6. Verify queen support and flights; shorten routine conversion.

## T28 round 2: White vs Stockfish, repetition escape
- Be3 blocked Re1-e4; Bxa4 removed Bc2's support of e4. ...exd4 cleared Bb7-e4, enabling ...Nxe4 Nxe4 Bxe4. Re1 could not recapture through Be3.
- Nd2 removed Nf3 from Bb7-g2. ...Qg6 threatened Qxg2#; g3 weakened h3. Qxb5 axb5 opened Ra8-a2 and created a b-passer.
- Kg2 pinned Nd2 to Ra2; Kf1 released it. Ne4 later opened Ra2-e2 while Ba6 guarded e2 through b5/c4/d3. ...Rxe2 Nxc3 Rxe3+ lost a full rook overall; Kxe2 was illegal.
- SF eventually repeated with Q+R versus bare K. Practical escape, not a fortress; 54-57-second losing moves wasted time.

## Retained warnings
- ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5 Bxd5?? Nd3+! Kg1 Qxd5. Rxe5 also needs ...Qf6+ calculation; no verified move-12 replacement.
- Qg1 Re1! Qxe1 Qxe1+ loses Q for R. ...Qb6?? dxe5 uncovers Be3-b6. Qf3 abandons b3 to ...Nb3 against Ra1/Bd2.
- Qg6/Nf5 vs Kg8/Qf7/Nh7: Nh6+ Kh8 Nxf7+ wins Q; Qxf7+ only trades.
- Pinned blockade: ...Rf8 Rxf8+ Nxf8 b8=Q. c2 attacks b1/d1. Ra2?? b3xa2 loses R.
