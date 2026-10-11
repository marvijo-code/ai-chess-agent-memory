# Black QGD vs 1.d4 (Sol: G13 W, G18 W, T11SF2G1 W; T7SF2G1 L. DeepSeek: 10 W, T19R3 ... T30R2, T30R5.2)

## Setup (DeepSeek plays it every time)
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 (or 4.Nf3 Be7 5.Bg5) Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7, then:
- 9.Nxe4 dxe4 10.Nd2 f5! 11.f3 exf3, 12.gxf3 (T22R2) or 12.Nxf3 Nc6 (T30R2, T28R5.2, T24R2, T23R5.2).
- 9.cxd5 Nxc3 10.bxc3 exd5 (T24R5.2, T30R5.2).
- 9.Rc1 (T27R5.2) Nxc3 10.Rxc3 dxc4 11.Bxc4 b6!

## T30R5.2 vs DeepSeek (W mate 24; 16:30 v 7:43; 1-18 s/move)
9.cxd5 Nxc3 10.bxc3 exd5 11.Qb3 c6 12.Rc1 Nd7 13.Bd3 Nf6 14.O-O Be6 15.Qc2 Rfe8 16.Rfd1 Rac8 17.c4 dxc4 18.Bxc4 Bxc4 19.Qxc4 Nd5 20.Qc5? Qxc5 21.Rxc5 b6 22.Rxc6?? Rxc6 23.Rc1?? Rxc1+ 24.Ne1 Rxe1#.
- Vs Qb3: ...c6 (Bc8 guards b7), ...Nd7-f6 (Q then guards b7), ...Be6, ...Rfe8, ...Rac8. 17.c4 dxc4 18.Bxc4 Bxc4 trades his active bishop; ...Nd5 hits c3/e3 + blocks d-file; queens off, ...b6 kicks the rook (c6 held by Rc8).
- Back rank: his K had f2/g2/h2 pawns, no luft. After Rc1 Rxc1+ any block (Ne1) falls to Rxe1#. Each move ask 'which of his rooks is unguarded and what is on his first rank?'.
- Play ...Nd5 only with c6 behind it; ...Nxe3 threat needs e3 guarded only by f2.

## T30R2 vs DeepSeek (W mate 21; 14:31 v 9:43)
12.Nxf3 Nc6 13.Bd3 Bd7 14.O-O Rad8 15.Ne5 Nxe5 16.dxe5 Bc6 17.Rc1 Qc5 (...Qxe5 ILLEGAL: own e6 pawn) 18.Qe2 Qxe5 19.c5 Rxd3? 20.Qxd3 Qd5 21.Qc3?? Qxg2#.
- 19...Rxd3? = R for B (Rd3 unguarded). Try 19...Rd5/...Rfe8/...Qd5.
- After f3/Nxf3/Bd3 vanish g2 has only the K: Bc6 + Qd5/Qe4 = Qxg2#. Check each move.

## T28R5.2 (W mate 27)
13.Bd3 Bd7 14.O-O Rad8 15.Qe2 Qf6 16.Rfe1 Rfe8 17.Ne5? Nxe5! 18.dxe5 Qxe5! 19.Qh5 Qf6 20.Qxf5?? exf5 ... 27.Re1 Rxe1#. 19.Qh5 hit f5/h6: ...Qf6 kept both. Up Q+B: trade rooks, ...Be4 threatens Qxg2#.

## T27R5.2 (W mate 24)
11.Bxc4 b6 12.O-O Bb7 13.Qe2 Nd7 14.Rfc1 Rac8 15.Bd3 c5 16.dxc5 Nxc5 17.Rxc5? Rxc5 18.Rxc5 Qxc5 19.Nd4 Rc8 20.Nf5? exf5 ... 24.a3 Rc1#. 11...b6 not ...c5 (Bxe6 uncovers Rc3). Recapture on c5: rooks first, queen last.

## T24R5.2 (W mate 39)
9.cxd5 Nxc3 10.bxc3 exd5 11.Bd3 Nc6 12.O-O Bg4 13.h3 Bxf3 14.Qxf3 Rad8 15.Rfe1 Rfe8 16.Rad1 Qd6 17.e4 dxe4 18.Bxe4 Qf6 19.Qxf6 gxf6 20.Bxc6 bxc6 21.c4? Rxe1+ ... 39...Qg3#. Illegal try ...Qd4: own Rb2 blocked.

## Older v DeepSeek
- T24R2 (m29): 13.Be2 Rd8 14.O-O Bd7 15.Rc1 Rac8 16.Qb3 Na5 ... 23.Qxb7?? Bxb7.
- T23R5.2: 13.Bd3 Bd7 14.O-O Rad8 15.Rc1 Nb4 16.a3 Nxd3 17.Qxd3 Be8 18.Ne5 Qf6 19.c5 Bc6?? (try ...Rd5/...Bg6). Keep g6 guarded.
- T22R5.2: 13.Qc2 Bd7 14.Bd3 Rad8 15.O-O Nb4! forks Qc2+Bd3. T22R2: 12.gxf3 Nc6 13.Be2 Qb4 14.O-O Qxb2; safer 13...Bd7.
- T19R3: 10...Nc6?! lost e4 (own e6 blocks Qe7-e4). 10...f5 is the move.

## v Sol
- T11SF2G1 (W m60): 9.Rc1 Nxc3 10.Rxc3 c6 (not ...c5) 11.Bd3 Nd7 12.O-O dxc4 13.Bxc4 e5 14.Qc2 exd4 15.exd4 Nb6 16.Bb3 Nd5! 17.Rd3? Nb4! 18.Re3 Qxe3! ILLEGAL: ...Rad8 with Rfd8 on d8.
- T7SF2G1 (L m52): 13.Qc2 Be6 14.Rfe1 Rfe8 15.e4 dxe4 16.Bxe4 Nxe4 17.Rxe4 c6 ... 28...Qe7?? 29.d5. Try 13...c6 14.Rfe1 Bf5.
- G13 (W): 17.Qe2? Nd4! 19.Rc5?? Qxc5. G18 Exchange 4.cxd5: 17...Rd8? 18.d5 ... 22.Bh7+.

## General
- Lasker is equal; 1-10 s per move in book, 15-30 s at moves 9-18. DeepSeek hangs pieces and back ranks (Nd7 fork, Nxc6, Qh7+, Qxb7, Rxc6, Nf5, Qc3?? v Qxg2#, Rc1?? v Rxe1#). Punish forks (Nb4, Nd4). Before every queen/rook capture list his recapturers incl. queen lines on ranks.
