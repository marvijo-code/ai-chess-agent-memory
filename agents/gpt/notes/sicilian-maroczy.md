# Sicilian Maroczy: exchanges, checking skewers and king safety

## Opening geometry
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5.
- Qa5 pins Nc3 to Ke1 via b4/c3/d2. Qd1 recaptures d4 only while d2/d3 remain clear; f3 supports e4. Bd2 blocks Qxd4.
- Earlier Qd2/d6/Be2/Be6/O-O Bxc4 Bxc4 Qc5+ Qf2 Qxc4 lost c4 through an intermediate check.
- T14 Nb3 Qd8 avoided that sequence, not certified optimal. Nxc5 dxc5 vacated d6 and created the c5 passer; d6 was no longer a pawn target.

## T15 round 2: White vs Stockfish 19, mate loss
7.f3 Nxd4 8.Qxd4! Bg7 9.Be3 d6 10.Qd2 O-O 11.Be2 Be6 12.O-O Rfc8 13.b3 Ng4 14.Rfc1?! Nxe3! 15.Qxe3! Rc6 16.Nd5 Re8?! 17.Rab1 Qc5 18.Qxc5 dxc5.
- Be3 and b3 avoided the earlier c4-loss line. Rfc1 supported Nc3 but allowed Black to obtain the bishop pair. Assess the attacked bishop's exchanges before routine rook development. No engine-best replacement for Rfc1 was supplied.
- Nd5 threatened Nxe7+ against Kg8/Rc6, but Black moved the rook to e8. Reassess threats after defenders relocate.

### Pawn protection makes a checking skewer safe
19.Rd1 f5 20.Kf2 fxe4 21.fxe4 Bc8 22.Ke3 Kh8 23.Rf1 Bd4+ 24.Kd3 Be5 25.Rf7 Rd6 26.Ke3 Bd4+ 27.Kf3? h5? 28.Nxe7?? Bg4+ 29.Kf4 Bxe2.
- Kd3 had put Nd5 between Rd6 and my king; Ke3 released that pin. Unpinning the knight did not establish that its capture was safe.
- With Kf3 and Be2, Bg4+ skewered king and bishop along g4-f3-e2. Bc8 reached g4 through clear d7/e6/f5. Black's h5 pawn protected g4, preventing Kxg4.
- Nxe7 attacked Bc8 and was defended by Rf7, but the bishop escaped with check, then took Be2 after my king moved. Check took priority over the fork. ...h5 was marked a mistake: no claim that the skewer was unavoidable before Nxe7, and no verified best alternative supplied.
- After Bxe2, I had two rooks and knight against two rooks and two bishops, with one extra pawn. The active rook did not compensate for the lost bishop.

### Rook checks outrun pawn collection
30.Nd5 g5+ 31.Kxg5 Rg8+ 32.Kf5 Bg4+ 33.Kf4 Be6 34.Rxb7 Rdd8 35.Rxa7 Rdf8+ 36.Rf7 Rxf7+ 37.Nf6 Rxf6#.
- Kxg5 cleared the g-file for Rg8+; king activity became exposure. Be6 attacked Rf7, so Rxb7 moved an attacked rook, but subsequent captures still required a king-safety scan.
- Before Rxa7, ...Rdf8+ was decisive. Bd4 controlled e3/e5; my e4 pawn occupied e4. Be6 controlled g4, also guarded by h5. Rg8 controlled g3/g5, and the checking rook controlled f3/f5. The king had no exit.
- Rf7 blocked the check but was captured; Nf6 was then the only legal block and was also captured. Test rook checks and all eight neighboring squares before pawn grabs.
- No invalid attempts; 12:56 after Nxe7 and 11:24 at mate. Nxe7 took 42 seconds. Calculation lacked a forcing-reply scan; clock shortage did not cause the loss.

## T14 round 1: exchanges and passers
- Bxd4? Rxd4? Rfd1 Rhd8 Rxd4? cxd4 attacked Nc3; d3 then attacked Be2. Both recapture types require calculation. Equal material did not reduce pressure with Rd8 behind the passer.
- ...Bc6 drove Na4 to c3; ...Bxc3 damaged the structure. ...Ba4 attacked blockading Rd1; Be2 Bxd1 Bxd1 conceded rook for bishop.
- Bd5 screened Rd8, enabling Kxd2. ...bxc4 removed c4's protection of Bd5; Ke2 allowed Rxd5. Rescue the screen after its defender disappears.
- Kh5/h7 versus Rg2/Ke6: h8=Q Rh2+ Kg6 Rxh8. My king blocked Qh8's defense down the h-file.
- Ka5 with own pawn a4 versus Kc5/Rb8: f4 Ra8#. Kc5 covered b4/b5/b6; a4 occupied an escape.

## Earlier destination failures
- Nd5 Nxd5 exd5 Qxa2: Black removed the forking knight first; moving both knights opened Bg7 toward b2, and Rac1 abandoned a2.
- Qa2 attacks b3: Rb3 Qxb3 loses rook; b2 guards a3/c3, not b3. Ba7 Rxa7 can lose to the other blockading rook.
- Qb4 Rxb4+ cxb4 Qxb4+ loses queen for rook. Count the full chain.
- Rb1 axb1=Q: a2 has both forward and capture-promotions.
