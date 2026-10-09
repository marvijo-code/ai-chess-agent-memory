# Sicilian Rossolimo: defender removal and queenless mate

## T6 round 2: White vs Stockfish 19, checkmate loss
1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.Nc3 Nc7 6.Bxc6 dxc6 7.O-O Bg4 8.d3 f5 9.exf6 e.p. exf6 10.Re1+ Be7 11.h3 Bh5 12.Bf4 O-O 13.Qe2 Re8 14.d4 Bf8 15.Qd2 Ne6 16.Bg3? Bxf3 17.gxf3! cxd4 18.Ne4?! f5 19.Ng5 Qxg5 20.Qxg5 Nxg5.

## Bishop retreat left the center vulnerable
Before 16.Bg3, White had Kg1/Qd2/Ra1/Re1/Bf4/Nc3/Nf3; Black had Kg8/Qd8/Ra8/Re8/Bh5/Bf8/Ne6. Black's c-pawns stood on c5/c6.
- Ne6 attacked both Bf4 and d4. Nf3 and Qd2 defended d4 against c5 and Ne6; Nc3 did not defend d4.
- Bg3 saved the attacked bishop but allowed ...Bxf3 to remove a central defender. gxf3 was marked the only good move, yet weakened the king and did not restore d4's defense.
- ...cxd4 captured the pawn and attacked Nc3. Qd2 could geometrically capture d4, but ...Ne6xd4 would then take the queen. A remaining queen defender did not make the pawn recoverable.
- Bg3 was marked a mistake; no best replacement was supplied. Evaluate the opponent's defender-removing exchange before selecting the bishop retreat.

## Queen exchange concealed a lost knight
- Ne4 escaped the d4 pawn but allowed ...f5 with another tempo. Ne4 was marked an inaccuracy.
- ...f6-f5 vacated f6 and opened Qd8-e7-f6-g5. Ng5 landed on this queen diagonal and on Ne6's capture square.
- ...Qxg5 Qxg5 Nxg5 removed both queens AND White's remaining knight. The queen recapture did not recover the knight; Black retained B+N against B, plus the extra pawn.
- Ng5 had no adverse mark. The explicit capture sequence establishes the loss independently of annotations. After each pawn move, rescan newly opened queen and bishop diagonals.

## Further material giveaways
21.Kg2 Nf7 22.Rad1 c5 23.c3 Red8 24.Re5 dxc3 25.bxc3 f4 26.Red5 fxg3 27.Kxg3.
- Re5 was on Nf7's capture square; Black chose ...dxc3 instead. This unmarked rook move was not validated by escaping capture.
- ...f4 attacked Bg3 directly along f4-g3. Red5 contested the d-file but ignored the bishop attack; ...fxg3 won it for a pawn after Kxg3.
- After this exchange, White had two rooks against two rooks, bishop, and knight. Rook activity did not constitute material recovery.

## King advance entered a complete mating net
27...Rd6 28.R5d3 Rg6+ 29.Kf4 Nd6 30.Ke5 Re8+ 31.Kd5 Rg5#.
- Final White pieces: Kd5/Rd3/Rd1; pawns a2 c3 f2 f3 h3. Black: Kg8/Re8/Rg5/Bf8/Nd6; pawns a7 b7 c5 g7 h7.
- Rg5 checked along g5-f5-e5-d5 and covered c5 after the king vacated d5. Rd3's third-rank activity could not answer this fifth-rank check.
- c4/e4 were attacked by Nd6; d4 by c5; c6 by b7. Nd6 occupied d6 and was protected by Bf8 through e7. Re8 controlled e6/e5/e4; Rg5 also controlled e5.
- Neither rook could capture Rg5 or interpose on e5/f5. All king exits were unavailable.
- Finished with about 13:37 and no illegal attempts. Familiar opening moves took 3-9 seconds; Red5 took 53 seconds yet ignored the pawn attack. Use time to test concrete captures and escape squares, rather than justify activity.
