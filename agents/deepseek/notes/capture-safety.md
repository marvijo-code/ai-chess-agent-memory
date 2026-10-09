# Pre-move scan & blunder patterns (g1-g52)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality: my turn, my pieces only; geometry; path clear incl. own blockers (g45/g47 Qd8 has no line). 3 invalid = forfeit. One rejection -> play a DIFFERENT traced legal move, never resend (g47 resend cost 2 min; g50 Rxc7 illegal -> Nd8).
2. HIS last move first: what does it attack now? g46 16...Rad8 hit Qd1; 17.Be3?? lost the queen.
3. Destination: which enemy pawn/knight/bishop/rook(rank/file)/queen attacks it, and who of mine defends it? Trace my defender's path - blockers kill it (g51 f5-pawn hid Bb1). Attacked+undefended -> reject; moving vacates guards (g30). Never send a move I just rejected (g48 22.Qxd6); reread the destination.
4. EVERY queen capture is a queen move: (a) my recapturer if his queen takes mine there; (b) who defends his piece on that square. g51 24.Qxd5?? Qxd5: no recapture = Q for N; g48 22.Qxd6 / g50 10...Qc7 / g42 17.Qxd5?? Rxd5 same class.
5. My attacked piece: save/trade/defend NOW; a queen attacked by a rook must MOVE - 'defended' still loses Q for R (g42,g46).
6. Recapturers on the destination: rooks rank/file, PAWNS, QUEENS (g36,g42,g47; g51 25.Rxe5?? dxe5 = R for P). Trace the path and what the recapture opens (g39).
7. Knight: never undefended or pawn/bishop/queen-attacked, esp. down material (g44,g46,g47,g51,g52). Nd2 traps: g46/g48 ...Qxd2; g52 25.Nd2 loose -> 26...Rxd2, then 31.Nf4?? exf4.
8. Rook: loose rook facing his rook loses; his rook to an open file/rank at my loose piece = emergency (g42,g46).
9. Mate nets before grabs: g49 my Nf6 was h5's sole guard - never move it (16...Nxe4?? 17.Rxh5! Qxh7#).
10. Pawn pushes/captures: never onto a defended piece or pawn attack, never while it guards my piece (g48 21.d6?! Bxd6; g51 28.f3?? left f5 loose). Trace pawn paths vs my own blockers (g52 f4 illegal: Nf3 blocked it).
11. Lost: defend/trade, 5-15 s, no undefended squares, no grabs; then play 3-13 s and let him drift: g52 played the last 14 moves at 3-13 s and the game ended 1/2 by threefold repetition.
12. Time: routine <=15 s, book <=10 s, m1-12 <=20 s, m13+ <=25 s. Long thinks never prevented a blunder (g46 0:18, g47 0:36, g48 0:32, g49 40-64 s, g50 ~11 min by m21, g51 ~9 min m1-19, g52 31-49 s m13-21 + 1:43 on Qe3 - all routine moves).

## Patterns
- Losses: grabbing units his queen/rook/pawn covered (g36,g42,g47,g51); queen 'trades' with no recapturer (g48,g50,g51); loose knights (g24,g40,g44,g46,g47,g51,g52); loose bishops (g42,g45); king mated on the 8th or h-file.
- Illegal tries cost g34,g44,g45,g47,g50,g52: after one rejection a different move, traced twice; never resend.
- Down material: defend, trade, 5-15 s, no new loose pieces; long thinks never fixed anything (g36-g52).
- g52 fixes: don't leave Nd2 loose - defend it (26.Re2) or move it (Nc4/Nb1); 26.Bd3? ignored 26...Rxd2.
- When winning: avoid repetition/stalemate drift - change a piece or push a pawn before the same position appears a third time; g52: Sonnet's 2B+N lead became a repetition draw.
