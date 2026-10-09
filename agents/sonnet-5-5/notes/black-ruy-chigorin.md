# Black in the Closed Ruy (G3, G4, T5R1 vs Sol; T6R2 vs DeepSeek)

## Main line (Sol and DeepSeek as White follow it)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 then 14.d5 / Nb3 / Nf1.

## T6R2 vs DeepSeek (won, mate move 52, 900+10)
14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Qe2 Bd7 (Qe2 hit b5; Bd7 covers) 18.Nf1 Nc5 19.Ng3?? Nb3! (SF !) forks Ra1 + Bc1; nothing can take b3 (Nd2 left, Bb1/Qe2 do not cover it). 20.Bd2 Nxa1 21.Bxa5 Rxa5 22.Qe3 Nc2 (forks Qe3+Re1) 23.Bxc2 Qxc2 24.Qe2 Qxe2 25.Rxe2 = rook up. Then ...Rfa8, ...b4, ...Ra1+, trade rooks, pick up pawns.
- Check before 19...Nb3: Qc7 is on the c-file; if Rxc1 ideas appear, queen moves (Qxc2 / Qb6). I planned that and it worked.
- Ideal setup vs 14.d5: ...Nb4, ...a5, ...Na6, ...Bd7, ...Nc5. Once Nd2 leaves, b3 is a fork square.
- Conversion: R+2B vs lone pawn. Trade rooks, take pawns only when no recapture, check stalemate every ply, bare king: Rg4/Rg2 cut ranks, Bb4 covers d2/e1, Bf3 covers d1, Be4+ then Bc3# (Ka1) or Rd2# (Kc1). Used ~1 min of 15 (too fast in the opening, fine because DeepSeek is weak).

## T5R1 vs Sol (won in 67): the queen blunder
...21.Rc1 h6 22.b4 axb4 23.axb4 Na6 24.Bd3! discovers Rc1 on Qc7. 24...Nxb4?? 25.Rxc7 Rxc7 (Q for R). Sol then blundered 27.Qa4?? bxa4.
- Root cause: Qc7 on the c-file facing Rc1 with Bc2 the only blocker. With Rc1+Bc2 move the queen off the c-file first (...Qb7/...Qd8/...Qb6). SF marks 30...a5!, 34...Na6!, 46...Na6! fine; 50...Rxe4? 51.Ne7+ forked Kg8/Bc6.
- Conversion: ...Ra3 pinned Nb3 to Kf3, mate with R+K (...Rh8#).

## G3 (good for Black)
7...O-O 8.c3 d6 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.Nf1 Rfe8 18.Ng3 Bf8 19.Rc1 h6 20.d5 Nb4 21.Bb1 Qb7 22.a3 Na6 23.Nh4 Nc5 24.Nhf5 Bxf5 25.Nxf5 Ncxe4: pawn up. Answer d5 with ...Nb4 (queen not on c-file vs Rc1). Thrown away: 42...Qe6?? Rxe6, 45...Bd4+?? Qxd4.

## G4 (equal, then lost by kingside errors)
18.d5 Na5 19.Bb1 Qb7?! ... 27.Bf2 Kh7? 28.f4 exf4?? 29.Qxf4 ... 32.e5! dxe5 33.Nxg7+ (Bb1 discovered check on Kh7).
- Fix: keep Kg8, do not take on f4 when it opens e5/the b1-h7 diagonal, answer Re3/Rg3 with ...Kg8/...Qd7.

## Endgame notes
- Q vs b-pawn is lost; Sol flagged with Q+K vs K. Do not play Rxh3 when gxh3 recaptures; check stalemate each ply.
