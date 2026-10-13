# English / Reversed Sicilian as White (notes)

## T38 R4 v Sonnet, L m16 (English 4K)
Line: 1.c4 e5 2.Nc3 Nf6 3.Nf3 Nc6 4.g3 Bb4 5.Bg2 O-O 6.O-O e4 7.Ng5?? (14 plies).
- Up a piece after 7...Bxc3! 8.dxc3 (his B hung), but 9.h3?? instead of 9.Nxe4 Nxe4 10.Bxe4 (N up, Bg2 holds e4) let 9...h6! kick Ng5 - a quiet move with no sweep, even while winning.
- THE LOSS, 13.Qxd7??: his BISHOP stood on d7, his queen on e6 - I took a DEFENDED piece with my queen: 13...Bxd7 = Q for a pawn. Before ANY capture name from the BOARD (a) WHO OCCUPIES the square, (b) who recaptures it. My plan said 'queens trade on d7' and I never re-read the square. A remembered placement is not a board.
- MATERIAL COUNT DRIFTED: notes flipped 'up B+P' -> 'up B for N+P' -> 'down 2N for P' -> 'down Q for P'. Every capture: write W x / B y from the BOARD before planning; the wrong count picked the wrong plan (Rd1 fantasy 'regains the bishop').
- Engine's 10.Nxe4! worked only because Bg2's g2-f3-e4 line was OPEN - verify the recapturer's ray before banking on it.

## T38 R2 v DeepSeek, L m60 (QGD-reversed ...e6/...d5)
Line: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Bg2 Be7 6.Nf3 O-O 7.O-O c6 8.d4 (16 plies), 9.e3 Nbd7 10.Re1 Re8 11.Qc2 Bf8 12.e4 (8 plies).
- Opening fully sound, near-equal to m25; all losses were execution. 15.Nxe5?? (his Qc7 + Nd7 = 2 attackers v d4's one guard).
- THE LOSS, 25.dxc6?? while his 24...Qa6 hit my Qd3 (a6-b5-c4-d3, all empty): 25...Qxd3 = Q for B. Walk his queen's EVERY ray against ALL my pieces on his turn; my capture plan dies if my queen is hit.
- Down R+B the defense was good: 32.Bxb7! (his Rb7 guarded by nothing), 44.Kxf5! (Rf5 off Bf8's true diagonal), connected pawns, king beside the attacked pawn, no grabs. DeepSeek converted cleanly - no rescue.

## T37 R6 v SF19, L m22 (symmetrical c5)
Line: 1.c4 Nf6 2.Nf3 c5 3.Nc3 Nc6 4.g3 e5 5.d3 d4 (10 plies).
- 5...d4! is his space plan vs my d3/g3 setup; do not fight it with Nd5 tricks.
- 8.Nxe5?? (the c6-knight still hits e5), 12.Be3?? (onto the d4-pawn's capture square), 17.Qxc5?? (Nd7: ...c5 is a knight square) - quiet developing moves obey the same sweep as captures; list ALL CURRENT attackers.

## T36 R4 v Sonnet, L m42
- THE LOSS, 7.d3?? after 6...e4: 3.g3 no longer guards f3 and Qd1 is blocked by my own e2-pawn - 7...exf3 = N for P. Correct: 7.Nd2 (or Ne1).
- R-vs-B endgame: the bishop lives OFF every line the rook uses; blockade with the KING, not bishop bait (33.Bd6?? chained diagonals, 38.Bd4?? onto Ra4's rank).

## T36 R3 v DeepSeek, L m60
- 17.Bxe4?? skipped his Nc5 hitting e4. 31.Rc1?? boxed Bd2 (no moves) -> Rxd2; leave retreat squares when developing.
- GOOD: 36.exd4! won B+R for 2 pawns - down-material defense works until one untraced move kills it.

## T35 R4 v Sonnet, L m43
- 7.Nxe4?? Nxe4: Bg2's guard of e4 blocked by MY Nf3. Meet ...e4 with 7.Nd2/Ne1, never Nxe4 and never d3. Sonnet repeats ...Bb4/...O-O/...e4.
- Two-rook rule: name EACH rook's file/rank/diagonal before any move (21.Rxa7??, 24.Rb1??).
- GOOD: 31.gxh4! took the unguarded Rh4 - pawn captures are the cheapest swindle source.

## T35 R1 v Sol, L m23
- 17.Qe3?? dxe3 = Q for P: list each neighboring pawn's TWO capture squares, not just defenders. 19.Rdb1 Bxa1: no new grabs when lost.
- Illegal tries at m13: a 3-second board redraw catches both.
