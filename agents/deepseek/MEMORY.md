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
- 3 rejected replies on ONE move = forfeit. Walk MY OWN pieces' paths FIRST: piece, ACTUAL square, occupant, destination, path, off board. ONE rejection = redraw a DIFFERENT piece/idea, never resend. T60F: 4 illegal tries, every one a redraw of the SAME idea. T61R1: 3 invalid (a 2nd try needed on 14...dxe4, 15...Nc4, 26...Bh5) - each burns clock and the 3rd forfeits. T59R5.2: 0 illegal (won); T58: 6 tries burned ~6 min; T60R2: pushed d4-d5 where my own KNIGHT stood. Read the occupant off the BOARD, not the plan.
- His last move first, then MY destination: 0 guards + his capture = gift. Quiet, retreat and tempo moves get the same sweep.
- CLOCK: routine 10-15 s, cap 30; UP MATERIAL 5-10 s; under 15 min 5-10 s; under 5 min 3-5 s; from move 20 never over 60 s. Every flag was a clock game. T60R2: a loss was a QUEEN HANG, not the clock - a simple/level position is a 5-15 s position, and the written list is the check.

## Rule 1 - destination sweep
- LIST HIS PAWNS' CAPTURE SQUARES AGAINST EVERY PIECE LANDING, KNIGHTS INCLUDED: T61R1 25...Nd5?? 'defended by c6, nothing attacks d5' - HIS e4-PAWN took it (26.exd5; e4 owns d5 and f5). A knight that is only pawn-guarded is lost to the pawn's capture. e5 owns d6/f6, e4 owns d5/f5, d5 owns c4/e4, c6 owns b7/d7.
- WITH WHITE's e5-PAWN ALIVE, f6 AND d6 ARE ITS CAPTURE SQUARES - FOR EVERY PIECE, KNIGHT INCLUDED. THE repeated blunder: T59 11...Nf6?? 12.Nxf6; T60F 10...Nf6?? 11.exf6 = N for a pawn, lost from move 11. Before ANY knight move list every enemy pawn on ranks 3-6 and BOTH its forward capture squares.
- MY OWN PIECE ON A LINE IS MY ONLY SCREEN - moving it exposes whatever it hid. T60R2: Qd2, O-O-O and Bd4 all piled on the d-file with his Roc8/Rfd8 free; 13...Rad8 aimed at d2 and my BISHOP on d4 was the lone plug; 14.Bxa7?? unplugged the file and ...Rxd2 won my QUEEN for a rook. Before any bishop/rook move on the file my queen or king stands on, list what that piece is screening.
- TWO LOOSE UNITS IN A ROW THROW A WON OPENING: T60R3 15...Bxe4 left Nd7 loose (16.Qxd7) and then 16...Bc6?? left Be7 loose (17.Qxe7). Every developing/bishop move: list MY undefended pieces and his queen/rook/bishop that reach them in ONE move.
- HITTING HIS QUEEN IS NOT AN ANSWER WHEN IT OPENS A CHECK (T55 Final 15...Be7 16.Bg6+!). List HIS checks on the NEW board before any tempo hit.
- OPEN FILE WITH HIS ROOK BEHIND IS DEATH: T56R3 14...exf5 15.gxf5 Bxf5 16.Rxf5.
- A PAWN THAT LEAVES ABANDONS ITS POST. In the Caro never ...f6 while my king is on e8/uncastled and e6 has no PIECE guard. In reversed QGD the c6-pawn guards d5: ...c5 only when d5 has a PIECE guard.
- A PINNED PAWN IS NOT A GUARD; MY OWN piece between his heavy piece and my destination is no shield.
- NEVER A KNIGHT ON A SQUARE HIS PIECE OR PAWN COVERS: retreat a d5-knight to b4/e7/b6/c7, never f6 while his e5-pawn lives.
- HIS UNDEFENDED PIECE IS FREE EVERY MOVE - scan HIS guards (pawns first): T59R5.2 his Bd4/Nc3/Rd3/Re2 all had no guard. T60R1 32.Rc6?? ...bxc6. T60R3: his Nd7 and Be7 both went loose to Qxd7/Qxe7 - but check MINE first.
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5, d5<-c4/e4. A moved pawn still attacks; its NEXT PUSH hits too.
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and EVERY knight jump; a central jump needs EVERY recapturer. A FORK IS ONLY A FORK IF THE LANDING IS SAFE AND ITS TARGETS CANNOT STEP WITH TEMPO.
- Rooks and knights only where GUARDED; before a ROOK CHECK ask can his king take. The recapturer must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH. A ROOK ON THE 6th/7th: list his a/b/c-pawn captures.
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY OTHER MOVE.
- A TEMPO HIT BY A BISHOP/ROOK: list his checks and the pawn-covered squares beside my king.
- A SUPPORTED PAWN BREAK e5 (f4 guarding) FORKS QUEEN AND KNIGHT: move the knight or queen first.

## Rule 1b - mate first
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3 is luft. TWO ROOKS GUARDING EACH OTHER on f2+f3 stop ...Qh2+/...Qg2+ nets.
- T58: 8.Qb3?? let ...Qxh1; 9.Kf1?? Bh3+ 10.Ke1 Qxg1#.
- King g8 + rook f8 + g7 GONE: his Re8+ ...Rf8 block is Qg7# if his bishop covers g7/h8. Keep the g7-pawn.
- Back rank: keep a rank-1 blocker or luft. T61R1 38.Re8# - my only 8th-rank rook had walked to d8 and Kg8 had no luft.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. QUEEN CHECKS: list EVERY block.
- WON POSITION: the forcing check beats a slow lift; Q+R: protected checks drive to the edge; Q vs K: knight's-move box, no stalemate. T60R3 model conversion: up Q vs N+B, kept every unit guarded, traded rooks on my terms, promoted, mate.
- BISHOP PINNED ON g1 + K h1: ...Rc1+ freezes it; his f3+h3 then threaten ...hxg2#.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. A BISHOP LANDING WITH TEMPO ON HER = she moves.
- T61R1 29...Qd7?? onto his c6-PAWN's capture square (c6 owns b7 AND d7): 30.cxd7 won the QUEEN for a pawn, up-material game thrown. Before every queen move LIST every enemy pawn on ranks 3-6 and its two capture squares.
- QUEEN NEVER ON AN ENEMY BISHOP'S DIAGONAL, KNIGHT JUMP SQUARE, OR PAWN'S CAPTURE SQUARE (LIST HIS PAWNS FIRST on any queen capture): T56R5 25...Qc5?? d4-pawn; T60S2G1 30.Qxc5?? dxc5 = Q for B.
- QUEEN RECAPTURE: walk EVERY enemy attacker of the landing square, not just the piece taken. T60F 22...Qxg5?? - White's Qd2 also hit g5 (d2-e3-f4-g5); lost my QUEEN for a bishop.
- A QUEEN THAT IS THE ONLY GUARD OF A BISHOP'S RAY TO MY ROOK: T59 14...Ba6, 15.Qd2?? Bxf1.
- UP A QUEEN: no queen move onto any bishop diagonal or pawn square; force his last rook trade or mate - no grabs.
- BEFORE every queen move list what she defended where she stood AND every enemy knight/pawn hitting the destination. A BLOCKED GUARD IS NOT A GUARD.
- A QUEEN CAPTURE ON A SQUARE GUARDED BY A ROOK ON THE SAME FILE IS LOST: T59 22...Qxd3?? 23.Rxd3.
- QUEEN PAWN-GRABS OPEN HIS ROOK LINES: T59 my Qxb2/Qxc3 won pawn+knight but his rooks reached b7/e7/a7.

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing. ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE PIECE.
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P. A ROOK THAT GRABS IN HIS CAMP MUST BE DEFENDED.
- AFTER a capture that wins a piece rescan for MY loose units; after ANY trade re-count ALL my guards.
- UP THE EXCHANGE WITH QUEENS ON: no pawn-grabs with a rook, keep both rooks guarded, trade rooks on my terms.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE; rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND. T60R2: level after the d5 exchanges, then my 13.Bd4?/14.Bxa7?? traded my QUEEN for a rook.
- LEVEL MATERIAL WITH A BROKEN KING IS LOST vs SF.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s a move. T60R3 model: 46...Qad2#. T61R1: up a knight but still let 26.exd5 and 30.cxd7 win pieces - CONSOLIDATE, keep every unit off his pawn squares.
- UP A ROOK (2R v R, pawns level) IS A PROGRESS PROBLEM: T60R1 32...bxc6 won his rook, then 20 moves of shuffles = THREEFOLD DRAW. Plan: extra rook to an OPEN file/7th, offer a defended rook-for-rook trade, drive his king. PROGRESS TEST after every move: 'what does this threaten that the last move did not?' Nothing = a shuffle, banned.
- DOWN A PIECE VS SF IS LOST: no pawn-grabbing with the queen, guard every unit, hunt ONE freeing trade.
- AFTER A QUEEN TRADE, RECOUNT: if the recapture chain loses the queen, don't start it.

## Openings
- Caro B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies); then ...cxd4/...Bc5/...Bb6/...Ne7/O-O. T60F: after 9.O-O Qc7 10.Na4, 10...Nf6?? was the game-loser (11.exf6, down N for P) - the e5-pawn owns f6; play ...Nbd7/...Bd7/...h6/...Qb6. Never ...f6 while e6 has no PIECE guard; retreat the bishop before f4-f5; never recapture ...Bxf5 on the open f-file (T56R3 16.Rxf5); recapture ...hxg6, never ...Nxg6; ...Be4 loses to Nxe4.
- English as Black (reversed QGD; W T59R5.2, T60R3 by mate; D T60R1; L T61R1): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies). Then ...Bf5, ...Nbd7, ...Qb6/...Qc7, ...Rfc8. ...c5 ONLY when d5 has a PIECE guard: route ...Nbd7-...Nb6 or ...Ne4 first. T60R1: ...c5 with the knight on d7 = Nxd5 won a pawn. T61R1: took 13.Ne5?? free (up N) but 19...Nf6? (his e4-pawn) and 25...Nd5?? exd5 won it back, then 29...Qd7?? cxd7 lost the queen. BANS: no knight on his e4-pawn's d5/f5, no queen on d7 (his c6-pawn) or any pawn square, ...Na4?? bxa4, ...Bxa4?? Rxa4, ...Bd6?? onto Nf5's jump.
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); then ...Na5/Bc2, ...c5, d4/Nbd2. As Black move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo. As White keep Rc1; no piece on a square his g6-pawn covers. BANS: ...Qxd4?? c3, ...Re8?? Rxe8+.
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then ...Qd7, ...Rfe8, ...d5. If ...Bg4, Re1 and h3. T60S2G1 WIN v GLM: 11.Nb3?! Nxb3 12.d4 Nxc1?? 13.Rxc1, then 16.Ba4! Qxa4?? 17.Qxa4! won her. BANS: 10.d4?!, queen on d5 while his f6-knight lives.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); then f4, Qd2, Rad1, Kh1. 9.f4 b5 10.e5! best; after ...Nd5 take it. WINs T55S2G1, T54S2G1, T54R1, T53R3, T57R3. BANS: 12.Qd2?? after ...Bc5, 15.Nd5??, 26.Rxa6??, 27.Qf4??.
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies); 9.Qg4. With my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8). T50R3: 11...g6?? 15.Qf6 won h8. T55 Final: 12...f6?? 13.Nxd5!/14.exf6.
- Dragon / Yugoslav as White (T37R7 L, T60R2 L by mate): the Nc3/Be3/f3/Qd2/O-O-O build with Bc4/Bb3 is only safe if NOTHING piles on the d-file with queens on. T37R7: 14.Bh6?? Bxh6 Qxh6 Rxh6. Bans: 15.Qd2?? while a bishop aims at f1; h3 only when e3 is guarded twice.

## Opponents
- SF19: instant, zero errors. Punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares, every voluntary pawn loosening. T60F: as White in the Caro Advance he played 11.exf6 the moment I put a knight on that pawn's square, then took my g5-queen along d2-e3-f4-g5. Give him no pawn break, no loose unit, no piece on his e5-pawn's f6/d6, nothing stacked on a file he can open; 10-15 s.
- GLM 5.3 Flash (13 wins incl. T59R5.2, T60R3, T60S2G1 by mate): slow, miscounts material, leaves pieces and rooks undefended (T60R3: my Nd7/Be7 went loose; he then blundered Qxf7+?? Kxf7). Take every gift, then trade queens and count, 10-15 s. Punishes MY loose knight jumps.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded, converts cleanly and PUNISHES a piece or queen on his pawn's capture square. T60R1 (draw, I threw a rook-up): its Rc6?? hung a rook to ...bxc6. T61R1 (0-1): after I won a knight it stayed patient, played 26.exd5! when my Nd5 sat on its e4-pawn's square, and 30.cxd7! when my queen sat on its c6-pawn's square, then 38.Re8#. Take every loose unit only AFTER the pawn capture list, then CONVERT with a named plan, 5-10 s once ahead.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery; converts the moment I leave a piece on a pawn's capture square.
- Sonnet 5.5, GPT-6.1 Sol, Astra: take every unguarded unit, punish a loose queen or rook, no gifts; keep every unit guarded and bank clock.
- Haiku 5.5: solid Italian Pianissimo, fast; I forfeited and lost twice on the clock there - 10-15 s, bank time, check legality twice.
