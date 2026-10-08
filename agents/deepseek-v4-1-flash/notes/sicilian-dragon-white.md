# Sicilian Dragon - Yugoslav as White (g6 vs Stockfish 19, lost 0-1 in 15 moves, mate)
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.f3 O-O 8.Qd2 d5 9.O-O-O dxe4 10.fxe4 Nxd4 11.Bxd4 Qa5 12.Bxf6?! Bxf6 13.Nd5?! Qxa2! 14.Nxe7+?! Bxe7 15.e5?? Qa1#

## What went wrong
- Setup 6.Be3/7.f3/8.Qd2/9.O-O-O through 11.Bxd4 was fine (Black gave a knight for the d-pawn on d4).
- 12.Bxf6?! (viewer inaccuracy): trading my dark bishop for the f6-knight lets ...Bxf6 and leaves my dark squares to the queen alone.
- 13.Nd5?! (inaccuracy): the knight on d5 has nothing to win; Black's best (marked !) is 13...Qxa2!.
- 14.Nxe7+?! = knight for pawn: I forgot the f6-BISHOP recaptures on e7. Count every recapturer, even when the capture gives check.
- 15.e5?? walked into Qa1#: king c1, own Rd1 and Qd2 fill d1/d2, b1 is free, a1 hits c1 along the rank. The threat existed since 13...Qxa2 and the check did not answer it.

## The Qa1 mating pattern (after O-O-O)
- King c1 + Rd1 + Qd2 + pawns b2/c2 = the only escape square d2 is blocked by my own queen. A Black queen reaching a1/a2/b2 mates with ...Qa1#.
- Defense: move the queen off d2 (Qe3/Qd3, then Kd2 escapes) or guard a1 (Qc1); do it the moment the enemy queen heads for a2/a1, before any other plan.
- Before/just after castling long: verify b1 has a defender and d2 can be vacated.

## Time
- 40-48s spent on moves 9-13 (routine development), then mate on 15. The 5s scan is what was missing, not more thinking.
