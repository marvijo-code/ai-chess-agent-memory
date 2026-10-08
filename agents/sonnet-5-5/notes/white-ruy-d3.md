# White Ruy with 4.d3 (G5 and G8 wins vs GPT-6.1 Sol)

## G5 (Armageddon, White needs a win)
1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 Bc5 5.c3 O-O 6.O-O d6 7.Nbd2 a6 8.Ba4 b5 9.Bc2 Bb7 10.Re1 Re8 11.Nf1 d5 12.Ng3 dxe4 13.dxe4 Qxd1 14.Rxd1 Rad8 15.Be3 Bxe3 16.fxe3 Rxd1+ 17.Rxd1 Rd8 18.Rxd8+ Nxd8 19.Nxe5 Nxe4?? 20.Nxe4 Bxe4 21.Bxe4 (piece up) Ne6 22.Bd5 Kf8 23.Bxe6 fxe6 24.Kf2 ... N+6P vs 6P ending, won by king march Kf2-f3-e4-f4, h4, g3, Nf3, e4+, Ne5#.
- Sol played 19...Nxe4?? after the knight left c6. Sol is weak at counting attackers/defenders in simplified positions.
- Ending: king to the centre early, avoid Nd3 (...c4) and Nc4+ (bxc4).

## G8 (900+10, mate in 24 moves)
1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 Bc5 5.O-O O-O 6.c3 d6 7.Nbd2 a6 8.Ba4 Ba7 9.Bb3 Be6 10.h3 (stops ...Ng4/...Bg4 on f2 with Ba7) d5 11.exd5 Nxd5 12.Re1 Re8 13.Nc4 Qf6 14.Ne3 Rad8 15.Nxd5 Bxd5 16.Bxd5 Rxd5 17.Qb3 Rb5 18.Qc2 Qg6 19.Be3 Bxe3 20.Rxe3 Rd8 21.Rae1 Nd4?? 22.Nxd4 exd4 23.Re8+ Rxe8 24.Rxe8#.
- Engine marks: 14.Ne3? (ok but not best), 17.Qb3?!. Everything else fine.
- Pattern: the e-file rooks plus f7/g7/h7 pawns and Qg6 not covering e8 made a back-rank mate. Before each move check whether Black's back rank has luft (it had none) and whether Black's queen guards e8.
- Tactical cautions I tracked all game and they paid off: never Nxe5 (Nc6/Rb5/Qg6/Re8 all hit e5), ...e4 with Rd5 x-raying Qd1 (play Qe2/Qc2 first), ...Bxf2+ (Ba7 diagonal), ...Nf4 (hits d3/h3/g2).
- Sol as Black vs 4.d3: ...Bc5, O-O, d6, a6, Ba7, Be6, d5, Qf6, Rad8, Rb5, Qg6. Sol drifts into passive pieces and then blunders a tactic. Keep pieces protected, trade when safe, wait.

## Time
- G5: 4-15 s a move, finished with 10:17 left. G8: 1-8 s on book/routine moves, 40 s on key decisions (Ne3, Nxd5, Qb3); finished with 13:21 vs Sol 12:43.
