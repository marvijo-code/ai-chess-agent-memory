# Sicilian as Black (g28,g29,g30,g32,g36)

## g36 vs Stockfish 19 (4.c3 delayed Alapin, 0-1 on time, m30)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nf6 5.Qxd4 Nc6 6.Qd3 g6 7.Be2 Bg7 8.O-O O-O 9.Rd1 Bd7 10.a4 Rc8 11.Na3 Ne5 12.Nxe5 dxe5 13.Qc2 Qa5 14.Nc4 Qxa4??
- Dragon setup solid; roughly equal through 13...Qa5 (hits a4 and c3). 11...Ne5 is protected by d6 and fine.
- 14...Qxa4??: a4 was DEFENDED by Ra1 (a-file open - White's a-pawn on a4, a2/a3 empty) and by Qc2. 15.Rxa4 Bxa4 16.Qxa4 wins the bishop too: Black gave Q+B for R+R+P (eval +8). Bd7 'defends' a4 only by recapturing after the queen is gone. Never Qx(flank pawn) on an open file an enemy rook controls.
- After that I was lost but kept 30-70s/move and flagged with 27s left at move 30. Down material: 5-15s/move, defend, trade, never a new loose piece.
- 1 illegal try: 12...Nxe5 (f6-knight cannot reach e5); the pawn recapture dxe5 was correct. Check geometry before sending.

## g30 vs Stockfish 19 (Dragon vs 4.Bb5, 0-1 m32)
- 5...Nh5?! offside; retreat ...Nd5/...Ng8. 9...f5?? let 10.Nxc5 win a pawn - guard c5 or don't kick the knight.
- 13.e6! forks Bd7+f7; 13...Bxe6 had NO defender (f5-pawn, Qe8 blocked by e7) -> 14.Nbd4/16.Nxe6 won a piece. Alternatives ...Bc8/...Ba4; after 14...Bxd4 15.Nxd4 play 15...Qd7! not 15...Nf6??.
- 20...f4?? pushed f5, the only defender of Ne4 -> 21.Rxe4. Never push a pawn that guards my piece.
- Clock 30-45s on routine moves; ended 4:06 vs 20:09.

## g32/g29 (Rauzer) vs Sonnet 5.5
- After 9...Nxd4 10.Qxd4 11.Bxf6 recapture 11...gxf6! - Be7 still guards d6 (12.Qxd6?? Bxd6 wins the queen). Bxf6?? left d6 loose (Qd8 blocked by Bd7) and 12.Qxd6! hit Bd7 (defended only by Qd8, Rd1 behind).
- If White's Q/R lands on d6 hitting Bd7: fix d7 with a non-queen piece or give the pawn (...Bc8/...Be8). g32 12...Bxc3?? 13.Qxd7! Qxd7 14.Rxd7 won the bishop; g29 16...Rxc3?? 17.Rxd7 the same.
- Down material trade like for like: g32 14...Bxb2+ = B for P; 17...Rxd3?? cxd3 = R for B. g29 19...Rd8?? -> 20.Rxd8# (king g8, no luft): keep a back-rank guard or make luft.
- Clock 36-59s on moves 8-18, ended 4:19 vs 16:38.

## g28 vs Stockfish 19 (Dragon vs 4.c3, 0-1 m31)
- ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O then ...a6, ...Nd7-...Nc5, ...Bd7, ...Rc8, ...Qa5: sound, equal through 18.Qxc3. 15.Nd5 meet with ...e6.
- 18...Qxc4?? Bxc4 took the QUEEN ('defended' is irrelevant: check all enemy recapturers). 21...Nd4??: piece onto an attacked, undefended square while down material.

## Recurring
- d6/d7 is the weak point: don't let Bd7 be the only shield of d6; recapture Bxf6 with ...gxf6.
- Queen: never ...Qxa4/...Qxc4 when rooks/bishops hit the square; list all enemy recapturers first.
- Time: long thinks never fixed anything; flag risk is real when down material.
