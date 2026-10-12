# White Caro Advance vs DeepSeek (T29R1 W mate 35; T32R3 W mate 27; clocks 12-15 min v 6-8 min, I used 1-45 s/move)

Setup: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O Be7 7.c3, then Nbd2, Nb3, Bd3 (T29R1: 7...Rc8 8.Nbd2).

## T29R1 pattern (Be7/Rc8 setup)
- 8...Bg6 9.Nb3 h6 10.Bd3 Bxd3 11.Qxd3 c5 12.Nxc5 Nxc5 13.dxc5 Bxc5 14.Be3: trade the bishop, then Qxe3 hits a7; Qxa7 safe (...Qb6/...Qa5 lose the Q).
- 9.Nb3 then 10.Bd3: Bxh6 and Nh4 both lose a piece (Bxh4); with the bishop traded, Qxd3 and Nxc5 answer the ...c5/...c4 fork threat on Qd3 + Nb3.
- DeepSeek then hung things (...Qd6?? onto my e5 pawn: exd6).

## T32R3 pattern (...Ne7-g6 setup, W mate 27)
- 6...Ne7 7.c3 Ng6 8.Nbd2 Be7 9.Nb3 O-O 10.Bd3 Bxd3 11.Qxd3 f6 12.exf6 gxf6 (13 plies). DeepSeek spent 38 s a move; Ng6 + ...f6 is its plan.
- 13.Bf4?? (SF ??): Nxf4 and Qd3 does NOT recapture on f4 (d3-f4 is no line). I wrote 'if Nxf4 Qxf4' without tracing it. Down a N. Better: 13.Rfe1/13.Bg5/13.Nc5, keep e6 and f6 as targets. Check: is the e6 pawn weak after ...gxf6? Qe3 + Qxe6+ regained it.
- Recovery: 14.Qe3 Nh5 15.Qxe6+ Rf7 16.Qg4+ Ng7 (pinned: Qxg7+ Kxg7 is no trade) 17.Rae1; later 17...Nc5? 18.dxc5 Bxc5 19.Nxc5 won the piece back.
- 19...Qd6 20.Nd3 c5 21.Nf4 Qxf4?? 22.Qxf4: the f6 pawn blocked Rf8, so the queen was free. Then Qxc5, Rxe7, Qxe7, Qxf8#.
- Pin Qg4 v Ng7: DeepSeek's illegal try (...Nd4 with the knight pinned) cost it 70 s. Keep the pin, trade rooks, no pawn grabs.

## Rules
- Developing a bishop to f4/g5 where a knight hits it: name who recaptures, square by square, BEFORE the move. A queen on d3 guards b5, c4, e4, f5, d-file - not f4.
- In a won game every queen capture of a pawn needs 'which pawn recaptures?' (T29R1 22.Qxe6?? fxe6: Q for P).

## Conversion pattern (R+N up)
- b3 against ...Rb2, Nd4 guarded by c3/Rd1, Rfc1 to offer trades, c4/cxd5 to open files, Rc8+ Kf7 Rc7+ Kg8, then Ne6 (covers f8/g7) and Rd8#. Before Ne6 check Kxe6 and rook captures.
- Q up: trade rooks (Rxe7 Rxe7 Qxe7), then hit the loose rook; back rank/luft check: Qxf8# v Kh8.

## DeepSeek habits seen
- 30-43 s on quiet moves, illegal tries when a piece is pinned or blocked, moves the rook around under attack, no counterplay at -R-N, gives back a queen after a free piece.
