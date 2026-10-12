# Sicilian as Black - Alapin/Dragon/Taimanov (g28-g158)

## Taimanov B vs 6.Nxc6/8.e5 clamp (g158 vs SF19, 0-1, Qxg7# m11)
Book: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (15 plies), 9.Qg4. My 8...Nd5! was right (SF's key move was his 9.Nxd4! earlier), but then 9...O-O?? 10.Bh6! Bb7?? 11.Qxg7#.
- The mate: his Qg4 + Bh6 hit g7, whose ONLY guard is my king (Nd5 does not cover g7); two attackers vs one guard. Development was irrelevant.
- Answer the clamp at once: ...d6 (hits e5, opens lines), or ...h6/...Nf6/...Nxc3 to remove the e5 support. NEVER O-O into Qg4 + Bd3.
- My fastest loss: 2-11 s a move, no illegal tries - one unanswered mate question at move 9 decided it. Ask 'what mates if I pass?' from the moment e5 appears.

## Taimanov B, quiet 6.Be2 (g103,g150,g152,g156)
Book: 6.Be2 e6 7.O-O Be7 8.Be3 O-O 9.f4 a6 10.Kh1 Bd7 11.a4 Qc7 12.Bf3 Nxd4 13.Bxd4 (15 plies), then ...Rfe8/...Rad8. His Qe1-g3 + Bd4 battery threatens Qxg7#; my Nf6 is only a SCREEN. Trade the Bd4 or free f6 for ...f6/luft the moment Qg3 appears - never a passive rook shuffle.
- g156 vs Sol (0-1, Qxg7# m22): 15...Qb6?? lost my QUEEN to 16.Bxb6: she stood on that bishop's own d4-b6 diagonal. Before ANY queen move walk every enemy bishop diagonal to its end. 14...Rfe8?!, 14...Rad8?! were the shuffles that let 15.Qg3 come.
- 18.e5 dxe5 19.fxe5 Nh5?? 20.Bxh5 - a loose knight, second gift; 21...Rxc3 was the only grab, then 22.Qxg7#. Never leave loose pieces when he is up a queen.
- g152 (0-1, Qxg7# m19): 15...e5? screened only by a pawn: 16.fxe5 Nxe5 17.Nd5 Qd7?? 18.Bxe5! mate; only 18...f6 blocked. No ...Nd7/...e5 while the battery stands.
- g103 vs Sol (0-1, m33): 12...Bd6?? guarded only by my queen - 13.Qxd6 Qxd6 14.Bxd6 = B+Q for B; 17...Bf5?? Rxf5 on the open f-file. Both 36-38 s thinks.

## Taimanov B, g34 vs GLM (1-0 m26)
6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 a6 10.Be2 Bd7 11.g4 b5 (15 plies) is safe while White has no a4. 13...Bxd4! 14.Qxd4?? Nxd4 = Q for B. Then ...Qc7/...f6/...gxf6/...d5/...Bc6. 24...Qxf4+ 25.Kb1?? dropped Kc1's guard of d2 -> 25...Qxd2 26...Qe1#.

## Alapin 4.c3
- 5.Qxd4: ...Nc6/...g6/...Bg7/...O-O/...Nc5. No ...Nb4, no knight to d4 (12...Nd4?? 13.Rxd4), no ...b5 while Rd1 faces Qd8 (g64: 11...b5?? 12.Bxc5! dxc5 13.Rxd8).
- g95 (0-1, Qe8# m28): 6...Nf6?! allows 7.Nc3!; after 3...d5 the queen MOVES off d5 when hit - 7...e6?? 8.Nxd5 exd5 = Q for N.
- g91 (0-1, Qf7# m22): 10...bxc6! not ...Bxc6?! (11.d5! kicks it); 14...Bxe6! not ...fxe6?! (16.exd6+); 19...Qxd6?? 20.Qxd6+ - the d6-pawn was the last screen on the open d-file.

## Recurring
- QUEEN: hit by anything -> she moves that move; 'defended' never counts. Enemy pawns: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6. Bishop diagonals to her landing square (g91, g156).
- MATE FIRST, quiet moves too: Qg4/Bh6 (g158) and Qg3/Bd4 (g152,g156,g157) - count the guards of g7 BEFORE castling or shuffling. Break the e5 clamp with ...d6.
- SCREEN: a capture on the last screen of his queen/rook file = Q/R for P (g64,g79,g91,g148).
- PIN: verify a recapturer is not pinned (g90). RECAPTURE != TRADE: name my recapturer on the destination.
- Time: book <=10 s, routine <=15 s (g103/g156 36-38 s blunders); long thinks fixed nothing.
