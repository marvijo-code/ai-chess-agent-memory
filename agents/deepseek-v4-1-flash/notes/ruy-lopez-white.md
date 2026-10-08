# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb4 (15.Bb1 or 16.Rac1).

## What was fine (game 2)
- 11.d4, 13.cxd4 (engine !), 14.Nb3, 15.d5 all fine; blunder came at move 16.
- After 13.cxd4 the c-file opens: Black's Qc7 and Nc6-b4 ideas aim at c2.

## The 15...Nb4 moment
- Knight b4 attacks Bc2, d5 (guarded by e4), a2 (guarded by Ra1), d3 (empty). Main threat: ...Nxc2.
- 16.a3?? (my losing move): 16...Nxc2 forks Ra1 and Re1; Qc7 protects it. 17.Qxc2 Qxc2 and no White piece attacks c2 -> queen lost for knight. Also a3 stops guarding Nb3; 18...Qxb3 won the knight.
- Safe: 16.Rac1 (covers c2; 16...Nxc2 17.Rxc2, and 17...Qxc2 18.Qxc2 would mean Black gives Q for R) or 16.Bb1 (move the attacked bishop). 16.Bd3 hangs to Nxd3.
- Rule: with the c-file open, never allow ...Nxc2 unless a rook already covers c2; do not kick the b4-knight until then.

## Game 5 vs GPT-6.1 Sol (same line, lost 0-1)
- 14.d5! (engine: only good move) Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Bd7 18.Ng3 Nc5 19.Bg5 h6 20.Bh4 Rfe8 21.Qd2 Nh7 22.Qc3 Bxh4 23.Nxh4 g6 24.Rd1 Kg7: fine through ~15; here 16.a3 is safe because Qd1 AND Bb1 cover c2 (in game 2 only the queen covered it).
- Engine disliked 20.Bh4?!, 21.Qd2?, 22.Qc3??: after ...Rfe8 play Red1/Rd1 at once, keep queen e2/e3, plan f4; 23.Nxh4! was the only good move after 22...Bxh4??.
- '22.Rad1' was illegal (my own Bb1 blocked the a1-rook); 22.Red1 was the legal move. With two rooks, check each path before choosing the disambiguation.
- Losing sequence: 26.Qd2?? ...Nb3! forks Qd2+Ra1; d1 was occupied by my own rook, so no queen can defend a1 - best case loses the exchange. 27.Qxa5?? Rxa5 lost the queen for a pawn (a5 attacked by Nb3 and Ra8 via the open a-file).
- Rule: with a Black knight on c5 (or able to reach b3) never put the queen on d2; run the knight-fork scan before every queen move.

## Game management
- g2 lost 0-1 (mated on move 30). After 17...Qxc2 the game was over; I still burned 30-55s per move through move 23.
- g5: eight 30-45s thinks on moves 14-22, then the fork blunder; in dead-lost positions play 5s moves and keep the clock.
