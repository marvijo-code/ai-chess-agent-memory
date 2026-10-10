# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate pawn/knight captures and trace EVERY bishop ray through ALL pieces. Check, attack and pin never establish destination safety.
- Name exact defenders, screens and legal recapturers. Moving one can lose guards, blocks and escapes. Refresh pins after king or pinning-piece moves.
- One piece can screen TWO targets. Before moving it, trace every newly opened enemy queen/rook/bishop ray to its endpoint.
- Before recapturing, inspect opened lines and stronger forcing replies; count the FULL exchange by values. Attacking Q/R does not force retreat: test checks FIRST.
- Track actual pawn squares and forward AND capture-promotions. A defended piece can lose to a cheaper capturer; verify my recapture is legal.
- After EVERY capture, refresh the capturing piece's attacks. Trust board changes over commentary; wins and sparse marks do not validate moves.
- When forked, compare saving the higher-value piece WITH defense of the other target. Before king moves, list guards LOST and destination attacks.

## Clock and conversion
- Clocks run during thinking. Deadline INCLUDING output: book/forced 1-5 seconds; normal tactics 20-40. Below 5 minutes use 10-15, cap 20; below 90 seconds use 1-3.
- Long thinks did not prevent captures. Calculate enemy replies, especially checks after my planned attack.
- Ahead: restrain counterplay and simplify safely. Worse or Black with draw odds: seek activity/repetition. Escort passers with king/minors.
- Opposite-colored bishops: count separated passers, blockade squares, king routes and promotion races. Keep the blocker defended.
- Queen conversion: restrict king, approach with mine, protected mate; check queen safety and stalemate.

## T20 R1: White Italian vs Stockfish, mate loss
- 3.Bc4 Nf6 4.d3 d5 exd5 Nxd5 O-O Bc5 Re1 O-O Nc3 Nxc3 bxc3! Qf6 Bg5 Qg6: Nf3 guarded Bg5. d4?! exd4! cxd4 Nxd4 Nxd4 Qxg5! removed that guard. Full chain exchanged Black's knight for my bishop and lost a pawn; it did not merely remove a central knight. No verified best replacement supplied.
- Qxc4! Rfe8 Rd5? Qxa1+: Re5 screened Qf6-e5-d4-c3-b2-a1. Moving it exposed Ra1 with check. Before rook activity, trace enemy queen diagonals through the rook to distant targets.
- Qf1 blocked checks, but later Qc4 permitted Re1+ Nxe1 Qxf2+ Kh1 Qg1#. Bc5 protected f2/g1; the rook sacrifice diverted Nf3 from its g1 guard. Test deflection checks and bishop-supported queen entry before leaving a defensive square.
- Finished with 12:52; d4/Nxd4 took 44/46 seconds. This was lost-guard and screen geometry with ample clock.

## Caro-Kann as Black
- Advance a3/e6/h4/h5/Bd3/Bxd3: Nd7/Ne7-f5/c5/Be7/O-O worked in T19. cxd4/Nxd4/Rac8 pressured c3; f6/fxe5/Nxe5 opened the f-file. A usable setup, not a forced win.
- Qxe5 Rxf2 Qxd5??: e6 screened Qe7 from Re1. Rxc3+ Kb1 Rxb2+ Kxb2 Qxa3+ Kb1 exd5 relocated my queen with check before the pawn recapture. bxc3 instead permits Qxa3+ Kb1 Qb2#, supported by Rf2.
- Depth-5 Stockfish blundered; never assume infallibility. See note for promotion and pin failures.

## Chigorin: retreats and exchanges
- d5 Nb4 Bb1: a5 frees a6; a3 Na6 Nc5 preserves N. Prepare a retreat before accepting a pawn kick.
- Nxc4 bxc4 Rxc4 trades N for TWO pawns despite attacking Q. Nc2 guarded a1: a1=Q Rxa1 Nxa1 exchanged passer for R.
- Rb1+?? Bxb1: Bd3-c2-b1 was clear. Nxd5?? exd5: Ba2-b3-c4-d5 made Kd6xd5 illegal. A time win proved no clean conversion.
- Bb1 guards e4; Be3 screens Re1. Rc1/Re1 permit Nd3's double-rook fork. Nxe3 forks Qd1/Bc2 and clears c4 for Qxc2 Qxc2 Rxc2.
- Qb6 behind Be3/d4 permits dxe5 to uncover the bishop attack AND hit Nf6. Qxc8 Rxc8 Rxc8+ Bxc8 leaves Black Q vs R; the win does not validate Qb6/Nb4.

## White Benoni: double screens
- Be3/Nc3/Rc1/Re1 vs Qa5/Rc8/Re8/Nc5/Bg7: Bxc5?? Rxc5 activates Rc5 against Nc3 and clears e3 for Bh6's attack on Rc1.
- Qd3 Bh6 Rc2 Rec8 e5 dxe5: Nc3 screens BOTH Qa5-b4-c3-d2-e1 and Rc5-c4-c3-c2. Ne4 allows Qxe1+ Kh2 Nxe4 Bxe4 Rxc2, losing both rooks despite attacking Rc5.

## Black Ruy and Four Knights
- Ruy d3: Be7 screens Re8; d5 exd5 Nxd5 leaves e5 defended only by Nc6. Nxe5 Nxe5 Rxe5 Bf6 Rxe8+ Qxe8 loses a pawn.
- Four Knights 5.Nd5 attacks Nc6/Bb4/Nf6. O-O? Bxc6 dxc6 Nxb4 Nxe4 loses a minor for pawn. Resolve attacks before castling; calculate Nxd5 branches.
- d4 vacates d2: Qf4?? Bxf4 uses Bc1-d2-e3-f4. Pinning g3 to Kh2 does not protect Qf4.
- Uncastled Nd5 Nxd5 exd5 Ne7 Nxe5 Nxd5 a3 Be7 Nxf7 Kxf7 Qh5+ Ke6 O-O: Nf6?? abandons Nd5's e3 block/f4 control, allowing forcing rook-check mate.

## Sicilian geometry
- Qa4 abandons Qd1-e2-f3's recapture: Nxf3+ gxf3 exposes Kg1. Bxb5 then attacks Qa4; respond immediately.
- c3 blocks Bb2-d4. c3 d3 Re1 d2 Red1 dxc1=Q Rxc1 loses R for pawn; Rd1 stops only forward promotion.
- Dragon Nc4 hits Qd2/Bb3: Bxc4 Rxc4 removes it. g4 BEFORE h5 permits gxh5 after Nxh5; h5 first leaves g6 protecting Nh5.
- hxg6 hxg6 clears h-file; Bxg7 Kxg7 Qh6+ Kg8 Qh7# uses Rh1. Kg8 was not forced. Uncastled Rh8/h5 makes Bh6 Bxh6 Qxh6 Rxh6 lose Q.

## Note files
- notes/accelerated-dragon.md - Rook capture geometry and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Forcing clearance, promotions and pins.
- notes/deepseek.md - Chigorin tactics and Dragon pawn order.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Benoni double screens and QGD defenders.
- notes/ruy-lopez.md - Central exchanges and bishop endings.
- notes/sicilian-maroczy.md - Recapture guards and mate.
