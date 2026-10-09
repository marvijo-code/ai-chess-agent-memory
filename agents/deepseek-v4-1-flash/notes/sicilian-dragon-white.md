# Sicilian Dragon - Yugoslav as White (g6 vs Stockfish 19, lost 0-1 in 15 moves, mate)
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.f3 O-O 8.Qd2 d5 9.O-O-O dxe4 10.fxe4 Nxd4 11.Bxd4 Qa5 12.Bxf6?! Bxf6 13.Nd5?! Qxa2! 14.Nxe7+?! Bxe7 15.e5?? Qa1#

## g6 what went wrong
- Setup 6.Be3/7.f3/8.Qd2/9.O-O-O through 11.Bxd4 was fine (Black gave a knight for the d-pawn on d4).
- 12.Bxf6?! (inaccuracy): trading my dark bishop for the f6-knight lets ...Bxf6 and leaves my dark squares to the queen alone.
- 13.Nd5?!: the knight on d5 has nothing to win; Black's best is 13...Qxa2!.
- 14.Nxe7+?! = knight for pawn: the f6-BISHOP recaptures on e7. Count every recapturer, even when the capture gives check.
- 15.e5?? walked into Qa1#: king c1, own Rd1 and Qd2 fill d1/d2, b1 free, a1 hits c1 along the rank. The threat existed since 13...Qxa2 and the check did not answer it.
- Qa1 pattern: after O-O-O, if his queen reaches a1/a2/b2 it mates; vacate d2 (Qe3/Qd3) or guard a1 the moment his queen heads there. Before/just after O-O-O verify b1 has a defender and d2 can be vacated.

## g34 vs Stockfish 19 (0-1, forfeit after 3 illegal tries, m15)
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Be3 Nf6 6.f3 d5 7.Nxc6 bxc6 8.Nc3 e5 9.Bd3 d4!
- Equal-ish through 8...e5. 9...d4! clamps and hits Nc3 (d4 attacks c3 and e3, defended by e5-pawn and Qd8).
- 10.Bxd4?? Qxd4 = B for P (same class as g23: bishop grab of a twice-defended pawn). Correct: move the hit knight to a safe flight (Ne2/Nb1/a4); the clamp costs nothing. An attacked piece must be saved before any grab.
- Being a piece down, 11.Qd2 (trade offer Black just declines: ...a6, ...Qc5) and 14.Qe3?? Qxe3: my queen went to a square his Qc5 attacked, and NOTHING recaptured on e3 (f-pawn on f3 attacks g4/e4, not e3; a d3-bishop is not on the e3 diagonal). A queen trade offer is only sound chess if a recapturer exists on that square.
- Then 3 illegal tries Bxe3 (bishop d3 -> e3 is not a legal move) = forfeit. Verify the geometry of the recapturing/attacking piece before sending; illegal replies cost the game.
- Clock: 37-63s on routine moves 8-14 and it still went wrong; only the 5s final-move scan helps.
