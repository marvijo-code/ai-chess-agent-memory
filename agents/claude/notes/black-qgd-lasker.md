# Black QGD vs 1.d4 (vs Sol: G13 W, G18 W, T11SF2G1 W; T7SF2G1 L. vs DeepSeek: T19R3 W, T22R2 W, T22R5.2 W)

## Setup (DeepSeek plays it every time)
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Nxe4 dxe4 10.Nd2 f5! 11.f3 exf3, then 12.gxf3 (T22R2) or 12.Nxf3 (T22R5.2) Nc6.

## T22R5.2 vs DeepSeek (WON mate 33, ~1 min used of 15)
12.Nxf3 Nc6 13.Qc2 Bd7 14.Bd3 Rad8 15.O-O Nb4! 16.Qc3 Nxd3 17.Qxd3 Bc6 18.Rfe1 Rfe8 19.Ne5 Be4 20.Qc3 c6 21.Nxc6?? Bxc6 22.Qb3 b6 23.Qd3 Be4 24.Qe2 Rd7 25.Kh1 Kh7 26.Qd3?? Bxd3 27.Kg1 Bxc4 28.Rac1 Bd5 29.Rc8 Rxc8 30.h3 Qb4 31.Rb1 Rc1+ 32.Rxc1 Qxb2 33.Kh2 Qxg2#.
- Plan: Nb4 forks Qc2+Bd3 (Bxf5 fails to Nxc2), trade N for his light bishop, Bc6 then Be4: f5 guards it, so Qxe4 fxe4 loses the queen. 19.Ne5 Be4 20.Qc3 c6 let 21.Nxc6 give a piece for a pawn.
- SF marks: 13...Bd7?!, 14...Rad8?! only minor. Mate net: Qxg2 guarded by Bd5, Kh2 no flight; Rc1+ forced the rook trade. Stalemate checked each ply.

## T22R2 vs DeepSeek (WON mate 32)
12.gxf3 Nc6 13.Be2 Qb4 14.O-O Qxb2 15.Rb1 Qxa2 16.Qb3? Qxb3 17.Nxb3 b6 18.c5 bxc5 19.Nxc5 Rb8 20.Nd7?? Rxb1 21.Rxb1 Bxd7 22.Rb8 Rxb8 23.d5 exd5 24.Bd3 Nb4 25.Bb5 Bxb5 26.Kg2 Rb6 27.h4 Rg6+ 28.Kh2 Bf1 29.h5 Rg2+ 30.Kh3 Nd3 31.f4 Nf2+ 32.Kh4 Rg4#.
- 13...Qb4/14...Qxb2/15...Qxa2: SF marks Qb4??, Qxb2?!. It worked only because DeepSeek played 14.O-O, 15.Rb1, 16.Qb3; the queen can be trapped (a3, Rb1, Nb3). Not vs SF/Sol; safer 13...Bd7 then ...Rad8/...Rae8.
- Mate net: Rg6+, Bf1 (guards g2), Rg2+, Nd3-f2+, Rg4#.

## T19R3 vs DeepSeek (WON mate 23)
10...Nc6?! 11.Nxe4 f5 12.Ng3 Rd8 13.Be2 e5 14.O-O exd4 15.Qxd4?? Nxd4 ... 23.Nf1 Rxf1#.
- 10...Nc6? lost e4: my own e6 pawn blocks Qe7-e4. 10...f5 is the move.

## T11 SF2G1 (WON mate 60): Nb4 fork
...6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Rc1 Nxc3 10.Rxc3 c6 11.Bd3 Nd7 12.O-O dxc4 13.Bxc4 e5 14.Qc2 exd4 15.exd4 Nb6 16.Bb3 Nd5! 17.Rd3? Nb4! 18.Re3 Qxe3! 19.fxe3 Nxc2 20.Bxc2 (exchange up).
- 10...c6 (not ...c5: dxc5 Qxc5?? Rxc5). Conversion: no Rxd4 while d4 has Rd1+K+B. ILLEGAL: 23...Rad8 with Rfd8 on d8.

## T7SF2G1 (LOST mate 52): e-file pin on Be6
...13.Qc2 Be6 14.Rfe1 Rfe8 15.e4 dxe4 16.Bxe4 Nxe4 17.Rxe4 c6 ... 28...Qe7?? 29.d5 hit the pinned bishop. Qe7+Be6+Re8 vs Re4+Re1: every bishop move pinned. Try 13...c6 14.Rfe1 Bf5 (unverified).

## G13 (won 64), G18 (won 66)
- G13: 4.Nc3 Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Rc1 Nxc3 10.Rxc3 dxc4 11.Bxc4 c5 12.O-O Nc6 13.d5 exd5 14.Bxd5 Nb4 ... 17.Qe2? Nd4! 19.Rc5?? Qxc5.
- G18 Exchange: 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 ... 17.Ng3 Rd8? 18.d5 ... 22.Bh7+. Root: Qd7 on the d-file vs Rd1 with Bd3 the sole blocker.

## General
- Lasker is equal; 1-10 s per move in book, 15-30 s at moves 9-18. Sol blunders with no plan; DeepSeek hangs pieces (T22R2: Nd7 fork, Rb8, Bb5; T22R5.2: Nxc6, Qd3). Punish forks (Nb4, Nd4). Before every queen capture list his queen's lines incl. ranks.
