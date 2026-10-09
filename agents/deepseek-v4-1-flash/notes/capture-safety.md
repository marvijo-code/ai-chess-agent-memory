# Pre-move scan & blunder catalogue (g1-g39)

## Scan (EVERY move, 5s) - on the FINAL move, not the plan
1. Destination: which enemy PAWN, KNIGHT, BISHOP, KING, QUEEN, ROOK attacks it? Attacked+undefended -> reject. Lines: d3/c2-B hits g6+h7; Qf3 hits f5; Qc7+Rc8 cover c2; e3-B covers d2+c1 (g35); c6-PAWN covers d5 (g39).
2. Scan what the move OPENS (vacating square/file): g38 19.Bb3 uncovered c2->b3 (Rc1 hit Qc7); g39 15.Nf4 vacated d5, opening the d-file (16...Qd4#).
3. MY attacked piece: save/trade/defend it NOW (g30), before any pawn-grab (g29). A moving piece OR PAWN stops defending its old squares (g30); re-scan after checks/every enemy move.
4. Pawn hits my KNIGHT -> safe flight, never grab with a piece (g34). Pawn hits my QUEEN -> retreat, not capture (g37 28.Qxc3?? bxc3). Knight captures: count every recapturer, even a check (g6,g19,g22,g23).
5. Queen move/capture: list ALL attackers AND defenders of the destination incl. rooks on files, bishops on diagonals, PAWNS (g37 c3; g39 13.Qxd5?? cxd5 - c6-pawn). Never Qx a defended rook (g35 Qxc1?? Bxc1). No Q for R/B/N/P (g18,g25,g35-g39). Never Qxp on a square an enemy ROOK hits (g36 Qxa4?? Rxa4!).
6. Q on the c-file (Qc7/Qc8) with his Be3+Rc1: retreat ...Qb8/...Qd8 before the file opens (g35,g38). Q trade offer needs a legal recapturer (g34). Rook hits my queen -> retreat, never grab (g35).
7. Knight forks: cover BOTH targets or vacate one (g23,g27); never step onto a forker's square (g23); 2v2 = LAST recapturer lands there (g27).
8. Pinned Nd7 (Ba4, Re8): moving loses the exchange; unpin ...Rb8 (g15).
9. Mate nets: Qa1# (g6); Qd4# from Qd8 down an open d-file onto Kf2 (g39); Qxh7+ covered by Qh5+Bd3 - play ...g6 not ...Qf6?? (g25); Qf2#/Rb1#/Qg8# (g10,g21,g24); king on the 8th, no luft -> Re8#/Qc8#/Qd8#/Rxd8# (g14..g32).
10. Pawn pushes: never onto a defended piece (g12), a knight-attacked square (g16), an enemy pawn's attack (g24), a bishop's capture (g25), where a queen takes with tempo (g19), or when it guards my piece (g30).
11. Pawn grabs: never a pawn a recapturer defends (g18,g23,g29,g34); never down material or while a piece hangs.
12. Legality BEFORE sending (3 invalid tries = forfeit, g34): trace the path square by square (g39 Qxd8 blocked by his Nd5; g38 Rac8 blocked by Bc8); knight/bishop geometry (g28,g34,g36).
13. A recapture I cannot make is no defense (g30 13...Bxe6).

## Blunder catalogue (all losses, g1-g39)
g1 Nxb2|g2 a3 Nxc2|g3 Bxd4/Qxe4|g4 Bxd2/Re8 Qxe8#|g5 Qd2 Nb3|g6 e5 Qa1#|g8 Bf5/Qd7|g10 Qc2 Rxc2|g11 Bf5/Qxb4|g12 h6/Nh7/Qxd5|g13 Qxh6/Qh8+|g14 Qe1+|g15 Nb6/Bxd5|g16 Nc4/Nxe4|g17 Qd6|g18 Qd5/Rxe5|g19 Nd7/b3/Qxd5/Rc8|g20 Nd7|g21 Bd3/Nc4/Qb3/Rb1#|g22 Nef5/Nxd6/Qxc4|g23 Ng3/Bd2/Bxa5/Nxe5|g24 Bg4|g25 d3/Qf6/Qg6|g26 Bf5/Qd7|g27 Nc2/Rac1/Rc2/Re2|g28 Qxc4/Nd4|g29 Rxc3/Rxc2/Rd8|g30 Bxe6?/Nf6??/f4??|g31 Re7?/Qd6?/Bxh6?/Nxb5?|g32 Bxf6?/Bxc3?/Rxd3?|g33 Be3?/Qd2?/Nxe5?/Bd4?|g34 Bxd4??/Qe3??/3x illegal|g35 Rfe8?/Qxc1??|g36 Qxa4??/1 illegal/flagged m30|g37 28.Qxc3?? bxc3|g38 18...Nc4??+19...Nb6?? -> 20.Rxc7|g39 12.Bxe5??/13.Qxd5?? cxd5 (Q for N)/15.Nf4?? Bxf4+ -> Qd4#

## Patterns
- Queen on a square his queen/slider/rook/PAWN covers (g10,g12,g13,g17,g18,g19,g22,g28,g31,g34-g39); d5 the classic trap (c6-pawn, g39).
- Tempo hits: rook hits queen -> retreat, never grab (g35,g38); pawn hits queen -> retreat (g37).
- Back rank: no luft + enemy Q/R on the 8th (g14,g16,g19,g20,g24,g25,g26,g29,g32).
- Lost positions: no 'active' piece to an undefended square (g39 15.Nf4?? Bxf4+); defend/trade, 5-15s.
- Pawn hits/forks: e6 forks Bd7+f7 (g30); ...f5 lets Nxc5 (g30); never push a pawn that guards a piece (g30 f4).
- Illegal tries (g25,g28,g30,g33,g34,g36,g38,g39) = forfeit risk at 3: trace path/geometry before sending.
- Clock: g36 flagged m30; g37 38-56s/m2-28; g38 26-45s m12-20; g39 37-83s m9-13 (illegal try after 83s), blunder m12.
