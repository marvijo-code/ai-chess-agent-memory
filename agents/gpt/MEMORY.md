# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before Q/R moves, enumerate enemy pawn/knight captures and trace EVERY bishop ray. Check, attack and pin never establish destination safety.
- Name exact defenders, screens and LEGAL recapturers; trace through OWN pawns. Simulate the enemy capture before claiming protection.
- Refresh pins after either endpoint moves. Leaving one bishop ray may enter another behind the SAME screen. Relative pins permit moves that lose Q/R.
- Before moving a screen, name BOTH endpoints and exposed targets. Attacking the pinning bishop does not stop it taking my queen.
- Calculate FULL exchanges, including final KING recaptures and losses elsewhere. Attacking Q/R does not force retreat: test checks AND captures of the attacker.
- Track pawn squares and forward AND capture-promotions. Blocked pawns attack diagonally; advancing a supporting pawn can abandon its target. Verify replacement guards on the final board.
- After EVERY capture, refresh the capturer's attacks and lines vacated by its origin. Trust the board over commentary, wins and sparse marks.
- When forked, compare saving the higher-value piece WITH defending the other target. Before king/Q moves, list guards and screens LOST, including back-rank entries.
- Before a fork/discovered attack, test enemy checks FIRST. A centralized knight may be the only screen against a mating rook entry.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical tactics 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Long thinks do not replace reply calculation. Name a target or pawn break before shuffling; shorten routine endgame maneuvers.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition.
- Escort passers; count races before chasing pawns. Minor endings need a target, entry or break. Opposite bishops: count separated passers, blockades and king routes; defend the blocker.
- Use protected checks and restricted exits. Check stalemate after EVERY quiet move/capture; preserve pawn tempi against an immobilized king.

## White openings
- T22 SF2 Sonnet, d3 Ruy: ...Nb4 Bb1 d5 e5!; Qd3 threatens Qh7#, but ...g6! answers it. ...Bxf3 Rxd8 Rxd8 gxf3! preserves Re1's e5 guard. ...Rd5? f4 Nd4 Be4! saves Bc2 with tempo. Bxd4?! Rxd4 Bxb7! permits ...Rb4/Rxb2; no verified better move. Bd5 guards a2: ...Rxa2 Bxa2 wins R. Finish: e6/Rf7+; e7 clears Ba2-f7, replacing the pawn's rook guard; e8=Q#.
- T22 Classical Caro: dxe5 opens d-file; Qxd3 Rxd3 Nd5 attacks Bf4. Rd7?!/Rxb7?!: examine c4 against Nd5 guarding Be7; no best replacement verified. Bf6?! exf6 wins B for P. ...c5 abandons d5: Rxd5. Rh8# needs Bg7 guarding h8/h6, Nf5 guarding Bg7 and h5 barring g6.
- T22 Stockfish: ...Bh5 Qe2 Nc4 Ne5?? Bxe2 Rxe2 loses Q for B. Nf3 still screened Bh5-e2. Answer the attack on Bd2 without exposing Q. Finish: Bf4 Rd8 Nxf7?? Re1#; Ne5 screened Re6-e1. Fork/discovered attack could not answer mate; f2/g2/h2 denied flights.
- T21 d3 Ruy: ...d5 e5 Ne4 Nc3 Nxc3 bxc3! Nxe5! uncovers Bd7-c6-b5. Rxe5 Bxb5 exchanges N for B. Rxd5?? Qxd5 loses R: OWN d4 blocks Qd1-d5. Assess a safe rook retreat.
- Ng5 g6 Ne4? Qxe4 Qxe4 Rxe4 loses N: Re8 backs Qd5's capture. Fork threats do not prevent capturing the knight.
- Chigorin Nb3/Be3/Nbd2 and central exchanges kept material level. Bb1/e5 clears b1-h7; Qe4-h7 vacates its own screen. ...dxe5 allowed Qh7+ Kf8 Qh8#; no earlier forced win established.

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
- notes/berlin-endgame.md - d3 Ruy, bishop tempi and promotion guards.
- notes/caro-kann-advance.md - A-file mate and queen screens.
- notes/deepseek.md - Classical Caro, Dragon liquidation and stalemate.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Benoni screens and defenders.
- notes/ruy-lopez.md - Relative pin, rook mate, Chigorin batteries.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
