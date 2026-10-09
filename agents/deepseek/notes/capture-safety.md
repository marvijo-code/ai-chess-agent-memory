# Pre-move scan & blunders (g1-g50)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality: my turn, my pieces only; geometry; path clear incl. own blockers (g45/g47 illegal Qxb7/Qxb4: Qd8 has no line). 3 invalid = forfeit (g34,g44,g45). After one rejection play a DIFFERENT trivial legal move - never resend (g50 Rxc7 illegal -> Nd8, correct).
2. HIS last move first: what does it attack now? g46 16...Rad8 hit Qd1; 17.Be3?? ignored it and lost the queen.
3. Destination: which enemy PAWN/knight/bishop/rook(rank-file)/queen/king attacks it? Attacked+undefended -> reject. Moving vacates guards (g30). QUEEN-vs-QUEEN: if my queen attacks his, check MY square first - attacked+undefended means he captures first (g50 10...Qc7?? undefended vs Qd6, 11.Qxc7 = free queen). A trade needs a legal recapture.
4. My attacked piece: save/trade/defend NOW; queen attacked by a rook must MOVE (g42,g46).
5. Recapturers on the destination: include rooks on rank/file, PAWNS, QUEENS (g36,g42,g47; g48 22.Qxd6?? Qxd6 = Q for B). Before relying on a recapture, trace its path: no Black rook reaches c7 (g50).
6. Knight: never undefended or pawn/bishop/queen-attacked, esp. down material (g44,g46,g47). Nd2 trap: g46/g48 Nd2?? Qxd2 - free whenever his queen reaches d2.
7. Rook: loose rook facing his rook loses (g27,g43); his rook to an open file/rank at my loose piece = emergency (g42,g46).
8. Mate nets before grabs: g49 15...Bxh6?? 16.Qxh6 + 17.Rxh5 (removes the h5 block, rook guards h7) -> Qxh7#; cover h7 or refuse the trade. 16...Nxe4?? grabbed while the net stood.
9. Pawn pushes/captures: never onto a defended piece or pawn's attack, never while it guards my piece; g48 21.d6?! Bxd6 lost a pawn.
10. Lost: defend/trade, 5-15 s, no 'active' piece to an undefended square (g39,g40,g46,g47).
11. Time: routine <=15 s, book <=10 s, m1-12 <=20 s. g46 flagged 0:18; g47 0:36; g48 mated 0:32; g49 40-64 s/move, mated m18; g50 ~11 min used in 21 moves (54-99 s thinks), queen lost m10. Long thinks never prevented a blunder.

## Blunder catalogue (g1-g50, all losses)
g1 Nxb2, g2 Nxc2, g3 Bxd4, g4 Re8, g5 Nb3, g6 Qa1#, g8 Bf5, g10 Qc2, g11 Bf5/Qxb4, g12 Qxd5, g13 Qh6, g14 Qe1+, g15 Bxd5, g16 Nc4, g17 Qd6, g18 Rxe5, g19 Qxd5/Rc8#, g20 Nd7, g21 Rb1#, g22 Nef5, g23 Nb3, g24 Bg4, g25 Qf6/Qg6, g26 Bf5/Qd7, g27 Rc2, g28 Qxc4/Nd4, g29 Rd8, g30 Bxe6/f4, g31 Re7/Qd6, g32 Bxc3/Rxd3, g33 Be3/Qd2, g34 Bxd4/Qe3+3illegal, g35 Qxc1, g36 Qxa4, g37 Qxc3, g38 Nc4->Rxc7, g39 Bxe5/Qxd5/Qd4#, g40 Qxh7#, g41 Rfd8->Bxa5, g42 Qxd5/Rfc8, g43 Bxb4/Qa4, g44 Nc5+illegal, g45 Ra5/Qxb7+forfeit, g46 Be3/Rxd1+flag, g47 Nxe4/Nb4+2illegal+flag, g48 d6/Qxd6/Nd2, g49 Bxh6/Nxe4->Rxh5/Qxh7#, g50 Qc7?? (free queen) + illegal Rxc7.

## Patterns
- Illegal tries cost g34,g44,g45; g47 resent Qxb4 twice; g50 tried Rxc7 (no rook line). One rejection -> different move, traced twice.
- Never send a move my reasoning just rejected (g48 22.Qxd6).
- Nd2 trap: g46,g48.
- Queen on his line/attacked square or facing his rook/queen (g10..g50); d5,a4,b5,d1,c7 are traps. A queen move 'attacking his queen' is only a trade if MY square is defended and a recapture exists (g50).
- His rook lands on my loose piece's file -> fix it that move (g42,g46).
- Knight to an undefended/pawn-attacked square, esp. down material (g24,g40,g44,g46,g47).
- Grab while his mate net stands = loss (g49 16...Nxe4; g43 Bxd6).
- Down material: no tricks; defend, trade, 5-15 s.
- No luft + enemy Q/R on the 8th or h-file -> mate (g14..g32,g42,g49).
- Long thinks never fixed anything (g36..g50).
