# Chess memory

## Move discipline
- Start with the enemy's last move: ALL attacks and changed pawn controls. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate pawn/knight captures and sweep bishop diagonals; trace sliding paths through ALL pieces. A useful purpose does not make a destination safe.
- Name exact defenders and legal recapturers. Moving a defender/screen can lose guards, interpositions, escapes AND planned recaptures. Refresh pins after king or pinning-piece moves.
- Before recapturing, inspect opened lines and stronger forcing replies; recount the full exchange. Queen attacks do not force retreat: test checks FIRST.
- Compare capturers: preserve crucial screens. Track actual pawn squares and BOTH forward/capture-promotions. Enumerate king captures/exits, own blockers and pawn attacks.
- Trust board changes over commentary. After EVERY capture, refresh the capturing piece's attacks. Wins and sparse marks do not validate moves.

## Clock and conversion
- Use actual start/remaining clocks; posted clocks run. T16 Armageddon Black started 7:30+10 with draw odds despite the header.
- Deadline INCLUDING output: book/forced 1-5 seconds; normal tactics 20-40. Below 5 minutes use 10-15, cap 20; below 90 seconds use 1-3.
- Unbounded turns caused flags; long thinks did not prevent captures. Spend calculation on enemy replies.
- Black draw odds: sound repetition/simplification. Ahead: progress; worse: activity/repetition. Support passers with king/minors; test checks before pawn loot.
- Q vs bare king: restrict, approach, protected mate; verify queen safety and a legal enemy move before nonchecks.

## Four Knights: Black vs Stockfish
- Uncastled Nd5 Nxd5 exd5 Ne7 Nxe5 Nxd5 a3 Be7 Nxf7 Kxf7! Qh5+ Ke6 O-O: no forced opening loss established.
- ...Nf6?? chased Qh5 but abandoned Nd5's e3 interposition/f4 control: Re1+ Ne4 Rxe4+ Kf6 Rf4+ Ke6 Qf5+ Kd6 Rd4#. Ne4 no longer attacked Qh5.
- ...e4/Qe2/Qe7 branch: Qe7 releases e4's pin. dxc6 exf3 cxd7+ Bxd7! Bxd7+ Kxd7! Qxe7+ Bxe7 gxf3 leaves Black a pawn down, not proven lost.
- Castled Bxe6 fxe6 Qb3: Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4. ...Be6?! weakened pawns; ...Rb8?! Qxc6 conceded two pawns.
- Qe4 hits a8 through d5/c6/b7. ...Qh4's mate threat can lose to Qf3+ Bf6 R1b7#.
- R1e7? Rxe7! Bxe7! Kf7! Rxf8+ Kxe7!: kings can capture away from the checking file.

## Benoni: White vs Stockfish
- g4? removed g2's guard of Bf3: Qf2! hit Bf3/b2; Bg2 Qxb2 enabled invasion/passers. Audit queen entries and lost guards before storms.
- Re3 guarded Ne2. Rc1 allowed Qd2 to hit Re3/Ne2; Rg3 abandoned Ne2 to Qxe2. Rc1 blockaded c2 but not Rc8-c3#. Own f4/h4 blocked king exits.

## Chigorin
- Bb1 guards e4; Be3 screens Re1. Bc2-b3 can leave only Nd2: ...Ncxe4 Nxe4 Nxe4 wins a pawn. Rc1/Re1 permit ...Nd3's double-rook fork.
- ...a5 frees a6 for Nb4-a6-c5; d6 supports Nc5. ...a4 b4 permits ...axb3 e.p.; Bxb3 abandons e4, while axb3 can open Ra8-a1 with Bb1 blocking Re1.
- T18 Black: ...cxd4 cxd4 opened the c-file. ...h6??/...Nc4?? were blunders, no verified repairs. Nh5?? Nxe3 forked Qd1/Bc2 AND cleared c4: fxe3 Qxc2 Qxc2 Rxc2 won a bishop.
- T18 Re2 was undefended; ...Rxe2/...Rxe1+ won both rooks. Kf2 did NOT recapture: ...Rc1 saved R. ...Re1+ Kh2 Be5#: Rc2 pinned g2, forbidding g3.
- T17 White: d5 Nb4 Bb1 Rfc8 a3 Nc2 Bxc2 Qxc2 Qxc2 Rxc2 trades N for B and queens. Rab1 guards b2. Rec1?/f3?! remain warnings despite the win.
- Be3-a7 captured R through d4/c5/b6; Rc8 pinned Bd8. Rc7 supported b7; ...Kd8 unpinned Nd7, then Rxd7+ Kxd7 b8=Q removed its promotion-square guard.
- ...dxc5/...c4 made a protected passer; Bd6 blockaded d5. Bd6 vs Kh2: ...f5 exf5?? e4+! clears d6-e5-f4-g3-h2 AND hits Nf3. ...f5 itself was inaccurate.
- ...Rc2??: Qxc2 preserves Ne3's Qb6-f2 screen; Nxc2?? Qxf2+ loses. ...e4 forks Qd3/Nf3 and clears Bf6-a1. Nd2 can block Qe2's guard of Bc2.

## Sicilian: White
- T18 Qa4? abandoned Qd1-e2-f3's planned recapture: ...Nxf3+ gxf3 exposed Kg1. Guarding Nb4/b5 did not replace that defensive function.
- ...Bxb5 attacked Qa4 directly along b5-a4. Rfd1 and Kg2 ignored it; ...Bxa4 won Q. Refresh bishop rays after captures; pawn protection can become a queen attack.
- Bh5? g6 Bf3 lost tempi while Black improved. A defended retreat can still invite a useful pawn attack. T18 ended with 9:44: calculation, not clock shortage.
- Ke2 allowed ...Re8+ Ne5 Rxe5#: Qh3 covered rank 3/f1, Ba4 covered d1, own Rd2/f2 blocked exits. Test rook checks before central king moves.
- ...Bxe2 Bxe2! keeps Q off Re8's file. ...Nc5 bxc5! Qxe2! Qxe2 Rxe2 trades N for B and queens.
- Rfd1 supports Bxd4; ...Rd8 guards d4. c3 blocks Bb2-d4. c3?! d3 Re1?! d2 Red1 dxc1=Q Rxc1 loses R for pawn; Rd1 stops only forward promotion.
- Qa5 pins Nc3 to Ke1. Qd1 recaptures d4 only with d2/d3 clear; Bd2 blocks it. Assess ...Ng4 exchanges before routine development.
- Kf3? permits ...Bg4+ against Be2. ...h5 guards g4; Nxe7?? Bg4+ Kf4 Bxe2 defeats the fork. Rxa7 allowed ...Rdf8+ Rf7 Rxf7+ Nf6 Rxf6#.
- Dragon ...Nc4 hits Qd2/Bb3; Bxc4! Rxc4! removes it. g4 BEFORE h5 permits gxh5 after ...Nxh5; after h5 Nxh5 g4 Nf6 g5, g6 protects ...Nh5.
- hxg6 hxg6 clears h-file; Bxg7 Kxg7 Qh6+ Kg8 Qh7# uses Rh1. ...Kg8 was not forced. ...Nxe4 abandons h7.
- ...gxh5 Bh6 abandons Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R. Uncastled Rh8/...h5: Bh6?? Bxh6 Qxh6 Rxh6 loses Q.

## Note files
- notes/accelerated-dragon.md - Rook capture geometry and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Chigorin c-file tactics and Dragon pawn order.
- notes/four-knights.md - Opening branches, exposed king and deadlines.
- notes/qgd-exchange.md - QGD/Benoni double attacks, guards and passers.
- notes/ruy-lopez.md - Chigorin screens, rook raids and passer conversion.
- notes/sicilian-maroczy.md - Recapture guards, bishop attacks, passers and mate.
