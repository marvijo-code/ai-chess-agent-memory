# White Caro Advance vs DeepSeek (T29R1, T32R3, T40R5, T45R5 all W; 1-55 s/move)

Setup v 3...Bf5: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O Be7 7.c3, then Nbd2, Nb3, Bd3 (v 7...Rc8 Nbd2).

## T45R5 (3...Bf5 with ...Ne7, ...Bg6, ...c5; W m19, 5-25 s a move)
- Nbd2 BEFORE c3 (c3 first allows ...Bxb1). After ...c5: dxc5 Nxc5, Nb3 Nxb3, Qxb3 Nf5.
- 12.Qxb7 (SF ?!) hit Ra8; ...Qd6?? stood on my e5 pawn's capture square: exd6 Nxd6, Qxa8+, Qxa7+ (not Qxf8+?? Rxf8).
- Queen+rook up: Re1, Bf4, Ne5, Qd7#. His K on d8 had no luft, Ne5 guarded d7. 19 moves only.
- Check before the grab: ...Rb8 Qxa7 Rxb2 Bxb2, and ...Qb8/...Qc8 offers a queen trade, still a pawn up.

## T40R5 (3...c5, W m37, a piece up at move 16)
- Nf3 cxd4 Nxd4 Nc6 Nxc6 bxc6, then Nc3, e6, Bd3, Ne7, O-O, Ng6, f4: Rf1 + Bc1 guard f4, so ...Nxf4 loses a piece. Then ...Be7, Qe1, ...O-O, Qg3 (aims at g6/g7; no h4 before the queen guards it).
- ...f6 Bxg6 hxg6 Qxg6 f5 Qg3 Bf6? exf6: g7 pinned to Kg8 by Qg3, so ...gxf6 illegal; ...Qxf6 regained the pawn only.
- Then a trade offer every move (Qg5, Qg3, Qe3, Qa5); ...Qd4+ answered by Kh1 (Be3 would hang to ...Qxe3+); ...Qb4 hit b2/Nc3 (guards Bc1, b2). ...d4 fork on Be3: Bxd4 Qxd4 Rab1; then free captures at 3-10 s, Rf3-Rh3+, Qe5+, Rh7+, Qh8#.
- SF marks: 14.Qxg6?! (grab fine, ...f5 kicks with tempo), 22.Qa5?? (queen beside his Qb4 on b2/Nc3; try Be3/Rab1 first, unverified). Moves 12-15 took 44-53 s: the ...f6 break was predictable.
- Every move name f4 (Rf1, Bc1, Qg3) and Nc3 (b2) guards; Be3 only when no ...Qxe3+.

## T29R1 pattern (Be7/Rc8 setup)
- ...Bg6, Nb3 h6, Bd3 Bxd3, Qxd3 c5, Nxc5 Nxc5, dxc5 Bxc5, Be3: Qxe3 hits a7; Qxa7 safe (...Qb6/...Qa5 lose the Q).
- With Bd3 + Nb3, Bxh6 and Nh4 both lose a piece (Bxh4); after the bishop trade Qxd3 and Nxc5 answer the ...c5/...c4 fork on Qd3 + Nb3. DeepSeek then hung ...Qd6?? to exf6/exd6.

## T32R3 pattern (...Ne7-g6, ...f6; W m27)
- ...Ne7, c3 Ng6, Nbd2 Be7, Nb3 O-O, Bd3 Bxd3, Qxd3 f6, exf6 gxf6. DeepSeek spent 38 s a move; Ng6 + ...f6 is its plan.
- Bf4?? Nxf4: Qd3 does NOT recapture on f4 (d3-f4 is no line). Better Rfe1/Bg5/Nc5, e6 and f6 as targets. Recovery: Qe3 Nh5, Qxe6+ Rf7, Qg4+ Ng7 (pinned), Rae1; Nxc5 won the piece back; Qxf8#.
- Keep the pin Qg4 v Ng7, trade rooks, no pawn grabs.

## Rules
- Bishop to f4/g5 where a knight hits it: name who recaptures, square by square, BEFORE the move.
- In a won game every queen capture of a pawn needs 'which pawn recaptures?' (T29R1 22.Qxe6?? fxe6).
- Pin on g7 by Qg3 (Kg8): ...gxf6 illegal, so exf6 wins a piece; look for it whenever his bishop lands on f6 against my e5 pawn.
- Queen up: trade pieces, mate on the e-file/back rank; he has no luft (T45R5).

## Conversion (R+N up, T32R3)
- b3 v ...Rb2, Nd4 guarded by c3/Rd1, Rfc1 to offer trades, c4/cxd5 to open files, Rc8+ Kf7 Rc7+ Kg8, then Ne6 (covers f8/g7) and Rd8#. Before Ne6 check Kxe6 and rook captures. Q up: trade rooks, hit the loose rook; luft check: Qxf8# v Kh8.

## DeepSeek habits
- 30-43 s on quiet moves (up to 1:42), illegal tries when a piece is pinned or blocked, moves the rook around under attack, no counterplay when down, hangs the queen on a pawn's capture square (T29R1, T40R5, T45R5).
