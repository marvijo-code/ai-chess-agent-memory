# DeepSeek V4.1 Flash: tactics and conversion

Wins and opponent explanations do not validate my moves. Maintain an independent material inventory. Shared Chigorin opening is in notes/ruy-lopez.md.

## T10 round 1: White, checkmate win
Shared Chigorin through 13...Nc6, then 14.Nf1 Bb7 15.d5 Na5 16.Ng3 Rfe8 17.Be3 Bc8 18.Rc1 Nc4 19.Bb3 Nb6 20.Rxc7.
- Rc1/Qc7 initially had TWO screens: White Bc2 and Black Nc4. Bb3 attacked Nc4 and removed my screen. ...Nb6 removed Black's screen, allowing Rxc7 to win the queen outright, with no rook recapture.
- Nc4 was pinned to the queen only in a material sense; it could legally move. The bishop attack did not force Black's losing retreat. No engine analysis established the best defense or validated the preceding play.
- ...Na5 did not attack Bc2: its destinations include b3/c4, not c2. Enumerate actual attacks instead of trusting move commentary.
- 21.Qd3 Na4 22.Bxa4 bxa4 exchanged bishop for knight. 23.Rec1 doubled rooks. 24.Nf5 Nb6 25.Bxb6 Bxf5 26.exf5 won the other knight while exchanging my other knight for Bc8. White retained Q+2R+B+N against 2R+B.
- 26...Rac8 27.Rxc8 Rxc8 28.Rxc8 exchanged ONE White rook for BOTH Black rooks. The rear rook supplied the final recapture; the net gain was one rook, not two free rooks.
- 28...e4 attacked Qd3/Nf3, but Qxe4 removed the forking pawn safely. Continue scanning threats even with an overwhelming advantage.
- Finish: 29...h6 30.Qe8 Kh7 31.Qxf8 g6 32.Qh8#. Rc8 protected the queen along the eighth rank. ...Kh7 released Bf8's pin, and Qxf8 was not check. Before ...g6, Qh8+ allowed Kg6; ...g6 occupied that escape square. At mate Qh8 covered g7/g8, while Black's h6/g6 pawns blocked the remaining escapes.
- Finished with 13:42 and no illegal attempts. Familiar development took 3-8 seconds; Bb3 took 37. Routine conversion sometimes took 20-42 seconds despite simple material superiority.

## T9 round 3: White, checkmate win
13...Bd7 14.Nf1 Rac8 15.Ng3 Rfe8 16.Bd3 h6 17.Be3 Nb7 18.Rc1 Qxc1 19.Bxc1 Rxc1 20.Qxc1.
- Unlike T10, Black's knight stayed on a5, leaving the c-file clear above Bc2. After ...Rac8, ...Qxc2 Qxc2 Rxc2 could win Bc2. Ng3 ignored this threat; Bd3 later saved the bishop after Black missed it.
- Once Bd3 and ...Nb7 cleared the file, Rc1 attacked Qc7. ...Qxc1 miscounted: Bxc1 absorbed ...Rxc1, preserving Qd1 for Qxc1. Black gave Q+R for R+B.
- 20...Nc5 21.dxc5 dxc5 22.Nxe5 Nxe4 23.Nxe4 Bg5 24.Nxg5 hxg5 25.Nxd7 Re7 26.Rxe7 removed Black's remaining pieces. Nxe4/Nxg5 used Ng3; Nxd7 used Ne5. Track each knight separately.
- 26...g6 27.Re8+ Kg7 28.Qc3+ Kh7 29.Rh8#: Qc3 protected h8 through d4/e5/f6/g7 and covered g7; Bd3 covered h7.
- Ng3 was marked a blunder. Finished with 13:37; the missed capture, not time shortage, was the lesson.

## T8: Black, two checkmate wins
- Third place: ...Nc4 Nxc4 Qxc4 Be3 Rfe8 Qd2 Bxe4 Bxe4 Nxe4 dxe5 Nxd2. ...Nc4 was inaccurate; ...Rfe8/...Bxe4 were blunders. White ignoring Nxe4's queen attack did not validate the combination. Be3 screened Re1, but Nf3 still defended e4.
- Later ...Qd5 Nf3 dxe5 Nxe5 Qxe5 Bd4 Qxd4 exploited loose pieces. ...Rc2 protected Qxf2+/Qxg2# along the second rank; Rac1's rook attack could not answer check.
- Round 3: ...Qc7 supported e5. Nxd6 Bxd6 Nxe5 Bxe5 Bxe5 Qxe5 gained two minor pieces for a pawn; Bb2xe5 cleared Qc7-d6-e5.

## Earlier recurring failures
- Nf3-f1 abandoned e4. ...Qc6 dxc6 Bxc6 lost queen for pawn; flagging did not repair the play.
- dxc5 opened Qc7-d6-e5. Rxe5 Bxe5 Nxe5 Rxe5 traded rook and knight for bishop and pawn. Qd4 cxd4 lost the queen before any rook retreat.
- Bf8 abandoned Nf6. Rec8 defended Rc4. Bxc5 dxc5 opened Bb7's diagonal for Qd5 Bxd5.
- Qg3+ fxg3 and Kf1 Qf3+ gxf3 lost queens. Refresh pins after king moves.
- Nb4 Bd3 Nxd3 Qe2 Nxe1 worked because Nd2 blocked Qd1xd3. Nc4 allowed bxc4; Qb3 allowed cxb3.
- Bd4+ allowed Kxd4; Qe3+ allowed fxe3; Bd6+ abandoned Nh4 to Kxh4. Checks do not ensure safety.
