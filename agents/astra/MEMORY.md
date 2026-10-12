# Chess memory

## Main lessons
- Before every move inspect the opponent's changed attacks, then checks, captures and threats on the proposed board. Count legal defenders through actual blockers; check pawn diagonals and backward bishop captures. Checks and supported pieces can still lose material.
- KING ACTIVITY NEEDS A CONCRETE TARGET AND RETURN ROUTE. T37R2: my king left the center to chase f4 while White's Kc5 and bishop approached d5. 46...Kh6?? moved farther from the pawn chain; Be6 followed. A king excursion is not progress if the enemy can liquidate my center first.
- SOLE BISHOP DEFENDER IS NOT ENOUGH AGAINST KING + BISHOP. Ba8 alone guarded d5; d5 guarded c4. White could play Bxd5, answer ...Bxd5 with Kxd5, then collect c4. Before leaving a chain, calculate capture of its base through the final king recapture. Keep king support or find a concrete tactical answer before pursuing a remote pawn.
- BISHOP EXCHANGE MEANS EVALUATE THE PAWN ENDING FIRST. In this game 50.Bxd5 Bxd5 51.Kxd5 surrendered d5 and exposed c4. My active-looking king and f-pawn did not compensate for White's king penetration and outside b-pawn. The repair was needed earlier; no verified replacement for ...Kh6 is stored.
- EXTRA PAWN DOES NOT GUARANTEE A WIN. The opening advantage dwindled as White invaded the a-file and blockaded my connected passers with Kd4. Compare king entry squares, blockade strength and remaining pawn targets before simplifying or advancing the majority.
- TWO SEPARATED PASSERS STRETCH A LONE KING. After losing the center, opposition did not save me against b- and f-pawns. Taking f6 allowed the b-pawn to queen. Count promotion tempi and king arrival squares; 'stay central' is not a drawing proof.

## Black opening: Spanish Four Knights
- Tested T37R2 versus SF19: 1.e4 e5, Nf3/Nc3 met by ...Nc6/...Nf6; against Bb5 play ...Bb4 and castle.
- Played continuation: 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Bd6 11.d4 Qh4 12.g3 Qxd4.
- Pattern: ...e4 attacks Nf3 while White takes Nc6; complete both pawn removals to restore material balance. Then Bd6 + Qh4 threatens Qxh2#, allowing ...Qxd4 after g3, with tempo on Bc4. Both queen moves were marked only good moves in the supplied review; verify the matching board.
- ...Bg4 attacked Qf3 while Qd4 supported the bishop. White's Be3 counterattacked my queen; ...Bxf3 and Bxd4 exchanged queens and retained the extra pawn. Count both captures rather than treating the first queen capture as a win.
- ...b5/...a6 and axb5 ...axb5 opened the a-file for Ra6-a7. Prepare to contest the file when changing the pawn structure. Later ...Ra8 with Be4 supporting a8 enabled safe liquidation of both rook pairs.
- After Bxd6+, ...cxd6 created a passed d-pawn. King centralization supported it, but ...b4 liquidation let White establish Kd4. Connected passers require a way to dislodge the blockader, not merely another push.

## Opponent and clock
- SF19 in this game searched at depth 4 and moved essentially instantly. It found the central blockade and won both central pawns, then promoted, but failed to coordinate queen and king and allowed threefold repetition against my bare king. This is one observed shallow-search failure, not a reliable escape plan against Stockfish generally.
- In a lost ending, continue with legal resistance: keep available central escape squares, avoid confinement and track repeated positions including side to move. A repeated king square alone is not a repeated position.
- 900+10: zero illegal attempts; finished with about nine minutes. Opening and forced recaptures generally took 3-9 seconds. Several strategic decisions took 43-62 seconds without solving the central weakness. Aim for 10-15 seconds on routine moves; spend longer only on a concrete capture sequence, pawn race or irreversible decision. Verified defensive cycles should fit within the increment.

## Record
- T37R2, Black versus SF19: draw by repetition on move 97. Won a pawn in the Four Knights, lost the central chain after a king excursion, survived queen versus bare king through repetition. Result does not validate the conversion.

## Note files
- None.
