# Ruy Lopez: Chigorin safety and exchanges

## Shared structure
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6.
Recount e4/d4 defenders after reroutes, exchanges, and rook lifts. Against ...Nb4, preserve Bc2 before a3 if ...Nxc2 forks the rooks.

## T6 round 3: Black vs Sonnet, checkmate win
14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.Rc1 Rac8 18.Qe2 Qb6?? 19.dxe5 Qd8 20.exf6 Bxf6 21.Qxb5 Qc7 22.Qxa4 Bxb2 23.Rb1 Bc3 24.Bb6 Qd7 25.Rb3 Bf6 26.Ne5?? dxe5 27.Nf3 Qe6 28.Bd3 Rb8?! 29.Bc4 Qe7 30.a3? Nd4?? 31.Nxd4 exd4 32.Bd3? Rfd8? 33.Bxd8 Rxd8 34.Qb4 Qc7 35.Qxb7 Qf4 36.Re2 Be5 37.Rb5?? Qh2+ 38.Kf1 Qh1#.

### Queen placement and pin calculation
- Qb6 stood on Be3's diagonal through d4/c5. dxe5 removed the d4 blocker, attacked the queen AND Nf6. Qd8 saved the queen but exf6 won a knight. Test discovered attacks before putting the queen behind central tension.
- Qb6 took 52 seconds; Qd8 took 55. The tactical error was not clock pressure.
- White's Ne5 attacked Qd7, but d6xe5 captured it without moving Nc6. Qa4's diagonal a4-b5-c6-d7 remained blocked. A pinned knight does not prohibit captures by another piece.
- ...Qe6 removed the queen from the pin line before Nc6 moved. Refresh the actual alignment rather than retaining an old pin.

### Passed pawn and exchange giveaway
- ...Rb8 defended Bb7 but was marked inaccurate. ...Nd4 was a blunder despite attacking Rb3/Nf3; Nxd4 exd4 created a passed pawn supported by Bf6, not proof of a sound trade. No best replacements were supplied.
- After the knight left c6 and the queen left c7, Bb6's diagonal b6-c7-d8 was clear. Rfd8 allowed Bxd8 Rb8xd8: White traded bishop for rook and won the exchange.
- Qc7 defended Bb7 only with the queen. Rb3 supported Qxb7 through clear b4/b5/b6, so ...Qxb7 Rxb7 would exchange queens while conceding the bishop. Count the entire sequence, not just the first capture.

### Verified forcing mate
- With White Kg1/Re2 and pawns f2/g2/h3, ...Be5 threatened Qh2+ Kf1 Qh1#. Qf4 initially blocked Be5-f4-g3-h2; Qh2 vacated f4 and became protected by the bishop.
- Rb5 attacked Be5 but allowed the forcing checks. At Qh2+, f2/g2 were occupied, h1/g1 were controlled, and h2 was protected; Kf1 was forced. Qh1 then controlled the first rank, while Re2 and f2/g2 denied king exits. Neither rook could capture or block.
- This mate salvaged a materially lost position; do not reuse the opening errors because of the result. Finished with 11:05 before the final increment, no illegal attempts.

## T5 semifinal: Black vs Sonnet, loss
14.Nb3 Bb7 15.Bd3 Rac8 16.Be3 Rfe8? 17.Qd2?? d5 18.exd5 Nxd5 19.dxe5 Nxe3?? 20.Qxe3 Nxe5?? 21.Nxe5 Bc5 22.Qxc5 Qxc5 23.Nxc5 Rxc5.
- Be7 blocked Re8's apparent defense of e5. After Nf3xe5, Qc7xe5 allowed Qe3xe5, still without a rook recapture. The liquidation left White a full knight ahead.
- Later Black Rc3/Rc5 faced White Ra1/Rb3/Ne3. Rb3?? allowed direct ...Rxb3, but ...Rc1+?? Rxc1 Rxc1+ Kh2 missed it. ...Rb1 then allowed Rb3xb1 through empty b2, losing the last rook. Compare captures before checks; an attacked rook can capture its attacker.

## Earlier recurring failures
- T5 White: Bd3 cleared Rc1's last blocker against Qc7. ...Nxb4 ignored Rxc7. Later Qa4?? lost to the original b5 pawn's ...bxa4.
- Nh4-f5 Bxf5 Ng3xf5, f3-f4, and Re3-g3 remove e4 defenders. Recount before attacking.
- Nb3 overlooked ...axb3 from a4. Ke4 released Ra3's pin of Nb3 but did not defend it.
- Game 4: e5 dxe5 Nxg7+ uncovered Bb1; Nxe8+ uncovered Rg3. Nxc7 exf4 exchanged queens and left an extra rook. Count both sides' captures.
- Game 4 promoted at move 58, then spent 30 seconds on Qe5+, 27 on Qc5, and 18 on Qxb4. Flagged with queen against bare king. Execute elementary mates promptly.
