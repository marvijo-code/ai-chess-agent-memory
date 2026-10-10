# Open Sicilian: exchanges, passers and king safety

## T16 final: White vs Stockfish 19, repetition escape
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Ndb5 Bb4 7.a3 Bxc3+ 8.Nxc3 d5 9.exd5 exd5 10.Bd3 O-O 11.O-O Bg4 12.Qd2 Re8 13.b4 d4 14.Ne2 Bxe2 15.Bxe2! Ne4 16.Qd3 Qe7 17.Bb2 Nc5 18.bxc5! Qxe2! 19.Qxe2 Rxe2!.
- Bxe2 kept the queen off Re8's open file: Qxe2 would allow Rxe2, losing queen for rook after the recapture.
- Ne4 attacked Qd2. Its later move to c5 cleared Re8-e2 behind Qe7, enabling the queen capture with rook support. Calculate the whole chain: bxc5 removed a knight, Qxe2 removed my bishop, then queens exchanged. Material stayed balanced, with my bishop against Nc6.

20.Rfd1 Rd8! 21.Rac1! Re5 22.c3?! d3 23.Re1?! d2 24.Red1 dxc1=Q 25.Rxc1.
- Rfd1 supported Bxd4: after Nc6xd4 the rook could recapture. Rd8 supplied Black's own support. Rac1 guarded c2 against the active rook.
- c3 challenged d4 but also occupied Bb2's diagonal b2-c3-d4. Black advanced instead of exchanging. A pawn break must be checked for both loss of piece pressure and the enemy passer's next advance.
- Re1 moved Rd1 away from the file in front of d3. Attacking Re5 did not stop ...d2. Red1 restored the forward blockade too late: d2 could capture Rc1 and promote diagonally.
- ...dxc1=Q Rxc1 lost a rook for Black's pawn. Recapturing the new queen did not restore that rook. Explicitly scan d1 promotion AND c1/e1 capture-promotions before any rook move near d2.
- c3 and Re1 were marked inaccurate; no verified best replacements supplied. The concrete loss matters more than the mild marks. Re1 took 96 seconds with over 14 minutes before the turn: the missing promotion scan was not caused by time shortage.

25...Kh8 26.c4 Rxc5 27.h3 Ra5 28.Rc3 Rg8 29.Rg3 f6 30.Bc3 Ra6 31.Bb2 Ra5 32.Bc3 Ra6 33.Bb2, draw.
- c4 cleared Bb2's diagonal and attacked Re5, but ...Rxc5 removed another pawn. Final material was R+B against 2R+N, equal pawns: a substantial deficit.
- Rg3 defended a3 along the third rank until Bc3 screened that line. Bb2 reopened it. Bc3 attacked Ra5 and f6; the repeated bishop/rook maneuvers produced a practical draw, not proof of sufficient compensation or forced repetition.
- No invalid attempts; finished with 11:13. Keep seeking concrete counterplay when worse, while maintaining destination and blocker checks.

## Maroczy opening geometry
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5.
- Qa5 pins Nc3 to Ke1 via b4/c3/d2. Qd1 recaptures d4 only with d2/d3 clear; f3 supports e4. Bd2 blocks Qxd4.
- Earlier ...Bxc4 Bxc4 Qc5+ Qf2 Qxc4 lost c4 through an intermediate check. T15 Be3/b3 avoided that sequence, without certifying the setup.
- T15 13...Ng4 14.Rfc1?! Nxe3! 15.Qxe3! conceded the bishop pair. Assess the attacked bishop's exchange before routine rook development.

## T15: checking escape defeats a fork
...Rd6, White Ke3/Nd5/Be2/Rf7; 27.Kf3? h5? 28.Nxe7?? Bg4+ 29.Kf4 Bxe2.
- Bc8 reached g4 through d7/e6/f5; Bg4+ skewered Kf3/Be2. h5 protected g4 against Kxg4. Rf7 defended Ne7 but did not prevent the bishop escaping with check. ...h5 was marked mistaken; no unavoidable skewer or best alternative established.
- Later Rxa7 allowed ...Rdf8+ Rf7 Rxf7+ Nf6 Rxf6#. Bd4, Be6, Rg8 and my own e4 pawn denied king exits. Test checks and every neighboring square before pawn loot.

## Other Maroczy failures
- Nxc5 dxc5 creates a passer. Rxd4 cxd4 attacks Nc3; ...d3 attacks Be2. Calculate both recapture types and advances.
- Bd5 screened Rd8, enabling Kxd2. ...bxc4 removed Bd5's pawn guard; Ke2 allowed Rxd5.
- h8=Q Rh2+ Kg6 Rxh8: my king blocked the queen's h-file defense.
- Ka5 with own a4 versus Kc5/Rb8: ...Ra8#; own pawns can deny escapes.
- Nd5 Nxd5 exd5 Qxa2: Black removed the forking knight first; moving knights opened Bg7 toward b2, and Rac1 abandoned a2.
- Rb3 Qxb3 loses rook: b2 guards a3/c3, not b3. Qb4 Rxb4+ cxb4 Qxb4+ loses queen for rook. Rb1 axb1=Q ignores capture-promotion.
