# Sicilian Maroczy: recapture paths and passed-pawn safety

## Shared opening
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5.
Qa5 pins Nc3 to Ke1 along a5-b4-c3-d2-e1. Qd1 can recapture on d4 only while d2/d3 remain clear. Nc3 does not defend Nd4.

## T7 round 2: White vs Stockfish 19, checkmate loss
7.f3 Nxd4 8.Qxd4! Bg7 9.Qd2 d6 10.Be2 Be6 11.O-O Bxc4 12.Bxc4 Qc5+! 13.Qf2 Qxc4! 14.Be3 Qa6 15.Rac1 O-O 16.Rfd1 Rfc8 17.a3 Ne8 18.Nd5 Kf8 19.f4?! Rxc1 20.Rxc1 Qb5 21.Qd2 Qxb2 22.Qxb2?! Bxb2! 23.Rb1 Bxa3! 24.Rxb7.

- f3 preserved Qxd4, correcting the earlier Bd2 recapture obstruction. This verifies that specific improvement, not every later opening move.
- c4 was defended by Be2, but ...Bxc4 Bxc4 Qc5+ forced a check response before ...Qxc4 recovered the bishop. The complete sequence exchanged bishops and cost White the c-pawn.
- Nd5 vacated c3, opening Bg7-f6-e5-d4-c3-b2. Qd2 defended b2, yet ...Qxb2 Qxb2 Bxb2 exchanged queens and still lost the pawn.
- Rb1 attacked Bb2 but allowed Bxa3, escaping while capturing another pawn. Rxb7 recovered one pawn, leaving Black two pawns ahead overall and an a-passer. Count the entire sequence before claiming recovery.
- f4 was marked inaccurate and removed f3's support of e4. No best replacement was supplied.

24...e6 25.Ne7 a5 26.Nc6 a4 27.e5 Bc5 28.Bd4 Bxd4+ 29.Nxd4 a3 30.Rb1 dxe5 31.fxe5 h6 32.Ra1 Nc7 33.Nc2 Nb5 34.Kf2 Kg7 35.Ke3 Ra4 36.Rb1 Nc3 37.Rb3 Nd5+ 38.Kf3 a2 39.Rb1?? axb1=Q.

- Rb7 really protected Ne7 along the seventh rank. However, 26.Nc6 did NOT attack Ra8: enumerate a knight's actual destinations before claiming a tempo.
- Bd4 Bxd4+ Nxd4 traded bishops while the passer advanced. Centralization alone did not stop a3.
- Ra1 blockaded a3. Nc2 attacked a3, but Ra8 defended it and Nb5 added support. An attacked passer is not necessarily capturable.
- 36.Rb1 chased Nb5 but abandoned a1. ...Nc3 attacked Rb1; Rb3 attacked the knight, but ...Nd5+ escaped with check and enabled ...a2.
- After ...a2, the pawn could promote straight on a1 OR capture on b1. 39.Rb1 placed the rook directly on its capture-promotion square. The intended rank defense of a1 was irrelevant once axb1=Q removed the rook.
- 40.Ne3 Qe4+ 41.Kf2 Qxe3+ 42.Kf1 Ra1# followed. Nd5 protected Qe3, preventing a king recapture.
- Finished with 8:09 and no illegal attempts. Several moves took 39-53 seconds; the decisive promotion capture had no adverse move mark. Safety checks, not additional thinking time or annotations, were missing.

## T3 semifinal Armageddon: earlier recapture failure
7.Bd2? Nxd4! 8.Nb5! Qb6 9.Be3?! e5! 10.Nxd4 exd4 11.Bxd4 Bc5 12.Bc3 Bxf2+ 13.Ke2 Qe3#.

- Bd2 broke the king pin but blocked Qxd4, losing Nd4. Nb5 uncovered Bd2's attack on Qa5, but the queen retreat preserved Black's advantage.
- Qb6 defended Nd4 through c5; ...e5 added another defender. Nxd4 exd4 Bxd4 removed White's last knight while Black retained Nf6: material was not recovered.
- Bxd4 attacked Qb6, but ...Bc5 interposed a protected bishop and targeted f2. Bd4 blocked that diagonal and defended f2; Bc3 removed both functions.
- After Bxf2+, Qb6 protected Bf2 through c5/d4/e3. Ke2 Qe3# used Bf2 to protect the adjacent checking queen; White's own pieces occupied d1/f1.
- Lost with 8:55 remaining. Before development or retreat, inspect blocked recaptures, queen interpositions, and every defensive function being removed.
