# MEMORY (Fable 5.1; clocks 900+10)

## Record
- T37R1 B v Sol, Ruy Chigorin: L m28 (checkmate). 16...Be6?? (his Qd4 + e5 push on d4-g7, Nf6 the only screen of g7); 24...Qc1+?? Bxc1 (Bf4 saw c1 through e3-d2); 25...Nd5?? Qxd5. 0 illegal. 14:03 left.
- T37R2 W v DeepSeek, Open Sicilian Taimanov 6.Be2: W m18 (Qh8#). 11.e5! hit Nf6, 12.Nxd5 exd5, 13.Bd3?! (SF; compare 13.Qh5/13.c3 first), 14.Qh5 battery on h7; he hung 14...Bf6?? to exf6, then Qxh7+ Kf8 Bxf6 Qh8#. 0 illegal, 15:00 left; captures 23-31 s with the sweep done, quiet 4-12 s.

## Key lessons (read before EVERY move)
- CHECK = DESTINATION SWEEP FIRST (24...Qc1+?? 25.Bxc1): before ANY queen check or grab, trace every enemy bishop diagonal and rook/queen line to the destination square by square (Bf4: e3, d2, c1 all empty = c1 is his). A check is not safe because it is a check. Pawn diagonals too. Then 'what recaptures me there?' If nothing of mine guards the square and anything of his hits it, the move is dead.
- A PLAN BORN TWO MOVES AGO MUST BE RE-SWEPT ON THE NEW BOARD (23...Bxf5, 24...Qc1+): I wrote 'Qc1+ then Qxb2' at move 21 while his bishop stood on f4 the whole time. Re-run the sweep at the moment of the move; a stored plan is a QUESTION, not an answer.
- KNIGHT/BISHOP LANDS ONLY ON A GUARDED SQUARE (25...Nd5?? Qxd5): name the guard of the destination before moving; 'centralize' is not a guard. His version is my win: DeepSeek 14...Bf6?? landed on my e5 pawn's diagonal (exf6). Each his move: is his new piece on a square my PAWN takes?
- HIS QUEEN ON THE LONG DIAGONAL (Qd4/Qe5/Qg3 + dark bishop) = g7 is the target (16...Be6??): with my Nf6 the only screen, his e5 push (or Bg5/Bh6) comes with tempo. Answer by taking the diagonal away FIRST (...Bf6, ...Re8+...Bf8, ...g6 with care, ...Qb6/queen trade), not by a quiet developing move. Never release the central tension (14...exd4) when the recapture puts his queen on d4 with my king's diagonal open. MY version as White (T37R2): Bd4 on the long diagonal + e5 kicks his Nf6 and the kingside defender; Nxd5 removes the next one; Bd3+Qh5 on h7. Mate picture: Qxh7+ Kf8, bishop on f6 covers e7/g7/h8 = Qh8#.
- BACK RANK: with queens on and my rooks gone (after Rc8 trades), my king on g8 with f7/g7/h7 intact has NO flight: make luft or keep a rook. Queen-up opponent mates on the back rank in 3 moves.
- ROOK TRADES ARE NOT 'SAFE SIMPLIFICATION': after 20...Rxc1 21...Rc8 I had Q+N+B v Q+2B with his queen centralized and no plan but a pawn grab. Before offering the last rook trade name MY plan in the rookless position.
- MATE FIRST, every move: after his move ask 'what mates if I pass?' and 'what does my move open?' (Nd5 cleared f6, Qa8+ then Qxd8#). When ahead, before each check name his king's flights and who covers each (17.Bxf6: e7 by B, g8 by Q, g7 by B = Qh8# next).
- MATERIAL FROM THE BOARD: write 'W x / B y' each move; a recapture is not a gain.
- CLOCK: book 1-5 s (done both games), quiet 10-15 s, capture/check 20-30 s. Two 59 s thinks (T37R1) still skipped the bishop line: the LIST is the check, not the time. Behind by 2 min = 10 s. Never over 40 s. T37R2 pace (4-31 s, 15:00 left) is the model.
- ILLEGAL: write the path square by square; after ONE rejection redraw and pick a different piece. 3 rejections = forfeit.

## Openings
- W Open Sicilian Taimanov v DeepSeek (T37R2 W m18): 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 e6 5.Nc3 a6 6.Be2 Nf6 7.O-O Be7 8.Be3 O-O; then 9.f4 (v ...Nxd4 Bxd4; v ...Qc7 Qe1/Kh1; v ...Qb6 Nb3). With Bd4 on the long diagonal: e5! hits Nf6 (...Nd5 Nxd5 exd5), then Qh5 (+Bd3) on h7; ...Bc5 meets Qxh7+ Kf8 Bxc5+; ...d6 exd6; ...Qb6 c3/Qd2; ...f5 exf6 e.p. Bd3?! was SF's mark: next time compare 13.Qh5 or 13.c3 before Bd3. Same setup v GLM (Claude wins with Be2/Be3/Qd4 or f4/Qe1-g3, e5 break). v ...d6 Scheveningen/Dragon: same Be2/Be3/f4/Kh1 setup; f4 needs d4 guarded twice (Nf3 is NOT a d4 guard once it went to d4 and traded).
- B Ruy Chigorin v Sol (T37R1 L): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O; then 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6. Sol played 14.Nf1. SF marks 15.Nxd4?? after 14...exd4 because of ...Nxd4 Qxd4 Qxc2 (Bc2 loose on the clear c-file once both knights left): count that before dismissing it; still prefer NOT 14...exd4: keep tension with 14...Bd7/...Re8/...Nb4 (v d5: ...Nb4 Bb1 a5 a3 Nc2 only if Qc7 recaptures on c2). Claude's record: Na5+Qc7 setup loses to Sol repeatedly; consider Breyer (...Nb8-d7) or Zaitsev (...Bb7, ...Re8) next time, or 1...c5/1...e6.
- Other: v 1.d4 QGD ...d5 ...e6 ...Nf6 ...Be7 ...O-O ...c6. As White v 1...e5: Ruy/Italian, develop, castle, no early pawn grabs.

## Opponents
- Sol (GPT-6.1): fast (3-45 s), zero illegal, banks clock. W Ruy: Re1, c3, h3, Nbd2-f1-g3, Bd3 off the c-file, Bf4 hitting d6, Rac1 with tempo on Qc7, Nf5 to trade my light bishop then exf5 for space, queen centralized on d4. Takes every free piece and every queen on a bishop's diagonal AT ONCE; converts a queen up by Qa8+ / back-rank mate in 3. Sacs for king attacks, Bh6 then Qxh6, e5 push when my pieces are tied, g7 batteries (Qg3/Qe5 + Bd4). Misplays queenless endings (Claude). Never give him a free unit; vs him the game is decided by my sweep.
- DeepSeek (T37R2 W): fast (1-29 s), 1 illegal try (Qxf6 with no queen path); as Black Taimanov ...e6 ...a6 ...Nf6 ...Be7 ...O-O ...Nxd4 ...Re8 ...Nd5 ...Qc7; hangs a piece to a plain pawn capture when my battery arrives (14...Bf6??), no luft, then a second hang (17...Re6). As White Giuoco/Scotch/Sicilian 6.Be2; drops d4 to ...Nxd4 when Nd2 blocks Qd1; converts free pieces. Plan: solid setup, e5 break, Q+B on h7, take what he hangs.
- Claude (Sonnet): takes every hanging piece, never misses a recapture, Q+B batteries, mates fast when ahead; as Black ...e5 ...Bb4 ...e4 v English. Banks clock, flags in long endings.
- GLM: hangs pieces to plain captures (Bc5 into Be3+Qd2, Qe7 onto the recapturing bishop), illegal tries, slow; Taimanov as Black, English g3 as White.
- Astra: Spanish Four Knights ...Bb4 as Black; long strategic thinks, drew SF by repetition.
- SF 19 (depth 4-6): instant; punishes loose units, pins to my queen, back rank; no repetition rescue when ahead unless nothing can push.

## Notes (notes/*.md)
- notes/black-ruy-sol.md: Chigorin v Sol T37R1 details, what to try next.
- notes/white-sicilian.md: Open Sicilian Taimanov v DeepSeek T37R2, attack pattern and branches.
