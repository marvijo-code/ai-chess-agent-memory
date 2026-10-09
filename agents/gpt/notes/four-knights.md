# Four Knights: defense before activity

## Shared opening
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4. Both pairs of knights disappear.
After ...Be6 Bxe6 fxe6 Qb3, Qe7 defends Bb4 along e7-d6-c5-b4 and e6 vertically. Qd5?? merely attacks Qb3 and permits Qxb4.

## T13 round 1: Black vs Stockfish 19, mate loss
10...Be6 11.Bxe6 fxe6! 12.Qb3 Qe7 13.d4 Rab8 14.Be3 Bd6 15.Rae1 Kh8 16.h3 e5 17.Bd2 Qf6 18.dxe5 Bxe5! 19.Bb4 Rfd8 20.Re4 Rd4?! 21.Re3 Bf4? 22.Bc3! Bxe3 23.fxe3 Rd3 24.cxd3.

### Crossed attacks and an illegal imagined recapture
- Before ...Bf4, Qf6 defended Be5 and Rd4. Attacking Re3 did not force a retreat: Bc3 created an x-ray on Qf6 through my Rd4.
- ...Bxe3 won a rook for bishop temporarily. f2xe3 then attacked Rd4, which still screened Bc3-d4-e5-f6. Moving that rook would expose my queen.
- My proposed ...Rxc3 after fxe3 was impossible: a rook on d4 cannot capture diagonally on c3. Rb8 could not capture c3 either. Verify movement geometry before evaluating a liquidation.
- ...Rd3 attacked Qb3 through Bc3, but c2xd3 simply captured the rook while uncovering Bc3's attack on Qf6. Counterattacking did not force Bxf6 or a queen retreat.
- After ...Qg6, Black had lost R+B for White's R: a bishop deficit. No engine-best replacement for ...Rd4 or ...Bf4 was supplied; prevent the crossed attacks before assuming the exchange is profitable.

### Checking clearance wins the queen
24...Qg6 25.Rf7 Qxd3 26.Bxg7+! Kg8 27.Qxd3 Kxf7.
- Qb3 already lined up with Qd3, screened only by White's Bc3. Bxg7+ removed that screen with check. Black had to answer the check before White captured Qd3.
- Rf7 protected Bg7, preventing Kxg7. Kxf7 later recovered only the rook; White retained Q+B against R.
- Before placing a queen behind an enemy blocker, calculate that blocker's checks and captures. Its departure can uncover a queen attack with tempo.
- Finish: ...Rg8 Qf5+ Ke7 Qf6+ Kd7 Qf7+ Kc8 Qe6+ Kb8 Qxg8#. Bd4 covered a7; Black's b7/c7 pawns enclosed the king.
- No invalid submissions. Had 12:43 after ...Rd3 and 11:41 before mate. ...Bf4 took 35 seconds, ...Bxe3 41, ...Rd3 65: ample calculation time still missed geometry and direct pawn capture.

## T10 round 3: Black vs Stockfish, mate loss
10...Qe7 11.d3 Be6 12.a3 Bd6 13.Re1 Rae8 14.Bxe6 fxe6 15.Qe2 e5 16.Qe4 Qf6 17.Re2 Qg6 18.Qxg6 hxg6!.
19.Bd2 Kf7 20.Rae1 Re7 21.g3 Rfe8 22.Re4 Kf6 23.Kg2 c5 24.h4 Rh8? 25.Bg5+ Ke6 26.Bxe7 Kxe7.
- Kf6/Re7 lay on Bg5-f6-e7. h4 protected the checking bishop and enabled the skewer. Bd6's defense and Kxe7 did not prevent losing the exchange. No best replacement for ...Rh8 was supplied.
- 27.f4 Kf6 28.fxe5+ Ke6 29.exd6+ Kxd6 lost Bd6. The pawn capture cleared Re4's checking file.
- Re6+ Kd5 R1e5+ Kd4 Re4+ Kd5 c4#: d3 protected c4, rooks covered escapes, and my c5 pawn enclosed the king. Finished with 10:11.

## Earlier failures and repetition escapes
- ...Qh4 f4 Bxf4? Bxf4 Rxf4 defused the attack. ...Ref8 abandoned e6. Rf4 blocked Rf1 and could recapture on f8; ...Re4 removed both duties, allowing Rxf8#. ...Qe3+ Kh1 Qxc3 also ignored Rf8#.
- T5: f4 blocked Bd6's mating diagonal; Qg2 defended h2. Rf6 defended e6, Rh6 abandoned it. ...h3 released Qg2 without breaking through h2.
- Qxf5 exf5 cleared e6, the only screen between Re2 and Re8, allowing Rxe8+. Later repetition against promoted Q+R did not establish compensation or a theoretical draw.
- ...Rgf8 occupied Bh6's escape; Rf6 Bf4 Rxf4 won it because f7 blocked the recapture. ...c5 allowed en passant dxc6+.
- ...Qe1+ Rxe1 fxe3 Rxf8+ Bxf8 lost queen for rook: Ra1 had a clear path through b1/c1/d1.
- ...Rd1+ Kf2 Rd2+ Ke1 h6 Kxd2 lost the attacked rook. Creating luft did not answer its capture.
