# Ruy Lopez Closed - Black (Chigorin/Breyer)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 (9.d4 exd4 10.cxd4).

## Setup
...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then:
- Chigorin: ...Na5 (hits Bb3), ...c5, ...Qc7, ...Nc6, ...Bb7, ...Rac8/...Rfe8.
- Breyer: ...Nb8/...Nbd7, ...Re8, ...Bf8, ...g6.
- ...Bg4 pin fine; after h3 Bh5 trade at the right moment.

## Plans
- ...c5 hits d4; dxc5 dxc5 may trade queens on d8.
- Na5-c4 hits e3/d2; if White plays Bc1 the knight has no targets -> ...c5/...Re8/...Bg6.
- TRAP: knight on c4 with Bc1 guarding b2: ...Nxb2?? loses a knight (a8-rook cannot recapture).
- Keep f7 covered; White aims Bd3/Bd5 at a8/f7.
- Qc7 behind an open c-file defends c3/c2: a White grab there is Q for N.
- NEVER move a piece to a square a White knight attacks, even as a trade (g8 20...Bf5?? Nxf5).
- White up material trades queens; avoid lost endings.

## g15 vs Sonnet 5.5 (0-1, mated m34) - Breyer
9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4 bxa4 16.Bxa4 c5?! 17.d5 Nb6? 18.Bxe8! Qxe8 19.Be3 Bxd5?? 20.exd5 Nfxd5 21.Qd2 Nxe3 22.Qxe3 d5 23.Nxe5 Qxe5?? 24.Qxe5 Bd6 25.Qxd6 Nc4 26.Qxd5 Nb6 27.Qb3 Nd7 28.Qb7 Nb8 29.Qxa8 34.Rf8#.
- Equal through 15...bxa4; the Breyer setup (...Re8/...Bf8/...g6) is fine (...b4 avoids the pin idea).
- 16.Bxa4 PINS Nd7 to Re8. Then 16...c5?! 17.d5 Nb6? 18.Bxe8 wins the exchange: never move the pinned knight or push ...c5 before unpinning. Fix: ...Rb8 (rook off e8), then Bxd7 is only equal.
- 19...Bxd5?? = B for P: d5 is defended by the e4-pawn; the c5-pawn cannot recapture (only Nfxd5, which then trades for Be3). Count PAWN defenders.
- 23...Qxe5?? = Q for N: the e-file was open (e4-pawn gone), White's Qe3 covered e5 and my Qe8 was undefended. Never recapture on a square an enemy queen's file hits.
- 25...Nc4 chased the queen but had no home: Qxd5/Qb3/Qb7 all hit it. Down material: keep knights defended or trade them.
- Clock: 32-46s on most moves 12-29; ended 5:46 vs 15:29.

## g12 vs Sonnet 5.5 (0-1, mated m34) - Chigorin
13.d5 Nb8 14.Nf1 Nbd7 15.Ng3 g6 16.Bh6 Re8 17.Qd2 Nh5?! 18.Nxh5 gxh5 19.Bg5 h6?? 20.Bxh6 Bf6 21.Bg5 Bxg5 22.Qxg5+ Kh8 23.Qxh5+ Kg8 24.Ng5 Nf6 25.Qh4 Nh7?? 26.Nxh7 Kg7 27.Ng5 Bd7 28.Rad1 Qb7 29.Nf3 Qxd5?? 30.exd5 34.Qxf7#.
- Equal through 15.Ng3; 16.Bh6/17.Qd2 is the standard battery.
- 17...Nh5? opens the g-file and loses h6/h5; prefer ...Bd7/...Rc8/...Kh8/...Nb6.
- 19...h6?? kicked a DEFENDED bishop with an undefended pawn: 20.Bxh6.
- 25...Nh7?? lost a knight (defended by Qh4; Kxh7 illegal).
- 29...Qxd5?? exd5 = Q for P (e4-pawn). 33...Kf8?? walked into Qxf7# (defense 33...Re7!).

## g7, g8 vs Sonnet 5.5
- g7: 22...Nf6??/24...Nf6?? dropped a piece to exf6; 35...Rxb2?? Rxb2 (rook for pawn; 31...Qxd4 was right).
- g8: 14.Nb3 Be6 (inferior to ...Bb7); 20...Bf5?? (Ng3 attacks f5); 26...Qd7?? Qxb6; 28...Qf5?? (Ng3's square + Rc7 hanging). 36-90s moves, 5:44 vs 15:11.

## Game 1
12...Na5 13.Bc2 Nc4 14.Bc1: play ...c5 or ...Bg6; 14...Nxb2?? 15.Bxb2.
