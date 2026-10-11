# Pre-move scan & blunder catalogue (g1-g111)

## Before every move (final board)
1. Legality: paths clear; two units -> full name; O-O f1/g1 (Black f8/g8) empty; bishops trace to edge; own blockers; PINs (g90); re-read after every capture.
2. Knight sweep: his knights' 8 squares on my destination (quiet moves too), before any queen move (g84,g95,g104).
3. Destination: attacks his LAST move made - pawn diagonals (even blocked), rook files, bishop rays incl. parked ones (g105 Bc6: b7/a8/d7/e8; g108 Qxb7?? Bxb7). Attacked+undefended -> save NOW. PAWN first: never a piece where his pawn takes it (g109 13...Nc5? dxc5).
4. Queen: hit by anything -> she moves THAT move; 'defended' never counts. No capture on a defended square; no trade without my surviving recapturer; never on a standing bishop's ray (g105,g108,g109); not back on the ray that chased her (g102). QUEEN CAPTURE of a pawn: count EVERY defender incl. knights (g110 13...Qxd4?? 14.Qxd4: guards Qd3+Nf3+Nc3, listed two = Q for P).
5. Queen checks: only when his king CANNOT take her (g106 26.Qh7+?? Kxh7).
6. Captures: name every recapturer + his 2nd attacker; write HIS recapture and the material (g108 Qxb7 = Q for P; g111 26.Rxc6?? Rxc6 = R for P - his c4-rook down the open file, and my note had said 'his rook defends c6'). A DEFENDED target = his recapture, always. PIN = recapturer cannot move (g90). X-ray: his rook files/bishop diagonals onto the square (g97).
7. Retreat: safe only with a pawn/2nd guard - queen-only guard loses to Qx, Q-trade, Rx (g107). KING-ONLY guard = no guard (g110 24...Nc5 -> 25.Rxc5+).
8. Pawn push: write the squares it ABANDONS (g111 21.c4!? left d4 - c3 guarded it; 22...Rxd4).
9. Mate nets: Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; K h2-h4: Rg2/Rg6+Bf1+Nf2 (g98); Qxg2# (g101,g102); Qd1+ Rf1 Qxf1# (g108); Kh4 vs Rg5: Qg2+/Qg4# (g111).
10. Down: keep queens; repetition; no bad trades; no free pieces (g107 19...Rd1+?? Rxd1). Clock: routine <=15 s; long thinks never prevented a blunder (g106-g111: 36-48 s).

## Patterns
- Queen on an attacked square moves THAT move; 'defended' never counts (g41,g94,g95,g100).
- Free gifts: undefended unit or 'trade offer' on an attacked square (g98,g104,g107,g110); anything into his queen's range.
- A check is not safety (g106,g107). Queen-only guard loses to Qx+2nd attacker (g103,g107) or a pawn (g109).
- Parked bishop: list its whole ray before ANY piece/queen move (g105,g108,g109).
- SELF-BAN: a move my scan or note called bad is DEAD (g98,g103,g105,g108,g109,g111); 'defended' in my note = don't capture. A pawn push abandons the guards it left.

## Key games
- g111 QGD Lasker vs Sonnet (0-1 m39): 21.c4!? abandoned d4 -> 22...Rxd4; 26.Rxc6?? Rxc6 = R for P (c4-rook, open c-file). Clock 8:53 vs 14:24.
- g110 Caro Advance vs SF (0-1 m27): 13...Qxd4?? 14.Qxd4 = Q for P (guards Qd3+Nf3+Nc3); 24...Nc5 blocked a check with king-only guard -> 25.Rxc5+.
- g109 Caro Advance (m38): 13...Nc5? dxc5; 23...Rc2?? Qxc2; 28...Qd6?? Bxd6.
- g108 QGD Lasker (m29): 20.Ne5? drops e5; 22.Qb3?? Bc6! 23.Qxb7?? Bxb7 = Q for P.
- g107 Caro Classical (m29): 15...Nd7?? only Qd8 guarded -> 16.Qxd7 Qxd7 17.Rxd7.
- g106 QGD Lasker (m31): 26.Qh7+?? Kxh7 = Q for nothing.
- g105 Open Chigorin (m36): after ...b5 the c6-knight has NO pawn recapture; 9.Bd5! -> 9...Nxd5 = only; 10...Bb7??/12...Qd7?? on the c6-bishop's rays.
