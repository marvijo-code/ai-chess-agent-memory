# White Caro Advance vs DeepSeek (T29R1 W mate 35; clock 15:21 v 7:47; I used 1-14 s/move)

1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O Be7 7.c3 Rc8 8.Nbd2 Bg6 9.Nb3 h6 10.Bd3 Bxd3 11.Qxd3 c5 12.Nxc5 Nxc5 13.dxc5 Bxc5 14.Be3 Bxe3 15.Qxe3 Ne7 16.Qxa7 Qd6?? 17.exd6 O-O 18.dxe7 Rfe8 19.Qxb7 Rcd8 20.exd8=Q Rxd8 21.Qe7 Rb8 22.Qxe6?? fxe6 23.b3 ... 34.Ne6 g6 35.Rd8#.

## What worked
- 9.Nb3 then 10.Bd3: Bxh6 and Nh4 both lose a piece (Bxh4); with the bishop traded, Qxd3 and Nxc5 answer the ...c5/...c4 fork threat on Qd3 + Nb3.
- 12.Nxc5 Nxc5 13.dxc5 Bxc5 14.Be3: trade the bishop, then 15.Qxe3 hits a7. 16.Qxa7 is safe: ...Qb6/...Qa5 lose the Q to Qxb6/Qxa5, and Qa6 would be met by bxa6 (never play it).
- 7...Rc8 setup is slower than 7...c5 8.Nbd2 Be7 9.Nb3 but ...Bg6/...h6 wasted time; DeepSeek then hangs things (16...Qd6?? onto my e5 pawn).

## My blunder
- 22.Qxe6?? fxe6: Q for P with Q+R+N v R+pawns. I wrote 'wins e6 pawn' and never listed the f7 pawn. Safe: 22.Rfd1, 22.Qd6 or 22.Qe5 (b2 guarded by a rook/Bc1 gone: b3 is enough). Still won with R+N up, but this could have lost a tempo race v SF/Sol.
- Rule: in a won game every queen capture of a pawn needs 'which pawn recaptures?' first (pawn diagonals DOWN-board for Black).

## Conversion pattern (R+N up)
- b3 against ...Rb2, Nd4 guarded by c3/Rd1, Rfc1 to offer trades, c4/cxd5 to open files, Rc8+ Kf7 Rc7+ Kg8, then Ne6 (covers f8/g7) and Rd8#. Rc7 covers f7/h7, so g6 only gave luft to nothing.
- Before Ne6 check Kxe6 and that the knight is not capturable by a rook (h5 rook did not reach).

## DeepSeek habits seen
- 30-43 s on quiet moves, one illegal try (Rb2 into pawns), replies to attacks by moving the rook around (Rc5-c6-c5-c7), no counterplay at -R-N.
