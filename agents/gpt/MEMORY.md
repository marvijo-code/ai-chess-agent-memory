# Chess memory

## Move discipline
- Apply warnings BEFORE choosing. T25 repeated T23's ...f6/...Qd6?? exd6. Reuse a rejected move only after resolving its refutation on the actual board.
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Queen attacks do not force retreat. T26R2 Ne5 attacked Qc6 but cleared c6-d5-e4-f3-g2: ...Qxg2# with Bb7 support. Qe2 guarding Nf3 did not replace its screening duty.
- Before EVERY Q/R move, scan pawn/knight captures and bishop rays. Qd6?? exd6; Bh6 Bxh6 Qxh6 Rxh6 with Rh8 uncastled. Purpose, check and pins do not establish safety.
- Name exact defenders, screens and LEGAL surviving recapturers. Trace through BOTH sides' pieces/pawns; count full exchanges and rear attackers. Queen-only defense can fail to Qx Qx Rx.
- Before claiming mate, test Kxchecker FIRST. Rh7+?? Kxh7: f7 blocked Rb7-h7; Bd4 guarded g7/h8, not h7. Pinned blockers still obstruct rays.
- Refresh pins after endpoints move. Rd1/Qd8: ...Nd4?? Nxd4 cxd4 Rxd8+. A king move can release pawn recaptures; a pinned piece can capture its pinning queen.
- Before moving a screen, name BOTH endpoints and exposed targets. Rf6 screened Qd4-g7; ...Rxe6 exposed Qxg7. En passant changes THREE squares: exf6 e.p. opened Re1-e7 and Bc2-h7.
- Pawn advances abandon guards AND enable captures removing screens. ...f6 abandoned Be6; exf6 cleared Qe2-e6, then Qxe6+ won B.
- After captures, refresh the capturer's attacks and vacated lines. Before pawn grabs, test breaks forking the capturer and another piece.
- Before forks, test captures of supports and checking replies. Ne6 Bxe6 dxe6 Rxe6 lost N+P for B. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N: Rh1's rear path was clear.
- Bb7/Nd5 versus Kh1 with g2 empty: ...Nxc3+ uncovered check and attacked Qe2. Qg2 became absolutely pinned; Qxh3 was illegal after ...Qxh3#.
- Own d6 blocked Rd8's defense of Nd5. Nxe7 Qxe7 Rxe7 won Q for N. ...Nd4 cxd4 cxd4 gives N for P; require verified compensation.
- Queenless does not mean safe. T26R3 Be4 supported Rg2 and Rh1 through f3/g2. After ...Rxh2, Rxe7 ignored ...Rh1#. Kf1 cannot take guarded Rg2; Be2 cannot play Bf1 while its king occupies f1. Test interpositions on the actual board.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Name a target or break before shuffling. Long thinks do not replace reply calculation. T26R3 ...Rxg2+ took 52 seconds despite a clear battery; shorten verified forcing moves.
- Track TOTAL material after trades. T26R2 e5 dxe5 Nxe5 did not recover lost d4: still ONE PAWN DOWN. Equal rook exchanges do not recover pieces.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition. Sacrifice a rook only for verified promotion or mate.
- Escort passers; count races, captures and blockaders. Rf8 failed to Qe6+/Qd6+, forking Kb8/Rf8. Scan straight AND capture-promotions two advances ahead.
- Use protected checks; test every flight and stalemate. Qh5 supported Re8+ Rxe8 Qxe8#. Preserve pawn tempi against an immobilized king.
- Endings need targets, entries or breaks. Kd4/Ra4 versus Nd5 permits ...Nb6+; c4 can attack Rb5/Nd5.

## White openings
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N. Bc1/...Qc7/f4 supports e5; ...Nxf4?? Bxf4 wins N because e5 screens Qc7-f4.
- Ruy d3/...Bc5/...Bb6/...Bb7 with d4/e4: Nbd2 blocks Qd1-d4. ...exd4 cxd4 Nxd4 Nxd4 Bxd4 wins d4. Preserve sufficient recaptures BEFORE developing.
- d3 Ruy: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. d5 Bxd5 lost P because Nf6 barred Qxd5. Qd3/Bb1 threatens Qh7#; ...g6 answers. ...Bxf3 Rxd8 Rxd8 gxf3 keeps Re1 guarding e5.
- Ruy ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5. Do not auto-play d4: ...Qh4+ Kg1 Ng4 brings mate threats. Rxe5 needs ...Qf6+ fork calculation; no verified replacement.
- Chigorin: Nf1 clears d2 and restores Qd1-d4. T25 Qd2/f4/Nf5 were adverse despite winning; Bxf5 exf5 opened the e-file without forced compensation.
- Storms: g6 hxg6 hxg6 fxg6 cost P; N5h4 allowed Bxh4. Bh5/Qe2 share Nf3 (Ne5 Bxe2); Ne5 screens Re6-e1 (Nxf7 Re1#); own d4 blocks Qd1-d5 (Rxd5 Qxd5).

## Black openings
- Berlin queens-on: O-O Nxe4 d4 Nd6 Bxc6 dxc6 dxe5 Nf5 Qe2 Be7?! Rd1! Nd4?? Nxd4 lost N. Address the open d-file before routine development; no verified replacement.
- SF Advance Nge7/Bg5 Qb6/Nf5/Be7 Bxe7 Ncxe7/O-O/Qc7: ...f6? Nf4! repeated T23/T25; ...Qd6 loses Q to exd6. Nh6/Bxh6/gxh6 with queenside castling gave no proven compensation.
- Sonnet Advance: distinguish central structures. Earlier ...f6 BEFORE cxd4 worked tactically: c3 screened Qb3-d3, Bd3?? Bxd3; Rd1 removed Nc6-Qc7 pin but Nd2 blocked Rd1-d3; ...c4 attacked Q and guarded Bd3.
- T26R3 Ng6/Nb3: ...cxd4? Nbxd4 Nxd4? cxd4 was marked adverse. Qb6/Qxb6 axb6 opened a-file but left b6 weak. Queenless ...f6/exf6/Rxf6?! N e5/Nxe5/dxe5/Rg6? let Bxb6 win P; later mate does not validate this sequence.
- Ngxe5 dxe5 Bxe5 can win P despite Nc6's pin. Bd6 Bxd6 Qxd6 abandons b7; Qxb7 Rab8?? Qxc6 Qxc6 Rxc6 loses N. Bg5 pins Ne7-Qd8: Nf5?? Bxd8. ...e5 leaves Qd8 guarding d5/Ne4: Qf6?? Rxd5.
- QGD Bxf6/c5/Nc6/cxd4 exd4/dxc4 Bxc4 gives White an IQP. Qe2 abandons d4: ...Nxd4 Nxd4 Bxd4 wins P; Nc3 does NOT attack d4. Bb7 supports h1 once d5/g2 clear.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - Berlin d-file and clearance.
- notes/caro-kann-advance.md - Central exchanges, breaks and queenless mate.
- notes/deepseek.md - Classical Caro tactics and conversion.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - IQP tactics and mating diagonals.
- notes/ruy-lopez.md - Central recaptures and king screens.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
