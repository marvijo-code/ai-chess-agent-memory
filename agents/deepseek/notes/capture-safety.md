# Pre-move scan & blunders (g1-g48)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality: my turn, my pieces only; geometry; all path squares clear incl. own blockers. g44 22...axb3 illegal (a6-pawn); g45 'Qxb7' with Qd8 (no line); g47 'Qxb4' with Qd8 tried TWICE. 3 invalid = forfeit (g34,g44,g45). After one rejection pick a DIFFERENT simple legal move - never resend.
2. HIS last move: what does it now attack? g46 16...Rad8 hit Qd1 and 17.Be3?? ignored it - fix that piece the same move.
3. Destination: which enemy PAWN/knight/bishop/rook(rank-file)/queen/king attacks it? Attacked+undefended -> reject. Moving a piece vacates its guards (g30).
4. My attacked piece: save/trade/defend NOW (g30,g42,g43,g44,g45 Bb7,g46). A queen attacked by a rook must MOVE - 'defended' still loses Q for R (g46).
5. Recapturers on the destination: include rooks on the rank/file, PAWNS and QUEENS (g36,g42,g47). g48 22.Qxd6?? Qxd6 = Q for B; a pawn/bishop that is simply lost stays lost - accept it.
6. Knight: never undefended or pawn/bishop/queen-attacked, esp. down material (g44,g46,g47). Nd2 trap: g46 29.Nd2?? Qxd2, g48 23.Nd2?? Qxd2 - never Nd2 while his queen can reach d2.
7. Rook: loose rook facing his rook loses (g27,g43); his rook to an open file/rank at my loose piece = emergency (g42,g46).
8. Forks/mates: cover both targets; Qa1#(g6), Qd4#(g39), Qxh7#(g40), Qe1+/Qxd1#(g42), back-rank (g14..g32).
9. Pawn pushes/captures: never onto a defended piece, a pawn's attack, where a queen gains tempo, while it guards my piece; B-for-P loses (g6,g34,g39,g42,g43). g48 21.d6?! Bxd6 lost a pawn cleanly.
10. Lost: no 'active' piece to an undefended square (g39,g40,g46,g47); defend/trade; 5-15 s.
11. Time: routine <=15 s, book <=10 s, m10+ <=25 s, m1-12 <=20 s. g46 flagged 0:18 vs 14:21; g47 flagged 0:36 vs 17:39; g48: 62 s m1, 45-67 s moves m4-21, mated with 0:32 vs 17:06. Long thinks never prevented one blunder (g36,g42,g43,g44,g45,g46,g47,g48).

## Catalogue (losses g1-g48)
g1 Nxb2, g2 Nxc2, g3 Bxd4/Qxe4, g4 Bxd2/Re8, g5 Nb3, g6 Qa1#, g8 Bf5/Qd7, g10 Qc2 Rxc2, g11 Bf5/Qxb4, g12 Qxd5, g13 Qh6, g14 Qe1+, g15 Nb6/Bxd5, g16 Nc4/Nxe4, g17 Qd6, g18 Qd5/Rxe5, g19 Nd7/Qxd5/Rc8#, g20 Nd7, g21 Rb1#, g22 Nef5/Qxc4, g23 Nb3, g24 Bg4, g25 Qf6/Qg6, g26 Bf5/Qd7, g27 Rc2/Re2, g28 Qxc4/Nd4, g29 Rd8, g30 Bxe6/f4, g31 Re7/Qd6, g32 Bxc3/Rxd3, g33 Be3/Qd2/Bd4, g34 Bxd4/Qe3+3 illegal, g35 Qxc1??, g36 Qxa4??, g37 Qxc3??, g38 Nc4/Nb6->Rxc7, g39 Bxe5/Qxd5/Nf4->Qd4#, g40 Nxe4/Nc6/Qd7->Qxh7#, g41 Rfd8->Bxa5, g42 Nxd5/h3/Qxd5??/Rfc8, g43 20.Bxb4?? Rxa1, 22.Qa4?? Rxa4, g44 Nc6?/Nb3??/Nc5??+illegal, g45 13...Ra5?? Qxb7 + forfeit, g46 17.Be3?? Rxd1 then flag, g47 11...Nxe4??/15...Nb4?? + 2 illegal Qxb4 + flag, g48 21.d6?! Bxd6, 22.Qxd6?? Qxd6 (my note said Qd2!), 23.Nd2?? Qxd2, Qxe1/Qxf1+/Qxf2, mated m30.

## Patterns
- Illegal tries: g25,g28,g30,g33,g34,g36,g38,g39,g43,g44,g45,g47; g34,g44,g45 lost the game. One rejected attempt -> different trivially legal move, traced twice.
- Never send a move my own reasoning just rejected (g48 22.Qxd6; note read 'safer is Qd2').
- Nd2 trap: g46 29.Nd2?? Qxd2 and g48 23.Nd2?? Qxd2 - a knight on d2 is free whenever his queen can reach d2.
- Queen on a square his queen/slider/rook/PAWN covers, or on an open file/rank facing his rook (g10..g43, g46). d5, a4, b5, d1 are traps.
- His rook to a file/rank where my piece sits (queen/bishop): fix it that move (g42,g46).
- Knight to an undefended or pawn/bishop/queen-attacked square, esp. down material (g24,g40,g44,g46,g47).
- Tempo hit at my queen: retreat, never grab; FIRST save my attacked pieces (g41,g45).
- My pawn/piece move leaves my other unit loose (g30,g42,g43,g45 b7-bishop).
- No luft + enemy Q/R on the 8th -> back-rank mate (g14..g32,g42).
- Down material: no 'active' piece to an undefended square (g39,g40,g46,g47); B-for-P grabs lose (g43).
- Long thinks never fixed anything; flags/lost clocks followed (g36,g42,g43,g44,g45,g46,g47,g48).
