# Pre-move scan & blunder catalogue (g1-g37)

## Scan (EVERY move, 5s) - on the FINAL move, not the plan
1. Destination: which enemy PAWN, KNIGHT, BISHOP, KING, QUEEN, ROOK attacks it? Attacked+undefended -> reject. Lines: d3/c2-B hits g6+h7; Qf3 hits f5; Qc7+Rc8 cover c2; e3-B covers d2+c1 (g35).
2. MY attacked piece: 0 defenders -> defend/move it NOW (g30). Save/trade it before any pawn-grab (g29).
3. A moving piece OR PAWN stops defending its old squares (g30); re-scan after checks/forced moves and every enemy move.
4. Pawn hits my KNIGHT -> safe flight, never grab with a piece (g34). Pawn hits my QUEEN -> retreat, not capture (g37 28.Qxc3?? bxc3: b4-pawn guarded c3, Qc7 behind on the file). Knight captures: count every recapturer, even a check (g6,g19,g22,g23).
5. Queen captures/moves: list ALL attackers AND defenders of the destination incl. rooks on files, bishops on diagonals, PAWNS (g37 c3). NEVER take a defended rook with the queen (g35 18...Qxc1?? Bxc1!). No Q for R/B/N/P (g18,g25,g35,g37); d5 is a queen trap (g12,g17,g18,g19). Never Qxp on a square an enemy ROOK hits down an open file (g36 14...Qxa4?? Rxa4!).
6. Queen trade offer needs a legal recapturer on the square (g34 14.Qe3?? Qxe3). Queen attacked by a rook: retreat, never grab (g35).
7. Knight forks: cover BOTH targets or vacate one (g23,g27); never step onto a forker's square (g23); 2v2 = LAST recapturer lands there (g27).
8. Pinned knight (Ba4-d7-e8): moving loses the exchange; unpin ...Rb8 (g15).
9. Mate nets: ...Qa1# (g6); Qxh7+ covered by his Qh5+Bd3 - defend ...g6 not ...Qf6?? (g25); ...Qf2#/...Rb1#/...Qg8# (g10,g21,g24); king on the 8th, f7/g7/h7, no luft -> Re8#/Qc8#/Qd8#/Qxe8#/Rxd8# (g14..g32).
10. Pawn pushes: never onto a defended piece (g12), a knight-attacked square (g16), an enemy pawn's attack (g24), a bishop's capture (g25), where a queen takes with tempo (g19), or when it guards my piece (g30).
11. Pawn grabs: no rook/major/bishop grab of a pawn a recapturer defends (g18,g23,g29,g34); no pawn grabs down material or while a piece hangs.
12. Legality BEFORE sending (3 invalid tries = forfeit, g34): path clear/own pieces block (g25,g30); knight geometry (g28; g36); bishop geometry (g34).
13. A recapture I cannot make is no defense: after 13...Bxe6 (g30) e6 had no recapturer.

## Blunder catalogue (all losses, g1-g37)
g1 Nxb2|g2 a3 Nxc2|g3 Bxd4/Qxe4|g4 Bxd2/Re8 Qxe8#|g5 Qd2 Nb3|g6 e5 Qa1#|g8 Bf5/Qd7|g10 Qc2 Rxc2|g11 Bf5/Qxb4|g12 h6/Nh7/Qxd5|g13 Qxh6/Qh8+|g14 Qe1+|g15 Nb6/Bxd5|g16 Nc4/Nxe4|g17 Qd6|g18 Qd5/Rxe5|g19 Nd7/b3/Qxd5/Rc8|g20 Nd7|g21 Bd3/Nc4/Qb3/Rb1#|g22 Nef5/Nxd6/Qxc4|g23 Ng3/Bd2/Bxa5/Nxe5|g24 Bg4|g25 d3/Qf6/Qg6|g26 Bf5/Qd7|g27 Nc2/Rac1/Rc2/Re2|g28 Qxc4/Nd4|g29 Rxc3/Rxc2/Rd8|g30 Bxe6?/Nf6??/f4??|g31 Re7?/Qd6?/Bxh6?/Nxb5?|g32 Bxf6?/Bxc3?/Rxd3?|g33 Be3?/Qd2?/Nxe5?/Bd4?|g34 Bxd4??/Qe3??/3x illegal|g35 Rfe8?/Qxc1??|g36 Qxa4??/1 illegal/flagged m30|g37 28.Qxc3?? bxc3 (b4-pawn; Qc7 on file) Q for P

## Patterns
- Queen on a square his queen/slider/rook/PAWN covers (g10,g12,g13,g17,g18,g19,g22,g28,g31,g34,g35,g36,g37); d5 the classic trap; trade offers with no recapturer lose the queen (g34); rook files: Qxa4/Qxc1 (g35,g36).
- Tempo hits: his rook hits my queen (Rc1xc7) - retreat, never grab (g35); his pawn hits my queen - retreat, not capture (g37).
- Back rank: no luft + enemy Q/R on the 8th (g14,g16,g19,g20,g24,g25,g26,g29,g32).
- Pawn hits/forks: e6 forks Bd7+f7 (g30); ...f5 lets Nxc5 (g30); never push a pawn that guards a piece (g30 f4).
- Illegal tries (g25,g28,g30,g33,g34,g36) = forfeit risk: verify path/geometry before sending.
- Clock: g36 flagged m30 (27s left); g37 38-56s/moves 2-28, the m28 blunder still came. Only the 5s final-move scan helps.
