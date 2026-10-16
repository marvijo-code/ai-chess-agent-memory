# Chess memory

## Move discipline
- START WITH THE ENEMY'S LAST MOVE. On EACH candidate's resulting board inspect checks, captures, forks, promotions and quiet mates. Rejecting one blunder does not validate another. Apply memory before choosing.
- DESTINATION BEFORE PURPOSE: development, defense, check and tempo do not make a square safe. Name the actual legal guard, excluding the mover. Bc6 defended b5 but Nd4xc6 won B; Bd6 guarded c5 but Rd1xd6 won B.
- PAWN DIAGONALS FIRST, then every knight and complete sliding rays, including backward bishops. Refresh BOTH diagonals after pushes and recaptures: a pawn abandons its old capture squares. Include king captures of adjacent pieces.
- TRACE GUARDS THROUGH EVERY SQUARE. Qa5 pinned Nc3 to Ke1, so Be3 did not defend e4. Nf3 does not attack e4; Nc3 does not attack d4. A piece beside K need not be legally protected.
- OWN SCREENS: Nd2 blocks Qd1-d3; Be3 blocks Re1-e4; f7 blocks Rf8-f2. Nf6xe4 opened Bg7-a1, but d5 still blocked Bb7-e4. Clearing one line does not clear another.
- KING MOVES CHANGE GUARDS, PINS AND SCREENS. Ke7 unpinned f5 but blocked Re8-e6. exf5 attacked Re6; Kxe6 was illegal because f5 controlled e6. Kh2 can release g3's pin and restore gxh4 against Qxh4+.
- LAST GUARD: Nc3 screened Qa5-e1; Rd1 guarded Re1. Nxd5 removed the screen; Bd3/Bxd3/Rxd3 moved Re1's last guard. Development can permit Qxe1+. Before moving any sole defender, inspect the abandoned duty.
- PAWN BREAKS: place the enemy capture first. f4 exf4 forked Be3/Ng3 and opened Qd6-f4. f6/exf6 exposed Be6 to Qe2. With Qf3/Rf8, my f-pawn screened MY queen; fxe6 allowed Rxf3.
- CHECKS NEED A CAPTURE SCAN, including king and pawn captures. Verify current battery support. After discovered checks identify the actual checker; capturing the moving piece may leave check unanswered. A checking block must survive the final capture.
- BACKWARD BISHOPS: Bf4 reaches c1 through e3/d2; Bh6 reaches c1 through g5/f4/e3/d2; Bf6 reaches d8 through e7. Sweep the full diagonal before queen or rook landings.
- FINISH THE CAPTURE CHAIN AND RECOUNT BOTH ARMIES. Nc4 Qxc4 Qxc4 Rxc4 lost N. Opponent may STOP exchanging: Qd5 Rxd5 loses Q for R despite support. Sweep the final recapturer's destination and newly opened rays.
- ATTACKS NEED NOT FORCE RETREAT. b3 attacked Rc4 but opened Bf6-a1: Bxa1 bxc4 Bc3 retained extra B. Rdb1 attacked Bb2, but Bxa1 took R. Search captures by the attacked piece AND other pieces.
- REFRESH PINS WHEN ENDPOINTS MOVE. Nd4 Nxd4 cxd4 opens Rxd8+ against Qd8. Kb1 released Rd2; Kf1 released Nd2's pin to Ra2. A pinned rook can capture its pinning queen.
- BEFORE FORKS/TRADES TEST CAPTURES AND CHECKING INTERMEZZOS. Nc3+ Qxc3 Rxd1 Rxd1 lost N. Bxd5 allowed Nd3+ before Qxd5. A double attack is only a candidate: calculate captures of the attacker and exchange order.
- MATE FIRST, including quiet moves and queenless positions. Nxf4 hit Qh5 but allowed Qxh7#; Rxe7 ignored Rh1#. exf6 can win a minor AND support Qxg7#. Luft solves only the mate its flight prevents.
- BACK RANK: a boxed king needs an explicit defense against rook entry. T44 DeepSeek's Rc1 guarded d1; Rxc5 abandoned that duty and allowed Rd1#. Test mate after a capture, not merely whether the capturer survives.
- QUEEN CONTACT NEEDS A LEGAL RECAPTURER. Qb6 Qxb6 lost Q; c7 blocked Qd6-b8 after Rb8 Qxb8+. Qg4 failed to Be6xg4. A counterattack or offered trade does not answer a direct capture until the opponent accepts.
- TRACE VACATED RAYS BEYOND THE FIRST TARGET. e5 uncovered Bf3-a8; Nf5 blocked Bf4-d6. Kb3 screened Rb1-b7; Ka4 allowed Rxb7. After queen trades and pawn recaptures recount remote guards, not just material.
- Validate destination, occupancy and full path before submission. After ONE rejection reconstruct the board and choose a verified legal move; three invalid replies forfeit. Recovery still needs a capture scan. Match blockers, placement and castling before using memory.

## Clock and endings
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below five minutes cap 15; below 90 seconds use 1-3. Budget from the actual starting clock, especially Armageddon White's ten minutes.
- LONG THOUGHT DOES NOT VALIDATE A MOVE. Spend critical time on concrete reply chains, changed guards and flights. T44 Rad8/Nxd4 took 142/79 seconds; the question was d4's remaining guards. Open Ruy Ra7? took 39 seconds. Even 60+10 does not justify routine multi-minute thinks.
- MATERIAL FROM THE BOARD, not comments or previous evaluation. Equal trades preserve deficits. Verified recaptures and conversion need 1-5 seconds unless checks, pawn moves or changed rays alter them. Sparse annotations are not a complete tactical audit.
- Ahead: remove counterplay and simplify safely. Before trades list cheaper capturers, legal recapturers, abandoned guards and the resulting pawn race. Rf4 Bd2xf4 Bxf4 loses the exchange. An offered queen trade has no defensive effect until accepted.
- ROOK DESTINATIONS NEED EXITS. c4 displaced Rb5 to Rb4; Bd2 attacked it while a5 was loose. Pawn support did not prevent displacement or Bxa5. Count pawn kicks and bishop approaches before placing R ahead of enemy pawns.
- KING CAGE BEFORE PAWN COUNTERPLAY. Kf5 with own e5/g5/h5 faced f3/g3 and Bd8. Bishop-supported Rf6# sealed e6/g6 while pawns covered e4/f4/g4. Ra7's blockade did not answer mate. Map all eight exits.
- CONNECTED PASSERS NEED A BREAK AND A LEGAL ESCORT. Astra's Nd4/e3/K blockaded c4/d5 while N collected kingside pawns; remote raids failed. T44 Sonnet: K reached c6 then d7 BEFORE c6-c7, forcing Bxc7/Kxc7. A guarded promotion square can make a bishop blockade temporary.
- PRESERVE THE LAST PAWN'S GUARD. After sacrificing the c-pawn for B, b4 needed protection against Kc4; Bc5 guarded b4 while b4 guarded B. This tied K to the queenside and freed my king to collect h7/g6. Do not rush b5 into Kxb5 or abandon the guard before K can escort it.
- Stop advanced counterplay before remote raids unless a forcing finish is verified. Rb7 controlled d7 while K approached Sonnet's passer. Scan straight AND capture-promotions two advances ahead; include en passant. T44 h8=Q allowed fxg2, but Qh5+ forced Kf4 and Qf5#; that exact mate justified the race, not the extra queen alone.
- CHECKING EXCHANGES REMOVE REMOTE GUARDS. R8f3+ Rxf3 Rxf3+ removed White's only rook and Nb3's sole guard; Rxb3 won N. Supported passers can buy exchanges, but finish the chain: Qc7 Qxc7 dxc7 still faced Bxc7.
- KING ACTIVITY NEEDS LEGAL TARGETS AND ARRIVAL TIMES. Ke4 hit d4 but Kc5 guarded it; d4+ forked Ke5/Bc5. g6-supported Rf7+ drove the sole king guard away before Rxe6 won R. In rook mate approach with K covering flights, use safe waiting moves and check stalemate.

## White openings
- Quiet Sicilian: Be2/O-O/Be3/f4/Kh1, then a4/Bf3/Qe1-g3 suits me; distinguish Dragon/Maroczy and whether cxd4 occurred. Wins depended on errors. Qe1 and automatic Nxc6 after Qxe5 were inaccurate; compare immediate queen exchange.
- GLM omitted cxd4 in T41: d-pawn remained d4, N remained f3. d5/exd5/exd5 attacked Nc6; castling ignored it and dxc6 won N for P. Ndb5 branch: Qb6+ required Kh1; Qxb2 attacked Nc3. Nd5/Nxd5/exd5 hit Be6; d6 screened Rd8-Qd3. Rab1 escaped Bf6-a1 with tempo.
- Taimanov: Bxd4 keeps B active. e5/dxe5/fxe5 opens Rd1 and hits Nf6. Bf6 exf6 can win B and support mate. Bg3's retreat opened g3-f4-e5-d6-c7: Bxc7 won Q. T43 Bf3/Qd1 attacked d5, guarded only by Qc5; b5 cleared d5-c6-b7-a8 and Qxd5/Qxa8 won material. Flag win establishes no forced opening edge.
- MAROCZY vs Qa5: f3 guards e4 while Nc3 is pinned; Qxd4! after Nxd4. Ng4 can hit Be3 AND uncover Bg7 against Qd4. b3/Bf2 can uncover Qa5-c3. Long castling: Nxd5 or Bd3/Bxd3/Rxd3 abandons e1 defenses. Short castling: exchanges can enable Bd4+ against Kg1/Ra1 with b2 empty.
- SF MAROCZY: Bxc4 allowed Qc5+ Kh1 Qxc4, exposing Rf1 through d3/e2; Bc1 blocked Ra1-f1 and b3 allowed Qxf1#. T44 Nd5's double attack failed to Qxd2 and the ensuing liquidation. exd5 was correct but d6/e7 meant d5 was NOT passed. Be3's bishop trade led to a worse rook ending; no verified replacement.
- T43 MAROCZY: Qb5/Bc4/b3 needed a queen-exit scan before Rfd1; a6 trapped Q behind my Bc4. Qa4 Qxa4 bxa4 removed BOTH Bc4 guards, permitting Rxc4. Before doubling behind a passer, name how to remove its blockader. T44 Rd8 aligned Kd4/Rd8: e5+ fxe5 Rd1+ then Rxd8 lost R to a checking skewer.
- DRAGON: with Black uncastled, h5 vacates h7 and opens Rh8-h6. Bh6 Bxh6 attacks Qd2 through g5/f4/e3; Qxh6 loses Q to Rxh6. Long-castled g4 liquidated my f/g/h pawns for Black's h-pawn. Short-castled Bb3/Nxe3/fxe3 concedes bishop pair; Bg4 hits Qe2 through f3. Nxf3+ needed gxf3, Bh3 needed Rfe1, Bxc3 needed bxc3. Qh4/Rd3 allowed Rc5-h5; Qxa5 ignored Qg4+ and mate.
- CLOSED RUY: Qxf3 abandons d5; exd5 can expose Rxe1+ with Bb1/Bc1 blocking Ra1. Bf4 permits Bxe4 with tempo on Qf3. Nf1 restores Qd1-d4; Qf3 abandons b3. Nxd4/Qxd4 can lose loose Bc2 on cleared Qc7-c2. f6 hits Re7 AND opens Bc2-h7: compare mate before grabbing.
- ZAITSEV: g6/Qd6 guards f4 after exf4; avoid f4 with Be3/Ng3. h4-h5 induced g5 and freed Nf5 with tempo, but g4/f3 were mistakes. Distinguish Nb4/c5/d5/Nd7 from Nb8.
- RUY d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by g6. Before g3/h4 calculate f5/fxe4 and queen entry. T41 Berlin exd4/cxd4/d5 needed e5!, not familiar Nf1. Nxg3 hxg3 opened h-file; Bf4/Bd3/Qxd3 and Re3-h3 plus g4-g5 built mate. hxg5 cleared Rh3-h7 for Qh7#.
- T44 OPEN RUY vs Sonnet: after Nxe4 use d4, Bb3, dxe5, Nbd2/c3/Bc2. Against d4 and Nxb3, axb3! opened Ra1's file. bxc3?! allowed Qxd1!; no verified better recapture supplied. Rad8 left a6 loose, but Rxa6/Nb8 Ra7? was marked a mistake; Nc6? then permitted Rxc7. Do not treat the two-pawn gain as forced. After Rxd1+, Bxd1! retained material; safe rook trades led to a two-pawn-up bishop ending. Nc6 screened Bd7-b5 until Nxe5 vacated it: Nxb5/Nxe5/Bxe5/Bxb5 traded knights, preserving two extra pawns.
- CLASSICAL CARO: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and hits Nf6. Nd7 permits Qxd7 Qxd7 Rxd7, winning N; Bf6 exf6 wins B for P. Be1 guards Ng3 through f2.

## Black openings
- FOUR KNIGHTS: castle before Nd5. Nxd5/exd5/e4/dxc6/exf3/Qxf3/dxc6 leaves equal material. Against Bc4/d4, Bd6/Qh4 threatens Qxh2#; g3 allowed Qxd4!, gaining P with tempo. Actual branch, not a forced win against every reply.
- T41 FOUR KNIGHTS: Be6/Bxe6/fxe6 opened f-file, but Qb3/Qd5/Qxb7 restored equal pawns despite rook tempos. With Rd1 pressuring d5, e5?! abandoned its pawn guard: Qxd5+ cxd5 Rxd5 left P down. Bd6 later guarded c5 but stood undefended on Rd1's file. No verified replacements.
- FOUR KNIGHTS QUEENLESS: Rae8/Be6/Rxe6 and Rfe8/f5/g6/c5 reached near equality. Re6/Re8 do not guard f5; g6 does. Kf7 blocks Rf8-f5; Ke7 blocks Re8-e6. Kg7 unpinned f5 but gxf5 gxf5 Rxf5 lost P. Kh8 entered Bc3-h8's cage; Rd5# discovered bishop check. Former bishop support does not validate Rxh2+ after B has moved.
- ITALIAN vs DeepSeek: Bc5/Nf6/O-O/d6/a6/Ba7 usable. Bg4-h5-g6 avoids Be6 screening Re8-e5. Qe7/e4 gained P, but Qd5 lost Q to Nf6xd5. T41 Qd7/Nf6 inaccurate despite winning; no verified repairs.
- ITALIAN CLEARANCE: Be6 screens Re8-e4. T40 Nxe4?! allowed Rxe4!; Bxb3! cleared file AND attacked Qd1. T42 Nxe4?? allowed Nxe4!; Bxb3 did NOT attack Qd2, and Ne4 had Nf6+ against Kg8/Qd7/Re8. axb3?? allowed Rxe4. Match queen placement; wins followed gifts.
- T44 ITALIAN: after Bxe6/fxe6 and Bxe3/Rxe3, d5/dxe4 and central exchanges activated my pieces. Ne5?! removed Nf3's defense of d4; Qd1 alone could not withstand Nc6/Qd5. Nxd4 won P but did NOT attack Re3. Nxf3+ led to Qxf3!, resolving queen contact and retaining the pawn. White could recapture Rxf3; doubled pawns were not forced. Rd2 invaded, b5 saved b7, and c5 tempted Rxc5, abandoning d1 to Rd1#. No forced opening advantage established.
- ENGLISH vs GLM: e5/Nf6/Nc6/d5/cxd5/Nxd5, then Nb6/Be7/O-O/Be6/Qd7/Rad8 active. White's c-pawn was gone: not a Maroczy. Nxd4/Qxd4 lost Q on open Qd8-d4. Distinguish e4 before Bg2 from d3.
- CHIGORIN: Na5/c5/Qc7, central exchanges/Nc6, a5-a4/Bd7/Rfc8. Rc1/Bb1 pins Nc6: move Q off c7 BEFORE d5. Na5/Be6 allowed supported Bxb5/Bxa4. T40 SF Na5/Nc4/Rxc4 inaccurate; b5 support did not justify Bd3 attacking R. Qxe4! after Bxe4 retained equality.
- SONNET RUY: T41 Nxe4/Rxe4 lost B for P because d5 still blocked Bb7-e4. T42 Breyer Nb8-d7/Bb7/Re8/Bf8/g6/Bg7, then c5/d5/c4/Nc5; b4 displaced N to a4. Bxa4 required bxa4!, but Rc7/Rec8 did not retain c4/a4: TWO pawns down. Bc8-d7-b5 gained a queen tempo; h5/Kh7 enabled protected Bh6, skewering Qe3/Rc1. Qxf3 FIRST, then Bxc1; collecting R first allowed Qxf6. Recovery does not justify pawn concessions.
- ASTRA RUY: Qb7 released Nc6; Bd8-b6/Na5-c4 reached equality before Qb6 hung Q. Zaitsev exd4/Nb4/c5/Nd7/f5 gave activity; N7f6/d5 inaccurate. Queen exchange left bishop pair plus P, then unsupported Bc6 lost B.
- RUY d3: Re8/Bb7/Bf8, central d5 exchange, f5/Qd7/g6. Nxe3 Qxe3 permits f4 forking Q/Ng3; fxe3 avoids it. Move Q off Rd1's file BEFORE e4 dxe4. SF 6.d4: exd4/Nd5/Nxd4, Nb6/Nxa4, d6/Bxd6/Be6 near equal; against Rad1/Bxd6, cxd6 retained d6 while Qe7 lost it. Qb6 permits dxe5 uncovering Be3-b6.
- CARO: Classical h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O; c5 d5 against O-O/c4/Rfe1 adverse. Advance f6 Nf4/Qd6 exd6 repeatedly loses Q. Earlier f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3. Queenless f6/Rxf6/Ne5 differs: dxe5 clears Be3-b6 while hitting Rf6.
- QGD: Bxf3 Qxf3 removes Nf3 and Qd1's d4 guard, permitting Nxd4. Nb4 clears Rc8-c4 AND Bb7-f3; Qe2 Bxf3 Qxf3 abandons c4, gxf3 retains its guard. Bd6 loses B if d4 blocks Rd1-d6. IQP Nbd7/dxc4/c5/cxd4/b6/Bb7/Rc8 developed smoothly; Nd5/Bxd5 retained e6. h6/Qc7/Rfd8 adverse despite winning.

## Opponents
- SF19: takes loose material; exploits pins, king screens, deflected defenders, trapped queens and checking skewers. No reliance on repetition or offered queen trades. Its queen can finish while chased by a pawn.
- Astra: coordinated Closed Ruy bishops/knight; takes unsupported Q/B. Nd4/e3/K blockaded my passers while N collected kingside pawns and g-pawn promoted.
- Sonnet: exploits blocked recaptures, clearance, pawn forks and back-rank mate. Can miss bishop skewers, checking trades removing remote guards, and king-supported passer breakthroughs. T44 Open Ruy offered sound queen exchange but Nb8/Nc6 replies conceded pawns; later sent K away while B alone stopped my c-pawn. Still seek its active king and promotion counterplay. One illegal king move; several 60-120-second thinks did not improve defense.
- DeepSeek: takes loose pieces and necessary recaptures, but misses changed guards, checking intermezzos and mate. T44 Ne5 conceded d4; Rxc5 ignored Rd1# after eight minutes of thought. Derive material, attacks and legal recapturers independently of its claims.
- GLM: English g3/e4 or d3; Sicilian as Black. Can omit recaptures, ignore central attacks or lose Q on files/bishop rays. T43 grabbed exposed Ra8, then doubled rooks stripped its blockade. Flagged in 60+10 after repeated multi-minute thinks. Its errors do not validate my opening.
- Fable: missed Qxc2 after central exchanges; Qc1+ ignored Bf4-c1, then Nd5 hung N. Can still find back-rank swindles from lost positions.

## Note files
- notes/accelerated-dragon.md - Uncastled h-rook trap, pawn captures, pinned blocks and king exposure.
- notes/berlin-endgame.md - D-file, clearance and English capture chains.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Italian rook screens, capture chains and conversion.
- notes/four-knights.md - Pawn-winning setup, queen exchanges, king screens and mating cages.
- notes/qgd-exchange.md - IQP blockades, capture chains, clearance and mate.
- notes/ruy-lopez.md - Bishop paths, rook captures, h-file attacks and back-rank mate.
- notes/sicilian-maroczy.md - Central pressure, remote rook targets, mating batteries and passers.
