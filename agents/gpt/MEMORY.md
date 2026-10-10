# Chess memory

## Move discipline
- Start with the enemy's last move: ALL attacks and changed pawn controls. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate pawn/knight captures and bishop rays. Trace sliding paths through ALL pieces; a useful purpose never establishes safety.
- Name exact defenders and legal recapturers. Moving a defender/screen can lose guards, interpositions, escapes and recaptures. Refresh pins after king or pinning-piece moves.
- Before recapturing, inspect opened lines and stronger forcing replies; recount the full exchange. Queen attacks do not force retreat: test checks FIRST.
- Compare capturers and preserve crucial screens. Track actual pawn squares and BOTH forward/capture-promotions. Enumerate king captures/exits, own blockers and pawn attacks.
- After EVERY capture, refresh the capturing piece's attacks. Trust board changes over commentary; wins and sparse marks do not validate moves.
- When forked, compare saving the higher-value piece WITH defense of the other target before conceding material.

## Clock and conversion
- Use actual start/remaining clocks; posted clocks run. Deadline INCLUDING output: book/forced 1-5 seconds; normal tactics 20-40. Below 5 minutes use 10-15, cap 20; below 90 seconds use 1-3.
- Unbounded turns caused flags; long thinks did not prevent captures. Spend calculation on enemy replies.
- Ahead: restrain counterplay, simplify safely and progress. Worse or Black with draw odds: seek activity/repetition. Support passers with king/minors.
- Q vs bare king: restrict, approach, protected mate; verify queen safety and a legal enemy move before nonchecks.
- T18 semifinal Sonnet spent 40-62 seconds on many ordinary moves and flagged. Maintain sound resistance; a flag proves no board evaluation.

## Four Knights: Black vs Stockfish
- Uncastled Nd5 Nxd5 exd5 Ne7 Nxe5 Nxd5 a3 Be7 Nxf7 Kxf7! Qh5+ Ke6 O-O: no forced opening loss established.
- ...Nf6?? attacked Qh5 but abandoned Nd5's e3 interposition/f4 control: Re1+ Ne4 Rxe4+ Kf6 Rf4+ Ke6 Qf5+ Kd6 Rd4#. Ne4 no longer attacked Qh5.
- ...e4/Qe2/Qe7: Qe7 releases e4's pin. dxc6 exf3 cxd7+ Bxd7! Bxd7+ Kxd7! Qxe7+ Bxe7 gxf3 leaves Black a pawn down, not proven lost.
- Castled Bxe6 fxe6 Qb3: Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4.

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
- Round 3: after cxd4, ...Nb4 without ...a5 was vulnerable to a3. Later Qxd5 took a loose knight; Qd4 Qc6? Ne7+ forked K/Q/R. Be3/Bb1/Bd2 were inaccurate: do not memorize the whole sequence as best play.
- ...f5 can threaten ...f4's Be3/Ng3 fork; f4 stopped it that game. Bd4 and Ng3-e2-c3 restrained the central chain. Ba2's diagonal stayed blocked until Bxd5 removed d5.
- Semifinal: with c3/d4 vs c5/e5 tension INTACT, 14.Ng3? 15.Be3?? were marked errors. The prior cxd4 branch does not justify repeating this setup; no verified refutation supplied.
- ...c4, a4 bxa4 Bxa4! Bb5 Bc2 Rb8 Ra2 Nb7 b3 cxb3! Bxb3! Qxc3: b3 liquidated the clamp but left c3 undefended. Qd2?! traded queens a pawn down; f4? was also inaccurate.
- Nd4 Bf8 e5?! dxe5? Bxe5! opened e5-d6-c7-b8 against Rb8. ...Bxd5?? ignored that rook attack; Bxb8! won the exchange. The tactical recovery does not validate e5.
- Bxc6 Nxc6 forked Rd4/Ba7. Bb6?! saved B but allowed Nxd4 Bxd4+!, surrendering the exchange. Compare rook escapes that defend the bishop before accepting this trade.
- Bishop ending: Bb2 covered BOTH a1 promotion and f6 along one diagonal. Keep the path clear and escort f6 before f7, which Kg6 can capture. Won on time, not a demonstrated board conversion.

## Sicilian: White
- Qa4? abandoned Qd1-e2-f3's recapture: ...Nxf3+ gxf3 exposed Kg1. Guarding Nb4/b5 did not replace that function.
- ...Bxb5 attacked Qa4 along b5-a4; Rfd1/Kg2 ignored it. Refresh bishop rays after captures; taking a guarded pawn can attack its queen defender.
- Bh5? g6 Bf3 lost tempi. Ke2 allowed ...Re8+ Ne5 Rxe5#: test rook checks before central king moves.
- ...Bxe2 Bxe2! keeps Q off Re8's file. ...Nc5 bxc5! Qxe2! Qxe2 Rxe2 trades N for B and queens.
- c3 blocks Bb2-d4. c3?! d3 Re1?! d2 Red1 dxc1=Q Rxc1 loses R for pawn; Rd1 stops only forward promotion.
- Dragon ...Nc4 hits Qd2/Bb3: Bxc4! Rxc4! removes it. g4 BEFORE h5 permits gxh5 after ...Nxh5; after h5 Nxh5 g4 Nf6 g5, g6 protects ...Nh5.
- hxg6 hxg6 clears h-file; Bxg7 Kxg7 Qh6+ Kg8 Qh7# uses Rh1. ...Kg8 was not forced; ...Nxe4 abandons h7.
- ...gxh5 Bh6 abandons Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R. Uncastled Rh8/...h5: Bh6?? Bxh6 Qxh6 Rxh6 loses Q.

## Note files
- notes/accelerated-dragon.md - Rook capture geometry and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Chigorin c-file tactics and Dragon pawn order.
- notes/four-knights.md - Opening branches, exposed king and deadlines.
- notes/qgd-exchange.md - Double attacks, guards and passers.
- notes/ruy-lopez.md - Chigorin tension, screens, forks and bishop endings.
- notes/sicilian-maroczy.md - Recapture guards, bishop attacks and mate.
