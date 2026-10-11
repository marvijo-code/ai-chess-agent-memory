# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. Every alternative needs its own forcing scan: avoiding Rxe5's fork did not make Bxd5?? Nd3+ safe. Repeated ...f6/...Qd6?? exd6 shows recognition alone fails.
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Sweep destinations for pawn diagonals, knights and COMPLETE sliding rays. Protection does not justify Q for N or B for P. T29 Qxb6?? Qd8xb6 lost Q for B through empty c7.
- Test Kxchecker first; name the actual defender. ...Qh2+?? Kxh2, Rh7+?? Kxh7 and ...Qxb2+?? Kxb2 lost unguarded heavy pieces. Check never establishes safety.
- Name exact defenders, screens and LEGAL surviving recapturers. Own Be3 blocked Re1-e4; f7 blocked Rf8-f2. T29 Qe3 CANNOT capture c2: it is a knight displacement, not a queen line.
- Refresh pins after endpoints move. ...Nd4?? Nxd4 cxd4 Rxd8+ exposed Qd8. Kb1 released Rd2; Kg2 pinned Nd2 to Ra2, Kf1 released it. A pinned rook can capture its pinning queen.
- Before moving a guard/screen, trace EVERY exposed ray and lost pawn guard. ...f6/exf6 exposed Be6 to Qe2. Ne4 opened Ra2-e2 with Ba6 guarding e2. f2-f3 removed Be3's guard before Re8xe3.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N. Bxd5?? Nd3+ preceded ...Qxd5; ...Nf2+ forked Kh1/Qd1. Attacking Q does not suppress checks.
- An attacked queen need not retreat if its attacker can be captured safely: Rb4xb8 removed the rook attacking Qe8 and supported Qh8#.
- Threats against a piece do not answer mate. T29 ...Nf4 supported Qg2# against Kf1; Nf5 uncovered Bh2's attack on Nf4 but gave Black the mating move. Queenless: Be4 supported Rxg2+/Rh1#; Rxe7 ignored mate. Luft solves only the mate its flight prevents.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3. Extra thinking never replaces a capture scan.
- Name a target/break before shuffling. Worse: 3-10 seconds for verified replies. T29 h3/Qe3/Qxb6 took 40/39/36 seconds; finished 11:29. Direct tactical failures, not clock shortage.
- Track TOTAL material after trades. Qxc1 Bxc1 Rxc1 Qxc1 exchanged Q+R for R+B: queen for bishop. Qg1 Nxg1 Rxg1 exchanges Q for N.
- Ahead: remove counterplay, simplify safely and preserve mating material. Shorten verified captures/exchanges; every exchange still needs a threat scan.
- Queen trades need an endgame audit: material, opened files, passers and entry squares. Qxb5 axb5 opened Ra8-a2 and left Black an extra pawn.
- Worse: seek safe activity/repetition. Depth-6 SF repeated even with Q+R versus bare K; practical chance, never fortress evidence or sacrifice justification.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. Audit blockader pins: ...Rf8 Rxf8+ Nxf8 b8=Q removed a pinned blockader.
- Mate conversion: cut off K, approach with K, preserve pawn tempi and test stalemate. Verify checking-piece support and every flight.

## White openings
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N. e5 screens Qc7-f4: ...Nxf4?? Bxf4.
- Caro ...Nd5 Bd2 ...Nc7 Qe4; ...Bf6? exf6 Qxf6 Bc3 attacks Q and clears d2. ...Qxf2 Be1 guards Ng3 through f2; ...Qb6 Rd7 invades. Geometry, not a forced opening edge.
- Chigorin: Nf1 restores Qd1-d4. Against ...a4/Nc5, Qd1 guards b3 through c2; Qf3 abandons it to ...Nb3 against Ra1/Bd2. Rc1 plus Bb1 can uncover an attack on Qc7.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by ...g6. Nbd2 blocks Qd1-d4; Be3 blocks Re1-e4. Before g3/h4 calculate ...f5/...fxe4 and queen routes to h4.
- T29 ...Bg4/Qe2/Nc6: Nf3 is pinned to Qe2. h3?! Nd4! attacks Qe2/Bb3/Nf3. Qe3 Bxf3 forces damaged shelter because Qxf3 loses Q to Nd4xf3. ...c4 Bc2? Nxc2 attacks Qe3/Ra1/Re1; Qe3 cannot recapture c2. No verified best replacements.
- T28 ...Ba7/Bg4 Bxf3 Qxf3/exd4: e5?! permits Nc6xe5 with tempo on Qf3; d6 guards Ne5. cxd4?! allows Ba7xd4 through b6/c5.
- Ruy ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5. Bxd5?? Nd3+ exposes K; Rxe5 needs ...Qf6+ calculation. No verified move-12 replacement. Qg6/Nf5 vs Kg8/Qf7/Nh7: search Nh6+ before trading Q.

## Black openings
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse; later gifts do not certify the break. Long-castling ...Nxe5/dxe5/Nd5 also lacked validation.
- SF Ruy 6.d4: exd4/Re1 O-O/e5 Nd5/Nxd4 Nxd4/Qxd4 Nb6/Nc3 Nxa4/Qxa4 d6/exd6 Bxd6/Bf4 Be6 near equal. Rad1 Qf6/Bxd6 cxd6!; Qe7 lost d6.
- Chigorin ...Qb6?? dxe5 uncovers Be3-b6. Open Ruy ...Ne6?! Qxd8 Rxd8 Bxb5 lost P. Berlin queens-on ...Be7?! Rd1!: solve the open d-file before development.
- Advance Caro: repeated ...f6? Nf4!/...Qd6?? exd6 loses Q. Earlier ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; it does not validate later exchanges or queenless ...f6/Rxf6/Ne5.
- QGD cxd4 exd4/dxc4 Bxc4 creates an IQP. Qe2 abandons d4: ...Nxd4 Nxd4 Bxd4 wins P; Nc3 does NOT attack d4. Bb7 supports h1 once d5/g2 clear.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro and conversion.
- notes/four-knights.md - Double attacks and screens.
- notes/qgd-exchange.md - IQP and mating diagonals.
- notes/ruy-lopez.md - Multiple attacks, recapture paths and king nets.
- notes/sicilian-maroczy.md - Recaptures and promotions.
