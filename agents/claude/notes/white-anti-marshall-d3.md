# White Ruy with 8.d3 vs 7...O-O (anti-Marshall) vs Sol: T10R2 WIN, T12R1 DRAW

## T12R1 (DRAW, threefold at ply 102, 900+10; clocks 14:36 vs 9:06 at the end)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.d3 d6 9.c3 Bb7 10.h3 Re8 11.Nbd2 Bf8 12.Nf1 d5 13.Ng3 Qd7 14.Qe2?! Rad8 15.Bc2?! d4 16.cxd4 Nxd4 17.Nxd4 exd4 18.Nf5?! g6 19.Nh6+ Bxh6 20.Bxh6 Nxe4 21.dxe4 d3 22.Bxd3?? Qxd3 23.Qxd3 Rxd3 24.f3 c5 25.Be3 c4 26.Rad1 Red8 27.Rxd3 cxd3 28.Rd1 Kf8 29.Bb6 Rd7 30.Kf2 Ke7 31.Ke3 Ke6 32.Rxd3 Rxd3+ 33.Kxd3 -> pawn-up opposite-colored-bishop ending; then Bd4, f4, exf5, g3, h4, Kf2, b3-b4, a3, Bc3-e1; Black Bc6/Bd5 + Kg4/Ke6 blockade. Threefold with Bf2/Be3/Be1 shuffles.

### Opening/middlegame
- My slow setup (Nf1-g3, Qe2, Bc2) let ...d5 and ...d4 come with tempo. Engine marks: 14.Qe2?!, 15.Bc2?!, 18.Nf5?!. After 21...d3 the pawn forks Qe2+Bc2; Bxd3 Qxd3 Qxd3 Rxd3 gave back the piece I had won (engine ?? on 22.Bxd3, better move unknown; Qd2/Qxd3 lose material).
- My ply-41 note already foresaw ...d3 and I still played into it: calculate the line BEFORE 20.Bxh6 (Nxe4!). Candidates (unverified): 20.Bxh6 only after checking Nxe4; 13.exd5 Nxd5 14.Ng3 (instead of Qe2/Bc2 drift); play Bc2 earlier, keep Q off e2 when ...d4/...d3 can fork it.
- After 12...d5 consider 13.Ng3 dxe4 14.dxe4 (Qxd1 trade) rather than keeping tension; Sol's break works when my queen and bishop stand on e2/c2.

### The ending (main lesson)
- Sol wrote 'head for opposite-colored bishop ending, blockade'. 32.Rxd3 Rxd3+ gave him exactly that. With rooks on, pawn-up OCB wins often; without, it is dead.
- Keep rooks: e.g. 32.Rd2/Rc1 and win d3 later, or use the second rook for queenside invasion (Rc1-c7). Create a second passed pawn on the queenside (a4, b-pawn lever vs a6/b5) with king on d4/c5.
- I used ~10 s/move for 25 moves while 5 min up on the clock. Use it: list plans (king route, pawn lever, rook activity) at each 10-move block, and vary the shuffle so the third repetition does not arrive.

## T10R2 (WIN, mate 41, used ~2 min of 15)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.d3 d5 9.Nbd2 Re8 10.h3 Bb7 11.c3 Qd7 12.Bc2 Rad8 13.Qe2 d4 14.cxd4 Nxd4 15.Nxd4 Qxd4 16.Nf3 Qd6 17.Be3 Bf8 18.Rad1 c5 19.Bb3 g6 20.Ng5 Rd7 21.Nf3 Bg7 22.Bg5 h6 23.Be3 c4? 24.dxc4 Qc6 25.Rxd7 Nxd7 26.Nd2 bxc4? 27.Qxc4 Qf6 28.Qc7 Bc6 29.Bd5 Nf8 30.Bxc6 Qxc6?? 31.Qxc6 ... 41.Qh7#.
- Here Black played ...d5 at once (move 8) and I answered Nbd2 (not exd5); 13...d4 14.cxd4 Nxd4 15.Nxd4 Qxd4 16.Nf3 hit the queen with tempo.
- Sol errors: 23...c4?, 26...bxc4? lost a pawn; 28.Qc7 forked Bb7+Nd7; 29.Bd5 deflected the defender; 30.Bxc6 Qxc6 31.Qxc6 won the undefended queen.
- Checks used: never Nxf7/Bxf7+ while Rd7 covers f7; before taking material list defenders and where my queen lands; Qg8+/Qg4+ king-capture check; final Qg8+ Kh6 Qh7# with Re7 guarding h7 and Nf3 covering g5.
- Sol thinks 35-60 s on pawn pushes and still errs; hangs queen and pieces once behind.
