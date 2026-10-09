# Four Knights as Black - 4.Bb5 Bb4 (g3,g4,g11,g14,g17,g20,g24,g25 - all lost)

## g25 vs Stockfish 19 (0-1, mated m18)
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 Nd4 8.Nxd4 exd4 9.b3 Bc5 10.a4.
- 10...d3?! 11.Bxd3: pushing the passed pawn to d3 just loses it (c2 was defended; the f1-bishop takes it free). Play ...d6/...Re8/...a5, finish development, hit d5. Eval -0.02 -> +1.18.
- 12.Qh5: his Bd3 covers h7 AND g6. Defense: 12...g6! (attacks the queen and blocks the d3-h7 diagonal, so Qxh7+ no longer works).
- 12...Qf6?? 13.Qxh7+! (Kxh7 illegal: Bd3 covers h7) Kf8 14.Rb1; king stuck, 17.Re1+ Kd8 18.Rxe8# (Qg6 defended e8). Qf6 is only fine when it truly defends the hit pawn and no Qxh7+ sac exists (cf. g17, where Qf6 was correct).
- 14...Qg6?? 15.Bxg6: never put the queen on the d3-g6-h7 bishop diagonal; scan bishop lines on every queen move.
- c8-bishop blocked by the d7-pawn: ...Bg4/...Be6/...Bf5 illegal before ...d6 (g25 tried Bg4, 87s, 1 illegal attempt; g24 ...Bg4?? hxg4).
- Clock: 50/40/87/44/54s on moves 9-14; routine moves need <=15s.

## g24 vs Stockfish 19 - never ...Bg4 after h3
6.Re1 d6 7.h3 Bxc3 8.bxc3 Re8 9.d4 exd4 10.cxd4.
- 10...Bg4?? 11.hxg4 Nxg4 = B for P (engine +8): with h3 played the Rubinstein ...Bg4 is dead; play ...Bd7/...Ne7.
- 10.c3 attacks Bb4 -> retreat (...Ba5/Be7/d6); 10...Bxc3?? dxc3 = B for P (g11); same as 8...Bxd2?? (g4).
- Down a piece: 30-56s/move only delayed mate; play 5-15s.

## 6.Nd5 lines (g3,g4,g11,g14,g17,g20)
- 6.Nd5 -> 6...Nxd5! (7.exd5 Nd4!); 6...Be7?! lets 7.c3 and 9.Nxe5! (g20).
- g14 (11.Qf3): do not open with ...c6/...cxd5: 12.Bd3 cxd5? 13.Bb2! ... 15.Qxd5 wins d5 and d4. Keep d4 covered, c-file closed.
- 6...Be7: 10...Bc5 11.d4 Bb6 12.Bd3 d6 solid (g3); 13.Nc4! b5! 14.Nxb6 axb6 = B for N.
- ...c6 boxes the c8 bishop while the d7-pawn sits; free with ...d6 first (g14).

## g17 vs Stockfish 19 (0-1, mated m14)
9.b3 a6 10.Bd3 Re8 11.Qg4 Qf6! (fine here) 12.Bb2 Qd6?? 13.Qxd4! Qxd5?? 14.Qxg7#.
- 12...Qd6?? abandons d4 (d7-pawn blocks the retreat) and allows Qxd4/Qxg7# with Bb2.
- 13...Qxd5?? grabbed a pawn with mate on the board: defend the mate first.
- 10...c6! > ...Re8 (keeps Rf8 for the dark squares).
- Context decides: Qf6 fine at g17, blunder at g25.

## Legality (g11,g14,g16,g24,g25)
- d5-knight: c7 e7 b6 f6 b4 f4 c3 e3 (not d2). c8-bishop blocked by d7/b7 pawns. Own piece blocks (g16 20...f5 with Nf6). Check before submitting; illegal tries waste clock.

## Late blunders
- g11 25...Bf5?? Nxf5; 26...Qxb4?? cxb4. g14 17...Qe1+?? Rxe1, then 19.Re8#. g3 15...Ne4?? Bxe4; 19...Qxe4?? Rxe4. g4 10...Nf4?? Qxf4; 13...Re8?? Qxe8#.
- Back rank: king h8/c8/d8 with no luft and an enemy Q/R: keep a guard (g19 33...Rc8?? Qxc8#; g25 18.Rxe8#).
- Down material: 5-15s, defend loose pieces, no grabs.

## Working setup
- ...d6/...c6/...Re8; keep f7 covered, d4 defended, e5/f6 occupied or g7 guarded. White's b3/Bb2/Bd3/Qh5 aim at d4/g7/h7: keep h7 defended or blocked (...g6); never a queen on g6/h7.
