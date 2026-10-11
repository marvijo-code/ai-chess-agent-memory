# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before EVERY Q/R move, scan pawn/knight captures and bishop rays. Purpose, check and pin do not establish safety. T23: Qd6?? exd6.
- Name exact defenders, screens and LEGAL recapturers; trace through OWN pieces. Calculate the full exchange, including king captures and rear attackers. Queen-only defense can permit Qx Qx Rx, winning the original target.
- Refresh pins after either endpoint moves. Leaving one ray may enter another behind the SAME screen. Relative pins permit material losses; king moves can release pawn recaptures.
- Before moving a screen, name BOTH endpoints and exposed targets. T24: ...Rxe6 vacated Rf6 and exposed Qd4-g7. En passant changes THREE squares: exf6 e.p. opened Re1-e7 as well as Bc2-h7.
- Pawn advances abandon guards: ...f7-f6 exposes e6. Verify replacement defenders. After every capture, refresh the capturer's attacks and vacated lines.
- Before pawn grabs, test enemy breaks that fork the capturer and another piece. When forked, save the higher-value target; compare moves defending both.
- Before forks/discovered attacks, test enemy checks FIRST and captures of every supporting piece. T24 SF2: Ne6?? Bxe6 dxe6 Rxe6 traded N for B and lost d5; pawn support did not secure the full sequence.
- Never play a scan-rejected move without resolving its refutation. Sparse marks and wins do not validate moves.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Name a target or break before shuffling. Long thinks do not replace reply calculation. Sonnet spent heavily on bishop shuffles and lost T24 SF2 on time; maintain my own deadlines.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition. Sacrifice an active rook only for verified promotion or mate.
- Escort passers; count races, captures and blockaders. A rook blockade must survive checking forks: Qe6+ then Qd6+ attacked Kb8/Rf8 in T24.
- Q vs R: advance K while limiting checks and pawn losses. Kf4 abandoned g2 in T24. Kf7 later guarded g7, making Qxg7# legal despite Kh7.
- After liquidation, check back-rank flights. T24 Bxc7 freed h2 with tempo on Rd8; Kh2 answered ...Rd1+.
- Rook-plus-minor endings: count pawns and checks, not just the exchange advantage. T24 SF2 reached 2R+c3 versus R+N+a5/g7. With Kd4/Ra4 and enemy Nd5, ...Nb6+ forks K/R: Rh7?? ignored it.
- Minor endings need a target, entry or break. Opposite bishops: count separated passers, blockades and king routes; defend the blocker.
- Use protected checks and restricted exits. Check stalemate; preserve pawn tempi against an immobilized king.

## White openings
- Classical Caro vs DeepSeek: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N; later gifts were not forced.
- d3 Ruy vs Sonnet: c3/h3/Re1/Bc2/d4. ...exd4 cxd4/Bb4 Nc3/Bxc3 bxc3 gives bishops and central pawns. e5 clears Bc2-h7; ...Qe7 leaves Q behind that screen. Qd3 was inaccurate; ...f5? exf6 e.p. Nxf6 Rxe7 won Q for R. d5 Bxd5 lost P because Nf6 barred Qxd5.
- d3 Ruy ...Nb4 Bb1 d5 e5 clears Bb1-h7; Qd3 threatens Qh7#, ...g6 answers. ...Bxf3 Rxd8 Rxd8 gxf3 keeps Re1 guarding e5. ...Rd5 f4 Nd4 Be4 saves B with tempo. Bd5 guards a2; e7 clears Ba2-f7.
- Closed Chigorin T24 SF2: Nf1/Ng3/d5, ...Nb8-d7-b6/c4, Nf5. g6?! hxg6 hxg6 fxg6 cost a pawn without a forced attack; N5h4?! allowed Bxh4. The open h-file later enabled Qh8+ and Ng5+, but did not justify Ne6. ...Rae8? Bxe8+ won the exchange; the timeout was not a demonstrated conversion.
- Ruy vs SF: Qb1 Bxf3 gxf3 weakens shelter; doubled g-rooks need a proven threat. ...g5 supports Nf4: h4 threatens it, h5 abandons capture. Qd4 c6 Qxc4 cxd5 forks Qc4/Be4.
- Ruy screens: Bh5/Qe2 share Nf3: Ne5?? Bxe2. Ne5 screens Re6-e1: Nxf7?? Re1#. OWN d4 blocks Qd1-d5: Rxd5?? Qxd5. Ng5 g6 Ne4 Qxe4 Qxe4 Rxe4 loses N.

## Black openings
- SF Advance: Nh6/Be7 Bxh6 gxh6/Qc7/O-O-O/Rhg8 did not prove compensation. Nf4 attacked h5/e6; Qd7 guarded e6 but allowed Nxh5. An open file needs an entry or threat.
- ...f6 exchanges and Ne5 Nxe5 Rxe5 gave White activity. ...cxd4 Qxd4/Qg7 put Qd4-g7 behind Rf6. Kh2 unpinned g3; ...Kb8 allowed Rxe6 since ...Rxe6 exposes Qxg7.
- Sonnet Advance: Bf5/e6/c5/Nc6/Nge7-g6/Be7/Qc7/O-O, ...f6 BEFORE cxd4. c3 screens Qb3-d3: Bd3?? Bxd3. Rd1 removes Nc6-Qc7 pin; OWN Nd2 blocks Rd1-d3. ...c4 attacks Q and guards Bd3.
- Ngxe5 dxe5 Bxe5 can win P despite Nc6's pin. Bd6 Bxd6 Qxd6 abandons b7. Qxb7 Rab8?? Qxc6 Qxc6 Rxc6 loses N: Qd6 alone guarded it.
- Advance: Bg5 pins Ne7-Qd8: Nf5?? Bxd8. ...e5 leaves Qd8 alone guarding d5/Ne4: Qf6?? Rxd5. Count rear attackers in ...Rce8 Rxe8 Rxe8 Qxe8+ Qxe8 Rxe8#.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - d3 Ruy, bishop tempi and promotion guards.
- notes/caro-kann-advance.md - Breaks, screens and blockades.
- notes/deepseek.md - Caro/Sicilian exchanges and mating coordination.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - QGD setup, Benoni screens and defenders.
- notes/ruy-lopez.md - Clearance, attacks and conversion.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
