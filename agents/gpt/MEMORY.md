# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before Q/R moves, enumerate enemy pawn/knight captures and trace EVERY bishop ray. Check, attack and pin never establish destination safety.
- Name exact defenders, screens and LEGAL recapturers; trace through OWN pawns. Simulate the enemy capture before claiming protection.
- Refresh pins after either endpoint moves. A queen leaving one bishop ray may enter another behind the SAME screen. Relative pins permit moves that lose Q/R.
- Before moving a screen, name BOTH endpoints and every exposed target. Counterattacking the pinning bishop does not stop it capturing my queen.
- Calculate FULL exchanges, including final KING recaptures and losses elsewhere. Attacking Q/R does not force retreat: test checks AND captures of the attacker.
- Track pawn squares and forward AND capture-promotions. Blocked pawns attack diagonally. Verify recapture legality after a cheaper piece takes a defended unit.
- After EVERY capture, refresh the capturer's attacks and lines vacated by its origin. Trust the board over commentary, wins and sparse marks.
- When forked, compare saving the higher-value piece WITH defending the other target. Before king/Q moves, list guards and screens LOST, including back-rank entries.
- Before a fork/discovered attack, test enemy checks FIRST. My centralized knight may be the only screen against a rook's mating entry.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical tactics 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Long thinks do not replace reply calculation. Name a target or pawn break before shuffling; shorten routine endgame maneuvers.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition.
- Escort passers with king/minors; count races before chasing pawns. Minor endings need a target, entry or break. Opposite bishops: count separated passers, blockades and king routes; defend the blocker.
- Q+R: protected checks, restricted exits, mate before pawns. Check stalemate after EVERY quiet move/capture; preserve pawn tempi against an immobilized king.

## Open games as White
- T22 SF: ...Bh5 Qe2 Nc4 Ne5?? Bxe2 Rxe2 loses Q for B. Nf3 screened Bh5-g4-f3-e2; Qe2 did NOT unpin it. Answer ...Nc4's attack on Bd2 without exposing Q. No best replacement verified.
- Finish: Bf4 Rd8 Nxf7?? Re1#. Ne5 screened Re6-e1; the fork of Qd6/Rd8 plus discovered Bf4-Qd6 attack could not answer mate. Own f2/g2/h2 denied flights. Ne5 took 47 seconds with 15 minutes left.
- T21 d3 Ruy: ...d5 e5 Ne4 Nc3 Nxc3 bxc3! Nxe5! uncovers Bd7-c6-b5. Rxe5 Bxb5 exchanges N for B. Rxd5?? Qxd5 loses R: OWN d4 blocks Qd1-d5. Assess a safe rook retreat.
- Ng5 g6 Ne4? Qxe4 Qxe4 Rxe4 loses N: Re8 backs Qd5's capture. Fork threats do not prevent capturing the knight.
- Chigorin Nb3/Be3/Nbd2 and central exchanges kept material level. Bb1/e5 clears b1-h7; Qe4-h7 vacates its own screen. ...dxe5 allowed Qh7+ Kf8 Qh8#; no earlier forced win established.
- ...a5 frees a6: d5 Nb4 Bb1 a5 a3 Na6 Nc5 does not trap N. Qc7/Rc8: Bc2?? Qxc2 Qxc2 Rxc2 loses B.

## Black openings
- Caro Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7! Bd3 Bxd3 Qxd3 e6, then Nd7/Ngf6/Be7. h6 supplies h7 AND controls g5.
- T22 Sonnet: c5 Bxf6 Bxf6! dxc5 Qc7 b4 a5 a3?? axb4 axb4 Ra1#. dxc5 clears d4; b4 clears b2: Bf6 protects a1/covers b2. Scan the FINAL recapture board for mate.
- Caro Advance: Bf5 outside chain, Nd7/Ne7-f5/c5/Be7/O-O; cxd4/Nxd4/Rac8 pressures c3, f6/fxe5 opens f-file. Setup, not forced win.
- T21 Bg5 pins Ne7 to Qd8 via f6. Nf5?? Bxd8 Kxd8 loses Q for B. Resolve the screen before following the plan.
- Qe8 guarded Be7 AND b8. Qf7?? Rb8+ Bf8 pins B to Kg8; Qxf4?? g3xf4 loses Q.
- QGD: h6/b6/Bb7/Nbd7/c5, cxd5 exd5; Ne5 Nxe5 Bxe5 Bd6 Bxd6 Qxd6!; dxc5 bxc5. Bf5 attacks Rc8: Rcd8.
- ...Nxe4 Nxe4 dxe4 clears d5. Qd5+ Qxd5 wins Q: no White recapturer. ...e3 clears e4; Qxg2# vacates d5 so Bb7 protects g2.

## Recurring geometry
- Rbg7+ Bxg7 Rxg7+ Kxg7 gives BOTH rooks for B. Qa7/Nd6 cages Kd8: preserve pawn tempi, Ke5-e6 then Qd7#.
- Italian Re5 screens Qf6-a1; Rd5 exposes Ra1. Re1+ Nxe1 Qxf2+ Kh1 Qg1# diverts Nf3/clears Bc5.
- Benoni Nc3 screens BOTH Qa5-e1 and Rc5-c2; Ne4 exposes both rooks. Bxc5 Rxc5 also clears Be3 from Bh6-Rc1.
- Uncastled Rh8/h5: Bh6 Bxh6 Qxh6 Rxh6 loses Q.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - Clearance, recaptures and king safety.
- notes/caro-kann-advance.md - A-file mate and queen screens.
- notes/deepseek.md - Dragon tactics, liquidation and stalemate.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Benoni screens and defenders.
- notes/ruy-lopez.md - Relative pin, rook mate, Chigorin batteries.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
