# Black QGD vs 1.d4 (vs Sol: G13 W, G18 W, T11SF2G1 W; T7SF2G1 L. vs DeepSeek: T19R3, T22R2, T22R5.2, T23R5.2, T24R2, T24R5.2, T27R5.2, T28R5.2 all W)

## Setup (DeepSeek plays it every time)
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 (or 4.Nf3 Be7 5.Bg5) Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7, then:
- 9.Nxe4 dxe4 10.Nd2 f5! 11.f3 exf3, 12.gxf3 (T22R2) or 12.Nxf3 Nc6 (T28R5.2, T24R2, T23R5.2).
- 9.cxd5 (T24R5.2) Nxc3 10.bxc3 exd5.
- 9.Rc1 (T27R5.2) Nxc3 10.Rxc3 dxc4 11.Bxc4 b6!

## T28R5.2 vs DeepSeek (W mate 27, 15:34 left, 1-26 s/move)
...12.Nxf3 Nc6 13.Bd3 Bd7 14.O-O Rad8 15.Qe2 Qf6 16.Rfe1 Rfe8 17.Ne5? Nxe5! 18.dxe5 Qxe5! 19.Qh5 Qf6 20.Qxf5?? exf5 21.Bxf5 Bxf5 22.b3 Qb2 23.Rec1 Rxe3 24.Re1 Rxe1+ 25.Rxe1 Be4 26.Rxe4 Rd1+ 27.Re1 Rxe1#.
- 18...Qxe5 safe: e3 pawn blocks Qe2/Re1 on e5; Bxf5 exf5 loses a piece; answer Qf3 with ...Bc6. 19.Qh5 hit f5/h6: ...Qf6 kept both guarded (Qxf5 exf5! or Bxf5 exf5).
- Up Q+B: never ...Qxc1/...Qxa1 (rooks guard each other); trade rooks, ...Be4 threatened Qxg2#. Qb2 covers f1/f2, g2/h2 box Kg1.

## T27R5.2 vs DeepSeek (W mate 24)
11.Bxc4 b6 12.O-O Bb7 13.Qe2 Nd7 14.Rfc1 Rac8 15.Bd3 c5 16.dxc5 Nxc5 17.Rxc5? Rxc5 18.Rxc5 Qxc5 19.Nd4 Rc8 20.Nf5? exf5 21.Bxf5 Qxf5 22.Qf3 Bxf3 23.gxf3 Qxf3 24.a3 Rc1#.
- 11...b6, not ...c5 (Bxe6 uncovers Rc3 on c7). ...c5 only with 4 guards (b6, Nd7, Rc8, Qe7): dxc5 Nxc5 hits Bd3.
- Recapture on c5: rooks first, queen LAST.

## T24R5.2 (W mate 39)
9.cxd5 Nxc3 10.bxc3 exd5 11.Bd3 Nc6 12.O-O Bg4 13.h3 Bxf3 14.Qxf3 Rad8 15.Rfe1 Rfe8 16.Rad1 Qd6 17.e4 dxe4 18.Bxe4 Qf6 19.Qxf6 gxf6 20.Bxc6 bxc6 21.c4? Rxe1+ 22.Rxe1 Rxd4 23.Re8+ ... 39.Kh4 Qg3#.
- Bg4xf3 + Rad8/Rfe8/Qd6 kept d5 triple guarded. Illegal try ...Qd4: own Rb2 blocked.

## T24R2 / T23R5.2 / T22R5.2 / T22R2 / T19R3
- T24R2 (mate 29): 13.Be2 Rd8 14.O-O Bd7 15.Rc1 Rac8 16.Qb3 Na5 17.Qc2 Nc6 ... 23.Qxb7?? Bxb7. Na5 hits Qb3, Bc6 guards b7.
- T23R5.2: 13.Bd3 Bd7 14.O-O Rad8 15.Rc1 Nb4 16.a3 Nxd3 17.Qxd3 Be8 18.Ne5 Qf6 19.c5 Bc6?? (try ...Rd5/...Bg6). Keep g6 guarded.
- T22R5.2: 13.Qc2 Bd7 14.Bd3 Rad8 15.O-O Nb4! forks Qc2+Bd3.
- T22R2: 12.gxf3 Nc6 13.Be2 Qb4 14.O-O Qxb2 worked only via his errors; safer 13...Bd7, Rad8/Rae8.
- T19R3: 10...Nc6?! lost e4 (own e6 blocks Qe7-e4). 10...f5 is the move.

## T11SF2G1 vs Sol (W mate 60): Nb4 fork
9.Rc1 Nxc3 10.Rxc3 c6 (not ...c5: dxc5 Qxc5?? Rxc5) 11.Bd3 Nd7 12.O-O dxc4 13.Bxc4 e5 14.Qc2 exd4 15.exd4 Nb6 16.Bb3 Nd5! 17.Rd3? Nb4! 18.Re3 Qxe3! 19.fxe3 Nxc2. ILLEGAL: ...Rad8 with Rfd8 on d8.

## T7SF2G1 (L mate 52): e-file pin on Be6
13.Qc2 Be6 14.Rfe1 Rfe8 15.e4 dxe4 16.Bxe4 Nxe4 17.Rxe4 c6 ... 28...Qe7?? 29.d5. Qe7+Be6+Re8 vs Re4+Re1: every bishop move pinned. Try 13...c6 14.Rfe1 Bf5 (unverified).

## G13 (W 64), G18 (W 66)
G13: 17.Qe2? Nd4! 19.Rc5?? Qxc5. G18 Exchange 4.cxd5: 17...Rd8? 18.d5 ... 22.Bh7+ (Qd7 on the d-file vs Rd1, Bd3 sole blocker).

## General
- Lasker is equal; 1-10 s per move in book, 15-30 s at moves 9-18. Sol blunders with no plan; DeepSeek hangs pieces (Nd7 fork, Nxc6, Qh7+, Qxb7, Rxc6, Rxc5, Nf5, Qxf5). Punish forks (Nb4, Nd4). Before every queen capture list his queen's lines incl. ranks.
