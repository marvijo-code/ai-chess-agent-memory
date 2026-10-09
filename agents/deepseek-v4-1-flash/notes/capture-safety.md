# Pre-move scan & blunders (g1-g44)

## Scan (EVERY move, 5 s) - FINAL position
1. Destination: which enemy PAWN, KNIGHT, BISHOP, rook (rank/file), QUEEN, KING attacks it? Attacked+undefended -> reject. Piece moves vacate squares; pawn pushes stop guarding old squares (g30).
2. My attacked piece: save/trade/defend NOW before any other move (g30,g42,g43,g44).
3. Queen: never on a square his PAWN/slider/rook attacks (g37,g43). Every queen capture/trade: count ALL recapturers incl. rooks on destination rank/file and PAWNS (g36,g42). No Q for R/B/N/P (g18,g35-g43).
4. Knight: never an undefended square or one a pawn/bishop takes, esp. down material (g40 Nxe4/Nc6; g44 21...Nb3?? Bxb3, 22...Nc5?? bxc5).
5. Rook: undefended rook facing his rook loses (g27,g43); his rook to an open file at my loose piece = emergency (g42).
6. Forks/mate nets: cover both targets; Qa1# (g6), Qd4# (g39), Qxh7# with Ng5+Qh5 -> ...g6 (g40), back-rank (g14..g41), Qe1+/Qxd1# vs loose Rd1 (g42).
7. Pawn pushes/captures: never onto a defended piece, a pawn's attack, a bishop's capture, where a queen gains tempo, while it guards my piece, or a pawn a recapturer defends; B-for-P loses (g6,g34,g39,g42,g43).
8. Legality BEFORE sending (3 invalid = forfeit): trace path square by square; check own blockers. g44 22...axb3 illegal (a6-pawn to b5, not b3); 22...Rxc1 blocked by own c5-pawn/Qc7.
9. Lost position: no 'active' piece to an undefended square (g39,g40); defend/trade; 5-15 s.
10. Time: routine <=15 s; from m10 NO move >25 s. g44 spent 47-63 s many moves and 2:10 on 22...Nc5, clock 2:58 vs 13:38, then timeout/forfeit. Long thinks never fixed anything.

## Catalogue (losses g1-g44)
g1 Nxb2, g2 Nxc2, g3 Bxd4/Qxe4, g4 Bxd2/Re8, g5 Nb3, g6 Qa1#, g8 Bf5/Qd7, g10 Qc2 Rxc2, g11 Bf5/Qxb4, g12 Qxd5, g13 Qh6/Qh8+, g14 Qe1+, g15 Nb6/Bxd5, g16 Nc4/Nxe4, g17 Qd6, g18 Qd5/Rxe5, g19 Nd7/Qxd5/Rc8#, g20 Nd7, g21 Rb1#, g22 Nef5/Qxc4, g23 Nb3/Bxa5, g24 Bg4, g25 Qf6/Qg6, g26 Bf5/Qd7, g27 Rc2/Re2, g28 Qxc4/Nd4, g29 Rd8, g30 Bxe6/f4, g31 Re7/Qd6, g32 Bxc3/Rxd3, g33 Be3/Qd2/Bd4, g34 Bxd4/Qe3+3 illegal, g35 Qxc1??, g36 Qxa4??, g37 Qxc3??, g38 Nc4/Nb6->Rxc7, g39 Bxe5/Qxd5/Nf4->Qd4#, g40 Nxe4/Nc6/Qd7->Qxh7#, g41 Rfd8->Bxa5, g42 Nxd5/h3/Qxd5??, g43 20.Bxb4?? Rxa1, 22.Qa4?? Rxa4, g44 15...Nc6?->16.d5, 21...Nb3?? Bxb3, 22...Nc5?? bxc5, 22...axb3/Rxc1 illegal.

## Patterns
- Queen on a square his queen/slider/rook/PAWN covers (g10..g43); d5 and a4 are traps.
- Knight to an undefended or pawn/bishop-attacked square, esp. down material (g24,g40,g44).
- Tempo hits at my queen: retreat, never grab (g35,g37,g38,g41); rook at my loose piece: save it (g42,g43).
- My pawn capture opening a file next to my undefended rook (g43).
- No luft + enemy Q/R on the 8th -> back-rank mate (g14..g32); Qxh7# with Ng5 (g40); Qe1+/Qxd1# (g42).
- Down material: no 'active' piece to an undefended square (g39,g40); B-for-P grabs (g43) and pawn pushes that guard a piece (g30) lose.
- Illegal tries (g25,g28,g30,g33,g34,g36,g38,g39,g43,g44): forfeit at 3; trace path/geometry/own blockers before sending.
- Long thinks (47-82 s) never fixed anything and caused flag/timeout (g36,g42,g43,g44); the 5-s destination scan catches the blunders.
