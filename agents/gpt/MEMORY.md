# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing; every alternative needs its own scan. Avoiding Rxe5's fork did not make Bxd5?? Nd3+ safe. Repeated ...f6/...Qd6?? exd6 proves recognition alone fails.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before EVERY Q/R move, scan pawn diagonals, knights and complete bishop/rook rays, including horizontal rooks. ...Qxf2? allowed Rd2xf2 through e2; f7 blocked Rf8. Ra2?? allowed b3xa2.
- Test Kxchecker FIRST. ...Qh2+?? Kxh2: no defender guarded h2. Rh7+?? Kxh7: f7 blocked Rb7-h7. An attacking purpose never establishes safety.
- Name exact defenders, screens and LEGAL surviving recapturers; count the full exchange including rear attackers. Own Be3 blocked Re1-e4 in T28. Queen-only defense fails to Qx Qx Rx.
- Refresh pins after endpoints move. ...Nd4?? Nxd4 cxd4 Rxd8+ exposed Qd8. Kb1 released Rd2 from Qg5's pin. T28 Kg2 CREATED Ra2's pin of Nd2; Kf1 released it. A pinned rook can capture its pinning queen.
- Before moving a screen/guard, name exposed targets. ...Rxe6 exposed Qd4xg7; ...f6 abandoned Be6 and exf6 cleared Qe2-e6. ...Qb6?? dxe5! uncovered Be3-b6 with tempo.
- Check ALL opened rays. T28 Ne4 cleared Ra2-d2-e2, allowing ...Rxe2; Ba6 guarded e2 through b5/c4/d3. Attacking Bc3 did not save Re2.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N to the rear rook. Bxd5?? Nd3+ preceded ...Qxd5; ...Nf2+ then forked Kh1/Qd1.
- An attack does not force retreat: Ne5 cleared ...Qxg2#; Nf5 fell to ...exf5 or ...Rxf5. Before king invasions scan knight checks against king AND rear pieces: ...Kf4/Bf5 allowed Nd5+, losing Rc7.
- Queenless is not safe: Be4 supported Rxg2+/Rh1#; Rxe7 ignored mate. Rxf5 ignored ...Rxd1#. Qg1 Re1! Qxe1 Qxe1+ lost Q for R. Luft solves only the mate its flight prevents.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Name a target/break before shuffling. When worse use 3-10 seconds for verified replies. T28 Ne4/Nxc3/d5 took 54/56/57 seconds in a lost position; Qh2 in round 1 took 53 and still missed Kxh2.
- Track TOTAL material after trades. Qxf7+ Kxf7 discarded a winning fork. ...Rxc1/...Nxd3 did not repair a queen loss. T28 ...Rxe2/Nxc3/Rxe3+ cost a full rook overall.
- Ahead: remove counterplay, simplify safely, preserve mating material. After T28's queen gift, 2R+B+N versus R still won; recount and reset the plan.
- Worse: seek safe activity/repetition. Depth-6 SF repeated even with Q+R against bare K in T28; earlier +8/+9 escapes also occurred. Practical chance, never proof of a fortress or sound sacrifice.
- Queen trades require an endgame audit: material, opened rook files, passers and entry squares. T28 Qxb5 axb5 opened Ra8-a2 and left an extra black pawn; removing queens did not make the ending safe.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1: Qd1?? cxd1=Q+ loses Q.
- Audit blockader pins and escorts after EVERY move. b7/Rb8/Ra8 pinned Rb8 to Kg8; ...Rf8 Rxf8+ Nxf8 b8=Q removed it. ...Nf2 abandoned Kd4; ...Kb4 abandoned a2 to Re2xa2.
- Mate conversion: cut off K, approach with K, preserve pawn tempi, test stalemate. Nc2 guarded e1 and cleared Bd4-g1; Kg3 supported Rh2# against Kh1.

## White openings
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1, attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N. ...Qc7/f4: ...Nxf4?? Bxf4; e5 screens Qc7-f4.
- Chigorin: Nf1 restores Qd1-d4. With ...a4/Nc5, Qd1 guards b3 through c2; Qf3 abandons it, allowing ...Nb3 against Ra1/Bd2. Resolve queenside threats before storming.
- Qg6/Nf5 vs Kg8/Qf7/g7/Nh7/Bf8: Nh6+! Kh8 Nxf7+ wins Q; search knight checks before queen trades.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#; ...g6 answers. Nbd2 blocks Qd1-d4. Before g3/h4 calculate ...f5/...fxe4 and queen routes to h4.
- T28 d3/...Bc5: Be3 blocks Re1-e4; Bc2xa4 removes another e4 defender. Qb4?! exd4 cxd4 Nxe4! Nxe4 Bxe4! lost a central pawn. ...Qg6/Bb7 threatens g2, but g3?! weakened h3 to ...Qf5. No verified replacements supplied.
- Ruy ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5. Bxd5?? Nd3+! Kg1 Qxd5 exposes K; Rxe5 needs ...Qf6+ calculation. No verified move-12 replacement. d4?? permits ...Qh4+ Kg1 Ng4.

## Black openings
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse; later Bxh6?? gxh6 Qg6+ fxg6 gifts do not certify the break.
- Classical long-castling: ...Nxe5?! dxe5 Nd5?! adverse. Qxd5?? Bxg5+ Qd2 Bxd2+ Rxd2 wins Q for B; not proof of sound earlier play.
- SF Ruy 6.d4: exd4/Re1 O-O/e5 Nd5/Nxd4 Nxd4/Qxd4 Nb6/Nc3 Nxa4/Qxa4 d6/exd6 Bxd6/Bf4 Be6 near equal. Rad1 Qf6/Bxd6 cxd6!; Qe7 lost d6 to Qxd6 Qxd6 Rxd6.
- Chigorin ...Qb6?? dxe5/Bxb6 loses Q. Open Ruy ...Ne6?! Qxd8 Rxd8 Bxb5 left a pawn deficit; evaluate captures after queen trades.
- Berlin queens-on: ...Nxe4/d4 Nd6/Bxc6 dxc6/dxe5 Nf5/Qe2 Be7?! Rd1! Nd4?? Nxd4 loses N. Solve the open d-file before development.
- SF Advance: ...f6? Nf4! repeated; ...Qd6 loses Q to exd6. Nh6/Bxh6/gxh6 and long castling gave no proven compensation.
- Sonnet Advance: ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3. Ng6/Nb3: ...cxd4? Nbxd4 Nxd4? adverse; queenless ...f6/Rxf6/Ne5 allowed Bxb6.
- QGD cxd4 exd4/dxc4 Bxc4 gives White an IQP. Qe2 abandons d4: ...Nxd4 Nxd4 Bxd4 wins P; Nc3 does NOT attack d4. Bb7 supports h1 once d5/g2 clear.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro and intermezzos.
- notes/four-knights.md - Double attacks and screens.
- notes/qgd-exchange.md - IQP and mating diagonals.
- notes/ruy-lopez.md - Central guards, pins, intermezzos and repetition.
- notes/sicilian-maroczy.md - Recaptures and promotions.
