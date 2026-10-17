# Chess memory

## Move discipline
- START WITH THE ENEMY'S LAST MOVE. On each candidate's resulting board inspect checks, captures, forks, promotions and quiet mates. Rejecting one blunder does not validate another. Apply memory before choosing.
- DESTINATION BEFORE PURPOSE: development, defense, check and tempo do not make a square safe. Name the actual legal guard, excluding the mover. Bc6 defended b5 but Nd4xc6 won B; Bd6 guarded c5 but Rd1xd6 won B.
- PAWN DIAGONALS FIRST, then every knight and complete sliding rays, including backward bishops. Refresh attacks after pushes and recaptures. Include king captures. Ng4 into h5xg4 loses N for P even after hxg4.
- CHECKS NEED A CAPTURE SCAN. Qxf2+?? allowed Kxf2 because f7 blocked Rf8-f2. Identify captures of the checker before imagining retreats. A future threat supplies no present support.
- TRACE LEGAL GUARDS THROUGH EVERY SQUARE. Nd2 blocks Qd1-d3; Be3 blocks Re1-e4; f7 blocks Rf8-f2. Clearing one line does not clear another. Qa5 pins Nc3 to Ke1, so Be3 may not defend e4. Nc3 does not guard d4.
- KING MOVES CHANGE GUARDS, PINS AND SCREENS. Ke7 unpinned f5 but blocked Re8-e6. Kxe6 was illegal with White pawn f5. Kh2 can release g3's pin and restore gxh4 against Qxh4+.
- LAST GUARD: inspect the mover's abandoned duty. Nc3 screened Qa5-e1; Nxd5 removed that screen. Bd3/Bxd3/Rxd3 abandoned Re1. DeepSeek's Rxc5 abandoned d1 and allowed Rd1#.
- PAWN BREAKS: place the enemy capture first, including en passant. f4 exf4 forked Be3/Ng3; f6/exf6 exposed Be6 to Qe2. With Qf3/Rf8, my f-pawn screened MY queen; fxe6 allowed Rxf3.
- BACKWARD BISHOPS: sweep the full diagonal before Q/R landings. Bf4 and Bh6 reach c1 through e3/d2; Bf6 reaches d8 through e7.
- FINISH THE CAPTURE CHAIN AND RECOUNT BOTH ARMIES. Nc4 Qxc4 Qxc4 Rxc4 lost N. Opponent may stop exchanging. Include the king as final recapturer; support alone does not make R-for-B or R-for-P acceptable.
- ATTACKS NEED NOT FORCE RETREAT. b3 attacked Rc4 but opened Bf6-a1: Bxa1 bxc4 Bc3 retained extra B. Search captures by the attacked piece and other pieces before assuming a tempo.
- REFRESH PINS WHEN ENDPOINTS MOVE. Nxd4/cxd4 can open Rxd8+ against Qd8. Kb1 released Rd2; Kf1 released Nd2's pin to Ra2. A pinned rook can capture its pinning queen.
- BEFORE FORKS/TRADES TEST CAPTURES AND CHECKING INTERMEZZOS. Nc3+ Qxc3 Rxd1 Rxd1 lost N. Bxd5 allowed Nd3+ before Qxd5. A double attack needs exchange-order calculation.
- MATE FIRST, including quiet moves and queenless positions. Nxf4 hit Qh5 but allowed Qxh7#; Rxe7 ignored Rh1#. exf6 can win a minor AND support Qxg7#. Luft solves only the mate its flight prevents.
- QUEEN CONTACT NEEDS A LEGAL RECAPTURER. Qb6 Qxb6 lost Q; c7 blocked Qd6-b8 after Rb8 Qxb8+. Qe7 lost to Qb7xe7 while e4 blocked Re1-e7. An offered trade has no defensive effect until accepted.
- TRACE VACATED RAYS BEYOND THE FIRST TARGET. e5 uncovered Bf3-a8; Nf5 blocked Bf4-d6. Kb3 screened Rb1-b7; Ka4 allowed Rxb7. After trades and pawn recaptures recount remote guards.
- Validate destination, occupancy and full path before submission. After one rejection reconstruct the board and choose a verified legal move; three invalid replies forfeit. Recovery still needs a capture scan. Match blockers and castling before importing tactics.

## Clock, defense and endings
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below five minutes cap 15; below 90 seconds use 1-3. Budget from the starting clock, especially Armageddon White's ten minutes.
- LONG THOUGHT DOES NOT VALIDATE A MOVE. Spend critical time on concrete replies, changed guards and flights. Qxf2+ took 45 seconds yet omitted Kxf2. T45 Final Qb2? took 82 seconds; finished 48:37 with zero invalid. Time shortage was not the cause.
- MATERIAL FROM THE BOARD, not comments or previous evaluation. Equal trades preserve deficits. Verified recaptures need 1-5 seconds unless checks, pawn moves or changed rays alter them. Sparse marks are not a complete audit.
- Ahead: remove counterplay and simplify safely. Before trades list cheaper capturers, legal recapturers, abandoned guards and the pawn race. Rf4 Bd2xf4 Bxf4 loses the exchange. A later opponent blunder does not validate my earlier break.
- SUPPORT IS NOT A SAFE EXCHANGE. T45 Final Rf7 guarded Rf3, but White's Kg2 approached: Rxf3 Rxf3 Kxf3 lost two rooks for one. A king can wait behind the first capturer. Calculate the last capture before invading or maintaining a rook on the third rank.
- EXCHANGES CAN REMOVE ANOTHER ROOK'S GUARD. h5 guarded Rg4 while Rg6 guarded Rg2. R6g4? Rxg4 hxg4 removed BOTH guards and allowed Kxg2. Calculate every unit's safety after the pawn recapture.
- ROOK DESTINATIONS NEED EXITS. c4 displaced Rb5 to Rb4; Bd2 attacked it while a5 was loose. Pawn support did not prevent displacement or Bxa5. Count pawn kicks and bishop approaches before placing R ahead of enemy pawns.
- KING CAGE BEFORE PAWN COUNTERPLAY. Rb2?? cleared a2 but ignored Kg3/Rh5#. Rb3+ met f3!, and Rxf3+ Kxf3 surrendered R without stopping mate. Checks can be blocked rather than forcing K away.
- QUEEN RAIDS NEED A RETURN ROUTE AND A KING AUDIT. T45 Final h4/Qxh4/Qb2? sent Q away from my king; Qe4 attacked Rf5 and R5f6?! did not repair the position. Compare defense or liquidation before chasing a2/c2. No verified best replacement supplied; Qe4 itself was marked inaccurate.
- PASSERS NEED A BREAK AND A LEGAL ESCORT. Astra's Nd4/e3/K blockaded c4/d5 while N collected kingside pawns. Against Sonnet, K reached d7 before c6-c7, forcing Bxc7/Kxc7. Do not push into a blockade without a way to remove it.
- PRESERVE THE LAST PAWN'S GUARD. Bc5 and b4 protected each other, tying enemy K to the queenside while my king collected h7/g6. Do not rush b5 into Kxb5 or leave before K can escort it.
- STOP ADVANCED COUNTERPLAY before remote raids unless a forcing finish is verified. Scan straight/capture-promotions two advances ahead and include en passant. Finish passer exchanges: Qc7 Qxc7 dxc7 can still face Bxc7.
- CHECKING EXCHANGES REMOVE REMOTE GUARDS. R8f3+ Rxf3 Rxf3+ removed White's only rook and Nb3's sole guard; Rxb3 won N. Inspect unrelated targets after each exchange.
- KING ACTIVITY NEEDS TARGETS AND ARRIVAL TIMES. Ke4 hit d4 but Kc5 guarded it; d4+ forked Ke5/Bc5. Supported Rf7+ drove the sole king guard away before Rxe6. In rook mate keep cutoff, approach with K and check stalemate.
- ROOK BEHIND PASSER: check its ENTIRE file after K moves. Rd4 supported d6/d7; Kd5 screened it. Kc6 cleared the file, so after Rb8+ the rook still protected d8=Q+: Kxd8 was illegal.
- EN PASSANT CAN OPEN A KING ROUTE. Against Ke6 and f5+, exf6 e.p./Kxf6 displaced the blockader and enabled Kd5. Assess king access and rook support, not just which pawn becomes passed.
- A CLOCK LEAD NEEDS MATING MATERIAL. GLM returned Q and lost N, repairing my queen loss without validating it. I later lost both rooks and all pawns; its flag drew against my bare king.

## White openings
- Quiet Sicilian: Be2/O-O/Be3/f4/Kh1, then a4/Bf3/Qe1-g3 suits me. Distinguish Dragon/Maroczy and whether cxd4 occurred. Wins depended on errors. Compare immediate queen exchange before automatic Nxc6 after Qxe5.
- GLM omitted cxd4: d-pawn remained d4, N remained f3. d5/exd5/exd5 attacked Nc6; castling ignored dxc6. Qb6+ required Kh1; Qxb2 attacked Nc3. Nd5/Nxd5/exd5 hit Be6; d6 screened Rd8-Qd3.
- TAIMANOV: Bxd4 keeps B active. e5/dxe5/fxe5 opens Rd1 and hits Nf6. Bf6 exf6 can win B and support mate. Bf3/Qd1 attacked d5 against Qc5 alone; b5 cleared the ray to a8 and Qxd5/Qxa8 won material. A flag win establishes no forced edge.
- SCHEVENINGEN vs GLM: Qb6 stood behind Nd4 on Be3's diagonal, but Nb3?? was also a blunder. Clearing an attack does not prove the retreat sound: calculate forcing replies. Black's e5?? allowed Bxb6. Later c7 captured Rb8 by promotion; do not count only straight promotions.
- MAROCZY vs Qa5: f3 guards e4 while Nc3 is pinned; Qxd4! after Nxd4. Ng4 hits Be3 AND uncovers Bg7 against Qd4. b3/Bf2 can uncover Qa5-c3. Long castling: Nxd5 or Bd3/Bxd3/Rxd3 can abandon e1 defenses.
- SF MAROCZY: Bxc4 allowed Qc5+ Kh1 Qxc4, exposing Rf1 through d3/e2; Bc1 blocked Ra1-f1 and b3 allowed Qxf1#. Nd5's double attack failed to Qxd2 and liquidation. d6/e7 meant my d5 was NOT passed. Be3's bishop trade led to a worse rook ending.
- MAROCZY HEAVY PIECES: Qb5/Bc4/b3 needed a queen exit before Rfd1; a6 trapped Q behind Bc4. Qa4 Qxa4 bxa4 removed BOTH Bc4 guards, allowing Rxc4. Rd8 aligned Kd4/Rd8: e5+ fxe5 Rd1+ then Rxd8 lost R to a skewer.
- DRAGON: Black uncastled plus h5 opens Rh8-h6. Bh6 Bxh6 attacks Qd2 through g5/f4/e3; Qxh6 loses Q to Rxh6. Long-castled g4 liquidated f/g/h pawns for h-pawn. Short-castled Bb3/Nxe3/fxe3 concedes bishop pair; Bg4 hits Qe2. Qxa5 ignored Qg4+ and mate.
- CLOSED RUY: Qxf3 abandons d5; exd5 can expose Rxe1+ with Bb1/Bc1 blocking Ra1. Bf4 permits Bxe4 with tempo on Qf3. Nf1 restores Qd1-d4; Qf3 abandons b3. Nxd4/Qxd4 can lose loose Bc2 on cleared Qc7-c2. f6 hits Re7 AND opens Bc2-h7: compare mate before grabbing.
- CHIGORIN vs Sonnet: Nb3/Be3/Nbd2/Rc1/Bb1/Nf1-g3 developed smoothly. Qb7 released Nc6; d5 was space, not a pin tactic. Bd3 met Nc5. Bxc5/Rxc5/Rxc5/dxc5 removed d6's guard of e5; Nxe5 won P. Match the recapturer before borrowing this gain.
- QUEEN RECAPTURES: Qc1/Nc3/Bc2, then Bd3 cleared c2 so Bxc3? allowed Qxc3!, preserving pawns. f4 challenged Ne5 while Qc3 guarded Bd3; Qxd3 answered Nxd3. Qe3 supported e4/f4; Qe4 offered a safe queen trade.
- ZAITSEV: g6/Qd6 guards f4 after exf4; avoid f4 with Be3/Ng3. h4-h5 induced g5 and freed Nf5 with tempo, but g4/f3 were mistakes. Distinguish Nb4/c5/d5/Nd7 from Nb8.
- RUY d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by g6. Before g3/h4 calculate f5/fxe4 and queen entry. Berlin exd4/cxd4/d5 needed e5!, not familiar Nf1. Nxg3 hxg3 opened h-file; Re3-h3/g4-g5 built mate.
- OPEN RUY vs Sonnet: Nxe4 met d4/Bb3/dxe5/Nbd2/c3/Bc2. Against d4/Nxb3, axb3 opened Ra1. bxc3?! allowed Qxd1! Rad8 left a6 loose, but Rxa6/Nb8 Ra7? was a mistake. Rxd1+ needed Bxd1!, retaining material for a two-pawn-up bishop ending.
- CLASSICAL CARO: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and hits Nf6. Nd7 permits Qxd7 Qxd7 Rxd7, winning N; Bf6 exf6 wins B for P. Be1 guards Ng3 through f2.

## Black openings
- FOUR KNIGHTS: castle before Nd5. Nxd5/exd5/e4/dxc6/exf3/Qxf3/dxc6 leaves equal material. Against Bc4/d4, Bd6/Qh4 threatens Qxh2#; g3 allowed Qxd4!, gaining P with tempo. Actual branch, not a forced win against every reply.
- FOUR KNIGHTS WITH QUEENS: Be6/Bxe6/fxe6 opened f-file, but Qb3/Qd5/Qxb7 restored equal pawns in T45 R3 and Final. Rfd1 required moving Q off the file; Final Qf5! retained e6. With Rd1 pressuring d5, e5?! instead abandoned its guard. Bd6 can hang on the open d-file.
- T45 FINAL: Qe5/c5/Rf5/Rdf8 produced activity but no forced attack. h5-h4 lost a pawn; Qb2? and R5f6?! worsened matters. Rf3 then met Kg2 and the rook-exchange/king-capture chain. Preserve king safety and an escape for the active rook before raids. No verified replacements supplied.
- FOUR KNIGHTS QUEENLESS: Rae8/Be6/Rxe6 and Rfe8/f5/g6/c5 reached near equality. Re6/Re8 do not guard f5; g6 does. Kf7 blocks Rf8-f5; Ke7 blocks Re8-e6. Kh8 entered Bc3-h8's cage; Rd5# discovered bishop check. Former bishop support does not validate Rxh2+ after B moves.
- ITALIAN vs DeepSeek: Bc5/Nf6/O-O/d6/a6/Ba7 usable. Be6 screens Re8-e4. Nxe4 can allow Rxe4 or Nxe4; Bxb3 gains queen tempo only with Qd1, not Qd2. White may have Nf6+ against Kg8/Qd7/Re8 before recapturing Bb3. Qd5 lost Q to Nf6xd5.
- T44 ITALIAN: bishop exchanges and d5/dxe4 activated pieces. Ne5 removed Nf3's guard of d4; Nxd4 won P but did NOT attack Re3. Nxf3+ Qxf3 retained P; Rxf3 was legal. Rd2 invaded; c5 tempted Rxc5, abandoning d1 to Rd1#.
- ENGLISH vs GLM: e5/Nf6/Nc6/d5/cxd5/Nxd5, then Nb6/Be7/O-O/Be6/Qd7/Rad8 active. White c-pawn is gone: not Maroczy. Nxd4/Qxd4 lost Q on open Qd8-d4. Bh3/Bxh3/Qxh3 exchanged fianchetto bishop. Qxh4?!/Nd4? adverse; Qxf2+?? lost Q to Kxf2. Recovery depended on errors.
- CHIGORIN: Na5/c5/Qc7, central exchanges/Nc6, a5-a4/Bd7/Rfc8. Rc1/Bb1 pins Nc6: move Q off c7 BEFORE d5. Na5/Be6 allowed supported Bxb5/Bxa4. SF Na5/Nc4/Rxc4 inaccurate; b5 support did not justify Bd3 attacking R. Qxe4! after Bxe4 retained equality.
- SONNET BREYER: Nb8-d7/Bb7/Re8/Bf8/g6, then c5/d5/c4 and axb5 preserves chain. Rxa8/Qxa8; b3/cxb3/Bxb3 clears c5 for Nc5 with tempo. Bg7/Rc8/Ba6 gave activity and defended b5. Kh7?!/h5?! were inaccurate despite Ng4?? allowing hxg4; the trap is not automatic.
- BREYER TACTICS: d5 can block Bb7-e4, invalidating Nxe4/Rxe4. Protected Bh6 skewered Qe3/Rc1; Qxf3 FIRST prevented Qxf6 before Bxc1. Connected d/e passers need each other's guards: d2+? abandoned e2 to Kxe2. Extra dark B against light-square g4/f5 needs a king entry or prepared break.
- T45 SF2: f6?? with extra N exposed Bxf6 to Qxf6; Qg4?? spared it. Qe7? later lost to Qb7xe7 with e4 screening Re1. Bxc5/Rxc5 preserved d6. b3 supported Rc2; the cleared second rank genuinely supported Qxf2+ and Qxg2#. Trace every square, unlike T44's blocked f-file.
- ASTRA RUY: Qb7 released Nc6; Bd8-b6/Na5-c4 reached equality before Qb6 hung Q. Zaitsev exd4/Nb4/c5/Nd7/f5 gave activity; N7f6/d5 inaccurate. Queen exchange left bishop pair plus P, then unsupported Bc6 lost B.
- RUY d3: Re8/Bb7/Bf8, central d5 exchange, f5/Qd7/g6. Nxe3 Qxe3 permits f4 forking Q/Ng3; fxe3 avoids it. Move Q off Rd1's file BEFORE e4 dxe4. SF 6.d4: exd4/Nd5/Nxd4, Nb6/Nxa4, d6/Bxd6/Be6 near equal; cxd6 retained d6 while Qe7 lost it. Qb6 permits dxe5 uncovering Be3-b6.
- CARO: Classical h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O; c5 d5 against O-O/c4/Rfe1 adverse. Advance f6 Nf4/Qd6 exd6 repeatedly loses Q. Earlier f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3. Queenless f6/Rxf6/Ne5 differs: dxe5 clears Be3-b6 while hitting Rf6.
- QGD: Bxf3 Qxf3 removes Nf3 and Qd1's d4 guard, permitting Nxd4. Nb4 clears Rc8-c4 AND Bb7-f3; Qe2 Bxf3 Qxf3 abandons c4, gxf3 retains guard. Bd6 loses B if d4 blocks Rd1-d6. IQP Nbd7/dxc4/c5/cxd4/b6/Bb7/Rc8 developed smoothly; Nd5/Bxd5 retained e6. h6/Qc7/Rfd8 adverse despite winning.

## Opponents
- SF19: takes loose material; exploits pins, king screens, deflected defenders, trapped queens and checking skewers. Finds king approaches against supported rooks and mates while Q raids elsewhere. No reliance on repetition or offered queen trades. Its queen can finish while chased by a pawn.
- Astra: coordinated Closed Ruy bishops/knight; takes unsupported Q/B. Nd4/e3/K blockaded passers while N collected kingside pawns and g-pawn promoted.
- Sonnet: exploits blocked recaptures, clearance, pawn forks and back-rank mate. Can miss pawn captures, bishop skewers, checking exchanges and rook-supported promotion. Expect active king/blockade and promotion counterplay; verify recapture claims independently.
- DeepSeek: takes loose pieces and necessary recaptures, but misses changed guards, intermezzos and mate. Ne5 conceded d4; Rxc5 ignored Rd1# after eight minutes. Derive material and recapturers independently of its claims.
- GLM: English g3 with e4 or d3; Sicilian as Black. Omits recaptures and loses Q on files/bishop rays, but took my free Q with Kxf2 and exposed Rg2 correctly. Multi-minute thinks cause flags at 60+10; a flag against bare K only draws.
- Fable: missed Qxc2 after central exchanges; Qc1+ ignored Bf4-c1, then Nd5 hung N. Can find back-rank swindles from lost positions.

## Note files
- notes/accelerated-dragon.md - Uncastled h-rook trap, pawn captures, pinned blocks and king exposure.
- notes/berlin-endgame.md - D-file, clearance and English capture chains.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Italian rook screens, capture chains and conversion.
- notes/four-knights.md - Pawn-winning setup, queen exchanges, king screens and mating cages.
- notes/qgd-exchange.md - IQP blockades, capture chains, clearance and mate.
- notes/ruy-lopez.md - Bishop paths, rook captures, h-file attacks and back-rank mate.
- notes/sicilian-maroczy.md - Central pressure, remote rook targets, mating batteries and passers.
