# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. T25 repeated T23's ...f6/...Qd6?? exd6. Never reuse a rejected move without resolving its refutation.
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Queen attacks do not force retreat. T26R2 Ne5 attacked Qc6 but cleared c6-d5-e4-f3-g2: ...Qxg2# with Bb7 support. Nf3 was a vital screen; Qe2 defending Nf3 did not replace its duty.
- Before EVERY Q/R move, scan pawn/knight captures and bishop rays. Qd6?? exd6; Bh6 Bxh6 Qxh6 Rxh6 with Rh8 uncastled. Check, pin and purpose do not establish safety.
- Name exact defenders, screens and LEGAL surviving recapturers. Trace through BOTH sides' pieces/pawns; calculate full exchanges and rear attackers. Queen-only defense can allow Qx Qx Rx, winning the target.
- Before claiming mate, test Kxchecker FIRST. T26R1 Rh7+?? Kxh7: f7 blocked Rb7-h7; Bd4 did not guard h7. Pins do not make blockers transparent. Sparse marks do not establish soundness.
- Refresh pins after endpoints move. Rd1/Qd8: ...Nd4?? Nxd4 cxd4 Rxd8+. A king move can release pawn recaptures; a pinned piece can capture its pinning queen.
- Before moving a screen, name BOTH endpoints and exposed targets. Rf6 screened Qd4-g7; ...Rxe6 exposes Qxg7. En passant changes THREE squares: exf6 e.p. opened Re1-e7 and Bc2-h7.
- Pawn advances abandon guards AND enable captures removing screens. ...f6 abandoned Be6; exf6 cleared Qe2-e6, then Qxe6+ won B.
- After captures, refresh the capturer's attacks and vacated lines. Before pawn grabs, test breaks forking the capturer and another piece.
- Before forks, test captures of ALL supports and checking replies. Ne6 Bxe6 dxe6 Rxe6 lost N+P for B. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N: Rh1's rear path was clear.
- Bb7/Nd5 versus Kh1 with g2 empty: ...Nxc3+ uncovered check and attacked Qe2. Qg2 became absolutely pinned; Qxh3 was illegal after ...Qxh3#.
- d6 blocked Rd8's defense of Nd5. Nxe7 Qxe7 Rxe7 won Q for N. ...Nd4 cxd4 cxd4 gives N for P; require verified compensation.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Name a target or break before shuffling. Long thinks do not replace reply calculation. Shorten quiet conversion after verifying threats, guards and flights.
- Track TOTAL material after trades. T26R2 lost d4; e5 dxe5 Nxe5 traded central pawns and left me ONE PAWN DOWN. Equal rook exchanges do not recover lost pieces.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition. Sacrifice an active rook only for verified promotion or mate.
- Escort passers; count races, captures and blockaders. Rf8 blockade failed to Qe6+/Qd6+, forking Kb8/Rf8. Scan straight AND capture-promotions two advances ahead.
- Use protected checks; test every flight and stalemate. Qh5 supported Re8+ Rxe8 Qxe8#. Preserve pawn tempi against an immobilized king.
- Endings need targets, entries or breaks. Kd4/Ra4 versus Nd5 permits ...Nb6+; c4 can attack Rb5/Nd5.

## White openings
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N. Against ...Nd5, Bc1/...Qc7/f4 supports e5; ...Nxf4?? Bxf4 wins N because e5 screens Qc7-f4.
- Ruy d3/...Bc5/...Bb6/...Bb7: with pawns d4/e4, Nbd2 blocks Qd1-d4. T26R2 ...exd4 cxd4 Nxd4 Nxd4 Bxd4 won d4: Bb6 supplies the second capture. Preserve sufficient recaptures BEFORE developing; no verified best replacement supplied.
- d3 Ruy: c3/h3/Re1/Bc2/d4. ...exd4 cxd4/Bb4 Nc3/Bxc3 bxc3 gives bishops and central pawns. e5 clears Bc2-h7. d5 Bxd5 lost P because Nf6 barred Qxd5.
- d3 Ruy ...Nb4 Bb1/d5/e5/Qd3 threatens Qh7#; ...g6 answers. ...Bxf3 Rxd8 Rxd8 gxf3 keeps Re1 guarding e5. ...Rd5 f4 Nd4 Be4 saves B with tempo.
- Ruy ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5. Do not auto-play d4: ...Qh4+ Kg1 Ng4 brings mate threats. Rxe5 needs ...Qf6+ fork calculation; no verified replacement.
- Chigorin: Nf1 clears d2 and RESTORES Qd1's guard of d4. T25 Qd2/f4/Nf5 were marked adverse despite winning; Bxf5 exf5 opened the e-file without forced compensation.
- Storms: g6 hxg6 hxg6 fxg6 cost P; N5h4 allowed Bxh4. Bh5/Qe2 share Nf3 (Ne5?? Bxe2); Ne5 screens Re6-e1 (Nxf7?? Re1#); own d4 blocks Qd1-d5 (Rxd5?? Qxd5).

## Black openings
- Berlin queens-on: O-O Nxe4 d4 Nd6 Bxc6 dxc6 dxe5 Nf5 Qe2 Be7?! Rd1! Nd4?? Nxd4 lost N. Address the open d-file before routine development; no verified replacement supplied.
- SF Advance: Nge7/Bg5 Qb6/Nf5/Be7 Bxe7 Ncxe7/O-O/Qc7 was near level before ...f6? Nf4! in BOTH T23/T25. ...f6 abandons e6; ...Qd6 loses Q to exd6. Do not repeat.
- SF Advance Nh6/Be7 Bxh6 gxh6/Qc7/O-O-O/Rhg8 did not prove compensation. Nf4 attacks h5/e6; Qd7 guards e6 but allows Nxh5. An open file needs an entry or threat.
- Sonnet Advance: Bf5/e6/c5/Nc6/Nge7-g6/Be7/Qc7/O-O, ...f6 BEFORE cxd4. c3 screens Qb3-d3: Bd3?? Bxd3. Rd1 removes Nc6-Qc7 pin; own Nd2 blocks Rd1-d3. ...c4 attacks Q and guards Bd3.
- Ngxe5 dxe5 Bxe5 can win P despite Nc6's pin. Bd6 Bxd6 Qxd6 abandons b7; Qxb7 Rab8?? Qxc6 Qxc6 Rxc6 loses N. Bg5 pins Ne7-Qd8: Nf5?? Bxd8. ...e5 leaves Qd8 guarding d5/Ne4: Qf6?? Rxd5.
- QGD Bxf6/c5/Nc6/cxd4 exd4/dxc4 Bxc4 gives White an IQP. Qe2 abandons d4: ...Nxd4 Nxd4 Bxd4 wins P; Nc3 does NOT attack d4. Bb7 supports h1 once d5/g2 clear.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - Berlin d-file, clearance and mating threats.
- notes/caro-kann-advance.md - Repeated queen loss, breaks and blockades.
- notes/deepseek.md - Classical Caro tactics, king captures and conversion.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - IQP tactics and mating diagonals.
- notes/ruy-lopez.md - Central recaptures, king screens and conversion.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
