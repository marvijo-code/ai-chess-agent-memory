# White Open Sicilian 1.e4 c5 2.Nf3 (DeepSeek: Rauzer 2/2, Yugoslav 6/6; SF Maroczy: T33R3 W, T13R3 D, T14R2 D, T31R2 D; T19R2 D a piece down)

## Maroczy vs SF (1 W, 3 D)
Setup, SF plays it every time: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6, then
5.c4 Nf6 6.Nc3 Qa5 7.Nb3 Qd8 8.Be2 d6 9.O-O b6 10.Be3 Bg7 11.Qd2 Ng4
12.Bxg4 Bxg4 13.f3 Be6 14.Nd5 O-O 15.Rac1 Rc8 16.Rfd1 f5 17.exf5 Rxf5 (T33R3 W, mate 51)

### T33R3 WIN (14:xx v 12:xx, ended 11:39 left)
- Nd5 guarded by c4, e4, Qd2, Rd1: SF cannot take it profitably; I named guards of d5/f4/b2 every move.
- 18.Bd4? (40 s, SF ?) Ne5 19.Bxe5 Rxe5 20.f4 Rf5 21.Nd4 Bxd4+ 22.Qxd4 Qf8 23.g3 (f4 hit twice: Rf5 + Qf8) Bxd5 24.cxd5 Rc5 25.Rxc5 bxc5: equal. Untested alternatives to 18.Bd4: 18.Nd4, 18.Qe3.
- 26.Qe4 Qg7 27.Rd2 a5 28.Kg2 Kf8 29.Qa4 (hits a5, d5 and b2 guarded) Rxd5?? 30.Rxd5 e6 31.Rxd6 Qxb2+ 32.Kh3 (not Kf1/Rd2/Qc2) Qe2 33.Qd1 Qxd1 34.Rxd1: R up. Then Rd7+ Rxh7, Rxc4, Rxa5, a-pawn queens, Qb7+ Re6+ Qh7#.
- Time: moves 20-23 took 38-61 s (too slow); conversion moves 2-10 s.

### T31R2 (D, pawns down, SF +6)
- 14.Qe2?! Bxc3! 15.bxc3 Ne5 (+1.0): c3 weak, c4 hit by Ne5/Bxc4. 17.f4 took 67 s. Later 32...Rce7! 33.Kh2?? Qxe4: e4 attacked by Qe6+Re7, guarded by Qd3 only; Kh2/Kg1 guarded nothing.
- Fix: book 14.Nd5. After doubled c-pawns keep c4 guarded by Nd2 + Qe2 BEFORE ...Ne5; at move 32 add a second e4 guard (Re1/Bd4/Rfe2).
- Fortress that held: Ra3 guarding a4+c3, K Kc2/Kd2, no pawn moves; SF repeated at +6.3 (move 63, 50 s left).
- T13R3: 14.Nd5 fine; c4 became the target (20.Nd4? Rxc4): b3/Qd3 BEFORE trading minors. T14R2 12.h3?! Nxe3 13.Qxe3 Bh6: keep Q off e3; lifeline Qd4 + Ne2.

## Yugoslav vs DeepSeek Dragon (6/6 won; T21R2 mate 26)
5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Nxd4 10.Bxd4 Be6 11.Bb3 Qa5 12.O-O Rfc8 13.Rac1 Bxb3 14.axb3 a6, then Qe3, Nd5, Qxd4.
- Qa5 pins Nc3 to Qd2: never move Nc3 before Qe3 (Rac1 backs c3). Check the b3 pawn recapture before bxc4.
- T20R1: 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 h5: h6 is a hole (Bh6, Qxh6, Ng5); ...Rxe4?? fxe4 then Qh7#. T18R2: 9.Bc4 Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6 12.O-O-O; 19.g5?? (try Rdg1/Nd5). T9R2: 16.g5 Ne8?? 17.Qxh7#. T15R2: 11.Kb1 safer than Bxf6.

## Rauzer vs DeepSeek (2/2)
T8R1: 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4: traded queens on c3, won by 16.Rxd6! (mate 20).

## SF losses
- T19R2 5.Nc3 e6 (D, B for P down, SF +10): 6.Nxc6 bxc6 7.e5 Nd5 8.Bd2 Qc7 9.Nxd5 cxd5 10.Bc3 Bc5 11.Bd3? d4! 12.Bxd4?? Bxd4 (own Bd3 blocks d1-d4). Try 8.Ne4 Qc7 9.f4 or 11.Be2/Qd2. SF never converted: Kb1/Kc1, Re2, Rd1, c2 guarding Bd3.
- T7R3 Rossolimo 4.e5 Nd5 5.Nc3 Nc7 6.Bc4 e6 7.O-O Be7 8.d4 cxd4 9.Nb5 Nxb5 10.Bxb5 O-O 11.Nxd4? Nxe5: fix 4.Bxc6/O-O/c3.
- G22 7.Bc4 d6 8.Bb3 Ng4 9.Bd2?? Bxd4: f3/Qd2 BEFORE Bc4/Bb3. T6R1 16.Nd5? Bxb2 (Nc3 sole block of Bg7). G17 18.Qe2? f4! 22.Kh2?? Rxf2+.

## Rules
- Per move: what does the moved piece shield, block or defend (b2, d4, e5, f2, c4, e4, d-file)? Which pawn push/knight jump/pin comes next? Attackers v guards on each of my loose pawns.
- A 'watch' note that does not change the move is useless.
