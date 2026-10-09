# Ruy Lopez Closed - Black (Chigorin/Breyer)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3.

## Setup
...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then:
- Chigorin: ...Na5 (hits Bb3), ...c5, ...Qc7, ...Nc6/...Nb7, ...Bb7/...Bd7, ...Rac8/...Rfe8.
- Breyer: ...Nb8/...Nbd7, ...Re8, ...Bf8, ...g6.
- After 9.h3 the ...Bg4 pin is off.

## Plans/traps
- ...c5 hits d4; dxc5 dxc5 may trade queens on d8.
- Na5-c4 hits e3/d2; with Bc1 it has no target -> ...c5/...Bg6. ...Nc4 only when White cannot play b3; ...Nxb2?? with Bc1 loses a knight (a8-rook cannot recapture).
- Keep f7 covered (Bd3/Bd5 aim at a8/f7). White up material trades queens: avoid lost endings.
- NEVER move a piece to a square a White knight attacks, even as a trade (g8 20...Bf5?? Nxf5).
- White's d5 break: a knight on c6 is hit -> ...Ne7/...Nb8 or pre-move the knight.
- Qc7 on the c-file: once White has Be3 (guards c1+d2) and can play Rc1, Qc7 is a tempo target; a 'defended' queen (Rc8 behind) is still lost to Rxc7/Qxc7 = R for Q. RETREAT ...Qb8/...Qd8/...Qb6; never grab a defended rook on c1 (g35).

## g35 vs GPT-6.1 Sol (0-1, mated m29) - Chigorin
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Bd7 14.Nf1 Rac8 15.Ng3 Rfe8?! 16.Bd3 h6 17.Be3 Nb7 18.Rc1! Qxc1?? 19.Bxc1 Rxc1 20.Qxc1 Nc5 21.dxc5 dxc5 22.Nxe5 Nxe4 23.Nxe4 Bg5 24.Nxg5 hxg5 25.Nxd7 Re7 26.Rxe7 g6 27.Re8+ Kg7 28.Qc3+ Kh7 29.Rh8#.
- Through 17...Nb7 this was a normal, solid Chigorin; Stockfish flags 15...Rfe8?? (prefer ...Nb7/...Rcd8/...Bf8) and 18...Qxc1??. Clock 68s on move 18 and it still blundered: long thinks don't help.
- 18.Rc1 attacks Qc7 up the c-file (c2-c6 empty). c1 is DEFENDED by Be3 (e3-d2-c1) and Qd1. The queen must retreat; Qxc1 = Q for R (then ...Rxc1 Qxc1 gives Q+R for R+B: -6 net).
- Root error: I counted only my own ...Rxc1 recapture and missed White's Bxc1 taking the queen. Before ANY capture (especially a queen capture) list ALL enemy recapturers of the DESTINATION, including bishops on diagonals.
- After the blunder: no counterplay existed; down material play 5-15s and defend.

## Older games - condensed
- g19 Chigorin (0-1 m34): 16...a5?! / 17...b4?! weakened my queenside; 18.d5 hit Nc6 and 18...Nd7?! moved the wrong knight (19.dxc6 won it). 28...Qxd5?? Bxd5 = Q for B. 33...Rc8?? Qxc8# (king h8, pawns f7/g7/h7, no luft).
- g15 Breyer (0-1 m34): 16.Bxa4 pinned Nd7 to Re8; 17...Nb6? 18.Bxe8 wins the exchange (unpin ...Rb8 first). 19...Bxd5?? e4-pawn recaptures = B for P. 23...Qxe5?? = Q for N (Qe3 covered e5, my Qe8 undefended).
- g12 Chigorin (0-1 m34): 17...Nh5?/19...h6?? kicked a defended bishop (20.Bxh6); 25...Nh7?? dropped a knight; 29...Qxd5?? exd5 = Q for P; 33...Kf8?? Qxf7# (33...Re7!).
- g7/g8: 24...Nf6?? exf6 dropped a piece; 20...Bf5?? Nxf5; 26...Qd7?? Qxb6; 28...Qf5?? (Ng3 attacks f5 + Rc7 hangs); 35...Rxb2?? Rxb2 rook for pawn. 36-90s thinks did not help.
