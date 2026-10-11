# Ruy Lopez: captures, clearance and guards

## T29 round 1: White vs Stockfish 19, mate loss
6.Bb3! Bc5 7.d3 d6 8.c3 h6 9.Re1 O-O 10.Nbd2 Bb6 11.Nf1 Ne7 12.d4 exd4 13.cxd4 Bg4 14.Qd3 c5 15.dxc5 dxc5! 16.Qe2 Nc6 17.h3?! Nd4! 18.Qe3 Bxf3 19.gxf3 c4 20.Bc2 Nxc2 21.Qxb6?? Qxb6.
- Qd3/Bb3 faced ...c4's pawn fork. After dxc5 dxc5, Black still had a c5 pawn able to advance to c4. Resolving tension did not remove that threat.
- Qe2 put Nf3 on Bg4-f3-e2: the knight was pinned to the queen. Nd4 attacked Qe2, Bb3 and Nf3 together. h3 challenged Bg4 but did not prevent this jump. Moving Q to e3 released the pin, yet Bxf3 could not be met by Qxf3 because Nd4xf3 would take Q. gxf3 damaged the king shelter.
- ...c4 attacked Bb3. Bc2 put B on Nd4's capture square. The claim that Qe3 could recapture c2 was false: e3-c2 is not a rank, file or diagonal. Nxc2 also attacked Qe3, Ra1 and Re1. List ALL targets of a knight jump before choosing a retreat.
- Qxb6 captured Bb6 but landed on Qd8-c7-b6; c7 was empty after ...c5-c4. Qxb6 lost Q for B. No surviving White recapture existed. A material-recovery purpose never makes a capture safe.
22.Bf4 Nh5 23.Bh2 Nxe1 24.Rxe1 Rfe8 25.Ng3 Qg6 26.Kf1 Nf4 27.Nf5 Qg2#.
- Bf4 cleared c1, allowing Ra1xe1 after the fork. That traded R for N; it did not repair the queen loss. Final material was R+B+N against Q+2R+N, six pawns each.
- Qg6 pinned Ng3 to Kg1 down the open g-file. Kf1 released that pin but placed K on g2-f1. Nf4 then supported Qg2# directly. Nf5 uncovered Bh2-g3-f4 against the knight but did not force a response.
- At mate, Nf4 guarded g2/e2, Qg2 controlled f1/g1, and White's Re1/f2 pawn occupied e1/f2. Scan the enemy's mate before pursuing activity or an attack on its defender.
- Only h3 was marked adverse among White's moves; unmarked Qxb6 still lost Q. No verified best replacements supplied. No invalid attempts; 11:29 remained. h3/Qe3/Qxb6 took 40/39/36 seconds: calculation discipline, not time shortage.

## T28 final: White vs Stockfish 19, mate loss
...Ba7/Bg4 11.h3 Bxf3! 12.Qxf3 exd4! 13.e5?! Nxe5! 14.Qg3 O-O 15.cxd4?! Bxd4!.
- Nc6xe5 captured P with tempo against Qf3; d6 guarded Ne5. Attacking Nf6 did not force its retreat. Ba7-b6-c5-d4 captured the recapturing c-pawn. White lost c/d/e against Black's e-pawn: two pawns down.
- ...Nh5 attacked Qg3; ...Nd3 attacked Re1/f2. Ne5-d3-f4-e2 cleared Re8's file. f2-f3 removed e3's pawn guard, so returning Bd4-e3 allowed Re8xe3. A formerly safe square needs a fresh audit.
- Qg1?? Ne2xg1 Rxg1 lost Q for N despite rook protection. Later Nf4xg2 removed the rook screening Qf3-h1. Re1+ drove Kg1-f2; Qe3# was backed by Re8. h3 luft did not answer this net.
- Finished 9:26; e5/cxd4 each took 49 seconds and Qg1 42. No verified best replacements for the early inaccuracies.

## T28 round 3: White vs Sonnet, mate win
- Chigorin Nf1 cleared Qd1-d4. Rc1/Bb1 cleared c2, uncovering an attack on Qc7. Qxc1 Bxc1 Rxc1 Qxc1 cost Black Q+R against White R+B: queen for bishop. Later safe exchanges and an escorted a-pawn converted; no forced opening edge established.

## T28 round 2: White vs Stockfish, repetition escape
- Be3 blocked Re1-e4; Bxa4 removed Bc2's support. ...exd4 opened Bb7-e4, enabling ...Nxe4 Nxe4 Bxe4 with no rook recapture.
- Nd2 cleared Bb7-g2; ...Qg6 threatened Qxg2#. Qxb5 axb5 opened Ra8-a2. Kg2 pinned Nd2 to Ra2; Kf1 released it. Ne4 opened Ra2-e2 while Ba6 guarded e2. ...Rxe2 Nxc3 Rxe3+ lost a full rook overall.
- SF repeated with Q+R versus bare K: practical escape, not a fortress.

## Retained warnings
- ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5 Bxd5?? Nd3+! Kg1 Qxd5. Rxe5 needs ...Qf6+ calculation; no verified move-12 replacement.
- Qg1 Re1! Qxe1 Qxe1+ loses Q for R. ...Qb6?? dxe5 uncovers Be3-b6. Qf3 abandons b3 to ...Nb3 against Ra1/Bd2.
- Qg6/Nf5 vs Kg8/Qf7/Nh7: Nh6+ Kh8 Nxf7+ wins Q; Qxf7+ only trades.
- ...Rf8 Rxf8+ Nxf8 b8=Q removes a pinned blockader. c2 attacks b1/d1; Ra2?? b3xa2 loses R.
