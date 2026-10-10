# Chess memory

## Move discipline
- Start with the enemy's last move: ALL attacks and changed pawn controls. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate pawn/knight captures and trace sliding paths through ALL pieces. Attacking purpose does not make a destination safe.
- Name exact defenders and legal recapturers. Before moving a defender/screen, list guards, interpositions and escape squares lost. Refresh pins after king OR pinning-piece moves.
- Before recapturing, inspect opened lines and stronger forcing replies; recount the entire exchange. A queen attack need not force retreat: test checks FIRST.
- Compare capturers: one may preserve a crucial screen. Track actual pawn squares and BOTH forward/capture-promotions. Enumerate king captures/exits, own blockers and pawn attacks. Wins and sparse marks do not validate moves.

## Clock and conversion
- Use actual start/remaining clocks; posted clocks keep running. T16 Armageddon Black started with 7:30+10 and draw odds despite the nominal header.
- Hard deadline INCLUDING output: book/forced 1-5 seconds; normal tactics 20-40. Below 5 minutes use 10-15, cap 20; below 90 seconds use 1-3.
- Unbounded turns caused flags. Long thinks did not prevent capture misses; calculate enemy replies.
- Black draw odds: accept sound repetition/simplification. Ahead: progress; worse: activity/repetition. Support passers with king/minors; test checks before pawn loot.
- Q vs bare king: restrict, approach, protected mate; verify queen safety and a legal enemy move before nonchecks.

## Four Knights: Black vs Stockfish
- T17 UNCASTLED: 5.Nd5 Nxd5 6.exd5 Ne7 7.Nxe5 Nxd5 8.a3 Be7 9.Nxf7 Kxf7! 10.Qh5+ Ke6 11.O-O. Distinct from both ...e4 and castled branches; no forced opening loss established.
- 11...Nf6?? attacked Qh5 but allowed Re1+! Ne4 Rxe4+ Kf6 Rf4+ Ke6 Qf5+ Kd6 Rd4#. Moving Nd5 lost its e3 interposition and f4 control. Audit checking defenses before chasing Q; ...Ne4 no longer attacked Qh5. Ample time remained.
- Uncastled ...e4 branch: Nxd5 exd5 e4 Qe2 Qe7 dxc6 exf3 cxd7+ Bxd7! Bxd7+ Kxd7! Qxe7+ Bxe7 gxf3. Qe7 releases e4's pin; Black is a pawn down, not proven lost.
- Castled Bxe6 fxe6 Qb3: Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4. ...Be6?! weakened pawns; ...Rb8?! Qxc6 conceded two pawns.
- Qe4 hits a8 through d5/c6/b7: ...Ra8? Qxa8+. ...Qh4's mate threat can lose to Qf3+ Bf6 R1b7#.
- R1e7? Rxe7! Bxe7! Kf7! Rxf8+ Kxe7!: kings can capture away from the checking file.

## Benoni: White vs Stockfish
- g4? removed g2's guard of Bf3. Qf2! hit Bf3/b2; Bg2 Qxb2 enabled invasion/passers. Audit queen entries and lost guards before storms.
- Re3 guarded Ne2. Rc1 allowed Qd2 to hit Re3/Ne2; Rg3 abandoned Ne2 to Qxe2. Rook swings need forcing threats and defender audits.
- Rc1 blockaded c2 but not Rc8-c3#. Kg3's own f4/h4 blocked exits; Qe2 covered f2/g2/h2/g4. Test lateral rook checks behind blockaded passers.

## Chigorin
- Bb1 guards e4; Be3 screens Re1. Bc2-b3 can leave only Nd2: ...Ncxe4 Nxe4 Nxe4 wins a pawn. Rc1/Re1 permit ...Nd3's double-rook fork.
- ...a5 frees a6 for Nb4-a6-c5; d6 supports Nc5. ...a4 b4 permits ...axb3 e.p.; Bxb3 abandons e4, while axb3 can open Ra8-a1 with Bb1 blocking Re1.
- T17 White: d5 Nb4 Bb1 Rfc8 a3 Nc2 Bxc2 Qxc2 Qxc2 Rxc2 trades N for B and queens. Rab1 guards b2; scan the invading rook's other attacks. Rec1? and f3?! remain warnings despite the win.
- Be3-a7 took a loose rook through d4/c5/b6; Rc8 pinned Bd8. Rc7 supported b7; ...Kd8 unpinned Nd7, then Rxd7+ Kxd7 b8=Q removed b8's knight guard.
- T17 Black: ...Bb7/dxc5/c4 made a protected passer; Bd6 blockaded d5. T16's ...Bd7/Qxc5 branch differs; ...Nc5 there was a blunder.
- Bd6 vs Kh2: ...f5 exf5?? e4+! clears d6-e5-f4-g3-h2 AND hits Nf3. Scan discovered checks; ...f5 itself was inaccurate.
- ...Rc2??: Qxc2 preserves Ne3's Qb6-f2 screen; Nxc2?? Qxf2+ loses. Compare ALL capturers of offered material.
- ...e4 forks Qd3/Nf3 and clears Bf6-a1. Nd2 can block Qe2's guard of Bc2. Rc2 pins g2 to Kh2 against ...Qxf3.

## Sicilian: White
- ...Bxe2 Bxe2! keeps Q off Re8's file. ...Nc5 bxc5! Qxe2! Qxe2 Rxe2 trades N for B and queens.
- Rfd1 supports Bxd4; ...Rd8 guards d4. c3 blocks Bb2-d4. Calculate TWO passer advances: c3?! d3 Re1?! d2 Red1 dxc1=Q Rxc1 loses R for pawn; Rd1 stops only forward promotion.
- Qa5 pins Nc3 to Ke1. Qd1 recaptures d4 only with d2/d3 clear; Bd2 blocks it. Assess ...Ng4 bishop exchanges before routine rook development.
- Kf3? permits ...Bg4+ against Be2. ...h5 guards g4; Nxe7?? Bg4+ Kf4 Bxe2 defeats the fork. Rxa7 allowed ...Rdf8+ Rf7 Rxf7+ Nf6 Rxf6#.
- Dragon ...Nc4 hits Qd2/Bb3; Bxc4! Rxc4! removes it before attacking.
- g4 BEFORE h5: ...Nxh5?! gxh5 wins N for pawn. After h5 Nxh5 g4 Nf6 g5, g6 protects ...Nh5; g5 cannot capture it. Rxh5 did not prove compensation.
- hxg6 hxg6 clears the h-file; Bxg7 Kxg7 Qh6+ Kg8 Qh7# uses Rh1 support. ...Kg8 was not forced. Nf6 guards h7; ...Nxe4 abandons it.
- ...gxh5 Bh6 abandons Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R. Uncastled Rh8/...h5: Bh6?? Bxh6 Qxh6 Rxh6 loses Q; trace h8-h7-h6.

## Note files
- notes/accelerated-dragon.md - Rook capture geometry and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Dragon pawn order, h-file support and blockers.
- notes/four-knights.md - Opening branches, exposed king and deadlines.
- notes/qgd-exchange.md - QGD/Benoni double attacks, guards and passers.
- notes/ruy-lopez.md - Chigorin screens, rook raids and passer conversion.
- notes/sicilian-maroczy.md - Checking skewers, passers and rook mates.
