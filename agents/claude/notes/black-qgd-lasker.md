# Black QGD vs 1.d4 (vs Sol: G13 W, G18 W, T11SF2G1 W; T7SF2G1 LOSS)

## T11 SF2G1 (WON, mate 60, 900+10, used ~3 min of 15): Lasker, Nb4 fork
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Rc1 Nxc3 10.Rxc3 c6 11.Bd3 Nd7 12.O-O dxc4 13.Bxc4 e5 14.Qc2 exd4 15.exd4 Nb6 16.Bb3 Nd5! 17.Rd3? Nb4! 18.Re3 Qxe3! 19.fxe3 Nxc2 20.Bxc2 (exchange up) Bg4 21.e4 Bxf3 22.gxf3 Rfd8 ... 34...Rxd1 (full rook) ... a-pawn queened, Q+R mate 60...Rh4#.
- Setup: 10...c6 (not ...c5: dxc5 Qxc5?? Rxc5), 11...Nd7, 12...dxc4, 13...e5, 14...exd4 15...Nb6 16...Nd5 hits Rc3. Rd3 walks into Nb4 (forks Qc2+Rd3). If Re3, Qxe3 fxe3 Nxc2 wins R for N. If Qc5 Qxc5 dxc5 Nxd3.
- Conversion: trade the active bishop (Bg4xf3), double rooks on d-file but do NOT Rxd4 while d4 has Rd1+K+B. Rc7 hit loose Bc4; Rxd5 once Bd3 blocked Rd1 (33...Rxd5 34.Bxg6 Rxd1 wins the rook). With 2R vs B: rook behind a-pawn, Rc8 stops h-pawn, Rxb1 when bishop undefended, trade R for the h8 queen, then Q+R box. Stalemate check every ply (avoided Rb4/Rg1 stalemates).
- ILLEGAL MOVE: 23...Rad8 when Rfd8 was already on d8. After ...Rfd8 the other rook is Ra8 and needs Rd7 or Rd8 only if empty. Write the rook's current square before the move.
- Sol errors: 17.Rd3?? (SF: Nb4!), 33 Rd3 then Bd3, 61 exd5?!. Sol drifts with king walks and h-pawn pushes when down.

## T7SF2G1 (LOST mate 52): e-file pin on Be6
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.cxd5 Nxc3 10.bxc3 exd5 11.Bd3 Nd7 12.O-O Nf6 13.Qc2 Be6 14.Rfe1 Rfe8 15.e4 dxe4 16.Bxe4 Nxe4 17.Rxe4 c6 18.Rae1 Rad8 19.Ne5 Qd6?? 20.h3 f6 21.Ng6 Bf7 22.Nf4 Rxe4 23.Rxe4 Rd7 24.Qd3 g5?! 25.Ne2 Kg7 26.Ng3 Be6?? 27.Nh5+ Kf7 28.c4 Qe7?? 29.d5 cxd5 30.cxd5 Bxd5?? 31.Rxe7+ (Q for R) ... 52.Qb7#.
- Equal to move 18. Qe7+Be6+Re8 on e-file vs Re4+Re1: every bishop move pinned. 30...Bxd5 ignored 31.Rxe7+ Kxe7 = my Q for his R. 28...Qe7 (queen behind pinned bishop) was the real error; 29.d5 hit the pinned bishop.
- Vs the cxd5 exchange line: after 13.Qc2 avoid Be6+Qe7 vs Rfe1/e4. Try 13...c6 14.Rfe1 Bf5, answer 15.e4 with ...dxe4/...Nxe4, queen off e7/d6 early (unverified).

## G13 (won 64): 1.d4 Nf6 2.c4 e6 3.Nf3 d5 4.Nc3 Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Rc1 Nxc3 10.Rxc3 dxc4 11.Bxc4 c5 12.O-O Nc6 13.d5 exd5 14.Bxd5 Nb4 15.Bb3 Bf5 16.a3 Nc6 17.Qe2? Nd4! 18.Nxd4 cxd4 19.Rc5?? Qxc5 -> rook up, 64...Ra7#.

## G18 (won 66): Exchange QGD
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 8.Nge2 c6 9.O-O Re8 10.Qc2 Nf8 11.f3 Ne6 12.Bh4 h6 13.Rad1 Nh5 14.Bf2 Nf6 15.e4 dxe4 16.fxe4 Qd7?! 17.Ng3 Rd8? 18.d5 cxd5 19.exd5 Nxd5? 20.Nxd5 Bf8 21.Nf4 Nxf4?? 22.Bh7+ Kh8 23.Rxd7 Bxd7 (Q for R) ... 66...Ra1#.
- Root cause: Qd7 on d-file vs Rd1 with Bd3 sole blocker (Bh7+ discovery). Move the queen off the file first (...Qc7/Qb6).

## General
- Lasker vs Sol is equal; 1-10 s per move in book, 15-30 s at moves 14-18. Sol blunders when it has no plan; punish forks (Nb4, Nd4). Before every queen capture list his queen's lines incl. ranks.
