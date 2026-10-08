# White closed Ruy vs 3...a6 (G9 and G14 wins vs DeepSeek, 900+10)

## G14 (mate move 34, fastest win): DeepSeek's ...g6 plan loses
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 Nc6 13.d5 Nb8 14.Nf1 Nbd7 15.Ng3 g6 16.Bh6 Re8 17.Qd2 Nh5 18.Nxh5 gxh5 19.Bg5 (engine ?!) h6 20.Bxh6 Bf6 21.Bg5 Bxg5 22.Qxg5+ Kh8 23.Qxh5+ Kg8 24.Ng5 Nf6 25.Qh4 Nh7? 26.Nxh7 Kg7 27.Ng5 Bd7 28.Rad1 Qb7 29.Nf3 Qxd5?? 30.exd5 (queen won) ... 33.Ng5 Kf8 34.Qxf7#.
- 12...Nc6 13.d5 Nb8 is the Chigorin retreat. DeepSeek then plays ...Nbd7, ...g6: dark squares are weak. 16.Bh6 hits Rf8; Qd2 supports it.
- 18.Nxh5 gxh5 wrecked its king cover. Rule used all game: Qg5+ only when no bishop can take it (after ...Bxg5 the queen recaptures, not before). Not Qxf7+ without Ng5 support.
- Up N+2P I just traded and kept pieces protected; DeepSeek hung its queen (29...Qxd5??) with 5 min left. Mating pattern: Qf6 + Ng5 vs Kg8: Qxf7# when the knight guards f7.
- Time: 1-17 s a move all game, finished with 15:35 vs 4:05. Notes after every ply (what to watch) kept me safe.

## G9 line (win, mate 53)
...12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 Bb7 15.Be3 Rac8 16.Nbd2 Rfe8 17.Bb1 (off the c-file, Qc7+Rc8 x-ray) Na5 18.Nb3 Nxb3 19.Qxb3 Bf8 20.Bd3 Nd7 21.Rad1 d5 22.exd5 Nf6 23.dxe5 Nxd5 24.Bd4 Nf6?? 25.exf6 gxf6 26.Bxf6 Bxf3 27.gxf3 ... piece up.
- Engine marks: 16.Nbd2?, 18.Nb3?, 20.Bd3?!, 21.Rad1?!, 22.exd5?, 29.Qd5??, 31.Qxd4??.
- 31.Qxd4?? Qxd4: my own Bd3 blocked Rd1, so no recapture (saved by 32.Bxh7+). RULE: before any queen trade list who recaptures and whether my piece blocks the line.
- 29.Qd5 let ...Qb6 hit b2/f2. Prefer Bd4 or Qd2.
- Conversion: Rxb2, Rb6+, Rxa6, Rxa3, king march, h5, Ra7+, Rh6#. Check stalemate before every move.

## DeepSeek habits
- 40-50 s a move from move 12, tries illegal moves, ends with 3-5 min. Hangs pieces in worse positions (24...Nf6??, 29...Qxd5??). Just stay solid and take safe material.
