# Pre-move scan & blunder catalogue (ALL losses: g1-g7)

## Scan (EVERY move, not only captures)
1. Destination: list enemy pieces/PAWNS attacking it. If any and my piece is undefended -> don't play it. Pawn magnets: e5 pawn hits d6/f6; d5 pawn hits c6/e6. With a White pawn on e5, a knight on f6/d6 hangs (g7 22...Nf6?? then 24...Nf6?? 25.exf6).
2. Capture/pawn grab: list every recapturer/defender of the TARGET SQUARE (pawns always, queen/rook behind), then count material after the exchange. Never: piece for one pawn; queen for N/B/P; rook/minor onto an enemy-attacked square. b2/c2 grabs are a chronic killer: g1 12...Nxb2?? Bxb2; g2 16.a3?? ...Nxc2; g7 35...Rxb2?? Rxb2 (b2 defended by the rook just placed on b4). Only grab a pawn if NO enemy piece attacks that square. This includes my check-captures: g6 14.Nxe7+ was knight-for-pawn (f6-bishop recaptured on e7).
3. Mate net: enemy queen/rook lines to my king's entry squares. With king c1, Rd1, Qd2, b2/c2 pawns, the only escape d2 is occupied by my own queen: ...Qa1#. Black queen on a1/a2/b2 near my castled king -> free d2 (Qe3/Qd3) or guard a1 (Qc1) NOW; no quiet pawn moves or checks first.
4. After my check / forced sequence: re-scan threats; the mate may still be there once the check is parried (g6: 13...Qxa2!; 14.Nxe7+ Bxe7; 15.e5?? Qa1#).
5. Knight-fork scan: list enemy knight jumps attacking two of my pieces. Nb3 hits a1+d2; Nc2 hits Ra1+Re1; Nf3+ hits Ke1+Qd2; knight on c5 aiming at b3 = classic Qd2/Ra1 fork. Never move the queen onto such a square.
6. Legality: own pieces must not block the intended path (g5: 22.Rad1 illegal, my Bb1 blocked; 22.Red1). Before any capture the target must hold an ENEMY piece and my piece must travel a clear rank/file/diagonal (g7: illegal tries Bxd5 - my own knight was on d5; Qxf6 - c7 to f6 is not a queen line). Illegal tries waste clock and show tangled visualization: count plies/pieces before attempting.

## Blunder catalogue (every loss ended here)
- g1 Black RL: 12...Nxb2?? Bxb2 (knight for pawn; a8-rook cannot cover b2).
- g2 White RL: 16.a3?? ...Nxc2 17.Qxc2 Qxc2 - queen for knight.
- g3 Black 4N: 14...Bxd4?? cxd4; 15...Ne4?? Bxe4; 19...Qxe4?? Rxe4.
- g4 Black 4N: 8...Bxd2?? Qxd2; 10...Nf4?? Qxf4; 12...Qxe5?? Qxe5; 13...Re8?? Qxe8#.
- g5 White RL: 21.Qd2?/22.Qc3?? queen shuffles; 26.Qd2?? ...Nb3 forks Qd2+Ra1 (d1 self-blocked); 27.Qxa5?? Rxa5.
- g6 White Dragon: 13.Nd5?! ...Qxa2! (mate net); 14.Nxe7+?! knight for pawn; 15.e5?? Qa1# (king c1, escape d2 blocked, b1 undefended).
- g7 Black RL: 22...Nf6?? and 24...Nf6?? (25.exf6, knight for free - pawn on e5 hits f6); 29...Qb6??; 35...Rxb2?? Rxb2 - rook for pawn, the final killer in a holdable R+5P vs R+4P ending.

## Sibling pattern - the f6 square in closed games
- With a White pawn on e5 (or able to reach e5), Black's Nf6/d6 is poison: e5xf6 wins it. g7: after 23.dxe5 the e5 pawn made 24...Nf6?? lose a piece. Keep the knight on d5/c5/e7 instead; it was safe on d5 because Bb7 recaptured.
- My own Nf6 also grabbed in Four Knights lines when the e5 pawn advanced - always check the pawn in front.

## Habits that failed
- Long thinks never prevented the blunder: g5 eight 30-45s thinks then the fork; g6 40-48s on routine moves 9-13, mated 15; g7 40-50s on moves 14-24 then 24...Nf6??. The 5s scan is the fix, not the clock.
- Quiet plans/pawn moves that ignore a pending mate threat, a loose piece, or a defended pawn (g6 15.e5??, g7 35...Rxb2??).
