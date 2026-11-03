# Ruy Lopez as White

## T80R3 v Sonnet (0-1 forfeit m51) - 5.d3 line
- 5.d3 Ruy: c3/Be7/O-O/Nbd2 then Re1/Bc2/Nf1-g3/d4. Level to m30.
- His plan: ...Na5, ...c5, ...Bb7, ...Re8, ...Qc7, ...Nfg4 hitting Be3; after ...dxe4 never take with queen (Qb7 covers e4).
- I played d4/exd4/cxd4, then ...Nb4/a3/Nxc2/Qxc2, ...c5/...c4, e5/dxe5/dxe5, ...Nd5, b3/...c3. The c3 pawn became a blockader; my knights shuffled Nf5/Nd4/Nd6/Nf5 while his queen and rooks squeezed. I had chances but no clear plan.
- CLOCK: 11:47 on 45.Kh2 (3 invalid), 5:18 on 38.e6, 5:37 on 40.Nexc6, 3:19 on 32.Bc5. Finished 3:32 v 41:06. 9 invalid tries total.
- FORFEIT: after ...Rb2 hit b3, my tool flagged the pawn loss; I tried 3 invalid replies and forfeited. A pawn-loss flag is not a search: send the least-bad DIFFERENT legal move in ONE try (Rc2/Rb1/king move), accept the pawn.
- Lesson: in a level Ruy, 5-15 s keepers; no 3-11 min thinks on quiet king/pawn moves. Name ONE target (c5/d6 or kingside f5) and play it.

## T78R1 v Sonnet (0-1, forfeit m33) - the 5.d3 line
- 5.d3 Ruy: c3/Be7/O-O/Nbd2 then Re1/Bc2/Nf1-g3/d4. Opening level to move 30. His plan: ...Na5/...c5/...Bb7/...Re8/...Qd7/...Rac8/...Ne5/...Nfg4 hitting Be3.
- The d4 break and Ndf5/Be3 were fine; a4/bxa4/Bxa4 won a tempo on Qd7 (best move of the game), he answered ...Bc6/Bxc6/Nxc6 and a6 stayed covered.
- What went wrong: Nh4/Nhf5 was kicked by ...g6/...h5; then Nd4-Nf3-Nd4-Nf3 for five moves with no target; Nf3? let ...Nxf3+ wreck f2/g2; ...d5! and Qd4?? (1:15 think, the only ?? move) met ...dxe4 - the d-file opened onto my queen and Qb7 covered e4. Every reply I tried was refused and I forfeited.
- RULES: with queens on, d4 in front of his Rd8 and on his Qb7 diagonal (b7-c6-d5-e4) is a trap. Never take on e4 with the queen there. A knight needs a target square; otherwise play a rook/pawn plan.

## T77R5 v Sonnet (0-1, Qh2# m59) - a queen trade lost the exchange
- 30.Qd3? ...Bb5!; 31.Qc3 Qxc3 32.Nxc3?? Bxf1: Ne2 had screened b5-f1. Before a queen trade name the ray my recapturer blocks from its OLD square.
- Sonnet vs Be3+Qd2: ...Re8, ...Bf8, ...Qe5/...Qh5, ...Bf5 kicked my e4-knight every time.
- Ra3 pinning Bc3: the pinned bishop, guarded only by Ne2, fell (40.Ng3 Bxc3).
- 12 invalid tries, all on forced moves: one UCI in 5-10 s, a refusal means a different legal move at once.

## T76R2 v Sonnet (0-1 m56) - Closed Chigorin
- 20.b4?! axb4 21.Bd2 bxa3 lost a pawn; b4 only when b5 falls and the a-file is safe.
- King moves drop guards (29.Kh2?! f2; 54.Kf1 e3): name what the king guarded before stepping.

## T76R7 v Muse (1-0, forfeit m43) - 5.Nc3
- 11.Nxf6+ traded Nd5 for Bf6 and freed ...c5/...b4; keep Nd5.
- 15.Bc3?? after ...c5 allowed ...b4; 23.f3?? does not stop ...Ne5 hitting c4.

## T71R3 v GLM (draw, threefold)
- Put Rb1 under b2 before the queen leaves rank 2; all pawns on one wing: keep queens, Rb1-b6/c4-c5/f4-g4.

## Other book shapes
- Classical 5...Bc5: c3, O-O, Re1, h3, d4; after exd4 cxd4 the bishop goes b6 and the knight c3, then Bg5/Nd5.
- Closed Chigorin 5...Be7: h3/Bc2 vs ...Na5, d4, Nbd2/Nf1-g3; keep Kg1 on f2 until queens off; never b4 while b5 stands.
- 5.Nc3: d3/Be3/Re1/Qd2, d4 exd4 Nxd4, keep Nd5/Nf5.

## Recurring
- QUEEN FOR A PAWN: she stood on an enemy pawn capture square (7 games). List pawn squares first.
- No piece where his g6-pawn covers it (f5/h5); no check he can take.
- Long thinks in this line produce illegal tries; routine <=15 s.
