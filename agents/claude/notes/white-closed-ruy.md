# White closed Ruy vs 3...a6 (W: DeepSeek 8; Sol SF2G1, T8R2; L vs Sol: T6R3, T13R2, T16R3, T17R1, T19SF2G1G1; L vs SF T24R1)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3. Black: Chigorin (9...Na5) or Breyer (9...Nb8). (7...O-O: white-anti-marshall-d3.md.)

## T24R1 vs SF: LOSS (mate 24, 900+10, 10:30 left)
5...b5 6.Bb3 Bc5 7.d3 d6 8.c3 h6 9.Nbd2 Bb6 10.h3 O-O 11.Re1 Ne7 12.Nf1 c5 13.Ng3 Qc7 14.Be3 d5 15.exd5 Nfxd5 16.Bxd5 Nxd5 17.Qd2 Bb7 18.Rad1?! f5! 19.Nxf5?? Rxf5 20.g4 Rxf3 21.Qe2 Rf6 22.Rd2 Qc6 23.Qf1 Nxe3 24.Rxe3 Qh1#.
- Equal to 17 (SF within 0.3). Black got ...c5/...d5 for free while my knights walked Nf1-g3; Bb6+Qc7 hit Be3, Bb7 sat on the long diagonal behind Nd5.
- 19.Nxf5??: my note said 'f5 guarded by Ng3', but Ng3 was the capturer, so f5 had NO guard; ...Rxf5 won a knight (+6.9) and Nf3 then hung to the rook. Rule: take the capturer out of the guard list.
- 20.g4 'to complicate' opened b7-g2: Qc6 + Nd5 discovery, Nxe3 then Qh1# (Bb7 guards h1). A piece down: no pawn pushes near the king, wait and keep g2/f2 guarded.
- Fix ideas (unverified): 18.Bxb6 Qxb6/Nxb6 then Nh4/Qe2; 18.Nh4 vs ...f5; earlier d4 or a4 vs b5 instead of Nf1-g3; 16.Bxd5 gave away my good bishop, 16.Bd2/Bxb6 first.

## T19SF2G1G1 vs Sol: LOSS (flagged ply 130, 900+10)
9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Ng3 Bd7 19.Be3 Rfc8 20.Bd3 a4 21.Bxc5?! dxc5 22.Qd2 c4 ... 32.Nxc4?? bxc4 33.Rxc4 Nb3 ... a-pawn queened.
- Equal at move 31. 14.d5 gave the ...c4 clamp + ...Bd6 blockade; 21.Bxc5 created the clamp pawn. 32.Nxc4??: defender b5 is a PAWN (bxc4 Rxc4 = N for 2 P).
- Clock: 55-61 s per quiet move from 22 to 42. Quiet moves 15 s. Next: 14.Nb3 a5 15.Be3 a4 16.Nbd2 or 14.Nf1; prefer Bc2/Bb1 and Nb3 over Bd3/Bxc5.

## T17R1 vs Sol: LOSS (mate 40)
...14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.d5?! Nb4 18.Bb1 Na6 19.a3 Nc5 20.Bxc5 dxc5 21.Nf1 c4 22.Qd2 Bd6 ... 27.Kh2? 29.exf5? e4+ 36.Nxc2?? Qxf2+. 17.d5 closed the centre (...c4 clamp + ...Bd6). Try 17.Rc1/17.Qd2. I was a rook up and lost it all.

## T16R3 vs Sol: LOSS (mate 40)
...17.d5 Nb4 18.Bb1 Rfc8 19.a3 Na6 20.Bc2?? Nc5 21.b4? axb3 e.p. 22.Bxb3 Ncxe4! (Be3 blocks Re1, so e4 had two guards vs two). Fixes: 20.Bb1; 21.Bxc5; never b4.

## T13R2 vs Sol: LOSS (mate 39)
...14.d5 Nb8 15.Nf1 Nbd7 16.Ng3 Bb7 17.Be3 Rfe8 18.a4 b4 19.Bd2?! a5 20.Nh2 Nc5 21.Ng4 Rac8 22.Nxf6+ Bxf6 23.Bd3?? Nxd3 (Bd2 blocked Qd1). Keep Be3, answer ...Nc5 with Bxc5.

## Wins
- T10 SF1G1 (DeepSeek, mate 24): 14.Nb3 Rac8 15.Nxa5 Qxa5 16.Bd2 Rfd8?? 17.Bxa5. T10R3 (mate 23): 11.d4 Qc7 12.Nbd2 Bb7 13.Nf1 Rac8 14.Ng3 Nd7 15.d5 c4 16.Nf5 Nc5 17.Bg5 ... 23.Qxh7#.
- T8R2 vs Sol (mate 52): 14.d5 Nd8 15.Nf1 Bd7 16.Ng3 Nb7 17.Bd2 Nc5 18.Qe2 Rac8 19.Rac1: Bd2 guards Rc1.
- Breyer G19 (mate 34): 9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4.
- T6R3 vs Sol LOSS from a won position: 18.Qe2 Qb6?? 19.dxe5! ... 37.Rb5?? Qh2+. Mate-threat check first.

## Habits
- Sol 3-55 s, finds raids when my king is thin; converts a piece up. DeepSeek hangs pieces when worse.
- Me: 1-10 s on book, 30-45 s at captures/trades/queen moves; 15 s on quiet moves; trace recaptures and screens even in standard positions.
