# Pre-move scan & blunder patterns (g1-g62)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality: my turn, my pieces only; geometry; path clear incl. own blockers; destination not mine; never repeat a piece's current square (g61 Qd2 twice = 92 s). Two pieces reach one square -> write the full name (Rfd8, not Rd8): ambiguous = invalid (g62). Knights: c5->e4/e6/d3/d7/b3/b7/a4/a6, f6->e4/g4/h5/h7/e8/g8/d5/d7. One rejection -> play a DIFFERENT traced move; 3 invalid = forfeit.
2. HIS last move first: what does it attack now? Name EVERY enemy piece that attacks my destination, tracing its path; for ANY piece move also trace his ROOK's file+rank from its current square (g62 15...Bd4?? Rd6xd4; 24...Rb7?? Rxb7, c7 empty); attacked+undefended -> reject.
3. Moving vacates guards; the enemy KING attacks his 8 neighbours (g55 27...Rd2?? Kxd2).
4. My attacked/loose piece: save/trade/defend NOW; a queen attacked by a rook must MOVE; his rook on my 2nd rank: moving a blocker drops the piece behind it.
5. Pawns: is this pawn the SOLE guard of my piece? (g55 19...gxf5?? 20.Rxh5). No piece on a pawn-attacked square even if defended (g59 24...Rxa5?? bxa5). A push that opens a file: who enters first, can I recapture? (g61 21.b4? axb3! e.p. 22.axb3?! Rxa1 - own Bb1 blocked Re1; 22.Nxb3 keeps a1 guarded).
6. QUEEN moves: list ALL enemy pieces covering the destination - PAWNS FIRST - and my recapturer. No recapturer = queen lost (g48,g50,g51,g56,g57; g58 22...Qxd5?? cxd5; g59 22...Qxb5?? Nxb5; g60 21.Qxa4?? bxa4). Never the queen onto a line facing his rook/queen with nothing between (g61 24.Qa3?? Rxa3). Flank squares touch pawns: a4/a5/b4/b5/c3/f3/h3/c6.
7. Recapturers: rooks rank/file, PAWNS, KNIGHTS, QUEENS; value the chain: R for N+B = -1 (g58 13...Bxd4); if HIS side makes the last capture, it loses (g59 13...Na4?? 14.Nxa4).
8. Captures + follow-up: verify the follow-up on the CURRENT board (g60 18.Nxe5?? dxe5: d6 undefended; g61 25.Nxe5?? dxe5).
9. Loose knights/bishops: before a jump OR a retreat when hit, list every enemy attacker of the square (rooks file/rank, BISHOP diagonals, knights, pawns) and the chain; a fork he can just take is not a fork; the retreat square must be attacked by NOTHING (g59 Na4??; only d7 safe).
10. Mate nets before grabs; his Q+R on rank 2 = Qxf2+/Qxg2#. His Qb6+Bc5 on f2: guard f2 with a piece or block the diagonal (g61 30...Bxf2+ 31.Kh2 Bg3+ 32.Nxg3 Qe3! 33...Qxg3+ 34.Kg1 Rb1+ 35.Rc1 Rxc1#; Qg3 covers f2/g2/h2).
11. Down material: defend/trade, 5-15 s, no undefended pieces, no desperate grabs (g61 25.Nxe5??); repetition/stalemate = half point. When winning: make progress.
12. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g61: 40-92 s routine m14-33; g62: 35-55 s m9-24, two blunders, 8 min left).

## Patterns
- Losses: queen onto a pawn-attacked/covered square or in front of his rook on an open line (g48-g51,g56-g61); queen recaptured by a pawn/knight; covered-unit grabs (g59 Rxa5??/Nxe4??; g61 Nxe5??); captures whose follow-up is blocked (g60 18.Nxe5??); knight on a pawn-attacked square or taken by a rook with a winning chain (g58); a hit piece retreating into an attack (g59); opening a file to his rook while my recapture path is blocked (g61 21.b4?); bishop/rook onto his rook's file/rank undefended (g62 15...Bd4?? Rd6xd4; 24...Rb7?? Rxb7); f2-battery sacs; mates on the 8th/h-file/rank 1.
- Illegal tries: trace twice before sending; verify knight geometry; never send a move already on the board; disambiguate when two pieces reach the square (g62 "Rd8" = invalid).
- When winning: avoid repetition/stalemate drift.
