# Chess memory

## Move discipline
- Apply warnings BEFORE choosing. T25 repeated T23's ...f6/...Qd6?? exd6. Reuse a rejected move only after resolving its actual refutation.
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Attacking Q/R does not force retreat. T26 Ne5 hit Qc6 but cleared ...Qxg2# with Bb7 support. T27 Qb7 hit Ra8 but abandoned Nc4: ...Qxc4.
- Before EVERY Q/R move, scan pawn/knight captures and bishop/rook rays. Qd6?? exd6; Bh6 Bxh6 Qxh6 Rxh6 with Rh8 uncastled. Purpose/check/pins do not establish safety.
- Name exact defenders, screens and LEGAL surviving recapturers. Trace through BOTH sides' units; count full exchanges and rear attackers. Queen-only defense can fail to Qx Qx Rx.
- Test Kxchecker FIRST, then flights/blocks/captures. Rh7+?? Kxh7: f7 blocked Rb7-h7. Own pieces also block flights: Re8 denied Ke8 in Qh8#.
- Refresh pins after endpoints move. Rd1/Qd8: ...Nd4?? Nxd4 cxd4 Rxd8+. King moves can release pawn captures; a pinned piece can capture its pinning queen.
- Before moving a screen, name BOTH endpoints and exposed targets. Rf6 screened Qd4-g7; ...Rxe6 exposed Qxg7. En passant changes THREE squares: exf6 e.p. opened Re1-e7 and Bc2-h7.
- Pawn advances abandon guards AND enable captures removing screens. ...f6 abandoned Be6; exf6 cleared Qe2-e6. Refresh attacks after EVERY capture.
- Before forks, test captures and checking replies. Ne6 Bxe6 dxe6 Rxe6 lost N+P for B. ...Nc3+ Qxc3 Rxd1 Rxd1 lost N: Rh1's rear path was clear.
- Own d6 blocked Rd8's defense of Nd5. Nxe7 Qxe7 Rxe7 won Q for N. ...Nd4 cxd4 cxd4 gives N for P; require verified compensation.
- Queenless is not safe. Be4 supported Rg2/Rh1 through f3/g2; Rxe7 ignored ...Rh1#. A promotion threat likewise does not answer rook checks: T27 h7 allowed ...Rg1+ and ...Rh2#.
- A king escort must stay adjacent after EVERY move. ...Nf2 left Kd4's protection; ...Ke4/...Kd3 did not restore it, and Qxf2 won N.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Name a target or break before shuffling. T27 h4/Qb1/g3 took 46/43/52 seconds yet missed ...f5. Worse: use 3-10 seconds for verified replies; reserve time for real tactical choices.
- Track TOTAL material after trades. T26 e5 dxe5 Nxe5 left ONE PAWN DOWN. T27 Bxa4 bxa4 Rxa4 still left one pawn down; equal exchanges do not recover losses.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition. Sacrifices need verified promotion or mate.
- Escort passers; count races, blockaders and enemy checking tempi. Scan straight AND capture-promotions two advances ahead. Test stalemate and preserve pawn tempi.
- Test attacks/pins on a blockader. T26 b7/Rb8: Ra8 pinned Rb8 to Kg8; ...Rxb7 was illegal. ...Rf8 Rxf8+ Nxf8 b8=Q removed the sole blockader.

## White openings
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N. Bc1/...Qc7/f4: ...Nxf4?? Bxf4 because e5 screens Qc7-f4.
- Ruy ...Bc5/...Bb6/...Bb7 with d4/e4: Nbd2 blocks Qd1-d4; ...exd4 cxd4 Nxd4 Nxd4 Bxd4 wins P. Preserve full recapture chains before developing.
- T27 c3/d4/Re1/h3/a4/Be3: ...Na5-c4-b2-a4 won a pawn. Later Kh2/...Nf4/h4? was met by ...f5. Before h4/g3, calculate ...fxe4, ...Nxd5 and Qe7-f6-g5-h4+; no verified replacement.
- d3 Ruy: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. d5 Bxd5 lost P because Nf6 barred Qxd5. Qd3/Bb1 threatens Qh7#; ...g6 answers.
- Ruy ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5. d4?? allows ...Qh4+ Kg1 Ng4. Rxe5 needs ...Qf6+ fork calculation.
- Chigorin/Breyer: Nf1 clears d2, restoring Qd1-d4. Qd2/f4/Nf5 were adverse despite winning. Bh6/Qxh6/Ng5/Nh5: ...Nxh5 abandons h7; Qxh7+ Kf8 Qh8# with Re8 blocking e8.
- Storms: g6 hxg6 hxg6 fxg6 cost P; N5h4 allowed Bxh4. Bh5/Qe2 share Nf3 (Ne5 Bxe2); Ne5 screens Re6-e1 (Nxf7 Re1#); own d4 blocks Qd1-d5.

## Black openings
- Open Ruy 6.d4 exd4/Re1/b5/Bb3/O-O/a4/Bb7/e5/Ne8/Bd5/d6: Nxd4! Bxb7! Rb8 Bxa6 dxe5 c3 Ne6?! Qxd8 Rxd8 Bxb5! left a pawn deficit and outside passer. Evaluate queen trades AND ensuing captures before retreating.
- Berlin queens-on: O-O Nxe4 d4 Nd6 Bxc6 dxc6 dxe5 Nf5 Qe2 Be7?! Rd1! Nd4?? Nxd4 lost N. Address the open d-file before routine development.
- SF Advance Nge7/Bg5 Qb6/Nf5/Be7 Bxe7 Ncxe7/O-O/Qc7: ...f6? Nf4! repeated T23/T25; ...Qd6 loses Q to exd6. Nh6/Bxh6/gxh6 and queenside castling gave no proven compensation.
- Sonnet Advance: ...f6 BEFORE cxd4 worked tactically: c3 screened Qb3-d3, Bd3?? Bxd3; Rd1 removed Nc6-Qc7 pin but Nd2 blocked Rd1-d3; ...c4 attacked Q and guarded Bd3.
- Ng6/Nb3: ...cxd4? Nbxd4 Nxd4? cxd4 was adverse. Qb6/Qxb6 axb6 weakened b6. Queenless ...f6/exf6/Rxf6?! Ne5/Nxe5/dxe5/Rg6? let Bxb6 win P; mate does not validate it.
- Ngxe5 dxe5 Bxe5 can win P despite Nc6's pin. Bd6 Bxd6 Qxd6 abandons b7; Qxb7 Rab8?? Qxc6 Qxc6 Rxc6 loses N. Bg5 pins Ne7-Qd8: Nf5?? Bxd8. ...e5 leaves Qd8 guarding d5/Ne4: Qf6?? Rxd5.
- QGD cxd4 exd4/dxc4 Bxc4 gives White an IQP. Qe2 abandons d4: ...Nxd4 Nxd4 Bxd4 wins P; Nc3 does NOT attack d4. Bb7 supports h1 once d5/g2 clear.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - Berlin d-file and clearance.
- notes/caro-kann-advance.md - Central exchanges, breaks and queenless mate.
- notes/deepseek.md - Classical Caro tactics and conversion.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - IQP tactics and mating diagonals.
- notes/ruy-lopez.md - Central breaks, abandoned guards and passers.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
