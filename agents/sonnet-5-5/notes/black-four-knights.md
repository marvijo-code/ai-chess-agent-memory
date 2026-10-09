# Black vs 1.e4 e5 2.Nf3 Nc6 3.Nc3 (Stockfish 19 plays this as White every time)

DECISION: stop 3...Nf6 vs SF (4.Bb5 Bb4 lost G6 and T9R3 to 6.Nd5; 4.Bb5 Nd4 lost the same way twice). Next game play 3...Bc5 (G7 was equal, see below) and keep a written reply for 4.Nxe5.

## T9R3: LOST in 19 (3...Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5)
6...Nxd5 7.exd5 Ne7 8.Nxe5 Nxd5 9.Bc4 Nf6 10.c3 Bd6? 11.d4 Bxe5? 12.dxe5 (+1.6) Ne8 13.Qh5 d6 14.Bg5 Qd7 15.f4 dxe5 16.fxe5 Qg4 17.Bxf7+ Rxf7 18.Qxf7+ Kh8 19.Qxe8#.
- 12.dxe5 hits Nf6: Nd5 Bxd5 (d7 blocks my Qd8), Ng4 and Nh5 lose a piece. Ne8 then blocked my back rank. Engine marks: 11...Bxe5?!, 15...dxe5?.
- Root: 10.c3 hit Bb4 and 10...Bd6 11.d4 left Bd6 and Nf6 both pinned to tactics. Try 9...Nb6 or 10...Ba5/Bxc3, but calculate d4 and Nxf7 first (unverified). Better still: avoid the line.
- My notes said '4...Bb4 is bad unless I know 6.Nd5' and I chose 7...Ne7 (not the prepared 7...e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bxc6 Rb8). Moves took only 5-30 s; I had 14 min left.

## 3...Nf6 4.Bb5 Nd4 5.Nxe5 Qe7 6.f4 Nxb5 7.Nxb5 d6 8.Nf3 Nxe4?! 9.Qe2 (T6 and T8R3: SAME BLUNDER TWICE)
- 6...d6 is ILLEGAL (d-pawn pinned by Bb5). Play 6...Nxb5 directly.
- T6: 9...c6 10.d3 Nf6?? 11.Nc7+ Kd8 12.Nxa8. T8R3: 9...d5 10.d3 Nd6?? 11.Nxc7+ Kd8 12.Qxe7+ Bxe7 13.Nxa8.
- Root: Ke8 + Qe7 + Ne4 on the e-file facing Qe2 with Nb5 alive. Any Ne4 retreat loses the exchange. Don't play 8...Nxe4 (try 8...Bg4 / 8...c6, unverified).

## Fortress that drew twice (T6, T8R3), down exchange + 2 pawns
- T8R3: bishop g4/h5 pawn protect each other, king active e4/f3/g2, bishop on c8-h3 diagonal vs the c-pawn. SF shuffled and repeated at ply 120 despite +5. Never play Bxc6 when Rxc6 follows; never Kxg3 when Rxg4+.
- T6: a-pawn on a7 blockaded by Bb7, Rh8 covering a8. Keep every piece protected. Other illegal try T8R3: 38...Bd5 (own king on c6).

## G7: 3...Bc5 (draw, piece down from move 9) - THE LINE TO PLAY
4.Nxe5 Nxe5 5.d4 Bd6 6.dxe5 Bxe5 7.Bd3 Nf6 8.Ne2 d6?? 9.f4! Bc3+ 10.bxc3. 8...d6 filled the retreat square; play 8...O-O 9.f4 Bd6.

## G6: 3...Nf6 4.Bb5 Bb4 (0-1 in 25)
5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 bxc6? 10.d4 ... Rxf8#. Prep 9...dxc6 10.Bxc6 Rb8.

## G11: Caro-Kann Advance vs SF (lost in 34)
1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 Ne7 6.a3 c5 7.Bg5 Nbc6?? 8.Nb5! a6 9.Nd6+ Kd7 10.Nxf7 forks Qd8/Rh8. Before ...c5/...Nbc6/...a6 ask: can a knight land on b5 with Nd6+/Nc7+? Then 33...Bf7?? walked into Rxf7#. Skip Caro; play 1...e5.

## General
- Keep king pawns intact. ...d6 only after bishop safety is checked, ...Re8 only when e-file tactics are counted.
- Use time at moves 6-12 on 'what does his best reply do', not 'is my move safe'.
