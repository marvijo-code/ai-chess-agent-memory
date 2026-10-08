# White Open Sicilian vs Stockfish Accelerated Dragon (G17, 1/2 in 43, was a queen down)

1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5 7.Nb3 Qd8 8.Be2 d6 9.O-O b6 10.Be3 Bg7 11.h3 Bb7 12.Qd2 O-O 13.Bf3?! Ne5 14.Qe2 Nfd7 15.Rfd1 Nxf3+ 16.Qxf3 Rc8 17.Nd2 f5 18.Qe2? f4! 19.Bxf4 Rxf4 20.g3 Rf7 21.Rac1 Qf8 22.Kh2?? Rxf2+ 23.Qxf2 Qxf2+ 24.Kh1 Qxg3 ... 43.Kh1 repetition.

## Evals (SF, side to move)
- Moves 7-12 were good for White (Black -0.7 to -1.0). Opening setup is fine: Nb3 vs Qa5, Be2, O-O, Be3, h3 early (h3 played on time).
- 13.Bf3?! Ne5! flipped it to +0.6 Black: Ne5 hits Bf3 and c4, forces Qe2 and a bishop-for-knight trade.
- 18.Qe2? f4! = +6. Be3 attacked, Bd4 hangs to Bxd4, Nc3 only defended by b2, and the Rf8 hits f-file. I lost B for P.
- 22.Kh2?? Rxf2+ (f2 defended only by the queen; the king stepping off g1 removed a defender).

## Fixes for next time (unverified)
- Move 13: play Rfd1 or Rac1 (or Nd5/Qd2 ideas); keep the bishop on e2 as long as Ne5 is possible, or answer ...Ne5 only with Bxe... checked. Do not put Bf3 on a square the knight can hit with tempo.
- Black's ...f5-f4 plan vs Be3: before playing a quiet move once ...f5 is on the board, count the Be3 retreat squares (d4, c1, f2 all poor). Consider 18.exf5 or 18.f4 or Rac1 first, and do not play Nd2 that blocks the Qd2-Rd1 coordination.
- My watch-list ignored pawn pushes (...f4). Add every enemy pawn push that attacks a piece of mine to the watch-list.
- King walk Kh2/Kh1 only after counting what the king stops guarding (f2, g3, h3).

## Saving a lost game
- SF at depth 4 shuttled the queen with checks (Qxh3+, Qe3+, Qh3+, Qg3+) while I played Kg1/Kh1 with Rc1 and Rc7 protecting each other and the g1/h1 squares safe. Threefold repetition followed even at +11. Build a fortress: rooks mutually protected on one file, king on g1/h1, no loose piece the queen can fork.
- Time: used about 5 min of 15; thought 20-60 s on captures. Fine, but the real errors were quiet moves at 10-30 s.
