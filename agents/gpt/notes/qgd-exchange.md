# White d4: double attacks, defenders and passers

## T17 round 2: Benoni vs Stockfish 19, mate loss
1.d4 Nf6 2.c4 c5 3.d5 g6 4.Nc3 Bg7 5.e4 d6 6.Nf3 O-O 7.Be2 e6 8.O-O exd5 9.cxd5 Bg4 10.h3 Bxf3! 11.Bxf3 Nbd7 12.Bf4 Qe7 13.Re1 a6 14.a4 Rfe8 15.Qd2 Rac8 16.Rad1 Ne5 17.Be2 c4 18.Bh6 Bxh6 19.Qxh6! b5 20.axb5 axb5 21.f4 Qa7+ 22.Kh1 Ned7! 23.Bf3 Qc5.
- Opening remained roughly balanced in the supplied shallow evaluations. Qxh6 was the only good move; this game does not establish an opening failure or a best replacement for later errors.
- f4 vacated f2 and enabled Qa7+ along a7-b6-c5-d4-e3-f2-g1. Include newly opened queen diagonals in pawn-push calculations.

24.g4? Qf2! 25.Bg2 Qxb2 26.Re3 b4 27.Ne2 c3 28.Rc1 Qd2 29.Rg3 Qxe2.
- g4 removed g2's protection of Bf3. Qf2 attacked that bishop vertically and b2 along f2-e2-d2-c2-b2. Bg2 saved the bishop but conceded the pawn and queen invasion. Preparing g5 was too slow; calculate enemy queen entries and every guard lost before a pawn storm. No verified best replacement supplied.
- Re3 guarded Nc3 across d3, then Ne2 after the retreat. Black's b4 supported c3, while Rc8 stood behind the passer.
- Rc1 moved Rd1 away from its control of d2. Qd2 then attacked Re3 diagonally and Ne2 horizontally. Rg3 saved the rook but removed Ne2's e-file defender, permitting Qxe2. List ALL attacks from the last queen move, and what a proposed rook swing abandons.
- The queen on h6 and rook on g3 did not create a forcing attack quickly enough to justify the knight loss. Sparse move marks did not absolve this direct capture.

30.g5 Nxe4 31.Bxe4 Qxe4+ 32.Kh2 Qd4 33.Rg4 Re2+ 34.Rg2 Rxg2+ 35.Kxg2 Qe4+ 36.Kg3 c2 37.h4 Qd3+ 38.Kg4 Qe2+ 39.Kg3 Rc3#.
- Rc1 blockaded c2 but did not prevent Rc8-c3 with a lateral checking line. At mate Qe2 covered f2/g2/h2 and g4; Rc3 covered f3/g3/h3. Own f4 and h4 occupied the remaining adjacent exits. A blockaded passer can coexist with a decisive rook invasion.
- No invalid attempts; finished with 9:03. g4 took 45 seconds, Rg3 58: missing guard and double-attack scans caused the loss despite ample clock.

## T11 semifinal 2: QGD vs Sonnet, mate loss
After the Lasker exchanges, White Rc3/Qc2 faced ...Nd5. 17.Rd3?? allowed Nb4, forking rook and queen. 18.Re3 Qxe3! 19.fxe3 Nxc2! 20.Bxc2 traded queens and lost rook for knight. Attacking the queen did not force retreat; calculate its capture before the fork resolves. Examine Bxd5 cxd5 before retreating, without claiming it engine-best.
- Ke3 defended d4 against doubled rooks; name exact defenders.
- d5 cxd5 exd5?! a4 Bc4 Rc7 Bd3 Rxd5 Bxg6 Rxd1: Bd3 blocked Rd1's defense of d5 and did not itself guard d5. Bxg6 then cleared the file, exposing undefended Rd1. Ke3 could not recapture on d1.
- Bb1 intended to stop a2 but landed on Rg1's clear first rank: Rxb1. Blockade destinations still need capture checks. Had ample time.

## T11 round 2: QGD vs Stockfish, mate loss
- Qe2 removed Qd1's defense of isolated d4: Nxd4 Nxd4 Qxd4 lost a pawn.
- R6d3? saved a rook but blocked Qe2-d3-c4-b5, abandoning Nb5. Qc6 attacked it and threatened Qg2# with Bb7 support; the g-pawn was on g3. Rf3 Qxf3 Qxf3 Bxf3 lost an extra rook.
- Kh2 abandoned Bf1's king protection to Ra1xf1. King evacuation must include guards lost.

## Other QGD geometry
- ...Bf5 can skewer Re4/Qc2 or Re4/Qd3; moving Be6 can uncover Qe7 against Ne5.
- d5 cxd5 cxd5 Bxd5 cleared Be6 from the e-file, allowing Rxe7+ Kxe7, rook for queen. Rxd5 preserved the bishop screen and attacked Qd3: compare recapturers.
- Bf2 does not defend f4. Bd3 can block Rd1 against Qd7; Bh7+ removes that blocker with check.
- Qxa7 allows Rxa7 when the pinned rook captures the pinning queen. Rc5 against Qe7-d6-c5 and Bc6 against b7 allow direct captures.
