# White closed Ruy vs 3...a6 (W: DeepSeek 8, Sol 2; L v Sol T6R3, T13R2, T16R3, T17R1, T19SF2G1G1, T27SF2G1G1, T33F; L v SF T24R1)

Setup: O-O, Re1, Bb3, c3, h3 (9.h3). Black plays Chigorin (9...Na5) or Breyer (9...Nb8). Plan v Chigorin: Bc2, d4, Nbd2, cxd4, then Nb3 a5 Be3 a4 Nbd2 (T27 W).

## T33F vs Sol: LOST mate 37 (11:48 left, I was never short of time)
- Chigorin: 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.Bd3?! Rfc8 18.Bc2 Nb4 19.Bd3?? Nxd3 (11 plies).
- 17.Bd3 'hits b5' but Nd2 sits between Qd1 and d3: the bishop had NO guard. 18.Bc2 took 58 s, then 19.Bd3 'offer a trade, Nxd3 Qxd3': Qd1 cannot reach d3. A free piece. Same error T13R2 (Bd2 blocked Qd1).
- Better: 17.Rc1 (T27) or 17.Qb1; v ...Nb4 Bc2 is guarded by Qd1 (Nxc2 Qxc2), or Bb1 then a3. Never a bishop on d3 while a minor piece shares the d-file with Qd1.
- A piece down he traded Q (...Qc2) and R (...Rc2), then ...d5, ...Ne4, ...dxe4: a supported passed e-pawn. 32.Nxe4?! made it; 34.h4 and 35.Nf1 lost the race (e3, e2, e1=Q, mate). Keep knights on, K to f2/e3 at once, no pawn moves.
- Check that would have saved it: 'which of my pieces guards d3?' (5 s).

## T27SF2G1G1 vs Sol: LOST mate 47 from Q+R up
- Opening plan was right (SF marks 13...Bb3, cxd4 good). 18.Bd3 unmasked Rc1 on Qc7; 18...Qb6? 19.dxe5! opened Be3 v Qb6 (dxe5/Nxe5 both lose the Q).
- 31.Qd1??: I wrote 'attacks c2 and covers c1' but the c2 pawn simply captures d1 (pawn hits b1/d1). Fix: 31.Rc3 or 31.Qc4. I was still Q+R v R+pawn; my K then walked to a1 and Qb2#.
- Habit: moves 28-31 took 12-20 s with no pawn-capture check. In a won game list pawn captures and promotion squares for EVERY queen/rook move.

## T24R1 vs SF: LOST mate 24
- 5...b5 6.Bb3 Bc5 7.d3 d6 8.c3 h6, equal to 17; 18.Rad1?! f5! 19.Nxf5?? Rxf5: Ng3 was the capturer, so f5 had NO guard. 20.g4 opened b7-g2 (Nxe3 then Qh1#). A piece down: no pawn pushes near the king.
- Ideas: 18.Bxb6 then Nh4/Qe2; earlier d4/a4; keep Bd3 instead of 16.Bxd5.

## T19SF2G1G1 vs Sol: LOSS (flagged ply 130)
- 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 gave a ...c4 clamp + ...Bd6; 21.Bxc5 made the clamp pawn. 55-61 s per quiet move 22-42. Prefer 14.Nb3 a5 15.Be3 a4 16.Nbd2 (won T27).

## T17R1 / T16R3 / T13R2 vs Sol: LOSSES (mate about 40)
- T17R1: d5, Nb4, Bb1, Na6, a3, Nc5, then Bxc5 dxc5 and ...c4: rook up and lost it all. Try 17.Rc1/17.Qd2.
- T16R3: 20.Bc2?? Nc5 21.b4? axb3 e.p. and ...Ncxe4! (Be3 blocked Re1). Never b4; keep Bb1.
- T13R2: 14.d5 Nb8 ... 22.Nxf6+ Bxf6 23.Bd3?? Nxd3 (Bd2 blocked Qd1). Keep Be3; answer ...Nc5 with Bxc5.

## Wins
- T10 SF1G1 (DeepSeek, mate 24): 14.Nb3 Rac8 15.Nxa5 Qxa5 16.Bd2 Rfd8?? 17.Bxa5. T10R3 (mate 23): Nbd2, Nf1-g3, d5 c4, Nf5, Bg5 ... Qxh7#.
- T8R2 vs Sol (mate 52): 14.d5 Nd8, Nf1-g3, Bd2, Qe2, Rac1. Breyer G19 (mate 34): 9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4.
- T6R3 vs Sol LOSS from won: 18.Qe2 Qb6?? 19.dxe5! ... 37.Rb5?? Qh2+. Mate-threat check first.

## Habits
- Sol 3-55 s, finds raids when my king is thin; converts anything given. DeepSeek hangs pieces when worse.
- Me: 1-10 s on book, 30-45 s at captures/trades/queen moves; 15 s quiet; trace recaptures, screens and PAWN captures even in standard or won positions. Every piece landing on d3/c2/b1: name the guard THROUGH my own pieces.
