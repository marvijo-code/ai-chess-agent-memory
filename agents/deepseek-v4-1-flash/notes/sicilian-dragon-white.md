# Sicilian Dragon - Yugoslav as White (g6, g34, g39 - all 0-1 vs Stockfish 19)

## g39 (mated m16): 8...d5 line
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.f3 O-O 8.Qd2 d5 9.exd5 Nxd5 10.Nxc6 bxc6 11.Bd4 e5 12.Bxe5?? Bxe5 13.Qxd5?? cxd5 14.Nxd5 Re8 15.Nf4?? Bxf4+ 16.Kf2 Qd4#.
- Through 11...e5 equal (+0.7 W). 12.Bxe5?? (SF ??) Bxe5: do NOT trade the dark bishop for the e5-pawn here; Black recaptures, and my queen still has no d-file entry (his Nd5 blocks d8). Retreat/defend the Bd4 (Bg3/Bc3) instead.
- 13.Qxd5?? cxd5: the c6-PAWN (from bxc6) guards d5 permanently. Q for N, lost. Same class as g37/g28: never Qx a pawn-defended square.
- Qxd8 was never possible: his Nd5 sits on the d-file. I tried it (1 illegal), then spent 83s producing the Qxd5 blunder. Before planning a long-range queen move, trace the path and re-check it after every change.
- 15.Nf4?? in a lost position: undefended f4, Bxf4+ won the knight; the vacated d5 then opened the d-file and 16...Qd4# (Kf2). When lost: defend/trade, 5-15s, no 'active' hang.
- Clock: 37-83s on moves 9-13; the blunder came after 83s.

## g6 (m15, Qa1#)
Setup 6.Be3 7.f3 8.Qd2 9.O-O-O fine through 11.Bxd4.
- 12.Bxf6?! (trade B for N, dark squares fall) 13.Nd5?! (no threat) 13...Qxa2! 14.Nxe7+?! = N for P (his f6-BISHOP recaptures - count recapturers even on checks) 15.e5?? Qa1#.
- After O-O-O, if his queen reaches a1/a2/b2 it mates (king c1, d1/d2 blocked by own Rd1/Qd2): vacate d2 or guard a1 the moment his queen heads there.

## g34 (forfeit, 3 illegal tries, m15): 6.f3 d5 7.Nxc6 bxc6 8.Nc3 e5 9.Bd3 d4!
- 9...d4! hits Nc3 (defended by e5). 10.Bxd4?? Qxd4 = B for P; correct: move the hit knight (Ne2/Nb1/a4).
- 14.Qe3?? Qxe3 with NO recapturer = queen gone (f3-pawn attacks g4/e4, not e3; Bd3 is not on the e3 diagonal). A trade offer needs a legal recapturer.
- 3 illegal Bxe3 tries = forfeit: verify the recapturer's geometry before sending.

## Rules from g6/g34/g39
- The Yugoslav setup is fine; the losses are captures/central trades: count recapturers (PAWNS!) on d5/e5/d4 before entering.
- Never trade bishop for knight/pawn without a concrete follow-up (12.Bxf6, 14.Nxe7+, 12.Bxe5, 10.Bxd4).
- d5 in the ...d5 lines: always defended by his c/b-pawns, and his Nd5 also blocks my Qd8. No queen/knight grabs there.
- Queen-entry mates after my king moves: Qa1# (O-O-O), Qd4# from d8 down an open d-file (Kf2).
