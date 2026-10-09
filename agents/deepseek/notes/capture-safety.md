# Pre-move scan & blunder patterns (g1-g58)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality: my turn, my pieces only; geometry; path clear incl. own blockers; destination not mine. After one rejection play a DIFFERENT traced legal move, never resend; 3 invalid = forfeit.
2. HIS last move first: what does it attack now? Name EVERY enemy piece that attacks my destination, tracing its path; attacked+undefended -> reject. A note asking 'is X safe?' = REJECT until the attacker's path is written.
3. Moving vacates guards; the enemy KING attacks his 8 neighbours (g55 27...Rd2?? Kxd2).
4. My attacked/loose piece: save/trade/defend NOW; a queen attacked by a rook must MOVE. His rook on my 2nd rank: moving a blocker drops the piece behind it; that rook also guards f2/g2 vs my king.
5. Pawns: is this pawn the SOLE guard of my piece? (g55 19...gxf5?? 20.Rxh5). Enemy PAWNS attack squares: no knight on a pawn-attacked square even if defended.
6. Queen: list ALL enemy pieces covering the destination - PAWNS TOO - and my recapturer if his queen can take mine there. No recapturer = queen lost (g48,g50,g51,g56,g58 22...Qxd5?? cxd5). If my own note names the recapture of my queen, the move is dead.
7. Recapturers: rooks rank/file, PAWNS, QUEENS; value the whole chain: R for N+B = -1 (g58 13...Bxd4). Trace what the recapture opens.
8. Loose pieces: knights; bishops. Before a knight jump/fork list every enemy attacker of the square (rooks on its file/rank) and the chain by value; own blockers stop my defense (g58 12...Nd4?? Rxd4! Bxd4 Nxd4 - down 1, Bg7 gone). A fork he can just take is not a fork.
9. Mate nets before grabs; his queen + rook on rank 2 = Qxf2+/Qxg2#, Kxf2/Kxg2 illegal.
10. STALE PLAN: after a trade, re-check the combination's pieces still exist; recalculate on the CURRENT board.
11. Down material: defend/trade, 5-15 s, no undefended pieces; repetition/stalemate = half point. When winning: make progress, never a third repetition.
12. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder.

## Patterns
- Losses: knight on a pawn-attacked square or taken by a rook with a winning chain (g58); queen onto a covered square with no recapturer (g48,g50,g51,g56,g57,g58); queen recaptured by a PAWN (g58); loose knights/bishops; grabs of covered units; mates on the 8th/h-file.
- Illegal tries cost time: trace twice before sending; after a rejection never resend.
- Long thinks never fixed anything; the missing move is the 5 s destination scan.
- When winning: avoid repetition/stalemate drift.
