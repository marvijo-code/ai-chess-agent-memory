# Ruy Lopez Closed - White (Chigorin)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nf1 a5 15.Ng3/Ne3 Bd7 16.Be3 (NOT Bd2) Rac8 17.Qd2/Rc1 Rfe8.
Record: 0-6, all from middle-game discipline (broken recapture chains, loose pieces, rook grabs).

## g121 vs Sonnet (0-1, Qa4# m43) - Bd2 breaks the d4 recapture: piece down
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nf1 a5 15.Ne3 Bd7 16.Bd2?! Rac8 17.Rc1 Rfe8 18.Nf5 Bxf5 19.exf5 exd4! 20.Nxd4?? Nxd4! 21.Bc3 Nxc2 22.Qxc2 Nd5 23.Qe4 Nxc3 24.bxc3 Bf8 ... Q vs R, mate m43.
- 16.Bd2?! (SF ?!) blocks the d-file: after 19...exd4 the recapture 20.Nxd4 is met by 20...Nxd4 and my Qd1 can NEVER retake d4 (own Bd2 on d2). Piece for a pawn. Play 16.Be3 (guards d4 and leaves the d-file; SF's line) or at least verify the recapture chain before taking.
- Rule: my own bishop/pawn on d2 kills Qd1's d-file recapture of d4. Before a central recapture name every recapturer AND trace its line through my own pieces.
- 18.Nf5 Bxf5 19.exf5 was fine per SF, but it left d4 held only by Nf3, so ...exd4 came.
- After the piece loss it never recovered: 25.Qxe8 Rxe8 26.Rxe8 Qd7 27.Rxf8+ Kxf8 = Q vs R, queen picked off every pawn (f5,h5,b4,f2,a4,b6), mate m43. Down a piece, a Q-for-2R trade is not a save.
- Clock: 31-47 s on moves 8-24 (8.c3 31, 14.Nf1 46, 18.Nf5 46, 20.Nxd4 47, 21-24 ~45 s each) and the blunder came anyway; ended 6:33 vs 11:33. Routine <=15 s.

## g104 vs Sonnet (0-1) - keep Rc1; no undefended knight jump
16.Be3 Rac8 17.Qd2 Rfe8 18.Rac1 h6 19.Rcd1?? Bf8 20.Nh5??.
- 19.Rcd1??: Rc1 guarded c2. Once it left, ...Nb4-...Nc2 + ...Rxc2 won a piece (22...Nb4 23.Bb1 Nc2 24.Qxc2 Qxc2 25.Bxc2 Rxc2, nothing recaptures on c2). Keep Rc1 while his Nc6/Na5, Qc7 and c8-rook are live; move the queenside rook only for a concrete reason.
- 20.Nh5??: undefended knight onto a square his f6-knight attacks = piece for nothing. A 'trade offer' needs a defender or a legal recapturer.
- Cascade after the loss: 26.Rd4?? exd4; 28.Rxe4?? Rxe4; 32.Be5?? dxe5 (bishop onto the d6-pawn's square). Clock 36-46 s on moves 13-20, ended 5:46 vs 14:35.

## g84/g82/g78 (0-1 each) - knight geometry, queen squares, d4 defense
- g84: 19.Qc2?? with Bd3 let ...Nb4! fork Qc2+Bd3; his f8-rook recaptured c8 (grab of a DEFENDED rook = Q+R for 2R). Sweep his knight's squares before ANY queen move: c2/d3 must not both be b4-knight squares.
- g82: 17...exd4 18.Nxd4?? Nxd4 - d4 had ONE defender (Nf3); Qe2 does NOT cover d4 (only Qd1/Qd2 do), so no recapturer. 20.Nf5?? Bxf5 (d7-e6-f5 ray); 22.Rxe7??; 23.Qxd5?? (e7+f6 hit d5). Keep Qd1/Qd2 while ...Nc6/...exd4 loom: Nf1 BEFORE Qe2.
- g78: 16.Bg5?? h6 17.Be3?? Nc4! 18.Nh5?? Nxe3! 19.fxe3 Qxc2! (Bc2 had one defender, rook second-attacked). After ...h6 do not return to e3; trade on f6 or play Bd2/Bf4.

## Older - condensed
- g77: 13.d5 c4; 16...g6 takes f5 from both knights; 20.Bxc5?? B for N; 39...Bc6 aimed Qxg2#.
- g73: 23.Be5?? dxe5 24.Qd2?? Rxd2; when his capture opens a file onto my queen, leave the FILE.
- g67/g65/g61/g60: 26.Rxe7??; 21.Bxh6?? gxh6; 24.Qa3?? Rxa3; 21.Qxa4?? bxa4.

## Working
- 14...Nb4 -> 15.Bb1!; reroute Nf1-g3 only with d4 safe (Qd2/Nf3) and ...g6 off.
- 16.Be3 keeps the d-file and guards d4; 16.Bd2 blocks my queen's recapture line.
- No queen on d4 vs his e5-pawn; no undefended rook onto his rook's rank/file; count every recapturer.
- Never Qc2 with Bd3 while ...Nb4 is possible (g84); equal Chigorin: improve slowly, keep Rc1, routine <=15 s.
