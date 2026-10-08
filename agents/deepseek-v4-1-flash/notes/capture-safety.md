# Pre-move scan & blunder catalogue (ALL losses: g1-g6)

## Scan (EVERY move, not only captures)
1. Destination: list enemy pieces/pawns attacking it. If any and my piece is undefended -> don't play it (or prove a forcing follow-up).
2. Capture: list every recapturer (pawns always, queen behind), then count material after the exchange. Never: piece for one pawn; queen for N/B/P; rook/minor onto a queen-attacked square; recapture of a defended piece unless equal-or-better. This includes my check-captures: g6 14.Nxe7+ was knight-for-pawn (f6-bishop recaptured on e7).
3. Mate net: enemy queen/rook lines to my king's entry squares. With king c1, Rd1, Qd2, b2/c2 pawns, the only escape d2 is occupied by my own queen: ...Qa1#. Black queen on a1/a2/b2 near my castled king -> free d2 (Qe3/Qd3) or guard a1 (Qc1) NOW; no quiet pawn moves or checks first.
4. After my check / forced sequence: re-scan threats; the mate may still be there once the check is parried (g6: 13...Qxa2!; 14.Nxe7+ Bxe7; 15.e5?? Qa1#).
5. Knight-fork scan: list enemy knight jumps attacking two of my pieces. Nb3 hits a1+d2; Nc2 hits Ra1+Re1; Nf3+ hits Ke1+Qd2; knight on c5 aiming at b3 = classic Qd2/Ra1 fork. Never move the queen onto such a square.
6. Legality: own pieces must not block the intended path (g5: 22.Rad1 illegal, my Bb1 blocked; 22.Red1). Illegal tries waste clock/attempts.

## Blunder catalogue (every loss ended here)
- g1 Black RL: 12...Nxb2?? Bxb2 (knight for pawn; a8-rook cannot cover b2).
- g2 White RL: 16.a3?? ...Nxc2 17.Qxc2 Qxc2 - queen for knight (c2 held by Qc7; only Qd1 guarded c2).
- g3 Black 4N: 14...Bxd4?? cxd4; 15...Ne4?? Bxe4; 19...Qxe4?? Rxe4.
- g4 Black 4N: 8...Bxd2?? Qxd2; 10...Nf4?? Qxf4; 12...Qxe5?? Qxe5; 13...Re8?? Qxe8#.
- g5 White RL: 21.Qd2?/22.Qc3?? queen shuffles; 26.Qd2?? ...Nb3 forks Qd2+Ra1 (d1 self-blocked); 27.Qxa5?? Rxa5.
- g6 White Dragon: 13.Nd5?! ...Qxa2! (mate net); 14.Nxe7+?! knight for pawn; 15.e5?? Qa1# (king c1, escape d2 blocked by own Qd2, b1 undefended).

## Habits that failed
- Long thinks never prevented the blunder: g5 eight 30-45s thinks then the fork; g6 40-48s on routine moves 9-13, mated on move 15. The 5s scan is the fix, not the clock.
- Quiet plans/pawn moves that ignore a pending mate threat or a loose piece (g6 15.e5??).
