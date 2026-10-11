# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. Each alternative needs its own scan: T27 avoided Rxe5's fork but chose Bxd5?? Nd3+. T25 repeated ...f6/...Qd6?? exd6.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before EVERY Q/R move, scan pawn diagonals, knight captures and complete bishop/rook rays, including horizontal rooks. ...Qxf2? allowed Rd2xf2 through e2; f7 blocked Rf8. Ra2?? allowed b3xa2.
- Test Kxchecker FIRST. T28 ...Qh2+?? Kxh2 lost Q: neither Rf5, Bg7 nor Nf6 guarded h2. T26 Rh7+?? Kxh7: f7 blocked Rb7-h7. A check or attacking purpose never establishes safety.
- Name exact defenders, screens and LEGAL surviving recapturers. Trace through BOTH sides' units and count the full exchange, including rear attackers. Queen-only defense fails to Qx Qx Rx.
- Refresh pins after endpoints move. Rd1/Qd8: ...Nd4?? Nxd4 cxd4 Rxd8+. Kb1 released Rd2 from Qg5's pin. A pinned piece can capture its pinning queen.
- Before moving a screen/guard, name exposed targets. ...Rxe6 exposed Qd4xg7; ...f6 abandoned Be6 and exf6 cleared Qe2-e6. ...Qb6?? behind d4 allowed dxe5!, uncovering Be3-b6 with tempo on Nc6.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N because Rh1's rear path was clear. Bxd5?? Nd3+ preceded ...Qxd5; later ...Nf2+ forked Kh1/Qd1.
- An attack does not force retreat: Ne5 cleared ...Qxg2#; Nf5 fell to ...exf5 or ...Rxf5. Before king invasions scan knight checks against king AND rear pieces: ...Kf4/Bf5 allowed Nd5+ and lost Rc7.
- Queenless is not safe: Be4 supported Rxg2+/Rh1#; Rxe7 ignored mate. Rxf5 ignored ...Rxd1#. Queen challenges also need a forcing scan: Qg1 Re1! Qxe1 Qxe1+ lost Q for R. Luft solves only the mate its flight actually prevents.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Name a target/break before shuffling. When worse use 3-10 seconds for verified replies. T28 Qh2 took 53 seconds and still missed Kxh2; long thought is no substitute for the capture scan.
- Track TOTAL material after trades. Qxf7+ Kxf7 discarded a winning fork. ...Rxc1/...Nxd3 did not repair ...Qb6's queen loss; White saved its majors and took Bb7.
- Ahead: remove counterplay, simplify safely, preserve mating material. T28 Bf8/Bxg7 stopped the g-passer; ...Ne4 guarded Rf2 before ...Rxf1+ traded White's last rook. After the queen blunder, 2R+B+N versus R still won; recount and reset the plan.
- Worse or Black with draw odds: seek activity/repetition. SF repeated around +8 in T27; practical escape, not sound compensation.
- Escort passers; count blockaders/checking tempi. Scan straight AND capture-promotions two advances ahead: c2 attacks b1/d1, so Qd1?? cxd1=Q+ loses Q.
- Audit blockader pins: b7/Rb8/Ra8 pinned Rb8 to Kg8; ...Rxb7 illegal. ...Rf8 Rxf8+ Nxf8 b8=Q removed it. Keep escorts after EVERY move: ...Nf2 abandoned Kd4; ...Kb4 abandoned a2 to Re2xa2.
- Mate conversion: cut off the king, approach with K, preserve pawn tempi, test stalemate. T28 Nc2 guarded e1 and cleared Bd4-g1; Kg3 supported Rh2# against Kh1.

## White openings
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N. Bc1/...Qc7/f4: ...Nxf4?? Bxf4; e5 screens Qc7-f4.
- Chigorin: Nf1 restores Qd1-d4. With ...a4/Nc5, Qd1 guards b3 through c2; Qf3 abandons it, permitting ...Nb3 against Ra1/Bd2. Resolve queenside threats before storming.
- Qg6/Nf5 vs Kg8/Qf7/g7/Nh7/Bf8: Nh6+! pins g7; ...Kh8 Nxf7+ wins Q. Search knight checks before trading queens.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#; ...g6 answers. Nbd2 blocks Qd1-d4; count ...exd4 exchanges. Before g3/h4 calculate ...f5/...fxe4 and Qe7-f6-g5-h4+.
- Ruy ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5. Bxd5?? Nd3+! Kg1 Qxd5 exposes K; Rxe5 needs ...Qf6+ calculation. No verified move-12 replacement. d4?? permits ...Qh4+ Kg1 Ng4.

## Black openings
- Classical Caro: ...h6/Bh7!/Nd7/Bxd3/e6/Ngf6/Be7/O-O. T28 White O-O/c4/Rfe1: 14...c5? 15.d5! exd5 16.cxd5? Re8; no verified improvement supplied. Bxh6?? gxh6! Qg6+ fxg6 won B+Q for pawns; later gifts do not certify ...c5.
- Classical long-castling branch: ...Nxe5?! dxe5 Nd5?! adverse. Qxd5?? Bxg5+ Qd2 Bxd2+ Rxd2 wins Q for B; checking intermezzo, not proof of sound earlier play.
- SF Ruy 6.d4: exd4/Re1 O-O/e5 Nd5/Nxd4 Nxd4/Qxd4 Nb6/Nc3 Nxa4/Qxa4 d6/exd6 Bxd6/Bf4 Be6 near equal. Rad1 Qf6/Bxd6 cxd6!; Qe7 lost d6 to Qxd6 Qxd6 Rxd6.
- Chigorin: ...Qb6?? dxe5/Bxb6 loses Q. Open Ruy: Nxd4! Bxb7! Rb8 Bxa6 dxe5 c3 Ne6?! Qxd8 Rxd8 Bxb5! left pawn deficit. Evaluate queen trades and ensuing captures.
- Berlin queens-on: ...Nxe4/d4 Nd6/Bxc6 dxc6/dxe5 Nf5/Qe2 Be7?! Rd1! Nd4?? Nxd4 loses N. Solve the open d-file before routine development.
- SF Advance: ...f6? Nf4! repeated T23/T25; ...Qd6 loses Q to exd6. Nh6/Bxh6/gxh6 and long castling gave no proven compensation.
- Sonnet Advance: ...f6 BEFORE cxd4 worked tactically with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3. Ng6/Nb3: ...cxd4? Nbxd4 Nxd4? adverse; queenless ...f6/Rxf6/Ne5 allowed Bxb6.
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
