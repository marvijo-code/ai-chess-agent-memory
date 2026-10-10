# Chess memory

## Move discipline
- Start with the enemy's last move: ALL attacks and changed pawn controls. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate pawn/knight captures and trace sliding attacks through ALL blockers. An attacking purpose does not make a destination safe.
- Name exact defenders and legal recapturers. Before moving a defender/screen, list guards lost and lines opened. Refresh pins after king OR pinning-piece moves.
- Before recapturing, inspect opened lines and stronger forcing moves; calculate the next forcing reply and recount material.
- Forks and queen attacks do not force retreat: test checks, captures, promotions, blocks and exchanges. Compare capturers: one may preserve a crucial screen.
- Track actual pawn squares and BOTH forward/capture-promotions. Enumerate king captures/exits, own occupied squares and pawn attacks. Wins and sparse marks do not validate moves.

## Clock and conversion
- Use actual start/remaining clocks; posted clocks keep running. T16 Armageddon Black started with 7:30+10 and draw odds despite the nominal header.
- Set a hard turn deadline INCLUDING output. Book/forced moves 1-5 seconds; normal tactics 20-40. Below 5 minutes use 10-15 seconds, cap 20; below 90 seconds use 1-3.
- Routine opening thinks and unbounded endgame turns caused flags. Ample time did not prevent capture misses; calculate enemy replies.
- Black draw odds: accept sound repetition/simplification. Support passers with king/minors; test checks before pawn loot. Ahead: progress; worse: activity/repetition.
- Q vs bare king: restrict, approach, protected mate; verify queen safety and a legal enemy move before nonchecks.

## Benoni: White vs Stockfish
- T17 g4? removed g2's guard of Bf3. Qf2! attacked Bf3/b2; Bg2 Qxb2 enabled invasion and supported passers. Audit queen entries and lost pawn guards before storms.
- Re3 guarded Ne2. Rc1 allowed Qd2 to attack Re3 diagonally AND Ne2 horizontally; Rg3 abandoned Ne2 to Qxe2. Rook swings need a forcing threat and defender audit.
- Rc1 blockaded c2 but did not stop Rc8-c3#. Kg3's own f4/h4 blocked exits; Qe2 covered f2/g2/h2/g4. Calculate lateral rook checks behind blockaded passers.

## Chigorin
- ...a5 frees a6 for Nb4-a6-c5; d6 supports Nc5. Bb1 guards e4; Be3 screens Re1. Bc2-b3 may leave only Nd2: ...Ncxe4 Nxe4 Nxe4 wins a pawn. Rc1/Re1 permit ...Nd3's double-rook fork.
- ...a4 b4 permits ...axb3 e.p.; Bxb3 removes e4's bishop guard, while axb3 can clear Ra8-a1 with Bb1 blocking Re1. Qa3 may allow ...Rxa3.
- T17 ...Bb7 d5 Nb4! Bb1 Na6 a3 Nc5 Bxc5 dxc5 c4 created a protected passer; Bd6 blockaded d5. Distinguish T16's ...Bd7/Qxc5 branch; its ...Nc5 was marked a blunder.
- Bd6 vs Kh2: ...f5 exf5?? e4+! clears d6-e5-f4-g3-h2 AND attacks Nf3. Scan discovered checks before recaptures; ...f5 itself was inaccurate.
- ...Rc2?? allowed Qxc2, preserving Ne3's screen on Qb6-f2. Nxc2?? allowed Qxf2+ Kh1 Bxg3 Qxg3 Qxg3. A pre-capture pin does not validate a sacrifice.
- ...e4 can fork Qd3/Nf3 and clear Bf6-a1. Nd2 may block Qe2's defense of Bc2. Rc2 pins g2 to Kh2 against ...Qxf3.
- Nxc4 can abandon Rf7 to Kxf7. After b4 axb3 e.p. Nxb3 Nxb3, test Rxc7 Rxc7 Bxb3 before Bxb3: clearing the c-file can win Q for R.

## Four Knights: Black vs Stockfish
- Distinguish castled 6.Nd5 from uncastled 5.Nd5. Uncastled: Nxd5 exd5 e4 Qe2 Qe7 dxc6 exf3 cxd7+ Bxd7! Bxd7+ Kxd7! Qxe7+ Bxe7 gxf3. Qe7 releases e4's pin; Black is a pawn down, not proven lost.
- Castled Bxe6 fxe6 Qb3: Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4. ...Be6?! weakened pawns; ...Rb8?! Qxc6 conceded two pawns.
- Qe4 hits a8 through d5/c6/b7: ...Ra8? Qxa8+. ...Qh4's mate threat can lose to Qf3+ Bf6 R1b7#.
- R1e7? Rxe7! Bxe7! Kf7! Rxf8+ Kxe7!: a king can capture away from the checking file.

## Open Sicilian and Maroczy: White vs Stockfish
- Four Knights Sicilian: ...Bxe2 Bxe2! keeps Q off Re8's file. ...Nc5 bxc5! Qxe2! Qxe2 Rxe2 exchanges N for B and queens.
- Rfd1 supports Bxd4; ...Rd8 defends d4. c3 blocks Bb2-d4. Calculate a passer's next TWO advances: c3?! d3 Re1?! d2 Red1 dxc1=Q Rxc1 lost R for pawn. Rd1 blocks only forward promotion.
- Rg3 guards a3 only with the whole third rank clear; Bc3 screens it.
- Maroczy: Qa5 pins Nc3 to Ke1. Qd1 recaptures d4 only with d2/d3 clear; Bd2 blocks it. f3 supports e4. Assess ...Ng4 bishop exchanges before routine rook development.
- Kf3? permits ...Bg4+ against Be2. ...h5 guards g4; Nxe7?? Bg4+ Kf4 Bxe2 defeats the fork. Rxa7 allowed ...Rdf8+ Rf7 Rxf7+ Nf6 Rxf6#.
- Nxc5 dxc5 creates a passer. Rxd4 cxd4 attacks Nc3; ...d3 attacks Be2. Calculate recaptures, advances and rook files.

## Dragon: White
- ...Nc4 attacks Qd2/Bb3; Bxc4! Rxc4! removes it before attacking.
- T17: 14.g4 Rc8?! 15.h5 Nxh5?! 16.gxh5 won N for pawn. Keeping g4 until the capture avoids an exchange sacrifice; no best Black defense established.
- Contrast h5 Nxh5 g4 Nf6 g5: g6 protects ...Nh5, and g5 cannot capture it. Rxh5 gxh5/Nd5 did not establish compensation.
- T17 hxg6 hxg6 cleared the h-file; Bxg7 Kxg7 Qh6+ Kg8 Qh7# used Rh1 support. ...Kg8 was not forced. Nf6 guards h7; ...Nxe4 abandons it. Qh6 needs rook support for Qxh7.
- ...gxh5 Bh6 abandons Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R. Uncastled Rh8/...h5: Bh6?? Bxh6 Qxh6 Rxh6 loses Q; trace h8-h7-h6.

## Note files
- notes/accelerated-dragon.md - Rook capture geometry and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Dragon pawn order, h-file support and blockers.
- notes/four-knights.md - Opening branches, liquidation and deadlines.
- notes/qgd-exchange.md - QGD and Benoni: double attacks, guards and passers.
- notes/ruy-lopez.md - Chigorin screens, discovered checks and rook raids.
- notes/sicilian-maroczy.md - Checking skewers, passers and rook mates.
