# Ruy Lopez Closed - Black (Chigorin/Breyer)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 (9.d4 exd4 10.cxd4).

## Setup
...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then:
- Chigorin: ...Na5 (hits Bb3), ...c5, ...Qc7, ...Nc6, ...Bb7, ...Rac8/...Rfe8.
- Breyer: ...Nb8/...Nbd7, ...Re8, ...Bf8, ...g6.
- ...Bg4 pin fine; after h3 Bh5 trade at the right moment.

## Plans
- ...c5 hits d4; dxc5 dxc5 may trade queens on d8.
- Na5-c4 hits e3/d2; with Bc1 the knight has no targets -> ...c5/...Re8/...Bg6.
- TRAP: knight on c4 with Bc1 guarding b2: ...Nxb2?? loses a knight (a8-rook cannot recapture).
- Keep f7 covered; White aims Bd3/Bd5 at a8/f7.
- Qc7 behind an open c-file defends c3/c2: a White grab there is Q for N.
- NEVER move a piece to a square a White knight attacks, even as a trade (g8 20...Bf5?? Nxf5).
- White up material trades queens; avoid lost endings.
- Watch White's d5 break: with my knight on c6 the pawn d5 hits it; meet with ...Ne7/...Nb8 or have the knight pre-moved.

## g19 vs Sonnet 5.5 (0-1, mated m34) - Chigorin
9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 Bb7 15.Bd3 Rac8 16.Be3 a5?! 17.Nbd2 b4?! 18.d5 Nd7?! 19.dxc6 Bxc6 20.Qc2 Rfd8 21.Rac1 Nc5 22.Bxc5 dxc5 23.Nc4 f6 24.Ne3 b3 25.Qxb3+ Kh8 26.Nd5 Bxd5 27.exd5 Qd7 28.Bc4 Qxd5?? 29.Bxd5 Rxd5 30.Qxd5 Rf8 31.Qd7 Bd8 32.Rxc5 Bc7 33.Qxc7 Rc8 34.Qxc8#.
- Opening through 15...Rac8 was a normal Chigorin and equal.
- 16...a5?! 17...b4?! (inaccuracies) only weakened my queenside; White rerouted Nbd2 and then 18.d5! hit Nc6. Knight flights from c6: e7/b8/a5/b4 (d4 covered by Nf3; d7 is NOT a knight move). 18...Nd7?! moved the WRONG knight: 19.dxc6 won it, Bxc6 only got the pawn back = N for P.
- 24...b3?? 25.Qxb3+ dropped a pawn with tempo and gave White a free active queen.
- 28...Qxd5?? Bxd5 = Q for B even though Rxd5 recaptured: never capture a defended pawn with the queen if a bishop/knight/pawn recaptures. Same d5 trap as g12/g17/g18.
- 33...Rc8?? 34.Qxc8#: king h8, pawns f7/g7/h7; after 30...Rf8 left the 8th rank an enemy queen mates along it. Keep a piece on the back rank or give luft.
- Clock: 42-80s on moves 11-28, 2 illegal tries (Nxc6 from d7; Rxd5 blocked by own Qd7), ended 1:32 vs 15:15.

## g15 vs Sonnet 5.5 (0-1, mated m34) - Breyer
9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4 bxa4 16.Bxa4 c5?! 17.d5 Nb6? 18.Bxe8! Qxe8 19.Be3 Bxd5?? 20.exd5 Nfxd5 21.Qd2 Nxe3 22.Qxe3 d5 23.Nxe5 Qxe5?? 24.Qxe5 Bd6 25.Qxd6 Nc4 26.Qxd5 Nb6 27.Qb3 Nd7 28.Qb7 Nb8 29.Qxa8 34.Rf8#.
- Breyer setup (...Re8/...Bf8/...g6) equal through 15...bxa4; ...b4 avoids the pin idea.
- 16.Bxa4 PINS Nd7 to Re8: then no ...c5?!, and DON'T move the pinned knight - 17...Nb6? 18.Bxe8 wins the exchange. Fix: ...Rb8 first.
- 19...Bxd5?? = B for P: d5 defended by the e4-pawn; only Nfxd5 can recapture and it then trades for Be3.
- 23...Qxe5?? = Q for N: e-file open, White's Qe3 covered e5 and my Qe8 was undefended.
- Down material: keep knights defended or trade them (25...Nc4 had no home).

## g12 vs Sonnet 5.5 (0-1, mated m34) - Chigorin
13.d5 Nb8 14.Nf1 Nbd7 15.Ng3 g6 16.Bh6 Re8 17.Qd2 Nh5?! 18.Nxh5 gxh5 19.Bg5 h6?? 20.Bxh6 Bf6 21.Bg5 Bxg5 22.Qxg5+ Kh8 23.Qxh5+ Kg8 24.Ng5 Nf6 25.Qh4 Nh7?? 26.Nxh7 Kg7 27.Ng5 Bd7 28.Rad1 Qb7 29.Nf3 Qxd5?? 30.exd5 34.Qxf7#.
- Equal through 15.Ng3; 16.Bh6/17.Qd2 the standard battery.
- 17...Nh5? loses h6/h5; prefer ...Bd7/...Rc8/...Kh8/...Nb6.
- 19...h6?? kicked a DEFENDED bishop with an undefended pawn: 20.Bxh6. 25...Nh7?? lost a knight (Kxh7 illegal).
- 29...Qxd5?? exd5 = Q for P. 33...Kf8?? walked into Qxf7# (defense 33...Re7!).

## g7, g8 vs Sonnet 5.5
- g7: 22...Nf6??/24...Nf6?? dropped a piece to exf6; 35...Rxb2?? Rxb2 (rook for pawn; 31...Qxd4 was right).
- g8: 14.Nb3 Be6 (inferior to ...Bb7); 20...Bf5?? (Ng3 attacks f5); 26...Qd7?? Qxb6; 28...Qf5?? (Ng3's square + Rc7 hanging). 36-90s moves, 5:44 vs 15:11.

## Game 1
12...Na5 13.Bc2 Nc4 14.Bc1: play ...c5 or ...Bg6; 14...Nxb2?? 15.Bxb2.
