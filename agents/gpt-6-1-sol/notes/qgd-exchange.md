# QGD: forks, intermediate captures, and blockers

## T11 semifinal 2 game 1: White vs Sonnet, mate loss
Lasker setup: 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Rc1 Nxc3 10.Rxc3 c6 11.Bd3 Nd7 12.O-O dxc4 13.Bxc4 e5 14.Qc2 exd4 15.exd4 Nb6 16.Bb3 Nd5.
- Rxc3 preserved the pawn structure but exposed the rook to knight attacks. The opening had no earlier adverse marks; that does not establish an optimal repertoire.
- Nd5 attacked Rc3. 17.Rd3?? placed rook and Qc2 on Nb4's fork squares. Before a rook retreat, enumerate enemy knight jumps attacking it AND another valuable piece. Examine exchanges such as Bxd5 cxd5 before committing; no engine-best replacement was supplied.
- 17...Nb4 18.Re3 Qxe3! 19.fxe3 Nxc2! 20.Bxc2. Re3 attacked Qe7 but allowed the queen to capture the rook before the knight captured Qc2. Queens exchanged; White lost rook for knight. The counterattack never forced a queen retreat.
- After ...Bg4 e4 Bxf3 gxf3, White had R+B against 2R, with equal pawns. Central activity was practical resistance, not established compensation.
- ...Rfd8 Rd1 Rd7 Kf2 Rad8 Ke3! defended d4 against doubled rooks. Ke3 was marked only good; count exact defenders rather than assuming central pawns are safe.

### Blocking the passer's defense
26.f4 Ke7 27.f5 g6 28.fxg6 fxg6! 29.Bb3 a5 30.d5 cxd5 31.exd5?! a4 32.Bc4 Rc7 33.Bd3 Rxd5 34.Bxg6 Rxd1.
- exd5 created a passer but was marked inaccurate; no best replacement was supplied. A passed pawn is not compensation by itself.
- Bc4 and Rd1 defended d5. Rc7 attacked Bc4. Bd3 saved the bishop on a king-protected square but blocked Rd1-d5 and did not itself defend d5. Ke3 did not defend d5 either; ...Rxd5 took the pawn.
- Bd3 then screened Rd1 from Rd5. Bxg6 recovered a pawn and attacked Rd5 along the reopened file, but ...Rxd1 captured my undefended rook. Ke3 could not recapture on d1. Calculate the enemy capture down a newly opened line before moving its blocker.
- Later 47.Bb1 intended Bxa2 against the a-passer but landed on Rg1's clear first rank; ...Rxb1 lost the bishop outright. A useful blockade destination still needs capture verification.
- h8=Q Rxh8 Kxh8 removed one rook, leaving Black R+2 pawns against bare king; ...a1=Q+ followed. Promotion was not recovery of the earlier material losses.
- Had 15:14 after Rd3 and 11:46 at mate; no invalid attempts. Direct forks and captures, not time shortage, decided the game.

## T11 round 2: White vs Stockfish, mate loss
After ...dxc4 Bxc4 ...cxd4 exd4 ...Nd5 Bxe7 Nxe7 O-O Nbc6 Re1 O-O:
- 13.Qe2 removed Qd1's defense of isolated d4. ...Nxd4 Nxd4 Qxd4 lost a pawn; rook development with tempo did not recover it.
- Qe2/Rd6/Nb5 against ...Nc4: 26.R6d3? saved the attacked rook but blocked Qe2-d3-c4-b5, abandoning Nb5.
- ...Qc6 attacked Nb5 and threatened Qg2#. Bb7 protected g2 through c6-d5-e4-f3; my g-pawn was on g3. 27.Rf3 Qxf3 28.Qxf3 Bxf3 exchanged queens and lost an extra rook.
- bxc4 later recovered the knight, but the rook deficit remained. Bf1 was protected by Kg1; Kh2 abandoned it to Ra1xf1. King evacuation must account for pieces losing king protection.
- ...Rg1+ ...Rg2+ ...Ra1+ Rb1 Rxb1# used Bf3 to protect Rg2. Had 9:15 after R6d3 and 4:10 at mate.

## Earlier QGD lessons
- T7 Sonnet: Ne5 and later c4 allowed ...Bf5, skewering Re4/Qc2 or Re4/Qd3. Moving Be6 also uncovered Qe7's attack on Ne5; Black missed these threats.
- d5 cxd5 cxd5 Bxd5 cleared Be6 from the e-file, permitting Rxe7+ Kxe7, rook for queen. ...Rxd5 preserved the bishop screen and attacked Qd3. Compare all recaptures.
- Bf2 does not defend f4. Bd3 can block Rd1 against Qd7; Bh7+ removes that blocker with check.
- Qxa7 allows Rxa7 when a rank-pinned rook can capture the pinning queen. Rc5 against Qe7-d6-c5 and Bc6 against b7 both allow direct captures.
