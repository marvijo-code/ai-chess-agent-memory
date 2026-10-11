# Pre-move scan & blunder catalogue (g1-g109)

## Before every move (5 s on the FINAL board)
1. Legality: paths clear; two units -> full name; O-O f1/g1 (Black f8/g8) empty; bishops trace to edge; own blockers; PINs (g90); re-read after every capture.
2. Knight sweep first: his knights' 8 squares on my destination (quiet moves too), especially before any queen move (g84,g95; g104 20.Nh5?? Nxh5).
3. Destination: attacks his LAST move made - pawn diagonals (even blocked), rook files, bishop rays incl. parked ones (g105 Bc6: b7/a8/d7/e8; g108 23.Qxb7?? Bxb7). Attacked+undefended -> save NOW; re-list guards after trades. PAWN first: never a piece on a square his pawn takes (g109 13...Nc5? dxc5, 16...Bf6? exf6 - e5-pawn owns d6/f6).
4. Queen: hit by anything -> she moves THAT move; 'defended' never counts (g41,g94,g95,g100). No capture on a defended square; no trade without my surviving recapturer; never on a bishop's ray (g105 Qd7??; g108 Qxb7??; g109 28...Qd6?? Bxd6); never back onto the ray that chased her (g100,g102).
5. Queen checks: only when his king CANNOT take her (g106 26.Qh7+?? Kxh7). A check is not safety.
6. Captures: name every recapturer + his 2nd attacker; write HIS recapture and the material (g102 21.Nxc6??; g103 12...Bd6??; g108 Qxb7 'wins a pawn' = Q for P; g109 13...Nc5 'queen defends' = N for P). PIN = recapturer cannot move (g90). X-ray: walk his rook files/bishop diagonals onto the square (g97).
7. Retreat: an attacked piece's new square is safe only with a pawn/2nd guard - queen-only guard loses to Qx, Q-trade, Rx (g107 15...Nd7?? 16.Qxd7 Qxd7 17.Rxd7).
8. Mate nets first: Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; K h2-h4: Rg2/Rg6+Bf1+Nf2 (g98); Qxg2# (g101,g102); K boxed by g2/h2: Qd1+ Rf1 Qxf1# (g108).
9. Down: keep queens; repetition; no bad trades; no free pieces (g107 19...Rd1+?? Rxd1).
10. Clock: routine <=15 s; long thinks never prevented a blunder (g106 33-45 s, g107 36-43, g108 41-47, g109 30-40 - ended 5:06 vs 21:19; down = 5-15 s).

## Patterns
- Attacked queen moves that move; 'defended' never counts.
- Free gifts: undefended unit or 'trade offer' on an attacked square (g78,g98,g104,g105,g107); undefended into his queen's range (g109 23...Rc2?? Qxc2).
- A check is not safety (g106,g107).
- Queen-only guard loses to Qx + 2nd attacker (g103,g107) or to a pawn (g109).
- PAWN-ATTACKED squares: g109 13...Nc5? dxc5, 16...Bf6? exf6; a queen's 'defense' does not stop a pawn capture.
- Parked bishop: list its whole ray before ANY piece/queen move (g105,g108,g109).
- Last-screen grabs g81,g83,g91; tempo on queen g41,g98.
- SELF-BAN: a move my scan or note called bad is DEAD (g98,g103,g104,g105,g108; g109 - my note named Bf4's e5-d6 ray and I played Qd6 anyway).

## Key games
- g109 Caro Advance vs SF (0-1 m38): 13...Nc5? dxc5 (pawn-attacked, queen-only guard = N for P), 16...Bf6? exf6 (B for P), 23...Rc2?? Qxc2 (R for nothing), 28...Qd6?? Bxd6 (queen on Bf4's e5-d6 ray, named in my own note a move earlier). Four gifts, all caught by Rule 1/2.
- g108 QGD Lasker vs Sonnet (0-1, m29): 20.Ne5? Nxe5 21.dxe5 Qxe5 = pawn down; then 22.Qb3?? Bc6! (guards b7) 23.Qxb7?? Bxb7 = QUEEN for a pawn. Never put the queen on b7/d7/a8 while a bishop on c6 stands (2nd time after g105).
- g107 Caro Classical vs Sol (0-1 m29): equal till 15.dxe5; 15...Nd7?? had only Qd8's guard -> 16.Qxd7 Qxd7 17.Rxd7 = knight for nothing. ...Nd5 (c6-pawn) or ...Ne8 was fine.
- g105 Open Chigorin vs SF (0-1 m36): after ...b5 the c6-knight has NO pawn recapture; 9.Bd5! -> only ...Nxd5 =; 9...O-O?? drops a piece; 10...Bb7??/12...Qd7?? on the c6-bishop's rays.
- g106 QGD Lasker vs Sonnet (0-1 m31): equal till 25...Rd5; 26.Qh7+?? Kxh7 = Q for nothing.
