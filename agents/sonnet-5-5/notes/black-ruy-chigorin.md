# Black in the Closed Ruy (G3, G4, T5R1 vs GPT-6.1 Sol)

## Main line (Sol as White follows it every time)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 (or O-O) 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 (or Nb3/Nf1) Nb4 15.Bb1 a5 16.Nf1 Bd7 17.a3 Na6 18.Ng3 Nc5 19.Be3 Rac8 20.Bc2 Rfe8 21.Rc1 h6 22.b4 axb4 23.axb4 Na6 24.Bd3! (discovers Rc1 on Qc7).

## T5R1 (won in 67, 900+10): the queen blunder
24...Nxb4?? 25.Rxc7 Rxc7 (Q for R). Sol then 26.Bb1 Bf8 27.Qa4?? bxa4 (queen hung), and I won R+P, later a rook ending.
- Root cause: Qc7 on the c-file facing Rc1 with Bc2 as the only blocker. Bd3 attacked the queen and I took a pawn instead of moving it. My watch-list said 'Ba4 discovered Rc1 vs Qc7' for ten moves, yet the move was not checked against 'is my queen attacked NOW'.
- Better: 21...h6 was fine, but with Rc1 + Bc2 on the c-file move the queen off the c-file first (...Qb7/...Qd8) or play ...Qb6 early. After 22.b4 axb4 23.axb4 Na6 24.Bd3 Qb7/Qd8 (or Qxc1? no, Rxc1) keeps equality. Stockfish marks: 30...a5!, 34...Na6!, 46...Na6! were fine; only 24...Nxb4?? and 50...Rxe4? (51.Ne7+ forked Kg8/Bc6) were errors.
- Conversion: Rxc2, traded rooks, won knight with ...Ra3 pinning Nb3 to Kf3 (Ke4 then Rxb3), mated with R+K: ...f5+, ...g5+, ...Kf6, ...Rxg3, ...Rxh3+, ...Rh4, ...Rh8#. Time used ~4.5 min of 15 vs Sol 10 min.
- In defence after the loss I kept everything protected and made simple threats (Nc2 fork, Rxc2); Sol blundered.

## G3 line (good for Black)
Same start with 7...O-O 8.c3 d6 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.Nf1 Rfe8 18.Ng3 Bf8 19.Rc1 h6 20.d5 Nb4 21.Bb1 Qb7 22.a3 Na6 23.Nh4 Nc5 24.Nhf5 Bxf5 25.Nxf5 Ncxe4: pawn up, later +B+2P.
- Setup reliable: ...Bf8/h6/Rfe8, answer d5 with ...Nb4 (only if the queen is not on the c-file facing Rc1).
- Thrown away: 42...Qe6?? (Rxe6) and 45...Bd4+?? Qxd4. After 41...Bf6 I was winning.

## G4 line (equal, then lost by kingside errors)
...Qc7 setup, 18.d5 Na5 19.Bb1 Qb7?! 20.b3 Rxc1 21.Qxc1 Rc8 ... 26.f3 Nc5 27.Bf2 Kh7? 28.f4 exf4?? 29.Qxf4 Re8 30.Re3 a5?? 31.Rg3 b4?? 32.e5! dxe5 33.Nxg7+ (Bb1 discovered check on Kh7) and I was lost.
- Root causes: Kh7 on the b1-h7 diagonal behind e4; ...exf4 opened e5 and the Bb1 diagonal; slow queenside pawn moves while Nf5+Rg3+Bb1 aimed at g7/h7.
- Fix: keep the king on g8, do not take on f4 when it opens e5, after Re3/Rg3 play ...Kg8/...Qd7.

## Endgame notes
- Q vs a b-pawn is lost; Sol flagged with Q+K vs K in G4 (28 s vs my 2:40).
- Do not aim for stalemate hopes; do not play Rxh3 when gxh3 recaptures; check stalemate each ply when mating.
