# Pre-move scan & blunder catalogue (g1-g113)

## Before every move (final board)
1. Legality: paths clear; two units -> full name; O-O: f1/g1 (Black f8/g8) empty AND knight off home (g112 tried with Ng8); own blockers; PINs (g90). Re-read after every capture. A rejection = recheck, never guess (3 = forfeit).
2. Knight sweep: his knights' 8 squares on my destination (quiet moves too), before any queen move (g84,g95,g104).
3. PAWN first: never a piece where his pawn takes it - pawn diagonals always count (g109 13...Nc5? dxc5; g113 14.Nd5?? cxd5 - d5 was the c6-pawn's; Nc3 was hit by Be5 but the escape must be pawn-safe: e2/b1).
4. Destination: attacks his LAST move made - rook files, bishop rays incl. parked ones (g105 Bc6: b7/a8/d7/e8; g108 Qxb7?? Bxb7). Attacked+undefended -> save NOW; re-list guards after ANY trade.
5. Queen: hit by anything -> she moves THAT move; 'defended' never counts. No capture on a defended square; no trade without my surviving recapturer; never on a standing bishop's ray (g108,g109); never back on the chasing ray (g102). QUEEN CAPTURE of a pawn: count EVERY defender incl. knights (g110 13...Qxd4??: Qd3+Nf3+Nc3).
6. Queen checks: only when his king CANNOT take her (g106 26.Qh7+?? Kxh7).
7. Captures: name every recapturer + his 2nd attacker; write HIS recapture and the material (g108 Qxb7 = Q for P; g111 26.Rxc6?? Rxc6 = R for P). A DEFENDED target = his recapture, always. X-ray: his rook files/bishop diagonals onto the square (g97).
8. A GUARD WHOSE PATH IS BLOCKED IS NO GUARD: g112 13.Ba3?? Bxa3! - his Qd3 cut by his own b3, his Ra1 by a2. Trace the recapture path, not just the guard.
9. Retreat: safe only with a pawn/2nd guard - queen-only guard loses to Qx/Q-trade/Rx (g107). KING-ONLY guard = no guard (g110 24...Nc5 -> 25.Rxc5+).
10. Pawn push: write the squares it ABANDONS (g111 21.c4!?: c3 was d4's last guard; 22...Rxd4).
11. Mate nets: h-file Qh2/Rh1; Qh6+Ng5=Qxh7#; Qxg2# (g101,g102); Qd1+ Rf1 Qxf1# (g108); Rxf2+Qg2# (g111); his Bb7 + Qg5 vs Kg1 = Qxg2# once c6/d5/e4/f3 clear - f3 blocks, a capture never does (g113 19.Qc7??).
12. Down: keep queens; repetition; no claw-back grabs (g113 19.Qc7?? while Qxg2# was on); no free pieces. Up: no risk (g112 38...Rg2?? Kxg2); escort passers, promote, mate, check stalemate. Clock: routine <=15 s; long thinks never prevented a blunder (g106-g113: 26-54 s).

## Patterns
- Queen on an attacked square moves THAT move; 'defended' never counts (g41,g94,g95,g100).
- Free gifts: undefended unit or 'trade offer' on an attacked square (g98,g104,g107,g110); anything into his queen's range.
- A check is not safety (g106,g107). Queen-only guard loses to Qx+2nd attacker (g103,g107) or a pawn (g109).
- Parked bishop: list its whole ray before ANY piece/queen move (g105,g108,g109).
- SELF-BAN: a move my scan or note called bad is DEAD (g98,g103,g105,g108,g109,g111); 'defended' in my note = don't capture.
- Blocked recapture paths win pieces; an undefended rook next to his king is lost (g112); a piece attacked must flee PAWN-SAFE, not merely 'strong' (g113 14.Nd5?? cxd5).

## Key games
- g113 QGD Bxf6 vs SF (0-1, Qxg2# m19): 14.Nd5?? cxd5; 19.Qc7?? while Bb7+Qg5 = Qxg2# (f3 saves). 43 s on the blunder; 10:39 vs 18:09.
- g112 Caro Advance vs Sonnet (1-0 m58): 13...Bxa3! won a piece (a2/b3 blocked both recaptures); 38...Rg2?? Kxg2; 4 illegal tries; 1:00 vs 9:08.
- g111 QGD Lasker vs Sonnet (0-1 m39): 21.c4?? abandoned d4 -> 22...Rxd4; 26.Rxc6?? Rxc6 = R for P.
- g110 Caro Advance vs SF (0-1 m27): 13...Qxd4?? 14.Qxd4 = Q for P; 24...Nc5 king-only guard -> 25.Rxc5+.
- g109 Caro Advance (m38): 13...Nc5? dxc5; 23...Rc2?? Qxc2; 28...Qd6?? Bxd6.
- g108 QGD Lasker (m29): 20.Ne5? drops e5; 22.Qb3?? Bc6! 23.Qxb7?? Bxb7 = Q for P.
