# Chess memory

## Move discipline
- Start with the enemy's last move: ALL attacks, changed pawn controls and newly opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate pawn/knight captures and trace EVERY bishop ray through ALL pieces. A useful attack or pin never establishes destination safety.
- Name exact defenders and legal recapturers. Moving a defender/screen can lose guards, interpositions, escapes and recaptures. Refresh pins after king or pinning-piece moves.
- Before recapturing, inspect opened lines and stronger forcing replies; recount the full exchange. Queen attacks do not force retreat: test checks FIRST.
- Track actual pawn squares and BOTH forward/capture-promotions. A defended knight can still lose to a pawn capture; calculate the resulting trade.
- After EVERY capture, refresh the capturing piece's attacks. Trust board changes over commentary; wins and sparse marks do not validate moves.
- When forked, compare saving the higher-value piece WITH defense of the other target. Enumerate king captures/exits, own blockers and pawn attacks before entering a mating net.

## Clock and conversion
- Use actual start/remaining clocks; posted clocks run. Deadline INCLUDING output: book/forced 1-5 seconds; normal tactics 20-40. Below 5 minutes use 10-15, cap 20; below 90 seconds use 1-3.
- Unbounded turns caused flags; long thinks did not prevent captures. Spend calculation on enemy replies.
- Ahead: restrain counterplay, simplify safely and progress. Worse or Black with draw odds: seek activity/repetition. Support passers with king/minors.
- Q vs bare king: restrict, approach, protected mate; verify queen safety and a legal enemy move before nonchecks.
- Sonnet flagged in T18 semifinal after many 40-62-second ordinary moves. Maintain sound resistance; a flag proves no board evaluation.

## Four Knights: Black vs Stockfish
- After 4...Bb4 5.Nd5, Nd5 attacks Nc6/Bb4/Nf6. T18 5...O-O? Bxc6! dxc6 Nxb4! Nxe4 lost a minor for a pawn. Resolve the attacked pieces concretely before castling; recheck ...Nxd5 branches.
- T18 d4 vacated d2: ...Qf4?? Bxf4 used Bc1-d2-e3-f4. Pinning g3 to Kh2 did not make Qf4 safe. ...Nc3/Nxb1 recovered R for the lost Q, not equality.
- ...Ne3 supported by f4 still allowed fxe3 fxe3, trading N for pawn. An advanced passer needs concrete compensation.
- Uncastled Nd5 Nxd5 exd5 Ne7 Nxe5 Nxd5 a3 Be7 Nxf7 Kxf7! Qh5+ Ke6 O-O: no forced opening loss established. ...Nf6?? abandoned Nd5's e3 block/f4 control: Re1+ Ne4 Rxe4+ Kf6 Rf4+ Ke6 Qf5+ Kd6 Rd4#.
- ...e4/Qe2/Qe7 releases e4's pin. dxc6 exf3 cxd7+ Bxd7! Bxd7+ Kxd7! Qxe7+ Bxe7 gxf3 leaves Black a pawn down, not proven lost.
- Castled Bxe6 fxe6 Qb3: Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4.
- Connected rooks do not secure an exposed king: T18 Qg6+ Kh8 Nf7+! Rxf7 Re8+ Rf8 Rxf8#. Check queen/knight control of g8/g7/h7 and rook-deflection checks.

## Benoni: White vs Stockfish
- g4? removed g2's guard of Bf3: Qf2! hit Bf3/b2; Bg2 Qxb2 enabled invasion/passers.
- Re3 guarded Ne2. Rc1 allowed Qd2 to hit Re3/Ne2; Rg3 abandoned Ne2. Rc1 blockaded c2 but not Rc8-c3#. Own f4/h4 blocked king exits.

## Chigorin: screens and files
- Bb1 guards e4; Be3 screens Re1. Moving Bb1 can allow ...Ncxe4 Nxe4 Nxe4. Rc1/Re1 permit ...Nd3's double-rook fork.
- ...a5 frees a6 for Nb4-a6-c5; d6 supports Nc5. ...a4 b4 permits ...axb3 e.p.; Bxb3 abandons e4, while axb3 can open Ra8-a1 with Bb1 blocking Re1.
- Open c-file: ...Nxe3 can fork Qd1/Bc2 AND clear c4 for ...Qxc2 Qxc2 Rxc2. T18 ...h6/...Nc4 were blunders despite the win.
- ...Rc2??: Qxc2 preserves Ne3's Qb6-f2 screen; Nxc2?? Qxf2+ loses. Bd6 vs Kh2: ...f5 exf5?? e4+! opens the bishop diagonal and hits Nf3.
- Rc2 can pin g2 to Kh2, forbidding g3 against ...Be5#. Check legal interpositions.

## White vs Sonnet: T18 Chigorin
- With c3/d4 vs c5/e5 tension INTACT, Ng3?/Be3?? were errors. The prior cxd4 branch does not justify this setup; no verified refutation supplied.
- ...c4 clamp: a4/b3 exchanges left c3 loose. Qd2?! traded queens a pawn down; f4? was inaccurate.
- e5?! dxe5? Bxe5! opened e5-d6-c7-b8 against Rb8; ...Bxd5?? Bxb8 won the exchange. Recovery does not validate e5.
- Bxc6 Nxc6 forked Rd4/Ba7. Bb6?! Nxd4 Bxd4+ conceded the exchange; compare rook escapes defending the bishop.
- Bb2 covered a1 promotion AND f6. Keep that diagonal clear and escort f6 before f7, which Kg6 can capture. Won on time, not demonstrated conversion.

## Sicilian: White
- Qa4? abandoned Qd1-e2-f3's recapture: ...Nxf3+ gxf3 exposed Kg1. ...Bxb5 then attacked Qa4 along b5-a4; Rfd1/Kg2 ignored it.
- Bh5? g6 Bf3 lost tempi. Ke2 allowed ...Re8+ Ne5 Rxe5#: test rook checks before central king moves.
- ...Bxe2 Bxe2! keeps Q off Re8's file. ...Nc5 bxc5! Qxe2! Qxe2 Rxe2 trades N for B and queens.
- c3 blocks Bb2-d4. c3?! d3 Re1?! d2 Red1 dxc1=Q Rxc1 loses R for pawn; Rd1 stops only forward promotion.
- Dragon ...Nc4 hits Qd2/Bb3: Bxc4! Rxc4! removes it. g4 BEFORE h5 permits gxh5 after ...Nxh5; h5 first leaves g6 protecting ...Nh5.
- hxg6 hxg6 clears h-file; Bxg7 Kxg7 Qh6+ Kg8 Qh7# uses Rh1. ...Kg8 was not forced; ...Nxe4 abandons h7.
- ...gxh5 Bh6 abandons Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R. Uncastled Rh8/...h5: Bh6?? Bxh6 Qxh6 Rxh6 loses Q.

## Note files
- notes/accelerated-dragon.md - Rook capture geometry and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Chigorin c-file tactics and Dragon pawn order.
- notes/four-knights.md - Double attacks, bishop screens, king nets and clocks.
- notes/qgd-exchange.md - Double attacks, guards and passers.
- notes/ruy-lopez.md - Chigorin tension, screens, forks and bishop endings.
- notes/sicilian-maroczy.md - Recapture guards, bishop attacks and mate.
