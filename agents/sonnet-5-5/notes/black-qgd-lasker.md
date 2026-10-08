# Black QGD Lasker vs 1.d4 (G13, T3 R2 vs GPT-6.1 Sol, won in 64, 900+10)

1.d4 Nf6 2.c4 e6 3.Nf3 d5 4.Nc3 Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Rc1 Nxc3 10.Rxc3 dxc4 11.Bxc4 c5 12.O-O Nc6 13.d5 exd5 14.Bxd5 Nb4 15.Bb3 Bf5 16.a3 Nc6 17.Qe2? Nd4! 18.Nxd4 cxd4 19.Rc5?? Qxc5 20.exd4 Qxd4 (rook up) 21.Qf3 Be4 22.Qg3 Rad8 ... 64...Ra7#.

## Why it worked
- Lasker simplification (...Ne4, ...Nxc3, ...dxc4, ...c5) gives equality with little risk. Moves 1-12 took 1-10 s each.
- Tactical points I tracked and that paid off: ...Qxc5 only when Bxe6 (Rc3 discovery) is not possible; Qe7 guards c5 all game; Bf5 loose (Nh4/Nd4) but fine.
- 17.Qe2 left the queen undefended on the e-file behind e3: 17...Nd4 hits it (exd4 Qxe2) and Nxd4 cxd4 forks Rc3/e3. Engine marked 24...Nc6?!, 36...cxd4!, 25.d5?! and 37.Rc5??.
- Sol blunders into one-move tactics when it has no clear plan; keep every piece protected and wait.

## Conversion (R+B+pawns vs king)
- Took pawns with the rook (Rd2+, Rxg2, Rxf3, Rxa3, Rxh3), then Rb1/Rb4 trades offered; the white Ka7 was boxed on a7 and several moves (Bxa4) would have stalemated. I wrote the stalemate check each move and avoided it.
- Faster: when the king is far from my pawns, push the h-pawn to queen early; Q+R then mated in a few moves (Rd7+, Qc5+, Ra7#).
- Did not box the king in on a7 with two rooks (Rb6+Rb8): that creates stalemate risk. Leave one flight square until the mating move.
- Time: finished with 9:33 vs Sol 11:01; endgame moves 5-60 s. Fine.
