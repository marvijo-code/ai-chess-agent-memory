# White closed Ruy vs 3...a6 (W: DeepSeek 8; Sol SF2G1, T8R2; L vs Sol: T6R3, T13R2, T16R3, T17R1, T19SF2G1G1, T27SF2G1G1; L vs SF T24R1)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3. Black: Chigorin (9...Na5) or Breyer (9...Nb8).

## T27SF2G1G1 vs Sol: LOST mate 47 from Q+R up (0-1; 11:49 v 12:30 at end)
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.Rc1 Rac8 18.Bd3 Qb6?? 19.dxe5! Nxe5 20.Bxb6 Rxc1 21.Qxc1 Nxd3 22.Qc7 Rc8 23.Qxb7 Re8 24.Re3 Nxb2 25.Bd4 Nc4 26.Nxc4 bxc4 27.Bxf6 Bxf6 28.Qb4 c3 29.Nd4 Bxd4 30.Qxd4 c2 31.Qd1?? cxd1=Q+ 32.Kh2 Qd4 ... 47...Qb2#.
- Opening plan was right (SF marks 13...Bb3, 25 cxd4 good). 18.Bd3 unmasked Rc1 on Qc7; 18...Qb6? let 19.dxe5 open Be3 vs Qb6 (dxe5/Nxe5 both lose the Q).
- 31.Qd1??: I wrote 'attacks c2 and covers c1' but the c2 pawn simply captures d1 (pawn hits b1/d1). Fix: 31.Rc3 or 31.Qc4 (c-file contact, c1 covered), I was still Q+R v R+pawn.
- Habit: moves 28-31 took 12-20 s with no pawn-capture check. In a won game list pawn captures and promotion squares for EVERY queen/rook move.
- After it: Q v pawns, no counterplay; king walked f1-e1-d1-c1-b1-a1 to ...Qb2#.

## T24R1 vs SF: LOSS (mate 24)
5...b5 6.Bb3 Bc5 7.d3 d6 8.c3 h6 9.Nbd2 Bb6 10.h3 O-O 11.Re1 Ne7 12.Nf1 c5 13.Ng3 Qc7 14.Be3 d5 15.exd5 Nfxd5 16.Bxd5 Nxd5 17.Qd2 Bb7 18.Rad1?! f5! 19.Nxf5?? Rxf5 20.g4 Rxf3 21.Qe2 Rf6 ... 24.Rxe3 Qh1#.
- Equal to 17. 19.Nxf5??: Ng3 was the capturer, so f5 had NO guard. 20.g4 opened b7-g2 (Nxe3 then Qh1#). A piece down: no pawn pushes near the king.
- Ideas: 18.Bxb6 then Nh4/Qe2; earlier d4/a4; keep Bd3 instead of 16.Bxd5.

## T19SF2G1G1 vs Sol: LOSS (flagged ply 130)
...12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Ng3 Bd7 19.Be3 Rfc8 20.Bd3 a4 21.Bxc5?! dxc5 22.Qd2 c4 ... 32.Nxc4?? bxc4 33.Rxc4 Nb3.
- 14.d5 gave ...c4 clamp + ...Bd6; 21.Bxc5 made the clamp pawn. Clock 55-61 s per quiet move 22-42. Prefer 14.Nb3 a5 15.Be3 a4 16.Nbd2 (won T27).

## T17R1 / T16R3 / T13R2 vs Sol: LOSSES (mate 40/40/39)
- T17R1: 17.d5?! Nb4 18.Bb1 Na6 19.a3 Nc5 20.Bxc5 dxc5 21.Nf1 c4 ... rook up and lost it all. Try 17.Rc1/17.Qd2.
- T16R3: ...17.d5 Nb4 18.Bb1 Rfc8 19.a3 Na6 20.Bc2?? Nc5 21.b4? axb3 e.p. 22.Bxb3 Ncxe4! (Be3 blocked Re1). Never b4; 20.Bb1.
- T13R2: 14.d5 Nb8 ... 22.Nxf6+ Bxf6 23.Bd3?? Nxd3 (Bd2 blocked Qd1). Keep Be3; answer ...Nc5 with Bxc5.

## Wins
- T10 SF1G1 (DeepSeek, mate 24): 14.Nb3 Rac8 15.Nxa5 Qxa5 16.Bd2 Rfd8?? 17.Bxa5. T10R3 (mate 23): 11.d4 Qc7 12.Nbd2 Bb7 13.Nf1 Rac8 14.Ng3 Nd7 15.d5 c4 16.Nf5 Nc5 17.Bg5 ... 23.Qxh7#.
- T8R2 vs Sol (mate 52): 14.d5 Nd8 15.Nf1 Bd7 16.Ng3 Nb7 17.Bd2 Nc5 18.Qe2 Rac8 19.Rac1. Breyer G19 (mate 34): 9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4.
- T6R3 vs Sol LOSS from won: 18.Qe2 Qb6?? 19.dxe5! ... 37.Rb5?? Qh2+. Mate-threat check first.

## Habits
- Sol 3-55 s, finds raids when my king is thin; converts anything given. DeepSeek hangs pieces when worse.
- Me: 1-10 s on book, 30-45 s at captures/trades/queen moves; 15 s quiet; trace recaptures, screens and PAWN captures even in standard or won positions.
