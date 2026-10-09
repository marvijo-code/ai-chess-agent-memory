# Pre-move scan & blunder patterns (g1-g57)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality: my turn, my pieces only; geometry; path clear incl. own blockers (g57 Be3 illegal: Nd2 on d2); destination not mine. After one rejection play a DIFFERENT traced legal move, never resend; 3 invalid = forfeit.
2. HIS last move first: what does it attack now? Name EVERY enemy piece that attacks my destination, tracing its path; attacked+undefended -> reject. A note asking 'is X safe?' = REJECT until the attacker's path is written (g56).
3. Moving vacates guards (g30); the enemy KING attacks his 8 neighbours (g55 27...Rd2?? Kxd2).
4. My attacked/loose piece: save/trade/defend NOW; a queen attacked by a rook must MOVE (g42,g46). His rook on my 2nd rank: moving a blocker drops the piece behind it (g52); that rook also guards f2/g2 vs my king (g57).
5. Pawns: is this pawn the SOLE guard of my piece? (g55 19...gxf5?? 20.Rxh5). Enemy PAWNS attack squares: no knight on a pawn-attacked square even if defended (g56 Nc4/bxc4; g47 Nb4/cxb4; g57 Nd4/exd4).
6. Queen: list all enemy pieces covering the destination AND my recapturer if his queen can take mine there. No recapturer = queen lost (g48,g50,g51,g56 19.Qd6??, g57 24.Qxd4??).
7. Recapturers: rooks rank/file, PAWNS, QUEENS (g51 25.Rxe5?? dxe5); trace what the recapture opens (g39).
8. Loose pieces: knights (g24,g40,g44,g46,g47,g51,g52,g56,g57); bishops (g42,g45; g57 25.Bc2?? Rxc2).
9. Mate nets before grabs (g49,g53); his queen + rook on rank 2 = Qxf2+/Qxg2#, Kxf2/Kxg2 illegal (g57).
10. STALE PLAN: after a trade, re-check the combination's pieces still exist (g57: planned Bxd4 after the bishop was traded on c5) and recalculate on the CURRENT board.
11. Down material: defend/trade, 5-15 s, no undefended pieces; repetition/stalemate = half point (g52). When winning: make progress, never a third repetition.
12. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g46-g56; g57 1:44+60 s routine m16-20, mated with 5:06 vs 16:02).

## Patterns
- Losses: knight on a pawn-attacked square (g56,g57); queen onto a covered square with no recapturer (g48,g50,g51,g56,g57); queen 'trade' with no recapturer; loose knights/bishops; grabs of covered units (g36,g42,g47); mates on the 8th/h-file (g6,g25,g26,g40,g42,g49,g53,g54); Q entry to f2/g2 with a rook on rank 2 (g57).
- Illegal tries cost g34,g44,g45,g47,g50,g52,g56,g57 (own-piece blockers and geometry): trace twice before sending; after a rejection never resend.
- Long thinks never fixed anything; the missing move is the 5 s destination scan (g36-g57).
- When winning: avoid repetition/stalemate drift - change something before the same position appears a third time (g52).
