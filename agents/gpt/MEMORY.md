# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before EVERY Q/R move, scan enemy pawn/knight captures and every bishop ray. Purpose, check and pin do not establish safety. T23: Qd6?? exd6; e5 still attacked d6.
- Name exact defenders, screens and LEGAL recapturers; trace through OWN pieces. Calculate the full exchange, including king captures and rear attackers. A queen-only defender can permit Qx Qx Rx, winning the original target.
- Refresh pins after either endpoint moves. Leaving one ray may enter another behind the SAME screen. Relative pins permit moves that lose Q/R; a king move can release a pawn's recapture.
- Before moving a screen, name BOTH endpoints and exposed targets. A defender may be unable to recapture safely because it screens Q/R. T24: Rf6 guarded e6 but ...Rxe6 exposed Qd4-g7.
- Track pawn squares, diagonals and promotions. Advances abandon guards: ...f7-f6 exposes e6. Verify replacement defenders; g2 captures h3 until it moves.
- After EVERY capture, refresh the capturer's attacks and vacated lines. Before pawn grabs, test enemy breaks that fork the capturer and another piece.
- When forked, save the higher-value target; compare moves defending both. Before king/Q moves, list guards and screens LOST.
- Before forks/discovered attacks, test enemy checks FIRST. Test captures of every checking/supporting piece before claiming a forced retreat.
- Never play a scan-rejected move without resolving its refutation. Sparse marks and wins do not validate moves.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Long thinks do not replace reply calculation. Name a target or break before shuffling. T24: repeated 30-52-second rook/queen moves supplied no concrete counterplay; lost with 7:29 left.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition. Sacrifice an active rook only for verified promotion or mate.
- Escort passers; count races, captures and blockaders. A rook blockade needs defense against checking forks: Qe6+ then Qd6+ attacked Kb8/Rf8 in T24.
- Minor endings need a target, entry or break. Opposite bishops: count separated passers, blockades and king routes; defend the blocker.
- Use protected checks and restricted exits. Check stalemate after quiet moves/captures; preserve pawn tempi against an immobilized king.

## White openings
- Classical Caro vs DeepSeek: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and attacks Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 wins N. Later rook/bishop gifts were not forced gains.
- Ruy vs SF: Qb1 Bxf3 gxf3 weakens shelter; doubled g-rooks need a proven threat. ...g5 supports Nf4: h4 threatens it, h5 abandons capture. Qd4 c6 Qxc4 cxd5 forks Qc4/Be4: save Q first.
- Open Sicilian vs DeepSeek: Be2/O-O/Be3/f4; ...Bd6?? Qxd6 Qxd6 Bxd6 wins B. Nf6+ screens Rf1-f7, permitting Kxf7; Nxe8+ restores check. Count liquidation, not imagined mate.
- d3 Ruy: ...Nb4 Bb1 d5 e5 clears Bb1-h7; Qd3 threatens Qh7#, ...g6 answers. ...Bxf3 Rxd8 Rxd8 gxf3 keeps Re1 guarding e5. ...Rd5 f4 Nd4 Be4 saves B with tempo. Bd5 guards a2; e7 clears Ba2-f7.
- Ruy traps: Bh5/Qe2 share Nf3's screen: Ne5?? Bxe2. Ne5 screens Re6-e1: Nxf7?? Re1#. OWN d4 blocks Qd1-d5: Rxd5?? Qxd5. Ng5 g6 Ne4 Qxe4 Qxe4 Rxe4 loses N to the rear rook.

## Black openings
- T24 SF Advance: Nh6/Be7 Bxh6 gxh6/Qc7/O-O-O/Rhg8 did not prove compensation for doubled h-pawns. Nf4 attacked h5/e6; Qd7 guarded e6 but allowed Nxh5. An open file needs an actual entry or threat.
- T24 heavy pieces: ...f6 exchanges and Ne5 Nxe5 Rxe5 left White an active rook. ...cxd4 Qxd4/Qg7 created Qd4-g7 behind Rf6. Kh2 unpinned g3, restoring gxf4; ...Kb8 allowed Rxe6 since ...Rxe6 exposes Qxg7. Refresh threats before quiet king moves.
- T23 SF Advance h4 h5/Bxd3 stayed playable through Qc7/Qd2. ...f6? abandoned e6's f7 guard; Nf4 threatens Nxe6 forking Qc7/Rf8. ...Qd6?? exd6 Nxd6 loses Q for P.
- Sonnet Advance: Bf5/e6/c5/Nc6/Nge7-g6/Be7/Qc7/O-O, ...f6 BEFORE cxd4. c3 screens Qb3-d3: Bd3?? Bxd3 wins B. Rd1 removes Rc1's Nc6-Qc7 pin; OWN Nd2 blocks Rd1-d3. ...c4 attacks Q and guards Bd3. This does not justify ...f6 on other boards.
- Ngxe5 dxe5 Bxe5 can win P despite Nc6-Qc7 pin. Bd6 Bxd6 Qxd6 abandons b7. Qxb7 Rab8?? Qxc6 Qxc6 Rxc6 loses N: Qd6 alone guarded it.
- Caro Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7; Bd3 Bxd3 Qxd3 e6, Nd7/Ngf6/Be7. h6 supplies h7 and controls g5.
- Advance: Bg5 pins Ne7-Qd8: Nf5?? Bxd8. ...e5 leaves Qd8 alone guarding d5/Ne4: Qf6?? Rxd5. ...Nxc3 Rxe5 Qd6 bxc3 loses N despite Rc8: Qe3 guards c3.
- ...Rce8 Rxe8 Rxe8 Qxe8+ Qxe8 Rxe8#: count rear attackers; Ng5 bars f7/h7. Qe8 guards Be7 AND b8: Qf7?? Rb8+ Bf8 pins B.
- QGD: h6/b6/Bb7/Nbd7/c5, cxd5 exd5; Ne5 Nxe5 Bxe5 Bd6 Bxd6 Qxd6; dxc5 bxc5. Bf5 hits Rc8: Rcd8. ...Nxe4 Nxe4 dxe4 clears d5; Qd5+ Qxd5 wins Q without recapturer. ...e3 clears Bb7-g2 for Qxg2#.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - d3 Ruy, bishop tempi and promotion guards.
- notes/caro-kann-advance.md - Breaks, defender screens and blockades.
- notes/deepseek.md - Caro/Sicilian exchanges and mating coordination.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Benoni screens and defenders.
- notes/ruy-lopez.md - Pawn forks, relative pins and king attacks.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
