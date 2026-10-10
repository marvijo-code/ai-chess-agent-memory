# Black QGD vs 1.d4 (vs Sol: G13 W, G18 W, T11SF2G1 W; T7SF2G1 L. vs DeepSeek: T19R3 W, T22R2 W)

## T22R2 vs DeepSeek (WON mate 32, ~2 min used of 15)
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Nxe4 dxe4 10.Nd2 f5 11.f3 exf3 12.gxf3 Nc6 13.Be2 Qb4 14.O-O Qxb2 15.Rb1 Qxa2 16.Qb3? Qxb3 17.Nxb3 b6 18.c5 bxc5 19.Nxc5 Rb8 20.Nd7?? Rxb1 21.Rxb1 Bxd7 22.Rb8 Rxb8 23.d5 exd5 24.Bd3 Nb4 25.Bb5 Bxb5 26.Kg2 Rb6 27.h4 Rg6+ 28.Kh2 Bf1 29.h5 Rg2+ 30.Kh3 Nd3 31.f4 Nf2+ 32.Kh4 Rg4#.
- 10...f5 (T19 note) then 11.f3 exf3 12.gxf3: his g-file and king side are broken (d4/e3/f3 weak); equal at least.
- 13...Qb4 / 14...Qxb2 / 15...Qxa2: SF marks Qb4??, Qxb2?!, Qxb3?. It pins Nd2 and wins 2 pawns but the queen is far from home and can be trapped (a3, Rb1, Nb3, Rb1+Qb3). It worked because DeepSeek played 14.O-O, 15.Rb1, 16.Qb3. Do not repeat vs SF/Sol unverified; safer: 13...Bd7 then ...Rad8 / ...Rae8 hitting d4/e3.
- Conversion: queens off, 17...b6 stopped Nc5; every trick (Nd7 fork, Rb8) answered by trading: Rxb1, Bxd7, Rxb8 won N and R. Mate net: Rg6+, Bf1 (guards g2), Rg2+, Nd3-f2+, Rg4# (f5 covers g4, h6 covers g5). Stalemate checked each ply.
- DeepSeek tried illegal O-O (13) and Bxd5+ (24).

## T19R3 vs DeepSeek (WON mate 23)
...4.Nf3 Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Nxe4 dxe4 10.Nd2 Nc6?! 11.Nxe4 f5 12.Ng3 Rd8 13.Be2 e5 14.O-O exd4 15.Qxd4?? Nxd4 16.exd4 Rxd4 ... 23.Nf1 Rxf1#.
- 10...Nc6? lost e4: my own e6 pawn blocks Qe7-e4. Ask who guards e4 THROUGH which squares. 10...f5 is the move (T22R2).
- Conversion: trade rooks, Be6, Rd2; his K had no luft: Re1+ Nf1 Rxf1#.

## T11 SF2G1 (WON mate 60): Nb4 fork
...4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Rc1 Nxc3 10.Rxc3 c6 11.Bd3 Nd7 12.O-O dxc4 13.Bxc4 e5 14.Qc2 exd4 15.exd4 Nb6 16.Bb3 Nd5! 17.Rd3? Nb4! 18.Re3 Qxe3! 19.fxe3 Nxc2 20.Bxc2 (exchange up).
- 10...c6 (not ...c5: dxc5 Qxc5?? Rxc5). Rd3 walks into Nb4 forking Qc2+Rd3. Conversion: no Rxd4 while d4 has Rd1+K+B; rook behind the a-pawn. ILLEGAL: 23...Rad8 with Rfd8 already on d8; write the rook's square.

## T7SF2G1 (LOST mate 52): e-file pin on Be6
...8.Bxe7 Qxe7 9.cxd5 Nxc3 10.bxc3 exd5 11.Bd3 Nd7 12.O-O Nf6 13.Qc2 Be6 14.Rfe1 Rfe8 15.e4 dxe4 16.Bxe4 Nxe4 17.Rxe4 c6 18.Rae1 ... 28...Qe7?? 29.d5 hit the pinned bishop.
- Qe7+Be6+Re8 vs Re4+Re1: every bishop move pinned. After 13.Qc2 try 13...c6 14.Rfe1 Bf5 (unverified).

## G13 (won 64) and G18 (won 66)
- G13: 4.Nc3 Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Rc1 Nxc3 10.Rxc3 dxc4 11.Bxc4 c5 12.O-O Nc6 13.d5 exd5 14.Bxd5 Nb4 15.Bb3 Bf5 16.a3 Nc6 17.Qe2? Nd4! 18.Nxd4 cxd4 19.Rc5?? Qxc5.
- G18 Exchange: 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 8.Nge2 c6 9.O-O Re8 10.Qc2 Nf8 ... 16.fxe4 Qd7?! 17.Ng3 Rd8? 18.d5 ... 22.Bh7+. Root: Qd7 on the d-file vs Rd1 with Bd3 the sole blocker; move the queen off the file first.

## General
- Lasker is equal; 1-10 s per move in book, 15-30 s at moves 9-18. Sol blunders with no plan; DeepSeek hangs pieces (T22R2: Nd7 fork, Rb8 trade, Bb5 all free). Punish forks (Nb4, Nd4). Before every queen capture list his queen's lines incl. ranks.
