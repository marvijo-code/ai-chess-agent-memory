# Chess memory

## Move discipline
- MATE BEFORE MATERIAL, including queenless positions. T37R6 after ...Rxb1+ Kh2, Kg8 remained boxed by f7/g7/h7 and White threatened Rd8#. ...Rxd2?? collected B and lost immediately. Neither Rb1 nor Rd2 could capture Rd8 or block e8/f8. Check actual blocking squares, not whether a rook can reach rank eight.
- A FORCING SEQUENCE ENDS WHEN THE OPPONENT HAS A NEW THREAT. Kh2 answered my check AND preserved mate. Restart checks/captures/threats after every reply; an earlier calculated gain is only a candidate. A new capture is not an automatic recapture.
- LUFT BEFORE COLLECTION: with heavy pieces active and my king boxed, create a safe escape or control the mating entry. In T37R6 examine ...h6 before taking Bd2; h7 would become a flight against Rd8+. No verified best replacement supplied. Queens off does not settle king safety.
- Before every move inspect changed attacks, then checks, captures and threats on the proposed board. Count legal defenders through actual blockers; include pawn diagonals, every knight and backward bishop captures. Checks and supported pieces can still lose material.
- VACATED SCREEN: before recapturing, trace every line the enemy mover opened. T37R3 ...Nf6xd5 cleared Bg5-f6-e7-d8 against Qd8. exd5?? missed Bxd8, winning Q for B after ...Nxd8. My feared ...Bb4+ was impossible because d6 blocked Bf8. Verify the alleged refutation's path.
- REMOVED DEFENDER + CLEARANCE WITH TEMPO: T37R7 ...Be7xf6 abandoned Nc5's bishop guard. My Nd4 still screened Be3-c5; Nxc6! cleared that diagonal while attacking Qd8. After ...bxc6, Bxc5 won N and attacked Rf8. Scan the departed piece's OLD guards, then moves that uncover attacks with tempo.
- PAWN GEOMETRY: a white pawn on c6 attacks b7/d7, never Ra8. T37R3 dxc6 recovered N; ...Bd7?? then put B directly on its capture square. Inspect every newly placed enemy piece for plain pawn captures.
- KING APPROACH = NEW ATTACK: T37R3 Rb7 followed by ...Ka6 left R capturable; h7 allowed ...Kxb7. Promotion still won, but the rook loss was unnecessary. After each enemy king move inspect adjacent loose pieces.
- OWN KING CAN SCREEN OWN QUEEN: Kc6 blocked Qd6's sixth-rank control and allowed ...Ka6. Recompute flights and sliding attacks after king moves.
- MATERIAL FROM THE BOARD, never commentary. T37R5 Sonnet called the position level after losing R; T37R7 DeepSeek claimed a pawn lead while losing N. T37R6 my extra B did not persist through later sacrifices and captures. Recount after liquidation and promotion.
- QUEEN CHALLENGE MAY OFFER A FREE QUEEN. T37R4 ...Qb6 attacked Qc7 but had no recapturer after Qxb6. ...Nd7 then attacked Qb6 without defending Na5; Qxa5 escaped and won N. Verify guards independently of the claimed purpose.
- DOUBLE ATTACK IS NOT AN EVALUATION. T37R4 Qc7? hit Na5/d6, yet was marked a mistake; ...Qb6?? supplied the win. Calculate the strongest forcing reply before celebrating two targets. No verified replacement stored.
- A ROOK TRADE NEEDS A SECOND PIECE TO RECAPTURE. T37R5 Rc1?? moved White's LAST rook from e1; Be3 could not recapture because Nd2 blocked e3-d2-c1. ...Rxc1+ won R. Name recapturers on the resulting board, excluding the mover itself.
- TRACE EACH GUARD INDEPENDENTLY: T37R6 Nd2 blocked Qd1-d3, so Rc1?? against Qc3 allowed ...Qxd3! winning B; imagined Qxd3 was illegal. After the queen exchange, Be3 blocked Re1-e4 and ...Nxe4 won P. One cleared line does not clear another.
- CHECKS CAN LOSE TO REMOTE QUEEN DEFENSE. T37R5 ...Qd3 guarded g6 through e4/f5; Qxg6+ lost Q to ...Qxg6. Inspect complete queen diagonals even beside an exposed king.

## Conversion and endgames
- MATERIAL COUNTERPLAY DOES NOT ANSWER MATE. T37R6 the b-pawn promotion justified calculating past bishop losses, but not ignoring Rd8#. Audit final checks, flights and blocks BEFORE liquidation, then repeat after changed replies.
- PROMOTION CAN BUY A MATERIAL SURPLUS WITHOUT KEEPING Q. T37R6 ...b1=Q induced Rxb1 Rxb1+, leaving 2R against R+B. Taking Bd2 immediately was unnecessary and fatal. Consolidate king safety before extending a gain.
- FORKS: CHECKING CAPTURES CAN BE STRONGER THAN THE LARGEST TARGET. T37R7 Na4 hit Qb2 and Nb6 forked Ra8/Bd7. After ...Qxe2, Nxd7+ and Nxf6+ removed both bishops; ...gxf6 exposed the king. Qg8+ then drove Ke8 away and allowed Qxa8. Calculate the full liquidation instead of automatically choosing Nxa8.
- DEVELOP WITH THREATS WHILE KEEPING DEFENSES. T37R7 Rad1 activated the last piece; later Rde1 hit Qe4 while Rf1 retained f4's guard. Qxc6/Qxe6+ removed central pawns and opened entry squares. With a large surplus, active defended pieces beat unnecessary pawn collection.
- QUIET MATE MOVES: T37R7 Qf7 with Re7 against Kh6 threatened Qxh7#. On Qxh7, vacating f7 cleared Re7-f7-g7-h7 to protect Q; f4 controlled g5. List captures, checks and flights before relying on the threat. A rook's support can become clear only after the queen moves.
- KING ACTIVITY NEEDS A TARGET AND RETURN ROUTE. T37R2 my king chased f4 while Kc5+B approached d5; ...Kh6?? moved farther from the chain. An excursion is not progress if the enemy liquidates my center first.
- SOLE BISHOP DEFENDER CAN FAIL AGAINST K+B. Ba8 guarded d5, which guarded c4; Bxd5 Bxd5 Kxd5 removed both central pawns. Calculate through the final king recapture and evaluate the pawn ending BEFORE trading bishops.
- EXTRA PAWN IS NOT A PLAN. White invaded the a-file and blockaded connected passers with Kd4. Compare entries, blockade strength and targets before simplifying. Passers need a way to dislodge the blockader.
- SEPARATED PASSERS STRETCH A LONE KING. After losing the center, opposition did not save me against b- and f-pawns; taking f6 let b queen. Count promotion tempi and arrival squares, not just central king placement.
- EXTRA ROOK: remove active enemy pieces and central pawns, then promote safely. Guard the surviving rook even when promotion seems certain. With Q versus bare K, restrict flights, approach with K and check stalemate before quiet moves.
- RETURN PART OF A SURPLUS TO REMOVE COUNTERPLAY. T37R5 ...Nb3 induced Nxb3 axb3. Against Qd1, supported ...Rc2 screened d1-c2-b3. Bxc2 bxc2! Qxc2 left an extra B without rooks. Finish the calculated recapture; ...bxc2 was marked the only good move.
- RETREAT AFTER THE GAIN WHEN A SECOND CAPTURE WASTES IT. T37R5 after ...Rxc1+ Kh2, ...Rc8 saved the extra R; ...Rxb1 would allow Nd2xb1. A won piece does not make the next capture safe.
- ACTIVATE THE EXTRA MINOR WITH PAWN BREAKS. T37R5 ...g6/...Nh5 prepared ...f5; exf5 Bxf5 developed with tempo on Qd3. ...Be4 hit Nf3/d5; ...Bxd5 recovered the center with Qb7 supporting B. Verify support through cleared diagonals.
- CLEAR MY BISHOP'S DIAGONAL BEFORE COUNTING SUPPORT. T37R4 exf5 opened Bb1-c2-d3-e4-f5. After ...gxf5, Nxf5+ was protected by Bb1; N supported Qe7 and covered g7/h6/g3.
- CHECK PAWN MATES TOO. T37R4 Kh5 faced Qg7/Nf5 and g2: g4# checked from g4. Qg7 covered g6/g5/g4/h6; Nf5 covered h4/h6/g3. Verify captures and flights rather than searching queen checks alone.
- QUEEN + KNIGHT: list N's actual support squares before adjacent queen checks. T37R5 Nf4 supported Qe2/Qg2/Qxh3, NOT Qf3. ...Qh7 confined Kg5; ...Ne6+ forced Kf6 and ...Qf7# used Kg8's protection of f7 and Ne6's control of g5.

## White opening: Taimanov 6.Be2
- T37R7 versus DeepSeek: e4/Nf3/d4/Nxd4/Nc3 against ...c5/...e6/...Nc6/...a6; Be2, O-O, Be3 and f4 against ...Be7/...Nf6/...O-O. This solid setup suits me; no White moves marked adverse, but the win does not establish a forced opening edge.
- Against ...d5, e5 gained space with tempo on Nf6. After ...Nd7, Qe1-g3 aimed at the king; ...Nc5 placed N behind my Nd4 screen on Be3's diagonal. ...f6 challenged e5; exf6 Bxf6?? removed Nc5's Be7 guard. Nxc6 attacked Qd8 AND uncovered Bxc5. Remember the geometry, not an automatic combination in every Taimanov.
- Bxc5 also attacked Rf8 because ...f6 had vacated f7. After ...Bd7, Bxf8 Kxf8 increased the surplus and exposed K. Rad1 developed; ...Qb6+ was met by Kh1. Against ...Qxb2 attacking Nc3, Na4 gained tempo on Q and prepared Nb6.
- The checking knight liquidation after Nb6 kept the initiative despite ...Qxe2. Check all checks before grabbing Ra8. Black's pawn raids left the king and remaining pieces vulnerable; count the full board after each exchange.

## Black opening: Closed Ruy Lopez, Chigorin
- T37R5 Sonnet and T37R6 Fable: ...a6/...b5, ...Nf6/...Be7, castle, ...d6; against c3/d4 use ...Na5, ...c5, ...Qc7. After ...cxd4 cxd4 return ...Nc6. Both used Nb3/Be3; ...a5-a4 sent Nb3 back to d2.
- Sonnet branch: ...Bd7/...Rac8; Rc1/Bb1 opened the c-file against Qc7, so ...Qb7 released Nc6 BEFORE d5. ...Rfe8/...Bf8 supported d6. After a3/d5, ...Na5 was available. Win came from Rc1?? losing R, not a forced opening edge.
- Distinguish Qb7 from Qc7 remaining behind Nc6: a routine rook move can allow d5 with a pin. Refresh the pin whenever Q moves.
- Fable played earlier 17.d5?! before Rc1; my 17...Na5?! was also marked inaccurate. Do not automatically import the Sonnet retreat. Compare alternatives on the current board; no verified best replacement supplied.
- Fable's Bd3/b3 denied c4 but left Bd3 behind Nd2's blocked queen guard. ...Rac8/...Qc3 met Rc1?? with ...Qxd3! Nf1 finally cleared Qd1-d3; ...Qxd1 simplified. Be3 still blocked Re1-e4, so ...Nxe4 won P.
- Later ...Nxb3 and the b-pawn advance produced promotion and a surplus, but required full-board calculation. Never store this as automatic conversion: the loss came from ignoring the back rank.

## White opening: Closed Ruy Lopez, Chigorin
- T37R4 Sol: Bb5/Ba4/Bb3, O-O, Re1, c3, h3, Bc2 and d4 against ...Na5/...c5/...Qc7. After ...cxd4, cxd4 restored the center; this recapture and Bb3 were marked only good moves on their boards.
- Nb3 reinforced d4; after ...a5, Be3 and ...a4, Nbd2 supported e4. Rc1/Bb1 cleared the c-file, then Nf1-g3 improved N. Sol used ...Rac8/...Qb7 and ...Bd8-b6. Qb7 releases Nc6: do not import pinned-knight d5 tactics.
- d5 gained space and blocked Bb6 but allowed ...Na5-c4. Bxb6 traded attacked Be3; b3 displaced Nc4. Playable development, not a demonstrated forced advantage.
- Rxc8 removed a rook pair before Nhf5. After ...Bxf5, Nxf5 retained N on f5 rather than committing the e-pawn. ...Rc7 guarded e7, so Ne7+ needed fresh calculation.
- QUEEN LEAVES d1 = b3 LOSES ITS GUARD. Qf3?! abandoned d1-c2-b3. ...g6 displaced Nf5; Ne3 uncovered Qf3's attack on Nf6, answered by ...Kg7. Qd1 restored b3's guard. Compare a sortie's threat with its defensive tempo cost.
- Qd2 guarded c1 and enabled Rc1; ...Rxc1+ Qxc1 completed the exchange. Black's a3/b4 constrained me and ...Qd4 activated Q. Rook trades did not establish an advantage; Qc7? was rescued by ...Qb6??.

## White opening: Sicilian Ndb5
- T37R3 GLM: Open Sicilian ...e6/...Nf6/...Nc6, Ndb5, ...d6, Bf4, ...e5, Bg5, ...a6, Na3, ...b5, Nd5. ...e5 was marked Black's only good move: expect the bishop tempo and weakened d5 square.
- With Bg5 facing Qd8 through Nf6, ...Nxd5 can abandon Q. Inspect Bxd8 before exd5. My exd5?? squandered this; dxc6! after ...Qxg5 was the required recovery.
- Qf3 guarded c6 through e4/d5 and g2 diagonally. ...Bd7?? lost B to cxd7+, leaving N for P after ...Kxd7. This gift, not an opening advantage, decided the game.
- 17.O-O was marked a mistake; no verified replacement. Compare immediate tactics and activity even after queens are exchanged.
- Na3 returned through c2 after c3, then reached e3/d5 to blockade d6 and exchange Bf6. ...a5 removed a6's guard of b5: Bxb5+ also attacked Re8, winning the exchange. Pawn advances can expose a target and checking fork together.

## Black opening: Spanish Four Knights
- T37R2 SF19: against Nf3/Nc3/Bb5 use ...Nc6/...Nf6/...Bb4 and castle.
- Played: 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Bd6 11.d4 Qh4 12.g3 Qxd4.
- ...e4 attacks Nf3 while White takes Nc6; complete both pawn removals to restore balance. Bd6+Qh4 threatens Qxh2#, allowing ...Qxd4 after g3 with tempo on Bc4. Both Q moves were marked only good moves; verify the matching board.
- ...Bg4 attacked Qf3 with Qd4 supporting B. Be3 counterattacked Qd4; ...Bxf3 and Bxd4 exchanged queens, retaining the extra pawn. Count both captures.
- ...b5/...a6 and axb5 ...axb5 opened the a-file for Ra6-a7. Prepare to contest files when changing structure. ...Ra8 with Be4 supporting a8 enabled liquidation of both rook pairs.
- Bxd6+ ...cxd6 created a passed d-pawn. King centralization supported it, but ...b4 liquidation let White blockade with Kd4. Preserve the means to challenge a blockade.

## Opponents and clock
- DeepSeek V4.1 Flash, T37R7 Black: Taimanov ...a6/...Be7/...Nf6, ...d5 versus f4, then ...Nd7-c5 and ...f6. ...Bxf6?? forgot Be7's guard of Nc5; missed the clearance combination and later raided b2/c2/e2 while checking captures dismantled its pieces. Comments miscounted material and invented Bd7's recapture of Na8. Verify independently. One game, zero illegal attempts; do not generalize a forced opening win.
- Fable 5.1, T37R6 White: Closed Ruy Nb3/Be3, early d5, Bd3/b3. Rc1?? overlooked Nd2 blocking Qd1-d3 and then tried illegal Qxd3; also missed Be3 blocking Re1-e4. Found active resistance with Nd4/Rxe7/Rxd7, Bd2 against promotion and Rd8#. Earlier guard errors do not imply weak finishing. One illegal; finished 7:01.
- Fable spent 41-98 seconds around the bishop loss and 62-83 on late resistance. Kh2 commentary identified mate before I took Bd2. Commentary never replaces my board scan.
- Sonnet 5.5, T37R5 White: main-line Closed Ruy, Nb3/Be3, Rc1/Bb1, Qe2/a3/d5. Rc1?? imagined recapture from a vacated rook square and ignored Nd2 blocking Be3. Qxg6+ missed Qd3's diagonal. Coherent opening; independently verify pins, guards and material. Repeated 56-68 second thinks, zero illegal; finished 5:56.
- Sol, T37R4 Black: Chigorin ...a5-a4, ...Rac8/...Qb7, ...Bd8-b6, ...Na5-c4 and ...g6 versus Nf5. Kept queenside pressure and centralized Qd4, then hung Qb6 while claiming to defend two targets. ...Nd7 falsely claimed to guard Na5. Expect coherent counterplay before an error. Zero illegal; finished 13:54.
- GLM 5.3 Flash, T37R3: ...e6/...Nf6/...Nc6 into ...e5/...b5 against Ndb5. Found ...Qxg5 after my missed queen capture, but put Bd7 on c6's pawn diagonal and miscounted guards/material. Took my exposed rook with K: never assume it misses a simple capture. One illegal.
- SF19, T37R2: depth 4, essentially instant. Found the central blockade, won both central pawns and promoted, then allowed repetition against bare K. One shallow-search failure, not a reliable escape plan.
- In a lost ending keep legal resistance, escapes and an exact repetition count including side to move. Repeating a king square alone is not repeating a position.
- 900+10: routine moves 5-15 seconds; longer for critical captures, races or irreversible decisions. Spend time on concrete paths and final recaptures, not elaborating plans. Long thought does not validate the scan.
- T37R6 finished 14:20, zero illegal; fatal ...Rxd2?? took THREE seconds. Reserve 10-20 seconds for a fresh threat scan after a forcing sequence, especially with a boxed king. T37R7 used 32 seconds on Nxc6 and 35 on quiet Qf7; finished with over 13 minutes and zero illegal. Critical time should resolve a specific tactical question.

## Record
- T37R2 Black v SF19: draw by repetition, m97. Won P, lost the central chain after a king excursion, survived Q versus bare K. Result does not validate conversion.
- T37R3 White v GLM: Qa3#, m51. Missed Bxd8, recovered with dxc6, won B after ...Bd7, simplified and promoted. Avoidable rook loss.
- T37R4 White v Sol: g4#, m43. Chigorin; Qf3?! lost time, Qc7? rescued by ...Qb6??. Took Q/Na5 and coordinated Bb1/Nf5.
- T37R5 Black v Sonnet: Qf7#, m48. ...Qb7 released Nc6; Rc1?? lost R. Returned part of surplus, activated bishops with ...f5, took Qxg6+.
- T37R6 Black v Fable: lost to Rd8#, m35. Won B/P; promotion left 2R versus R+B. ...Rxd2?? ignored mate with ample clock.
- T37R7 White v DeepSeek: Qxh7#, m31. Taimanov 6.Be2; ...Bxf6?? abandoned Nc5 to clearance Nxc6. Checking knight liquidation and Qg8+ won remaining pieces; Q/R attack finished. No White move marks.

## Note files
- None.
