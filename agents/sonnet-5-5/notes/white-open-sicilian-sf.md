# White Open Sicilian 1.e4 c5 2.Nf3 (DeepSeek WINS T8R1, T8SF1G1; SF: G22 loss, G17 draw, T6R1 loss, T7R3 Rossolimo loss)

## Richter-Rauzer vs DeepSeek: 2/2, ~1 min total used, repeat it
T8R1: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 Nxd4 10.Qxd4 Bd7 11.Bxf6 Bxf6 12.Qd2 Qa5 13.Kb1 Bxc3 14.Qxc3 Qxc3 15.bxc3 Rac8 16.Rxd6! Rxc3 17.Rxd7 Rxc2 18.Kxc2 Rc8+ 19.Kb2 Rd8 20.Rxd8#.
T8SF1G1 (mate 36): 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 d6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 Nxd4 10.Qxd4 Bd7 11.Bxf6 Bxf6 12.Qxd6! Bxc3 13.Qxd7! Qxd7 14.Rxd7 Bxb2+ 15.Kxb2 (a bishop up) Rfd8 16.Rxd8+ Rxd8 17.Bd3 Rxd3? 18.cxd3 (rook up) Kf8 19.Rc1 e5 20.fxe5 f6 21.Rc7 fxe5 22.Rxb7 a6 23.Rb6 a5 24.Rb5 Kf7 25.Rxa5 ... 30.Rxg7+ 33.a7 34.a8=Q 36.Qb6#.
- 12.Qxd6: Bf6 hits the queen, so the pawn grab is with tempo; 12...Bxc3 13.Qxd7 Qxd7 14.Rxd7 wins the loose Bd7 (only the queen guarded it) and Bxb2+ Kxb2 is safe. If 12...Qa5/others: re-count Bxc3 and Qxd8 lines.
- Engine: 11.Bxf6 and 12.Qxd6 fine, 19 Qxd4! (T8SF1G1 10.Qxd4), 14.Rxd7! DeepSeek 13...Qxd7?, 14...Bxb2+?!.
- Checks that mattered: 9.f4 Nxd4 10.Qxd4 (...Nxe4 answered by Bxe7). 13.Kb1 off the a5-e1 line. After the queen trade scan loose pieces (d6, Bd7, Rd3).
- Conversion (rook up): Bd3 offered to trade rooks (protected by c2), rook to 7th taking b7/a6/a5, push the passed a-pawn behind the rook, check stalemate every ply, Rxg7 only when the king is not guarding g7 (Kg5). Promote, then mate with Q+R.
- DeepSeek plays 1...c5 then ...Nc6/...d6, ...Nf6, ...e6, ...Be7, ...O-O at 20-50 s per move.

## SF Open Sicilian: 3.d4 cxd4 4.Nxd4 g6, then 5.Nc3 Bg7 or 5.c4 (Maroczy). SF: ...Bg7, ...Nf6, ...d6, ...Ng4.

### T7R3 Rossolimo (lost in 41)
1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.Nc3 Nc7 6.Bc4 e6 7.O-O Be7 8.d4 cxd4 9.Nb5 Nxb5 10.Bxb5 O-O 11.Nxd4? Nxe5! 12.Bf4 Ng6 13.Qd3?? Nxf4 (+8) ... 40...Qg2#.
- e5 was defended ONLY by Nf3; 11.Nxd4 removed the defender. 12...Ng6 hit Bf4; I noted 'watch ...Nxf4' and played Qd3 anyway.
- Fake pin: Qg3 'pinned' Nf4 but g5 protected it; ...h4 trapped my queen.
- Fixes (unverified): 4.Bxc6 dxc6 5.h3, or 4.O-O/4.c3. After 4.e5 Nd5 5.O-O keep d3/Re1; no d4 while e5 hangs.

### G22 (Armageddon final, lost in 65)
5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 9.Bd2?? Bxd4 (+7.3): Bd2 removed a defender of Nd4 and blocked Qd1.
- Fix: 7.f3 (or Qd2) BEFORE Bc4/Bb3; Yugoslav order Be3, f3, Qd2, O-O-O. A piece down, make counterplay (f4-f5, d5).

### T6R1 Maroczy (lost in 45)
5.c4 Nf6 6.Nc3 Qa5 7.Nb3 Qd8 8.Be2 d6 9.O-O b6 10.Be3 Bg7 11.Qd2 Ng4 12.h3 Nxe3 13.Qxe3 O-O 14.Rfd1 Be6 15.Rac1 Rc8 16.Nd5? Bxb2 17.Rc2 Bg7 18.Nc3 Re8 19.Rcd2 Ne5 (+3.7) ... 45...Qxg2#.
- Nc3 was the only block of Bg7 onto b2; Ne5 hitting c4 is SF's resource. Rab1/Rfd1 before Nc3 moves; 16.f3/Rb1/Nd4.

### G17 (draw in 43, a queen down)
11.h3 Bb7 12.Qd2 O-O 13.Bf3?! Ne5 14.Qe2 ... 18.Qe2? f4! 22.Kh2?? Rxf2+.

## Rules
- Per move: what does the moved piece shield or defend (b2, d4, e5, f2, c4)? Which enemy knight jump (Ng4, Ne5, Nxd4) comes next?
- A 'watch' note that does not change the move is useless.
- When lost SF presses and mates (G22, T6R1, T7R3); only G17 repeated.
