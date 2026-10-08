# White closed Ruy vs 3...a6 (wins: DeepSeek G9, G14, G15, G19, G20, T5R3; Sol T5 SF2G1)

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3. Black picks Chigorin (9...Na5) or Breyer (9...Nb8).

## Chigorin: 9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 Bb7 15.Bd3! Rac8 16.Be3
- 15.Bd3 (not Nbd2, which blocks Qd1 and lets ...exd4 win a piece) leaves the c-file; Nb3+Nf3 guard d4.
- T5R3 vs DeepSeek (mate 34): 16...a5 17.Nbd2?! b4 18.d5! Nd7 19.dxc6 won a piece. ...a5/...b4 let d5 hit Nc6.
- SF2G1 vs Sol (mate 56): 16...Rfe8 17.Qd2?? (engine mark) d5 18.exd5 Nxd5 19.dxe5?! Nxe3?? 20.Qxe3 Nxe5?? 21.Nxe5 Bc5 22.Qxc5 Qxc5 23.Nxc5 Rxc5 24.Ng4: a knight up. Sol had played ...Rac8/...Rfe8/...d5 aiming at the c- and e-files.
  - Before 17.Qd2 check ...d5 and ...Nxe4 tricks (Qd2 sits on the d-file with Bd3, Be3, Nb3 stacked); the engine disliked it. Untested alternatives: 17.Rc1 / 17.Qe2 / 17.a4 / 17.Bb1 (list ...d5 replies first).
  - Sol grabbed a pawn it could not hold: it blundered under tactical tension. Keep the tension and count attackers on e5 and e3.
- Conversion SF2G1: trade rooks when a knight up. 33.Rb3?? was marked a blunder (check Rxe3 / Rc3 ideas), but Sol answered 33...Rc1+?? and lost a rook. Then the endgame: avoid Rxg5+ when Kxg5 recaptures, avoid Rxb5 when axb5, push the a-pawn to a8=Q, mate with Q+R+N (Ne6, Qg8+, Rh4#). Stalemate check every ply. Clock stayed ~14 min.
- Illegal move: Rb6 from b1 with Black pawn on b5 in the way. Trace the path square by square.
- G20 (mate 41): 13...Bb7 14.Nf1 Rac8 15.Ng3?? Rfe8 16.d5?? Nc4 17.b3 Nb6 18.Bd3 Nc4? 19.bxc4. Vs Rac8+Qc7 hitting Bc2 play 15.Bb1 (as G9) or Nb3/Rc1; do not close with d5 unless a knight is hit.
- G15/G14 (mate 34): 16.Ng3 g6 17.Bh6 Re8 18.Qd2 (Bf8 or Nh5) ... Qh6 threatens Qxh7#/Qg7#.
- G9 (mate 53): 31.Qxd4?? Qxd4 because my Bd3 blocked Rd1. Name the recapturer and its path before a queen trade.

## Breyer (G19, mate 34)
9...Nb8 10.Bc2 Nbd7 11.d4 Bb7 12.Nbd2 Re8 13.Nf1 Bf8 14.Ng3 g6 15.a4 bxa4 16.Bxa4 (pins Nd7) c5?! 17.d5?! Nb6? 18.Bxe8 Qxe8 19.Be3 ... 33.Rxf7 Kh8 34.Rf8#. 33.Qxf7+ was ILLEGAL (own Re7 in the way).

## Habits
- DeepSeek: 35-60 s a move from move 9, hangs pieces when worse, tries illegal recaptures.
- Sol (as Black): 3-30 s a move, Chigorin, plays ...d5 around move 17, falls for exchanges on e3/e5.
- Me: 1-10 s on book moves, 20-60 s at captures and queen moves.
