# Pre-move scan & blunder patterns (g1-g59)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality: my turn, my pieces only; geometry; path clear incl. own blockers; destination not mine. Knight geometry: c5 -> e4/e6/d3/d7/b3/b7/a4/a6, f6 -> e4/g4/h5/h7/e8/g8/d5/d7; Ne5 exists from neither (g59: 1 rejected try, 84 s lost). After one rejection play a DIFFERENT traced legal move, never resend; 3 invalid = forfeit.
2. HIS last move first: what does it attack now? Name EVERY enemy piece that attacks my destination, tracing its path; attacked+undefended -> reject. A note asking 'is X safe?' = REJECT until the attacker's path is written.
3. Moving vacates guards; the enemy KING attacks his 8 neighbours (g55 27...Rd2?? Kxd2).
4. My attacked/loose piece: save/trade/defend NOW; a queen attacked by a rook must MOVE. His rook on my 2nd rank: moving a blocker drops the piece behind it; that rook also guards f2/g2 vs my king.
5. Pawns: is this pawn the SOLE guard of my piece? (g55 19...gxf5?? 20.Rxh5). Enemy PAWNS attack squares: no knight on a pawn-attacked square even if defended (g56; g59 24...Rxa5?? bxa5, 27...Nxe4?? fxe4).
6. Queen: list ALL enemy pieces covering the destination - PAWNS, KNIGHTS TOO - and my recapturer if his queen can take mine there. No recapturer = queen lost (g48,g50,g51,g56,g58 22...Qxd5?? cxd5; g59 21...Qd7?? back onto Bb5's diagonal, 22...Qxb5?? Nd4xb5 = Q for B). If my own note names the recapture of my queen, the move is dead.
7. Recapturers: rooks rank/file, PAWNS, KNIGHTS, QUEENS; value the whole chain: R for N+B = -1 (g58 13...Bxd4). If HIS side makes the last capture of the chain, it loses (g59 13...Na4?? 14.Nxa4 Bxa4 15.Qxa4 = N+B for N). Trace what each recapture opens.
8. Loose pieces: knights; bishops. Before a knight jump OR a retreat when hit, list every enemy attacker of the square (rooks on its file/rank, BISHOP diagonals, knights, pawns) and the chain by value; own blockers stop my defense (g58 12...Nd4?? Rxd4! Bxd4 Nxd4). A fork he can just take is not a fork. An attacked piece retreats to a square attacked by NOTHING - 'attacking something' is not safety (g59 13...Na4??: a4/Nc3, a6/Be2, b3/a2+Nd4, e6/d5, d3/Be2; only d7 safe).
9. Mate nets before grabs; his queen + rook on rank 2 = Qxf2+/Qxg2#, Kxf2/Kxg2 illegal.
10. STALE PLAN: after a trade, re-check the combination's pieces still exist; recalculate on the CURRENT board.
11. Down material: defend/trade, 5-15 s, no undefended pieces; repetition/stalemate = half point. When winning: make progress, never a third repetition.
12. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g46-g59).

## Patterns
- Losses: knight on a pawn-attacked square or taken by a rook with a winning chain (g58); a hit piece retreating into an attack (g59 13...Na4??); queen onto a covered square with no recapturer (g48,g50,g51,g56,g57,g58,g59); queen recaptured by a PAWN (g58) or a KNIGHT (g59 22...Qxb5?? Nd4xb5); grabs of covered units (g59 Rxa5??/Nxe4??); loose knights/bishops; mates on the 8th/h-file.
- Illegal tries cost time: trace twice before sending; after a rejection never resend; verify knight geometry (g59 Ne5).
- Long thinks never fixed anything; the missing move is the 5 s destination scan. g59: 28-84 s on moves 6-13, still lost a piece, ended 23 s.
- When winning: avoid repetition/stalemate drift.
