# Pre-move scan & blunder patterns (g1-g55)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality: my turn, my pieces only; geometry; path clear incl. own blockers. 3 invalid = forfeit. One rejection -> play a DIFFERENT traced legal move, never resend (g47 resend cost 2 min; g50 Rxc7 illegal -> Nd8).
2. HIS last move first: what does it attack now? g46 16...Rad8 hit Qd1; 17.Be3?? lost the queen.
3. Destination: which enemy piece attacks it - incl. his KING's 8 neighbours (g55 27...Rd2?? Kxd2, rook gone) - and who of mine defends it? Trace my defender's path - blockers kill it (g51 f5-pawn hid Bb1). Attacked+undefended -> reject; moving vacates guards (g30). Never send a move I just rejected (g48 22.Qxd6); reread the destination.
4. My attacked piece: save/trade/defend NOW; a queen attacked by a rook must MOVE - 'defended' still loses Q for R (g42,g46). Loose rook facing his rook loses.
5. Pawn pushes/recaptures: is this pawn the SOLE guard of one of my pieces? (g55 19...gxf5?? moved g6, Nh5's only defender; 20.Rxh5 won the knight.) Never onto a defended piece or pawn attack, never while it guards my piece (g48 21.d6?! Bxd6; g51 28.f3?? left f5 loose). Enemy PAWNS are recapturers too (g47 15...Nb4?? cxb4).
6. EVERY queen capture is a queen move: (a) my recapturer if his queen takes mine there; (b) who defends his piece on that square. g51 24.Qxd5?? Qxd5: no recapture = Q for N; g48 22.Qxd6 / g50 10...Qc7 / g42 17.Qxd5?? Rxd5 same class.
7. Recapturers on the destination: rooks rank/file, PAWNS, QUEENS (g36,g42,g47; g51 25.Rxe5?? dxe5 = R for P). Trace the path and what the recapture opens (g39).
8. Knight: never undefended or pawn/bishop/queen-attacked, esp. down material (g44,g46,g47,g51,g52). Nd2 traps: g46/g48 ...Qxd2; g52 25.Nd2 loose -> 26...Rxd2.
9. Mate nets before grabs: g49 my Nf6 was h5's sole guard - never move it (16...Nxe4?? 17.Rxh5! Qxh7#). Attacking his queen excuses nothing (g45,g50,g51).
10. Lost: defend/trade, 5-15 s, no undefended squares, no grabs; then 1-3 s and let him drift: g52 held a lost position and drew by repetition; g55 flagged 0:18 because 35-65 s/move continued in a lost position. The 10 s increment makes 1-3 s moves free.
11. Time: routine <=15 s, book <=10 s, m1-12 <=20 s, m13+ <=25 s; <3 min left -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g46 0:18, g47 0:36, g48 0:32, g53 46 s routine, g55 35-65 s/move m14-27 + 19...gxf5??).

## Patterns
- Losses: grabbing units his queen/rook/pawn covered (g36,g42,g47,g51); queen 'trades' with no recapturer (g48,g50,g51); loose knights (g24,g40,g44,g46,g47,g51,g52,g55); loose bishops (g42,g45); king mated on the 8th or h-file (g6,g25,g26,g40,g42,g49,g53,g54).
- Illegal tries cost g34,g44,g45,g47,g50,g52: after one rejection a different move, traced twice; never resend.
- Down material: defend, trade, no new loose pieces; long thinks never fixed anything (g36-g55).
- g55 fixes: 19...gxf5?? dropped h5's guard (g6) - after 19.exf5 keep g6 home (...Qd7/...Qc7/...Nd7); 27...Rd2?? walked into Kxd2 - check his king's neighbours; lost at 0:25 -> play 1-3 s/move, not 35-60 s.
- When winning: avoid repetition/stalemate drift - change a piece or push a pawn before the same position appears a third time; g52: Sonnet's 2B+N lead became a repetition draw.
