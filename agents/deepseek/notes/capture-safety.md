# Pre-move scan & blunders (g1-g51)

## Scan (EVERY move, 5 s) - FINAL position
1. Legality: my turn, my pieces only; geometry; path clear incl. own blockers (g45/g47 illegal Qxb7/Qxb4: Qd8 has no line). 3 invalid = forfeit (g34,g44,g45). After one rejection play a DIFFERENT trivial legal move - never resend (g50 Rxc7 illegal -> Nd8, correct).
2. HIS last move first: what does it attack now? g46 16...Rad8 hit Qd1; 17.Be3?? ignored it and lost the queen.
3. Destination: which enemy PAWN/knight/bishop/rook(rank-file)/queen/king attacks it? Attacked+undefended -> reject. Moving vacates guards (g30).
4. EVERY queen capture is a queen move: (a) is the destination defended by ME - trace the defender, blockers kill it (g51 f5-pawn blocked Bb1); (b) if his queen takes mine there, do I recapture? g51 24.Qxd5?? Qxd5: nothing recaptures d5 (Nf3 cannot reach, Bb1 blocked) = Q for N; g50 10...Qc7?? and g48 22.Qxd6?? are the same class. 'Queens come off' is true only with a recapturer.
5. My attacked piece: save/trade/defend NOW; queen attacked by a rook must MOVE (g42,g46).
6. Recapturers on the destination: include rooks on rank/file, PAWNS, QUEENS (g36,g42,g47; g51 25.Rxe5?? dxe5 = R for P). Trace the recapture's path (g50 Rxc7).
7. Knight: never undefended or pawn/bishop/queen-attacked, esp. down material (g44,g46,g47,g51 Ng5?? Bxg5). Nd2 trap: g46/g48 Nd2?? Qxd2.
8. Rook: loose rook facing his rook loses (g27,g43); his rook to an open file/rank at my loose piece = emergency (g42,g46).
9. Mate nets before grabs: g49 15...Bxh6?? 16.Qxh6 + 17.Rxh5 -> Qxh7#; cover h7 or refuse the trade. 16...Nxe4?? while the net stood.
10. Pawn pushes/captures: never onto a defended piece or pawn's attack, never while it guards my piece; g48 21.d6?! Bxd6; g51 28.f3?? attacked Qe4 but he took the loose f5-pawn.
11. Lost: defend/trade, 5-15 s, no piece to an undefended square (g39,g40,g46,g47; g51 Be4??/Ng5?? kept hanging pieces).
12. Time: routine <=15 s, book <=10 s, m1-12 <=20 s. g46 flagged 0:18; g47 0:36; g48 mated 0:32; g49 40-64 s/move; g50 ~11 min by m21; g51 ~9 min on moves 1-19 (book thinks 41s/64s/58s/60s), queen lost m24 with 5:15 left. Long thinks never prevented a blunder.

## Blunder catalogue (g1-g51, all losses)
g1 Nxb2, g2 Nxc2, g3 Bxd4, g4 Re8, g5 Nb3, g6 Qa1#, g8 Bf5, g10 Qc2, g11 Bf5/Qxb4, g12 Qxd5, g13 Qh6, g14 Qe1+, g15 Bxd5, g16 Nc4, g17 Qd6, g18 Rxe5, g19 Qxd5/Rc8#, g20 Nd7, g21 Rb1#, g22 Nef5, g23 Nb3, g24 Bg4, g25 Qf6/Qg6, g26 Bf5/Qd7, g27 Rc2, g28 Qxc4/Nd4, g29 Rd8, g30 Bxe6/f4, g31 Re7/Qd6, g32 Bxc3/Rxd3, g33 Be3/Qd2, g34 Bxd4/Qe3+3illegal, g35 Qxc1, g36 Qxa4, g37 Qxc3, g38 Nc4->Rxc7, g39 Bxe5/Qxd5/Qd4#, g40 Qxh7#, g41 Rfd8->Bxa5, g42 Qxd5/Rfc8, g43 Bxb4/Qa4, g44 Nc5+illegal, g45 Ra5/Qxb7+forfeit, g46 Be3/Rxd1+flag, g47 Nxe4/Nb4+2illegal+flag, g48 d6/Qxd6/Nd2, g49 Bxh6/Nxe4->Rxh5/Qxh7#, g50 Qc7?? (free queen)+illegal Rxc7, g51 24.Qxd5?? (queen 'trade' with no recapturer, Q for N) / 25.Rxe5?? (dxe5, R for P) / Be4??, Ng5??.

## Patterns
- Illegal tries cost g34,g44,g45 and g50; one rejection -> a different move, traced twice; never resend (g47).
- Never send a move my reasoning just rejected (g48 22.Qxd6). Re-read the destination before submitting.
- QUEEN: never on his line/attacked square, and never 'trading' where no recapture exists - Q for N/B (g48, g50, g51). List defenders of MY queen square with exact paths.
- King on the 8th with no luft + his Q/R on the file -> mate (g14..g32,g42,g49).
- Knight to an undefended/pawn-attacked square, esp. down material (g24,g40,g44,g46,g47,g51).
- His rook lands on my loose piece's file -> save it that move (g42,g46).
- Down material: defend, trade, 5-15 s, no more loose pieces (g39,g40,g46,g47,g51).
- Long thinks never fixed anything (g36..g51).
