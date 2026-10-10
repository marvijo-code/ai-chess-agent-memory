# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before Q/R moves, enumerate enemy pawn/knight captures and trace EVERY bishop ray. Check, attack and pin never establish destination safety.
- Name exact defenders, screens and LEGAL recapturers. Trace recaptures through OWN pawns. Simulate the enemy capture before claiming protection.
- Relative pins permit moves exposing Q/R. Refresh pins after king/pinning-piece moves. One screen can hide TWO targets; trace opened rays to their endpoints.
- Calculate FULL exchanges, including final KING recaptures and losses elsewhere. Attacking Q/R does not force retreat: test checks AND captures of the attacker.
- Track pawn squares and forward AND capture-promotions. Blocked pawns attack diagonally. A defended piece can lose to a cheaper capturer; verify my recapture is legal.
- After EVERY capture, refresh the capturer's attacks and lines vacated by its origin. Trust the board over commentary, wins and sparse marks.
- When forked, compare saving the higher-value piece WITH defending the other target. Before king/Q moves, list guards and screens LOST, including back-rank entries.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical tactics 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Long thinks do not replace reply calculation. Name a target or pawn break before shuffling; shorten routine endgame maneuvers.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Include king recaptures before rook sacrifices. Worse or Black with draw odds: seek activity/repetition.
- Escort passers with king/minors; count races before chasing pawns. Minor endings need a target, entry or break. Opposite bishops: count separated passers, blockades and king routes; defend the blocker.
- Q+R: protected checks, restricted exits, mate before pawns. Forced interposition can enable liquidation. Check stalemate after EVERY quiet move/capture; preserve pawn tempi against an immobilized king.

## Open games as White
- T21 d3 Ruy: ...d5 e5 Ne4 Nc3 Nxc3 bxc3! Nxe5! uncovers Bd7-c6-b5. Rxe5 Bxb5 exchanges N for B. Rxd5?? Qxd5 loses R: OWN d4 blocks Qd1-d5. Assess a safe rook retreat.
- Ng5 g6 Ne4? Qxe4 Qxe4 Rxe4 loses N: Re8 backs Qd5's capture. A fork threat does not prevent capturing its knight.
- Chigorin Nb3/Be3/Nbd2 and central exchanges kept material level. Bb1/e5 clears b1-h7; Qe4-h7 vacates its own screen. ...dxe5 allowed Qh7+ Kf8 Qh8#; no earlier forced win established.
- ...a5 frees a6: d5 Nb4 Bb1 a5 a3 Na6 Nc5 does not trap N. Qc7/Rc8: Bc2?? Qxc2 Qxc2 Rxc2 loses B.

## Black openings
- Caro Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7! Bd3 Bxd3 Qxd3 e6, then Nd7/Ngf6/Be7. h6 supplies h7 AND controls g5.
- T22 Sonnet: long castling, Ne5 Nxe5 Bxe5 O-O, c5 Bxf6 Bxf6! dxc5 Qc7 b4 a5 a3?? axb4 axb4 Ra1#. dxc5 clears d4; b4 clears b2: Bf6 now protects a1/covers b2. Pawn exchanges open Ra8's file. Scan the FINAL recapture board for mate before preserving a pawn chain.
- Caro Advance: Bf5 outside chain, Nd7/Ne7-f5/c5/Be7/O-O; cxd4/Nxd4/Rac8 pressures c3, f6/fxe5 opens f-file. Setup, not forced win.
- T21 h4 h5 Bd3 Bxd3 Qxd3 e6 Nf3 Ne7 Bg5 pins Ne7 to Qd8 via f6. Nf5?? Bxd8 Kxd8 loses Q for B. Resolve the screen before following the plan.
- Qe8 guarded Be7 AND b8. Qf7?? Rb8+ Bf8 pins B to Kg8; Qxf4?? g3xf4 loses Q. Recheck back-rank checks and pawn captures.
- QGD: h6/b6/Bb7/Nbd7/c5, cxd5 exd5; Ne5 Nxe5 Bxe5 Bd6 Bxd6 Qxd6!; dxc5 bxc5. Bf5 attacks Rc8: Rcd8. Bg6?? fxg6 won B; no opening advantage proven.
- ...Nxe4 Nxe4 dxe4 clears d5. Qd5+ Qxd5 wins Q: no White recapturer. ...e3 clears e4; Qxg2# vacates d5 so Bb7 protects g2. Check the FINAL battery, including my queen's screen.

## Recurring geometry
- Dragon ...Nc4 hits Qd2/Bb3: Bxc4 Rxc4. Kb1? Qa5?? Nb3 attacks Q; Rfc8?? Nxa5. Rxc3 Qxc3 Rxc3 bxc3 removes both rooks. Bxf6 Bxf6 removes Bd7's defender before Rxd7.
- Rbg7+ Bxg7 Rxg7+ Kxg7 gives BOTH rooks for B. Qa7/Nd6 cages Kd8: preserve pawn tempi, Ke5-e6 then Qd7#.
- Qd2 guards d5 through empty d3/d4: Nxd5?? Qxd5. d6 screens Rd8 from Qd5. Be4 guards b7; Ba7 attacks Rb8/guards b8: b8=Q Rxb8 Bxb8.
- Italian d4 exd4 cxd4 Nxd4 Nxd4 Qxg5 abandons Bg5, losing a pawn overall. Re5 screens Qf6-a1; Rd5 exposes Ra1. Re1+ Nxe1 Qxf2+ Kh1 Qg1# diverts Nf3/clears Bc5.
- Nxc4 bxc4 Rxc4 gives N for TWO pawns. Rb1+?? Bxb1 follows Bd3-c2-b1. Nxd5?? exd5: Kd6 cannot recapture when Ba2 guards d5.
- Qb6 behind Be3/d4 permits dxe5 to uncover B AND hit Nf6. Qxc8 Rxc8 Rxc8+ Bxc8 leaves Black Q vs R.
- Be7 screens Re8; Nc6 guards e5. Four Knights Nd5 attacks Nc6/Bb4/Nf6: resolve before castling. d4 clears Bc1-f4: Qf4?? Bxf4.
- Benoni Bxc5?? Rxc5 activates Rc5/clears Be3 from Bh6-Rc1. Nc3 screens BOTH Qa5-e1 and Rc5-c2; Ne4 exposes both rooks.
- Qa4 abandons Qd1-f3's recapture; Nxf3+ gxf3 exposes Kg1. Bxb5 attacks Qa4 immediately. c3 blocks Bb2-d4; Rd1 alone cannot stop dxc1=Q.
- Dragon g4 BEFORE h5 permits gxh5 after Nxh5; h5 first leaves g6 guarding Nh5. hxg6 hxg6 clears Rh1-supported Qh7; verify king alternatives. Uncastled Rh8/h5: Bh6 Bxh6 Qxh6 Rxh6 loses Q.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - Clearance, recapture paths and king safety.
- notes/caro-kann-advance.md - Classical a-file mate, queen screens and conversion.
- notes/deepseek.md - Dragon tactics, liquidation and stalemate.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Tartakower, Benoni screens and defenders.
- notes/ruy-lopez.md - Chigorin breaks, batteries and conversion.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
