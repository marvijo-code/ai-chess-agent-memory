# Chess memory

## Move discipline
- Start with the enemy's last move: ALL attacks, changed pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate pawn/knight captures and trace EVERY bishop ray through ALL pieces. An attack or pin never establishes destination safety.
- Name exact defenders and legal recapturers. Moving a defender/screen can lose guards, blocks, escapes and recaptures. Refresh pins after king or pinning-piece moves.
- Before recapturing, inspect opened lines and stronger forcing replies; recount the full exchange. Queen attacks do not force retreat: test checks FIRST.
- Track actual pawn squares and BOTH forward/capture-promotions. A defended piece can lose to a cheaper capturer; calculate the resulting trade.
- After EVERY capture, refresh the capturing piece's attacks. Trust board changes over commentary; wins and sparse marks do not validate moves.
- When forked, compare saving the higher-value piece WITH defense of the other target. Before king moves, list guards LOST as well as destination attacks.

## Clock and conversion
- Use actual start/remaining clocks; posted clocks run. Deadline INCLUDING output: book/forced 1-5 seconds; normal tactics 20-40. Below 5 minutes use 10-15, cap 20; below 90 seconds use 1-3.
- Unbounded turns caused flags; long thinks did not prevent captures. Spend calculation on enemy replies.
- Ahead: restrain counterplay and simplify safely. Worse or Black with draw odds: seek activity/repetition. Escort passers with king/minors.
- Opposite-colored bishops are not an automatic draw: count separated passers, blockade squares, king routes and promotion races. Keep the blocker defended.
- Q vs bare king: restrict, approach, protected mate; check queen safety and stalemate.

## Black vs Sonnet: T19 d3 Ruy
- ...Bb7/...Re8 with Be7 still on e7: after ...d5 exd5 Nxd5, e5 has only Nc6's defense. Nxe5 Nxe5 Rxe5 Bf6 Rxe8+ Qxe8 conceded a pawn: the bishop's rook attack allowed a checking exchange. Calculate this chain before the break; no opening refutation or best replacement established.
- Kd6/Rh6 vs Be1, c3/d4: ...b4 cxb4 axb4 Bxb4+ lost another pawn. Vacating c3 opened Be1-d2-c3-b4-d5-c6's ray; b4-c5-d6 checked the king.
- T19 ...Bf5+ was protected by Ke5. After Kg5, ...Kd4?? abandoned Bf5: Kxf5! was safe; f7 guards e6/g6, not f5. Then h5-h8=Q outran queenside pawn grabs.
- Sonnet converted with mutually protected Bg7/f6 and an h-passer. A light-squared bishop cannot capture f6; calculate blockade and both wings before exchanging into this ending. Lost with 8:20 remaining; sparse marks omitted the bishop loss.

## Four Knights: Black vs Stockfish
- 4...Bb4 5.Nd5 attacks Nc6/Bb4/Nf6. T18 5...O-O? Bxc6 dxc6 Nxb4 Nxe4 lost a minor for a pawn. Resolve the attacks before castling; calculate ...Nxd5 branches.
- d4 vacated d2: ...Qf4?? Bxf4 used Bc1-d2-e3-f4. Pinning g3 to Kh2 did not protect Qf4. ...Nc3/Nxb1 recovered R for Q, not equality.
- ...Ne3 supported by f4 allowed fxe3 fxe3, N for pawn. Require concrete passer compensation.
- Uncastled Nd5 Nxd5 exd5 Ne7 Nxe5 Nxd5 a3 Be7 Nxf7 Kxf7! Qh5+ Ke6 O-O: ...Nf6?? abandoned Nd5's e3 block/f4 control, allowing Re1+ Ne4 Rxe4+ Kf6 Rf4+ Ke6 Qf5+ Kd6 Rd4#.
- ...e4/Qe2/Qe7 releases e4's pin. dxc6 exf3 cxd7+ Bxd7! Bxd7+ Kxd7! Qxe7+ Bxe7 gxf3 leaves Black a pawn down, not proven lost.
- Castled Bxe6 fxe6 Qb3: Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4.
- Qg6+ Kh8 Nf7+! Rxf7 Re8+ Rf8 Rxf8#: connected rooks cannot replace king escapes or stop rook deflection.

## Chigorin: screens, tension and files
- Bb1 guards e4; Be3 screens Re1. Moving Bb1 can allow ...Ncxe4 Nxe4 Nxe4. Rc1/Re1 permit ...Nd3's double-rook fork.
- ...a5 frees a6 for Nb4-a6-c5; d6 supports Nc5. ...a4 b4 permits ...axb3 e.p.; Bxb3 abandons e4, axb3 can open Ra8-a1.
- Open c-file: ...Nxe3 forks Qd1/Bc2 AND clears c4 for ...Qxc2 Qxc2 Rxc2. T18 ...h6/...Nc4 were blunders despite the win.
- ...Rc2?? Qxc2 preserves Ne3's Qb6-f2 screen; Nxc2?? Qxf2+ loses. Bd6 vs Kh2: ...f5 exf5?? e4+ opens the bishop ray and hits Nf3. Rc2 can pin g2, forbidding g3 against ...Be5#.
- T18 White vs Sonnet: intact c3/d4 vs c5/e5 made Ng3?/Be3?? unsound; do not transfer an exchanged-c-pawn setup blindly. Against ...c4, a4/b3 exchanges left c3 loose.
- e5?! dxe5? Bxe5 opened e5-d6-c7-b8 against Rb8; ...Bxd5?? Bxb8 won the exchange. Recovery did not validate e5.
- Bxc6 Nxc6 forked Rd4/Ba7; Bb6?! Nxd4 Bxd4+ conceded the exchange. Compare rook escapes defending the bishop.

## White: Benoni and Sicilian
- Benoni g4? removed g2's guard of Bf3: Qf2 hit Bf3/b2. Re3 guarded Ne2; Rc1 allowed Qd2's double attack, Rg3 abandoned Ne2. Blockading c2 did not stop Rc8-c3#; f4/h4 blocked exits.
- Sicilian Qa4? abandoned Qd1-e2-f3's recapture: ...Nxf3+ gxf3 exposed Kg1. ...Bxb5 then attacked Qa4; Rfd1/Kg2 ignored it.
- Bh5? g6 Bf3 lost tempi. Ke2 allowed ...Re8+ Ne5 Rxe5#: test rook checks before central king moves.
- ...Bxe2 Bxe2 keeps Q off Re8's file. ...Nc5 bxc5 Qxe2 Qxe2 Rxe2 trades N for B and queens.
- c3 blocks Bb2-d4. c3 d3 Re1 d2 Red1 dxc1=Q Rxc1 loses R for pawn; Rd1 stops only forward promotion.
- Dragon ...Nc4 hits Qd2/Bb3: Bxc4 Rxc4 removes it. g4 BEFORE h5 permits gxh5 after ...Nxh5; h5 first leaves g6 protecting Nh5.
- hxg6 hxg6 clears h-file; Bxg7 Kxg7 Qh6+ Kg8 Qh7# uses Rh1. ...Kg8 was not forced; ...Nxe4 abandons h7.
- ...gxh5 Bh6 abandons Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R. Uncastled Rh8/...h5: Bh6?? Bxh6 Qxh6 Rxh6 loses Q.

## Note files
- notes/accelerated-dragon.md - Rook capture geometry and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Chigorin c-file tactics and Dragon pawn order.
- notes/four-knights.md - Double attacks, screens, king nets and clocks.
- notes/qgd-exchange.md - Double attacks, guards and passers.
- notes/ruy-lopez.md - d3 center, Chigorin screens and bishop endings.
- notes/sicilian-maroczy.md - Recapture guards, bishop attacks and mate.
