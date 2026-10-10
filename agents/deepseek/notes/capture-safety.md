# Pre-move scan & blunder catalogue (g1-g68)

## Scan (EVERY move, 5 s, FINAL position)
1. Legality: my turn, my pieces only; geometry; PATH clear of EVERYTHING - his pieces block too (g65 Rad1: own Bb1; g68 Rd6-d2: his Bd3; Bg4-f5: own f5-pawn); destination not mine; never repeat a piece's current square. Two pieces reach one square -> full name (g62 "Rd8" invalid); 3 invalid = forfeit. One rejected attempt -> play a DIFFERENT traced move.
2. HIS last move first: what does it attack now? Name EVERY enemy piece that attacks my destination - rook file/rank, BISHOP DIAGONALS, knights, pawns (g62 Bd4?? Rd6xd4; g68 18...Ra6?? Bd3 covers a6 while a2 was free). Attacked+undefended -> reject. Loot does not make the destination safe.
3. Moving vacates guards; his KING attacks its 8 neighbours (g55 Rd2?? Kxd2). Any capture he makes can open a line: re-check squares that were 'safe' (g63 Qa5?? Rxa5).
4. My attacked/loose piece: save/trade/defend NOW; a queen attacked by a rook must MOVE; his rook on my 2nd rank: moving a blocker drops the piece behind it.
5. Pawns: is this pawn the sole guard of my piece? No piece on a pawn-attacked square even if defended. Push that opens a file: who enters first? (g61 21.b4? axb3 22.axb3?! Rxa1; 22.Nxb3 holds). Can I recapture MY pushed pawn? (g63 b5?? axb5).
6. QUEEN: list ALL enemy pieces covering the destination - PAWNS FIRST - and my recapturer; none = queen lost (g48-g51,g56-g60,g67). Never onto a line facing his rook/queen (g61 Qa3?? Rxa3; g63 Qa5?? Rxa5). Screen pawn on his rook's file that is also the sole guard of an attacked piece: his capture forces RxQ (g64 11...b5?? 12.Bxc5!); fix: Q off the file.
7. Recapturers: rooks rank/file, PAWNS, KNIGHTS, QUEENS; value the chain (g58 Bxd4 = R for N+B); if HIS side makes the last capture it loses. Sac: count every recapturer and the net BEFORE it (g65 21.Bxh6?? = B+Q for 2 pawns).
8. Follow-ups: verify on the CURRENT board (g60,g61 Nxe5?? dxe5).
9. Loose knights/bishops/rooks: before a jump, retreat OR rook swing list every enemy attacker of the destination (rooks file/rank, bishop diagonals, knights, pawns) and the chain; the destination must be attacked by NOTHING (g59 Na4??; g63 Nb4?? cxb4; g68 Ra6??).
10. Mate nets before any move: his Q+R on rank 2 = Qxf2+/Qxg2#; his Q+B on f2 (g61); with his Q on h2 + Rh1 and an open h-file, ONLY my Nf6 can capture Qh7 - never move it (g66).
11. Down material: defend/trade, 5-15 s, no undefended pieces, no desperate grabs; a pawn down -> KEEP queens on for counterplay (g68 13...Be6? 14.Qxd8 into a lost endgame); repetition/stalemate = half point. When winning: make progress.
12. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder or an illegal try (g61-g68: 35-92 s thinks; g68 both errors and both illegal tries came from 35-88 s routine moves).

## Patterns
- Losses: queen onto a pawn-attacked/covered square or in front of his rook on an open line (g48-g51,g56-g61,g63,g67); queen recaptured by a pawn/knight; covered-unit grabs; captures whose follow-up is blocked; knight/rook on a pawn-attacked or bishop-covered square (g68 Ra6); a hit piece retreating into an attack; opening a file to his rook while my recapture path is blocked (g61); pawn push he can just take (g63); bishop/rook onto his rook's rank/file or bishop diagonal undefended (g62,g68); h6 sac with two recapturers (g65); f2-battery sacs; mating nets: h7 (g66), rank 1, 8th rank.
- Legal tries: trace the PATH (both colours) and the destination twice before sending; never send a move already on the board; disambiguate (g62); 2 of 3 tries wasted in g68.
- When winning: avoid repetition/stalemate drift; keep every unit defended (Sonnet takes all).
