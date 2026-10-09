# Ruy Lopez Closed - Black (Chigorin/Breyer)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3.

## Setup
...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then:
- Chigorin: ...Na5 (hits Bb3), ...c5, ...Qc7, ...Nc6/...Nb7, ...Bb7/...Bd7, ...Rac8/...Rfe8.
- Breyer: ...Nb8/...Nbd7, ...Re8, ...Bf8, ...g6.
- After 9.h3 the ...Bg4 pin is off.

## Qc7 safety (THE recurring loss: g35, g38)
His Be3 (covers c1+d2) + Rc1 on the c-file = Qc7 is a tempo target; 'defended' (Rc8 behind) is still Rxc7 = R for Q. RETREAT ...Qb8/...Qd8 the move the file opens or earlier.
- g35: 18.Rc1! Qxc1?? 19.Bxc1 (Q for R, mated m29).
- g38: file blocked by his Bc2 and my Nc4; 18...Nc4?? then 19.Bb3! hit the knight AND opened c2->b3: 19...Nb6?? 20.Rxc7 = Q for R. Even saving the knight needed ...Qb8/...Qd8 first. Never a piece move that leaves the queen on the file.
- ...Nc4 only when Bb3 cannot come with tempo on the knight/queen (g16: no ...Nc4 once b3 is played).

## Plans/traps
- ...c5 hits d4; dxc5 dxc5 may trade queens on d8.
- Na5-c4 hits e3/d2; ...Nxb2?? with Bc1 loses a knight (a8-rook cannot recapture).
- Keep f7 covered (Bd3/Bd5 aim at a8/f7). White up material trades queens: avoid lost endings.
- NEVER move a piece to a square a White knight attacks, even as a trade (g8 20...Bf5?? Nxf5).
- White's d5 break: Nc6 is hit -> ...Ne7/...Nb8/...Na5 (g38 15.d5 Na5 16.Ng3 fine; my Bb7 then blocked by d5 becomes bad; ...Bc8 puts a piece on c8 and can block ...Rac8).

## g38 vs GPT-6.1 Sol (0-1, mated m32) - Chigorin
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nf1 Bb7 15.d5 Na5 16.Ng3 Rfe8 17.Be3 Bc8 18.Rc1 Nc4?? 19.Bb3 Nb6?? 20.Rxc7 Nfd7 21.Qd3 Na4 22.Bxa4 bxa4 23.Rec1 Bf8 24.Nf5 Nb6 25.Bxb6 Bxf5 26.exf5 Rac8 27.Rxc8 Rxc8 28.Rxc8 e4 29.Qxe4 ... 32.Qh8#.
- Through 17.Be3 the Chigorin was roughly normal (...Rfe8?! prefer ...Rcd8/...Bf8/...Nd7 as in g35). 18...Nc4?? was the game-losing move; 44s spent on it.
- Correct: 18...Qb8/...Qd8 (or ...Rac8/...Bd7 first), keep ...Nc4 for when the c2-bishop cannot leave with tempo.
- 24...Rac8 illegal (own Bc8 blocks c8) = 1 try, 84s; then 25.Bxb6 won the loose Nb6 (a6-pawn no longer guards b6).
- Clock: 26-45s on moves 12-20 (routine); the m18 blunder came after 44s. Only the 5s final-move scan fixes this.

## Older games - condensed
- g35 Chigorin (0-1 m29): 18.Rc1! Qxc1?? 19.Bxc1 wins Q for R+B; count ALL enemy recapturers incl. bishops. 15...Rfe8?! flagged.
- g19 Chigorin (0-1 m34): 16...a5?! / 17...b4?!; 18.d5 hit Nc6 and 18...Nd7?! moved the wrong knight (19.dxc6 won it). 28...Qxd5?? Bxd5 = Q for B. 33...Rc8?? Qxc8# (no luft).
- g15 Breyer (0-1 m34): Ba4 pins Nd7 to Re8; ...Nb6? Bxe8 loses the exchange (unpin ...Rb8 first). 19...Bxd5?? e4-pawn recaptures = B for P. 23...Qxe5?? = Q for N (Qe3 covered e5).
- g12 Chigorin (0-1 m34): 17...Nh5?/19...h6?? 20.Bxh6; 25...Nh7?? dropped a knight; 29...Qxd5?? exd5 = Q for P; 33...Kf8?? Qxf7#.
- g7/g8: 24...Nf6?? exf6; 20...Bf5?? Nxf5; 26...Qd7?? Qxb6; 35...Rxb2?? Rxb2 rook for pawn. 36-90s thinks did not help.
