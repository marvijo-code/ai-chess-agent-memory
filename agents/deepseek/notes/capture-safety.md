# Pre-move scan & blunder catalogue (g1-g114)

## Before every move (final board)
1. Legality: paths clear; two units -> full name; O-O needs f1/g1 empty + knight off home; re-read after captures. A rejection = recheck, never guess (g114 cost 1:12).
2. Knight sweep: his knights' 8 squares on my destination, before any queen move.
3. PAWN first: never a piece where his pawn takes it (g109 13...Nc5? dxc5; g113 14.Nd5?? cxd5; g114 16.Bd5?? exd5).
4. Destination: his LAST move's attacks - rook files, bishop rays incl. parked (g105 Bc6; g108 Qxb7?? Bxb7). Attacked+undefended -> save NOW; re-list guards after ANY trade.
5. Queen: hit -> she moves THAT move; 'defended' never counts. No capture on a defended square or a standing bishop ray. Queen capture: count EVERY defender incl. knights/pawns/x-rays (g110 13...Qxd4??; g114 23.Qxd4?? Qxd4 = Q for P).
6. Queen checks only when his king CANNOT take her (g106).
7. Captures: name every recapturer + his 2nd attacker; write HIS recapture and material (g108 Qxb7 = Q for P; g111 Rxc6?? Rxc6 = R for P).
8. Blocked guard = NO guard (g112 13.Ba3?? Bxa3: a2/b3 blocked both recaptures).
9. Retreat needs a pawn/2nd guard; queen-only guard loses to Qx/Q-trade/Rx; king-only guard = no guard (g110 24...Nc5 -> Rxc5+).
10. Pawn push: write the squares it ABANDONS (g111 21.c4?? left d4).
11. Mate nets: Qh2/Rh1; Qxg2# (g101,g102); Qd1+ Rf1 Qxf1# (g108); Rxf2+Qg2# (g111); Bb7 battery once c6-g2 clear: Qxg2/h1# (g113,g114 27...Qh1#). Scan HIS mates every ply when down.
12. Down: keep queens; repetition; no claw-back grabs or free pieces. Up: no risk (g112 38...Rg2?? Kxg2); escort passers; promote; mate; stalemate-check; 5-10 s.
13. IQP: count attackers vs defenders of d4 before moving a guard (g114 14.Qe2?! left only Nf3 vs Qd8+Bf6+Nc6 -> 14...Nxd4! Bxd4 won a pawn). Equal = hold; routine <=15 s; long thinks never prevented a blunder (g106-g114).

## Patterns
- Queen on attacked square moves THAT move; 'defended' never counts (g41,g94,g95,g100).
- Free gifts: undefended unit or 'trade offer' on an attacked square; anything into his queen's range.
- A check is not safety (g106,g107). Queen-only guard dies to Qx+2nd attacker or a pawn (g103,g107,g109).
- Parked bishop: list its whole ray before ANY piece/queen move (g105,g108,g109,g114).
- SELF-BAN: a move my scan or note called bad is DEAD (g98,g103,g105,g108,g109,g111).
- A piece attacked must flee PAWN-SAFE, not merely 'strong' (g113 14.Nd5?? cxd5; g114 16.Bd5?? exd5).

## Key games
- g114 QGD Bxf6 vs Sol (0-1, Qh1# m27): 14.Qe2?! 14...Nxd4! Bxd4 won a pawn; 16.Bd5?? exd5; 21.Nd6?? Qxd6; 23.Qxd4?? Qxd4 = Q for P; 25...Be5+ 26.f4 Bxf4+ 27.g3 Qh1#. 41 s quiet moves; 11:16 vs 15:10.
- g113 QGD Bxf6 vs SF (0-1, Qxg2# m19): 14.Nd5?? cxd5; 19.Qc7?? while Bb7+Qg5 = Qxg2# (f3 saves). 43 s on the blunder.
- g112 Caro Advance vs Sonnet (1-0 m58): 13...Bxa3! won a piece (a2/b3 blocked recaptures); 38...Rg2?? Kxg2; 4 illegal tries; 1:00 vs 9:08.
- g111/g109: 21.c4?? left d4 -> 22...Rxd4; 26.Rxc6?? Rxc6; 13...Nc5? dxc5; 28...Qd6?? Bxd6.
- g110/g108 (Q for P): 13...Qxd4?? 14.Qxd4; 24...Nc5 king-only guard -> Rxc5+; 23.Qxb7?? Bxb7.
