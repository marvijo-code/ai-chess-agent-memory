# Chess memory

## Move discipline
- Before every move inspect the opponent's changed attacks, then checks, captures and threats on the proposed board. Count legal defenders through actual blockers; check pawn diagonals and backward bishop captures. Checks and supported pieces can still lose material.
- VACATED SCREEN: before automatically recapturing, trace every line the enemy mover opened. T37R3 ...Nf6xd5 cleared Bg5-f6-e7-d8 against Black's queen. 11.exd5?? missed Bxd8 and allowed ...Qxg5. Bxd8 wins Q for B after ...Nxd8. My feared ...Bb4+ was impossible because d6 blocked Bf8. Verify the alleged refutation's path before rejecting a winning capture.
- PAWN GEOMETRY: a white pawn on c6 attacks b7/d7, never Ra8. T37R3 dxc6 recovered a knight; ...Bd7?? then put a bishop directly on that pawn's capture square. Inspect each newly placed enemy piece for plain pawn captures.
- KING APPROACH = NEW ATTACK: after every enemy king move, check adjacent squares for loose pieces. T37R3 Rb7 followed by ...Ka6 left the rook capturable; h7 allowed ...Kxb7. Promotion still won, but the rook loss was unnecessary.
- OWN KING CAN SCREEN OWN QUEEN: Kc6 blocked Qd6's sixth-rank control and allowed ...Ka6. Qa3# still worked because Kc6 covered b5/b6/b7 and Q controlled the a-file. Recompute flights after moving the king.
- MATERIAL FROM THE BOARD: count both sides after exchanges, ignoring commentary. T37R3 I had an extra knight for a pawn after ...Kxd7, then an extra rook after Bxe8/Nxf6+. T37R5 Sonnet called the position level after losing a rook, then described winning my rook for B+P without counting the existing deficit.
- QUEEN CHALLENGE MAY OFFER A FREE QUEEN. T37R4 ...Qb6 attacked Qc7 but had no recapturer after Qxb6. Then ...Nd7 attacked Qb6 but did NOT defend Na5; Qxa5 escaped and won another piece. Recount guards rather than accepting the stated purpose.
- DOUBLE ATTACK IS NOT AN EVALUATION. T37R4 Qc7? hit Na5/d6, yet was marked a mistake; ...Qb6?? supplied the win. Black's preceding ...Qd4 centralized its queen and pressured e4. Calculate the strongest forcing reply before celebrating two targets. No verified replacement stored.
- A ROOK TRADE NEEDS A SECOND PIECE TO RECAPTURE. T37R5 23.Rc1?? moved White's LAST rook from e1 to c1; there was no rook left on e1. Be3 could not recapture because Nd2 blocked e3-d2-c1. ...Rxc1+ won a whole rook. Name each recapturer on the resulting board; exclude the mover itself.
- CHECKS CAN LOSE TO REMOTE QUEEN DEFENSE. T37R5 ...Qd3 guarded g6 along d3-e4-f5-g6. Qxg6+ simply lost White's queen to ...Qxg6. Inspect queen diagonals as carefully as bishop diagonals, even when the target looks like an exposed pawn beside the king.

## Conversion and endgames
- KING ACTIVITY NEEDS A TARGET AND RETURN ROUTE. T37R2 my king chased f4 while White's Kc5 and bishop approached d5. ...Kh6?? moved farther from the chain; Be6 followed. An excursion is not progress if the enemy liquidates my center first.
- SOLE BISHOP DEFENDER MAY FAIL AGAINST KING + BISHOP. Ba8 guarded d5; d5 guarded c4. Bxd5 Bxd5 Kxd5 removed the center. Calculate through the final king recapture and evaluate the pawn ending BEFORE exchanging bishops. My active king and f-pawn did not compensate for penetration and the outside b-pawn. Repair needed earlier; no verified replacement for ...Kh6 stored.
- EXTRA PAWN IS NOT A PLAN. White invaded the a-file and blockaded my connected passers with Kd4. Compare king entries, blockade strength and targets before simplifying or advancing. Connected passers need a way to dislodge the blockader.
- SEPARATED PASSERS STRETCH A LONE KING. After losing the center, opposition did not save me against b- and f-pawns. Taking f6 let b queen. Count promotion tempi and arrival squares; central king placement is not a drawing proof.
- EXTRA ROOK: remove active enemy pieces and central pawns, then promote safely. T37R3 exchanges removed counterplay, but I still lost the surviving rook unnecessarily. With Q versus bare K, restrict flights, approach with K and check stalemate before quiet moves.
- RETURN PART OF A SURPLUS TO REMOVE COUNTERPLAY. T37R5, already a rook up, ...Nb3 induced Nxb3 axb3. Qd1 attacked b3, but ...Rc2 both screened d1-c2-b3 and was supported by that pawn. After Bxc2, ...bxc2! and Qxc2 left me an extra bishop with no rooks remaining. This was deliberate simplification, not a free rook. ...bxc2 was marked the only good move: finish the calculated recapture.
- RETREAT AFTER THE GAIN WHEN A SECOND CAPTURE WASTES IT. After ...Rxc1+ Kh2, ...Rc8 saved the extra rook. ...Rxb1 would allow Nd2xb1. Winning the rook did not make every following capture profitable.
- ACTIVATE THE EXTRA MINOR WITH PAWN BREAKS. T37R5 ...g6 and ...Nh5 prepared ...f5; exf5 Bxf5 developed with tempo on Qd3. ...Be4 attacked Nf3 and d5; ...Bxd5 recovered the center with Qb7 supporting the bishop. Later ...h6 drove Ng5 to e4, where ...Bxe4 and ...Qxe4 removed the knight and f-pawn. Verify queen support through the newly cleared diagonal.
- CLEAR MY BISHOP'S DIAGONAL BEFORE COUNTING SUPPORT. T37R4 exf5 vacated e4, opening Bb1-c2-d3-e4-f5. After ...gxf5, Nxf5+ was protected by Bb1. That knight supported Qe7 and controlled g7/h6/g3 while the queen drove the king toward h5.
- CHECK PAWN MATES TOO. T37R4 Kh5 faced Qg7/Nf5 and g2: g4# checked from g4. Qg7 covered g6/g5/g4/h6; Nf5 covered h4/h6/g3. Verify all flights and captures rather than restricting the search to queen checks.
- QUEEN + KNIGHT: list the knight's actual support squares before adjacent queen checks. T37R5 Nf4 supported Qe2, Qg2 and Qxh3; it did NOT support Qf3. Against Kg5, ...Qh7 restricted flights; ...Ne6+ forced Kf6 and ...Qf7# worked because Kg8 protected f7 and Ne6 covered g5. Quiet queen confinement can prepare the final knight check.

## Black opening: Closed Ruy Lopez, Chigorin
- Tested T37R5 versus Sonnet: ...a6/...b5, ...Nf6/...Be7, castle, ...d6; against c3/d4 use ...Na5, ...c5 and ...Qc7. After ...cxd4 cxd4, return ...Nc6. White used Nb3/Be3; ...a5-a4 sent Nb3 back to d2.
- Develop ...Bd7 and ...Rac8. When Rc1/Bb1 opens the c-file against Qc7, ...Qb7 removes the queen and releases Nc6 BEFORE a later d5. Then ...Rfe8/...Bf8 supported d6 and cleared the e-file. After a3/d5, ...Na5 was available. Sonnet called Nc6 pinned despite Qb7: use the board, not its description.
- Rxc8 ...Rxc8 left my remaining rook active on c8. White's second Rc1?? failed to a blocked recapture and supplied the advantage; the win does not establish a forced opening edge. This setup reached playable development without any of my moves marked adverse in the supplied review.
- Keep this branch distinct from Qc7 remaining behind Nc6: a routine rook move there can allow d5 with a pin. Do not copy the ...Qb7 plan into a position where the queen has not moved.

## White opening: Closed Ruy Lopez, Chigorin
- Tested T37R4 versus Sol: Bb5/Ba4/Bb3, O-O, Re1, c3, h3, Bc2 and d4 against ...Na5/...c5/...Qc7. After ...cxd4, cxd4 restored the center; this recapture and Bb3 were marked only good moves on their boards.
- Nb3 reinforced d4; after ...a5, Be3 and ...a4, Nbd2 returned to support e4. Rc1/Bb1 cleared the c-file, then Nf1-g3 improved the knight. Sol used ...Rac8/...Qb7 and ...Bd8-b6. Qb7 releases Nc6 from the c-file pin: do not import a d5 tactic from another branch.
- d5 gained space and blocked Bb6 but allowed ...Na5-c4. Bxb6 traded my attacked Be3; b3 displaced Nc4. Playable development, not a demonstrated forced advantage.
- Rxc8 removed one rook pair before Nhf5. After ...Bxf5, Nxf5 kept a knight on f5 rather than committing the e-pawn. ...Rc7 guarded e7, so Ne7+ needed fresh calculation.
- QUEEN LEAVES d1 = b3 LOSES ITS DIAGONAL GUARD. Qf3?! abandoned d1-c2-b3. ...g6 displaced Nf5; Ne3 uncovered Qf3's attack on Nf6, answered by ...Kg7. I returned Qd1 to defend b3. Compare a queen sortie's threat with its defensive tempo cost. No verified improvement stored.
- Qd2 guarded c1 and enabled Rc1; after ...Rxc1+, Qxc1 completed the exchange. Black's a3/b4 pawns constrained me and ...Qd4 activated its queen. Rook exchanges did not establish an advantage; Qc7? was rescued by ...Qb6??.

## White opening: Sicilian ...e6/...Nf6/...Nc6
- Tested T37R3 versus GLM: Open Sicilian with Ndb5, ...d6, Bf4, ...e5, Bg5, ...a6, Na3, ...b5, Nd5. ...e5 was marked Black's only good move: expect the bishop tempo and weakened d5 square.
- With Bg5 facing Qd8 through Nf6, ...Nxd5 can abandon the queen. Inspect Bxd8 before exd5. My 11.exd5?? squandered this; dxc6! after ...Qxg5 was the required recovery.
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
- Sonnet 5.5, T37R5 as White: main-line Closed Ruy, Nb3/Be3, Rc1/Bb1, Qe2/a3/d5. Recognized ...Qb7 removed the pin, then later called Nc6 pinned again. Rc1?? imagined a rook recapturing from its vacated square and ignored Nd2 blocking Be3. Later Qxg6+ missed Qd3's diagonal. One game: coherent opening, but verify its claims about pins, guards and material independently.
- Sonnet spent 56-68 seconds repeatedly in the middlegame, including 57 seconds on Rc1??, and finished 5:56 with zero illegal attempts. Long thought did not prevent simple guard errors. Maintain sound pressure; do not assume a free piece will appear or rely on its clock trouble.
- Sol, T37R4 as Black: Chigorin ...a5-a4, ...Rac8/...Qb7, ...Bd8-b6, ...Na5-c4 and ...g6 versus Nf5. Kept queenside pressure and centralized Qd4, then hung Qb6 while claiming to defend two targets. ...Nd7 falsely claimed to guard Na5. Expect coherent counterplay before an error. Zero illegal attempts; finished 13:54.
- GLM 5.3 Flash, T37R3: ...e6/...Nf6/...Nc6 into ...e5/...b5 against Ndb5. Found ...Qxg5 after my missed queen capture, but put Bd7 on c6's pawn diagonal and miscounted material/guards. Took my exposed rook with its king: never assume it misses a simple capture. One illegal attempt.
- SF19, T37R2: depth 4, essentially instant. Found the central blockade, won both central pawns and promoted, then allowed repetition against my bare king. One shallow-search failure, not a reliable escape plan against Stockfish.
- In a lost ending keep legal resistance, available escapes and a precise repetition count including side to move. A repeated king square alone is not a repeated position.
- 900+10: routine moves 5-15 seconds; longer for critical captures, races or irreversible decisions. T37R3 finished 15:26, zero illegal; a 28-second think still accepted an impossible refutation. T37R2 strategic thinks of 43-62 seconds did not solve the central weakness. Trace concrete paths and final recaptures rather than elaborating plans.
- T37R4 finished 12:53, zero illegal. Qf3/Ne3/Qd1/Qc7 took 23-53 seconds around a queen detour and a marked mistake. Use extra time to inspect forcing replies and abandoned guards. The 40-second Qh4+ calculation did produce a sound mating finish.
- T37R5 finished about 12:11, zero illegal. Fast development banked time; ...Rxc1+ took 17 seconds and the required ...bxc2 only four. Final mating calculations took 25-40 seconds. Once the capture chain is verified, execute promptly; reserve longer thinks for flights and support, not routine recaptures.

## Record
- T37R2, Black versus SF19: draw by repetition, move 97. Won a pawn, lost the central chain after a king excursion, survived Q versus bare K. Result does not validate conversion.
- T37R3, White versus GLM 5.3 Flash: win by Qa3#, move 51. Missed Bxd8, recovered with dxc6, won B after ...Bd7, simplified and promoted. Avoidable rook loss.
- T37R4, White versus GPT-6.1 Sol: win by g4#, move 43. Chigorin; Qf3?! lost time, Qc7? rescued by ...Qb6??. Took Q/Na5, activated Bb1/Nf5 and mated.
- T37R5, Black versus Sonnet 5.5: win by Qf7#, move 48. Chigorin ...Qb7 released Nc6; Rc1?? lost a rook to ...Rxc1+. Returned R for B+P to retain an extra minor, activated bishops with ...f5, then took Qxg6+ and finished with Q+N.

## Note files
- None.
