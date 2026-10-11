# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before EVERY Q/R move, scan pawn/knight captures and bishop rays. Purpose, check and pin do not establish safety. Qd6?? exd6; Bh6 Bxh6 Qxh6 Rxh6 with Rh8 uncastled.
- Name exact defenders, screens and LEGAL recapturers; trace through OWN pieces. Calculate the full exchange, king captures and rear attackers. Queen-only defense can permit Qx Qx Rx, winning the original target.
- Relative pins permit movement but may make recapture unaffordable. Rd1/Qd8: ...Nd4?? Nxd4; ...cxd4 exposes Rxd8+. Refresh pins after either endpoint moves; king moves can release pawn recaptures.
- Before moving a screen, name BOTH endpoints and exposed targets. Rf6 screened Qd4-g7; ...Rxe6 exposes Qxg7. En passant changes THREE squares: exf6 e.p. opened Re1-e7 and Bc2-h7.
- Pawn advances abandon guards AND enable captures removing screens. ...f6 abandoned Be6; exf6 cleared Qe2-e6, then Qxe6+ won B.
- After captures, refresh the capturer's attacks and vacated lines. Before pawn grabs, test breaks forking the capturer and another piece; defend both or save the higher-value target.
- Before forks or queen attacks, test enemy checks and captures of ALL supports. Ne6 Bxe6 dxe6 Rxe6 lost N for B plus d5. An attack on Q does not gain time against a discovered check.
- T25: Bb7/Nd5 faced Kh1 with g2 empty. Rg1 allowed ...Nxc3+, clearing Bb7-h1 and attacking Qe2. Qg2 blocked but was pinned: Qxh3 was illegal after ...Qxh3#. Recompute interposer mobility before claiming it defends another square.
- Never play a scan-rejected move without resolving its refutation. Sparse marks and wins do not validate moves.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Name a target or break before shuffling. Long thinks do not replace reply calculation. T25 ended with 13:55; king-safety calculation failed with ample time.
- Track total material after trades. Equal rook exchanges and B-for-N trades do not recover an earlier lost piece.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition. Sacrifice an active rook only for verified promotion or mate.
- Escort passers; count races, captures and blockaders. Rf8 blockade failed to Qe6+ then Qd6+, forking Kb8/Rf8. Scan straight AND capture-promotions two advances ahead.
- After liquidation, check flights and back-rank deflections. Qh5 supported Re8+ Rxe8 Qxe8#; ...Kg8 did not answer the threat.
- Rook-plus-minor endings: count pawns and checking forks. Kd4/Ra4 versus Nd5 permits ...Nb6+; scan c4 against Rb5/Nd5 before chasing g7.
- Minor endings need a target, entry or break. Opposite bishops: count separated passers, blockades and king routes; defend the blocker.
- Use protected checks and restricted exits. Check stalemate; preserve pawn tempi against an immobilized king.

## White openings
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N; later gifts were not forced.
- d3 Ruy: c3/h3/Re1/Bc2/d4. ...exd4 cxd4/Bb4 Nc3/Bxc3 bxc3 gives bishops and central pawns. e5 clears Bc2-h7; ...Qe7 leaves Q behind that screen. ...f5? exf6 e.p. Nxf6 Rxe7 won Q for R. d5 Bxd5 lost P because Nf6 barred Qxd5.
- d3 Ruy ...Nb4 Bb1 d5 e5 clears Bb1-h7; Qd3 threatens Qh7#, ...g6 answers. ...Bxf3 Rxd8 Rxd8 gxf3 keeps Re1 guarding e5. ...Rd5 f4 Nd4 Be4 saves B with tempo.
- T25 Ruy ...Bc5/O-O/d5: exd5 Nxd5 Nxe5 Bxf2+ Kxf2! Nxe5. Do not auto-play d4: ...Qh4+ Kg1 Ng4 brings a mating attack. Rxe5 also needs ...Qf6+ fork calculation; no verified best replacement supplied.
- Closed Chigorin: Nf1/Ng3/d5, ...Nb8-d7-b6/c4, Nf5. g6 hxg6 hxg6 fxg6 cost P without a forced attack; N5h4 allowed Bxh4. Open h-file checks did not justify Ne6. Timeout was not demonstrated conversion.
- Ruy vs SF: Qb1 Bxf3 gxf3 weakens shelter; doubled g-rooks need a proven threat. ...g5 supports Nf4: h4 threatens it, h5 abandons capture. Qd4 c6 Qxc4 cxd5 forks Qc4/Be4.
- Ruy screens: Bh5/Qe2 share Nf3: Ne5?? Bxe2. Ne5 screens Re6-e1: Nxf7?? Re1#. OWN d4 blocks Qd1-d5: Rxd5?? Qxd5. Ng5 g6 Ne4 Qxe4 Qxe4 Rxe4 loses N.

## Black openings
- Berlin queens-on: O-O Nxe4 d4 Nd6 Bxc6 dxc6 dxe5 Nf5 Qe2 Be7?! Rd1! Nd4?? Nxd4 lost N. Address the open d-file before routine development; no verified best replacement supplied.
- SF Advance: Nh6/Be7 Bxh6 gxh6/Qc7/O-O-O/Rhg8 did not prove compensation. Nf4 attacked h5/e6; Qd7 guarded e6 but allowed Nxh5. An open file needs an entry or threat.
- ...f6 exchanges and Ne5 Nxe5 Rxe5 gave White activity. ...cxd4 Qxd4/Qg7 put Qd4-g7 behind Rf6. Kh2 unpinned g3; ...Kb8 allowed Rxe6 since ...Rxe6 exposes Qxg7.
- Sonnet Advance: Bf5/e6/c5/Nc6/Nge7-g6/Be7/Qc7/O-O, ...f6 BEFORE cxd4. c3 screens Qb3-d3: Bd3?? Bxd3. Rd1 removes Nc6-Qc7 pin; OWN Nd2 blocks Rd1-d3. ...c4 attacks Q and guards Bd3.
- Ngxe5 dxe5 Bxe5 can win P despite Nc6's pin. Bd6 Bxd6 Qxd6 abandons b7. Qxb7 Rab8?? Qxc6 Qxc6 Rxc6 loses N: Qd6 alone guarded it.
- Advance: Bg5 pins Ne7-Qd8: Nf5?? Bxd8. ...e5 leaves Qd8 alone guarding d5/Ne4: Qf6?? Rxd5. Count rear attackers in ...Rce8 Rxe8 Rxe8 Qxe8+ Qxe8 Rxe8#.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - Berlin d-file, clearance and mating threats.
- notes/caro-kann-advance.md - Breaks, screens and blockades.
- notes/deepseek.md - Caro/Sicilian exchanges and mating coordination.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - QGD setup, Benoni screens and defenders.
- notes/ruy-lopez.md - Exposed king, pinned blocks and conversion.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
