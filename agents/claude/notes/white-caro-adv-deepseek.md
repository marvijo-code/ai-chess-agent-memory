# White Caro Advance vs DeepSeek (T29R1 W m35; T32R3 W m27; T40R5 W m37; I used 1-55 s/move with 9-12 min left)

Setup v 3...Bf5: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O Be7 7.c3, then Nbd2, Nb3, Bd3 (7...Rc8 8.Nbd2).

## T40R5 (3...c5, W m37, a piece up at move 16)
- 4.Nf3 cxd4 5.Nxd4 Nc6 6.Nxc6 bxc6 7.Nc3 e6 8.Bd3 Ne7 9.O-O Ng6 10.f4: Rf1 + Bc1 guard f4, so ...Nxf4 loses a piece. Then ...Be7, Qe1, ...O-O, Qg3 (aims at g6/g7; no h4 before the queen guards it).
- 12...f6 13.Bxg6 hxg6 14.Qxg6 f5 15.Qg3 Bf6? 16.exf6: g7 pinned to Kg8 by Qg3, so ...gxf6 illegal; ...Qxf6 regained the pawn only.
- Then a trade offer every move (Qg5, Qg3, Qe3, Qa5); ...Qd4+ answered by Kh1 (Be3 would hang to ...Qxe3+); ...Qb4 hit b2/Nc3 (guards Bc1, b2). 23.Be3 d4 fork: 24.Bxd4 Qxd4 25.Rab1; 25...Qd3?? cxd3; then free captures (Qxe5, Qd6, Qxd7, Qxc7, Qxc8+, Qxf5+) at 3-10 s, Rf3-Rh3+, Qe5+, Rh7+, Qh8#.
- SF marks: 14.Qxg6?! (grab fine, ...f5 kicks with tempo), 22.Qa5?? (unclear; queen beside his Qb4 on b2/Nc3; try Be3/Rab1 first, unverified). Moves 12-15 took 44-53 s: the ...f6 break was predictable, 15 s was enough.
- Every move name f4 (Rf1, Bc1, Qg3) and Nc3 (b2) guards; Bc1 guards b2, so Be3 only when no ...Qxe3+.

## T29R1 pattern (Be7/Rc8 setup)
- 8...Bg6 9.Nb3 h6 10.Bd3 Bxd3 11.Qxd3 c5 12.Nxc5 Nxc5 13.dxc5 Bxc5 14.Be3: Qxe3 hits a7; Qxa7 safe (...Qb6/...Qa5 lose the Q).
- With Bd3 + Nb3, Bxh6 and Nh4 both lose a piece (Bxh4); after the bishop trade Qxd3 and Nxc5 answer the ...c5/...c4 fork on Qd3 + Nb3. DeepSeek then hung ...Qd6?? to exf6/exd6.

## T32R3 pattern (...Ne7-g6, ...f6; W m27)
- 6...Ne7 7.c3 Ng6 8.Nbd2 Be7 9.Nb3 O-O 10.Bd3 Bxd3 11.Qxd3 f6 12.exf6 gxf6 (13 plies). DeepSeek spent 38 s a move; Ng6 + ...f6 is its plan.
- 13.Bf4?? Nxf4: Qd3 does NOT recapture on f4 (d3-f4 is no line). Better 13.Rfe1/Bg5/Nc5, e6 and f6 as targets. Recovery: 14.Qe3 Nh5 15.Qxe6+ Rf7 16.Qg4+ Ng7 (pinned) 17.Rae1; later 19.Nxc5 won the piece back; Qxf8#.
- Keep the pin Qg4 v Ng7, trade rooks, no pawn grabs.

## Rules
- Bishop to f4/g5 where a knight hits it: name who recaptures, square by square, BEFORE the move.
- In a won game every queen capture of a pawn needs 'which pawn recaptures?' (T29R1 22.Qxe6?? fxe6).
- Pin on g7 by Qg3 (Kg8): ...gxf6 illegal, so exf6 wins a piece; look for it whenever his bishop lands on f6 against my e5 pawn.

## Conversion (R+N up, T32R3)
- b3 v ...Rb2, Nd4 guarded by c3/Rd1, Rfc1 to offer trades, c4/cxd5 to open files, Rc8+ Kf7 Rc7+ Kg8, then Ne6 (covers f8/g7) and Rd8#. Before Ne6 check Kxe6 and rook captures. Q up: trade rooks, hit the loose rook; luft check: Qxf8# v Kh8.

## DeepSeek habits
- 30-43 s on quiet moves, illegal tries when a piece is pinned or blocked, moves the rook around under attack, no counterplay when down, gives back a queen after a free piece (T40R5 ...Qd3??).
