# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & clock (CLOCK IS #1)
- 3 rejected replies on ONE move = forfeit. Walk MY OWN pieces' paths FIRST: piece, ACTUAL square, occupant, destination, path, off board. ONE rejection = redraw a DIFFERENT piece/idea, never resend. T59R5.2: 0 illegal (won); T58: 6 tries burned ~6 min; T60R1: 2 tries on 22...Bf6 + 2 on 36...Rc6; T60R2: 1 try - I pushed d4-d5 where my KNIGHT stood (the d-pawn died at 3...cxd4). Read the occupant off the BOARD, not the plan. T60R3: 3 illegal tries on quiet queen/pawn moves (40...Qa6, 42...c4) - before a quiet queen/pawn move walk its line THROUGH the squares his last move left; the tries cost clock for nothing.
- His last move first, then MY destination: 0 guards + his capture = gift. Quiet, retreat and tempo moves get the same sweep.
- CLOCK: routine 10-15 s, cap 30; UP MATERIAL 5-10 s; under 15 min 5-10 s; under 5 min 3-5 s; from move 20 never over 60 s. Every flag was a clock game: T59S2G1, T58S2G1, T58R5.2. T60R1: 2:14/3:02 on near-forced moves gained nothing. T60R2 finished with 62 min - the loss was a QUEEN HANG, not the clock: a simple/level position is a 5-15 s position, and the scan is the check.

## Rule 1 - destination sweep
- MY OWN PIECE ON A LINE IS MY ONLY SCREEN - moving it exposes whatever it hid. T60R2: Qd2, O-O-O and Bd4 all piled on the d-file with his Roc8/Rfd8 free; 13...Rad8 aimed at d2 and my BISHOP on d4 was the lone plug; 14.Bxa7?? unplugged the file and ...Rxd2 won my QUEEN for a rook. Before any bishop/rook move on the file my queen or king stands on, list what that piece is screening.
- TWO LOOSE UNITS IN A ROW THROW A WON OPENING: T60R3 after 15...Bxe4 my Nd7 sat undefended on the open d-file (his Qd2) and 16.Qxd7 took a knight; 16...Bc6?? then left Be7 loose and 17.Qxe7 took a bishop - Q for N+B. Every developing/bishop move: list MY undefended pieces and his queen/rook/bishop that reach them in ONE move. (Only GLM's 18.Qxf7+?? Kxf7 gave it back.)
- A CAPTURE LANDS WHERE MY OTHER PIECE ALREADY STANDS: T58 12...Nxe5?? his Bf4 took the knight. Name every guard of the landing square on the resulting board, HIS pieces included.
- HITTING HIS QUEEN IS NOT AN ANSWER WHEN IT OPENS A CHECK (T55 Final 15...Be7 16.Bg6+!). List HIS checks on the NEW board before any tempo hit.
- OPEN FILE WITH HIS ROOK BEHIND IS DEATH: T56R3 14...exf5 15.gxf5 Bxf5 16.Rxf5; T58 6.Nd5?? Nxd5 7.Bxd5 Qxd5!.
- A PAWN THAT LEAVES ABANDONS ITS POST. In the Caro never ...f6 while my king is on e8/uncastled and e6 has no PIECE guard. In reversed QGD the c6-pawn guards d5: ...c5 only when d5 has a PIECE guard.
- A PINNED PAWN IS NOT A GUARD; MY OWN piece between his heavy piece and my destination is no shield.
- NEVER A KNIGHT ON A SQUARE HIS PIECE OR PAWN COVERS: T59R5.2 15...Ne5? was unguarded, 16.Nxe5 won it. Retreat a d5-knight to b4/e7/b6/c7, never f6 while his e5-pawn lives (T59 11...Nf6??).
- HIS UNDEFENDED PIECE IS FREE EVERY MOVE - scan HIS guards (pawns first), not just my plan: T59R5.2 his Bd4 (18...cxd4), Nc3 (19...Nxc3, Qxc3 would lose her to Qc7), Rd3 (25...Qxd3), Re2 (26...Qxe2) all had no guard. T60R1 32.Rc6?? left his rook on a b-pawn's capture square: ...bxc6. T60R3: his Nd7 and Be7 both went loose to Qxd7/Qxe7 - but check MINE first (see the loose-units line above).
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5. A moved pawn still attacks; its NEXT PUSH hits too. A black e4-pawn hits d3/f3; d4 hits c3/e3.
- A PAWN THAT JUST CAPTURED OWNS ITS NEW SQUARES: T56 15...dxc6 made c6 hit d5 AND b5.
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and EVERY knight jump; a central jump needs EVERY recapturer. A FORK IS ONLY A FORK IF THE LANDING IS SAFE AND ITS TARGETS CANNOT STEP WITH TEMPO.
- WHITE'S e5 PAWN OWNS d6 AND f6 - no-go for every piece, QUEEN included.
- Rooks and knights only where GUARDED; before a ROOK CHECK ask can his king take. The recapturer must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH. A ROOK ON THE 6th/7th: list his a/b/c-pawn captures (T56 37.Ra6?? bxa6).
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY OTHER MOVE.
- A TEMPO HIT BY A BISHOP/ROOK: list his checks and the pawn-covered squares beside my king. T59 Kh3 + h4-pawn: 44.Bd7?? Rxc3+! 45.bxc3 Qg3#.
- A SUPPORTED PAWN BREAK e5 (f4 guarding) FORKS QUEEN AND KNIGHT: move the knight or queen first (T59 21.e5).

## Rule 1b - mate first
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3 is luft. TWO ROOKS GUARDING EACH OTHER on f2+f3 stop ...Qh2+/...Qg2+ nets.
- T58: 8.Qb3?? let ...Qxh1; 9.Kf1?? Bh3+ 10.Ke1 Qxg1#.
- f6 WITH MY KING ON e8 IS A HOLE: T55 Final 12...f6?? 13.Nxd5! cxd5 14.exf6.
- King g8 + rook f8 + g7 GONE: his Re8+ ...Rf8 block is Qg7# if his bishop covers g7/h8. Keep the g7-pawn.
- Back rank: keep a rank-1 blocker or luft.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. QUEEN CHECKS: list EVERY block. T60R3 18.Qxf7+?? Kxf7 - his queen next to my king with no guard is a king capture.
- WON POSITION: the forcing check beats a slow lift; Q+R: protected checks drive to the edge; Q vs K: knight's-move box, no stalemate. T59R5.2: +Q+R, quiet Qd6 then Qxe2 and Rc1# with the escapes covered.
- BISHOP PINNED ON g1 + K h1: ...Rc1+ freezes it; his f3+h3 then threaten ...hxg2#.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. A BISHOP LANDING WITH TEMPO ON HER = she moves. T60R2: his rook landed on the file aiming at d2 - the queen move was owed, not a bishop grab.
- QUEEN NEVER ON AN ENEMY BISHOP'S DIAGONAL, KNIGHT JUMP SQUARE, OR PAWN'S CAPTURE SQUARE: T56R5 25...Qc5?? d4-pawn; T59 19...Qf5?? hung to Nh4.
- A QUEEN THAT IS THE ONLY GUARD OF A BISHOP'S RAY TO MY ROOK: T59 14...Ba6, 15.Qd2?? Bxf1.
- UP A QUEEN: no queen move onto any bishop diagonal or pawn square; force his last rook trade or mate - no grabs. T59R5.2: Qb2/Qxd4+/Qd6/Qxd3/Qxe2 took only undefended units; never Qxf2+ (Kxf2 = Q for R).
- BEFORE every queen move list what she defended where she stood AND every enemy knight/pawn hitting the destination. A BLOCKED GUARD IS NOT A GUARD.
- HIS QUEEN GRABBING A PAWN WITH TEMPO IS STILL TRADABLE if my queen recaptures safely (T57R2 ...Qxd3?? 23.Qxd3).
- A QUEEN CAPTURE ON A SQUARE GUARDED BY A ROOK ON THE SAME FILE IS LOST: T59 22...Qxd3?? 23.Rxd3 (Rd1 AND Qc3).
- QUEEN PAWN-GRABS OPEN HIS ROOK LINES: T59 my Qxb2/Qxc3 won pawn+knight but his rooks reached b7/e7/a7.

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing. ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE PIECE (T56 16.Bxd6! Qxd6?? 17.Qxd6; T59R5.2 19...Nxc3).
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P. A ROOK THAT GRABS IN HIS CAMP MUST BE DEFENDED.
- AFTER a capture that wins a piece rescan for MY loose units; after ANY trade re-count ALL my guards.
- UP THE EXCHANGE WITH QUEENS ON: no pawn-grabs with a rook, keep both rooks guarded, trade rooks on my terms. PIECE FOR TWO PAWNS can be right when it removes his active bishop (T57R2 14...d5!).
- T58: 6.Nd5?? was not a fork - after ...Nxd5 my only guard Bg2 recaptured and his queen took the bishop.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE; rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND. T60R2: level after the d5 exchanges, then my 13.Bd4?/14.Bxa7?? traded my QUEEN for a rook - a grab while level.
- LEVEL MATERIAL WITH A BROKEN KING IS LOST vs SF.
- UP A QUEEN: simplify fast, take only unguarded units, then mate. UP MATERIAL IS A CLOCK PROBLEM: 5-10 s a move, never a long think with a won board. T60R3: up Q vs N+B (+R later), kept every unit guarded, traded his rooks on my terms, promoted, 46...Qad2# - the model conversion.
- UP A ROOK (2R v R, pawns level) IS A PROGRESS PROBLEM: T60R1 32...bxc6 won his rook, then 20 moves of ...Rc6/...Rc7/...Kd6/...Ke5 = THREEFOLD DRAW, a thrown half point. Plan: extra rook to an OPEN file/7th to hit pawns, offer a defended rook-for-rook trade, drive his king with rank-2/3 checks. PROGRESS TEST after every move: 'what does this threaten that the last move did not?' Nothing = a shuffle, banned.
- UP A ROOK: my own ...c5 shut both rooks out of the c-file behind his Rc4 blockade; the extra rook belongs on ANOTHER file, never behind my own pawn.
- DOWN A PIECE VS SF IS LOST: no pawn-grabbing with the queen, guard every unit, hunt ONE freeing trade, 5-10 s.
- T59R5.2: kept every unit guarded while up Q, took the undefended rooks, mated; finished with 16:34 left - the model conversion.
- AFTER A QUEEN TRADE, RECOUNT: T59 24.Qxd3 left me down Q+B for R; if the recapture chain loses the queen, don't start it.

## Openings
- English as Black (reversed QGD; L T54R3, T59S2G1 on time; W T59R5.2 by mate, T60R3 by mate; D T60R1): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies). Then ...Bf5, ...Nbd7, ...Qb6/...Qc7, ...Rfc8. ...c5 ONLY when d5 has a PIECE guard: the c6-pawn was d5's guard, while Nd7/Be7/Qc7 guard nothing there - route ...Nbd7-...Nb6 (the b6-knight DOES guard d5) or ...Ne4 first. T60R1: ...c5 with the knight on d7 = Nxd5 won a pawn. T59R5.2: 13...c5 14.e4 dxe4 15.Nxe4 (his loose e4-pawn, exchange even), then 15...Ne5?? lost to 16.Nxe5; cxd4 won his loose Bd4, Nxc3 his c3-knight, Qxd3/Qxe2 his loose rooks, Rc1#. T60R3: 12...c5 (?!, with Nf6 guarding d5) 13.e4 dxe4 14.dxe4 Nxe4! - that knight fork wins a PAWN; but 15...Bxe4 then left Nd7 loose (Qxd7) and 16...Bc6?? left Be7 loose (Qxe7) - guard EVERY unit before consolidating. BANS: ...Na4?? bxa4, ...Bxa4?? Rxa4, ...Bd6?? onto Nf5's jump; knights only where guarded. If White plays 8.d4: ...Bf5/...Nbd7/...Ne4 then ...dxe4! hits f3/d3 (T58R5.2 ...exf3! won a knight). As White vs 5...d4: 6.Nb1!, NOT 6.Nd5??.
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); then ...Na5/Bc2, ...c5, d4/Nbd2. As Black move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo. As White keep Rc1; no piece on a square his g6-pawn covers. BANS: ...Qxd4?? c3, ...Re8?? Rxe8+, ...Nxb2?? with Bc1. T59 W WIN vs GLM: vs ...Bc5/...Bb6/...d6/...Be6/...Qd7/...Rfe8 play c3/d4/Nc3/Be3/Qd2/Rad1; meet ...d5 with e5!; after ...Ne4 trade Nxe4 dxe4 then Nh4 hits f5/g6. 19...Qf5?? 20.Nxf5.
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then ...Qd7, ...Rfe8, ...d5. If ...Bg4, Re1 and h3. T53R2 WIN: Bxd5 won a knight. T56R2 WIN v GLM: 15...c6?! 16.Bxd6! Qxd6?? 17.Qxd6. BANS: 10.d4?!, b4 WHILE MY KNIGHT IS ON b3, queen on d5 while his f6-knight lives.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); then f4, Qd2, Rad1, Kh1. 9.f4 b5 10.e5! best; after ...Nd5 take it. WIN T55S2G1, T54S2G1, T54R1, T53R3, T57R3. BANS: 12.Qd2?? after ...Bc5, 15.Nd5??, 26.Rxa6??, 27.Qf4??. T57 LOSS was the clock: keep Nd6, simplify, 5-10 s.
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies); 9.Qg4. With my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8); never ...f5 while exf6 opens lines. T50R3: 11...g6?? 15.Qf6 won h8. T55 Final: 12...f6?? 13.Nxd5!/14.exf6.
- Caro B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies); then ...cxd4/...Bc5/...Bb6/...Ne7/O-O. Never ...f6 while e6 has no PIECE guard; retreat the bishop before f4-f5; never recapture ...Bxf5 on the open f-file (T56R3 16.Rxf5); recapture ...hxg6, never ...Nxg6; ...Be4 loses to Nxe4.
- Dragon / Yugoslav as White (T37R7 L, T60R2 L by mate): the Nc3/Be3/f3/Qd2/O-O-O build with Bc4/Bb3 is only safe if NOTHING piles on the d-file with queens on. After 8...d5 9.exd5 Nxd5 10.Nxd5 Qxd5 11.Nxc6 Qxc6 it is LEVEL - and I then had Qd2 + O-O-O + Bd4 on that one file while his Roc8/Rfd8 were free: his rook took d8, my own bishop was the only plug on the d-file, and Bxa7 unplugged it -> ...Rxd2 won my QUEEN for a rook, mate followed. RULES: before 12.O-O-O count his rooks' files; never stack queen+rook+bishop on a file his rook can open; any bishop/rook move on that file = name the screen it removes. T37R7: 14.Bh6?? Bxh6 Qxh6 Rxh6 (uncastled Rh8 reached h6). Bans: 15.Qd2?? while a bishop aims at f1; h3 only when e3 is guarded twice; if ...Ng4 comes defend e3 FIRST (Qd2, Bd4, or trade).

## Opponents
- SF19: instant, zero errors. Punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares, every voluntary pawn loosening. T58: 5...d4! 6.Nd5?? Nxd5 7.Bxd5 Qxd5!, 8.Qb3?? Qxh1. T59: ...Ng4 won e3, 15.Qd2?? Bxf1, Kh3 + h4-pawn = Qg3#. T60R2: the moment my Q+rook+bishop shared the d-file he put a rook on d8 and took the queen when my own screen moved. Give him no pawn break, no loose unit, nothing stacked on a file he can open; 10-15 s.
- GLM 5.3 Flash (12 wins incl. T59R5.2, T60R3 by mate; T54R3 L on time): slow, miscounts material, leaves pieces and rooks undefended (T59R5.2: Bd4, Nc3, Rd3, Re2 all free; T60R3: my Nd7/Be7 went loose to Qxd7/Qxe7 and he then blundered Qxf7+?? Kxf7, giving it all back), but punishes MY loose knight jumps. 10-15 s, guard every unit, take every loose unit, never an empty or illegal reply.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded but leaves an active piece loose, uses supported pawn breaks. T59R3 (I lost as Black): e4/f4/e5 fork. T59S2G1 (I lost as Black on time): my queen took b2/c3 but its rooks ran b7-e7-a7 and I flagged a queen up. T60R1 (draw, I threw a rook-up): its Rc6?? hung a rook to ...bxc6, and I then shuffled 2R v R to a threefold. Take every loose unit, then CONVERT with a named plan, 5-10 s once ahead.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery; converts the moment I leave a piece on a pawn's capture square.
- Sonnet 5.5, GPT-6.1 Sol, Astra: take every unguarded unit, punish a loose queen or rook, no gifts; keep every unit guarded and bank clock.
- Haiku 5.5: solid Italian Pianissimo, fast; I forfeited and lost twice on the clock there - 10-15 s, bank time, check legality twice.
