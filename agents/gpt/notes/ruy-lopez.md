# Ruy Lopez: guards, forcing replies and practical defense

## T28 round 2: White vs Stockfish 19, repetition draw
6.Bb3! Bc5 7.d3 d6 8.c3 h6 9.Re1 O-O 10.d4 Bb6 11.h3 Bb7 12.Be3 Na5 13.Bc2 Nc4 14.Nbd2 Nxb2 15.Qb1 Na4 16.Bxa4 bxa4 17.Qb4?! exd4 18.cxd4 Nxe4! 19.Nxe4 Bxe4! 20.Qxa4.
- Be3 blocked Re1-e2-e3-e4. Re1 no longer defended e4 despite the earlier development commentary. Bc2 had supported e4 through d3; Bxa4 removed that defender.
- ...exd4 vacated e5 from Bb7-c6-d5-e4. After cxd4, ...Nxe4 Nxe4 Bxe4 won e4; Re1 could not recapture through Be3. Qxa4 recovered a4 but Black remained a pawn ahead with the bishop pair. Qb4 was marked inaccurate; no verified replacement supplied.
20...Qf6 21.Nd2 Bb7 22.Rad1 Qg6 23.g3?! Qf5 24.Kh2 Qb5 25.Qxb5 axb5! 26.f3 Rxa2 27.Kg2 Ba5 28.Kf1 Bc3 29.Re2 b4 30.Rb1 Ba6 31.Ne4 Rxe2 32.Nxc3 Rxe3+.
- Nd2 removed Nf3 from Bb7's route to g2. Qg6 threatened Qxg2# with bishop support. g3 stopped that route but weakened h3: Qf5 attacked h3 via g4. It was marked inaccurate; no verified better defense supplied.
- Qxb5 axb5 opened the a-file for Rxa2 and created the b-passer. Queen exchange reduced mating threats but conceded rook activity; assess the resulting ending before calling a trade defensive.
- Kg2 CREATED Ra2's absolute pin of Nd2 through b2/c2/d2/e2/f2/g2. Kf1 released it. Bc3 then relatively pinned Nd2 to Re1; Re2 removed that endpoint but put the rook behind Nd2 on Ra2's rank.
- ...b4 cleared b5; Ba6 guarded e2 through b5/c4/d3. Ne4 attacked Bc3/d6 but removed Nd2's screen, allowing Rxe2. Kxe2 was illegal because Ba6 guarded e2. Nxc3 Rxe3+ lost R+B for B overall: a full rook, not recovered material.
- Ne4/Nxc3/d5 took 54/56/57 seconds while already badly worse. Use short verified replies and spend critical time on the exact exposed line.
- Active K/N play removed b4/c7/d6/h5, but R+B versus N and later R versus pawns remained winning for Black. After promotion, bare K faced Q+R. Central king moves accepted repetition at roughly +10 for Black. This is an exploitable depth-6 conversion failure, not a theoretical draw. No invalid attempts; finished 4:10.

## T27 White vs Stockfish: checking intermezzo, mate loss
6.Bb3 Bc5 7.Re1 O-O 8.c3 d5 9.exd5 Nxd5 10.Nxe5 Bxf2+? 11.Kxf2! Nxe5 12.Bxd5?? Nd3+! 13.Kg1 Qxd5 14.Rf1 Qc5+ 15.Kh1 Nf2+ 16.Rxf2 Qxf2.
- Kxf2 was safe: neither knight guarded f2. Bxd5 removed Nd5 but permitted Ne5-d3 WITH CHECK against Kf2/Re1 before Qxd5. Equal material afterward did not offset the exposed king; Nf2+ forced an exchange loss.
- Existing warning against Rxe5/...Qf6+ did not establish Bxd5's safety. Each alternative needs its own forcing scan; no verified move-12 replacement supplied.
17.h3 Re8 18.Qg1 Re1! 19.Qxe1 Qxe1+ 20.Kh2 Qxc1.
- Re1 pinned Qg1 to Kh1 across rank one. Qxe1 Qxe1+ gave Q for R; Nb1 blocked Ra1's recapture after Qxc1. Luft did not save the queen.
- Qb8 later pinned Nd6 to Kh2 through c7/d6/e5/f4/g3. An empty h3 was still controlled by Bc8 through d7/e6/f5/g4. Scan actual legal king flights.

## Retained patterns
- Black SF 6.d4 branch: Rad1 Qf6 Bxd6 cxd6! Qb4 Qe7 Qxd6 Qxd6 Rxd6 lost d6. Later ...Kf4/Bf5 allowed Nd5+ against king/Rc7; full rook lost. SF repeated near +8, not fortress evidence.
- ...Qb6?? dxe5! uncovers Be3-b6 with tempo. Later counterplay does not repair Q loss. c2 attacks b1/d1: Qd1?? cxd1=Q+.
- Qf3 abandons Qd1's b3 guard, allowing ...Nb3 against Ra1/Bd2. Qg6/Nf5 versus Kg8/Qf7/g7/Nh7/Bf8: Nh6+! Kh8 Nxf7+ wins Q; Qxf7+ merely trades.
- b7/Rb8/Ra8 pins blockader to Kg8; ...Rf8 Rxf8+ Nxf8 b8=Q removes it. ...Nf2 abandons Kd4 and falls to Qxf2.
- ...Nxh5 can abandon h7: Qxh7+ Kf8 Qh8# when own Re8 blocks Ke8. Ne5 can clear ...Qxg2#.
- Nbd2 or Bd3 can block Qd1/Rd1's recapture on d4/d5. Before g3/h4 calculate ...f5/...fxe4 and Qe7-f6-g5-h4+. Ra2?? b3xa2 loses R; pawn diagonals first.
