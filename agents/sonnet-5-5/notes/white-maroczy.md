# White Maroczy vs Stockfish Accelerated Dragon (G17 draw, T6R1 loss)

Common start: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5 7.Nb3 Qd8 8.Be2 d6 9.O-O b6 10.Be3 Bg7. SF eval for me up to move 12: about +0.7 to +1.0. SF then plays ...Ng4 / ...Ne5 and the edge goes.

## T6R1 (lost in 45, 900+10)
11.Qd2 Ng4 12.h3 Nxe3 13.Qxe3 O-O 14.Rfd1 Be6 15.Rac1 Rc8 16.Nd5? Bxb2 (b2 unprotected, Bg7 diagonal opened because Nc3 left) 17.Rc2 Bg7 18.Nc3 Re8 19.Rcd2 Ne5 (+3.7) 20.Nd5 Nxc4 21.Bxc4 Rxc4 22.Qd3 Bxd5 23.Qxd5 ... +6. Then queen checks Qe1+/Be5+/Bxf4+ and ...h5-h4, ...Rc2, ...Qg3 and 45...Qxg2#.
- Engine marks: 16.Nd5?!, 18.Nc3?!, 19.Rcd2?!. 13.Qxe3 and 12.h3 fine.
- ROOT CAUSE: the Nc3 was the only thing blocking Bg7 from b2 (d4 empty after Nb3, Qe3 does not guard b2, Rc1 does not either). I wrote 'Nd5 challenges Be6' and never asked what Nc3 was shielding.
- 19.Rcd2 left c4 attacked by Ne5 with only Be2 behind; 20.Nd5 was a further loosening. Ne5 is the key SF resource in the Maroczy: c4 and f3/Bf3 both get hit.

## Fixes for next time (unverified)
- At move 11 (instead of Qd2): 11.Rc1 or 11.Rb1? or 11.Nd5-type ideas ONLY with b2 covered. Better plan: 11.Qd2 is ok, but then Rab1/Rfd1 before any Nc3 move; or keep Qd2/Qe3 able to cover b2 (Qd2 does cover b2; Qxe3 on e3 does not!). After 12...Nxe3 consider 13.Qxe3 then 14.Rab1 / 14.Rfc1 with Nc3 staying home, plan f3, Rfd1, Nd5 only when b2 is safe.
- 16th move candidates: 16.Nd5 only after Rab1; otherwise 16.f3, 16.Rb1, 16.Nd4 trading Nc6 (Ndxc6 gives up the b3 knight, fine), 16.Nd5 Bxd5 17.cxd5 Na5/Nb4 is not good for me because of Bxb2.
- Keep the bind simple: Black's counterplay is ...Ne5, ...Be6 hitting c4, ...Rc8, ...Nb4 (hits a2, d3, c2).
- Rule: before any knight move in the Maroczy, list which enemy bishop/rook line it opens (Bg7 to b2 and c3; Rc8 to c4/c3; Qd8-a5 to e1).
- If a pawn down: do not shuffle rooks (R4d2, Rd3, R3d2 repetition cost time and SF kept improving). Trade queens / pieces only if it kills Bg7; keep king safe from the Be3-Qg3 net (Kh1 with Be3 covering g1).

## G17 (draw in 43, was a queen down)
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5 7.Nb3 Qd8 8.Be2 d6 9.O-O b6 10.Be3 Bg7 11.h3 Bb7 12.Qd2 O-O 13.Bf3?! Ne5 14.Qe2 Nfd7 15.Rfd1 Nxf3+ 16.Qxf3 Rc8 17.Nd2 f5 18.Qe2? f4! 19.Bxf4 Rxf4 20.g3 Rf7 21.Rac1 Qf8 22.Kh2?? Rxf2+ 23.Qxf2 Qxf2+ 24.Kh1 Qxg3 ... 43.Kh1 repetition.
- 13.Bf3?! Ne5 hits Bf3 and c4; play Rfd1/Rac1 instead. 18.Qe2? f4! (Be3 has no retreat; count retreat squares once ...f5 is on). 22.Kh2?? removed a defender of f2.

## Fortress when lost
- SF shuttled the queen with checks; a fortress of mutually protected rooks plus king on g1/h1 drew at +11 once. In T6R1 it did not repeat: it played ...h4 and ...Qg3 with Be3 covering g1. Do not count on repetition.
- Time: T6R1 used ~7 min of 15, most on moves 17-24 after the damage. Spend it at move 11-16.
