# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb4 (15.Bb1 or 16.Rac1).

## What works (games 2, 5, g9)
- 11.d4, 13.cxd4, 14.d5 (! in two games), 15.Bb1 (!) are all good; main line after 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Bd7 18.Ng3 Nc5 is fine.
- 16.a3 is safe only when BOTH Qd1 and Bb1 cover c2; otherwise 16.Rac1/Bb1 (g2 16.a3?? ...Nxc2 lost the queen for a knight).

## The open c-file - both colors
- After 13.cxd4 the c-file is wide open and Black's Qc7 sits behind it: anything landing on c3/c2 is defended down the file.
- g9: 21.b4? Na4! (a5-pawn supports a4; knight then reaches c3, covered by Qc7) 22...Nc3 hit Bb1/e4.
- g9 blunder: 23.Qxc3?? Qxc3 (queen for knight); then 24.Rc1?? Qxc1+ took the e1-rook and a1-rook was blocked by my own Bb1. Do NOT capture a knight the queen behind it defends; handle the attacked piece instead (e.g. 23.Bd3) and keep queen/rook off the c-file.
- Before any capture on c3/c2/c1: check Qc7.

## The 15...Nb4 moment (game 2)
- 16.a3?? (losing): 16...Nxc2 forks Ra1 and Re1; Qc7 protects c2; 17.Qxc2 Qxc2 = queen for knight.
- Safe: 16.Rac1 (covers c2) or 16.Bb1. 16.Bd3 hangs to Nxd3.

## Game 5 vs Sol
- 20.Bh4?!, 21.Qd2?, 22.Qc3?? were slow; after ...Rfe8 play Red1/Rd1 at once, queen e2/e3, plan f4.
- 22.Rad1 illegal (own Bb1 blocked the a1-rook); check each rook's path with two rooks.
- 26.Qd2?? ...Nb3! fork (d1 occupied by my own rook) and 27.Qxa5?? Rxa5: never queen on d2 with a Black knight that can reach b3.

## Game management
- g2: after 17...Qxc2 the game was over; still 30-55s/move to move 23.
- g5, g9: many 30-50s thinks on routine development, then a blunder. Routine <=15s; the 5s scan is the fix.
