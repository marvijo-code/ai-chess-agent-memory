# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before Q/R moves, enumerate pawn/knight captures and trace EVERY bishop ray through ALL pieces. Check, attack and pin never establish destination safety.
- Name exact defenders, screens and LEGAL recapturers. Moving one can lose guards, blocks and escapes. Refresh pins after king or pinning-piece moves.
- One piece can screen TWO targets. Trace newly opened enemy Q/R/B rays to their endpoints before moving it.
- Calculate FULL exchanges by values, including final recaptures and losses elsewhere. Attacking Q/R does not force retreat: test checks FIRST.
- Track current pawn squares and forward AND capture-promotions. A defended piece can lose to a cheaper capturer; verify my recapture is legal.
- After EVERY capture, refresh the capturing piece's attacks. Trust the board over commentary; wins and sparse marks do not validate moves.
- When forked, compare saving the higher-value piece WITH defending the other target. Before king moves, list guards LOST and destination attacks.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical tactics 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Long thinks do not replace calculating enemy replies. Shorten routine endgame maneuvers; name a target or pawn break before shuffling.
- Ahead: restrain counterplay and simplify safely. Worse or Black with draw odds: seek activity/repetition. Escort passers with king/minors.
- Minor endings need a reachable target, entry or viable break. Opposite bishops: count separated passers, blockades, king routes and races; defend the blocker.
- Q+R: use protected checks and restrict exits. Prefer concrete mate over pawns; check safety and stalemate. A king net forcing the last rook to interpose can enable safe liquidation.

## Caro-Kann as Black
- Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7! Bd3 Bxd3 Qxd3 e6, then Nd7/Ngf6/Be7. h6 prepares h7 AND controls g5.
- T20 Sonnet Armageddon: against Bf4/O-O-O/Nf3/Ne5, Nxe5 Bxe5 O-O Ne4 Nxe4 Qxe4 Qd5 Qxd5 cxd5 simplified. Rac8, f6! drove Be5 away from g7; Kf7 removed g7's pin. Rfd8/Bd6/Bxd6 Rxd6 reached a two-rook ending, not a proven advantage.
- Same game: f5?!, Kf6?!, a6?!, Rf7?? and Ke7? were marked; no verified replacements/refutation. Rg6 doubled attacks on e6; Rc6 restored a second guard. Rxh6?? gxh6! won R for P: unpinned g7 controls h6. Do not infer good defense from the eventual win.
- Extra-rook conversion: remove counterplay, activate king, restrict enemy king. Rh1/Ra1+ forced Ra3; Rxa3+ Kxa3 dxc4 created a passer. c1=Q and Qb2# used Rb6's support. See notes for screens and details.
- DeepSeek: Bg5?? hxg5! wins B for P. Nxh5 Nxh5 Rxh5? was marked despite retaining extra B; Qh3? Rxh3 gxh3 Bxg5 exploited clear h-file. No verified replacement for Rxh5.
- Bd4/Qf6/Nc5 vs Kg3/Re4: Nxe4+ Kf3 Qxf5+ Kg2 Qf2+ Kh1 Ng3#. Bd4 guards f2; Qf2 guards g3 and covers g1/g2/h2.
- Advance: Bf5 outside chain, Nd7/Ne7-f5/c5/Be7/O-O; cxd4/Nxd4/Rac8 pressures c3, f6/fxe5/Nxe5 opens f-file. Setup, not forced win.
- Qxe5 Rxf2 Qxd5??: e6 screens Qe7 from Re1. Rxc3+ Kb1 Rxb2+ Kxb2 Qxa3+ Kb1 exd5 relocates Q with check BEFORE recapturing. bxc3 permits Qxa3+ Kb1 Qb2#, supported by Rf2.

## Chigorin vs Sonnet
- ...a5 frees a6: d5 Nb4 Bb1 a5 a3 Na6 Nc5 does not trap N.
- T20 SF G1: ...Na4 Qe2 Rfc8 Bc2?? Qxc2 Qxc2 Rxc2 lost B to Qc7/Rc8's battery. A queen recapture did not save the bishop.
- ...Nh5? Nxh5! recovered N: neither Bd7 nor Be7 guarded h5. ...g6 Ng3! saved it. Trace actual bishop geometry.
- Rc1 Rxc1 Nxc1 simplified safely, but Bd7/Be8 guarded b5/c6, d6 guarded c5 and b5 barred Ka4. No winning knight route; repetition was practical. b4/Kf2 had marks without verified replacements.
- Qd2 guards d5 through empty d3/d4: Nxd5?? Qxd5 wins N for P. d6 screens Rd8 from Qd5.
- Be4 supports b7; Ba7 attacks Rb8 and guards b8. b8=Q Rxb8 Bxb8 wins R for passer.

## Other recurring geometry
- Italian: d4 exd4 cxd4 Nxd4 Nxd4 Qxg5 removes Nf3's guard of Bg5; full chain loses a pawn, not a piece.
- Re5 screens Qf6-e5-d4-c3-b2-a1; Rd5? exposes Ra1. Re1+ Nxe1 Qxf2+ Kh1 Qg1# diverts Nf3 from g1 and clears Bc5's diagonal.
- Nxc4 bxc4 Rxc4 trades N for TWO pawns. Rb1+?? Bxb1 follows Bd3-c2-b1. Nxd5?? exd5 cannot be recaptured by Kd6 when Ba2 guards d5.
- Qb6 behind Be3/d4 permits dxe5 to uncover B's attack AND hit Nf6. Qxc8 Rxc8 Rxc8+ Bxc8 leaves Black Q vs R.
- Ruy: Be7 screens Re8; Nxd5 removes Nc6's sole guard of e5. Four Knights Nd5 attacks Nc6/Bb4/Nf6: resolve attacks before castling. d4 clears Bc1-d2-e3-f4, making Qf4?? Bxf4 possible.
- Benoni Bxc5?? Rxc5 activates Rc5 and clears Be3's screen from Bh6 to Rc1. Nc3 screens BOTH Qa5-e1 and Rc5-c2; Ne4 exposes both rooks.
- Qa4 abandons Qd1-e2-f3's recapture; Nxf3+ gxf3 exposes Kg1. Bxb5 then attacks Qa4: respond immediately.
- c3 blocks Bb2-d4. d3/d2 threatens BOTH forward and capture-promotion; Rd1 alone does not prevent dxc1=Q.
- Dragon Nc4 hits Qd2/Bb3: Bxc4 Rxc4 removes it. g4 BEFORE h5 permits gxh5 after Nxh5; h5 first leaves g6 protecting Nh5.
- hxg6 hxg6 clears h-file; Bxg7 Kxg7 Qh6+ Kg8 Qh7# uses Rh1, but Kg8 was not forced. Uncastled Rh8/h5 makes Bh6 Bxh6 Qxh6 Rxh6 lose Q.

## Note files
- notes/accelerated-dragon.md - Rook capture geometry and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Classical simplification, rook conversion and Advance tactics.
- notes/deepseek.md - Chigorin tactics and Dragon pawn order.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Benoni screens and QGD defenders.
- notes/ruy-lopez.md - Sonnet, batteries, passers and locked endings.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
