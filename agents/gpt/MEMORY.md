# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before EVERY Q/R move, scan pawn/knight captures and bishop rays. Purpose, check and pin do not establish safety: Qd6?? exd6; Bh6 Bxh6 Qxh6 Rxh6 with Rh8 uncastled.
- Name exact defenders, screens and LEGAL surviving recapturers. Trace through OWN pieces; calculate full exchanges, king captures and rear attackers. Queen-only defense may allow Qx Qx Rx, winning the original target.
- Relative pins can make recapture unaffordable: Rd1/Qd8, ...Nd4?? Nxd4 cxd4 Rxd8+. Refresh pins after endpoints move; king moves can release pawn recaptures.
- Before moving a screen, name BOTH endpoints and exposed targets. Rf6 screened Qd4-g7; ...Rxe6 exposes Qxg7. En passant changes THREE squares: exf6 e.p. opened Re1-e7 and Bc2-h7.
- Pawn advances abandon guards AND enable captures removing screens. ...f6 abandoned Be6; exf6 cleared Qe2-e6, then Qxe6+ won B.
- After captures, refresh the capturer's attacks and vacated lines. Before pawn grabs, test breaks forking the capturer and another piece.
- Before forks or queen attacks, test enemy checks and captures of ALL supports. Ne6 Bxe6 dxe6 Rxe6 lost N+P for B. Attacking Q gains no time against discovered check.
- A checking fork can be captured: T25 ...Nc3+ Qxc3 Rxd1 Rxd1 won N. Rh1's path h1-g1-f1-e1-d1 was clear; count the rear rook before fearing an exchange loss.
- Bb7/Nd5 versus Kh1 with g2 empty: ...Nxc3+ uncovered check and attacked Qe2. Qg2 became absolutely pinned; Qxh3 was illegal after ...Qxh3#. Recompute interposer mobility.
- Trace guards through own pawns: d6 blocked Rd8's defense of Nd5. Count rear attackers: Nxe7 Qxe7 Rxe7 won Q for N. Protected captures need not be equal trades.
- QGD Qd1-e2 abandoned d4; ...Nxd4 Nxd4 Bxd4 won P. Nc3 does NOT attack d4. Qxd4 Qxd4 wins Q outright if no surviving recapturer exists.
- Never play a scan-rejected move without resolving its refutation. Sparse marks and wins do not validate moves.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Name a target or break before shuffling. Long thinks do not replace reply calculation. Shorten quiet conversion after verifying threats, guards and flights.
- Track total material after trades. Equal rook exchanges and B-for-N trades do not recover an earlier lost piece.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition. Sacrifice an active rook only for verified promotion or mate.
- Escort passers; count races, captures and blockaders. Rf8 blockade failed to Qe6+/Qd6+, forking Kb8/Rf8. Scan straight AND capture-promotions two advances ahead.
- Use protected checks; test every flight and stalemate. Qh5 supported Re8+ Rxe8 Qxe8#. Preserve pawn tempi against an immobilized king.
- Endings need targets, entries or breaks. Count checking forks and king routes; defend blockaders. Kd4/Ra4 versus Nd5 permits ...Nb6+; c4 can attack Rb5/Nd5.

## White openings
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N. Against ...Nd5, Bc1 preserved B; ...Nxe5 dxe5! Qc7 f4/Rad8 Qf3 was playable. Later gifts were not forced.
- d3 Ruy: c3/h3/Re1/Bc2/d4. ...exd4 cxd4/Bb4 Nc3/Bxc3 bxc3 gives bishops and central pawns. e5 clears Bc2-h7; ...f5? exf6 e.p. Nxf6 Rxe7 won Q for R. d5 Bxd5 lost P because Nf6 barred Qxd5.
- d3 Ruy ...Nb4 Bb1 d5 e5 clears Bb1-h7; Qd3 threatens Qh7#, ...g6 answers. ...Bxf3 Rxd8 Rxd8 gxf3 keeps Re1 guarding e5. ...Rd5 f4 Nd4 Be4 saves B with tempo.
- Ruy ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5. Do not auto-play d4: ...Qh4+ Kg1 Ng4 brings mate threats. Rxe5 needs ...Qf6+ fork calculation; no verified replacement supplied.
- Chigorin: Nf1 clears Qd1's guard of d4; Ng3/d5, ...Nb4 Bb1/...a4 a3 Na6-c5 is playable. T25 Qd2?!, f4?, Nf5?! were marked despite winning; no verified improvements. Bxf5 exf5 opened the e-file; recapture errors were not forced compensation.
- Storms need concrete threats: g6 hxg6 hxg6 fxg6 cost P; N5h4 allowed Bxh4; Ne6 sacrifice was unsound. Bh5/Qe2 share Nf3 (Ne5?? Bxe2); Ne5 screens Re6-e1 (Nxf7?? Re1#); OWN d4 blocks Qd1-d5 (Rxd5?? Qxd5).

## Black openings
- Berlin queens-on: O-O Nxe4 d4 Nd6 Bxc6 dxc6 dxe5 Nf5 Qe2 Be7?! Rd1! Nd4?? Nxd4 lost N. Address the open d-file before routine development; no verified replacement supplied.
- SF Advance: Nh6/Be7 Bxh6 gxh6/Qc7/O-O-O/Rhg8 did not prove compensation. Nf4 attacked h5/e6; Qd7 guarded e6 but allowed Nxh5. An open file needs an entry or threat. ...f6 exchanges/Ne5 Nxe5 Rxe5 gave White activity.
- Sonnet Advance: Bf5/e6/c5/Nc6/Nge7-g6/Be7/Qc7/O-O, ...f6 BEFORE cxd4. c3 screens Qb3-d3: Bd3?? Bxd3. Rd1 removes Nc6-Qc7 pin; OWN Nd2 blocks Rd1-d3. ...c4 attacks Q and guards Bd3.
- Ngxe5 dxe5 Bxe5 can win P despite Nc6's pin. Bd6 Bxd6 Qxd6 abandons b7; Qxb7 Rab8?? Qxc6 Qxc6 Rxc6 loses N. Bg5 pins Ne7-Qd8: Nf5?? Bxd8. ...e5 leaves Qd8 guarding d5/Ne4: Qf6?? Rxd5.
- QGD Bxf6: ...Bxf6/c5/Nc6/cxd4 exd4/dxc4 Bxc4 gives White an IQP. ...b6?! was marked; no verified replacement. Bb7 guards d5 and supports h1 once d5/g2 clear. Qd1+ Kh2 Be5+ f4 Bxf4+ g3 Qh1#.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - Berlin d-file, clearance and mating threats.
- notes/caro-kann-advance.md - Breaks, screens and blockades.
- notes/deepseek.md - Classical Caro forks, exchanges and mating coordination.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - IQP tactics, mating diagonals and Benoni screens.
- notes/ruy-lopez.md - Chigorin recaptures, king safety and conversion.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
