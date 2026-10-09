# Pre-move scan & blunders (g1-g45)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality first: my turn, my pieces only; piece geometry; every path square clear incl. own blockers. g44 22...axb3 illegal (a6-pawn); g45 'Qxb7' with Qd8 (no line to b7). 3 invalid = forfeit (g34,g44,g45); after one rejection pick a DIFFERENT simple move.
2. Destination: which enemy PAWN/knight/bishop/rook(rank-file)/queen/king attacks it? Attacked+undefended -> reject. Moving a piece vacates its guards (g30).
3. My attacked piece: save/trade/defend NOW (g30,g42,g43,g44; g45 Bb7 after 13.Qxb5). Attacking his queen is no excuse for leaving my piece hanging (g45 13...Ra5??).
4. Queen: never on a pawn/slider/rook-attacked square (g37,g43). Count ALL recapturers incl. rooks on the destination rank/file and PAWNS (g36,g42).
5. Knight: never undefended or pawn/bishop-attacked, esp. down material (g44).
6. Rook: loose rook facing his rook loses (g27,g43); his rook to an open file at my loose piece = emergency (g42).
7. Forks/mates: cover both targets; Qa1#(g6), Qd4#(g39), Qxh7#(g40), Qe1+/Qxd1#(g42), back-rank (g14..g32).
8. Pawn pushes/captures: never onto a defended piece, a pawn's attack, where a queen gains tempo, while it guards my piece; B-for-P loses (g6,g34,g39,g42,g43).
9. Lost: no 'active' piece to an undefended square (g39,g40); defend/trade; 5-15 s.
10. Time: routine <=15 s, from m10 no move >25 s; long thinks never fixed anything and flag/forfeit risk is real (g36,g42,g43,g44,g45).

## Catalogue (losses g1-g45)
g1 Nxb2, g2 Nxc2, g3 Bxd4/Qxe4, g4 Bxd2/Re8, g5 Nb3, g6 Qa1#, g8 Bf5/Qd7, g10 Qc2 Rxc2, g11 Bf5/Qxb4, g12 Qxd5, g13 Qh6, g14 Qe1+, g15 Nb6/Bxd5, g16 Nc4/Nxe4, g17 Qd6, g18 Qd5/Rxe5, g19 Nd7/Qxd5/Rc8#, g20 Nd7, g21 Rb1#, g22 Nef5/Qxc4, g23 Nb3, g24 Bg4, g25 Qf6/Qg6, g26 Bf5/Qd7, g27 Rc2/Re2, g28 Qxc4/Nd4, g29 Rd8, g30 Bxe6/f4, g31 Re7/Qd6, g32 Bxc3/Rxd3, g33 Be3/Qd2/Bd4, g34 Bxd4/Qe3+3 illegal, g35 Qxc1??, g36 Qxa4??, g37 Qxc3??, g38 Nc4/Nb6->Rxc7, g39 Bxe5/Qxd5/Nf4->Qd4#, g40 Nxe4/Nc6/Qd7->Qxh7#, g41 Rfd8->Bxa5, g42 Nxd5/h3/Qxd5??, g43 20.Bxb4?? Rxa1, 22.Qa4?? Rxa4, g44 Nc6?/Nb3??/Nc5??+illegal, g45 13...Ra5?? Qxb7 + illegal 'Qxb7' forfeit.

## Patterns
- Illegal tries: g25,g28,g30,g33,g34,g36,g38,g39,g43,g44,g45; g34,g44,g45 lost the game. One rejected attempt -> different trivially legal move, traced twice.
- Queen on a square his queen/slider/rook/PAWN covers (g10..g43); d5, a4, b5 are traps.
- Knight to an undefended or pawn/bishop-attacked square, esp. down material (g24,g40,g44).
- Tempo hits at my queen: retreat, never grab; and FIRST save my attacked pieces (g41,g45).
- My pawn/piece move leaves my other unit loose (g30,g42,g43,g45 b7-bishop).
- No luft + enemy Q/R on the 8th -> back-rank mate (g14..g32,g42).
- Down material: no 'active' piece to an undefended square (g39,g40); B-for-P grabs lose (g43).
- Long thinks (47-82 s) never fixed anything; flags/forfeits followed (g36,g42,g43,g44,g45).
