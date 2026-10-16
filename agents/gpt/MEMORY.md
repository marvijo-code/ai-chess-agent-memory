# Chess memory

## Move discipline
- START WITH THE ENEMY'S LAST MOVE. Inspect checks, captures, forks, promotions and quiet mates on EACH candidate's proposed board. Rejecting one blunder does not validate another. Apply memory before choosing.
- DESTINATION BEFORE PURPOSE: development, defense, check and tempo do not make a square safe. Name the actual legal guard, excluding the mover. Bc6 defended b5 but Nd4xc6 won B; Bd6 guarded c5 but Rd1xd6 won B.
- PAWN DIAGONALS FIRST, then every knight and complete sliding rays, including backward bishops. Refresh BOTH diagonals after pawn moves and recaptures. A push abandons its OLD capture squares.
- TRACE GUARDS SQUARE BY SQUARE. Qa5 pinned Nc3 to Ke1, so Be3 did not defend e4. Nf3 does not attack e4; Nc3 does not attack d4. A piece beside K need not be legally protected.
- OWN SCREENS: Nd2 blocks Qd1-d3; Be3 blocks Re1-e4; f7 blocks Rf8-f2. Clearing one line does not clear another. Nf6xe4 opened Bg7-a1, but d5 still blocked Bb7-e4: Rxe4 lacked bishop support.
- KING MOVES CHANGE GUARDS AND SCREENS. Ke7 unpinned f5 but blocked Re8-e6 and abandoned Re6's king guard. exf5 attacked Re6; Kxe6 was illegal because f5 controlled e6. Kh2 can release g3's pin and restore gxh4 against Qxh4+.
- LAST GUARD: Nc3 screened Qa5-e1; Rd1 guarded Re1. Nxd5 removed the screen; Bd3/Bxd3/Rxd3 moved Re1's last guard. A developing move can permit Qxe1+.
- PAWN BREAKS: place the enemy capture first. f4 exf4 forked Be3/Ng3 and opened Qd6-f4; Bxf4 Qxf4 lost B. f6/exf6 exposed Be6 to Qe2. With Qf3/Rf8, my f-pawn screened MY queen; fxe6 allowed Rxf3.
- CHECKS STILL NEED A CAPTURE SCAN, including Kxchecker and pawn captures. A rook behind a pawn or a relocated bishop does not support an old battery. Identify the actual checker after discovered checks; capturing the moving piece may leave check unanswered.
- BACKWARD BISHOPS: Bf4 reaches c1 through e3/d2; Bh6 reaches c1 through g5/f4/e3/d2; Bf6 reaches d8 through e7. Sweep the full diagonal before any queen or rook landing.
- UNCASTLED DRAGON: h5 vacates h7, opening Rh8-h6. Bh6 Bxh6 attacks Qd2 through g5/f4/e3; Qxh6 loses Q to Rxh6. Verify the LAST capture and castling status before Bh6.
- OPEN A-FILE: axb5 axb5 opens Ra8-a1. Bc1/Bb1 can block a rook recapture; queen retreats then lose Ra1. Resolve rook contact first. Ra1/Rf1 defend each other only with b1-e1 empty.
- FINISH THE CAPTURE CHAIN AND RECOUNT BOTH ARMIES. Nc4 Qxc4 Qxc4 Rxc4 lost N. Opponent may STOP exchanging: Qd5 Rxd5 loses Q for R despite support. Sweep the recapturer's destination after clearance: Rxa2 Qxa2 Qxa2 can lose my whole queen.
- AN ATTACK NEED NOT FORCE RETREAT. b3 attacked Rc4 but opened Bf6-a1: Bxa1 bxc4 Bc3 retained extra B. Rdb1 attacked Bb2, but Bxa1 took R. Search captures by the attacked piece AND other pieces.
- REFRESH PINS WHEN ENDPOINTS MOVE. Nd4 Nxd4 cxd4 opens Rxd8+ against Qd8. Kb1 released Rd2; Kf1 released Nd2's pin to Ra2. A pinned rook can capture its pinning queen.
- BEFORE FORKS/TRADES TEST CAPTURES AND CHECKING INTERMEZZOS. Nc3+ Qxc3 Rxd1 Rxd1 lost N; Bxd5 allowed Nd3+ before Qxd5. Nc7's fork did not answer Qd8's attack on Qg8.
- TRACE VACATED RAYS BEYOND THE FIRST TARGET. e5 uncovered Bf3-a8; Nf5 blocked Bf4-d6. Kb3 screened Rb1-b7; Ka4 allowed Rxb7. A checking block must survive capture and the final reply.
- MATE FIRST, including quiet moves and queenless positions. Nxf4 hit Qh5 but allowed Qxh7#; Rxe7 ignored Rh1#. exf6 can win a minor AND support Qxg7#. Luft solves only the mate its flight prevents.
- BACK RANK: Kg8 behind f7/g7/h7 needs an explicit Re8+ defense. Bc6 abandoned Bd7-e8 AND screened Rc8-c5; Rxc5 then removed the last rank-8 defender. Scan after the LAST recapture.
- MATING SCREENS: Qg3/Bd4 needs f6 clear for the g7 battery. Ka1 behind b2 on Bg7's diagonal made bxa3 illegal after Qa3 Qxa3#. Nominal pawn support may be pinned.
- QUEEN CONTACT NEEDS A LEGAL RECAPTURER. Qb6 Qxb6 lost Q; c7 blocked Qd6-b8 after Rb8 Qxb8+. Qg4's double attack failed to Be6xg4. A counterattack does not answer a direct queen capture.
- T42 SF: Bxc4 anticipated Qc5+ without resolving its attack on Bc4. After Kh1 Qxc4, Q saw Rf1 through d3/e2; Bc1 blocked Ra1-f1 and Kh1 abandoned f1. b3 chased Q but allowed Qxf1#. Calculate check, response, capture and NEW rays before calling a move a tempo gain.
- T42 SONNET: Bh6 skewered Qe3/Rc1 through g5/f4/e3/d2. After Qf3, exchange queens BEFORE Bxc1 so the enemy queen cannot collect mine. Bb5 also attacked Ne2: Nxc1 saved it; Rxc1 would leave Bxe2. Enumerate both recapturers and their abandoned duties.
- Validate destination and full path before submission. After ONE rejection reconstruct the board and choose a verified legal move; three invalid replies forfeit. Recovery still needs a capture scan. Match blockers, placement and castling before using memory.

## Clock and endings
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below five minutes cap 15; below 90 seconds use 1-3. Budget from starting clock, especially Armageddon White's ten minutes.
- LONG THOUGHT DOES NOT VALIDATE A MOVE. Spend critical time on the reply chain, changed screens and flights, not the move's purpose. T42 Sonnet: Rc7 used 53 seconds before losing c4; g5/g4 used 54/40. Zero invalid, finished 9:09; verified late king moves and recaptures mostly 3-8 seconds sufficed.
- MATERIAL FROM THE BOARD, not comments or previous evaluation. Equal trades preserve deficits. Verified recaptures/conversion need 1-5 seconds unless checks, pawn moves or changed rays alter them.
- Ahead: remove counterplay and simplify safely. Before heavy-piece trades list cheaper capturers, legal recapturers and abandoned guards. Rf4 Bd2xf4 Bxf4 loses the exchange.
- ROOK DESTINATIONS NEED EXITS. c4 displaced Rb5 to Rb4; Bd2 attacked it while a5 was loose. Pawn support did not prevent displacement or Bxa5. Count pawn kicks and bishop approaches before advancing R.
- KING CAGE BEFORE PAWN COUNTERPLAY. Kf5 with own e5/g5/h5 faced f3/g3 and Bd8. Bishop-supported Rf6# sealed e6/g6 while pawns covered e4/f4/g4. Ra7's blockade did not answer mate. Map all eight exits.
- CONNECTED PASSERS NEED A BREAK. Astra's Nd4/e3/K blockaded c4/d5 while N collected kingside pawns. Remote king raids failed; d4 allowed exd4. Compare blockade removal and promotion tempi before raiding.
- Supported passers can purchase exchanges, but finish the chain: Qc7 Qxc7 dxc7 retained the passer; Bxc7 removed it. Re8 Rxe8 fxe8=Q+ removed the last enemy rook and promoted.
- Stop advanced counterplay before remote raids. T42 Sonnet: Rb7 controlled d7 while Kf6-e6-d6 collected the supported passer. Then take remaining pawns with K/R coordination; stalemate-check before quiet restrictions.
- KING AS SOLE ROOK GUARD: g6-supported Rf7+ drove K away before Rxe6 won R. Test checks deflecting K and both diagonals of advanced pawns. In B+P endings preserve the LAST pawn's guard before sending B away.
- T42 SONNET: g4 supported entry on f3 and restricted Kh3. R8f3+ forced Rxf3 Rxf3+, removing White's only rook and therefore Nb3's guard; Rxb3 won N. A supported checking trade can win a second target after the forced king reply. Recount guards after each exchange.
- Escort passers; scan straight AND capture-promotions two advances ahead. c2 attacks b1/d1; b8=Q+ can discover Ra7-d7, preventing Rxb8. Include en passant beside two-square pushes.
- KING ACTIVITY NEEDS LEGAL TARGETS AND ARRIVAL TIMES. Ke4 hit d4 but Kc5 guarded it. d4+ forked Ke5/Bc5. Pawn enclosures permit pawn/knight mate. In rook mate, approach with K covering second-rank flights; use a safe waiting move when direct opposition is unavailable.

## White openings
- Quiet Sicilian: Be2/O-O/Be3/f4/Kh1, then a4/Bf3/Qe1-g3 suits me; distinguish Dragon/Maroczy and whether cxd4 ACTUALLY occurred. Wins depended on errors. Qe1 and automatic Nxc6 after Qxe5 were inaccurate; compare immediate queen exchange.
- GLM omitted cxd4 in T41: my pawn remained d4 and N remained f3. Automatic development missed central opportunities. d5/exd5/exd5 renewed the attack on Nc6; castling ignored it and dxc6 won N for P. Bd3/Qe4 later threatened Qxh7# plus Be7.
- Ndb5 vs GLM: Nd4! Nxd4 Bxd4 and Be3! after e5 kept material. Qb6+ required Kh1; Qxb2 attacked Nc3. Nd5/Nxd5/exd5 hit Be6; d6 screened Rd8-Qd3. Rab1 escaped Bf6-a1 with tempo. Qd3 was inaccurate; no verified replacement.
- Taimanov: Bxd4 keeps B active. e5/dxe5/fxe5 opens Rd1 and hits Nf6. Bf6 exf6 can win B and support mate. T42 GLM's Qc7 landed on Bg3-f4-e5-d6-c7: Bxc7 won Q. Trace a retreating bishop beyond its central target.
- MAROCZY vs Qa5: f3 guards e4 while Nc3 is pinned; Qxd4! after Nxd4. Ng4 can hit Be3 AND uncover Bg7 against Qd4. b3/Bf2 can uncover Qa5-c3. Long castling: Nxd5 or Bd3/Bxd3/Rxd3 abandons e1 defenses. Short castling: exchanges can enable Bd4+ against Kg1/Ra1 with b2 empty.
- T42 SF Maroczy: Qd2?! inaccurate; no verified replacement. Be2/O-O/Be6 led to Bxc4 Bxc4 Qc5+! Kh1 Qxc4!, losing c4 and exposing Rf1. Preserve the pinned-knight lesson, but assess c4 and king rays after bishop exchanges. Loss does not refute 5.c4.
- Dragon: long-castled g4 liquidated my f/g/h pawns for Black's h-pawn; h4 avoided that but Bh6 repeated the uncastled Rh8 trap. Short-castled Bb3/Nxe3/fxe3 concedes bishop pair. Bg4 hits Qe2 through f3; Nxf3+ needed gxf3, Bh3 needed Rfe1, Bxc3 needed bxc3. Qh4/Rd3 allowed Rc5-h5; Qxa5 ignored Qg4+ and mate. Trade offers defend only when accepted.
- Closed Ruy: Qxf3 abandons d5; exd5 can expose Rxe1+ with Bb1/Bc1 blocking Ra1. Bf4 permits Bxe4 with tempo on Qf3. Nf1 restores Qd1-d4; Qf3 abandons b3. Nxd4/Qxd4 can lose loose Bc2 on cleared Qc7-c2. f6 hits Re7 AND opens Bc2-h7: compare mate before grabbing.
- Zaitsev: g6/Qd6 guards f4 after exf4; avoid f4 with Be3/Ng3. h4-h5 induced g5 and freed Nf5 with tempo, but g4/f3 were mistakes. Distinguish Nb4/c5/d5/Nd7 from Nb8.
- Ruy d3: c3/h3/Re1/Bc2/d4; e5 clears Bc2-h7. Qd3/Bb1 threatens Qh7#, answered by g6. Before g3/h4 calculate f5/fxe4 and queen entry. SF's e4 displaces Nf3 and Ne5-d3-f4 invades.
- T41 Berlin d3 vs Sonnet: exd4/cxd4/d5 needed e5!, but familiar Nf1 was a mistake. Nxg3 hxg3 opened the h-file; Bf4/Bd3/Qxd3 and Re3-h3 plus g4-g5 built mate. hxg5 cleared Rh3-h7 for Qh7#. a3/Nh2 inaccurate; no verified replacements.
- Classical Caro: h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1. Ne5 Nxe5 dxe5 opens Rd1 and hits Nf6. Nd7 permits Qxd7 Qxd7 Rxd7, winning N; Bf6 exf6 wins B for P. Be1 guards Ng3 through f2.

## Black openings
- Four Knights: castle before Nd5. Nxd5/exd5/e4/dxc6/exf3/Qxf3/dxc6 leaves equal material. Against Bc4/d4, Bd6/Qh4 threatens Qxh2#; g3 allowed Qxd4!, gaining P with tempo. This is an actual branch, not a forced win against every reply.
- T41 Final: Be6/Bxe6/fxe6 opened f-file. Qb3/Qd5/Qxb7 restored equal pawns despite active rook tempos. Rd1 warned of d-file pressure: e5?! then Qxd5+ cxd5 Rxd5 left P down. Calculate through the rook capture; no verified replacement for e5.
- Four Knights queenless: Rae8/Be6/Rxe6 and Rfe8/f5/g6/c5 reached near equality. Re6/Re8 do not guard f5; g6 does. Kf7 can block Rf8-f5; Ke7 can block Re8-e6. Kg7 unpinned f5 but gxf5 gxf5 Rxf5 lost P. Kh8 entered Bc3-h8's cage; an interposed bishop did not survive the final capture. Rd5# discovered that bishop check.
- Italian vs DeepSeek: Bc5/Nf6/O-O/d6/a6/Ba7 usable. Bg4-h5-g6 avoids Be6 screening Re8-e5. Qe7/e4 enabled a pawn gain, but Qd5 lost Q to Nf6xd5. T41 Qd7/Nf6 inaccurate despite winning; no verified repairs.
- Italian clearance: Be6 screens Re8-e4. T40 Nxe4?! allowed Rxe4!; Bxb3! cleared the file AND attacked Qd1. T42 Nxe4?? allowed Nxe4!; Bxb3 did NOT attack Qd2, and Ne4 could use Nf6+ against Kg8/Qd7/Re8. axb3?? then allowed Rxe4. Do not import the tempo from a different queen placement; the win followed enemy gifts.
- English vs GLM: e5/Nf6/Nc6/d5/cxd5/Nxd5, then Nb6/Be7/O-O/Be6/Qd7/Rad8 active. White's c-pawn was gone: not a Maroczy. Nxd4/Qxd4 lost Q on open Qd8-d4. Distinguish e4 before Bg2 from d3.
- Chigorin: Na5/c5/Qc7, central exchanges/Nc6, a5-a4/Bd7/Rfc8. Rc1/Bb1 pins Nc6: move Q off c7 BEFORE d5. Na5/Be6 allowed supported Bxb5/Bxa4. T40 SF Na5/Nc4/Rxc4 inaccurate; b5 support did not justify Bd3 attacking R. Qxe4! after Bxe4 retained equality.
- T41 Sonnet: Bb7/Re8/Bf8, exd4/Na5/c5/Nc4-e5 met d5/b3/Nxe5. After g6/Bg7/Be3/Qc7/Qd2, Nxe4? and Rxe4?? lost B for P: Bb7-e4 remained blocked by d5.
- T42 SONNET BREYER: Nb8-d7/Bb7/Re8/Bf8/g6/Bg7, then c5/d5/c4/Nc5. b4 displaced N to a4; Bxa4 required bxa4!, accepting doubled a-pawns for bishops. Rc7/Rec8 did not retain c4, and Nxa4 removed the doubled pawn: I was TWO pawns down. No adverse Black marks supplied, but this is not proof the pawn concessions were forced or sound.
- T42 Breyer recovery: Bc8-d7-b5 gained a queen tempo, then h5 cleared h6 and Kh7 protected it. Ne2?!/Kh2?? allowed Bh6!, skewering Qe3/Rc1. After the queen exchange and Bxc1/Nxc1, Rxc3 recovered P and activated R. Keep this diagonal pattern; do not rely on the opponent permitting it.
- Astra Ruy: Qb7 released Nc6; Bd8-b6/Na5-c4 reached equality before Qb6 hung Q. Zaitsev exd4/Nb4/c5/Nd7/f5 gave activity; N7f6/d5 inaccurate. Queen exchange left bishop pair plus P, then unsupported Bc6 lost B.
- Ruy d3: Re8/Bb7/Bf8, central d5 exchange, f5/Qd7/g6. Nxe3 Qxe3 permits f4 forking Q/Ng3, but fxe3 avoids it. Move Q off Rd1's file BEFORE e4 dxe4. SF 6.d4: exd4/Nd5/Nxd4, Nb6/Nxa4, d6/Bxd6/Be6 reached near equality; against Rad1/Bxd6, cxd6 retained d6 while Qe7 lost it. Qb6 permits dxe5 uncovering Be3-b6.
- Caro: Classical h6/Bh7/Nd7/Bxd3/e6/Ngf6/Be7/O-O; c5 d5 against O-O/c4/Rfe1 adverse. Advance f6 Nf4/Qd6 exd6 repeatedly loses Q. Earlier f6 BEFORE cxd4 worked with c3 screening Qb3-d3 and Nd2 blocking Rd1-d3. Queenless f6/Rxf6/Ne5 differs: dxe5 clears Be3-b6 while hitting Rf6.
- QGD: Bxf3 Qxf3 removes Nf3 and Qd1's d4 guard, permitting Nxd4. Nb4 clears Rc8-c4 AND Bb7-f3; Qe2 Bxf3 Qxf3 abandons c4, gxf3 retains its guard. Bd6 loses B if d4 blocks Rd1-d6. IQP Nbd7/dxc4/c5/cxd4/b6/Bb7/Rc8 developed smoothly; Nd5/Bxd5 retained e6. h6/Qc7/Rfd8 adverse despite winning.

## Opponents
- SF19: takes loose material and exploits pins, king screens and checks deflecting sole defenders. T42 Qc5+ gained c4; Qxc4 threatened Rf1 and mate. A queen chased by a pawn can finish immediately. No reliance on repetition or an offered queen as recovery.
- Astra: coordinated Closed Ruy bishops/knight; takes unsupported Q/B. Nd4/e3/K blockaded my passers while N collected kingside pawns and a g-pawn promoted.
- Sonnet: exploits blocked recaptures, clearance, pawn forks and back-rank mate. T42 Breyer collected c4/a4 safely but Ne2/Kh2 allowed the bishop skewer; being two pawns ahead did not solve loose heavy pieces. Later overlooked that a forced rook trade removed Nb3's guard. Quiet king moves still change tactics; calculate independently.
- DeepSeek: takes loose pieces but misses forcing clearance and final captures. T42 Nxe4 punished my blunder, then axb3 returned N and Ne5 lost another to d6. Ba4 attacked Q but Qxa4 won B; Qf5 ignored Nf4-supported Qxg2#. Comments invent guards/material.
- GLM: English g3/e4 or d3 after exchanging c4; can omit recaptures or lose Q on files/pawn diagonals. As Black follows Sicilian setup despite unresolved center and ignores Bd3/Qe4 mate. Verify independently; errors do not validate my opening.
- Fable: missed Qxc2 after central exchanges; Qc1+ ignored Bf4-c1, then Nd5 hung N. Verify remote captures independently.

## Note files
- notes/accelerated-dragon.md - Uncastled h-rook trap, pawn captures, pinned blocks and king exposure.
- notes/berlin-endgame.md - D-file, clearance and English capture chains.
- notes/caro-kann-advance.md - Breaks and queenless mate.
- notes/deepseek.md - Italian rook screens, capture chains and conversion.
- notes/four-knights.md - Pawn-winning setup, queen exchanges, king screens and mating cages.
- notes/qgd-exchange.md - IQP blockades, capture chains, clearance and mate.
- notes/ruy-lopez.md - Separate bishop paths, rook captures, h-file attacks and back-rank mate.
- notes/sicilian-maroczy.md - Central structure, pawn screens, mating batteries and passers.
