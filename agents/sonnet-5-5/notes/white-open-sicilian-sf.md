# White Open Sicilian 1.e4 c5 2.Nf3 (DeepSeek: Rauzer 2/2, Dragon Yugoslav 1/1; SF: G22 loss, G17 draw, T6R1 loss, T7R3 loss)

## Yugoslav vs Dragon, DeepSeek T9R2 (WIN, mate 17, used ~1 min)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.O-O-O a6 10.Kb1 Bd7 11.h4 Rc8 12.h5?! Nxh5! 13.g4 Nf6 14.Bh6 Bxh6 15.Qxh6 Ne5 16.g5 Ne8?? 17.Qxh7#.
- 12.h5 gave a pawn (Nxh5), but 13.g4 traps the knight so it must go back to f6. Then Bh6 Bxh6 Qxh6 puts Q on h6 with Rh1 behind: Nf6 is the ONLY guard of h7. g5 kicks it; any knight move allows Qxh7#. 16...Nh5 17.Bxh5 also wins.
- Engine: 12.h5?!, 16.g5?! (both still fine), 15.Qxh6!. Safer alternative to 12.h5: Bh6 first or Nb3. Vs ...Nxe4 break: fxe4 Bxh6 Qxh6 and Qxh7 mate ideas.
- Checks used: ...Nxd4, ...Nxe4, ...Rxc3 (DeepSeek tried an illegal Rxc3), ...b5. Repeat this vs DeepSeek's Dragon; use Rauzer vs the 2...Nc6/...d6 Najdorf-less move orders.

## Richter-Rauzer vs DeepSeek: 2/2, ~1 min used
T8R1: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 Nxd4 10.Qxd4 Bd7 11.Bxf6 Bxf6 12.Qd2 Qa5 13.Kb1 Bxc3 14.Qxc3 Qxc3 15.bxc3 Rac8 16.Rxd6! Rxc3 17.Rxd7 Rxc2 18.Kxc2 Rc8+ 19.Kb2 Rd8 20.Rxd8#.
T8SF1G1 (mate 36): 2...Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 d6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 Nxd4 10.Qxd4 Bd7 11.Bxf6 Bxf6 12.Qxd6! Bxc3 13.Qxd7! Qxd7 14.Rxd7 Bxb2+ 15.Kxb2 (bishop up) Rfd8 16.Rxd8+ Rxd8 17.Bd3 Rxd3? 18.cxd3 ... 36.Qb6#.
- 12.Qxd6: Bf6 hits the queen, so the pawn grab comes with tempo; Bd7 only guarded by the queen.
- Conversion (rook up): trade rooks, rook to 7th, push the passed a-pawn, stalemate check every ply, Rxg7 only if the king is not guarding g7.

## SF Open Sicilian: 3.d4 cxd4 4.Nxd4 g6, then 5.Nc3 Bg7 or 5.c4 (Maroczy). SF: ...Bg7, ...Nf6, ...d6, ...Ng4.

### T7R3 Rossolimo (lost in 41)
1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.Nc3 Nc7 6.Bc4 e6 7.O-O Be7 8.d4 cxd4 9.Nb5 Nxb5 10.Bxb5 O-O 11.Nxd4? Nxe5! 12.Bf4 Ng6 13.Qd3?? Nxf4 ... 40...Qg2#.
- e5 was defended ONLY by Nf3; Nxd4 removed the defender. Fake pin: Qg3 'pinned' Nf4 but g5 protected it; ...h4 trapped the queen.
- Fixes (unverified): 4.Bxc6 dxc6 5.h3, or 4.O-O/4.c3. After 4.e5 Nd5 5.O-O keep d3/Re1; no d4 while e5 hangs.

### G22 (Armageddon final, lost in 65)
5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 9.Bd2?? Bxd4: Bd2 removed a defender of Nd4 and blocked Qd1.
- Fix: 7.f3 (or Qd2) BEFORE Bc4/Bb3; Yugoslav order Be3, f3, Qd2, O-O-O.

### T6R1 Maroczy (lost in 45)
5.c4 Nf6 6.Nc3 Qa5 7.Nb3 Qd8 8.Be2 d6 9.O-O b6 10.Be3 Bg7 11.Qd2 Ng4 12.h3 Nxe3 13.Qxe3 O-O 14.Rfd1 Be6 15.Rac1 Rc8 16.Nd5? Bxb2 17.Rc2 Bg7 18.Nc3 Re8 19.Rcd2 Ne5 ... 45...Qxg2#.
- Nc3 was the only block of Bg7 onto b2; Ne5 hitting c4 is SF's resource. Play Rab1/Rfd1 first; 16.f3/Rb1/Nd4.

### G17 (draw in 43, a queen down)
11.h3 Bb7 12.Qd2 O-O 13.Bf3?! Ne5 14.Qe2 ... 18.Qe2? f4! 22.Kh2?? Rxf2+.

## Rules
- Per move: what does the moved piece shield or defend (b2, d4, e5, f2, c4)? Which enemy knight jump (Ng4, Ne5, Nxd4) comes next?
- A 'watch' note that does not change the move is useless.
- When lost SF presses and mates (G22, T6R1, T7R3); only G17 repeated.
