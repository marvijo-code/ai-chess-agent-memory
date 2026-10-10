# Pre-move scan & blunder patterns (g1-g60)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality: my turn, my pieces only; geometry; path clear incl. own blockers; destination not mine. Knight c5->e4/e6/d3/d7/b3/b7/a4/a6, f6->e4/g4/h5/h7/e8/g8/d5/d7. One rejection -> play a DIFFERENT traced move, never resend; 3 invalid = forfeit.
2. HIS last move first: what does it attack now? Name EVERY enemy piece that attacks my destination, tracing its path; attacked+undefended -> reject. 'Is X safe?' = REJECT until the attacker's path is written.
3. Moving vacates guards; the enemy KING attacks his 8 neighbours (g55 27...Rd2?? Kxd2).
4. My attacked/loose piece: save/trade/defend NOW; a queen attacked by a rook must MOVE. His rook on my 2nd rank: moving a blocker drops the piece behind it.
5. Pawns: is this pawn the SOLE guard of my piece? (g55 19...gxf5?? 20.Rxh5). No piece on a pawn-attacked square even if defended (g56; g59 24...Rxa5?? bxa5).
6. QUEEN moves: list ALL enemy pieces covering the destination - PAWNS FIRST - and my recapturer if his queen/bishop takes mine there. No recapturer = queen lost (g48,g50,g51,g56,g57; g58 22...Qxd5?? cxd5; g59 21...Qd7?? on Bb5's diagonal then 22...Qxb5?? Nxb5; g60 21.Qxa4?? bxa4 = Q for P). Flank pawns bracket a4/a5/b4/b5/c3/f3/h3/c6. If my note names the recapture of my queen, the move is dead.
7. Recapturers: rooks rank/file, PAWNS, KNIGHTS, QUEENS; value the chain: R for N+B = -1 (g58 13...Bxd4); if HIS side makes the last capture, it loses (g59 13...Na4?? 14.Nxa4 Bxa4 15.Qxa4 = N+B for N).
8. Captures + follow-up: verify the follow-up on the CURRENT board. g60 18.Nxe5?? dxe5 planned 19.d6: e5 had TWO guards (d6-pawn, Nf6); d6 had no defender (Nd2 blocked Qd1) so Bxd6 just took it - N for P. Same class as g57 (piece already traded).
9. Loose knights/bishops: before a jump OR a retreat when hit, list every enemy attacker of the square (rooks on file/rank, BISHOP diagonals, knights, pawns) and the chain; a fork he can just take is not a fork; the retreat square must be attacked by NOTHING - 'attacking something' is not safety (g59 13...Na4??; only d7 safe).
10. Mate nets before grabs; his Q+R on rank 2 = Qxf2+/Qxg2#, Kxf2/Kxg2 illegal.
11. Down material: defend/trade, 5-15 s, no undefended pieces; repetition/stalemate = half point. When winning: make progress.
12. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g46-g60; g60 40-51 s on m16-22 then hung the queen).

## Patterns
- Losses: queen onto a pawn-attacked square (g60 21.Qxa4??; g58 22...Qxd5??) or onto a covered square with no recapturer (g48-g51,g56,g57,g59); queen recaptured by a pawn or knight; grabs of covered units (g59 Rxa5??/Nxe4??); captures whose follow-up is blocked (g60 18.Nxe5??); knight on a pawn-attacked square or taken by a rook with a winning chain (g58); a hit piece retreating into an attack (g59); loose knights/bishops; mates on the 8th/h-file.
- Illegal tries cost time: trace twice before sending; verify knight geometry.
- When winning: avoid repetition/stalemate drift.
