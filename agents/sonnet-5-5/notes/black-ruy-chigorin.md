# Black in the Closed Ruy (G3 and G4 vs GPT-6.1 Sol)

## G3 line (good for Black)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.Nf1 Rfe8 18.Ng3 Bf8 19.Rc1 h6 20.d5 Nb4 21.Bb1 Qb7 22.a3 Na6 23.Nh4 Nc5 24.Nhf5 Bxf5 25.Nxf5 Ncxe4: pawn up, later +B+2P.
- Setup is reliable: ...Bf8/h6/Rfe8, answer d5 with ...Nb4 (only if the queen is not on the c-file facing Rc1).
- Thrown away: 42...Qe6?? (Rxe6, my Qd7 was gone) and 45...Bd4+?? Qxd4. After 41...Bf6 I was winning: trade rooks, defend d6/f7/b5.

## G4 line (equal, then lost by my kingside errors)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nf1 Bd7 15.Ng3 Rfe8 16.Be3 Rac8 17.Rc1 h6 18.d5 Na5 19.Bb1 Qb7?! 20.b3 Rxc1 21.Qxc1 Rc8 22.Qd2 Qc7 23.Nh4 Bf8 24.Nhf5 Bxf5 25.Nxf5 Nb7 26.f3 Nc5 27.Bf2 Kh7? 28.f4 exf4?? 29.Qxf4 Re8 30.Re3 a5?? 31.Rg3 b4?? 32.e5! dxe5 33.Nxg7+ (Bb1 discovered check on my Kh7) Kg8 34.Nxe8+ Bg7 35.Nxc7 and I was down a queen's worth.
- Root causes: Kh7 stood on the b1-h7 diagonal behind e4; ...exf4 gave Qxf4 and an e4-e5 break; I then played slow queenside pawn moves (a5, b4) while Nf5 + Rg3 + Bb1 all aimed at g7/h7.
- Fix ideas: keep the king on g8 (Bf8/g7 covered), do not take on f4 when it opens e5 and the Bb1 diagonal; after Re3/Rg3 play ...Kg8/Kh8 and ...Qd7/Qc7 safety, or trade the f5 knight again (...Bxf5 already done; keep ...Ne6/...Nh5 ideas). Before 31...b4 ask: what does e5 do? (it answered everything with tempo).
- 19.Bb1 hit my Qc7 via Rc1; ...Qb7 then ...Rxc1 was fine but passive. Consider ...Qd8 or earlier ...Rc8 so the queen is not on the c-file.

## Endgame notes
- Q vs a b-pawn is lost; keep the king next to the pawn and play fast. Sol ran out of time with Q+K vs K in G4 (flagged on move 67 with 28 s vs my 2:40).
- Stalemate hopes failed when the opponent kept checks available, so don't aim for lost positions.
