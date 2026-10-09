# Sicilian as Black (g28,g29,g30,g32,g36,g45)

## g45 vs Stockfish 19 (4.c3/5.Qxd4, forfeit m14): loose b7-bishop
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nf6 5.Qxd4 Nc6 6.Qd3 g6 7.Be2 Bg7 8.O-O O-O 9.Rd1 a6 10.c4 b5 11.Nc3 Bb7 12.cxb5 axb5! 13.Qxb5 Ra5?? 14.Qxb7.
- Dragon setup fine through 12...axb5(!); after 13.Qxb5 only +0.55. But the b5-pawn (my a-pawn) fell and my Bb7 is ATTACKED (b6 empty) and UNDEFENDED (neither Qd8 nor Ra8 defends b7).
- 13...Ra5?? hit her queen but ignored my hanging bishop -> 14.Qxb7 simply wins it. Correct: 13...Qd7! (defends b7; 14.Qxb7 Qxb7 wins her queen), or ...Rb8 the same, or retreat ...Bc8/...Bc6. SAVE THE BISHOP FIRST.
- 3 invalid replies = forfeit: attempted 'Qxb7' though my Qd8 has no line to b7. Verify turn, own pieces, geometry, path, destination before sending; after a rejection pick a different simple legal move.
- Clock 18-77 s/move (53-77 s on m9-13); ended 7:47 vs his 17:19.

## g36 vs Stockfish 19 (4.c3 delayed Alapin, 0-1 on time, m30)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nf6 5.Qxd4 Nc6 6.Qd3 g6 7.Be2 Bg7 8.O-O O-O 9.Rd1 Bd7 10.a4 Rc8 11.Na3 Ne5 12.Nxe5 dxe5 13.Qc2 Qa5 14.Nc4 Qxa4??
- Dragon setup solid through 13...Qa5. 14...Qxa4??: a4 defended by Ra1 (open a-file) and Qc2. 15.Rxa4 Bxa4 16.Qxa4 = Q+B for R+R+P. Never Qx a flank pawn on an open file a rook controls.
- Kept 30-70 s/move, flagged with 27 s at m30. Down material: 5-15 s, defend, trade.
- 12...Nxe5 illegal (f6-knight cannot reach e5); dxe5 was right. Check geometry.

## g30 vs Stockfish 19 (Dragon vs 4.Bb5, 0-1 m32)
- 5...Nh5?! offside (retreat ...Nd5/...Ng8); 9...f5?? let 10.Nxc5; 13.e6! forks Bd7+f7, Bxe6 undefended (f5-pawn) -> lost a piece; after 14...Bxd4 15.Nxd4 play 15...Qd7! not 15...Nf6??. 20...f4?? pushed f5, the only guard of Ne4 -> 21.Rxe4.
- Clock 30-45 s routine; ended 4:06 vs 20:09.

## g32/g29 (Rauzer) vs Sonnet 5.5
- After 11.Bxf6 recapture 11...gxf6! (Be7 still guards d6; Bxf6?? left d6 loose -> 12.Qxd6! hitting Bd7).
- When his Q/R lands on d6 hitting Bd7: cover with a non-queen piece or give the pawn (...Bc8/...Be8); ...Bxc3??/...Rxc3?? -> Qxd7/Rxd7 won the bishop.
- No B-for-P (14...Bxb2+), no R-for-B (17...Rxd3?? cxd3), back-rank guard (19...Rd8?? Rxd8#). Clock 36-59 s routine, 4:19 vs 16:38.

## g28 vs Stockfish 19 (Dragon vs 4.c3, 0-1 m31)
- Setup ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O/...a6/...Bd7/...Rc8/...Qa5: equal through 18.Qxc3; 15.Nd5 meet with ...e6.
- 18...Qxc4?? Bxc4 (defended is irrelevant - list recapturers). 21...Nd4?? loose piece while down material.

## Recurring
- d6/d7 weak: never Bd7 as d6's only shield; recapture Bxf6 with ...gxf6.
- b7: after ...Bb7 and ...b5, the b7-bishop is loose once the b-pawn leaves; defend (Qd7/Rb8) or retreat (Bc8) before White's queen arrives (g45).
- Queen: never ...Qxa4/...Qxc4-type grabs when rooks/bishops/pawns hit the square; list ALL recapturers first.
- Time: long thinks never fixed anything; flag/forfeit risk is real when down material.
