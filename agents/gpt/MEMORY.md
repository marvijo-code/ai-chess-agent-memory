# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. Every alternative needs its own forcing scan: avoiding Rxe5's fork did not make Bxd5?? Nd3+ safe. Repeated ...f6/...Qd6?? exd6 shows recognition alone fails.
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before every Q/R move, scan pawn diagonals, knights and COMPLETE sliding rays, including horizontal rooks. ...Qxf2? allowed Rd2xf2 through e2; f7 blocked Rf8. Ra2?? allowed b3xa2.
- Test Kxchecker first and name its actual defender. ...Qh2+?? Kxh2 and Rh7+?? Kxh7 lost unguarded heavy pieces. An attacking purpose never establishes safety.
- Name exact defenders, screens and LEGAL surviving recapturers. Own Be3 blocked Re1-e4. Queen-only defense fails to Qx Qx Rx. Count rear attackers and the entire exchange.
- Refresh pins after endpoints move. ...Nd4?? Nxd4 cxd4 Rxd8+ exposed Qd8. Kb1 released Rd2; Kg2 created Ra2's pin of Nd2, Kf1 released it. A pinned rook can capture its pinning queen.
- Before moving a screen/guard, trace EVERY exposed ray. ...f6 abandoned Be6 and exf6 cleared Qe2-e6. Ne4 cleared Ra2-e2; Ba6 guarded e2 through b5/c4/d3. Attacking Bc3 did not save Re2.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N. Bxd5?? Nd3+ preceded ...Qxd5; ...Nf2+ forked Kh1/Qd1. Attacking a queen does not suppress checks.
- Queenless still requires a mate scan: Be4 supported Rxg2+/Rh1#; Rxe7 ignored mate. Rxf5 ignored ...Rxd1#. Luft solves only the mate its flight prevents.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3. Extra thinking never replaces a capture scan.
- Name a target/break before shuffling. When worse use 3-10 seconds for verified replies. T28 Ne4/Nxc3/d5 took 54/56/57 seconds in a lost position; winning Qe6 took 53 unnecessarily.
- Track TOTAL material after trades. A local recovery does not erase a queen loss. T28 ...Qxc1 Bxc1 ...Rxc1 Qxc1 exchanged Q+R for R+B: queen for bishop, not an equal liquidation.
- Ahead: remove counterplay, simplify safely and preserve mating material. T28 Rc1 traded Black's last rook; minor exchanges left Q versus B. Then an outside a-passer forced promotion.
- Queen trades need an endgame audit: material, opened files, passers and entry squares. Qxb5 axb5 opened Ra8-a2 and left Black an extra pawn. Queenless did not mean safe.
- Worse: seek safe activity/repetition. Depth-6 SF repeated even with Q+R versus bare K; earlier +8/+9 escapes also occurred. Practical chance, never fortress evidence or proof of a sacrifice.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1: Qd1?? cxd1=Q+. Audit blockader pins and escorts after every move; ...Rf8 Rxf8+ Nxf8 b8=Q removed a pinned blockader.
- Mate conversion: cut off K, approach with K, preserve pawn tempi and test stalemate. Two queens: verify checking queen support and every flight; Qe6 protected Qg8 and covered h6 in T28.

## White openings
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N. ...Qc7/f4: e5 screens Qc7-f4, so ...Nxf4?? Bxf4.
- Chigorin: Nf1 restores Qd1-d4. Against ...a4/Nc5, Qd1 guards b3 through c2; Qf3 abandons it to ...Nb3 against Ra1/Bd2. Resolve queenside threats before storming.
- T28 Sonnet: Nf1/Ng3/Be3/Rc1, d5 Nb4 Bb1 uncovered Rc1's attack on Qc7. ...Qxc1? Bxc1 Rxc1 Qxc1 won Q for B. Calculate asymmetry; no forced opening advantage established.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by ...g6. Nbd2 blocks Qd1-d4; Be3 blocks Re1-e4. Before g3/h4 calculate ...f5/...fxe4 and queen routes to h4.
- Ruy ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5. Bxd5?? Nd3+! exposes K; Rxe5 needs ...Qf6+ calculation. No verified move-12 replacement. Qg6/Nf5 versus Kg8/Qf7/Nh7: search Nh6+ before trading Q.

## Black openings
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse; later gifts do not certify the break. Long-castling ...Nxe5/dxe5/Nd5 also lacked validation.
- SF Ruy 6.d4: exd4/Re1 O-O/e5 Nd5/Nxd4 Nxd4/Qxd4 Nb6/Nc3 Nxa4/Qxa4 d6/exd6 Bxd6/Bf4 Be6 near equal. Rad1 Qf6/Bxd6 cxd6!; Qe7 lost d6.
- Chigorin ...Qb6?? dxe5! uncovers Be3-b6. Open Ruy ...Ne6?! Qxd8 Rxd8 Bxb5 left a pawn deficit. Berlin queens-on: ...Nxe4/d4 Nd6/Bxc6 dxc6/dxe5 Nf5/Qe2 Be7?! Rd1!; solve the open d-file before development.
- Advance Caro: repeated ...f6? Nf4!/...Qd6?? exd6 loses Q. Against Sonnet, ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; this does not validate ...cxd4/Nxd4 or queenless ...f6/Rxf6/Ne5.
- QGD cxd4 exd4/dxc4 Bxc4 creates an IQP. Qe2 abandons d4: ...Nxd4 Nxd4 Bxd4 wins P; Nc3 does NOT attack d4. Bb7 supports h1 once d5/g2 clear.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro and intermezzos.
- notes/four-knights.md - Double attacks and screens.
- notes/qgd-exchange.md - IQP and mating diagonals.
- notes/ruy-lopez.md - C-file liquidation, guards and conversion.
- notes/sicilian-maroczy.md - Recaptures and promotions.
