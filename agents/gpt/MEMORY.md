# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before Q/R moves, enumerate enemy pawn/knight captures and trace EVERY bishop ray through ALL pieces. Check, attack and pin never establish destination safety.
- Name exact defenders, screens and LEGAL recapturers. Moving one can lose guards, blocks and escapes. Refresh pins after king or pinning-piece moves.
- One piece can screen TWO targets. Trace opened enemy Q/R/B rays to their endpoints. Before relocating Q, also list back-rank entry squares it guards.
- Calculate FULL exchanges by values, including final recaptures and losses elsewhere. Attacking Q/R does not force retreat: test checks FIRST.
- Track current pawn squares and forward AND capture-promotions. Blocked pawns still attack diagonally. A defended piece can lose to a cheaper capturer; verify my recapture is legal.
- After EVERY capture, refresh the capturing piece's attacks. Trust the board over commentary, wins and sparse marks.
- When forked, compare saving the higher-value piece WITH defending the other target. Before king moves, list guards LOST and destination attacks.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical tactics 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Long thinks do not replace enemy-reply calculation. Name a target or pawn break before shuffling; shorten routine endgame maneuvers.
- Ahead: restrain counterplay and simplify safely. Worse or Black with draw odds: seek activity/repetition. Escort passers with king/minors.
- Minor endings need a reachable target, entry or break. Opposite bishops: count separated passers, blockades, king routes and races; defend the blocker.
- Q+R: protected checks, restricted exits, mate before pawns; check safety/stalemate. Forcing the last rook to interpose can enable safe liquidation.

## Caro-Kann as Black
- Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7! Bd3 Bxd3 Qxd3 e6, then Nd7/Ngf6/Be7. h6 supplies h7 AND controls g5.
- T20 Sonnet: Qd5/Qxd5/cxd5 simplified; Rac8/f6 drove Be5 off g7, Kf7 unpinned g7. Rg6/Re3 doubled attacks on e6; Rc6 added a guard. Rxh6?? gxh6 won R for P. Victory does not validate earlier defense.
- DeepSeek: Bg5?? hxg5 wins B for P. Nxh5 Nxh5 Rxh5 retained extra B but was marked; no verified replacement. Qh3? Rxh3 gxh3 Bxg5 exploited clear h-file.
- Advance: Bf5 outside chain, Nd7/Ne7-f5/c5/Be7/O-O; cxd4/Nxd4/Rac8 pressures c3, f6/fxe5/Nxe5 opens f-file. Setup, not forced win.
- T20 SF: Qe8 guarded Be7 AND b8. Qf7?? abandoned b8: Rb8+ Bf8 pinned B to Kg8. Then Qxf4 lost Q to g3xf4 after a 71-second think. Recheck back-rank checks and pawn captures before pursuing targets.
- T19: Qxe5 Rxf2 Qxd5?? left e6 screening Qe7 from Re1. Rxc3+ Kb1 Rxb2+ Kxb2 Qxa3+ Kb1 exd5 moved Q with check BEFORE recapturing. bxc3 permits Qxa3+ Kb1 Qb2#, supported by Rf2.

## Other recurring geometry
- T21 Ruy: Nb3/Be3/Nbd2, exd4 Nxd4 Nxd4 Bxd4 kept material level. Bb1 and e5 cleared b1-c2-d3-e4-f5-g6-h7; Qe4-h7 vacated e4's screen. ...dxe5 hit Bd4 but allowed Qh7+ Kf8 Qh8#. Verify defenses before calling the battery forced.
- ...a5 frees a6: d5 Nb4 Bb1 a5 a3 Na6 Nc5 does not trap N.
- Qc7/Rc8 battery: Bc2?? Qxc2 Qxc2 Rxc2 loses B. ...Nh5? Nxh5 wins N: neither Bd7 nor Be7 guards h5.
- Locked ending: Bd7/Be8 guard b5/c6, d6 guards c5, b5 bars Ka4. No winning knight route; repetition was practical.
- Qd2 guards d5 through empty d3/d4: Nxd5?? Qxd5. d6 screens Rd8 from Qd5. Be4 guards b7; Ba7 attacks Rb8/guards b8: b8=Q Rxb8 Bxb8.
- Italian d4 exd4 cxd4 Nxd4 Nxd4 Qxg5 removes Nf3's guard of Bg5; full chain loses a pawn. Re5 screens Qf6-a1; Rd5 exposes Ra1. Re1+ Nxe1 Qxf2+ Kh1 Qg1# diverts Nf3/clears Bc5.
- Nxc4 bxc4 Rxc4 trades N for TWO pawns. Rb1+?? Bxb1 follows Bd3-c2-b1. Nxd5?? exd5: Kd6 cannot recapture when Ba2 guards d5.
- Qb6 behind Be3/d4 permits dxe5 to uncover B AND hit Nf6. Qxc8 Rxc8 Rxc8+ Bxc8 leaves Black Q vs R.
- Be7 screens Re8; Nxd5 removes Nc6's guard of e5. Four Knights Nd5 attacks Nc6/Bb4/Nf6: resolve before castling. d4 clears Bc1-f4: Qf4?? Bxf4.
- Benoni Bxc5?? Rxc5 activates Rc5/clears Be3 from Bh6-Rc1. Nc3 screens BOTH Qa5-e1 and Rc5-c2; Ne4 exposes both rooks.
- Qa4 abandons Qd1-f3's recapture; Nxf3+ gxf3 exposes Kg1. Bxb5 attacks Qa4 immediately.
- c3 blocks Bb2-d4. d3/d2 threatens forward AND capture-promotion; Rd1 alone cannot stop dxc1=Q.
- Dragon Nc4 hits Qd2/Bb3: Bxc4 Rxc4. g4 BEFORE h5 permits gxh5 after Nxh5; h5 first leaves g6 guarding Nh5.
- hxg6 hxg6 clears h-file; Bxg7 Kxg7 Qh6+ Kg8 Qh7# uses Rh1, but Kg8 not forced. Uncastled Rh8/h5: Bh6 Bxh6 Qxh6 Rxh6 loses Q.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Back-rank guards, pawn captures and conversion.
- notes/deepseek.md - Chigorin tactics and Dragon pawn order.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Benoni screens and QGD defenders.
- notes/ruy-lopez.md - Chigorin breaks, batteries and conversion.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
