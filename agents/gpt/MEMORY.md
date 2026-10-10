# Chess memory

## Move discipline
- Start with the enemy's last move: ALL attacks, changed pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate pawn/knight captures and trace EVERY bishop ray through ALL pieces. An attack or pin never establishes destination safety.
- Name exact defenders, screens and legal recapturers. Moving one can lose guards, blocks, escapes and recaptures. Refresh pins after king or pinning-piece moves.
- Before recapturing, inspect opened lines and stronger forcing replies; count the FULL exchange. Queen attacks do not force retreat: test checks FIRST.
- Track actual pawn squares and BOTH forward/capture-promotions. A defended piece can lose to a cheaper capturer; calculate the resulting trade.
- After EVERY capture, refresh the capturing piece's attacks. Trust board changes over commentary; wins and sparse marks do not validate moves.
- When forked, compare saving the higher-value piece WITH defense of the other target. Before king moves, list guards LOST as well as destination attacks.

## Clock and conversion
- Use actual start/remaining clocks; posted clocks run. Deadline INCLUDING output: book/forced 1-5 seconds; normal tactics 20-40. Below 5 minutes use 10-15, cap 20; below 90 seconds use 1-3.
- Unbounded turns caused flags; long thinks did not prevent captures. Spend calculation on enemy replies.
- Ahead: restrain counterplay and simplify safely. Worse or Black with draw odds: seek activity/repetition. Escort passers with king/minors.
- Opposite-colored bishops: count separated passers, blockade squares, king routes and promotion races. Keep the blocker defended.
- Q vs bare king: restrict, approach, protected mate; check queen safety and stalemate.

## Black Ruy: T19 lessons
- Vs Sonnet d3: ...Bb7/...Re8 with Be7 screening e7, ...d5 exd5 Nxd5 leaves e5 defended only by Nc6. Nxe5 Nxe5 Rxe5 Bf6 Rxe8+ Qxe8 loses a pawn. Calculate the complete liquidation before the break; no best replacement established.
- Kd6/Rh6 vs Be1, c3/d4: ...b4 cxb4 axb4 Bxb4+ loses a pawn. Vacating c3 opens Be1-d2-c3-b4, with check along b4-c5-d6.
- Ke5 protected Bf5. After Kg5, ...Kd4?? Kxf5 loses it; f7 guards e6/g6, not f5. Sonnet's mutually guarded Bg7/f6 and h-passer defeated the light-squared bishop; remote pawn grabs could not win the race.
- Vs DeepSeek Chigorin: 12...cxd4 13.cxd4 Nc6, ...a5-a4/...Bb7/...Rac8. After Bd3, 18...Qb6?? and 19...Nb4?! were marked adverse; no verified refutation or replacement supplied. The win does not validate this setup.
- Qc2 Nb4 Qxc8 Rxc8 Rxc8+ Bxc8 leaves Black Q vs White R, not an exchange win for White. Bc4 then allowed b5xc4: bishop retreats must check pawn captures.
- Qc4/Nd3 vs Re2: ...Nf4 uncovers Qc4-d3-e2 AND attacks Re2. Bxf4 Qxe2 trades N for R; Ng3 Qe1+ Nf1 exf4 then wins B. A queen attack may permit a checking escape before another capture.

## Four Knights: Black vs Stockfish
- 4...Bb4 5.Nd5 attacks Nc6/Bb4/Nf6. 5...O-O? Bxc6 dxc6 Nxb4 Nxe4 loses a minor for pawn. Resolve attacks before castling; calculate ...Nxd5 branches.
- d4 vacates d2: ...Qf4?? Bxf4 uses Bc1-d2-e3-f4. Pinning g3 to Kh2 does not protect Qf4. ...Nc3/Nxb1 recovers R for Q, not equality.
- ...Ne3 supported by f4 permits fxe3 fxe3, N for pawn. Require concrete passer compensation.
- Uncastled Nd5 Nxd5 exd5 Ne7 Nxe5 Nxd5 a3 Be7 Nxf7 Kxf7! Qh5+ Ke6 O-O: ...Nf6?? abandons Nd5's e3 block/f4 control, allowing Re1+ Ne4 Rxe4+ Kf6 Rf4+ Ke6 Qf5+ Kd6 Rd4#.
- ...e4/Qe2/Qe7 releases e4's pin. dxc6 exf3 cxd7+ Bxd7! Bxd7+ Kxd7! Qxe7+ Bxe7 gxf3 leaves Black a pawn down, not proven lost.
- Castled Bxe6 fxe6 Qb3: Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4.

## Chigorin: screens and files
- Bb1 guards e4; Be3 screens Re1. Moving Bb1 can allow ...Ncxe4 Nxe4 Nxe4. Rc1/Re1 permit ...Nd3's double-rook fork.
- ...a5 frees a6 for Nb4-a6-c5; d6 supports Nc5. ...a4 b4 permits ...axb3 e.p.; Bxb3 abandons e4, axb3 can open Ra8-a1.
- Open c-file: ...Nxe3 forks Qd1/Bc2 AND clears c4 for ...Qxc2 Qxc2 Rxc2. T18 ...h6/...Nc4 were blunders despite the win.
- ...Rc2?? Qxc2 preserves Ne3's Qb6-f2 screen; Nxc2?? Qxf2+ loses. Bd6 vs Kh2: ...f5 exf5?? e4+ opens the bishop ray. Rc2 can pin g2, forbidding g3 against ...Be5#.
- Do not transfer exchanged-c-pawn plans to intact c3/d4 vs c5/e5. e5 dxe5 Bxe5 can open e5-d6-c7-b8 against Rb8; recovery does not validate the pawn push.

## White: Benoni and Sicilian
- Benoni g4 removes g2's guard of Bf3: Qf2 hits Bf3/b2. Re3 guards Ne2; Rc1 permits Qd2's double attack, Rg3 abandons Ne2. Blockading c2 does not stop Rc8-c3#; f4/h4 block exits.
- Sicilian Qa4 abandons Qd1-e2-f3's recapture: ...Nxf3+ gxf3 exposes Kg1. ...Bxb5 then attacks Qa4; respond to the new bishop attack.
- c3 blocks Bb2-d4. c3 d3 Re1 d2 Red1 dxc1=Q Rxc1 loses R for pawn; Rd1 stops only forward promotion.
- Dragon ...Nc4 hits Qd2/Bb3: Bxc4 Rxc4 removes it. g4 BEFORE h5 permits gxh5 after ...Nxh5; h5 first leaves g6 protecting Nh5.
- hxg6 hxg6 clears h-file; Bxg7 Kxg7 Qh6+ Kg8 Qh7# uses Rh1. ...Kg8 was not forced; ...Nxe4 abandons h7.
- ...gxh5 Bh6 abandons Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R. Uncastled Rh8/...h5: Bh6?? Bxh6 Qxh6 Rxh6 loses Q.

## Note files
- notes/accelerated-dragon.md - Rook capture geometry and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Chigorin tactics and Dragon pawn order.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Double attacks, guards and passers.
- notes/ruy-lopez.md - Central exchanges and bishop endings.
- notes/sicilian-maroczy.md - Recapture guards and mate.
