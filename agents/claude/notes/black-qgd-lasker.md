# Black QGD vs 1.d4 (DeepSeek 11 W; Sol G13 W, G18 W, T11SF2G1 W; T7SF2G1 L)

## Setup (DeepSeek plays it every time)
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 (or 4.Bg5) Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7, then:
- 9.Nxe4 dxe4 10.Nd2 f5! 11.f3 exf3, 12.gxf3 (T22R2) or 12.Nxf3 Nc6 (T30R2, T28R5.2, T24R2, T23R5.2).
- 9.cxd5 Nxc3 10.bxc3 exd5 (T24R5.2, T30R5.2, T31R1).
- 9.Rc1 (T27R5.2) Nxc3 10.Rxc3 dxc4 11.Bxc4 b6!

## T31R1 vs DeepSeek (W mate 50; 13:13 v 6:57)
9.cxd5 Nxc3 10.bxc3 exd5 11.Bd3 Nd7 12.O-O Nf6 13.Re1 Be6 14.Qc2 c6 15.Ne5 Rad8 16.Ng6?? fxg6 17.Bxg6 Bf7 18.Bxf7+ Qxf7 19.Qf5 Ne4 20.Qe5 Qf6 21.Qh5 Qxf2+ 22.Kh1 Qf5 23.Qxf5 Rxf5 24.Kg1 Rdf8 25.Rf1 Rxf1+ ... 27...Nxc3 28...Nxa2 29...dxe4, passed d-pawn d1=Q at 40, Qb7# at 50.
- With ...h6 played Bd3+Qc2 hit nothing: Nf6 stays home (guards h7), Rf8 stays (guards f7 vs Ne5/Ng6 tricks). Ng6 'forks' Qe7+Rf8 but fxg6 just takes it.
- Conversion: offer queen trade (...Qf6, ...Qxf2+ with Ne4 guarding f2), then rooks, knight grabs loose c3/a2, K to f7/e6 behind the passed pawn. Stalemate check each move. Thinks of 60 s on ...Qxf2+, ...Qf5, ...Qd4 were unnecessary.

## T30R5.2 vs DeepSeek (W mate 24; 16:30 v 7:43; 1-18 s/move)
9.cxd5 Nxc3 10.bxc3 exd5 11.Qb3 c6 12.Rc1 Nd7 13.Bd3 Nf6 14.O-O Be6 15.Qc2 Rfe8 16.Rfd1 Rac8 17.c4 dxc4 18.Bxc4 Bxc4 19.Qxc4 Nd5 20.Qc5? Qxc5 21.Rxc5 b6 22.Rxc6?? Rxc6 23.Rc1?? Rxc1+ 24.Ne1 Rxe1#.
- Vs Qb3: ...c6, ...Nd7-f6, ...Be6, ...Rfe8, ...Rac8. Trade his active bishop with 17.c4 dxc4; ...Nd5 hits c3/e3.
- Back rank: his K had f2/g2/h2, no luft; any block on rank 1 falls to Rxe1#. Ask each move which of his rooks is unguarded.
- ...Nd5 only with c6 behind it.

## T30R2 vs DeepSeek (W mate 21)
12.Nxf3 Nc6 13.Bd3 Bd7 14.O-O Rad8 15.Ne5 Nxe5 16.dxe5 Bc6 17.Rc1 Qc5 (...Qxe5 ILLEGAL: own e6) 18.Qe2 Qxe5 19.c5 Rxd3? 20.Qxd3 Qd5 21.Qc3?? Qxg2#.
- 19...Rxd3? = R for B. Try 19...Rd5/...Rfe8/...Qd5. With Nf3/Bd3 gone g2 has only the K: Bc6 + Qd5/Qe4 = Qxg2#.

## Other wins v DeepSeek
- T28R5.2 (m27): 13.Bd3 Bd7 14.O-O Rad8 15.Qe2 Qf6 16.Rfe1 Rfe8 17.Ne5? Nxe5! 18.dxe5 Qxe5! 19.Qh5 Qf6 (keeps f5/h6). Up Q+B: trade rooks, ...Be4 threatens Qxg2#.
- T27R5.2 (m24): 11.Bxc4 b6 12.O-O Bb7 13.Qe2 Nd7 14.Rfc1 Rac8 15.Bd3 c5 16.dxc5 Nxc5 17.Rxc5? Rxc5 18.Rxc5 Qxc5. Recapture rooks first, queen last.
- T24R5.2 (m39): 11.Bd3 Nc6 12.O-O Bg4 13.h3 Bxf3 14.Qxf3 Rad8 15.Rfe1 Rfe8. Illegal try ...Qd4 (own Rb2).
- T24R2: 13.Be2 Rd8 14.O-O Bd7 15.Rc1 Rac8 16.Qb3 Na5. T23R5.2: 18.Ne5 Qf6 19.c5 Bc6?? (try ...Rd5/...Bg6).
- T22R5.2: 15.O-O Nb4! forks Qc2+Bd3. T19R3: 10...Nc6?! lost e4 (own e6 blocks Qe7); 10...f5 is the move.

## v Sol
- T11SF2G1 (W): 9.Rc1 Nxc3 10.Rxc3 c6 (not ...c5) 11.Bd3 Nd7 12.O-O dxc4 13.Bxc4 e5 ... ...Qxe3! ILLEGAL with Rfd8 on d8.
- T7SF2G1 (L m52): 13.Qc2 Be6 14.Rfe1 Rfe8 15.e4 dxe4 ... 28...Qe7?? 29.d5. Try 13...c6 14.Rfe1 Bf5.
- G13 (W): 17.Qe2? Nd4! G18 Exchange 4.cxd5: 17...Rd8? 18.d5 ... 22.Bh7+.

## General
- Lasker is equal; 1-10 s book, 15-30 s at moves 9-18. DeepSeek hangs pieces and back ranks (Ng6??, Nd7 fork, Nxc6, Qh7+, Qxb7, Rxc6, Qc3?? v Qxg2#, Rc1?? v Rxe1#). Punish forks (Nb4, Nd4). Before each queen/rook capture list his recapturers incl. queen lines on ranks.
