# White closed Ruy v 3...a6 (W: DeepSeek 8, Sol 6; L v Sol T6R3 T13R2 T16R3 T17R1 T19SF2G1G1 T27SF2G1G1 T33F T35SF2G1; L v SF T24R1; L v Astra T37R5)

Setup: O-O, Re1, Bb3, 8.h3 (luft), c3. Black plays Chigorin (9...Na5), Breyer or 9...Bb7. Plan v Chigorin: Bc2, d4, Nbd2, cxd4, Nb3, Be3, Nbd2 v ...a4, Rc1, Bb1.

## T40SF1G1 v Sol: WON m32 (900+10; 12:59 v 12:00 left)
- Book to 16.Nbd2 Bd7 17.Rc1 Qb7: queen left the c-file, so no d5 (e4 overloaded). 18.Bb1 Rfc8 19.a3 (stops ...Nb4) Na5 20.Rxc8+ Rxc8 21.Qe2 Nc4 22.Nxc4 Rxc4 23.Bd3?! (SF ?!, rook just moved) Rc8 24.dxe5 Nxe4 25.Bxe4 Qxe4 26.Bd4: queen trade with Re1 behind, e5 guarded by Bd4 + Nf3.
- 28.Bxe5 (NOT Nxe5: ...Rc1+ Kh2 Bd6 pins the knight). Then Bd4 offered a bishop trade; 30...Bc6?? left Re8# on the board: no luft, Bc6 the only guard of e8. Bxc5 Bxf3 gxf3 Rxc5 Re8#.
- Model: simplify with a guard list, keep my luft (h3), count HIS rank 8 after every trade. Moves 20-30 took 16-55 s; fine.

## T40R2 v Sol: WON m60
- ...Qb7 left the c-file (Rc1 pins nothing). 20.Bd3?! Be6 opened the b-file with tempo; grabs on b5/a4 came back: level. 27...Ra2?? hung his queen (Qb2 behind it unguarded). Moves 20-27 took 45-65 s; try Rb1/a3/Qd3. Illegal try 36.Bxd6 through own Ne5.

## T39R6.2 v Sol: WON m58
- Nbd2-f1-g3, Bc2, d5 buried ...Bb7; ...Nc4 hit Bc2 (b3). Wandering Bd3-c2 and Bxf4 gave the bishop pair; K shuffled while ...g5-g4 came; he lost it (33...g4??, 41.exf5?? Re3??). Fix: choose the K square once, keep Nf3/Nh2 for g4.

## T38SF2G1 v Sol: WON m81 from a lost ending
- 16.d5?! Na5 equal; then I wandered (Nd2-c4-b2, Bb4, 9-58 s), ...f5! won a pawn; saved by his 56...Qxb4+??. Fix: v ...Bd7/...Rac8 Rc1 + Bb1/Qe2, no d5; name his break (...f5) each move.

## Losses
- T37R5 Astra m48: ...Qb7 left the c-file, 21.d5 gained only space. 23.Rc1?? Rxc1+: Re1 was my ONLY rook (named the mover as recapturer), Nd2 blocked Be3-c1. 40.Qxg6+?? Qxg6 (Qd3 saw g6 via e4-f5).
- T35SF2G1 (piece up): 18...Rfe8?? 19.d5! pinned Nc6 only with Qc7 on the c-file. 30.Qg6+?? fxg6.
- T33F m37: 17.Bd3?! Rfc8 18.Bc2 Nb4 19.Bd3?? Nxd3: Nd2 between Qd1 and d3 (T13R2 same). Play 17.Rc1/Qb1; v ...Nb4 Bb1, a3.
- T27SF2G1G1 (Q+R up): 18.Bd3 unmasked Rc1 on Qc7; 31.Qd1?? cxd1=Q. T24R1 v SF: 18.Rad1?! f5!; 20.g4 opened b7-g2; a piece down: no pawn pushes near K. T19: 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 gave a ...c4 clamp; prefer 14.Nb3. T16R3 b4? e.p. T6R3 Rb5?? Qh2+.

## Habits
- Sol/Astra 3-60 s, raid when my K is thin; DeepSeek hangs pieces when worse; Sol hangs one when level (T40R2 Ra2??, T40SF1G1 Bc6??). Me: book 1-10 s, captures/queen moves 30 s max; list pieces BY SQUARE after every trade; name every recapturer through my own pieces; a pawn grab = write what falls back.
