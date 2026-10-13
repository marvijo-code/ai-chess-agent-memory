# White closed Ruy v 3...a6 (W: DeepSeek 8, Sol 5; L v Sol T6R3 T13R2 T16R3 T17R1 T19SF2G1G1 T27SF2G1G1 T33F T35SF2G1; L v SF T24R1; L v Astra T37R5)

Setup: O-O, Re1, Bb3, c3, h3 (9.h3). Black plays Chigorin (9...Na5), Breyer (9...Nb8) or 9...Bb7. Plan v Chigorin: Bc2, d4, Nbd2, cxd4, Nb3, Be3, Nbd2 v ...a4, Rc1, Bb1.

## T40R2 v Sol: WON m60 (queen won at move 29)
- Book to 15.Be3 Rfc8 16.Rc1 a5 17.Bb1 Qb7: the queen left the c-file, so Rc1 pins nothing and d5 only gains space. 18.Nbd2 a4 19.Qe2 Na5 (Qxa4?? bxa4; Nb3? axb3).
- 20.Bd3?! Be6: Bb1 had left b2, so the b-file opened with tempo. 21.Bxb5 Rcb8 22.Bxa4 Qxb2 23.Rc2?! Qb4 hit Ba4 24.Bb3 Bxb3 25.axb3 Nxb3 26.Nxb3 Qxb3: two pawns won, one back, level. Moves 20-27 took 45-65 s and found nothing. Try Rb1/a3/Qd3 before the grab (unverified).
- 27.Rec1 Ra2?? 28.Rxa2 Qxa2 29.Qxa2: his queen behind the rook had no guard (22 s, correct). Then Qd5/Qc4 off pawn squares, Nxe5, Bf4 + Nc6 fork, Nxe7+, d-passer, K walk, Qh8# at 3-30 s a move.
- Illegal try 36.Bxd6 through my own Ne5: write Bf4-e5-d6. After 36.Nc6 the bishop line was clear.

## T39R6.2 v Sol: WON m58 (900+10), equal until his pawn storm failed
- Black ...Bb7, ...Re8, ...Bf8, ...h6, ...Na5, ...c5. Me: Nbd2-f1-g3, Bc2, d5 (Bb7 buried). ...Nc4 hit Bc2: b3 Nb6, a4 b4, cxb4 cxb4, Bd2 a5, Rc1, Nf5. Level.
- 26.Bd3? Nc5 hit it: Bc2 back, 2 tempi, 106 s. 29.Bxf4? gave him the bishop pair + e-file. K shuffled Kh1/Kg1 and Nh2-f3-h2-f1 while ...g5-g4-g3 came.
- He lost it: 33...g4??, 37...Be5??, 41.exf5?? Re3?? 42.Rxe3 won a rook. Queens off, Rc7+, f-pawn queened, stalemate check.
- Fix: K square chosen once (Kg1 + h3), Nf3/Nh2 kept for g4, before a second pawn grab list his captures/checks on Qd2/Bc2/Rc1 (...Nd3, ...Nxb3, ...Qxc2).

## T38SF2G1 v Sol: WON m81 from a lost ending
- Book to 15.Be3 Rac8. 16.d5?! Na5 17.Nxa5 Qxa5 18.Bd2 Qc7 19.Bb1 a5: equal. 20.Rc1 ILLEGAL (own Bb1); Bd3 then Rc1, queens off m25.
- Then I wandered (Bb4, Kf1-e2, Rb7, Nd2-c4-b2, 9-58 s a move); ...f5!, ...fxe4, Nxg4 won a pawn, his h-pawn queened m53. Saved by 56...Qxb4+??. Then b-pawn + K walked, mate m81.
- Fix: v ...Bd7/...Rac8 play Rc1 + Bb1/Qe2, no d5. Level ending: Kf2/f3 so e4 is solid; name his break (...f5) each move.

## T37R5 v Astra: LOST mate 48 (equal to move 22)
- Same book; ...Qb7 left the c-file: no pin on Nc6, 21.d5 only gains space. 22.Rxc8 Rxc8 equal.
- 23.Rc1?? Rxc1+: my ONLY rook was Re1 ('Re1 recaptures' named the mover); Qe2 does not see c1, Be3 blocked by Nd2. First Qd1/Qe1 or Nb3/Bd3 (unverified). Later 40.Qxg6+?? Qxg6 (Qd3 saw g6 via e4-f5).

## T35SF2G1 v Sol: LOST m49 from a piece up
- 18...Rfe8?? 19.d5! pinned Nc6 to Qc7 by Rc1 (only with Qc7 on the c-file). Attack then 30.Qg6+?? fxg6: pawn diagonals before a queen check.

## T33F v Sol: LOST mate 37
- 17.Bd3?! Rfc8 18.Bc2 Nb4 19.Bd3?? Nxd3: Nd2 sat between Qd1 and d3 (T13R2 same). Play 17.Rc1 or Qb1; v ...Nb4 Bb1 then a3. A piece down: keep knights on, K to f2/e3, no pawn moves.

## Older losses and wins
- T27SF2G1G1 (Q+R up, m47): 18.Bd3 unmasked Rc1 on Qc7; 18...Qb6? 19.dxe5! opened Be3; 31.Qd1?? cxd1=Q (c2 pawn hits d1/b1).
- T24R1 v SF: 5...b5 6.Bb3 Bc5 7.d3 equal; 18.Rad1?! f5! 19.Nxf5?? Rxf5; 20.g4 opened b7-g2. A piece down: no pawn pushes near K.
- T19: 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 gave ...c4 clamp + ...Bd6; prefer 14.Nb3. T16R3 21.b4? e.p.: never b4. T13R2 23.Bd3?? Nxd3. T6R3 37.Rb5?? Qh2+.
- Wins v DeepSeek/Sol: T10SF1G1 Nb3, Nxa5 Qxa5, Bd2 Rfd8?? Bxa5; T10R3 Nf1-g3, d5 c4, Nf5, Bg5, Qxh7#; T8R2 d5 Nd8, Ng3, Bd2, Qe2, Rac1.

## Habits
- Sol/Astra 3-60 s, raid when my K is thin, convert anything given; DeepSeek hangs pieces when worse; Sol hangs one when level (T40R2 Ra2??). Me: book 1-10 s, captures/queen moves 30 s max; list pieces BY SQUARE after every trade; name every recapturer through my own pieces; a pawn grab = write what falls back.
