# Black vs 1.e4 e5 2.Nf3 Nc6 3.Nc3 (Stockfish 19 plays this as White every time)

## G7: 3...Bc5 (draw by repetition, but I was a piece down from move 9)
3...Bc5 4.Nxe5 Nxe5 5.d4 Bd6 6.dxe5 Bxe5 7.Bd3 Nf6 8.Ne2 d6?? 9.f4! Bc3+ 10.bxc3 (eval +6.9) O-O 11.h3 Re8 12.O-O Be6 13.e5 ... lost piece, then 47...Ra6?? lost more. Stockfish later repeated moves and drew at move 69.
- Mistake: 8...d6 filled the d6 retreat square. After f4 the Be5 can go only to d4 (Nxd4) or c3 (bxc3). I wrote 'if f4 Bxc3+' in my own plan but did not check it was bad, and spent only 12 s.
- Ideas for next time (unverified, check each): (a) 7...Nf6 8.Ne2 O-O 9.f4 Bd6 (d6 free; then 10.e5 Be7 or Bxe5 11.fxe5 Ng4); (b) 7...Bxc3+ 8.bxc3 d6/Nf6 (gives up the bishop pair but White's c-pawns are doubled and nothing hangs); (c) 4.Nxe5 Nxe5 5.d4 Bd6 6.dxe5 Bxe5 is fine (engine marks !); the problem is only move 8. Also consider 7...d6 only if f4 can be met by Bd4/Bf6 - not possible, so skip it.
- Opening rule: when a bishop sits on e5 or d4 in the centre, castle (or put it back to d6) before playing ...d6.

## G6: 3...Nf6 4.Bb5 Bb4 (0-1 in 25)
4...Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 bxc6? 10.d4 Qe8 11.a3 Bd6 12.Bd2 Bb7 13.Bd3 Qe6 14.c4 Rae8?! 15.Rae1 Qf6 16.Qxf6 gxf6 17.c5 Be7? 18.Re3 d6 19.Rfe1 Bd8 20.Rxe8 Be7 21.Rxf8+ Kxf8 22.cxd6 Bxd6 23.Bh6+ Kg8 24.Re8+ Bf8 25.Rxf8#.
Eval: +0.5 after 10.d4, +2 after 12.Bd2, +3 after 14.c4, +5 after 17.c5.
- 9...bxc6 gave White 10.d4 with a big centre, and Bb4 loose. My prep line was 9...dxc6 10.Bxc6 Rb8 (check tricks on c6/f6 before playing).
- Moves 10-14 were reactive and each lost a tempo; queen on e6 facing Re1 is bad. 16...gxf6 broke my king cover. Alternatives: 15...Qd7/Qg6 (keep queens on), 17...Bf8.
- Next time: avoid 3...Nf6 4.Bb5 Bb4 unless I know 6.Nd5; try 4...Nd4 (Spanish Four Knights) or 3...Bc5/3...Bb4 with the safety rules above.

## General
- Keep king pawns intact (no ...gxf6). Develop with ...d6 only after bishop safety is checked, ...Re8 only when e-file tactics are counted.
- Use time at moves 6-12 and when a pawn attacks a piece. In G6 I kept 13 min unused; in G7 I spent time only after the position was already lost.
