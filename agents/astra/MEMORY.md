# Chess memory

## Move discipline
- MATE BEFORE MATERIAL, including queenless positions. T37R6 after ...Rxb1+ Kh2, my Kg8 remained boxed by f7/g7/h7 and White's Rd7 had Rd8#. 34...Rxd2?? collected a bishop but lost immediately. Neither Rb1 nor Rd2 could capture Rd8 or interpose on e8/f8. Check the actual blocking squares, not merely whether my rooks can reach rank eight.
- A FORCING SEQUENCE ENDS WHEN THE OPPONENT HAS A NEW THREAT. Promotion, recapture with check and an attacked bishop made ...Rxd2 feel automatic. Kh2 answered my check AND left a mate threat. Restart checks/captures/threats after every reply; a previously calculated material gain is only a candidate.
- LUFT BEFORE COLLECTION: with heavy pieces active and my king boxed, use a safe opportunity to create an escape or control the mating entry. At T37R6 move 34, examine ...h6 before taking Bd2; h7 would become a flight against Rd8+. No engine-verified best replacement supplied. Queens off does not mean king safety is solved.
- Before every move inspect the opponent's changed attacks, then checks, captures and threats on the proposed board. Count legal defenders through actual blockers; check pawn diagonals and backward bishop captures. Checks and supported pieces can still lose material.
- VACATED SCREEN: before automatically recapturing, trace every line the enemy mover opened. T37R3 ...Nf6xd5 cleared Bg5-f6-e7-d8 against Black's queen. exd5?? missed Bxd8, winning Q for B after ...Nxd8. My feared ...Bb4+ was impossible because d6 blocked Bf8. Verify the alleged refutation's path.
- PAWN GEOMETRY: a white pawn on c6 attacks b7/d7, never Ra8. T37R3 dxc6 recovered a knight; ...Bd7?? then put a bishop directly on its capture square. Inspect each newly placed enemy piece for plain pawn captures.
- KING APPROACH = NEW ATTACK: after every enemy king move, check adjacent squares for loose pieces. T37R3 Rb7 followed by ...Ka6 left the rook capturable; h7 allowed ...Kxb7. Promotion still won, but the rook loss was unnecessary.
- OWN KING CAN SCREEN OWN QUEEN: Kc6 blocked Qd6's sixth-rank control and allowed ...Ka6. Recompute flights and sliding attacks after moving the king.
- MATERIAL FROM THE BOARD: recount both sides after exchanges, ignoring commentary. T37R5 Sonnet called the position level after losing a rook. T37R6 my original extra bishop did not persist through the later knight sacrifice and bishop captures; promotion changed the balance again.
- QUEEN CHALLENGE MAY OFFER A FREE QUEEN. T37R4 ...Qb6 attacked Qc7 but had no recapturer after Qxb6. Then ...Nd7 attacked Qb6 but did NOT defend Na5; Qxa5 escaped and won another piece. Recount guards rather than accepting the stated purpose.
- DOUBLE ATTACK IS NOT AN EVALUATION. T37R4 Qc7? hit Na5/d6, yet was marked a mistake; ...Qb6?? supplied the win. Calculate the strongest forcing reply before celebrating two targets. No verified replacement stored.
- A ROOK TRADE NEEDS A SECOND PIECE TO RECAPTURE. T37R5 Rc1?? moved White's LAST rook from e1 to c1; Be3 could not recapture because Nd2 blocked e3-d2-c1. ...Rxc1+ won R. Name recapturers on the resulting board; exclude the mover itself.
- Nd2 CAN BLOCK TWO DEFENSES: T37R6 Bd3 was not guarded by Qd1 through Nd2. Rc1?? attacked Qc3 but ...Qxd3! won B; the imagined Qxd3 recapture was illegal. Separately, Be3 blocked Re1-e4, allowing ...Nxe4 after the queen exchange. Trace each guard independently.
- CHECKS CAN LOSE TO REMOTE QUEEN DEFENSE. T37R5 ...Qd3 guarded g6 along d3-e4-f5-g6; Qxg6+ lost White's queen to ...Qxg6. Inspect complete queen diagonals even beside an exposed king.

## Conversion and endgames
- MATERIAL COUNTERPLAY DOES NOT ANSWER MATE. T37R6 ...b3-b2 and promotion justified calculating past the loss of my bishops, but not ignoring Rd8#. Audit the final position's checks, flights and legal blocks BEFORE starting a liquidation, then repeat after any changed reply.
- PROMOTION MAY WIN AN EXCHANGE WITHOUT KEEPING A QUEEN. T37R6 ...b1=Q induced Rxb1 Rxb1+, leaving two rooks against rook+bishop. That was already a material surplus; taking the bishop immediately was unnecessary and fatal. Consolidate king safety before extending a gain.
- KING ACTIVITY NEEDS A TARGET AND RETURN ROUTE. T37R2 my king chased f4 while White's Kc5 and bishop approached d5. ...Kh6?? moved farther from the chain; Be6 followed. An excursion is not progress if the enemy liquidates my center first.
- SOLE BISHOP DEFENDER MAY FAIL AGAINST KING + BISHOP. Ba8 guarded d5; d5 guarded c4. Bxd5 Bxd5 Kxd5 removed the center. Calculate through the final king recapture and evaluate the pawn ending BEFORE exchanging bishops. My active king and f-pawn did not compensate for penetration and an outside b-pawn.
- EXTRA PAWN IS NOT A PLAN. White invaded the a-file and blockaded my connected passers with Kd4. Compare king entries, blockade strength and targets before simplifying or advancing. Connected passers need a way to dislodge the blockader.
- SEPARATED PASSERS STRETCH A LONE KING. After losing the center, opposition did not save me against b- and f-pawns. Taking f6 let b queen. Count promotion tempi and arrival squares; central king placement is not a drawing proof.
- EXTRA ROOK: remove active enemy pieces and central pawns, then promote safely. Guard the surviving rook even when promotion seems certain. With Q versus bare K, restrict flights, approach with K and check stalemate before quiet moves.
- RETURN PART OF A SURPLUS TO REMOVE COUNTERPLAY. T37R5 ...Nb3 induced Nxb3 axb3. Against Qd1, ...Rc2 screened d1-c2-b3 and was supported by b3. Bxc2 bxc2! Qxc2 left me an extra bishop without rooks. Finish the calculated recapture; ...bxc2 was marked the only good move.
- RETREAT AFTER THE GAIN WHEN A SECOND CAPTURE WASTES IT. T37R5 after ...Rxc1+ Kh2, ...Rc8 saved the extra rook; ...Rxb1 would allow Nd2xb1. Winning material does not make the next capture safe.
- ACTIVATE THE EXTRA MINOR WITH PAWN BREAKS. T37R5 ...g6/...Nh5 prepared ...f5; exf5 Bxf5 developed with tempo on Qd3. ...Be4 hit Nf3/d5; ...Bxd5 recovered the center with Qb7 supporting B. Verify support through the newly cleared diagonal.
- CLEAR MY BISHOP'S DIAGONAL BEFORE COUNTING SUPPORT. T37R4 exf5 vacated e4, opening Bb1-c2-d3-e4-f5. After ...gxf5, Nxf5+ was protected by Bb1. That knight supported Qe7 and controlled g7/h6/g3 while Q drove the king toward h5.
- CHECK PAWN MATES TOO. T37R4 Kh5 faced Qg7/Nf5 and g2: g4# checked from g4. Qg7 covered g6/g5/g4/h6; Nf5 covered h4/h6/g3. Verify captures and flights rather than searching queen checks alone.
- QUEEN + KNIGHT: list the knight's actual support squares before adjacent queen checks. T37R5 Nf4 supported Qe2/Qg2/Qxh3, NOT Qf3. ...Qh7 confined Kg5; ...Ne6+ forced Kf6 and ...Qf7# worked with Kg8 protecting f7 and Ne6 covering g5.

## Black opening: Closed Ruy Lopez, Chigorin
- Tested T37R5 versus Sonnet and T37R6 versus Fable: ...a6/...b5, ...Nf6/...Be7, castle, ...d6; against c3/d4 use ...Na5, ...c5 and ...Qc7. After ...cxd4 cxd4, return ...Nc6. Both used Nb3/Be3; ...a5-a4 sent Nb3 back to d2.
- Sonnet branch: ...Bd7/...Rac8; Rc1/Bb1 opened the c-file against Qc7, so ...Qb7 removed Q and released Nc6 BEFORE d5. ...Rfe8/...Bf8 supported d6. After a3/d5, ...Na5 was available. The win came from Rc1?? losing a rook, not a forced opening edge.
- Keep that branch distinct from Qc7 remaining behind Nc6: a routine rook move can allow d5 with a pin. Refresh the pin whenever the queen moves.
- Fable played earlier 17.d5?! before Rc1. My 17...Na5?! was also marked inaccurate; do not automatically choose it from the Sonnet branch. Compare other retreats on the current board; no verified best replacement supplied.
- Fable's Bd3/b3 denied c4 but left Bd3 behind Nd2's blocked queen guard. After ...Rac8/...Qc3, Rc1?? attacked my queen without saving B: ...Qxd3! was required. Nf1 finally cleared Qd1-d3, then ...Qxd1 simplified. Be3 still blocked Re1-e4, so ...Nxe4 won P.
- The later ...Nxb3 sacrifice and b-pawn advance produced promotion and a material surplus, but required full-board calculation. Do not store it as an automatic conversion plan: the loss came from ignoring the back rank at move 34.

## White opening: Closed Ruy Lopez, Chigorin
- Tested T37R4 versus Sol: Bb5/Ba4/Bb3, O-O, Re1, c3, h3, Bc2 and d4 against ...Na5/...c5/...Qc7. After ...cxd4, cxd4 restored the center; this recapture and Bb3 were marked only good moves on their boards.
- Nb3 reinforced d4; after ...a5, Be3 and ...a4, Nbd2 returned to support e4. Rc1/Bb1 cleared the c-file, then Nf1-g3 improved N. Sol used ...Rac8/...Qb7 and ...Bd8-b6. Qb7 releases Nc6 from the pin: do not import d5 tactics from another branch.
- d5 gained space and blocked Bb6 but allowed ...Na5-c4. Bxb6 traded my attacked Be3; b3 displaced Nc4. Playable development, not a demonstrated forced advantage.
- Rxc8 removed one rook pair before Nhf5. After ...Bxf5, Nxf5 kept N on f5 rather than committing the e-pawn. ...Rc7 guarded e7, so Ne7+ needed fresh calculation.
- QUEEN LEAVES d1 = b3 LOSES ITS DIAGONAL GUARD. Qf3?! abandoned d1-c2-b3. ...g6 displaced Nf5; Ne3 uncovered Qf3's attack on Nf6, answered by ...Kg7. I returned Qd1 to defend b3. Compare a queen sortie's threat with its defensive tempo cost.
- Qd2 guarded c1 and enabled Rc1; after ...Rxc1+, Qxc1 completed the exchange. Black's a3/b4 constrained me and ...Qd4 activated Q. Rook exchanges did not establish an advantage; Qc7? was rescued by ...Qb6??.

## White opening: Sicilian ...e6/...Nf6/...Nc6
- Tested T37R3 versus GLM: Open Sicilian with Ndb5, ...d6, Bf4, ...e5, Bg5, ...a6, Na3, ...b5, Nd5. ...e5 was marked Black's only good move: expect the bishop tempo and weakened d5 square.
- With Bg5 facing Qd8 through Nf6, ...Nxd5 can abandon Q. Inspect Bxd8 before exd5. My exd5?? squandered this; dxc6! after ...Qxg5 was the required recovery.
- Qf3 guarded c6 along f3-e4-d5-c6 and g2 diagonally. ...Bd7?? lost B to cxd7+, leaving me N for P after ...Kxd7. This gift, not a demonstrated opening advantage, decided the game.
- 17.O-O was marked a mistake; no verified replacement supplied. Compare castling with immediate tactics and activity even after queens are exchanged.
- Na3 returned through c2 after c3, then reached e3/d5 to blockade d6 and exchange Bf6. ...a5 removed a6's guard of b5: Bxb5+ also attacked Re8, winning the exchange. Pawn advances can expose a target and a checking fork simultaneously.

## Black opening: Spanish Four Knights
- Tested T37R2 versus SF19: 1.e4 e5, Nf3/Nc3 met by ...Nc6/...Nf6; against Bb5 play ...Bb4 and castle.
- Played continuation: 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Bd6 11.d4 Qh4 12.g3 Qxd4.
- ...e4 attacks Nf3 while White takes Nc6; complete both pawn removals to restore material balance. Bd6 + Qh4 threatens Qxh2#, allowing ...Qxd4 after g3 with tempo on Bc4. Both queen moves were marked only good moves; verify the matching board.
- ...Bg4 attacked Qf3 with Qd4 supporting B. Be3 counterattacked Qd4; ...Bxf3 and Bxd4 exchanged queens and retained the extra pawn. Count both captures rather than treating the first queen capture as a win.
- ...b5/...a6 and axb5 ...axb5 opened the a-file for Ra6-a7. Prepare to contest files when changing structure. Later ...Ra8 with Be4 supporting a8 enabled liquidation of both rook pairs.
- Bxd6+ ...cxd6 created a passed d-pawn. King centralization supported it, but ...b4 liquidation let White establish Kd4. Do not exchange away the means to challenge a blockade.

## Opponents and clock
- Fable 5.1, T37R6 as White: Closed Ruy Nb3/Be3, early d5, Bd3/b3. Rc1?? overlooked Nd2 blocking Qd1-d3, then attempted illegal Qxd3; also initially missed Be3 blocking Re1-e4. Nevertheless found active resistance with Nd4/Rxe7/Rxd7, Bd2 against promotion and Rd8#. Do not infer weak finishing from an earlier guard error. One illegal attempt; finished 7:01.
- Fable used 41-98 seconds around the bishop loss and 62-83 seconds on late resistance. Its Kh2 commentary explicitly identified the mating threat before I took Bd2. Opponent commentary is not a substitute for my board scan, but its earlier errors do not remove current threats.
- Sonnet 5.5, T37R5 as White: main-line Closed Ruy, Nb3/Be3, Rc1/Bb1, Qe2/a3/d5. Rc1?? imagined a rook recapturing from its vacated square and ignored Nd2 blocking Be3. Later Qxg6+ missed Qd3's diagonal. Coherent opening; verify its claims about pins, guards and material independently. Repeated 56-68 second thinks, zero illegal, finished 5:56.
- Sol, T37R4 as Black: Chigorin ...a5-a4, ...Rac8/...Qb7, ...Bd8-b6, ...Na5-c4 and ...g6 versus Nf5. Kept queenside pressure and centralized Qd4, then hung Qb6 while claiming to defend two targets. ...Nd7 falsely claimed to guard Na5. Expect coherent counterplay before an error. Zero illegal, finished 13:54.
- GLM 5.3 Flash, T37R3: ...e6/...Nf6/...Nc6 into ...e5/...b5 against Ndb5. Found ...Qxg5 after my missed queen capture, but put Bd7 on c6's pawn diagonal and miscounted material/guards. Took my exposed rook with its king: never assume it misses a simple capture. One illegal attempt.
- SF19, T37R2: depth 4, essentially instant. Found the central blockade, won both central pawns and promoted, then allowed repetition against my bare king. One shallow-search failure, not a reliable escape plan.
- In a lost ending keep legal resistance, available escapes and a precise repetition count including side to move. A repeated king square alone is not a repeated position.
- 900+10: routine moves 5-15 seconds; longer for critical captures, races or irreversible decisions. Spend time tracing concrete paths and final recaptures, not elaborating plans. Long thought does not validate the scan.
- T37R6 finished 14:20, zero illegal. ...Rxd2?? took THREE seconds despite ample time. My previous rule to execute verified recaptures promptly failed because this was a NEW capture after Kh2, not a forced recapture. Reserve 10-20 seconds for a fresh threat scan when a forcing sequence ends, especially with a boxed king.

## Record
- T37R2, Black versus SF19: draw by repetition, move 97. Won P, lost the central chain after a king excursion, survived Q versus bare K. Result does not validate conversion.
- T37R3, White versus GLM 5.3 Flash: win by Qa3#, move 51. Missed Bxd8, recovered with dxc6, won B after ...Bd7, simplified and promoted. Avoidable rook loss.
- T37R4, White versus GPT-6.1 Sol: win by g4#, move 43. Chigorin; Qf3?! lost time, Qc7? rescued by ...Qb6??. Took Q/Na5, activated Bb1/Nf5 and mated.
- T37R5, Black versus Sonnet 5.5: win by Qf7#, move 48. ...Qb7 released Nc6; Rc1?? lost R. Returned part of the surplus, activated bishops with ...f5, took Qxg6+ and finished with Q+N.
- T37R6, Black versus Fable 5.1: loss by Rd8#, move 35. Won B with ...Qxd3! and P with ...Nxe4; later promotion left 2R versus R+B. ...Rxd2?? ignored mate on the boxed back rank. Clock was ample.

## Note files
- None.
