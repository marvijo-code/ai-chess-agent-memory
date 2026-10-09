# White 1.e4 c5 2.Nf3 vs Stockfish 19 (G22 loss, G17 draw, T6R1 loss, T7R3 Rossolimo loss)

Open Sicilian start: 3.d4 cxd4 4.Nxd4 g6, then 5.Nc3 Bg7 or 5.c4 (Maroczy). SF: ...Bg7, ...Nf6, ...d6, ...Ng4.

## T7R3 Rossolimo (lost in 41, 900+10, 7:30 unused)
1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.Nc3 Nc7 6.Bc4 e6 7.O-O Be7 8.d4 cxd4 9.Nb5 Nxb5 10.Bxb5 O-O 11.Nxd4? Nxe5! (+1.5) 12.Bf4 Ng6 13.Qd3?? Nxf4 (+8) ... 36...h4 37.Qxf4 Qxf4+ ... 40...Qg2#.
- e5 pawn was defended ONLY by Nf3. 11.Nxd4 removed the defender, so ...Nc6xe5 was free (Qxd4 impossible, Nxd4). Count defenders of e5 before moving Nf3.
- 12...Ng6 attacked Bf4; Qd3 does not guard f4. My note said 'watch ...Nxf4' and I played it anyway. After EVERY enemy move list the attacked pieces of mine and their defenders before choosing a move.
- Fake pin: Qg3 'pinned' Nf4 to Qc7, but g5 supported Nf4. ...h4 attacked Qg3 and she had no square (Qxf4 gxf4). A pin does nothing if the pinned piece is pawn-protected, and a pawn push can hit my queen. I based moves 28-36 on that pin.
- Fixes (unverified): avoid the 4.e5 / d4 structure. Try 4.Bxc6 dxc6 5.h3, or 4.O-O/4.c3 setups. After 4.e5 Nd5 5.O-O keep d3/Re1; do not play 8.d4 while e5 hangs on Nf3. After 8...cxd4 consider 9.Nxd4 Nxd4 10.Qxd4 instead of 9.Nb5.
- A pawn down is OK; a piece down vs SF is lost. Spend the 60+ s at moves 11-13, not at move 30.

## G22 (Armageddon final, lost in 65)
5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 9.Bd2?? Bxd4 (+7.3). 9.Bd2 removed a defender of Nd4 AND blocked Qd1.
- Fix: play 7.f3 (or Qd2 then f3) BEFORE Bc4/Bb3. Yugoslav order: Be3, f3, Qd2, then O-O-O. Vs ...Ng4 with Nd4 hit, consider 9.Nxc6 or 9.Bg5 and count every capture on d4.
- A piece down I shuffled Kg1/Kh1 and SF improved (...b4, ...Ba8, Nf2+). Make counterplay (f4-f5, d5).

## T6R1 Maroczy (lost in 45)
5.c4 Nf6 6.Nc3 Qa5 7.Nb3 Qd8 8.Be2 d6 9.O-O b6 10.Be3 Bg7 11.Qd2 Ng4 12.h3 Nxe3 13.Qxe3 O-O 14.Rfd1 Be6 15.Rac1 Rc8 16.Nd5? Bxb2 17.Rc2 Bg7 18.Nc3 Re8 19.Rcd2 Ne5 (+3.7) 20.Nd5 Nxc4 ... 45...Qxg2#.
- Nc3 was the only block of Bg7 onto b2. Ne5 hitting c4/Bf3 is SF's Maroczy resource. Fixes: Rab1/Rfd1 before Nc3 moves; 16.f3/Rb1/Nd4.

## G17 (draw in 43, was a queen down)
11.h3 Bb7 12.Qd2 O-O 13.Bf3?! Ne5 14.Qe2 Nfd7 15.Rfd1 Nxf3+ 16.Qxf3 Rc8 17.Nd2 f5 18.Qe2? f4! 19.Bxf4 Rxf4 20.g3 Rf7 ... 22.Kh2?? Rxf2+.

## Rules
- Per move: what does the moved piece shield or defend (b2, d4, e5, f2, c4)? Which enemy knight jump (Ng4, Ne5, Nxe5, Nxd4) hits next?
- A 'watch' note that does not change the move is useless.
- When lost SF usually presses and mates (G22, T6R1, T7R3); only G17 repeated.
