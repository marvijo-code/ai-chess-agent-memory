# White closed Ruy vs 3...a6 (G9, G14, G15 wins vs DeepSeek, 900+10)

## Plan vs DeepSeek's Chigorin (worked in G14 and G15)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 (cxd4 13.cxd4 Nc6 14.d5 Nb8) 15.Nf1 Nbd7 16.Ng3 g6 17.Bh6 Re8 18.Qd2.
- 14.d5 Nb8 is the Chigorin retreat; DeepSeek then plays ...Nbd7, ...g6, weakening the dark squares. 17.Bh6 hits Rf8, Qd2 supports it.

## G15 (mate 34, ~15 min left vs 2:48)
...18.Qd2 Bf8 19.Bxf8 Kxf8 20.Qh6+ Kg8 21.Nh4 Kh8 22.Qd2 (Nhf5 gxf5 looked unsound; passive but fine) Nc5 23.Nf3 Bd7 24.h4 Rac8 25.h5 g5? 26.Nxg5 Nxh5? 27.Nxh5 Nxe4 28.Bxe4 Bf5 29.Bxf5 f6 30.Nxf6 (forks Re8, Bf5 hits Rc8) Re7 31.Bxc8 Qxc8 32.Ne6 Qb8 33.Qh6 Rxe6 34.Qxh7#.
- 26.Nxg5 was safe: Qd2 covered g5, e4 had Bc2/Re1/Ng3. 27.Nxh5 won a piece because Nh5 was undefended.
- Illegal try 31.Qh6: my Ng5 stood on the d2-h6 diagonal. Qh6 only became legal after the knight moved to f6/e6 (32.Ne6 opened the diagonal with tempo on the queen).
- Mating pattern: Nf6 guards h7, Qh6 threatens Qxh7# and Qg7#; Black has no luft/defender on g7.
- Time: 1-20 s per move, 35-58 s only at the captures. Watch-list after every ply kept me error-free.

## G14 (mate 34)
...16.Bh6 Re8 17.Qd2 Nh5 18.Nxh5 gxh5 19.Bg5 h6 20.Bxh6 Bf6 21.Bg5 Bxg5 22.Qxg5+ Kh8 23.Qxh5+ Kg8 24.Ng5 Nf6 25.Qh4 Nh7? 26.Nxh7 ... 29...Qxd5?? 30.exd5 ... 34.Qxf7#.
- Qg5+ only when no bishop can take it. Not Qxf7+ without Ng5 support. Qf6 + Ng5 vs Kg8: Qxf7# when the knight guards f7.

## G9 line (win, mate 53)
...12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 Bb7 15.Be3 Rac8 16.Nbd2 Rfe8 17.Bb1 (off the c-file, Qc7+Rc8 x-ray) Na5 18.Nb3 Nxb3 19.Qxb3 Bf8 20.Bd3 Nd7 21.Rad1 d5 22.exd5 Nf6 23.dxe5 Nxd5 24.Bd4 Nf6?? 25.exf6 gxf6 26.Bxf6 Bxf3 27.gxf3 ... piece up.
- Engine marks: 16.Nbd2?, 18.Nb3?, 20.Bd3?!, 21.Rad1?!, 22.exd5?, 29.Qd5??, 31.Qxd4??.
- 31.Qxd4?? Qxd4: my own Bd3 blocked Rd1, so no recapture (saved by 32.Bxh7+). RULE: before any queen trade list who recaptures and whether my piece blocks the line.
- Conversion: Rxb2, Rb6+, Rxa6, Rxa3, king march, h5, Ra7+, Rh6#. Check stalemate before every move.

## DeepSeek habits
- 40-50 s a move from move 9, tries illegal moves (up to 3), ends with 2-5 min. Hangs pieces in worse positions (24...Nf6??, 29...Qxd5??, 26...Nxh5?). Just stay solid and take safe material.
