# Pre-move scan & blunder patterns (g1-g56)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality: my turn, my pieces only; geometry; path clear incl. own blockers; destination not mine. 3 invalid = forfeit; after one rejection play a DIFFERENT traced legal move, never resend (g47, g50, g56: 2 tries ~2 min).
2. HIS last move first: what does it attack now? (g46 16...Rad8 hit Qd1, 17.Be3??). Then name EVERY enemy piece that attacks my destination, tracing its path; attacked+undefended -> reject. A note asking 'is X safe?' = REJECT until the attacker's path is written (g56 'check Be7' -> 19.Qd6?? Bxd6).
3. Moving vacates guards (g30); his KING's 8 neighbour squares are attackers (g55 27...Rd2?? Kxd2).
4. My attacked/loose piece: save/trade/defend NOW; a queen attacked by a rook must MOVE - 'defended' still loses Q for R (g42,g46). His rook on my 2nd rank: moving a blocker drops the piece behind it (g52 26.Bd3? Rxd2). Loose rook facing his rook loses.
5. Pawn pushes/recaptures: is this pawn the SOLE guard of one of my pieces? (g55 19...gxf5?? moved g6, Nh5's only defender; 20.Rxh5 won the knight.) Never onto a defended piece/pawn attack or while it guards my piece (g48 21.d6?!, g51 28.f3??). Enemy PAWNS recapture (g47 15...Nb4?? cxb4) and attack SQUARES: no knight on a pawn-attacked square even if defended - 'defended' loses N for P (g56 16.Nc4?? bxc4).
6. EVERY queen move/capture: (a) list all enemy pieces covering the destination (g56 19.Qd6?? - Be7 and Qc7 one step away; undefended; Bxd6); (b) my recapturer if his queen can take mine there. g51 24.Qxd5?? Qxd5 = Q for N (no recapture); g48 22.Qxd6 / g50 10...Qc7 / g42 17.Qxd5?? Rxd5 same class.
7. Recapturers on the destination: rooks rank/file, PAWNS, QUEENS (g36,g42,g47; g51 25.Rxe5?? dxe5 = R for P). Trace the path and what the recapture opens (g39).
8. Knight: never undefended or pawn/bishop/queen-attacked, esp. down material (g44,g46,g47,g51,g52,g56). Nd2 traps: g46/g48 ...Qxd2; g52 25.Nd2 loose -> 26...Rxd2.
9. Mate nets before grabs: g49 my Nf6 was h5's sole guard - never move it (16...Nxe4?? 17.Rxh5! Qxh7#). Attacking his queen excuses nothing (g45,g50,g51); list his one-move mates first (g53).
10. Lost: defend/trade, 5-15 s, no undefended pieces, no grabs; then 1-3 s: g52 drew a lost position by repetition; g55 flagged 0:18 after 35-65 s moves. The 10 s increment makes 1-3 s moves free.
11. Time: routine <=15 s, book <=10 s, m1-12 <=20 s, m13+ <=25 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g46 0:18, g48 0:32, g53 46 s routine, g55 35-65 s/move, g56 1:34 on 14.Bb3 then 19.Qd6??).

## Patterns
- Losses: piece on a pawn-attacked square (g56 Nc4/bxc4); queen onto a square his bishop/queen covers (g56 Qd6/Bxd6; g48,g50,g51); grabs his queen/rook/pawn covered (g36,g42,g47,g51); queen 'trades' with no recapturer (g48,g50,g51); loose knights (g24,g40,g44,g46,g47,g51,g52,g56); loose bishops (g42,g45); mated on the 8th/h-file (g6,g25,g26,g40,g42,g49,g53,g54).
- Illegal tries cost g34,g44,g45,g47,g50,g52,g56: after one rejection a different move, traced twice; never resend.
- Down material: defend, trade, no new loose pieces; long thinks never fixed anything (g36-g56).
- When winning: avoid repetition/stalemate drift - change a piece or push a pawn before the same position appears a third time (g52: 2B+N up became a repetition draw).
