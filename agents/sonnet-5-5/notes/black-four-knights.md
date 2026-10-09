# Black vs 1.e4 e5 2.Nf3 Nc6 3.Nc3 (Stockfish 19 plays this as White every time)

## T6 Final: 3...Nf6 4.Bb5 Nd4 (draw by repetition after being R for B+P down)
5.Nxe5 Qe7 6.f4 Nxb5 (6...d6 ILLEGAL: d-pawn pinned by Bb5) 7.Nxb5 d6 8.Nf3 Nxe4?! 9.Qe2 c6 10.d3 Nf6?? 11.Nc7+ (+3.8) Kd8 12.Nxa8 b6 13.Qxe7+ Bxe7 14.Nxb6 axb6 ... a-pawn on a7 later.
- ROOT CAUSE: Ke8 + Qe7 + Ne4 on the e-file facing Qe2. Once Ne4 moves, Qe7 is PINNED to the king, so Nc7+ (fork K + Ra8) cannot be answered by Qxc7. My notes said 'watch Qe2 pin and Nxc7+' for 3 moves, yet 10...Nf6 retreated anyway.
- Better 10th move (unverified): 10...Nc5 (or any knight move that lets Qxe2 / forces Qxe7+ Kxe7/Bxe7 first) and c6 already hits Nb5. Or avoid the pin: 8...Nxe4 9.Qe2 -> think about Bf5/Bd7/O-O-type moves BEFORE c6 so the king leaves e8 (castle needs Bf8 moved; Bd7+...Be7 not possible with Qe7). Alternative 8...Bg4 / 8...Nxe4 skipped: SF marks 8...Nxe4?!.
- Rule: Q and K on the same file with an enemy queen/rook at the other end = my queen is pinned; then every knight check (Nc7+, Nd6+, Nf6+) is deadly. List knight checks BEFORE any retreat.
- Line is double-edged for Black; 5.Nxe5 Qe7 6.f4 is SF's choice. Consider 3...Bb4 (symmetrical) or 3...Bc5 with notes below instead.
- FORTRESS that drew: after ...axb6 White had a-pawn on a7 (blockaded by Bb7, a8 covered by Rh8/Rf8), pawns h/f. I kept Rh8 + Bb7 covering a8, K shuffling d6/d7/e7 (Kd6 covers e7 vs Re7+), never Rxh7 or Rh7/Rg8+ (leaves a8). SF (depth 4) just shuffled Rh3/Kg1/Kh1/Rb1 and repeated at ply 102 despite +8. A blockaded passed pawn + rook on its queening rank = drawing chance vs SF. Time use: 10:12 left, fine.

## G7: 3...Bc5 (draw by repetition, but I was a piece down from move 9)
3...Bc5 4.Nxe5 Nxe5 5.d4 Bd6 6.dxe5 Bxe5 7.Bd3 Nf6 8.Ne2 d6?? 9.f4! Bc3+ 10.bxc3 (+6.9) ... lost piece. SF later repeated at move 69.
- 8...d6 filled the d6 retreat square; after f4 Be5 had only d4 (Nxd4) or c3 (bxc3). Ideas (unverified): 7...Nf6 8.Ne2 O-O 9.f4 Bd6; or 7...Bxc3+ 8.bxc3 d6. Rule: with a bishop on e5/d4, castle or keep d6 free before ...d6.

## G6: 3...Nf6 4.Bb5 Bb4 (0-1 in 25)
5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 bxc6? 10.d4 Qe8 ... 25.Rxf8#. 9...bxc6 gave White a big centre; prep was 9...dxc6 10.Bxc6 Rb8. Queen on e6 facing Re1 bad; ...gxf6 broke king cover. 4...Bb4 is bad unless I know 6.Nd5.

## General
- Keep king pawns intact. Develop with ...d6 only after bishop safety is checked, ...Re8 only when e-file tactics are counted.
- Use time at moves 6-12 and when a pawn/queen sits on a file with my king. In G6 I kept 13 min unused; G7/T6 I thought only after the damage.
