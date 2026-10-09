# Black Closed Ruy / Chigorin (DeepSeek: W T6R2,T7R2,T7R5.2,T11R2,T12R2,T12R5.2,T14R1; D T13R1. Sol: W T9SF2G1,T5R1,T6SF2G1; L T7R1,G3,T14R3; D G4)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 then 14.d5 Nb4 15.Bb1 a5 (a3 Na6, ...Nc5) / 14.Nb3 / 14.Nf1 Bb7 / 14.Bb3 Bd7.

## T14R3 vs Sol: LOST (mate 52, 900+10): b5 pawn, then d6, then fork
14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Ng3 Bd7 19.Be3 Rac8 20.Nf5 Bxf5 21.exf5 Rfe8 22.Ba2 h6 23.Rc1 Kh8?? 24.Qe2 Bd8?? 25.Qxb5 Qb6 26.Qxb6 Bxb6 27.Red1 Rc7? 28.Nd2 Rec8 29.Nc4 Ba7 30.Nxd6 Rd8 31.Nb5 (forks Rc7+Ba7) Nxd5 32.Bxd5 Rb7 33.Bxb7 ... R+B down, 50.b8=Q, 52.Qh8#.
- SF: position fine at move 20. 20...Bxf5 removed Bd7, the ONLY guard of b5. Moves 21-24 (Rfe8, h6, Kh8, Bd8; ~1 min each) were waiting moves while Qe2 aimed at b5.
- Fix (unverified): 21...Qb7 (guards b5, keeps c-file) or ...Rb8 / ...b4 (axb4 axb4 opens a-file); or meet 20.Nf5 with ...Bf8 keeping Bd7. Each move write 'my pawns with no defender' (b5, d6, a5).
- 28...Rec8 29.Nc4 hit Bb6 and d6; Rc7+Ba7 stood a knight-jump from Nb5. List knight forks before placing two pieces on c7/a7/d6.
- Down R+B I shuffled Kh6/Kh7 while the b-pawn walked in; no fortress vs a passer. Avoid reaching it.

## T14R1 vs DeepSeek: WON (mate 33)
14.Bb3 Bd7 15.dxe5 dxe5 16.Nc4? bxc4! 17.Bxc4 Be6 18.Bxe6 fxe6! 19.Qd6?? Bxd6 20.Bg5 Be7 21.Bxf6 Bxf6 ... Qh2#. Nd2 blocks the d-file so Bd7 is safe; ...fxe6 keeps e5 guarded by Nc6+Qc7. Up a queen: trade pieces, rook to d-file, push passer to d3, Qc1+/Be5+ vs Kh2.

## T13R1 vs DeepSeek: DRAW (threefold, ply 99) with B+B+N vs pawns
My K sat on g7, I shuffled 15 moves vs K h1/h2/h3. Rules: walk my K to f3/g3; push h-pawn with K+B support; never allow a 2nd repetition (bishop-tempo triangulation); no mate in 10 -> promote or trade to won K+Q. Keep a spare move for stalemate.

## T12R5.2 / T12R2 / T11R2 vs DeepSeek: WON
T12R5.2: 14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.a3 Na6 18.Be3 Nc5 19.Bxc5 Qxc5 20.Qd2 Rfc8 21.Ng3 h6 22.Nf5 Bxf5 23.exf5 Nxd5?! (Rab8 safer) ... mate 34. Keep Ra8 guarding a5.
T12R2: 14.Nf1 Bb7 15.Ng3 Rfe8 16.d5 Nb4 17.Bb1 a5 18.a3 Na6! 19.Be3 Nc5 20.Bxc5 dxc5. Vs d5: ...Nb4, ...a5, a3 Na6 (Nc6?? dxc6), ...Nc5.
T11R2: 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.b4 axb4 18.axb4 Bd7! (not Nxb4: Rxa8) 19.Ba3 Nxb4 20.Bxb4 Rxa1!.
T7R5.2: 14.Nb3 a5 15.dxe5 dxe5 16.Be3 a4 17.Nc5? Bxc5. T7R2: 19.Qd2 Nc2!. T6R2: 19.Ng3?? Nb3! forks. DeepSeek leaves pieces hanging.

## Sol games
T9SF2G1 WON (mate 67): 14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rfc8 18.a3 Na6 19.Be3 Nc5 ... 23.Nf5 Bxf5 24.exf5 ... 26.g4 Bf6 27.g5 Bxg5. Trade outpost knight, ...Bf6 vs g5, queen off c-file, queen-trade offers + ...Nh7. Slip 44...b4?? 45.Be6.
T7R1 LOST (mate 36) after winning a piece: 19...Qc4?? 20.Rxc4. List queen escape squares before a queen grab.
T6SF2G1/T5R1 won: 14.Nb3 a5 15.Be3 a4 ... 19.a3 Nc2!; 24.Bd3! discovers Rc1 on Qc7. G3: pawn up, thrown away by 42...Qe6??. G4: 28.f4 exf4?? opened e5/b1-h7.

## Endgame
Q vs b-pawn is lost. No Rxh3 when gxh3. Ladder mate with two rooks: stalemate check every ply.
