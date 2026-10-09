# Black vs 1.e4 e5 2.Nf3 Nc6 3.Nc3 (Stockfish 19 plays this as White every time)

## 3...Nf6 4.Bb5 Nd4 5.Nxe5 Qe7 6.f4 Nxb5 7.Nxb5 d6 8.Nf3 Nxe4?! 9.Qe2 ... (T6 final AND T8R3: SAME BLUNDER TWICE)
- 6...d6 is ILLEGAL (d-pawn pinned by Bb5). Play 6...Nxb5 directly.
- T6: 9...c6 10.d3 Nf6?? 11.Nc7+ Kd8 12.Nxa8. T8R3: 9...d5 10.d3 Nd6?? 11.Nxc7+ Kd8 12.Qxe7+ Bxe7 13.Nxa8.
- ROOT CAUSE: Ke8 + Qe7 + Ne4 on the e-file facing Qe2 with Nb5 alive. Any Ne4 retreat loses the exchange.
- FIX (unverified): do NOT play 8...Nxe4. Try 8...Bg4 or 8...c6. Or choose 3...Bb4 (untested) or 3...Bc5 (G7).

## Fortress that drew twice (T6, T8R3), down exchange + 2 pawns
- T8R3: bishop g4/h5 pawn protect each other, king active e4/f3/g2, bishop on c8-h3 diagonal vs the c-pawn. SF (depth 4) shuffled and repeated at ply 120 despite +5. Never play Bxc6 when Rxc6 follows; never Kxg3 when Rxg4+.
- T6: a-pawn on a7 blockaded by Bb7, Rh8 covering a8. Holding is realistic vs SF; keep every piece protected.
- Other illegal try T8R3: 38...Bd5 (own king on c6 blocked). Trace paths.

## G7: 3...Bc5 (draw, piece down from move 9)
4.Nxe5 Nxe5 5.d4 Bd6 6.dxe5 Bxe5 7.Bd3 Nf6 8.Ne2 d6?? 9.f4! Bc3+ 10.bxc3. 8...d6 filled the retreat square; try 8...O-O 9.f4 Bd6.

## G6: 3...Nf6 4.Bb5 Bb4 (0-1 in 25)
5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 bxc6? 10.d4 ... Rxf8#. Prep 9...dxc6 10.Bxc6 Rb8. 4...Bb4 is bad unless I know 6.Nd5.

## G11: Caro-Kann Advance vs SF (lost in 34)
1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 Ne7 6.a3 c5 7.Bg5 Nbc6?? 8.Nb5! a6 9.Nd6+ Kd7 10.Nxf7 forks Qd8/Rh8. After ...c5 d6 has no pawn cover; Bg5 pins Ne7 to Qd8. Before ...c5/...Nbc6/...a6 ask: can a knight land on b5 with Nd6+/Nc7+? Try 7...Qb6 or 7...h6 8.Bxe7 Qxe7. Then 33...Bf7?? walked into Rxf7#. SF did NOT repeat when I was lost. Better: skip Caro, play 1...e5 with a prepared line.

## General
- Keep king pawns intact. ...d6 only after bishop safety is checked, ...Re8 only when e-file tactics are counted.
- Use time at moves 6-12 on 'what does his best reply do', not 'is my move safe'.
