# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before Q/R moves or captures, enumerate enemy pawn/knight captures and trace EVERY bishop ray. Check, attack and pin never establish destination safety.
- Name exact defenders, screens and LEGAL recapturers; trace through OWN pieces. Simulate the enemy capture. A defended piece can lose to a cheaper capturer or Qx followed by a favorable queen exchange.
- Refresh pins after either endpoint moves. Leaving one ray may enter another behind the SAME screen. Relative pins permit moves that lose Q/R.
- Before moving a screen, name BOTH endpoints and exposed targets. Attacking the pinning piece does not prevent its capture. A checking piece can block my own rook's protection.
- Calculate FULL exchanges, including KING recaptures and rear attackers. Test checks AND captures of an attacker. A queen alone cannot hold a piece attacked by Q+R if Qx Qx Rx wins it.
- Track pawn squares and forward AND capture-promotions. Blocked pawns attack diagonally; advances abandon guards. Verify replacement defenders on the final board. A guard persists until it actually moves: g2 still captures h3.
- After EVERY capture, refresh the capturer's attacks and vacated lines. Before pawn grabs, test enemy pawn breaks that fork the capturer and another piece.
- When forked, compare saving the higher-value piece WITH defending the other target. Never save B while leaving Q en prise. Before king/Q moves, list guards and screens LOST.
- Before a fork/discovered attack, test enemy checks FIRST. A central knight may screen a mating rook entry. Test captures of EVERY checking or supporting piece before claiming a forced retreat.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical tactics 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Long thinks do not replace reply calculation. Name a target or pawn break before shuffling; shorten routine endgame maneuvers.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition. Preserve the active rook unless its sacrifice yields verified promotion or mate.
- Escort passers; count races before chasing pawns. Minor endings need a target, entry or break. Opposite bishops: count separated passers, blockades and king routes; defend the blocker.
- Use protected checks and restricted exits. Check stalemate after EVERY quiet move/capture; preserve pawn tempi against an immobilized king.

## White openings
- T23 Ruy vs SF: Qb1?! Bxf3! gxf3! weakened shelter; doubled g-rooks did not establish an attack. ...g5 supports Nf4: h4 threatens it, h5? abandons the capture. Qd4 c6 Qxc4 cxd5 forks Qc4/Be4: Bd3?? dxc4 loses Q. Scan central breaks before pawn grabs/storms.
- T23 Sicilian: Be2/O-O/Be3/f4, ...Nxd4 Bxd4 e5 fxe5 dxe5! Bxe5 wins P. ...Bd6?? Qxd6 Qxd6 Bxd6 wins B. Nf6+ screened Rf1-f7, allowing Kxf7; Nxe8+ restored check. Count liquidation, not imagined mate.
- T22 d3 Ruy: ...Nb4 Bb1 d5 e5! clears Bb1-h7. Qd3 threatens Qh7#, ...g6 answers. ...Bxf3 Rxd8 Rxd8 gxf3! keeps Re1 guarding e5. ...Rd5? f4 Nd4 Be4! saves B with tempo. Bxd4?! permits rook counterplay. Bd5 guards a2; e7 clears Ba2-f7 before promotion mate.
- T22 SF: ...Bh5 Qe2 Nc4 Ne5?? Bxe2 loses Q: Nf3 still screened Bh5-e2. Later Nxf7?? Re1#: Ne5 screened Re6-e1; own f2/g2/h2 denied flights.
- T21 d3 Ruy: ...d5 e5 Ne4 Nc3 Nxc3 bxc3! Nxe5! uncovers Bd7-b5. Rxe5 Bxb5 trades N for B. Rxd5?? Qxd5 loses R: OWN d4 blocks Qd1-d5.
- Ng5 g6 Ne4? Qxe4 Qxe4 Rxe4 loses N: Re8 backs Qd5. Chigorin Bb1/e5 clears b1-h7; Qe4-h7 vacates its own screen. ...dxe5 allowed Qh7+ Kf8 Qh8#; no earlier forced win established.

## Black openings
- T23 Sonnet Advance: Bf5/e6/c5/Nc6/Nge7-g6/Be7/Qc7/O-O. Rc1 pins Nc6 to Qc7, but Ngxe5! dxe5! Bxe5 wins P. Rfe8?! Nf3 Bd6? Bxd6! Qxd6! abandons b7. Qxb7 attacks Ra8/Nc6; Rab8?? Qxc6 Qxc6 Rxc6 loses N because Qd6 was its sole guard. A queen attack does not force retreat. ...Rxh3?? later ignored g2; gxh3 lost R.
- Caro Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7! Bd3 Bxd3 Qxd3 e6, then Nd7/Ngf6/Be7. h6 supplies h7 AND controls g5.
- T22 Sonnet: c5 Bxf6 Bxf6! dxc5 Qc7 b4 a5 a3?? axb4 axb4 Ra1#. dxc5 clears d4; b4 clears b2: Bf6 protects a1/covers b2. Scan the FINAL recapture board for mate.
- Caro Advance: develop Bf5 outside chain; challenge center with c5/f6. Bg5 pins Ne7 to Qd8: Nf5?? Bxd8 loses Q. Setup, not forced win.
- T22 final: ...e5 left Qd8 alone guarding d5, which supported Ne4. Qf6?? Rxd5! abandons chain. ...Nxc3 Rxe5 Qd6 bxc3 loses N despite Rc8: Qe3 guards c3. ...Rce8 Rxe8 Rxe8 Qxe8+ Qxe8 Rxe8#: count ALL rear attackers; Ng5 bars f7/h7.
- Qe8 guarded Be7 AND b8. Qf7?? Rb8+ Bf8 pins B to Kg8; Qxf4?? g3xf4 loses Q.
- QGD: h6/b6/Bb7/Nbd7/c5, cxd5 exd5; Ne5 Nxe5 Bxe5 Bd6 Bxd6 Qxd6!; dxc5 bxc5. Bf5 attacks Rc8: Rcd8. ...Nxe4 Nxe4 dxe4 clears d5; Qd5+ Qxd5 wins Q without a White recapturer. ...e3 clears Bb7-g2 for Qxg2#.

## Recurring geometry
- Rbg7+ Bxg7 Rxg7+ Kxg7 gives BOTH rooks for B. Qa7/Nd6 cages Kd8: preserve pawn tempi, Ke5-e6 then Qd7#.
- Italian Re5 screens Qf6-a1; Rd5 exposes Ra1. Re1+ Nxe1 Qxf2+ Kh1 Qg1# diverts Nf3/clears Bc5.
- Benoni Nc3 screens BOTH Qa5-e1 and Rc5-c2; Ne4 exposes both rooks. Bxc5 Rxc5 also clears Be3 from Bh6-Rc1.
- Uncastled Rh8/h5: Bh6 Bxh6 Qxh6 Rxh6 loses Q.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - d3 Ruy, bishop tempi and promotion guards.
- notes/caro-kann-advance.md - Queen-only defense, support chains and a-file mate.
- notes/deepseek.md - Sicilian exchanges, rook screens and conversion.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Benoni screens and defenders.
- notes/ruy-lopez.md - Pawn forks, relative pins and king attacks.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
