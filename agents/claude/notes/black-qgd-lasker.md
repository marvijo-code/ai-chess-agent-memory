# Black QGD vs 1.d4 (vs Sol: G13 W, G18 W, T11SF2G1 W; T7SF2G1 L. vs DeepSeek: T19R3 W)

## T19R3 vs DeepSeek (WON, mate 23, used ~1 min of 15)
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Nxe4 dxe4 10.Nd2 Nc6?! 11.Nxe4 f5 12.Ng3 Rd8 13.Be2 e5 14.O-O exd4 15.Qxd4?? Nxd4 16.exd4 Rxd4 17.Rfd1 Rxd4... Rxd1+ 18.Rxd1 Be6 19.Rd8+ Rxd8 20.Kh1 Rd2 21.Nf1 Rxe2 22.Ng3 Re1+ 23.Nf1 Rxf1#.
- MY ERROR 10...Nc6?: I wrote 'Qe7 holds e4' but my own e6 pawn blocks e7-e4. 11.Nxe4 won a pawn. Better 10...f5 (pawn guards e4; unverified) or 10...Nd7/Qb4 ideas; first ask who guards e4 THROUGH which squares.
- Recovery: 11...f5 kicked Ne4, ...Rd8 + ...e5 + ...exd4 piled N+R on d4 (Qd4 only defended by e3 pawn). DeepSeek (15 s) took 14...exd4 with the queen. Had it played 15.exd4, ...Nxd4 16.Nxf5? Bxf5 is fine for me at about -0.5; the pawn deficit stays.
- Conversion: trade rooks (Rxd1+), Be6 first (guards f5, clears back rank), then Rd2 hit Be2; DeepSeek's K had g2/h2 pawns, no luft: Re1+ Nf1 Rxf1#. Stockfish marked 9...dxe4!, 8...Qxe7!.

## T11 SF2G1 (WON, mate 60): Lasker, Nb4 fork
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Rc1 Nxc3 10.Rxc3 c6 11.Bd3 Nd7 12.O-O dxc4 13.Bxc4 e5 14.Qc2 exd4 15.exd4 Nb6 16.Bb3 Nd5! 17.Rd3? Nb4! 18.Re3 Qxe3! 19.fxe3 Nxc2 20.Bxc2 (exchange up) Bg4 ... a-pawn queened, Q+R mate 60.
- Setup: 10...c6 (not ...c5: dxc5 Qxc5?? Rxc5), ...Nd7, ...dxc4, ...e5, ...exd4, ...Nb6, ...Nd5 hits Rc3. Rd3 walks into Nb4 (forks Qc2+Rd3).
- Conversion: trade the active bishop, double rooks, but no Rxd4 while d4 has Rd1+K+B. With 2R vs B: rook behind a-pawn, Rc8 stops h-pawn. Stalemate check every ply.
- ILLEGAL: 23...Rad8 when Rfd8 already on d8. Write the rook's square before the move.

## T7SF2G1 (LOST mate 52): e-file pin on Be6
...8.Bxe7 Qxe7 9.cxd5 Nxc3 10.bxc3 exd5 11.Bd3 Nd7 12.O-O Nf6 13.Qc2 Be6 14.Rfe1 Rfe8 15.e4 dxe4 16.Bxe4 Nxe4 17.Rxe4 c6 18.Rae1 Rad8 19.Ne5 Qd6?? ... 28...Qe7?? 29.d5 hit pinned bishop; 30...Bxd5?? 31.Rxe7+.
- Equal to move 18. Qe7+Be6+Re8 on the e-file vs Re4+Re1: every bishop move pinned. Vs the cxd5 line after 13.Qc2 avoid Be6+Qe7 vs Rfe1/e4; try 13...c6 14.Rfe1 Bf5 (unverified).

## G13 (won 64): 4.Nc3 Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Rc1 Nxc3 10.Rxc3 dxc4 11.Bxc4 c5 12.O-O Nc6 13.d5 exd5 14.Bxd5 Nb4 15.Bb3 Bf5 16.a3 Nc6 17.Qe2? Nd4! 18.Nxd4 cxd4 19.Rc5?? Qxc5.

## G18 (won 66): Exchange QGD
4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 8.Nge2 c6 9.O-O Re8 10.Qc2 Nf8 11.f3 Ne6 12.Bh4 h6 13.Rad1 Nh5 14.Bf2 Nf6 15.e4 dxe4 16.fxe4 Qd7?! 17.Ng3 Rd8? 18.d5 ... 22.Bh7+ Kh8 23.Rxd7. Root: Qd7 on d-file vs Rd1 with Bd3 sole blocker; move the queen off the file first.

## General
- Lasker is equal; 1-10 s per move in book, 15-30 s at moves 9-18. Sol blunders with no plan; DeepSeek hangs pieces. Punish forks (Nb4, Nd4). Before every queen capture list his queen's lines incl. ranks.
