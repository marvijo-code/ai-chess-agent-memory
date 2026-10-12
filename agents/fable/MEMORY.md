# MEMORY (Fable 5.1; clocks 900+10)

## Record
- T37R1 B v Sol, Ruy Chigorin: L m28 (checkmate). 16...Be6?? (SF: his Qd4 + e5 push on the d4-g7 diagonal, Nf6 the only screen of g7); 24...Qc1+?? Bxc1 (his Bf4 saw c1 through e3-d2); 25...Nd5?? Qxd5. 0 illegal tries. Clock fine (14:03 left).

## Key lessons (read before EVERY move)
- CHECK = DESTINATION SWEEP FIRST (24...Qc1+?? 25.Bxc1): before ANY queen check or grab, trace every enemy bishop diagonal and rook/queen line to the destination square by square (Bf4: e3, d2, c1 all empty = c1 is his). A check is not safe because it is a check. Pawn diagonals too. Then 'what recaptures me there?' If nothing of mine guards the square and anything of his hits it, the move is dead.
- A PLAN BORN TWO MOVES AGO MUST BE RE-SWEPT ON THE NEW BOARD (23...Bxf5, 24...Qc1+): I wrote 'Qc1+ then Qxb2' at move 21 while his bishop stood on f4 the whole time. Re-run the sweep at the moment of the move; a stored plan is a QUESTION, not an answer.
- KNIGHT/BISHOP LANDS ONLY ON A GUARDED SQUARE (25...Nd5?? Qxd5): name the guard of the destination before moving; 'centralize' is not a guard. Down material, hanging a second piece ends the game at once (Qa8+ Bd8 Qxd8#, back rank with no luft).
- HIS QUEEN ON THE LONG DIAGONAL (Qd4/Qe5/Qg3 + dark bishop) = g7 is the target (16...Be6??): with my Nf6 the only screen, his e5 push (or Bg5/Bh6) comes with tempo. Answer by taking the diagonal away FIRST (...Bf6, ...Re8+...Bf8, ...g6 with care, ...Qb6/queen trade), not by a quiet developing move. Never release the central tension (14...exd4) when the recapture puts his queen on d4 with my king's diagonal open; keep ...Bd7/...Re8/...Nb4 ideas instead.
- BACK RANK: with queens on and my rooks gone (after Rc8 trades), my king on g8 with f7/g7/h7 intact has NO flight: make luft or keep a rook. Queen-up opponent mates on the back rank in 3 moves.
- ROOK TRADES ARE NOT 'SAFE SIMPLIFICATION': after 20...Rxc1 21...Rc8 I had queen + N + B v queen + 2 bishops with his queen centralized and his pawn on f5 gaining space; I had no plan but a pawn grab. Before offering the last rook trade name MY plan in the queenless/rookless position.
- MATE FIRST, every move: after his move ask 'what mates if I pass?' and 'what does my move open?' (Nd5 cleared f6, Qa8+ then Qxd8#).
- MATERIAL FROM THE BOARD: write 'W x / B y' each move; a recapture is not a gain.
- CLOCK: book 1-5 s (done), quiet 10-15 s, capture/check 20-30 s. Two 59 s thinks (23...Bxf5, 24...Qc1+) still skipped the bishop line: the LIST is the check, not the time. Behind by 2 min = 10 s. Never over 40 s.
- ILLEGAL: write the path square by square; after ONE rejection redraw and pick a different piece. 3 rejections = forfeit.

## Openings
- B Ruy Chigorin v Sol (T37R1 L): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O; then 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6. Sol played 14.Nf1 (not d5). SF marks 15.Nxd4?? after 14...exd4: unverified, look at 15...Nxe4 hitting Re1/Bc2 recapture chains before 15...Nxd4. Better: do NOT play 14...exd4; keep tension with 14...Bd7/...Re8/...Nb4 (v d5: ...Nb4 Bb1 a5 a3 Nc2 only if Qc7 recaptures on c2). Claude's record: Na5+Qc7 setup loses to Sol repeatedly (4 W 16 L); consider Breyer (...Nb8-d7) or Zaitsev (...Bb7, ...Re8) next time, or 1...c5/1...e6.
- Other openings: untested. Default as Black v 1.e4: ...e5 solid; v 1.d4: QGD ...d5 ...e6 ...Nf6 ...Be7 ...O-O ...c6. As White: 1.e4, Ruy/Italian, develop, castle, no early pawn grabs.

## Opponents
- Sol (GPT-6.1): fast (3-45 s), zero illegal, banks clock. W Ruy: Re1, c3, h3, Nbd2-f1-g3, Bd3 off the c-file, Bf4 hitting d6, Rac1 with tempo on Qc7, Nf5 to trade my light bishop then exf5 for space, queen centralized on d4. Takes every free piece and every queen on a bishop's diagonal AT ONCE; converts a queen up by Qa8+ / back-rank mate in 3. Other players: sacs for king attacks, Bh6 then Qxh6, e5 push when my pieces are tied, g7 batteries (Qg3/Qe5 + Bd4). Misplays queenless endings (Claude). Never give him a free unit; vs him the game is decided by my sweep, not his play.
- Claude (Sonnet): takes every hanging piece, never misses a recapture, Q+B batteries, mates fast when ahead; as Black ...e5 ...Bb4 ...e4 v English. Banks clock, flags in long endings.
- DeepSeek: hangs pieces when worse or even, illegal tries, no luft; as White Giuoco/Scotch/Sicilian 6.Be2; converts free pieces.
- GLM: hangs pieces to plain captures, illegal tries, slow; Taimanov as Black, English g3 as White.
- SF 19 (depth 4-6): instant; punishes loose units, pins to my queen, back rank; no repetition rescue when ahead.

## Notes (notes/*.md)
- notes/black-ruy-sol.md: Chigorin v Sol T37R1 details, what to try next.
