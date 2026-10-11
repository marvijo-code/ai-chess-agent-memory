# Pre-move scan & blunder catalogue (g1-g107)

## Before every move (5 s on the FINAL board)
1. Legality: paths clear; two units -> full name; O-O f1/g1 empty; bishops trace to edge; own blockers; PINs (g90); re-read after every capture.
2. Knight sweep first: his knights' 8 squares on my destination (quiet moves too), especially before any queen move (g84,g95; g104 20.Nh5?? Nxh5).
3. Destination: attackers his LAST move made - pawn diagonals (even blocked), rook files, bishop rays incl. parked ones (g105 Bc6: b7/a8/d7/e8). Attacked+undefended -> save NOW; re-list guards after trades.
4. Queen: hit by anything -> she moves THAT move; 'defended' never counts (g41,g94,g95,g100). No capture on a defended square; no trade without my surviving recapturer; never on a bishop's ray (g105 Qd7??); never back onto the ray that chased her (g100,g102).
5. Queen checks: only when his king CANNOT take her (g106 26.Qh7+?? Kxh7). A check is not safety.
6. Captures: name every recapturer + his 2nd attacker; write HIS recapture and the material (g102 21.Nxc6??; g103 12...Bd6??). PIN = recapturer cannot move (g90). X-ray: walk his rook files/bishop diagonals onto the square (g97).
7. Retreat: an attacked piece's new square is safe only with a pawn/2nd guard - queen-only guard loses to Qx, Q-trade, Rx (g107 15...Nd7?? 16.Qxd7 Qxd7 17.Rxd7).
8. Mate nets first: Qh2/Rh1 h-file; Qh6+Ng5=Qxh7#; K h2-h4: Rg2/Rg6+Bf1+Nf2 (g98); Qxg2# (g101,g102).
9. Down: keep queens; repetition; no bad trades; no free pieces (g107 19...Rd1+?? Rxd1).
10. Clock: routine <=15 s; long thinks never prevented a blunder (g106 33-45 s, g107 36-43 s on book; 7:37/9:29 left vs 14:20/15:39).

## Patterns
- Attacked queen moves that move; 'defended' never counts.
- Free gifts: undefended unit or 'trade offer' on an attacked square (g78,g98,g104,g105,g107).
- A check is not safety (g106,g107).
- Queen-only guard loses to Qx + 2nd attacker (g103,g107).
- Parked bishop: list its whole ray before ANY piece/queen move (g105).
- Last-screen grabs g81,g83,g91; tempo on queen g41,g98.
- SELF-BAN: a move my scan or note called bad is DEAD (g98,g103,g104,g105).

## Key games
- g107 Caro Classical vs Sol (0-1 m29): equal till 15.dxe5; 15...Nd7?? had only Qd8's guard -> 16.Qxd7 Qxd7 17.Rxd7 = knight for nothing. ...Nd5 (c6-pawn) or ...Ne8 was fine.
- g105 Open Chigorin vs SF (0-1 m36): after ...b5 the c6-knight has NO pawn recapture; 9.Bd5! -> only ...Nxd5 =; 9...O-O?? drops a piece; 10...Bb7??/12...Qd7?? on the c6-bishop's rays.
- g106 QGD Lasker vs Sonnet (0-1 m31): equal till 25...Rd5; 26.Qh7+?? Kxh7 = Q for nothing.
