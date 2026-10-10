# Yugoslav Dragon as Black - 9.O-O-O (g75,g79,g80,g81,g83,g86)

## g86 vs Stockfish19 (0-1, Rh8# m29) - queen trade + 3 blunders
9.O-O-O d5 10.exd5 Nxd5 11.Nxc6 bxc6! 12.Nxd5 cxd5! 13.Qxd5 Qc7! 14.Qc5 Qxc5? 15.Bxc5 Bf5?? 16.Bxe7 Rfe8 17.Bg5! Bd3?! 18.Bxd3 Rab8 19.b3 h6 20.Bd2 Rb4 21.c3 Rxb3 22.axb3 Bxc3 23.Bf4 Rb8?? 24.Bxb8.
- 14...Qxc5? (SF ?; 0.00 -> +1.43): trading lets 15.Bxc5! use the clear c5-e7-f8 line (my d6-pawn left with ...d5 on m9; e7 loose, f8-rook kicked). Decline: 14...Qd8/...Qb6, keep queens.
- 15...Bf5?? dropped e7. Defend what his last bishop move attacks before developing: 15...Rfe8 (e8 defends e7, so 16.Bxe7 Rxe7 = B for P).
- 17...Bd3?! 18.Bxd3: my bishop onto the f1-bishop's ray (f1-e2-d3, e2 empty) with no recapture of mine (both c-pawns long gone). Check his bishop diagonals to my destination.
- 23...Rb8?? 24.Bxb8: last rook onto the f4-bishop's diagonal (f4-e5-d6-c7-b8, all empty). Walk every enemy bishop diagonal to its edge before a rook swing.
- 2 illegal tries: f5-bishop cannot reach e7 (f5-e6-d7-c8/e4-d3/g4-h3/g6-h7); c3-bishop cannot reach f3 (c3-d4-e5-f6/b4-a5/d2-e1). Trace bishop paths twice; 3 = forfeit.
- Clock 4:19 vs 19:49: 41-54 s routine (10...Nxd5 46, 12...cxd5 54, 13...Qc7 41, 16...Rfe8 1:51, 25...a6 44) and 15...Bf5 (39 s), 17...Bd3 (43 s) still blundered. Routine <=15 s.

## g83 vs Stockfish19 (0-1, m30) - 13...e6?? lost a rook
13.Qxd5 -> 13...Qc7! ONLY (13...e6/...Be6: Qd8 defended only by Rf8; after Qxd8 Rxd8 Rxd8+ my a8-rook cannot reach d8 - own Bc8 blocks rank 8 = Q+R for Q). Free the a8-rook with ...Rb8 early; f3-a8 diagonal = Bxa8 once open.

## g81 vs Stockfish19 (0-1, m29) - 17...dxe5?? took the last screen
9.O-O-O Nxd4 10.Bxd4 Be6 11.h4 Qa5 12.h5 Nxh5 13.Bxg7 Kxg7? 14.g4 Nf6 15.Qh6+ Kg8 16.Kb1 Qd8 17.e5 dxe5?? 18.Rxd8.
- 17...dxe5?? his Rd1 faced Qd8 with only the d6-pawn between: pushing the last blocker lost the queen. Meet 17.e5 with ...Nfd7; keep d6.
- 13...Nxg7! (knight from h5), not Kxg7?: the king recapture walks into g4/Qh6.

## g80/g79 - condensed
- g80: 12.Nxd5 -> pawn recapture 12...cxd5! (Qd8 keeps d5 guarded); 12...Qxd5? drops a pawn. 21...Rd2+?? undefended rook onto Be3/Kc2 = 22.Bxd2.
- g79: 18...Qe6?! queen on rank 6 with his Qh6 + screens Nf6/g6; 19.g5, 20.h5 removed the last -> 21.Qxe6. With one screen left, move the QUEEN off the rank first.

## g75/g71 - condensed
- g75 vs SF (1/2): 13...Qc7! only (13...Qxd5? after 44s). 18...Rb5?! 19.Rxb5 Bxb5 20.Bxb5: count ALL his attackers. 3x repetition = half point.
- g71: 13...Qc7!; 14...Qb6? 15.Qxb6 axb6.

## Rules
- 13.Qxd5 -> 13...Qc7! ONLY; after 14.Qc5 do NOT trade - keep queens (Qd8/Qb6).
- Queens on one rank/file: count screens; never move the last one (g79,g81,g83).
- Rook swings: count ALL his attackers incl. every bishop diagonal; a check changes nothing (g80,g86).
- Routine <=15 s; every long think in this line still blundered; lost 1-5 s; repetition = half point.
