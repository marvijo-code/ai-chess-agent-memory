# Ruy Lopez Closed - Black (Chigorin/Breyer)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 (also 9.d4 exd4 10.cxd4).

## Setup
...a6, ...Nf6, ...Be7, ...b5, ...d6, ...O-O. Then:
- Chigorin: ...Na5 (hits Bb3), ...c5, ...Qc7, ...Nc6, ...Bb7, ...Rac8, ...Rfe8, knight tours to c4/b4.
- Breyer: ...Nb8/...Nd7, ...Re8, ...Bf8.
- ...Bg4 pin is fine; after h3 Bh5, keep or trade the bishop at the right moment.

## Key plans
- Central break ...c5 hits d4; after dxc5 dxc5 queens may trade on d8 and ...Rfxd8 recaptures.
- Na5-c4 attacks e3/d2; if White answers Bc1 the knight has no targets, so play ...c5/...Re8 or ...Bg6 and keep moving fast.
- TRAP: with knight on c4 and Bc1 guarding b2, ...Nxb2?? just loses a knight: the a8-rook cannot recapture b2 in one move. Only play ...Nxb2 if a rook already covers b2.
- Do not take defended pieces with rooks: 18...Rxd2 (knight defended by Nf3, no pin) lost the exchange in game 1.
- Keep f7 covered; White aims Bd3/Bd5 to hit a8/f7 and force good exchanges.
- If White is up material he will trade queens on d8; do not enter lost endings.

## g7 vs Sonnet 5.5 (0-1, mated move 53) - same line, slow White plan
Move order: 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 (not 14.d5) Bb7 15.Be3 Rac8 16.Nbd2 Rfe8 17.Bb1 Na5 18.Nb3 Nxb3 19.Qxb3 Bf8 20.Bd3 Nd7 21.Rad1 d5 22.exd5 Nf6?? 23.dxe5 Nxd5 24.Bd4 Nf6?? 25.exf6 gxf6 26.Bxf6 Bxf3 27.gxf3 Bc5 28.Rxe8+ Rxe8 29.Qd5 Qb6?? 30.Bd4 Bxd4 31.Qxd4 Qxd4! 32.Bxh7+! Kxh7 33.Rxd4 Re1+ 34.Kg2 Re2 35.Rb4 Rxb2?? 36.Rxb2 Kg6 ... 53.Rh6#.
- Through move 21 the Chigorin setup was balanced; engine ?! only on ...Rfe8/...Na5/...Bf8/...Nd7.
- THE blunder: 22...Nf6?? then 24...Nf6?? - with a White pawn on e5 (from dxe5) the f6 square is poison; 25.exf6 won the knight. The d5-knight was immune (Qxd5?? Bxd5 = Q for N), so leave it there or use ...Nb4/...Nb6/...exd4.
- 29...Qb6?? (engine pref: keep the pieces coordinated / hit the queen safely); 31...Qxd4! was correct, but White escaped via the discovered 32.Bxh7+! Kxh7 33.Rxd4, leaving R+5P vs R+4P - holdable.
- In that R ending down one pawn: keep the rook, defend b2/b5, avoid pawn grabs. 35...Rxb2?? Rxb2 lost the rook for a pawn (b2 was defended by the R that had just gone to b4). Then trivial conversion.
- Clock: spent 40-50s per move on 14-24 and ended 3:19 vs 11:34. Cut routine middlegame moves to <=15-20s.

## Game 1 note
12...Na5 13.Bc2 Nc4 14.Bc1: play ...c5 or ...Bg6; 14...Nxb2?? 15.Bxb2 was the losing blunder (down a piece for a pawn; later flagged at move 32).
