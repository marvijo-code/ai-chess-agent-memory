# Pre-move scan & blunder catalogue

## Every move
1. LEGALITY, my pieces included: name the destination's occupant and each path square (T44R3 'b4': own knight on b3 = 3rd rejection = FORFEIT; T45R4 illegal Rxa8+; T45R7 two rejected tries on 20.Nbd4 and two on 22.Qd3 = four clock-burners). Two-step pawn: transit square empty. O-O needs f1/g1 (f8/g8) empty; after O-O-O my king is on c8. After ONE rejection redraw, pick a DIFFERENT piece.
2. His LAST move first, then MY destination: 0 guards + his capture = gift. Quiet, retreat and 'tempo' moves get the SAME sweep.
3. Enemy pawn captures: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-g6/e6, f6<-e5, g5<-h6. A moved pawn still attacks there; a piece on his pawn's capture square is FREE (T45R3 14.Bf4?? exf4). A pawn's next PUSH also hits: a queen on c3 with ...b4 available is a tempo target (T45R7).
4. Enemy knight jumps, all eight: f6 d5/d7/e4/e8/g4/g8/h5/h7; f5 d4/d6/e3/e7/g3/g7/h4/h6.
5. Screens: a piece leaving a square opens the line behind it onto my queen/king; a retreat landing on a diagonal must be walked to the end. HIS screener is no guard: T45R4 20...Qc7?? - his Bc5 was the only blocker of Qc2-c7; 21.Bxf8 opened the file and 22.Qxc7 won her.
6. Captures: list EVERY recapturer, pawns first; it must LAND there in ONE move, not be the attacked piece, and stay guarded after landing. Count HIS recapture too: T45R7 25.Qc3?? invited ...c4 but Rc8 recaptured.
7. Rook or check: 'can his king just take it?'; list every reply, captures of the checker included. NEVER a rook on a file/rank his rook holds unless the landing square is guarded: T45R6 13...Re8?? 14.Rxe8+ = a whole rook (my own Bc8 blocked Ra8).
8. Queen hit -> she moves that move, off every attacker ray; never on an enemy pawn's capture square or a bishop's diagonal.
9. A won piece must be re-guarded; an attacked piece needs an answer BEFORE any quiet move elsewhere.
10. MATE FIRST, quiet moves too; keep a rank-1 blocker or luft.
11. Material FROM THE BOARD after every capture; a recapture is not a gain.
12. Clock: routine 10-15 s, cap 30; BOOK AND FORCED RECAPTURES <=10 s; under 15 min 5-10 s. T45R7 flagged with 2:20 vs 49:40: 8:13 on 11.h3, 7:48 on Nbd4, 7:33 on Qd3 (illegal tries on both), 4:21 on Qd3 - all routine. A think over 30 s = STOP, write the list, play the first sound move. T45R6 also burned 90 s on 6...Nxd5 and hung a rook.
13. SELF-BAN: a move my note called bad is DEAD.

## Cases
- T45R7 vs Sonnet (0-1 on time): Giuoco Pianissimo; level to ~m19, then 15.cxd4? IQP his ...Rad8 hit, 16.Be3? Nxe3 17.fxe3 doubled my pawns, 19.d5? gave ...Ne5/Nxf3 with tempo; Qd3-Qc3-Qe3-Qd3 shuffles invited ...b5-...b4; flagged.
- T45R6 vs SF19 (0-1): Four Knights 4...Bb4; level to m13, then 13...Re8?? facing his Rfe1 - Rxe8+ won a WHOLE ROOK; mated m35.
- T45R4 vs GLM (won on his flag): English; 13...Ne5?? 14.Nxe5 Qxe5 15.f4! Qe6 16.Ba3 made c5 loose; 20...Qc7?? lost my queen (item 5). Rook on the 7th + Kd7-Kc6 = his flag.
- T45R3 vs Haiku (0-1 on time): 14.Bf4?? onto his e5-pawn's capture square -> exf4 won a bishop; 9:44 on 34.b3 then flagged while ahead.
- T44R5 vs Sonnet (0-1): Caro Advance; 12...f6? 13.exf6 Rxf6 14.Qg3; 21...e5?? 22.fxe5; 23.Rxf6 gxf6 24.exd6 opened the g-file -> Qxg8#.
- T42R4 vs Sol: 16.Nxe4! won a knight, 17.axb3?? left it loose -> Rxe4; 18.Ne5?? dxe5.

## Patterns
- Losses = one-move scan misses (screen / blocked guard / queen on a bishop or knight square / piece on a pawn's capture square / unguarded rook landing / wrong recapturer / illegal try) plus plan drift; the openings are fine.
- CLOCK IS MY BIGGEST LOSS MODE: T45 flags in R1, R3, R7. Long thinks never saved a move and repeatedly produced simple blunders. The written list is the check.
- One enemy pawn on TWO of my pieces = double attack: count my pieces on every capture-square pair before a pawn push.
- Winning material is not converting it: re-guard, trade evenly, rook ladder, then let his clock run.
