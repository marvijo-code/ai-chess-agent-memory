# Sicilian Maroczy: pins, exchanges, and passers

## Shared opening
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5.
Qa5 pins Nc3 to Ke1 along a5-b4-c3-d2-e1. Nc3 cannot legally recapture on e4/d4. Qd1 can recapture on d4 only while d2/d3 remain clear.

## T8 round 1: White vs Stockfish 19, repetition draw
7.Be3?! Nxe4! 8.Nxc6 dxc6 9.Qd4 Nf6 10.O-O-O Bg7 11.Qh4 h5 12.Be2 Bf5 13.Bd3 Ng4 14.Bxf5 Qxf5! 15.h3 Nxe3 16.fxe3 Qa5 17.Kb1 Bxc3 18.bxc3 O-O?!.

- Be3 supported Nd4 but left e4 undefended: Nc3 was pinned. T7's f3 addressed e4 and preserved Qxd4; Be3 did not address both central problems.
- Qd4 attacked Ne4 and Rh8, but ...Nf6 interposed on d4-e5-f6-g7-h8. A fork does not force a gain when one target can retreat to shield the other. Castling then freed Nc3, but did not recover the pawn.
- Bxf5 Qxf5 and ...Nxe3 fxe3 exchanged bishops and knights; ...Bxc3 bxc3 removed the remaining minor pieces. White had Q+2R against Q+2R, down one pawn with exposed c/e pawns.

19.Qxe7?! Rae8 20.Qxb7 Rb8 21.Qb4?? Rxb4+ 22.cxb4 Qxb4+ 23.Kc2 Qxc4+.

- e7 was undefended locally, but Qxe7 was marked inaccurate. No best replacement was supplied. Evaluate rook tempi, queen escapes, and king safety before collecting pawns.
- Qb4 was described as a queen-exchange offer, but Black captured with a ROOK. c3 defended b4 only enough to recapture that rook; ...Qxb4+ then removed the pawn. White lost queen and pawn for rook and retained 2R against Q+R. ...Qxc4+ cost another pawn.
- The decisive Qb4 had no adverse mark and took 51 seconds. Explicit material loss outweighs annotations and the final result.
- Before interposing an attacked queen, name every possible capturing piece and count the entire sequence. Protection by a pawn does not make a queen-for-rook exchange favorable.

27.Rxc6 Qxa2+ 28.Kf3 g5 29.Rhc1 Qd5+ 30.e4 Qd2 31.Rc7 Qf4+ 32.Ke2 Qxe4+.
- Active doubled rooks gave practical resistance but did not recover the queen deficit. Central king exposure allowed repeated checks and pawn collection.
- R1c3 later shielded the king and defended h3; g3 blocked ...Qd6+. King shuffles eventually repeated. This was an escape against depth-4 searches, not a theoretical draw or proof of compensation.
- Finished with 10:23 and no illegal attempts. Several choices took 24-51 seconds; tactical verification, not available time, failed.

## T7 round 2: White, checkmate loss
7.f3 Nxd4 8.Qxd4! Bg7 9.Qd2 d6 10.Be2 Be6 11.O-O Bxc4 12.Bxc4 Qc5+ 13.Qf2 Qxc4 14.Be3 Qa6 15.Rac1 O-O 16.Rfd1 Rfc8 17.a3 Ne8 18.Nd5 Kf8 19.f4?! Rxc1 20.Rxc1 Qb5 21.Qd2 Qxb2 22.Qxb2?! Bxb2 23.Rb1 Bxa3 24.Rxb7.

- f3 preserved Qxd4, fixing the earlier Bd2 obstruction. It did not validate later play.
- ...Bxc4 Bxc4 Qc5+ Qf2 Qxc4 exchanged bishops and won the c-pawn. Calculate forcing checks between captures.
- Nd5 opened Bg7-f6-e5-d4-c3-b2. Qd2's defense allowed a queen exchange but did not save b2. Rb1 allowed Bxa3; Rxb7 recovered only one pawn. Black remained two pawns ahead with an a-passer.
- f4 removed f3's support of e4. Nc6 later did NOT attack Ra8; enumerate actual knight destinations.
- Ra1 blockaded a3. Rb1 chased Nb5 but abandoned a1; ...Nc3 attacked the rook, then ...Nd5+ escaped Rb3 with check and enabled ...a2.
- 39.Rb1?? axb1=Q lost the rook directly. An a2 passer can promote on a1 OR capture-promote on b1. Rank defense of a1 is irrelevant after the rook is captured.
- Qe4+ Qxe3+ Ra1# followed. Finished with 8:09; the decisive promotion capture had no adverse mark.

## T3 Armageddon: recapture obstruction
7.Bd2? Nxd4! 8.Nb5 Qb6 9.Be3?! e5 10.Nxd4 exd4 11.Bxd4 Bc5 12.Bc3 Bxf2+ 13.Ke2 Qe3#.
- Bd2 blocked Qxd4. Nb5 attacked Qa5 but did not recover material; liquidation left Black an extra knight.
- Bxd4 attacked Qb6, but ...Bc5 interposed a protected bishop. Bc3 abandoned f2's defense and removed the diagonal blocker.
- Qb6 protected Bf2 through c5/d4/e3; Bf2 protected Qe3#. White's own pieces occupied d1/f1. Resolve blocked recaptures and defensive functions before counterattacking.
