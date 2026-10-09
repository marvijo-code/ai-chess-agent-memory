# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6, then 14.d5 / 14.dxe5 / 14.Nf1.

## g52 vs Sonnet (1/2-1/2) - repetition rescue; 26.Bd3? dropped the loose Nd2
13.d5 Nb8 14.Nf1 Nbd7 15.Be3 Nb6 16.Qd2 Bd7 17.Ng3 c4 18.Bxb6 Qxb6 19.Rac1 Rfc8 20.b3 cxb3 21.axb3 a5 22.Qe3 Qxe3 23.Rxe3 b4 24.cxb4 axb4 25.Nd2 Ra2 26.Bd3? Rxd2 27.Rc2 Rdxc2 28.Bxc2 Rxc2 29.Re2 Rxe2 30.Nxe2 Nxe4 31.Nf4?? exf4.
- 18.Bxb6?! (SF): trading bishop for knight lets his queen to b6 and keeps his bishop pair; his ...c4/...b4/...a5/...Ra2 bind was better for him. Consider 18.f4/18.Ne2 instead.
- 25.Nd2 put the knight on an undefended square. 25...Ra2 = double attack (Bc2 attacked twice, Nd2 loose). 26.Bd3? moved the blocker shielding Nd2: the a2-d2 rank cleared, Rxd2 won the knight. Save the loose piece FIRST; with his rook on my 2nd rank and a loose piece on that rank, moving any blocker loses the piece (26.Nf1 or 26.Re2 - the rook defends c2 AND d2 along rank 2).
- 31.Nf4?? undefended, 31...exf4 took the last knight; K+2P vs K+2B+N followed.
- Black then failed to mate for ~19 moves and the game ended 1/2 by threefold repetition. NEVER resign, keep moving 1-3 s in lost positions; repetition/stalemate rescues are real (g52).

## g51 vs Sonnet (0-1, m34)
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.a3 Na6 18.Be3 Nc5 19.Bxc5 Qxc5 20.Qd2 Rfc8 21.Ng3 h6 22.Nf5 Bxf5 23.exf5 Nxd5?? 24.Qxd5?? Qxd5 25.Rxe5?? dxe5.
- Good to 23.exf5 (SF: Bb3!, cxd4!, Bb1!, exf5!); Qc5 guards d5, so 24.Qxd5?? is Q for N, not a trade (my queen undefended, f5-pawn blocked Bb1). Name the recapturer and its value before capturing. 25.Rxe5?? dxe5: list enemy PAWNS as recapturers. Ended 3:28 vs his 17:18.

## g48 vs Sonnet (0-1, m30)
14.Nf1 Bb7 15.Ng3 Rfe8 16.d5 Nb4 17.Bb1 a5 18.a3 Na6 19.Be3 Nc5 20.Bxc5 dxc5 21.d6?! Bxd6 22.Qxd6?? Qxd6 23.Nd2?? Qxd2, mated m30.
- 21.d6?! just loses a pawn (Bxd6, guarded by Qc7); play Qd2/Rc1. 22.Qxd6?? I had already rejected it in my own reasoning - never send a rejected move. 23.Nd2?? Qxd2 (also g46). Mated with 0:32 vs 17:06.

## g46 vs GPT-6.1 Sol (0-1 on time, m31)
14.dxe5 dxe5 15.Nf1 Be6 16.Ng3 Rad8 17.Be3?? Rxd1 18.Raxd1 Rd8; down Q for R, flagged m31 (0:18 vs 14:21).
- 14.dxe5 OPENED the d-file while my queen stood on d1. When his rook enters an open file facing my queen, the queen leaves THAT move: 17.Qe2!. Down material: 5-15 s/move, not 13 hopeless moves.

## Keep (g10,g13,g18,g21,g22,g23,g33,g37)
- 14...Nb4 -> 15.Bb1! only; 14...Nb8: 15.Nf1 Nbd7 16.Be3. With his knight on c4 do NOT play Be3 (g33: 17.Be3?? Rfe8 18.Qd2?? Bxe4).
- 14...Nd7? (g40): resolve the centre or reroute BEFORE 15.d5; ...g6 vs Nf5/Ng5+Qh5 (22...Qd7?? 23.Qxh7#).
- Bishop: 20.Bxc5 dxc5 fine with the d5 clamp (g37); never B-for-P or give the bishop pair (g13,g18).
- g43: when my capture opens a file with my rook on it, fix the rook first (20.Rxa8! Rxa8 21.Bxb4 wins his loose knight; 19.Ba3?! Nxb4!). Down R+B: no tricks.

## Rook endings (g27,g31)
- Undefended rook chasing rook loses (Rc2?? Rxc2; Re2?? Rxe2); use a defended rook. Check the destination rank/file for rooks AND knights (Re7?? Nxe7). His rook to an open file at my loose rook: fix it at once.

## Game management
- Routine <=15 s; book <=10 s; m10+ <=25 s. (g43 47-63 s/move; g46 flagged 0:18; g48 mated with 0:32; g51/g52 40-50 s on routine moves, blunders anyway.)
- Down material: king safety, defend loose pieces, trade, 5-15 s, no pawn grabs, no capture his recapture answers (g43 Bxd6, g48 Qxd6, g51 Qxd5, g52 Rxd2).
