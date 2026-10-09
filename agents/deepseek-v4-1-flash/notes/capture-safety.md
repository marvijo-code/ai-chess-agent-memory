# Pre-move scan & blunder catalogue (g1-g35)

## Scan (EVERY move, 5s) - on the FINAL move, not the plan
1. Destination: which enemy PAWN, KNIGHT, BISHOP, KING, QUEEN, ROOK attacks it? Attacked+undefended -> reject. King attacks: no rook beside his king (g29). Lines: d3/c2-B hits g6+h7; Qf3 hits f5; Qf5 hits d7; Qc7+Rc8 cover c2; e3-B covers d2+c1 (g35).
2. MY attacked piece: 0 defenders -> defend/move it NOW (g30 15...Nf6?? lost the e6-bishop). Save/trade it before any pawn-grab (g29 16...Rxc3?? while Rd6 attacked Bd7).
3. A moving piece OR PAWN stops defending its old squares (g30 20...f4?? was Ne4's only defender). Re-scan after checks/forced moves and every enemy move (g16,g27,g30).
4. Pawn hits my knight -> move the knight to a safe flight; never grab the pawn with a piece (g34 10.Bxd4?? Qxd4 = B for P; d4 had e5-pawn+Qd8). Knight captures: count every recapturer, even a check (g6,g19,g22,g23).
5. Queen captures/moves: list ALL attackers AND defenders of the destination incl. rooks on files and bishops on diagonals (g35: Be3 defended c1). NEVER take a defended rook with the queen (g35 18...Qxc1?? Bxc1 Rxc1 Qxc1 = Q+R for R+B = -6). Reject Q for R/B/N/P (g18,g25,g35); d5 is a queen trap (g12,g17,g18,g19). Name the squares the queen leaves (g17).
6. A queen trade offer needs a legal recapturer on the square: 14.Qe3?? Qxe3 = queen for nothing (g34). Queen attacked by a rook: retreat, never grab a defended piece (g35).
7. Knight forks: cover BOTH targets or vacate one (g23,g27); never step onto a forker's square (g23); 2v2 means the LAST recapturer lands there (g27).
8. Pinned knight (Ba4-d7-e8): moving it loses the exchange; unpin ...Rb8 (g15).
9. Mate nets: c1 king ...Qa1# (g6); his Qh5+Bd3 cover h7 - defend ...g6 not ...Qf6?? (g25); Qxf7# (g12); ...Qf2#/...Rb1# (g10,g21); ...Qg8# (g24); king on the 8th, pawns f7/g7/h7, no luft -> Re8#/Qc8#/Qd8#/Qxe8#/Rxd8# (g14,g16,g19,g20,g24,g25,g26,g29,g32).
10. Pawn pushes: never onto a defended piece (g12), a knight-attacked square (g16), an enemy pawn's attack (g24), a bishop's capture (g25), where a queen takes with tempo (g19), or when that pawn guards one of my pieces (g30).
11. Pawn grabs: no rook grab of a pawn a rook/queen/king recaptures (g18,g29); no bishop/major grab of a twice-defended pawn (g23,g34); no pawn grabs down material.
12. Legality BEFORE sending (3 invalid tries = forfeit, g34): path clear/own pieces block (g25,g30); knight geometry (g28); bishop geometry (d3 cannot reach e3, g34).
13. A recapture you cannot make is no defense: after 13...Bxe6 (g30) e6 had no recapturer.

## Blunder catalogue (all losses, 35 games)
g1 Nxb2|g2 a3 Nxc2|g3 Bxd4/Qxe4|g4 Bxd2/Re8 Qxe8#|g5 Qd2 Nb3|g6 e5 Qa1#|g8 Bf5/Qd7|g10 Qc2 Rxc2|g11 Bf5/Qxb4|g12 h6/Nh7/Qxd5|g13 Qxh6/Qh8+|g14 Qe1+|g15 Nb6/Bxd5|g16 Nc4/Nxe4|g17 Qd6|g18 Qd5/Rxe5|g19 Nd7/b3/Qxd5/Rc8|g20 Nd7|g21 Bd3/Nc4/Qb3/Rb1#|g22 Nef5/Nxd6/Qxc4|g23 Ng3/Bd2/Bxa5/Nxe5|g24 Bg4|g25 d3/Qf6/Qg6|g26 Bf5/Qd7|g27 Nc2/Rac1/Rc2/Re2|g28 Qxc4/Nd4|g29 Rxc3/Rxc2/Rd8|g30 Bxe6?/Nf6??/f4??|g31 Re7?/Qd6?/Bxh6?/Nxb5?|g32 Bxf6?/Bxc3?/Rxd3?|g33 Be3?/Qd2?/Nxe5?/Bd4?|g34 Bxd4??/Qe3??/3x illegal|g35 Rfe8?/Qxc1??

## Patterns
- My queen on a square his queen/slider covers (g10,g12,g13,g17,g18,g19,g22,g28,g31,g34); d5 is the classic trap; a trade offer with no recapturer loses the queen outright (g34).
- Queen grabs: a defended target square is a killer - count ALL recapturers incl. bishops on diagonals with a clear path (g35 Be3-d2-c1); Q for R = -2, and here Q+R for R+B = -6 (g35).
- Tempo hits: his rook hits my queen (Rc1xc7); 'defended' does not save it - retreat or counter-hit, never grab (g35).
- Back rank: king without luft + enemy Q/R on the 8th (g14,g16,g19,g20,g24,g25,g26,g29,g32).
- Pawn hits/forks: e5-e6 forks Bd7+f7 (g30); ...f5 lets Nxc5 (g30); a pawn hitting my knight -> move the knight, not a piece grab (g34).
- Illegal tries (g25,g28,g30,g33,g34) cost games by forfeit: verify path/geometry before sending.
- Long thinks never prevented a blunder - the 5s destination scan is the fix (g35: 68s on move 18 still blundered).
