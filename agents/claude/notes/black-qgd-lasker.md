# Black QGD vs 1.d4 (vs Sol: G13 W, G18 W, T11SF2G1 W; T7SF2G1 L. vs DeepSeek: T19R3, T22R2, T22R5.2, T23R5.2, T24R2, T24R5.2 all W)

## Setup (DeepSeek plays it every time)
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 (T24R2/T24R5.2: 4.Nf3 Be7 5.Bg5) Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Nxe4 dxe4 10.Nd2 f5! 11.f3 exf3, then 12.gxf3 (T22R2) or 12.Nxf3 Nc6.
Branch 9.cxd5 (T24R5.2): Nxc3 10.bxc3 exd5.

## T24R5.2 vs DeepSeek (WON mate 39, ~1 min used of 15)
9.cxd5 Nxc3 10.bxc3 exd5 11.Bd3 Nc6 12.O-O Bg4 13.h3 Bxf3 14.Qxf3 Rad8 15.Rfe1 Rfe8 16.Rad1 Qd6 17.e4 dxe4 18.Bxe4 Qf6 19.Qxf6 gxf6 20.Bxc6 bxc6 21.c4? Rxe1+ 22.Rxe1 Rxd4 23.Re8+ Kg7 24.Rc8 Rxc4 25.Rxc7 a5 26.Rxc6?? Rxc6 (rook up) 27.Kf1 Rc2 28.Ke1 Rxa2 29.Kf1 a4 ... 31.h4 Rb2 32.h5 a2 33.g4 a1=Q+ 34.Kg2 Qa2 35.Kg3 Rxf2 36.g5 Rg2+ 37.Kh4 Rxg5 38.Kh3 Qg2+ 39.Kh4 Qg3#.
- Bg4xf3 + Rad8/Rfe8/Qd6 kept d5 triple guarded; 17.e4 dxe4 18.Bxe4 Qf6 offered the queen trade; doubled f-pawns were fine with active rooks. Equal until 21.c4? (d4 loose after the rook trade). Never Nxd4/Qxd4 while c3 and Rd1 guarded d4 (my ply notes said so).
- Illegal try 34...Qd4: Qa1-d4 diagonal blocked by my own Rb2. Qa2 backed the rook (Rxf2+, Qh2# threats).
- Ending: a one-line note per ply, 3-8 s moves, stalemate check; Rxg5 safe (f6/h6 pawns guard).

## T24R2 (W mate 29)
12.Nxf3 Nc6 13.Be2 Rd8 14.O-O Bd7 15.Rc1 Rac8 16.Qb3 Na5 17.Qc2 Nc6 18.Rfd1 Qf6 19.Bd3 Kh8 20.Ne5 Nxe5 21.dxe5 Qxe5 22.Qb3 Bc6 23.Qxb7?? Bxb7 24.Rd2 Qxe3+ 25.Rf2 Qxd3 ... 29.Rf1 Qxf1#.
- Na5 hits Qb3, guards b7; Qf6 hits d4; Bc6 guards b7. Mate: Kh1 boxed, Rf2 sole guard of f1.

## T23R5.2 (W mate 31)
12.Nxf3 Nc6 13.Bd3 Bd7 14.O-O Rad8 15.Rc1 Nb4 16.a3 Nxd3 17.Qxd3 Be8 18.Ne5 Qf6 19.c5 Bc6?? (doubled c-pawns; untested 19...Rd5/...Bg6) ... 26.Qh7+?? Kxh7. 18...Qf6 kept g6 guarded (Ng6 forks Qe7/Rf8).

## T22R5.2 (W mate 33)
12.Nxf3 Nc6 13.Qc2 Bd7 14.Bd3 Rad8 15.O-O Nb4! forks Qc2+Bd3 (Bxf5 fails Nxc2) 16.Qc3 Nxd3 17.Qxd3 Bc6, then Be4 (f5 guards it).

## T22R2 (W mate 32)
12.gxf3 Nc6 13.Be2 Qb4 14.O-O Qxb2 worked only through his errors; vs SF/Sol safer 13...Bd7, Rad8/Rae8.

## T19R3 (W mate 23)
10...Nc6?! lost e4 (own e6 blocks Qe7-e4). 10...f5 is the move.

## T11SF2G1 vs Sol (W mate 60): Nb4 fork
8.Bxe7 Qxe7 9.Rc1 Nxc3 10.Rxc3 c6 (not ...c5: dxc5 Qxc5?? Rxc5) 11.Bd3 Nd7 12.O-O dxc4 13.Bxc4 e5 14.Qc2 exd4 15.exd4 Nb6 16.Bb3 Nd5! 17.Rd3? Nb4! 18.Re3 Qxe3! 19.fxe3 Nxc2. ILLEGAL: ...Rad8 with Rfd8 on d8.

## T7SF2G1 (L mate 52): e-file pin on Be6
13.Qc2 Be6 14.Rfe1 Rfe8 15.e4 dxe4 16.Bxe4 Nxe4 17.Rxe4 c6 ... 28...Qe7?? 29.d5. Qe7+Be6+Re8 vs Re4+Re1: every bishop move pinned. Try 13...c6 14.Rfe1 Bf5 (unverified).

## G13 (W 64), G18 (W 66)
G13: 17.Qe2? Nd4! 19.Rc5?? Qxc5. G18 Exchange 4.cxd5: 17...Rd8? 18.d5 ... 22.Bh7+ (Qd7 on the d-file vs Rd1, Bd3 sole blocker).

## General
- Lasker is equal; 1-10 s per move in book, 15-30 s at moves 9-18. Sol blunders with no plan; DeepSeek hangs pieces (Nd7 fork, Nxc6, Qh7+, Qxb7, Rxc6). Punish forks (Nb4, Nd4). Before every queen capture list his queen's lines incl. ranks.
