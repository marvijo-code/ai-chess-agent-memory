# Pre-move scan & blunder catalogue (g1-g66)

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my turn, my pieces only; geometry; path clear incl. own blockers (g65 'Rad1' illegal: Bb1 blocks Ra1); destination not mine; never repeat a piece's current square. Two pieces reach one square -> full name (Rfd8): ambiguous = 1 invalid. Knights: c5->e4/e6/d3/d7/b3/b7/a4/a6; f6->e4/g4/h5/h7/e8/g8/d5/d7. One rejected attempt -> play a DIFFERENT traced move; 3 invalid = forfeit.
2. HIS last move first: what does it attack now? Name EVERY enemy piece that attacks my destination, tracing paths; for any piece move also trace his ROOK's file+rank from its current square (g62 Bd4?? Rd6xd4; Rb7?? Rxb7). Attacked+undefended -> reject.
3. Moving vacates guards; his KING attacks its 8 neighbours (g55 Rd2?? Kxd2). Any capture he makes can open a line: re-check squares that were 'safe' (g63 Qa5?? Rxa5).
4. My attacked/loose piece: save/trade/defend NOW; a queen attacked by a rook must MOVE; his rook on my 2nd rank: moving a blocker drops the piece behind it.
5. Pawns: is this pawn the sole guard of my piece? No piece on a pawn-attacked square even if defended. Push that opens a file: who enters first, can I recapture? (g61 21.b4? axb3 22.axb3?! Rxa1; 22.Nxb3 holds). Can I recapture MY pushed pawn? (g63 b5?? axb5: a7 takes b6 only, Bd7 blocked).
6. QUEEN moves: list ALL enemy pieces covering the destination - PAWNS FIRST - and my recapturer; none = queen lost (g48-g51,g56-g60). Never onto a line facing his rook/queen with nothing between (g61 Qa3?? Rxa3; g63 Qa5?? Rxa5). Screen pawn on his rook's file that is also the sole guard of an attacked piece: his capture forces RxQ (g64 11...b5?? 12.Bxc5! dxc5 13.Rxd8); fix: Q off the file.
7. Recapturers: rooks rank/file, PAWNS, KNIGHTS, QUEENS; value the chain (g58 Bxd4 = R for N+B); if HIS side makes the last capture it loses. Sac: count every recapturer and the net BEFORE it (g65 21.Bxh6?? gxh6 22.Qxh6 Bxh6 = B+Q for 2 pawns).
8. Follow-ups: verify on the CURRENT board (g60,g61 Nxe5?? dxe5).
9. Loose knights/bishops: before a jump OR retreat when hit, list every enemy attacker of the square (rooks file/rank, bishop diagonals, knights, pawns) and the chain; the retreat square must be attacked by NOTHING (g59 Na4??; g63 Nb4?? cxb4).
10. Mate nets before any move: his Q+R on rank 2 = Qxf2+/Qxg2#; his Q+B on f2 (g61 ...Bxf2+ Kh2 Bg3+ Nxg3 Qe3 ...Rb1-Rxc1#); with his Q on h2 + Rh1 and an open h-file, ONLY my Nf6 can capture Qh7 (his rook defends h7, Kg8 can't) - never move it (g66 17...Nxe4?? 18.Qxh7#).
11. Down material: defend/trade, 5-15 s, no undefended pieces, no desperate grabs; repetition/stalemate = half point. When winning: make progress.
12. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g61-g66: 40-92 s thinks, all blundered anyway).

## Patterns
- Losses: queen onto a pawn-attacked/covered square or in front of his rook on an open line (g48-g51,g56-g61,g63); queen recaptured by a pawn/knight; covered-unit grabs; captures whose follow-up is blocked; knight on a pawn-attacked square or taken by a rook with a winning chain; a hit piece retreating into an attack; opening a file to his rook while my recapture path is blocked (g61 21.b4?); pawn push he can just take (g63 b5??); bishop/rook onto his rook's file/rank undefended (g62); h6 sac with two recapturers (g65); f2-battery sacs; mating nets: h7 by Qxh7# once Nf6 leaves (g66), rank 1, 8th rank.
- Illegal tries: trace twice before sending; never send a move already on the board; disambiguate (g62 'Rd8' invalid); check own blockers (g65 Rad1).
- When winning: avoid repetition/stalemate drift; keep every unit defended (Sonnet takes all).
