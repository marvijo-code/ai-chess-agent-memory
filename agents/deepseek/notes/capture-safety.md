# Pre-move scan & blunder catalogue

## Every move
1 LEGALITY: name the destination's occupant and every path square, MY pieces too; two-step pawn transit empty; O-O needs f1/g1 (f8/g8) empty; after O-O-O my king is on c8. Three rejected tries on ONE move = FORFEIT. One rejection = redraw, pick a DIFFERENT piece/idea.
2 HIS LAST MOVE first, then MY destination: 0 guards + his capture = gift. Quiets, retreats and 'tempo' moves get the same sweep.
3 PAWN CAPTURES (a moved pawn still attacks): g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5. A pawn's NEXT PUSH hits too: a queen on c3 with ...b4 available.
4 KNIGHT JUMPS, all eight of every enemy knight; a central jump needs EVERY recapturer counted.
5 SCREENS: a piece leaving a square opens the line behind it onto my queen/king; walk every landing to the end. HIS screen is no shield: T45R4 20...Qc7?? only his own Bc5 blocked Qc2-c7; 21.Bxf8 and 22.Qxc7 won my queen.
6 CAPTURES: list every recapturer from the board, pawns first, each reaching in ONE move and guarded after landing; count HIS recapture too (T45R7 25.Qc3?? invited ...c4 but Rc8 recaptured).
7 ROOK/CHECK: 'can his king just take it?'; never a rook on his rook's line or where his rook captures it while MY OWN piece blocks my recapturer (T45R6 13...Re8?? 14.Rxe8+).
8 QUEEN: hit -> she moves that move, off every attacker ray; never on an enemy pawn's capture square or a bishop's diagonal.
9 A won piece must be re-guarded; an attacked piece needs an answer BEFORE any quiet move elsewhere.
10 MATE FIRST, quiet moves too; keep a rank-1 blocker or luft.
11 Material FROM THE BOARD after every capture; a recapture is not a gain.
12 CLOCK: routine 10-15 s, cap 30; book and forced recaptures <=10 s; under 15 min 5-10 s. Long thinks never saved a move and produced flags, blunders and forfeits.
13 SELF-BAN: a move my note called bad is DEAD.

## Cases
- T49R1 v DeepSeek1017: Taimanov 6.Be2 was level to m13; 6:07 on the routine 12.e5, then 3 attempts returned NO move = forfeit. Routine moves get routine time.
- T45R7 v Sonnet (0-1 on time): 14.Bf4?? onto his e5-pawn's capture square -> exf4; 15.cxd4? IQP; 19.d5? gave ...Ne5 with tempo; flagged 2:20 vs 49:40.
- T45R3 v Haiku: the same Bf4??/exf4; flagged while ahead.
- T44R5 v Sonnet: Caro 12...f6? 13.exf6 Rxf6 14.Qg3; 21...e5?? 22.fxe5; 24.exd6 opened the g-file -> mate.
- T45R6 v SF19: 13...Re8?? 14.Rxe8+ = a whole rook.
- T42R4: 16.Nxe4! won a knight, 17.axb3?? left it loose -> Rxe4.

## Patterns
- Losses = one-move scan misses (screen / blocked guard / queen on a bishop or knight square / piece on a pawn's capture square / unguarded rook landing / illegal try) plus plan drift; the openings are fine.
- CLOCK IS MY BIGGEST LOSS MODE: flags, illegal tries and one empty-reply forfeit. The written list is the check and it is faster than thinking.
- One enemy pawn on TWO of my pieces = double attack: count my pieces on every capture-square pair before a pawn push.
- Winning material is not converting it: re-guard, trade evenly, rook ladder, then let his clock run.
