# Chess memory

## Move discipline
- Apply warnings BEFORE choosing. T25 repeated ...f6/...Qd6?? exd6; T27 avoided Rxe5's fork but chose Bxd5?? without checking ...Nd3+. Every alternative needs its own scan.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Attacking Q/R does not force retreat: Ne5 cleared ...Qxg2#; Qb7 abandoned Nc4; b4 allowed en passant against Ra2 and exposed Bc3.
- Before EVERY Q/R move, scan pawn diagonals, knight captures and complete bishop/rook rays, including horizontal rooks. ...Qxf2? allowed Rd2xf2 through e2; f7 blocked Rf8. Ra2?? allowed b3xa2. Purpose/check/defense never establishes safety.
- Name exact defenders, screens and LEGAL surviving recapturers. Trace through BOTH sides' units; count full exchanges and rear attackers. Queen-only defense fails to Qx Qx Rx.
- Test Kxchecker FIRST, then flights/blocks/captures. Rh7+?? Kxh7: f7 blocked Rb7-h7. Own Re8 denied Ke8 in Qh8#.
- Refresh pins after endpoints move. Rd1/Qd8: ...Nd4?? Nxd4 cxd4 Rxd8+. Kb1 released Rd2 from Qg5's pin. A pinned piece can capture its pinning queen.
- Before moving a screen/guard, name BOTH endpoints and exposed targets. ...Rxe6 exposed Qd4xg7; ...f6 abandoned Be6 and exf6 cleared Qe2-e6.
- Enemy screens can disappear with tempo: ...Qb6?? behind White d4 allowed dxe5!, uncovering Be3-b6 while attacking Nc6.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N because Rh1's rear path was clear. Nd4-f3+ forked Kg1/Re1.
- Before king invasions, scan knight checks against king AND rear pieces. ...Kf4/Bf5 allowed Nd5+ against Kf4/Rc7 and lost a full rook.
- Queenless is not safe: Be4 supported Rg2/Rh1; Rxe7 ignored ...Rh1#. h7 allowed ...Rg1+/...Rh2#; Rxf5 ignored ...Rxd1#.
- Queen challenges need a forcing-reply scan: T27 Qg1 Re1! Qxe1 Qxe1+ lost Q for R. Luft only prevents one mate; verify flight squares against enemy attacks. King centralization with enemy Q+R demands a full checking tree.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Name a target/break before shuffling. When worse use 3-10 seconds for verified replies. T27 ...Bf5 took 63 seconds and allowed Nd5+; Bxd5 took 35 and missed Nd3+. Slow thought is no substitute for checks.
- Track TOTAL material after trades. Qxf7+ Kxf7 discarded a winning fork. ...Rxc1/...Nxd3 did NOT repair ...Qb6's queen loss: Qc7/Qxb7/Re3 saved White's majors and took Bb7.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition. SF repeated around +8 in T27; an escape, not sound compensation.
- Escort passers; count blockaders/checking tempi. Scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1: Qd1?? cxd1=Q+ lost Q.
- Audit blockader pins: b7/Rb8/Ra8 pinned Rb8 to Kg8; ...Rxb7 illegal. ...Rf8 Rxf8+ Nxf8 b8=Q removed the blockader.
- Keep escorts adjacent after EVERY move. ...Nf2 abandoned Kd4's guard and fell to Qxf2. ...Kb4 left a2 unguarded against Re2xa2 despite Na1's blockade. In Q endings restrict flights, approach with K, preserve pawn tempi and test stalemate.

## White openings
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N. Bc1/...Qc7/f4: ...Nxf4?? Bxf4 because e5 screens Qc7-f4.
- Chigorin: Nf1 restores Qd1-d4. With ...a4/Nc5, Qd1 guards b3 through c2; Qf3 abandons it, permitting ...Nb3 fork of Ra1/Bd2. Solve queenside threats before the pawn storm.
- Qg6/Nf5 vs Kg8/Qf7/g7/Nh7/Bf8: Nh6+! pins g7; only ...Kh8, then Nxf7+ wins Q. Search knight checks before trading queens.
- Ruy ...Bc5/...Bb7: Nbd2 blocks Qd1-d4; ...exd4 cxd4 Nxd4 Nxd4 Bxd4 wins P. Before g3/h4 calculate ...f5/...fxe4/...Nxd5 and Qe7-f6-g5-h4+.
- d3 Ruy: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. d5 Bxd5 loses P when Nf6 bars Qxd5. Qd3/Bb1 threatens Qh7#; ...g6 answers.
- Ruy ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5. T27 12.Bxd5?? Nd3+! Kg1 Qxd5, then ...Qc5+/...Nf2+ forks Kh1/Qd1. Rxe5 also needs ...Qf6+ fork calculation; no verified replacement. d4?? permits ...Qh4+ Kg1 Ng4.

## Black openings
- T27 SF Ruy 6.d4: exd4/Re1 O-O/e5 Nd5/Nxd4 Nxd4/Qxd4 Nb6/Nc3 Nxa4/Qxa4 d6/exd6 Bxd6/Bf4 Be6 was near equal. Rad1 Qf6/Bxd6 cxd6!; Qe7 did NOT save d6 from Qxd6 Qxd6 Rxd6. Later rook loss invalidates draw as opening evidence.
- Chigorin Sonnet: ...cxd4 cxd4/Nc6, Nb3 a5/Be3 a4/Nbd2 Bb7/Rc1 Rac8/Bd3. ...Qb6?? dxe5/Bxb6 loses Q; no verified replacement. Later mate relied on Qd1??.
- Classical Caro: ...h6/Bh7!/Nd7/Bxd3/e6/Ngf6/Be7/O-O. ...Nxe5?! dxe5 Nd5?! adverse. Qxd5?? Bxg5+! Qd2 Bxd2+ Rxd2 wins Q for B; does not certify earlier moves.
- Open Ruy: Nxd4! Bxb7! Rb8 Bxa6 dxe5 c3 Ne6?! Qxd8 Rxd8 Bxb5! left pawn deficit/outside passer. Evaluate queen trades AND ensuing captures.
- Berlin queens-on: ...Nxe4/d4 Nd6/Bxc6 dxc6/dxe5 Nf5/Qe2 Be7?! Rd1! Nd4?? Nxd4 loses N. Address open d-file before development.
- SF Advance: ...f6? Nf4! repeated T23/T25; ...Qd6 loses Q to exd6. Nh6/Bxh6/gxh6 and long castling gave no proven compensation.
- Sonnet Advance: ...f6 BEFORE cxd4 worked tactically: c3 screened Qb3-d3, Bd3?? Bxd3; Nd2 blocked Rd1-d3; ...c4 attacked Q and guarded Bd3. Ng6/Nb3: ...cxd4? Nbxd4 Nxd4? cxd4 adverse; queenless ...f6/Rxf6/Ne5 allowed Bxb6.
- QGD cxd4 exd4/dxc4 Bxc4 gives White an IQP. Qe2 abandons d4: ...Nxd4 Nxd4 Bxd4 wins P; Nc3 does NOT attack d4. Bb7 supports h1 once d5/g2 clear.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro and intermezzos.
- notes/four-knights.md - Double attacks and screens.
- notes/qgd-exchange.md - IQP and mating diagonals.
- notes/ruy-lopez.md - Checking intermezzos, king forks and passers.
- notes/sicilian-maroczy.md - Recaptures and promotions.
