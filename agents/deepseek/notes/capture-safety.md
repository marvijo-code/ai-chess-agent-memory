# Pre-move scan & blunder catalogue

## Every move
1 LEGALITY: name the piece's ACTUAL square, the destination's occupant and every path square, MY pieces too; two-step pawn transit empty; O-O needs f8/g8 (f1/g1) empty. Three rejected tries on ONE move = FORFEIT; an EMPTY reply is the same failure (T49R1 m14, T49R2 m13, T49R3, T49R4, T49R5 m16). T49R5: 4 invalid tries on book moves 10.Qd2/11.Rad1/14.fxe5 - read the square off the BOARD, not the plan. One rejection = redraw, pick a DIFFERENT piece/idea.
2 WHEN THE POSITION TURNS (I just won a piece, a pawn lost, his move forces an answer) the reply is ONE listed move: write the recapture/legal move and SEND it within 15 s. T49R5: +N for P after 15.exf6!, 52 min left, empty reply. Never re-derive from scratch.
3 HIS LAST MOVE first, then MY destination: 0 guards + his capture = gift. Quiets, retreats and 'tempo' moves get the same sweep.
4 PAWN CAPTURES (a moved pawn still attacks): g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5. A pawn's NEXT PUSH hits too.
5 KNIGHT JUMPS, all eight of every enemy knight; a central jump needs EVERY recapturer counted.
6 SCREENS: a piece leaving a square opens the line behind it onto my queen/king; walk every landing to the end. HIS screen is no shield: T45R4 20...Qc7?? only his own Bc5 blocked Qc2-c7; 21.Bxf8 and 22.Qxc7 won my queen.
7 CAPTURES: list every recapturer from the board, pawns first, each reaching in ONE move and guarded after landing; count HIS recapture too (T45R7 25.Qc3?? Rc8 recaptured).
8 ROOK/CHECK: 'can his king just take it?'; never a rook on his rook's line or where his rook captures it while MY OWN piece blocks my recapturer (T45R6 13...Re8?? 14.Rxe8+).
9 QUEEN: hit -> she moves that move, off every attacker ray; never on an enemy pawn's capture square or a bishop's diagonal.
10 A won piece must be re-guarded; an attacked piece needs an answer BEFORE any quiet move elsewhere.
11 MATE FIRST, quiet moves too; keep a rank-1 blocker or luft.
12 Material FROM THE BOARD after every capture; a recapture is not a gain.
13 CLOCK: routine 10-15 s, cap 30; book and forced recaptures <=10 s; under 15 min 5-10 s. Long thinks produced flags, blunders and forfeits; the clock is not the failure mode, empty replies are.
14 SELF-BAN: a move my note called bad is DEAD.

## Cases
- T49R5 v GLM (0-1 forfeit m16): Taimanov 6.Be2, 9.f4 b5 10.Qd2?! Bb7 11.Rad1?! d6 12.Nxc6 Bxc6 13.e5 dxe5 14.fxe5 Qc7?? 15.exf6! = +N for P. Four invalid tries on routine moves (Qd2 x3, Rad1, fxe5 x2), then an EMPTY reply while ahead. Qd2/Rad1 marked inaccurate (...b4 hits Nc3).
- T49R2 v GLM (0-1 forfeit m13): 11...c5?! 12.dxc5 Nxc5 13.Qxd5 won a pawn (d5 had only Qd8); three EMPTY replies.
- T49R1 v DeepSeek1017: Taimanov 6.Be2 level to m13; 6:07 on 12.e5, then empty replies.
- T45R7 v Sonnet: 14.Bf4?? exf4; 15.cxd4? IQP; 19.d5? ...Ne5; flagged.
- T45R3 v Haiku: same Bf4??/exf4; flagged while ahead.
- T44R5 v Sonnet: Caro 12...f6? 13.exf6 Rxf6 14.Qg3; 24.exd6 opened the g-file -> mate.
- T45R6 v SF19: 13...Re8?? 14.Rxe8+ = a whole rook.
- T42R4: 16.Nxe4! won a knight, 17.axb3?? left it loose -> Rxe4.

## Patterns
- Losses = one-move scan misses (screen / blocked guard / queen on a bishop or knight square / piece on a pawn's capture square / unguarded rook landing / illegal try / EMPTY reply) plus plan drift; the openings are fine.
- SUBMISSION: write the list, send the first sound move; a think over 30 s produces illegal or EMPTY replies.
- One enemy pawn on TWO of my pieces = double attack: count my pieces on every capture-square pair before a pawn push.
- Winning material is not converting it: re-guard, trade evenly, rook ladder, then let his clock run.
