# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. Every candidate needs its own forcing scan; rejecting one blunder does not validate another. Repeated ...f6/...Qd6?? exd6 shows recognition alone fails.
- Start with the enemy's last move: changed attacks, pawn controls, opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- PAWN DIAGONALS FIRST, then knights and complete sliding rays. Rb3?? a4xb3, Qe4?? d5xe4 and Qd5?? e6xd5: defending or attacking another piece never makes a heavy-piece destination safe.
- Test Kxchecker first and name its actual defender. ...Qh2+?? Kxh2, Rh7+?? Kxh7 and ...Qxb2+?? Kxb2 lost heavy pieces. Check does not establish safety.
- Name exact defenders, screens and LEGAL recapturers. Nd2 blocked Be3-c1, Rc1's sole guard. Be3 blocks Re1-e4; f7 blocks Rf8-f2; Qe3 cannot recapture c2. Audit friendly rays newly blocked as well as enemy rays opened.
- Count duties AFTER the last recapture. Re2?? Rxe2 Nxe2 removed BOTH e4 guards, Re1 and Ng3; ...Nxe4 won P. A locally equal trade can lose material elsewhere.
- Refresh pins when endpoints move. ...Nd4?? Nxd4 cxd4 Rxd8+ exposed Qd8. Kb1 released Rd2; Kg2 pinned Nd2 to Ra2, Kf1 released it. A pinned rook can capture its pinning queen.
- Before moving a guard/screen, trace lost guards and exposed rays. ...f6/exf6 exposed Be6 to Qe2; f2-f3 abandoned Be3. Ne4 opened Ra2-e2 with Ba6 guarding e2.
- Before forks/trades, test captures and checking intermezzos. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5?? Nd3+ preceded ...Qxd5. An attacked queen can capture its attacker; a capturer does not guard its own square.
- MATE FIRST, including quiet threats and queenless positions. ...Nxf4 attacked Qh5 but allowed Qxh7#; Rxe7 ignored ...Rh1#. Luft solves only the mate its flight prevents.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3. Long thinking never replaces a capture scan.
- Name a target/break before shuffling. T29 Re2/Rb4/Rb3 took 36/54/28 seconds yet missed guards and pawn captures. Verified conversions need 3-10 seconds, not 30-50.
- Track TOTAL material through the last recapture and the actual reply. Qxc1 Bxc1 Rxc1 Qxc1 costs Q+R for R+B. Ne2+ Nxc1 Rxc1 wins the exchange. ...Nxe4 taking B is not a trade until Qxe4 occurs; f3 instead leaves the captured bishop lost.
- Ahead: remove counterplay, simplify safely, preserve mating material. Check pawn guards and entry squares before queen trades. Worse: safe activity/repetition; later gifts do not validate earlier errors.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1. Ba1 Rc1+ Kh2 Rxa1 removes a blockader. ...Rf8 Rxf8+ Nxf8 b8=Q removes a pinned blockader.
- Verify mate support, all flights and stalemate. e5 clears Bb1-h7; ...Nf6xd5 can abandon h7. Qf2 supports Rd1# vs Kh1. Qg3/Ne4 supports Qxg3+ then Nf2#; Qg3 covers g1/g2/h2. SF repetition with Q+R vs bare K proves no fortress.

## White openings
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N; e5 screens Qc7-f4 against ...Nxf4.
- Caro ...Nd5 Bd2 ...Nc7 Qe4; ...Bf6? exf6 Qxf6 Bc3 attacks Q and clears d2. ...Qxf2 Be1 guards Ng3 through f2; ...Qb6 Rd7 invades. No forced opening edge established.
- Chigorin: Nf1 restores Qd1-d4; Qf3 abandons b3 to ...Nb3. Rc1/Bb1's queen trap needs actual c-file geometry; ...Qb7 avoids it. ...Rac8/d5 Nb4/Bb1 a5/a3 Nc2 forced Bxc2 Qxc2 Qxc2 Rxc2: equal material, active enemy rook.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by ...g6. Nbd2 blocks Qd1-d4; Be3 blocks Re1-e4. Before g3/h4 calculate ...f5/...fxe4 and Qh4 routes.
- Ruy ...Bg4/Qe2/Nc6: Nf3 pinned to Qe2. h3?! Nd4 hits Qe2/Bb3/Nf3. Qe3 Bxf3: Qxf3 loses Q to Nd4. ...c4 Bc2? Nxc2 forks Qe3/Ra1/Re1. No verified replacements.
- Ruy ...Ba7/Bg4 Bxf3 Qxf3/exd4: e5?! Nxe5 gains tempo; d6 guards Ne5. cxd4?! Ba7xd4 through b6/c5. ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5; Bxd5?? Nd3+. Rxe5 needs ...Qf6+ calculation.

## Black openings
- Classical Caro: ...h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O. Against O-O/c4/Rfe1, ...c5? d5! was adverse; gifts do not certify it. Long-castling ...Nxe5/dxe5/Nd5 also lacked validation.
- SF Ruy 6.d4: exd4/Re1 O-O/e5 Nd5/Nxd4 Nxd4/Qxd4 Nb6/Nc3 Nxa4/Qxa4 d6/exd6 Bxd6/Bf4 Be6 near equal. Rad1 Qf6/Bxd6 cxd6!; Qe7 lost d6.
- Chigorin ...Qb6?? dxe5 uncovers Be3-b6. Open Ruy ...Ne6?! Qxd8 Rxd8 Bxb5 lost P. Berlin queens-on ...Be7?! Rd1: solve the open d-file before development.
- Advance Caro: ...f6? Nf4!/...Qd6?? exd6 repeatedly loses Q. Earlier ...f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3; it validates neither later exchanges nor queenless ...f6/Rxf6/Ne5.
- QGD: recount d4's guards. Qe2 displaced Qd1; ...Bxf3 Qxf3 removed Nf3 AND displaced Qd1, allowing ...Nxd4 with tempo. Nc3 does NOT attack d4. ...Bg4/Bh5 were inaccurate. T29 third place: 15.Ne5?? Rac8? missed punishment; 16.Nd7?? Nxd7 won N. No verified move-15 replacement. Develop with a tactical scan.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - D-file and clearance.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Classical Caro and conversion.
- notes/four-knights.md - Double attacks and screens.
- notes/qgd-exchange.md - Central guards and mating lines.
- notes/ruy-lopez.md - Exchange duties and king nets.
- notes/sicilian-maroczy.md - Recaptures and promotions.
