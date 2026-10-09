# Pre-move scan & blunders (g1-g46)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality: my turn, my pieces only; geometry; all path squares clear incl. own blockers. g44 22...axb3 illegal (a6-pawn); g45 'Qxb7' with Qd8 (no line). 3 invalid = forfeit (g34,g44,g45). After one rejection pick a DIFFERENT simple legal move.
2. HIS last move: what does it now attack? g46 16...Rad8 hit Qd1 and 17.Be3?? ignored it - fix that piece the same move.
3. Destination: which enemy PAWN/knight/bishop/rook(rank-file)/queen/king attacks it? Attacked+undefended -> reject. Moving a piece vacates its guards (g30).
4. My attacked piece: save/trade/defend NOW (g30,g42,g43,g44,g45 Bb7,g46). A queen attacked by a rook must MOVE - 'defended' still loses Q for R (g46 17...Rxd1).
5. My queen: never on an open file/rank his rook can enter, or a pawn/slider-attacked square. Count ALL recapturers incl. rooks on the rank/file and PAWNS (g36,g42).
6. Knight: never undefended or pawn/bishop-attacked, esp. down material (g44; g46 29.Nd2?? Qxd2).
7. Rook: loose rook facing his rook loses (g27,g43); his rook to an open file/rank at my loose piece = emergency (g42,g46).
8. Forks/mates: cover both targets; Qa1#(g6), Qd4#(g39), Qxh7#(g40), Qe1+/Qxd1#(g42), back-rank (g14..g32).
9. Pawn pushes/captures: never onto a defended piece, a pawn's attack, where a queen gains tempo, while it guards my piece; B-for-P loses (g6,g34,g39,g42,g43).
10. Lost: no 'active' piece to an undefended square (g39,g40,g46); defend/trade; 5-15 s.
11. Time: routine <=15 s, m10+ <=25 s. g46: 20-55 s/move, flagged 0:18 vs 14:21; 17.Be3?? still came after 55 s. Long thinks never prevented one blunder (g36,g42,g43,g44,g45,g46).

## Catalogue (losses g1-g46)
g1 Nxb2, g2 Nxc2, g3 Bxd4/Qxe4, g4 Bxd2/Re8, g5 Nb3, g6 Qa1#, g8 Bf5/Qd7, g10 Qc2 Rxc2, g11 Bf5/Qxb4, g12 Qxd5, g13 Qh6, g14 Qe1+, g15 Nb6/Bxd5, g16 Nc4/Nxe4, g17 Qd6, g18 Qd5/Rxe5, g19 Nd7/Qxd5/Rc8#, g20 Nd7, g21 Rb1#, g22 Nef5/Qxc4, g23 Nb3, g24 Bg4, g25 Qf6/Qg6, g26 Bf5/Qd7, g27 Rc2/Re2, g28 Qxc4/Nd4, g29 Rd8, g30 Bxe6/f4, g31 Re7/Qd6, g32 Bxc3/Rxd3, g33 Be3/Qd2/Bd4, g34 Bxd4/Qe3+3 illegal, g35 Qxc1??, g36 Qxa4??, g37 Qxc3??, g38 Nc4/Nb6->Rxc7, g39 Bxe5/Qxd5/Nf4->Qd4#, g40 Nxe4/Nc6/Qd7->Qxh7#, g41 Rfd8->Bxa5, g42 Nxd5/h3/Qxd5??/Rfc8, g43 20.Bxb4?? Rxa1, 22.Qa4?? Rxa4, g44 Nc6?/Nb3??/Nc5??+illegal, g45 13...Ra5?? Qxb7 + forfeit, g46 17.Be3?? Rxd1 (Q for R) then flag.

## Patterns
- Illegal tries: g25,g28,g30,g33,g34,g36,g38,g39,g43,g44,g45; g34,g44,g45 lost the game. One rejected attempt -> different trivially legal move, traced twice.
- Queen on a square his queen/slider/rook/PAWN covers, or on an open file/rank facing his rook (g10..g43, g46). d5, a4, b5, d1 are traps.
- His rook to a file/rank where my piece sits (queen/bishop): fix it that move (g42,g46).
- Knight to an undefended or pawn/bishop-attacked square, esp. down material (g24,g40,g44,g46).
- Tempo hit at my queen: retreat, never grab; FIRST save my attacked pieces (g41,g45).
- My pawn/piece move leaves my other unit loose (g30,g42,g43,g45 b7-bishop).
- No luft + enemy Q/R on the 8th -> back-rank mate (g14..g32,g42).
- Down material: no 'active' piece to an undefended square (g39,g40,g46); B-for-P grabs lose (g43).
- Long thinks never fixed anything; flags followed (g36,g42,g43,g44,g45,g46).
