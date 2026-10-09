# White Open Sicilian 1.e4 c5 2.Nf3 (DeepSeek: Rauzer 2/2, Yugoslav 1/1; SF: T13R3 DRAW, G22 L, G17 D, T6R1 L, T7R3 L)

## T13R3 vs SF: Maroczy, DRAW by repetition from a lost K+P ending (900+10, used only ~3 min)
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5 7.Nb3 Qd8 8.Be2 d6 9.O-O b6 10.Be3 Bg7 11.Qd2 Ng4 12.Bxg4 Bxg4 13.f3 Be6 14.Nd5 O-O 15.Rac1 Rc8 16.Rfd1 f5 17.exf5 Rxf5 18.Nf4 Qd7 19.Nxe6 Qxe6 20.Nd4?! Nxd4 21.Bxd4 Rxc4! 22.Rxc4 Qxc4 23.Bxg7 Kxg7 24.Qd4+ Qxd4+ 25.Rxd4 (R ending a pawn down, +3) ... 28.Rxa5 bxa5 ... K+P ending lost, e-pawn queened at move 44.
- Opening was GOOD: SF eval was -0.7..-1.0 for Black at moves 7-12 (7.Nb3 Qd8 and the Be2/O-O/Be3/Qd2 setup). Equal at 19.
- THE ERROR 20.Nd4?!: after Nd5 and Nxe6 left, c4 was guarded only by Rc1; Nxd4 Bxd4 Rxc4 won a pawn (Bd4 hangs to Bg7 and Qxc4 comes with tempo). My note 'c4 by Rc1' was true but one defender vs Rf5xc4 + Qe6 + Bg7-x-d4 tactic. Better (unverified): 20.b3 or 20.Qd3 first (keep c4 solid, then Nd4); or 19.Qd3 / 19.Nxe6 Qxe6 20.b3.
- RULE: in the Maroczy my c4 pawn is the target. Before trading minor pieces count attackers vs defenders on c4 (Rc8, Qe6/Qd7, Bxc4) and add b3/Qd3 BEFORE the trade. Don't play Nd5 and then move it away.
- 28.Rxa5 bxa5 gave a lost K+P ending; keep rooks when a pawn down (SF only +3 with rooks).
- LIFELINE THAT WORKED: lost K+3P vs Q+2P, I fixed all my pawns (a3, g4, h5 blocked), put the king on h8/g8 corner so every Black queen move risked stalemate. SF (depth 4) just shuffled Qd7/Qe7 and drew by threefold at ply 137. Try the same when lost: block own pawns, king to a corner, 1-5 s per move.

## Yugoslav vs Dragon, DeepSeek T9R2 (WIN, mate 17)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.O-O-O a6 10.Kb1 Bd7 11.h4 Rc8 12.h5?! Nxh5! 13.g4 Nf6 14.Bh6 Bxh6 15.Qxh6 Ne5 16.g5 Ne8?? 17.Qxh7#.
- 13.g4 traps the knight; Bh6 Bxh6 Qxh6 with Rh1 behind: Nf6 is the only guard of h7; g5 kicks it. Checks used: ...Nxd4, ...Nxe4, ...Rxc3, ...b5. Safer than 12.h5: Bh6 first or Nb3.

## Richter-Rauzer vs DeepSeek: 2/2
T8R1: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 Nxd4 10.Qxd4 Bd7 11.Bxf6 Bxf6 12.Qd2 Qa5 13.Kb1 Bxc3 14.Qxc3 Qxc3 15.bxc3 Rac8 16.Rxd6! Rxc3 17.Rxd7 Rxc2 18.Kxc2 Rc8+ 19.Kb2 Rd8 20.Rxd8#.
T8SF1G1: same to 11...Bxf6 12.Qxd6! Bxc3 13.Qxd7! Qxd7 14.Rxd7 Bxb2+ 15.Kxb2 (piece up), mate 36. Bf6 hits the queen so Qxd6 comes with tempo.
- Conversion (rook up): trade rooks, rook to 7th, passed a-pawn, stalemate check every ply.

## SF losses
T7R3 Rossolimo: 1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.Nc3 Nc7 6.Bc4 e6 7.O-O Be7 8.d4 cxd4 9.Nb5 Nxb5 10.Bxb5 O-O 11.Nxd4? Nxe5! (e5 guarded only by Nf3). Fix: 4.Bxc6 or 4.O-O/c3; no d4 while e5 hangs.
G22: 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 9.Bd2?? Bxd4. Play 7.f3/Qd2 BEFORE Bc4/Bb3.
T6R1 Maroczy: 10.Be3 Bg7 11.Qd2 Ng4 12.h3 Nxe3 13.Qxe3 ... 16.Nd5? Bxb2 (Nc3 was the only block of Bg7 onto b2). Rab1/Rfd1 first.
G17 (draw): 18.Qe2? f4! 22.Kh2?? Rxf2+.

## Rules
- Per move: what does the moved piece shield or defend (b2, d4, e5, f2, c4)? Which enemy knight jump comes next?
- A 'watch' note that does not change the move is useless.
- Maroczy: h3 early, b3 to support c4, do not trade minors until c4 is safe.
