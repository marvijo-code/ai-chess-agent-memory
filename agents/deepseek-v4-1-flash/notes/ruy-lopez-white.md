# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5.

## g43 vs Sonnet 5.5 (0-1, mated m34) - queenside expansion went wrong
14...Nb4 15.Bb1 a5 16.a3 Na6 17.b4 axb4 18.axb4 Bd7 19.Ba3?! Nxb4! 20.Bxb4?? Rxa1 21.Bxd6 Bxd6 22.Qa4?? Rxa4 23.Nc4 Rxc4 24.Bd3 Rc3 25.Rd1 h6 26.Ne1 Rc1 27.Rxc1 Qxc1 28.Bxb5 Qxe1+ 29.Kh2 Bxb5 30.Kg3 Qxe4 31.f3 Qxd5 32.f4 exf4+ 33.Kf2 Qd2+ 34.Kf3 Qe2#.
- 18.axb4 OPENED the a-file: Ra1 vs Ra8; Ra1 UNDEFENDED (Bb1 blocks Qd1 and Re1). His a6-knight still blocked the file; 19...Nxb4 vacated a6 and won a pawn. Correct: 20.Rxa8! Rxa8 21.Bxb4 wins his loose knight (net N for P). 19.Ba3?! (SF) let the trick; 20.Bxb4?? ignored 20...Rxa1 (down R for N); 21.Bxd6? Bxd6 gave B for P (his e7-bishop recaptured); 22.Qa4?? stepped onto the a-file rook AND the b5-pawn's square with no defender -> Rxa4 wins the queen.
- Rule: when my pawn capture opens a file, fix the rook on it FIRST (trade Rxa8 or move/defend); then deal with pawn grabs. 28.Bxb5 was B for P again (Bd7 recaptures).
- Clock: 47-63 s every move m14-21 and 82 s on 22.Qa4 (plus illegal Qg4 try - Nf3 blocks d1-g4). Long thinks made it worse; 5 s scan then move. Down R+B no tricks: 23.Nc4?? Rxc4.

## Keep (g10,g13,g18,g21,g22,g23,g33,g37)
- 14...Nb4 -> 15.Bb1! only; 14...Nb8 standard 15.Nf1 Nbd7 16.Be3 ...; 14...Rac8 15.Ne3 Nc4: keep e3 EMPTY (g33: 17.Be3?? Rfe8 18.Qd2?? Bxe4).
- 14...Nd7? (g40): resolve the centre or reroute BEFORE 15.d5; ...g6 vs Nf5/Ng5+Qh5 (22...Qd7?? 23.Qxh7#).
- Bishop: 20.Bxc5 dxc5 fine with the d5 clamp (g37); don't hand over the bishop pair (21.Bxf6?! g13, 21.Bxc5?! g18); never B-for-P.
- After ...g6 no Nf5 (g22); 19.Ng3?? Nb3! (g23). Never a Q on an attacked square (g10,g18,g22,g31,g37: Qc2?? Qd5?? Qd6?? Qxc4?? Qxc3??); every queen capture: list pawns/rooks on the line.

## Rook endings (g27,g31)
- Undefended rook chasing rook loses (Rc2?? Rxc2, Re2?? Rxe2); use a defended rook (Rb1!). Check the destination rank/file for rooks AND knights (Re7?? Nxe7). g43: rooks facing on an open file - fix the loose one at once.

## Game management
- Routine <=15 s; from m10 cap ~25 s. Long thinks didn't prevent the g37/g43 blunders; g43 burned 19 min vs his 5 min (1:26 left).
- Down material: king safety, defend loose pieces, trade, 5-15 s, no pawn grabs, no capture his recapture answers (g43 Bxd6, Bxb5).
