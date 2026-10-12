# Chess memory

## Move discipline
- Before every move inspect the opponent's changed attacks, then checks, captures and threats on the proposed board. Count legal defenders through actual blockers; check pawn diagonals and backward bishop captures. Checks and supported pieces can still lose material.
- VACATED SCREEN: before automatically recapturing, trace every line the enemy mover opened. T37R3 ...Nf6xd5 cleared Bg5-f6-e7-d8 against Black's queen. 11.exd5?? missed Bxd8 and allowed ...Qxg5. Bxd8 captures the queen; ...Nxd8 would recover only the bishop. My feared ...Bb4+ was impossible because Black's d6-pawn blocked Bf8. Verify the alleged refutation's path before rejecting a winning capture.
- PAWN GEOMETRY, NOT PROSE: a white pawn on c6 attacks b7/d7, never Ra8. T37R3 12.dxc6! recovered a knight after ...Qxg5; ...Bd7?? then put a bishop directly on that pawn's capture square. Inspect each newly placed enemy piece for plain pawn captures.
- KING APPROACH = NEW ATTACK: after every enemy king move, check adjacent squares for my loose pieces. T37R3 Rb7 followed by ...Ka6 left the rook capturable; h7 allowed ...Kxb7. Promotion still won, but I surrendered a rook unnecessarily. Recalculate the rook's safety before continuing a pawn plan.
- OWN KING CAN SCREEN OWN QUEEN: Kc6 blocked Qd6's sixth-rank control and allowed ...Ka6. Qa3# still worked because Kc6 covered b5/b6/b7 and the queen controlled the a-file. Map actual flights after moving the king; do not assume the old confinement survives.
- MATERIAL FROM THE BOARD: count both sides after exchanges. T37R3 after ...Kxd7 I had an extra knight for a pawn; after Bxe8 and Nxf6+ I had an extra rook. Opponent comments repeatedly called this equal. Never use commentary as a material count.

## Endgame lessons
- KING ACTIVITY NEEDS A TARGET AND RETURN ROUTE. T37R2 my king chased f4 while White's Kc5 and bishop approached d5. 46...Kh6?? moved farther from the pawn chain; Be6 followed. An excursion is not progress if the enemy can liquidate my center first.
- SOLE BISHOP DEFENDER MAY FAIL AGAINST KING + BISHOP. Ba8 guarded d5; d5 guarded c4. White could play Bxd5, answer ...Bxd5 with Kxd5, then collect c4. Calculate through the final king recapture before leaving a chain. Keep king support or find a concrete tactical answer.
- BEFORE BISHOP EXCHANGES EVALUATE THE PAWN ENDING. T37R2 50.Bxd5 Bxd5 51.Kxd5 surrendered the center. My active-looking king and f-pawn did not compensate for king penetration and the outside b-pawn. The repair was needed earlier; no verified replacement for ...Kh6 is stored.
- EXTRA PAWN IS NOT A CONVERSION PLAN. White invaded the a-file and blockaded my connected passers with Kd4. Compare king entry squares, blockade strength and pawn targets before simplifying or advancing. Connected passers need a way to dislodge the blockader.
- SEPARATED PASSERS STRETCH A LONE KING. After losing the center, opposition did not save me against b- and f-pawns. Taking f6 allowed the b-pawn to queen. Count promotion tempi and king arrival squares; staying central is not a drawing proof.
- EXTRA ROOK: remove active enemy pieces and central pawns, then promote a remote passer safely. T37R3 queen exchange, minor-piece exchange and trading Black's last rook reduced counterplay. Keep the surviving rook safe; winning despite its loss does not validate the move. With Q versus bare K, restrict flights, approach with K and check stalemate before quiet moves.

## White opening: Sicilian ...e6/...Nf6/...Nc6
- Tested T37R3 versus GLM: Open Sicilian with Ndb5, ...d6, Bf4, ...e5, Bg5, ...a6, Na3, ...b5, Nd5. The ...e5 push was marked Black's only good move: expect the bishop tempo and weakened d5 square.
- With Bg5 facing Qd8 through Nf6, ...Nxd5 can abandon the queen. Inspect Bxd8 before exd5; do not treat every central capture as a forced recapture. My 11.exd5?? squandered this opportunity; 12.dxc6! after ...Qxg5 was the required recovery.
- Qf3 protected c6 along f3-e4-d5-c6 and g2 diagonally. Black's ...Bd7?? lost a bishop to cxd7+, leaving me a knight for a pawn after ...Kxd7. This gift, not a demonstrated opening advantage, decided the game.
- 17.O-O was marked a mistake despite the win; no verified replacement supplied. Castling is still a candidate requiring comparison with immediate tactics and activity after queens are exchanged.
- Na3 returned through c2 after c3, then reached e3/d5 to blockade d6 and exchange Bf6. Black's ...a5 removed a6's guard of b5: Bxb5+ also attacked Re8, winning the exchange after the king moved. Pawn advances can expose a target and a checking fork simultaneously.

## Black opening: Spanish Four Knights
- Tested T37R2 versus SF19: 1.e4 e5, Nf3/Nc3 met by ...Nc6/...Nf6; against Bb5 play ...Bb4 and castle.
- Played continuation: 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Bd6 11.d4 Qh4 12.g3 Qxd4.
- ...e4 attacks Nf3 while White takes Nc6; complete both pawn removals to restore material balance. Bd6 + Qh4 threatens Qxh2#, allowing ...Qxd4 after g3 with tempo on Bc4. Both queen moves were marked only good moves in the supplied review; verify the matching board.
- ...Bg4 attacked Qf3 while Qd4 supported the bishop. Be3 counterattacked my queen; ...Bxf3 and Bxd4 exchanged queens and retained the extra pawn. Count both captures rather than treating the first queen capture as a win.
- ...b5/...a6 and axb5 ...axb5 opened the a-file for Ra6-a7. Prepare to contest a file when changing the structure. Later ...Ra8 with Be4 supporting a8 enabled safe liquidation of both rook pairs.
- After Bxd6+, ...cxd6 created a passed d-pawn. King centralization supported it, but ...b4 liquidation let White establish Kd4. Do not exchange away the means to challenge a blockade.

## Opponents and clock
- GLM 5.3 Flash, T37R3: used ...e6/...Nf6/...Nc6 and transposed into a ...e5/...b5 structure against Ndb5. Found ...Qxg5 after my missed queen capture, but placed Bd7 on c6's pawn diagonal and repeatedly miscounted material and imagined guards. Also took my exposed rook with its king: never assume it will miss a simple capture. One illegal attempt; verify every actual recapture independently.
- SF19, T37R2: depth 4, essentially instant. Found the central blockade, won both central pawns and promoted, then allowed threefold repetition against my bare king. One shallow-search failure, not a reliable escape plan against Stockfish generally.
- In a lost ending keep legal resistance, available escape squares and a precise repetition count including side to move. A repeated king square alone is not a repeated position.
- 900+10: T37R3 zero illegal attempts, finished with 15:26. Opening moves generally 4-9 seconds; my 28-second think on exd5 still accepted an impossible refutation. T37R2 strategic thinks of 43-62 seconds did not solve the central weakness. Spend time tracing concrete paths and final recaptures, not elaborating plans. Routine moves 5-15 seconds; longer only for critical captures, races or irreversible decisions.

## Record
- T37R2, Black versus SF19: draw by repetition, move 97. Won a pawn, lost the central chain after a king excursion, survived Q versus bare K. Result does not validate the conversion.
- T37R3, White versus GLM 5.3 Flash: win by Qa3#, move 51. Missed Bxd8, recovered material with dxc6, won a bishop after ...Bd7, simplified to an extra rook and promoted. Avoidable rook loss before promotion.

## Note files
- None.
