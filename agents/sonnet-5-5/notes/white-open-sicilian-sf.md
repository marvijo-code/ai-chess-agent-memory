# White Open Sicilian 1.e4 c5 2.Nf3 (DeepSeek WIN T8R1; SF: G22 loss, G17 draw, T6R1 loss, T7R3 Rossolimo loss)

## T8R1 vs DeepSeek: Richter-Rauzer WIN (mate 20, 900+10, used ~1 min total)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 Nxd4 10.Qxd4 Bd7 11.Bxf6 Bxf6 12.Qd2 Qa5 13.Kb1 Bxc3 14.Qxc3 Qxc3 15.bxc3 Rac8 16.Rxd6! Rxc3 17.Rxd7 Rxc2 18.Kxc2 Rc8+ 19.Kb2 Rd8 20.Rxd8#.
- Engine: 19.Qxd4!, 27/29 trades fine; only 23.Qd2?! (12.Qd2) inexact. DeepSeek 32...Rxc3?? lost Bd7 (d6 pawn and Bd7 were loose after Rac8).
- Checks that mattered: 9.f4 Nxd4 10.Qxd4 (Bg5/Nc3 both protected; ...Nxe4 answered by Bxe7). 12.Qd2 after ...Bxf6 hits Qd4. 13.Kb1 off the a5-e1 line and guards a2. 14.Qxc3 Qxc3 15.bxc3 gives the b-file and an easy ending.
- After the queen trade look for loose Black pieces: d6 pawn plus Bd7 fell to Rxd6. Rd6xd7 then Kxc2 won R+B. Back-rank mate: Black's own pawns f7/g7/h7 block the king.
- Repeat this line vs DeepSeek. DeepSeek plays 1...c5 2...d6 3...cxd4 4...Nf6 5...Nc6 6...e6 7...Be7 8...O-O (25-50 s per move, takes about 1 min a move and falls behind on the clock).

## SF Open Sicilian: 3.d4 cxd4 4.Nxd4 g6, then 5.Nc3 Bg7 or 5.c4 (Maroczy). SF: ...Bg7, ...Nf6, ...d6, ...Ng4.

### T7R3 Rossolimo (lost in 41)
1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.Nc3 Nc7 6.Bc4 e6 7.O-O Be7 8.d4 cxd4 9.Nb5 Nxb5 10.Bxb5 O-O 11.Nxd4? Nxe5! 12.Bf4 Ng6 13.Qd3?? Nxf4 (+8) ... 40...Qg2#.
- e5 was defended ONLY by Nf3; 11.Nxd4 removed the defender. Count defenders of e5 first.
- 12...Ng6 hit Bf4; I had noted 'watch ...Nxf4' and played Qd3 anyway.
- Fake pin: Qg3 'pinned' Nf4 but g5 protected it; ...h4 trapped my queen. Pawn-protected pieces are not pinned.
- Fixes (unverified): 4.Bxc6 dxc6 5.h3, or 4.O-O/4.c3. After 4.e5 Nd5 5.O-O keep d3/Re1; no d4 while e5 hangs. After 8...cxd4 try 9.Nxd4.

### G22 (Armageddon final, lost in 65)
5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 9.Bd2?? Bxd4 (+7.3): Bd2 removed a defender of Nd4 and blocked Qd1.
- Fix: 7.f3 (or Qd2, f3) BEFORE Bc4/Bb3; Yugoslav order Be3, f3, Qd2, O-O-O. A piece down, shuffling Kg1/Kh1 lost; make counterplay (f4-f5, d5).

### T6R1 Maroczy (lost in 45)
5.c4 Nf6 6.Nc3 Qa5 7.Nb3 Qd8 8.Be2 d6 9.O-O b6 10.Be3 Bg7 11.Qd2 Ng4 12.h3 Nxe3 13.Qxe3 O-O 14.Rfd1 Be6 15.Rac1 Rc8 16.Nd5? Bxb2 17.Rc2 Bg7 18.Nc3 Re8 19.Rcd2 Ne5 (+3.7) ... 45...Qxg2#.
- Nc3 was the only block of Bg7 onto b2; Ne5 hitting c4 is SF's resource. Rab1/Rfd1 before Nc3 moves; 16.f3/Rb1/Nd4.

### G17 (draw in 43, a queen down)
11.h3 Bb7 12.Qd2 O-O 13.Bf3?! Ne5 14.Qe2 ... 18.Qe2? f4! 22.Kh2?? Rxf2+.

## Rules
- Per move: what does the moved piece shield or defend (b2, d4, e5, f2, c4)? Which enemy knight jump (Ng4, Ne5, Nxd4) comes next?
- A 'watch' note that does not change the move is useless.
- When lost SF presses and mates (G22, T6R1, T7R3); only G17 repeated.
