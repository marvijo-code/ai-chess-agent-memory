# White closed Ruy vs 3...a6 (G9 win vs DeepSeek, 900+10, mate move 53)

## Line played (all book, 1-6 s each)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 Bb7 15.Be3 Rac8 16.Nbd2 Rfe8 17.Bb1 (off the c-file, Qc7+Rc8 x-ray) Na5 18.Nb3 Nxb3 19.Qxb3 Bf8 20.Bd3 Nd7 21.Rad1 d5 22.exd5 Nf6 23.dxe5 Nxd5 24.Bd4 Nf6?? (DeepSeek tried an illegal Bxd5 first) 25.exf6 gxf6 26.Bxf6 Bxf3 27.gxf3 ... piece up.

## Engine marks on my moves
16.Nbd2?, 18.Nb3?, 20.Bd3?!, 21.Rad1?!, 22.exd5?, 24.Bd4?!: the middlegame was loose. 29.Qd5?? and 31.Qxd4?? were big errors.
- 31.Qxd4?? Qxd4: my own Bd3 blocked Rd1, so I could not recapture. 32.Bxh7+! Kxh7 33.Rxd4 got the queen back (luck, not calculation).
- RULE: before any queen trade or capture, list who recaptures and check that none of my pieces blocks the recapturing line. With a piece up, prefer simple trades (Bxd4 first, or Rxd4).
- 29.Qd5 let ...Qb6 hit b2/f2. Prefer Bd4 or Qd2 first.

## Conversion (rook vs pawns)
- 36.Rxb2 won the rook after 35...Rxb2??. Then Rb6+, Rxa6, Rxa3, king march Kg3-f4xf5, h5, Ra7+, Kf7, f4, Ra6, Rh6#.
- Check stalemate before every move. Keep the rook cutting off the king on a rank or file, with my king on f6/f7/g6.

## Time
I used 1-10 s on book moves and ~40 s on key decisions, and finished with 11:41 vs DeepSeek's 3:18. DeepSeek spends 40-50 s per move from move 14 and tries illegal moves.
