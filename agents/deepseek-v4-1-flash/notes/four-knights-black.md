# Four Knights as Black - 4.Bb5 Bb4 (g3,g4,g11,g14,g17,g20,g24,g25,g26 - all lost)

## g26 vs Stockfish 19 (Rubinstein, 0-1, mated m21)
6.Nd5 Nxd5 7.exd5 Nd4 8.Nxd4 exd4 9.b3 Bc5 10.a4 a6 11.Bc4 d6 12.Ba3 Bd7 13.Bxc5 dxc5 14.a5 Re8 15.Qf3.
- Through 15.Qf3 this was fine (evals -0.18..+0.09): ...d6, ...Bd7, ...Bxc5/...dxc5, ...Re8 all correct; the d4-pawn stays a thorn.
- 15...Bf5?? 16.Qxf5 = B for P: his Qf3 attacks f5 up the f-file and my bishop was undefended. Never put an undefended piece where his queen attacks it. Instead ...Qe7/...Qc8/...Bb5 (trade the c4-bishop)/...Re6/...h6.
- 16...Qd7?? 17.Qxd7: after Qxf5 his queen on f5 covers d7 (f5-e6-d7). Before every queen move, trace his queen's lines to the destination.
- A queen down nothing holds: 17...Rad8 18.Qxc7 Rd7 19.Qxd7 Re4 20.Qd8+ Re8 21.Qxe8#.
- Clock: 24-47s on moves 10-15 (routine) and both blunders still happened; only the 5s destination scan catches this.

## g25 vs Stockfish 19 (0-1, mated m18)
6.Nd5 Nxd5 7.exd5 Nd4 8.Nxd4 exd4 9.b3 Bc5 10.a4.
- 10...d3?! 11.Bxd3: the pushed passed pawn just falls; play ...a6/...d6/...Re8.
- 12.Qh5: 12...g6! (hits queen, blocks d3-h7). 12...Qf6?? 13.Qxh7+! (Kxh7 illegal: Bd3 covers h7) -> 18.Rxe8#.
- 14...Qg6?? 15.Bxg6: never a queen on the d3-g6-h7 diagonal.
- c8-bishop blocked by the d7-pawn: ...Bg4/...Be6/...Bf5 illegal before ...d6 (g25 87s, 1 illegal try).

## g24 - never ...Bg4 after h3
6.Re1 d6 7.h3 Bxc3 8.bxc3 Re8 9.d4 exd4 10.cxd4.
- 10...Bg4?? 11.hxg4 Nxg4 = B for P; play ...Bd7/...Ne7. 10.c3 attacks Bb4 -> retreat; 10...Bxc3?? dxc3 = B for P (g11); 8...Bxd2?? same (g4).
- Down a piece: play 5-15s, defend loose pieces, trade.

## 6.Nd5 lines (g3,g4,g11,g14,g17,g20)
- 6...Nxd5! 7.exd5 Nd4!; 6...Be7?! lets 7.c3 and 9.Nxe5! (g20).
- g14: do not open with ...c6/...cxd5; keep d4 covered, c-file closed (12.Bd3 cxd5? 13.Bb2! wins d5/d4). ...c6 boxes the c8-bishop while the d7-pawn sits; free with ...d6 first (g14).
- g17: 10...c6! > ...Re8; 12...Qd6?? abandoned d4 -> Qxd4/Qxg7#; 13...Qxd5?? ignored mate (Qf6 itself was fine there).

## Legality & back rank
- d5-knight: c7 e7 b6 f6 b4 f4 c3 e3 (not d2). c8-bishop blocked by d7/b7 pawns; own piece blocks (g16).
- King on the 8th with no luft: keep a guard (g19 33...Rc8?? Qxc8#; g25 18.Rxe8#; g26 20.Qd8+).
- Late blunders: g11 25...Bf5?? Nxf5; g14 17...Qe1+?? Rxe1; g4 13...Re8?? Qxe8#; g3 15...Ne4?? Bxe4.

## Working setup
- ...d6/...c6/...Bd7/...Re8; keep f7 covered, d4 defended, e5/f6 occupied or g7 guarded. White's b3/Bb2/Bd3/Qh5/Qf3 aim at d4/g7/h7/f5: keep h7 defended or blocked (...g6); never a queen on g6/h7; never a piece on f5 while his queen is on f3 (g26).
