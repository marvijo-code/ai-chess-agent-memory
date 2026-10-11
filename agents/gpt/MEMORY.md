# Chess memory

## Move discipline
- Apply stored warnings BEFORE choosing. T25 repeated T23's ...f6/...Qd6?? exd6. Reuse a rejected move only after resolving its actual refutation.
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Attacking Q/R does not force retreat: Ne5 hit Qc6 but cleared ...Qxg2#; Qb7 hit Ra8 but abandoned Nc4. A pawn attack on a rook can be answered by en passant or a capture elsewhere.
- Before EVERY Q/R move, scan pawn diagonals, knight captures and complete bishop/rook rays, including horizontal rooks. ...Qxf2? allowed Rd2xf2 through e2; f7 blocked Rf8. T27 Ra2?? allowed b3xa2. Purpose/check/defense never establishes safety.
- Name exact defenders, screens and LEGAL surviving recapturers. Trace through BOTH sides' units; count full exchanges and rear attackers. Queen-only defense can fail to Qx Qx Rx.
- Test Kxchecker FIRST, then flights/blocks/captures. Rh7+?? Kxh7: f7 blocked Rb7-h7. Own Re8 denied Ke8 in Qh8#.
- Refresh pins after endpoints move. Rd1/Qd8: ...Nd4?? Nxd4 cxd4 Rxd8+. Kb1 released Rd2 from Qg5's pin. A pinned piece can capture its pinning queen.
- Before moving a screen or guard, name BOTH endpoints and exposed targets. Rf6 screened Qd4-g7; ...Rxe6 exposed Qxg7. ...f6 abandoned Be6 and exf6 cleared Qe2-e6. T27 b2-b4 abandoned Bc3; ...axb3 e.p. hit Ra2, then ...Rxc3.
- Before forks/trades, test captures and checking intermezzos. Ne6 Bxe6 dxe6 Rxe6 lost N+P for B. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N because Rh1's rear path was clear.
- Audit knight forks of king and rooks: T27 Nd4-f3+ forked Kg1/Re1 after Bd3. A recapture after ...Nxe1 still loses the exchange.
- Queenless is not safe: Be4 supported Rg2/Rh1; Rxe7 ignored ...Rh1#. h7 allowed ...Rg1+/...Rh2#; Rxf5 ignored ...Rxd1#.
- A king escort must stay adjacent after EVERY move. ...Nf2 left Kd4's protection; ...Ke4/...Kd3 did not restore it, and Qxf2 won N.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Name a target or break before shuffling. Long thinks did not prevent T27 h4/...f5 or Qxf7+ missing Nh6+. When worse, use 3-10 seconds for verified replies.
- Track TOTAL material after trades. e5 dxe5 Nxe5 and Bxa4 bxa4 Rxa4 each left one pawn down. T27 vs Sonnet Qxf7+ Kxf7 was a legitimate queen trade with equal material, but discarded a winning fork.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition. Sacrifices need verified promotion or mate.
- Escort passers; count races/blockaders/checking tempi. Scan straight AND capture-promotions two advances ahead. Test stalemate; preserve pawn tempi.
- Audit blockader pins: b7/Rb8/Ra8 pinned Rb8 to Kg8; ...Rxb7 was illegal. ...Rf8 Rxf8+ Nxf8 b8=Q removed the sole blockader.

## White openings
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N. Bc1/...Qc7/f4: ...Nxf4?? Bxf4 because e5 screens Qc7-f4.
- Chigorin: Nf1 restores Qd1-d4. With ...a4/Nc5, Qd1 also guards b3 through c2; Qf3 abandons it and permits ...Nb3 forking Ra1/Bd2. Solve queenside threats before committing to g4/h4/g5.
- T27 Sonnet: Qg6/Nf5 vs Kg8/Qf7/g7/Nh7/Bf8: 33.Nh6+! pins g7 to Kg8, so ...gxh6 is illegal; only ...Kh8, then Nxf7+ wins Q. Search knight checks BEFORE accepting a queen trade.
- Ruy ...Bc5/...Bb6/...Bb7: Nbd2 blocks Qd1-d4; ...exd4 cxd4 Nxd4 Nxd4 Bxd4 wins P. T27 ...Na5-c4-b2-a4 won P. Kh2/Nf4/h4? met ...f5; before g3 calculate ...fxe4, ...Nxd5 and Qe7-f6-g5-h4+.
- d3 Ruy: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. d5 Bxd5 lost P because Nf6 barred Qxd5. Qd3/Bb1 threatens Qh7#; ...g6 answers.
- ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5. d4?? allows ...Qh4+ Kg1 Ng4. Rxe5 needs ...Qf6+ fork calculation.
- Bh6/Qxh6/Ng5/Nh5: ...Nxh5 abandons h7; Qxh7+ Kf8 Qh8# with Re8 blocking e8. Bh5/Qe2 share Nf3 (Ne5 Bxe2); Ne5 screens Re6-e1 (Nxf7 Re1#); own d4 blocks Qd1-d5.

## Black openings
- Classical Caro T27: ...h6/Bh7!/Nd7/Bxd3/e6/Ngf6/Be7/O-O. ...Nxe5?! dxe5 Nd5?! was adverse. Qxd5?? Bxg5+! Qd2 Bxd2+ Rxd2 won Q for B after losing N; exploit the check without certifying preceding moves.
- Open Ruy d4/exd4/Re1/b5/Bb3/O-O/a4/Bb7/e5/Ne8/Bd5/d6: Nxd4! Bxb7! Rb8 Bxa6 dxe5 c3 Ne6?! Qxd8 Rxd8 Bxb5! left a pawn deficit/outside passer. Evaluate queen trades AND ensuing captures.
- Berlin queens-on: O-O Nxe4 d4 Nd6 Bxc6 dxc6 dxe5 Nf5 Qe2 Be7?! Rd1! Nd4?? Nxd4 lost N. Address the open d-file before routine development.
- SF Advance Nge7/Bg5 Qb6/Nf5/Be7 Bxe7 Ncxe7/O-O/Qc7: ...f6? Nf4! repeated T23/T25; ...Qd6 loses Q to exd6. Nh6/Bxh6/gxh6 and long castling gave no proven compensation.
- Sonnet Advance: ...f6 BEFORE cxd4 worked tactically: c3 screened Qb3-d3, Bd3?? Bxd3; Rd1 removed Nc6-Qc7 pin but Nd2 blocked Rd1-d3; ...c4 attacked Q and guarded Bd3.
- Ng6/Nb3: ...cxd4? Nbxd4 Nxd4? cxd4 was adverse. Qb6/Qxb6 axb6 weakened b6. Queenless ...f6/exf6/Rxf6?! Ne5/Nxe5/dxe5/Rg6? let Bxb6 win P; mate does not validate it.
- Ngxe5 dxe5 Bxe5 can win P despite Nc6's pin. Bd6 Bxd6 Qxd6 abandons b7; Qxb7 Rab8?? Qxc6 Qxc6 Rxc6 loses N. Bg5 pins Ne7-Qd8: Nf5?? Bxd8. ...e5 leaves Qd8 guarding d5/Ne4: Qf6?? Rxd5.
- QGD cxd4 exd4/dxc4 Bxc4 gives White an IQP. Qe2 abandons d4: ...Nxd4 Nxd4 Bxd4 wins P; Nc3 does NOT attack d4. Bb7 supports h1 once d5/g2 clear.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - Berlin d-file and clearance.
- notes/caro-kann-advance.md - Central exchanges, breaks and queenless mate.
- notes/deepseek.md - Classical Caro, intermezzos and conversion errors.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - IQP tactics and mating diagonals.
- notes/ruy-lopez.md - Knight checks, central breaks, guards and passers.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
