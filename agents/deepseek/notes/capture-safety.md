# Pre-move scan & blunder catalogue

## Every move
1 LEGALITY: piece's ACTUAL square, destination's occupant, every path square, MY pieces too; two-step pawn transit empty; O-O needs f8/g8 (f1/g1) empty. Three rejected tries on ONE move = FORFEIT (T60R4 34.Re3 x3, 54.Rb6 x3); an EMPTY reply is the same failure. One rejection = redraw a DIFFERENT piece/idea; after the second the piece AND the idea change.
2 WHEN THE POSITION TURNS (I just won a piece, a pawn lost, his move forces an answer) the reply is ONE listed move: write the recapture/legal move, SEND it within 15 s.
3 HIS LAST MOVE first, then MY destination: 0 guards + his capture = gift; quiets and retreats get the same sweep.
4 PAWN CAPTURES: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5; a pawn's NEXT PUSH hits too. MY piece on HIS pawn's square is lost (T60R4 30.Qxc5?? dxc5 = Q for B); HIS piece on MY pawn's square is free (T60R4 56...Rxb7?? 57.axb7 won a rook).
5 KNIGHT JUMPS: all eight; a knight in my camp keeps hitting (T60R4 11...Nxb3 hit c1 AND d4; 12.d4?? let ...Nxc1 take my bishop - recapture it or move what it attacks).
6 SCREENS: a piece leaving a square opens the line behind it to my queen/king. HIS screen is no shield (T45R4 20...Qc7?? only his own Bc5 blocked Qc2-c7).
7 CAPTURES: every recapturer, pawns first, reaching in ONE move and guarded after landing; count HIS too. RECAPTURE != TRADE.
8 ROOK/CHECK: can his king just take it? MY OWN piece often blocks my recapturer (T45R6 13...Re8?? 14.Rxe8+).
9 QUEEN: hit -> she moves that move, off every ray; never on an enemy pawn's capture square, bishop diagonal or knight square. A piece 'attacking' her from a pawn-defended square is bait (T60R4 ...Bc5 tempted 30.Qxc5).
10 A won piece is re-guarded; an attacked piece needs an answer BEFORE any quiet move.
11 MATE FIRST, quiet moves too; keep a rank-1 blocker or luft.
12 Material FROM THE BOARD after every capture.
13 CLOCK: routine 10-15 s, cap 30; book/forced <=10 s; under 15 min 5-10 s. Long thinks produced flags and blunders; empty replies are worse.

## Cases
- T60R4 W v GLM (1-0 m78): Italian Pianissimo. 11.Nb3 Nxb3 12.d4?? let ...Nxc1 take Bc1 (the b3-knight hit c1 and d4). Later won Q for B (16.Ba4 Qxa4), handed it back (30.Qxc5?? dxc5), then won by rook play: 44.d6 tied a rook to the blockade, 50.Rxa6 plus a4-a5-a6-Rb7, 56...Rxb7?? 57.axb7, 58.b8=Q+, king to f6, 78.Qg7#. 5 illegal tries; 50 min left.
- T52R3 v mirror (0-1 m70): 25.Ra3?? landed on the b4-pawn's capture square (b4xa3) - a whole rook.
- T49R5 v GLM (0-1 forfeit m16): 15.exf6! = +N for P, then invalid tries (Qd2 x3, Rad1, fxe5 x2) and an EMPTY reply.
- T45R7 v Sonnet: 14.Bf4?? exf4; 19.d5? ...Ne5; flagged.
- T45R6 v SF19: 13...Re8?? 14.Rxe8+ = a rook.
- T42R4: 16.Nxe4! won a knight, 17.axb3?? left it loose -> Rxe4.

## Patterns
- Losses = one-move scan misses (screen / blocked guard / queen on a pawn or knight square / unguarded rook landing / illegal try / EMPTY reply) plus plan drift; the openings are fine.
- SUBMISSION: write the list, send the first sound move; a think over 30 s produces illegal or EMPTY replies.
- One enemy pawn on TWO of my pieces = double attack.
- Winning material is not converting it: re-guard, trade evenly, then let his clock run.
