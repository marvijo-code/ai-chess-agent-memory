# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 -> 14.d5 / 14.dxe5 / 14.Nf1.

## g61 vs Sol (0-1, Rxc1# m35) - b4 opens the a-file; queen in front of his rook
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Na6 18.Be3 Nc5 19.Qd2 Rfe8 20.Qe2 a4 21.b4? axb3! e.p. 22.axb3?! Rxa1 23.Qb2 Raa8 24.Qa3?? Rxa3 25.Nxe5?? dxe5 26.Bxc5 Bxc5 27.Bd3 Rxb3 28.Bc4 bxc4 29.Ne2 Qb6 30.Rc1 Bxf2+ 31.Kh2 Bg3+ 32.Nxg3 Qe3 33.Rxc4 Qxg3+ 34.Kg1 Rb1+ 35.Rc1 Rxc1#.
- Through 20...a4 equal (SF: 7.Bb3!, 13.cxd4! good; Sol: ...Rfe8, ...a4).
- 21.b4?: ...axb3 e.p. opened the a-file and Rxa1 won a rook - my own Bb1 blocked Re1. Recapture 22.Nxb3! (knight covers a1, so Rxa1 Nxa1 is only a rook trade). Before a pawn push/capture that opens a file: who enters first, can I recapture?
- 24.Qa3?? Rxa3: queen onto the open a-file facing his rook = he captures first. Same class as g56 19.Qd6??, g42 17.Qxd5?? Rxd5, and the g58/g60 pawn takes.
- 25.Nxe5?? dxe5: desperate grab, no follow-up (g60 same). Down material: defend, play fast, no grabs.
- 29...Qb6 (Q+B battery on f2): 30...Bxf2+ 31.Kh2 Bg3+ 32.Nxg3 Qe3! 33...Qxg3+ 34.Kg1 Rb1+ 35.Rc1 Rxc1# - rank-1 mate; his Qg3 covers f2/g2/h2, the rook covers f1/h1 along the rank. Guard f2 with a piece or block the c5-bishop diagonal; do not play a side move.
- Clock: 40-92 s on routine m14-33, 92 s on the rejected Qd2 (queen already on that square); ended 6:02 vs 14:20. The 5 s destination scan is the fix.

## g60 vs Sonnet (0-1, Qxg1# m30) - queen onto a pawn-attacked square
14.d5 Nb4 15.Bb1 a5 16.Nb3 a4 17.Nbd2 Bd7 18.Nxe5?? dxe5 19.d6 Bxd6 20.Nf3 Rac8 21.Qxa4?? bxa4 22.Be3 Nc2 23.Bxc2 Qxc2 24.Nd4 exd4 25.Bxd4 Nxe4 26.Be3 Qxb2 27.f3 Nc3 28.Re2 Nxe2+ 29.Kh1 Qxa1+ 30.Bg1 Qxg1#.
- Normal to 17...Bd7; 18.Nxe5?? (e5 had TWO guards, and the planned 19.d6 had no defender - Nd2 blocked Qd1) and 21.Qxa4?? bxa4 = Q for P. Sonnet took bxa4, Nc2, Nxe4, Qxb2.

## g57 vs Sol (0-1, Qxg2# m28) - stale plan; queen with no recapturer
14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Be3 Bd7 19.Ng3 Rac8 20.Nf5 Bxf5 21.exf5 Rfe8 22.Bxc5 Qxc5 23.Nd4?? exd4 24.Qxd4?? Qxd4 25.Bc2 Rxc2 26.Rxe7 Rxe7 27.Rc1 Qxf2+ 28.Kh1 Qxg2#.
- 23.Nd4?? used a plan from before 22.Bxc5 - after ANY trade rewrite the tactics on the current board. 24.Qxd4?? with no recapturer. Qxf2+/Qxg2# with his Rc2 guarding f2/g2 along rank 2.

## Working
- 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; ...a5-a4: step the b3-knight away (Nbd2); do not answer ...a4 with b4 unless 22.Nxb3 is the recapture (g61).
- Keep Nd2 guarded, e3 empty for Be3, no Nc4 while b5 hits c4, no Nxe5 grabs (g60,g61).
- No queen on flank squares touching pawns or on an open line facing his rook.

## Older - condensed
- g52 (draw): Re2/Nf1 defend c2/d2; K+2P vs K+2B+N never resign, 1-3 s; Sonnet failed to mate ~19 moves.
- g51: 24.Qxd5?? Qxd5; 25.Rxe5?? dxe5. g48/g46: never send a move my own reasoning rejected; rook entering an open file facing my queen -> queen leaves THAT move.
- Keep: never B-for-P; no undefended rook chasing a rook; down material defend/trade 5-15 s; vs ...Nd7 resolve the centre BEFORE 15.d5; vs Nf5/Ng5+Qh5 play ...g6.
