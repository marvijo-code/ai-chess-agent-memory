# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before EVERY Q/R move, scan enemy pawn/knight captures and every bishop ray. Defensive purpose, check and pin do not establish safety. T23: Qd6?? exd6; e5 still attacked d6.
- Name exact defenders, screens and LEGAL recapturers; trace through OWN pieces. Calculate the full exchange, including king captures and rear attackers. A queen-only defender can permit Qx Qx Rx, winning the original target.
- Refresh pins after either endpoint moves. Leaving one ray may enter another behind the SAME screen. Relative pins permit moves that lose Q/R.
- Before moving a screen, name BOTH endpoints and exposed targets. Attacking the pinning piece does not prevent capture. A checking piece can block my own rook's protection.
- Track pawn squares, diagonals and forward/capture-promotions. Advances abandon guards: ...f7-f6 can expose e6 to a knight fork. Verify replacement defenders; g2 captures h3 until it moves.
- After EVERY capture, refresh the capturer's attacks and vacated lines. Before pawn grabs, test enemy breaks that fork the capturer and another piece.
- When forked, save the higher-value target; compare moves defending both. Before king/Q moves, list guards and screens LOST.
- Before forks/discovered attacks, test enemy checks FIRST. Test captures of every checking/supporting piece before claiming a forced retreat.
- Never play a scan-rejected move without resolving its refutation. Sparse marks and wins do not validate moves.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Long thinks do not replace reply calculation. Name a target or break before shuffling; shorten routine endgame maneuvers.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition. Sacrifice an active rook only for verified promotion or mate.
- Escort passers; count races, captures and blockaders. Minor endings need a target, entry or break. Opposite bishops: count separated passers, blockades and king routes; defend the blocker.
- Use protected checks and restricted exits. Check stalemate after quiet moves/captures; preserve pawn tempi against an immobilized king.

## White openings
- T24 Classical Caro vs DeepSeek: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opened Rd1's file and attacked Nf6. ...Nd7?? Qxd7 Qxd7 Rxd7 won N. ...Rfd8 Rxd8+ Rxd8 simplified; ...Rd1+ Rxd1 and ...Bf6 exf6 were further gifts, not forced gains.
- T23 Ruy vs SF: Qb1 Bxf3 gxf3 weakened shelter; doubled g-rooks gave no proven attack. ...g5 supports Nf4: h4 threatens it, h5 abandons capture. Qd4 c6 Qxc4 cxd5 forks Qc4/Be4: save Q first.
- Open Sicilian vs DeepSeek: Be2/O-O/Be3/f4; ...Bd6?? Qxd6 Qxd6 Bxd6 won B. Nf6+ screened Rf1-f7, permitting Kxf7; Nxe8+ restored check. Count liquidation, not imagined mate.
- d3 Ruy: ...Nb4 Bb1 d5 e5 clears Bb1-h7; Qd3 threatens Qh7#, ...g6 answers. ...Bxf3 Rxd8 Rxd8 gxf3 keeps Re1 guarding e5. ...Rd5 f4 Nd4 Be4 saves B with tempo. Bd5 guards a2; e7 clears Ba2-f7 before promotion.
- Ruy traps: Bh5/Qe2 share Nf3's screen: Ne5?? Bxe2. Ne5 screens Re6-e1: Nxf7?? Re1#. OWN d4 blocks Qd1-d5: Rxd5?? Qxd5. Ng5 g6 Ne4 Qxe4 Qxe4 Rxe4 loses N to the rear rook.

## Black openings
- T23 SF Advance h4 h5/Bxd3 stayed playable through Qc7/Qd2. ...f6? abandoned e6's f7 guard; Nf4 threatens Nxe6 forking Qc7/Rf8. ...Qd6?? exd6 Nxd6 loses Q for P. Check lost guards and defensive destinations.
- T23 Sonnet Advance: Bf5/e6/c5/Nc6/Nge7-g6/Be7/Qc7/O-O, ...f6 BEFORE cxd4. c3 screens Qb3-d3: Bd3?? Bxd3 wins B. Rd1 removes Rc1's Nc6-Qc7 pin; OWN Nd2 blocks Rd1-d3. ...c4 attacks Q and guards Bd3. This does not justify ...f6 on other boards.
- T23 R3: Ngxe5 dxe5 Bxe5 wins P despite Nc6-Qc7 pin. Bd6 Bxd6 Qxd6 abandons b7. Qxb7 Rab8?? Qxc6 Qxc6 Rxc6 loses N: Qd6 alone guarded it. Secure defenders before chasing Q.
- Caro Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7; Bd3 Bxd3 Qxd3 e6, Nd7/Ngf6/Be7. h6 supplies h7 and controls g5.
- Advance: Bg5 pins Ne7-Qd8: Nf5?? Bxd8. ...e5 leaves Qd8 alone guarding d5/Ne4: Qf6?? Rxd5. ...Nxc3 Rxe5 Qd6 bxc3 loses N despite Rc8: Qe3 guards c3.
- ...Rce8 Rxe8 Rxe8 Qxe8+ Qxe8 Rxe8#: count ALL rear attackers; Ng5 bars f7/h7. Qe8 guards Be7 AND b8: Qf7?? Rb8+ Bf8 pins B. Qxf4?? g3xf4 loses Q.
- QGD: h6/b6/Bb7/Nbd7/c5, cxd5 exd5; Ne5 Nxe5 Bxe5 Bd6 Bxd6 Qxd6; dxc5 bxc5. Bf5 hits Rc8: Rcd8. ...Nxe4 Nxe4 dxe4 clears d5; Qd5+ Qxd5 wins Q without recapturer. ...e3 clears Bb7-g2 for Qxg2#.

## Recurring geometry
- Rbg7+ Bxg7 Rxg7+ Kxg7 gives BOTH rooks for B. Qa7/Nd6 cages Kd8: preserve pawn tempi, Ke5-e6 then Qd7#.
- Benoni Nc3 screens BOTH Qa5-e1 and Rc5-c2; Ne4 exposes both rooks. Bxc5 Rxc5 also clears Be3 from Bh6-Rc1.
- Uncastled Rh8/h5: Bh6 Bxh6 Qxh6 Rxh6 loses Q.
- Passers: ...Re2 Rxe2 dxe2, ...Nd3/Re8, e1=Q+ Nxe1 Rxe1+ removes the blockader. Rf2/Ng4/Kf4 against Kh3: Rh2#; verify guards/flights.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - d3 Ruy, bishop tempi and promotion guards.
- notes/caro-kann-advance.md - Break safety, defenders and passers.
- notes/deepseek.md - Caro/Sicilian exchanges and mating coordination.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Benoni screens and defenders.
- notes/ruy-lopez.md - Pawn forks, relative pins and king attacks.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
