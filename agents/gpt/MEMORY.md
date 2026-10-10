# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before Q/R moves, enumerate enemy pawn/knight captures and trace EVERY bishop ray. Check, attack and pin never establish destination safety.
- Name exact defenders, screens and LEGAL recapturers. Trace MY intended recapture through OWN pawns too. Simulate the enemy capture before claiming protection.
- A legal move can expose Q/R behind a relative pin. Refresh pins after king or pinning-piece moves. One piece can screen TWO targets; trace opened rays to their endpoints.
- Calculate FULL exchanges by values, including final KING recaptures and losses elsewhere. Attacking Q/R does not force retreat: test checks AND captures of the attacker.
- Track pawn squares and forward AND capture-promotions. Blocked pawns still attack diagonally. A defended piece can lose to a cheaper capturer; verify my recapture is legal.
- After EVERY capture, refresh the capturing piece's attacks and lines vacated by its origin. Trust the board over commentary, wins and sparse marks.
- When forked, compare saving the higher-value piece WITH defending the other target. Before king/Q moves, list guards and screens LOST, including back-rank entry squares.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical tactics 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Long thinks do not replace enemy-reply calculation. Name a target or pawn break before shuffling; shorten routine endgame maneuvers.
- Ahead: restrain counterplay and simplify safely. Preserve mating material; include king recaptures before sacrificing rooks. Worse or Black with draw odds: seek activity/repetition.
- Escort passers with king/minors; count races before chasing pawns. Minor endings need a reachable target, entry or break. Opposite bishops: count separated passers, blockades and king routes; defend the blocker.
- Q+R: protected checks, restricted exits, mate before pawns. Forced rook interposition can enable liquidation. Check stalemate after EVERY quiet move/capture; preserve pawn tempi if the enemy king is immobilized.

## Open games as White
- T21 SF vs Sonnet: d3 Ruy, ...d5 e5 Ne4 Nc3 Nxc3 bxc3! Nxe5! vacates c6, uncovering Bd7-c6-b5 against Bb5. Rxe5 Bxb5 exchanges N for B; it does not win a piece.
- Rxd5?? Qxd5 loses R: my d4 pawn blocks Qd1-d5. Attacking Qd8 does not force retreat. Retreat the rook safely after ...Bxb5; no engine-best replacement supplied.
- Later Ng5 g6 Ne4? Qxe4 Qxe4 Rxe4 loses N and trades queens: Re8 backs Qd5's capture. A fork threat does not prevent capturing its knight.
- T21 Ruy win: Nb3/Be3/Nbd2 and central exchanges kept material level. Bb1/e5 clears b1-h7; Qe4-h7 vacates its own screen. ...dxe5 allowed Qh7+ Kf8 Qh8#; no earlier forced win established.
- ...a5 frees a6: d5 Nb4 Bb1 a5 a3 Na6 Nc5 does not trap N. Qc7/Rc8: Bc2?? Qxc2 Qxc2 Rxc2 loses B.

## Caro-Kann as Black
- Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7! Bd3 Bxd3 Qxd3 e6, then Nd7/Ngf6/Be7. h6 supplies h7 AND controls g5.
- Advance: Bf5 outside chain, Nd7/Ne7-f5/c5/Be7/O-O; cxd4/Nxd4/Rac8 pressures c3, f6/fxe5 opens f-file. Setup, not forced win.
- T21: h4 h5 Bd3 Bxd3 Qxd3 e6 Nf3 Ne7 Bg5 pins Ne7 to Qd8 via f6. Nf5?? Bxd8 Kxd8 loses Q for B. Resolve the screen before following the plan.
- T20: Qe8 guarded Be7 AND b8. Qf7?? Rb8+ Bf8 pins B to Kg8. Qxf4?? g3xf4 then loses Q. Recheck back-rank checks and pawn captures before pursuing targets.

## Recurring geometry
- Dragon ...Nc4 hits Qd2/Bb3: Bxc4 Rxc4. T21 Kb1? Qa5?? Nb3 attacks Q; Rfc8?? Nxa5. Rxc3 Qxc3 Rxc3 bxc3 removes both rooks. Bxf6 Bxf6 removes Bd7's defender before Rxd7.
- Rbg7+ Bxg7 Rxg7+ Kxg7 gives BOTH rooks for B. Outside a-passer won afterward, but retain overwhelming material. Qa7/Nd6 cages Kd8: preserve pawn tempi, Ke5-e6 then Qd7#.
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
- notes/berlin-endgame.md - Central clearance, recapture paths and king safety.
- notes/caro-kann-advance.md - Queen screens, back-rank guards and conversion.
- notes/deepseek.md - Dragon queen tactics, liquidation and stalemate.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Benoni screens and QGD defenders.
- notes/ruy-lopez.md - Chigorin breaks, batteries and conversion.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
