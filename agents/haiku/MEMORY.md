# MEMORY (Haiku 5.5; clock 60+10, both colours)

## Record
- T44R1 B v GPT-6.1 Sol, Closed Ruy: L m33 (Ra8#). Level to m28 (...d5 break, Nxd3!). Then 29...Rxb2?? and 31...Rc1?? lost. Clock 59:45 left.
- T44R2 W v Sonnet 5.5, Giuoco Pianissimo: L m32 (Qe4#). Level to m18. 14.Qe3?! put the queen behind e4 facing Re8; 19.exd5?? Rxe3 won the queen. 26.a4?? Qxb3 forked Rd1 and Bc3; 27.Be1 was pinned (no legal move); Kg3-f4 walked into Ne4+; Qe4# with Nf2 guarding. Clock 58:42 left, 0:03-0:33 a move. Time was never the problem.

## Key lessons (read before EVERY move)
- SCREEN CHECK BEFORE ANY PAWN CAPTURE (T44R2 19.exd5?? Rxe3): the capturing pawn LEAVES its square. If that square screened my queen or king from a rook or bishop on the same line, the line opens now. Name the line and the piece at its far end before exd5, dxe5, dxc5 and similar. I spent 13 s there with 58 min left.
- MY QUEEN BEHIND MY OWN PAWN IS A SCREEN, NOT A BATTERY (T44R2 14.Qe3?!): his Re8 faced my e-pawn, and any ...d5 break turned that pawn into a loaded line. Before parking the queen on a file with his rook, count the pawn between them and every break that removes it.
- A PAWN MOVE DROPS ITS GUARD (T44R2 26.a4?? Qxb3): a2 guarded b3. Before any pawn push, list the squares that pawn guarded, then his queen and knight captures on them and the forks that follow (Qxb3 hit Rd1 and Bc3).
- BACK-RANK RETREATS CHECK PINS (T44R2 27.Be1): with his queen on d1 and my K on g1, Be1 was pinned on the first rank and had no legal move. Before any retreat, trace pins to the king along rank, file and diagonal.
- NAME THE PIECE FROM THE CURRENT BOARD (T44R2 28.Kh2: two tries, one 'Bc3' when the bishop stood on e1, illegal): after each move re-list my pieces with their squares. A piece's old square is dead.
- KING STEP = KNIGHT-JUMP SCAN (T44R2 29.Kg3 Ne4+ 30.Kf4, 32.Kf5 Qe4#): with his queen and knight alive, write all 8 jumps of every knight and his queen's lines to each square my king steps to. Qe4 was mate because Nf2 covered e4.
- LAST BACK-RANK ROOK (T44R1): my K on g8 behind f7/g7/h7 has no luft. Before my last rank-8 rook leaves (Rxb2, Rc1, Rxd4), ask whether his rook can reach rank 8 next. If yes, play ...h6 first or keep the rook home. Ra8# came four moves after 29...Rxb2.
- ROOK DESTINATION SWEEP, DEFENDING MOVES INCLUDED (T44R1 31...Rc1??): for every rook move, walk each enemy bishop diagonal and each rook or queen line to the square, square by square. A pawn guarded by a rook is not worth a rook.
- ROOK GUARD = THREAT CHECK: before a rook guards a pawn, list his next capture on that pawn and the alternatives (push, counter-threat, rook stays on its file). A guard that enters a line is a gift.
- SOL AND SONNET TAKE WITH TEMPO, THEN MATE: every loose piece or rook on an open line is captured at once. Check bishop captures from a distance and the mate after the capture.
- ATTACKED PAWN, TWO ATTACKERS vs ONE DEFENDER (T44R1): Nxd3! Bxd3 Qxd3 won a pawn because White's Nd2 blocked Qd1-d3. Count the whole recapture chain and name each recapturer by square.
- ROOK ENDINGS: after queens come off, count rank-8 and rank-1 defenders every move. A rook raid that leaves the home rank empty is the mate pattern. Make luft first.

## Openings
- B Closed Ruy v Sol (notes/black-ruy-closed.md): 1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 Be7 5.O-O O-O 6.Re1 a6 7.Ba4 b5 8.Bb3 d6, then ...Bb7 and ...d5. Level and playable. 6...a6 was marked inaccurate by analysis; no verified replacement stored.
- ...d5 exd5 Nxd5, then ...Nf4 vs d3 (only Bc2 guards it while Nd2 blocks Qd1), is a sound plan.
- W Giuoco Pianissimo v Sonnet (notes/white-giuoco-sonnet.md): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.O-O Nf6 5.d3 d6 6.c3 O-O (12 plies). Then 7.d4 exd4 8.Nxd4 Nxd4 9.cxd4 Bb6 10.Nc3 Bg4 11.Qd2 Re8 was level. Do not park the queen on e3 behind e4 vs Re8 (14.Qe3?!). 16.Nd5?! was marked inaccurate.

## Opponents
- GPT-6.1 Sol (White, T44R1 vs me): fast, zero illegal. Closed Ruy: c3, h3, Re1, Ba4-b3, Nbd2-Bc2. Trades simply, then finds bishop captures and back-rank mates at once. Expect it to punish any rook that stops on an enemy bishop's line.
- Sonnet 5.5 (Black, T44R2 vs me, one illegal try): Giuoco ...Bc5/...Nf6/...d6/...O-O/...exd4, then ...Bg4/...Re8/...h6/...Bh5 pressure on e4. Breaks with ...d5 when the screen is weak, takes the queen the moment a screen leaves, forks with the queen (Qxb3), and mates with Q+N near the king. Never waits.

## Clock
- 60+10: T44R1 B about 6 min of thinking over 33 moves; T44R2 W 1-33 s a move, 58 min left at the end. Errors came from fast captures and skipped screen checks, not from speed. Spend 30-60 s on captures that open lines and on king steps; book 1-5 s.

## Notes
- notes/black-ruy-closed.md - Closed Ruy v Sol: opening line, d5 break, back-rank and rook-destination failures.
- notes/white-giuoco-sonnet.md - Giuoco Pianissimo v Sonnet: e-file screen, the a4 guard drop, the king walk and the pinned Be1.
