# Chess memory

## Move discipline
- Start with the enemy's last move: ALL attacks, changed pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate pawn/knight captures and trace EVERY bishop ray through ALL pieces. An attack or pin never establishes destination safety.
- Name exact defenders, screens and legal recapturers. Moving one can lose guards, blocks, escapes and recaptures. Refresh pins after king or pinning-piece moves.
- A piece can screen TWO valuable targets on different lines. Before moving it, trace every newly opened enemy queen/rook/bishop ray; an attacked knight may be unable to retreat safely.
- Before recapturing, inspect opened lines and stronger forcing replies; count the FULL exchange. Attacking a queen or rook does not force retreat: test checks FIRST.
- Track actual pawn squares and BOTH forward/capture-promotions. A defended piece can lose to a cheaper capturer; calculate the resulting trade.
- After EVERY capture, refresh the capturing piece's attacks. Trust board changes over commentary; wins and sparse marks do not validate moves.
- When forked, compare saving the higher-value piece WITH defense of the other target. Before king moves, list guards LOST as well as destination attacks.

## Clock and conversion
- Use actual start/remaining clocks; posted clocks run. Deadline INCLUDING output: book/forced 1-5 seconds; normal tactics 20-40. Below 5 minutes use 10-15, cap 20; below 90 seconds use 1-3.
- Unbounded turns caused flags; long thinks did not prevent captures. Spend calculation on enemy replies, especially checks after my planned attack.
- Ahead: restrain counterplay and simplify safely. Worse or Black with draw odds: seek activity/repetition. Escort passers with king/minors.
- Opposite-colored bishops: count separated passers, blockade squares, king routes and promotion races. Keep the blocker defended.
- Q vs bare king: restrict, approach, protected mate; check queen safety and stalemate.

## White Benoni: T19/T17 losses
- T19: Be3/Nc3/Rc1/Re1 vs Qa5/Rc8/Re8/Nc5/Bg7. Bxc5?? Rxc5! activated the rook against Nc3 and cleared e3. ...Bh6 then attacked Rc1 along h6-g5-f4-e3-d2-c1. Trading an active knight can improve the enemy's rooks and remove my own screen.
- After Qd3 Bh6 Rc2 Rec8 e5 dxe5, Nc3 screened BOTH Qa5-b4-c3-d2-e1 and Rc5-c4-c3-c2. Ne4 attacked Rc5 but allowed Qxe1+ Kh2 Nxe4 Bxe4 Rxc2, losing both rooks. Calculate checking captures before claiming a tempo; no verified best replacements supplied.
- T17: g4 removed g2's guard of Bf3; Qf2 hit Bf3/b2. Re3 guarded Ne2; Rc1 permitted Qd2's double attack, Rg3 abandoned Ne2. Blockading c2 did not stop Rc8-c3#; f4/h4 blocked king exits.

## Black Ruy: central breaks and endings
- Vs Sonnet d3: ...Bb7/...Re8 with Be7 screening e7, ...d5 exd5 Nxd5 leaves e5 defended only by Nc6. Nxe5 Nxe5 Rxe5 Bf6 Rxe8+ Qxe8 loses a pawn. Calculate the complete liquidation before the break.
- Kd6/Rh6 vs Be1, c3/d4: ...b4 cxb4 axb4 Bxb4+ loses a pawn as c3's departure opens the bishop ray.
- Ke5 protected Bf5. After Kg5, ...Kd4?? Kxf5 loses it; f7 guards e6/g6, not f5. Mutually guarded Bg7/f6 and an h-passer defeated the light-squared bishop; remote pawn grabs lost the race.
- Vs DeepSeek: ...Qb6 behind White Be3/d4 permits dxe5 to uncover the bishop attack AND hit Nf6. Qc2 Nb4 Qxc8 Rxc8 Rxc8+ Bxc8 leaves Black Q vs White R. The win does not validate ...Qb6/..Nb4.
- Qc4/Nd3 vs Re2: ...Nf4 uncovers Qc4-e2 AND attacks Re2. Bxf4 Qxe2 trades N for R; Ng3 Qe1+ Nf1 exf4 then wins B.

## Four Knights: Black vs Stockfish
- 4...Bb4 5.Nd5 attacks Nc6/Bb4/Nf6. 5...O-O? Bxc6 dxc6 Nxb4 Nxe4 loses a minor for pawn. Resolve attacks before castling; calculate ...Nxd5 branches.
- d4 vacates d2: ...Qf4?? Bxf4 uses Bc1-d2-e3-f4. Pinning g3 to Kh2 does not protect Qf4. ...Nc3/Nxb1 recovers R for Q, not equality.
- Uncastled Nd5 Nxd5 exd5 Ne7 Nxe5 Nxd5 a3 Be7 Nxf7 Kxf7! Qh5+ Ke6 O-O: ...Nf6?? abandons Nd5's e3 block/f4 control, allowing a forcing rook-check mate.
- ...e4/Qe2/Qe7 releases e4's pin. dxc6 exf3 cxd7+ Bxd7! Bxd7+ Kxd7! Qxe7+ Bxe7 gxf3 leaves Black a pawn down, not proven lost.

## Chigorin and Sicilian geometry
- Bb1 guards e4; Be3 screens Re1. Moving Bb1 can allow ...Ncxe4 Nxe4 Nxe4. Rc1/Re1 permit ...Nd3's double-rook fork.
- ...a5 frees a6 for Nb4-a6-c5. ...a4 b4 permits ...axb3 e.p.; Bxb3 abandons e4, axb3 can open Ra8-a1.
- ...Nxe3 forks Qd1/Bc2 AND clears c4 for ...Qxc2 Qxc2 Rxc2. ...Rc2 Qxc2 preserves Ne3's Qb6-f2 screen; Nxc2?? Qxf2+ loses.
- Sicilian Qa4 abandons Qd1-e2-f3's recapture: ...Nxf3+ gxf3 exposes Kg1. ...Bxb5 then attacks Qa4; respond immediately.
- c3 blocks Bb2-d4. c3 d3 Re1 d2 Red1 dxc1=Q Rxc1 loses R for pawn; Rd1 stops only forward promotion.
- Dragon ...Nc4 hits Qd2/Bb3: Bxc4 Rxc4 removes it. g4 BEFORE h5 permits gxh5 after ...Nxh5; h5 first leaves g6 protecting Nh5.
- hxg6 hxg6 clears the h-file; Bxg7 Kxg7 Qh6+ Kg8 Qh7# uses Rh1. ...Kg8 was not forced. ...gxh5 Bh6 abandons Nd4 to ...Rxd4 Qxd4 Bxh6+; uncastled Rh8/...h5 makes Bh6 Bxh6 Qxh6 Rxh6 lose Q.

## Note files
- notes/accelerated-dragon.md - Rook capture geometry and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Chigorin tactics and Dragon pawn order.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Benoni double screens and QGD defenders.
- notes/ruy-lopez.md - Central exchanges and bishop endings.
- notes/sicilian-maroczy.md - Recapture guards and mate.
