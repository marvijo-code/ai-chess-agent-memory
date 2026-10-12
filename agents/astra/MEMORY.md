# Chess memory

## Move discipline
- MATE BEFORE MATERIAL, including queenless positions. T37R6 after ...Rxb1+ Kh2, Kg8 remained boxed by f7/g7/h7; ...Rxd2?? collected B and allowed Rd8#. Neither rook could capture Rd8 or block e8/f8. Check actual blocking squares and flights, not vague rook activity.
- RESTART AFTER EVERY REPLY. Kh2 answered my check AND preserved mate. A forcing sequence ends when the opponent creates or retains a threat; an earlier calculated gain is only a candidate. Reserve a fresh scan before the next capture.
- Before moving: inspect the opponent's changed attacks, then checks, captures and threats on the proposed board. Pawn diagonals first, every knight next, complete slider paths including backward bishop captures. Supported pieces and checking moves can still lose material.
- NAME LEGAL RECAPTURERS on the resulting board, excluding the mover itself. T37R5 Rc1?? moved White's last rook from e1; Nd2 blocked Be3-c1, so ...Rxc1+ won R. T37R6 Nd2 blocked Qd1-d3 and Be3 separately blocked Re1-e4. Clearing one line does not clear another.
- VACATED SCREEN: trace every line opened by a capture before recapturing. T37R3 ...Nf6xd5 cleared Bg5-f6-e7-d8 against Qd8; exd5?? missed Bxd8. My feared ...Bb4+ was impossible through d6. Verify the alleged refutation's path.
- REMOVED GUARD + CLEARANCE WITH TEMPO: T37R7 ...Be7xf6 abandoned Nc5. Nd4 still screened Be3-c5; Nxc6! attacked Qd8 while uncovering Bxc5 after ...bxc6. Scan the mover's OLD guards, then ways to clear my own screen with tempo.
- A GUARD-ADDING MOVE CAN HANG THE GUARD ITSELF. T37SF2G1 ...Bc6?? defended b5 but allowed Nd4xc6!; neither b5 nor d5 could recapture. After ...Bxe3 fxe3 I kept an extra N. Judge the destination before the move's strategic purpose.
- PAWN GEOMETRY: c6 attacks b7/d7, never Ra8; Black b5 attacks a4/c4, not c6. T37R3 ...Bd7?? put B on my c6-pawn's capture square. A supported piece still loses to a cheaper pawn capture.
- KING MOVES CHANGE ATTACKS AND SCREENS. T37R3 ...Ka6 attacked Rb7; h7 allowed ...Kxb7 unnecessarily. My Kc6 also blocked Qd6's sixth-rank control. Recompute adjacent loose pieces and slider flights after every king move.
- QUEEN CONTACT NEEDS A REAL RECAPTURER. T37R4 ...Qb6 attacked Qc7 and defended Na5/d6, yet Qxb6 won Q outright. ...Nd7 then attacked Qb6 without guarding Na5; Qxa5 won N. Counterattacking my queen does not force retreat.
- DOUBLE ATTACK IS NOT AN EVALUATION. T37R4 Qc7? hit Na5/d6 but needed ...Qb6?? to succeed. Calculate the strongest forcing reply, including captures by uninvolved pieces.
- REMOTE QUEEN DEFENSE: T37R5 ...Qd3 guarded g6 through e4/f5; Qxg6+ lost Q to ...Qxg6. Inspect complete diagonals even beside an exposed king.
- MATERIAL FROM THE BOARD, never commentary. Recount after liquidation and promotion; equal exchanges preserve an earlier deficit. Opponents have claimed equality after losing R and a pawn lead after losing N.
- A memory plan is a question on the current board. Match blockers, queen placement, pawn structure and castling status before importing an opening tactic. No verified replacement means compare candidates, not invent a forced improvement.

## Conversion and endgames
- LUFT BEFORE COLLECTION when heavy pieces can enter my back rank. T37R6 examine ...h6 before taking Bd2; h7 would become a flight against Rd8+. Queens off does not settle king safety. No verified best replacement stored.
- PROMOTION MAY BUY A SURPLUS WITHOUT KEEPING Q. T37R6 ...b1=Q induced Rxb1 Rxb1+, leaving 2R versus R+B. Consolidate before extending the gain; taking Bd2 immediately was fatal. Counterplay never answers an immediate mate.
- EXTRA MINOR VERSUS PASSERS: establish a supported blockade, bring K toward the pawn majority, then release N for targets. T37SF2G1 Nd4/e3 held d5 while K reached c3. Only then Ne6+ and Nxg7 became practical; return routes and pawn breaks still needed calculation.
- A DISTANT PASSER CAN WIN WITHOUT HOLDING EVERY CENTRAL PAWN. Against Sol, bxa3 stopped the advanced a-pawn and Kb2 guarded a3. Nf5 returned toward the center, Kc3 secured d4, and Nxh6 cleared the kingside. After g5 and ...d4, exd4 removed the break; giving up d4 later did not stop g8=Q. Count both races before releasing the blockade.
- REPETITION WITH A PURPOSE: Kc3/Kb2 answered Sol's ...Kc5/...Ka4 threats while N removed kingside pawns. Then g5 changed the position. Track exact positions including side to move; do not shuffle indefinitely in a won ending.
- AFTER PROMOTION, STOP THE ADVANCED COUNTERPLAY. T37SF2G1 Qc4+ displaced the king, Qxc3+ removed the passer, and Qxa5 removed the last pawn. Then restrict K and approach with my own K. Giving up g2 was harmless with Q+N; check stalemate before every quiet restriction.
- QUIET MATE PREPARATION: with Qe2 against Kg1 and Nh6, Ng4 protected h2 and left ...Kh1 as the only move; Qh2# followed. List the knight's actual support squares and all king flights. Do not search queen checks alone.
- CHECKING CAPTURES MAY BE BETTER THAN THE LARGEST TARGET. T37R7 Nb6 forked Ra8/Bd7; Nxd7+ and Nxf6+ removed both bishops and ...gxf6 exposed K. Qg8+ drove Ke8 away before Qxa8. Calculate the full liquidation instead of automatically grabbing R.
- DEVELOP WITH THREATS WHILE RETAINING DEFENSES. T37R7 Rad1 activated the last piece; Rde1 hit Qe4 while Rf1 kept f4 guarded. With a surplus, active defended pieces and removal of central pawns reduce counterplay.
- SUPPORT CAN APPEAR WHEN THE QUEEN MOVES. T37R7 Qf7 with Re7 against Kh6 threatened Qxh7#: vacating f7 cleared Re7-h7 to protect Q, while f4 covered g5. Check captures, blocks and flights before trusting the net.
- RETURN PART OF A SURPLUS TO REMOVE COUNTERPLAY. T37R5 ...Nb3 induced Nxb3 axb3; supported ...Rc2 screened Qd1 from b3. After Bxc2, ...bxc2! completed the liquidation and retained an extra B after Qxc2. Finish the calculated recapture.
- RETREAT AFTER A GAIN WHEN THE NEXT CAPTURE WASTES IT. T37R5 after ...Rxc1+ Kh2, ...Rc8 saved the extra rook; ...Rxb1 would allow Nd2xb1.
- ACTIVATE AN EXTRA MINOR WITH A SUPPORTED BREAK. T37R5 ...g6/...Nh5 prepared ...f5; exf5 Bxf5 developed with tempo, then ...Be4 attacked Nf3/d5. Verify every supporting diagonal after exchanges.
- KING ACTIVITY NEEDS A TARGET AND RETURN ROUTE. T37R2 my king chased f4 while Kc5+B approached d5; ...Kh6?? moved farther from the chain. Ba8 guarding d5 was insufficient against Bxd5 Bxd5 Kxd5. Evaluate the pawn ending through the final king recapture before trading bishops.
- EXTRA PAWN IS NOT A PLAN. White's Kd4 blockade and a-file invasion neutralized my connected passers. Preserve a way to dislodge the blockader. Separated b/f passers later stretched my lone K; count promotion tempi and arrival squares.
- PAWN MATES AND KNIGHT GEOMETRY: T37R4 Qg7/Nf5 confined Kh5 and g4# checked with a pawn. T37R5 Nf4 supported Qe2/Qg2/Qxh3, not Qf3. List exact support squares before adjacent queen checks.

## White opening: Ruy Lopez, Zaitsev
- T37SF2G1 Sol: h3/d4/Nbd2/a4/Bc2 against ...Bb7/...Re8/...Bf8/...h6. After ...exd4 use cxd4; ...Nb4 attacks Bc2, so Bb1 preserves it. Against ...c5, d5 gained space. This is distinct from the Chigorin pin on the c-file.
- Ra3-e3 reinforced e4 against ...f5, but after ...fxe4 and Nxe4, ...Nxd5 took d5 with Bb7 supporting N. R3e2 saved the attacked rook. Do not describe the rook lift as a free attack: track both central pawns and the bishop diagonal opened when e4 disappears.
- ...N7f6?! allowed Nxf6+; ...Nxf6! preserved the structure. My Bf4? and Qd3?! were marked adverse despite natural development and a Bb1/Qd3 battery. The win does not validate them; no verified replacements supplied.
- Rook exchanges left Q+B+B+N versus the same pieces, a pawn down. Ba2+ met ...c4! with tempo against Qd3. Before a diagonal check, calculate pawn interpositions that also attack my queen; an active-looking check can improve the enemy pawn mass.
- After Qd1 and ...d5?!, Nd4 established a blockade; Be3 supported it. Bb1 challenged ...Ne4, but Bxe4?! Qxe4! surrendered B for N and centralized Black's queen. Removing an outpost is not automatically worth improving the recapturer.
- Qg4 and the queen exchange reduced king danger but left Black's bishop pair and extra pawn. ...Bc6?? then lost a bishop to Nxc6!, the only good move. This gift decided the game; it does not prove the preceding simplification won by force.

## White opening: Ruy Lopez, Chigorin
- T37R4 Sol: Bb5/Ba4/Bb3, O-O/Re1/c3/h3/Bc2/d4 against ...Na5/...c5/...Qc7. After ...cxd4, cxd4 restored the center. Nb3/Be3 met ...a5-a4 with Nbd2; Rc1/Bb1 cleared the c-file and Nf1-g3 improved N.
- Sol's ...Qb7 released Nc6 before d5. Do not import pinned-knight tactics after Q leaves c7. d5 blocked Bb6 but allowed ...Na5-c4; Bxb6 and b3 resolved the pressure without demonstrating an opening advantage.
- After Rxc8 and Nhf5, ...Bxf5 Nxf5 kept the knight on f5. ...Rc7 guarded e7, so Ne7+ needed fresh calculation.
- Qf3?! abandoned Qd1-c2-b3. ...g6 displaced Nf5; Ne3 uncovered an attack on Nf6, but ...Kg7 answered it. Qd1 restored b3's guard. Compare a queen sortie's threat with its defensive tempo cost.
- Qd2 guarded c1 before Rc1 and ...Rxc1+ Qxc1. Black's a3/b4 constrained me and ...Qd4 activated Q. Qc7? was rescued by ...Qb6??, not by a forced double attack.
- exf5 later cleared Bb1-c2-d3-e4-f5; after ...gxf5, Nxf5+ had bishop support. Recompute my own screens before relying on the long diagonal.

## Black opening: Ruy Lopez, Chigorin
- T37R5 Sonnet/T37R6 Fable: ...a6/...b5/...Nf6/...Be7, castle, ...d6; against c3/d4 use ...Na5/...c5/...Qc7. After ...cxd4 cxd4 return ...Nc6. Their Nb3/Be3 met ...a5-a4, sending Nb3 to d2.
- Sonnet branch: ...Bd7/...Rac8; Rc1/Bb1 opened the c-file against Qc7, so ...Qb7 released Nc6 BEFORE d5. ...Rfe8/...Bf8 supported d6. After a3/d5, ...Na5 was available. The win came from Rc1?? losing R, not a forced opening edge.
- Fable's earlier d5?! and my ...Na5?! were both marked inaccurate. Do not automatically import the Sonnet retreat. No verified best replacement supplied.
- Fable's Bd3/b3 denied c4 but Nd2 blocked Qd1-d3. ...Rac8/...Qc3 met Rc1?? with ...Qxd3! Nf1 finally cleared the queen guard; after the queen exchange Be3 still blocked Re1-e4 and ...Nxe4 won P.
- Later ...Nxb3 and the b-passer produced promotion and a surplus, but ignoring Rd8# lost. Store the guard tactics and back-rank warning, not an automatic conversion recipe.

## White opening: Taimanov 6.Be2
- T37R7 DeepSeek: Open Sicilian with Nc3/Be2/O-O/Be3/f4 against ...e6/...Nc6/...a6/...Be7/...Nf6/...O-O. This setup suits me; no White moves marked adverse, but the win does not establish a forced opening edge.
- Against ...d5, e5 gained a tempo on Nf6; after ...Nd7, Qe1-g3 aimed at K. ...Nc5 put N behind my Nd4 screen on Be3's diagonal. ...f6 exf6 Bxf6?? removed Be7's guard of c5; Nxc6! attacked Qd8 and uncovered Bxc5.
- Bxc5 also attacked Rf8 because f7 was empty; Bxf8 increased the surplus. Rad1 developed; ...Qb6+ met Kh1. Against ...Qxb2 attacking Nc3, Na4 hit Q and prepared Nb6. Calculate checking knight captures before choosing Ra8.

## White opening: Sicilian Ndb5
- T37R3 GLM: against ...e6/...Nf6/...Nc6, Ndb5 met ...d6 with Bf4; ...e5 gained a bishop tempo and weakened d5. Bg5/...a6/Na3/...b5/Nd5 produced the Bg5-Qd8 screen tactic.
- ...Nxd5 abandoned Qd8; inspect Bxd8 before exd5. My exd5?? missed it; dxc6! after ...Qxg5 was the required recovery. Qf3 guarded c6 and g2; ...Bd7?? lost B to cxd7+.
- O-O at move 17 was marked a mistake; no verified replacement. Compare immediate tactics even with queens off. Na3-c2-e3-d5 blockaded d6. Later ...a5 removed a6's guard of b5, allowing Bxb5+ with an attack on Re8.

## Black opening: Spanish Four Knights
- T37R2 SF19: ...Nc6/...Nf6/...Bb4 and castle against Nf3/Nc3/Bb5.
- Played: 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Bd6 11.d4 Qh4 12.g3 Qxd4.
- Complete both pawn removals to restore balance. Bd6/Qh4 threatened Qxh2#, permitting ...Qxd4 after g3 with tempo on Bc4. Verify the matching board; both queen moves were marked only good moves.
- ...Bg4 attacked Qf3 with Qd4 supporting B; Be3 counterattacked Qd4, and ...Bxf3/Bxd4 exchanged queens while retaining the extra pawn. Count both captures.
- ...b5/...a6 and the a-file exchange required active rook contest. Bxd6+ ...cxd6 created a passer, but ...b4 liquidation let Kd4 blockade. Preserve a way to challenge K before simplifying.

## Opponents and clock
- Sol, T37R4 and SF2G1 Black: coherent Chigorin and Zaitsev development, active central counterplay, then guard failures. R4 hung Qb6 while defending two targets; SF2G1 hung Bc6 while reinforcing b5. Check the destination independently of its purpose. Neither win proves an opening edge.
- Sol's SF2G1 ...f5/...Nxd5 won a central pawn; ...c4! blocked check with tempo, and ...Qxe4! preserved active passers. After losing B, used Kc5/Ka4 and a3 to stretch the blockade. Expect active resistance, not immediate collapse. Zero illegal attempts; finished about 6:35.
- DeepSeek T37R7: Taimanov ...d5/...Nd7-c5/...f6; ...Bxf6?? forgot Nc5, then queen pawn raids allowed checking captures to dismantle its pieces. Comments invented guards and miscounted material. Verify independently.
- Fable T37R6: missed Nd2 blocking Qd1-d3 and Be3 blocking Re1-e4, including one illegal Qxd3. Found active rook resistance and Rd8# from a lost position. Earlier guard errors do not imply weak finishing. Finished 7:01 after several long thinks.
- Sonnet T37R5: coherent Closed Ruy opening; Rc1?? imagined a recapturer from the vacated rook square, then Qxg6+ missed a remote queen diagonal. Often spent 56-68 seconds; finished 5:56, zero illegal.
- GLM T37R3: found ...Qxg5 after my missed queen capture, but put Bd7 on a pawn diagonal and miscounted guards. Took my exposed rook with K; never assume a simple capture will be missed. One illegal.
- SF19 T37R2: shallow, essentially instant. Found the blockade and won my central chain; later repeated against bare K. One search failure is not a reliable defensive plan.
- 900+10: book 1-5 seconds, routine 5-15, critical 20-40 for a concrete question. T37R6 fatal ...Rxd2?? took THREE seconds with 14:20 left. Reserve 10-20 seconds for a fresh threat scan after forcing sequences, especially with a boxed K.
- SF2G1 finished with over ten minutes and zero illegal attempts. Spent 52 seconds on Nxe4, 53 on Ba2+, and 39 on inaccurate Bxe4. Long thought did not validate those choices. Nxc6 took 13 seconds: direct guard verification can be quick. Shorten routine queen-mate restriction; spend time on checks, changed guards and pawn races.

## Record
- T37R2 Black v SF19: draw, m97. Won P, lost central chain after king excursion, survived Q versus bare K by repetition.
- T37R3 White v GLM: Qa3#, m51. Missed Bxd8, recovered with dxc6, won B after ...Bd7, promoted; avoidable rook loss.
- T37R4 White v Sol: g4#, m43. Qf3?!/Qc7?; ...Qb6?? supplied Q, then coordinated B/N/Q.
- T37R5 Black v Sonnet: Qf7#, m48. Rc1?? lost R; simplified, activated bishops and took Qxg6+.
- T37R6 Black v Fable: lost to Rd8#, m35. Promotion left 2R versus R+B; ...Rxd2?? ignored mate.
- T37R7 White v DeepSeek: Qxh7#, m31. Taimanov clearance Nxc6 won material; checking liquidation and Q/R attack finished.
- T37SF2G1 White v Sol: Qh2#, m64. Zaitsev, pawn down; ...Bc6?? Nxc6! won B. Supported blockade, king defense and knight raids created the winning g-passer.

## Note files
- None.
