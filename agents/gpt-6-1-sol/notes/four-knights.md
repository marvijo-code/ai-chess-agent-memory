# Four Knights: defense before activity

## Shared opening
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4. Both pairs of knights disappear.
After ...Be6 Bxe6 fxe6 Qb3, Qe7 defends Bb4 along e7-d6-c5-b4 and e6 vertically. Qd5?? merely attacks Qb3 and permits Qxb4.

## T10 round 3: Black vs Stockfish 19, checkmate loss
10...Qe7 11.d3 Be6 12.a3 Bd6 13.Re1 Rae8 14.Bxe6 fxe6 15.Qe2 e5 16.Qe4 Qf6 17.Re2 Qg6 18.Qxg6 hxg6!.
- Early Qe7 supported Bb4 before developing Be6. This avoided the previous exposed-bishop problem; unmarked moves do not establish an optimal repertoire.
- The forced queen recapture was marked only good. An open h-file was a possibility, not proof of useful rook activity or a favorable endgame.

19.Bd2 Kf7 20.Rae1 Re7 21.g3 Rfe8 22.Re4 Kf6 23.Kg2 c5 24.h4 Rh8? 25.Bg5+ Ke6 26.Bxe7 Kxe7.
- Kf6/Re7 lay on Bg5-f6-e7. Before h4, Kxg5 could capture a bishop checking from g5; h4 protected that square and enabled the skewer.
- Rh8 pursued the open file without addressing the new protected check. Moving the king exposed Re7; Bxe7 traded White's bishop for my rook. Bd6's protection and Kxe7 recovered the bishop but did not prevent losing the exchange.
- The issue was the king-rook alignment and White's newly protected checking square, not merely whether Re7 had defenders. No engine-best replacement was supplied.

27.f4 Kf6 28.fxe5+ Ke6 29.exd6+ Kxd6.
- fxe5+ captured the central pawn, checked Kf6, and attacked Bd6. Ke6 allowed exd6+; vacating e5 uncovered Re4's check along the e-file.
- Kxd6 recovered only the attacking pawn. White retained two rooks against one, with no bishop left for Black.

30.Re6+ Kd5 31.R1e5+ Kd4 32.Re4+ Kd5 33.c4#.
- c2-c4 checked Kd5. Re6 covered c6/d6 and Re4 covered d4/e5; the rooks protected each other on the e-file. White's d3 pawn protected c4, and my c5 pawn occupied an escape square.
- A central king against two rooks can be mated by a pawn check even without queens. Enumerate escape squares before approaching pawns.
- Finished with 10:11 and no illegal attempts. Rh8 took 43 seconds and Kf6 at move 27 took 58; time shortage did not explain the misses.

## T5 round 3: repetition escape
13.d4 Rad8 14.c3 Bd6! 15.Qxb7 Qh4 16.f4 Rf6?! 17.g3 Qh3 18.Qxc6 Rh6 19.Qg2 Qf5 20.Bd2 Rg6 21.b3 h5 22.b4 h4 23.Rae1 h3?! 24.Qe4.
- f4 blocked Bd6's mating diagonal. Qg2 defended h2; the queen-rook battery did not force mate. Rf6 defended e6, while Rh6 abandoned it.
- ...h3 stopped attacking g3, let Qg2 leave, and remained blocked by h2. Pawn proximity did not establish a breakthrough.
24...Qg4 25.a4 Re8 26.Qd3 Qh5 27.c4 Rg4 28.Re2 Qf5 29.Rf3 g5 30.Qxf5 exf5 31.Rxe8+ Kg7.
- The forced queen recapture removed e6, the sole screen between Re2 and Re8, losing a rook outright. Inspect resulting files before offering queen exchanges.
- Later Kxg5 captured one White rook but Rxc6 captured my last rook. White retained a rook, promoted, and eventually repeated with Q+R against king and pawns. Depth-4 survival was not a theoretical draw or compensation.

## Earlier failures
- ...Qh4 f4 Bxf4? Bxf4 Rxf4 Qxc6 Ref8 Qxe6+ Kh8 Qe2 Re4 Rxf8#: Rf4 blocked Rf1 and could recapture on f8; Re4 removed both functions. g7/h7 denied escapes.
- Rxf8+ Qxf8 Bxh6 gxh6 left White Q+R against Q. Rf1 Qe3+ Kh1 Qxc3 ignored Rf8#.
- T4: ...Rgf8 occupied Bh6's escape square; Rf6 Bf4 Rxf4 won it because f7 blocked the rook recapture. ...c5 allowed en passant dxc6+. Bc5+ Bxf8 skewered king and rook. Rg2+ Kh8 Rh4# exploited my h2 pawn blocking Rh1.
- ...Qe1+ Rxe1 fxe3 Rxf8+ Bxf8 lost queen for rook: Ra1 could capture through clear b1/c1/d1. Repetition did not establish compensation.
- ...Rd1+ Kf2 Rd2+ Ke1 h6 Kxd2 lost the attacked rook. Creating luft did not answer its capture.
