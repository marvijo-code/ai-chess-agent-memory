# Black vs 1.e4 e5 2.Nf3 Nc6 3.Nc3 (Stockfish 19 plays this as White every time)

## 3...Nf6 4.Bb5 Nd4 5.Nxe5 Qe7 6.f4 Nxb5 7.Nxb5 d6 8.Nf3 Nxe4?! 9.Qe2 ... (T6 final AND T8R3: SAME BLUNDER TWICE)
- 6...d6 is ILLEGAL (d-pawn pinned by Bb5). I tried it in T6 and again in T8R3 (2 illegal tries). Play 6...Nxb5 directly.
- T6: 9...c6 10.d3 Nf6?? 11.Nc7+ Kd8 12.Nxa8 (+3.8). T8R3: 9...d5 10.d3 Nd6?? 11.Nxc7+ Kd8 12.Qxe7+ Bxe7 13.Nxa8 (+6.6).
- ROOT CAUSE: Ke8 + Qe7 + Ne4 on the e-file facing Qe2, with Nb5 still alive. Any Ne4 retreat lets Qxe7+ or Nc7+ fork K+Ra8. After 8...Nxe4 White's d3 hits the knight and every retreat loses the exchange. The notes said 'watch Nxc7+' and I still moved the knight.
- FIX (unverified): do NOT play 8...Nxe4. Candidates: 8...Bg4 (develop, keep e4 pawn issue for later), or 8...c6 (kicks Nb5; 9.Nxd6+ Qxd6, 9.Nc3 Bg4). Or choose another line: 3...Bb4 (symmetrical, untested) or 3...Bc5 (G7 below).
- If already in the pin: before any knight move, list Nxc7+ / Nd6+ forks. Ideas: ...f5 to hold e4; or ...Bd7 with Kd8 ready. Count c7 defenders (Qe7 is the only one).

## Fortress that drew twice (T6, T8R3), down exchange + 2 pawns (+5..+8)
- T8R3 final: bishop g4/h5 pawn protect each other, king active to e4/f3/g2 (won h2), bishop on the c8-h3 diagonal vs White's c-pawn (c6/c7), K never next to the Rook checks without cover. White had R+c6 vs B+h5.
- Final shuffle: Bd5 hits c6, Be6 covers c8/d7; SF (depth 4) shuffled Ra3/Rc3 and repeated at ply 120 despite +5. Never play Bxc6 when Rxc6 follows; never Kxg3 when Rxg4+ hxg4 and the c-pawn runs.
- T6 fortress: a-pawn on a7 blockaded by Bb7, Rh8 covering a8. SF repeats when it cannot make progress, so holding is realistic vs SF at depth 4; keep every piece protected, make small threats, never leave the blockading piece.
- Other illegal try T8R3: 38...Bd5 (own king on c6 blocked the diagonal). Trace paths.

## G7: 3...Bc5 (draw by repetition, piece down from move 9)
3...Bc5 4.Nxe5 Nxe5 5.d4 Bd6 6.dxe5 Bxe5 7.Bd3 Nf6 8.Ne2 d6?? 9.f4! Bc3+ 10.bxc3 (+6.9). 8...d6 filled the retreat square; with a bishop on e5/d4 castle or keep d6 free first. Ideas: 8...O-O 9.f4 Bd6.

## G6: 3...Nf6 4.Bb5 Bb4 (0-1 in 25)
5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 bxc6? 10.d4 Qe8 ... 25.Rxf8#. Prep was 9...dxc6 10.Bxc6 Rb8. 4...Bb4 is bad unless I know 6.Nd5.

## General
- Keep king pawns intact. ...d6 only after bishop safety is checked, ...Re8 only when e-file tactics are counted.
- Use time at moves 6-12 (T8R3: 53 s at move 10 but on the wrong question; ask 'what does his best reply do', not 'is my move safe').
