# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W (Classical + Chigorin)
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & clock (CLOCK IS #1)
- 3 rejected replies on ONE move = forfeit. Walk MY OWN pieces' paths FIRST: piece, ACTUAL square, occupant, destination, path, off board. ONE rejection = redraw a DIFFERENT piece/idea, never resend. T62R1: 5 invalid tries (2 each on 12.Bd4, 13.Bxg7, 14.Kxd2, 17.Kb1, 19.Rd1) - a rejection means my board picture is wrong, and the re-tries burned my clock and my concentration. T61Final: 3 illegal tries (Rxe6 from f8 blocked by my own Qe8; gxf6 with nothing on f6). T61R1: 3; T61R2/R3: 1 each; T61S2G1: 2 (Qd6xb7 - a queen never reaches b7 from d6: only rank, file, two diagonals).
- His last move first, then MY destination: 0 guards + his capture = gift. Quiet, retreat and tempo moves get the same sweep.
- CLOCK: routine 10-15 s, cap 30; UP MATERIAL 5-10 s; under 15 min 5-10 s; under 5 min 3-5 s; from move 20 never over 60 s. Every flag was a clock game. T60R2: the loss was a QUEEN HANG, not the clock - a simple/level position is a 5-15 s position and the written list is the check. T61R3 spent 3:20/2:30/1:57 on lost-position king moves. T61S2G1: up a queen I spent 1-1:38 on won moves - a won position is 5-10 s. T62R1: 2:29 on 12.Bd4 and 5:01 on 13.Bxg7 in a LEVEL position produced the queen loss; long thinks never find the miss, the written sweep does.

## Rule 1 - destination sweep
- LIST HIS PAWNS' CAPTURE SQUARES AGAINST EVERY PIECE LANDING, KNIGHTS INCLUDED: T61R1 25...Nd5?? his e4-PAWN took it. T61R2 15.Nxc7?? - the knight forked Qe6 and Ra8 but his b6-BISHOP guards c7: a whole knight for a pawn. A FORK ON A SQUARE ANY ENEMY PAWN/BISHOP/ROOK GUARDS IS A GIFT; walk every enemy slider to the landing square, not just the pawns.
- WITH WHITE's e5-PAWN ALIVE, f6 AND d6 ARE ITS CAPTURE SQUARES - FOR EVERY PIECE, KNIGHT INCLUDED. T59 11...Nf6??; T60F 10...Nf6?? = N for a pawn. Before ANY knight move list every enemy pawn on ranks 3-6 and BOTH its forward capture squares.
- MY OWN PIECE ON A LINE IS MY ONLY SCREEN - moving it exposes whatever it hid. T60R2 14.Bxa7?? unplugged the d-file and ...Rxd2 won my QUEEN. T62R1 12.Bd4?? was the only unit between his Rd8 and my Qd2: 12...Rd8 and 13.Bxg7?? Rxd2 won her. Before any bishop/rook move on a file my queen or king stands on, name what it screens; when his rook lands there SHE moves - a capture elsewhere is no answer.
- TWO LOOSE UNITS IN A ROW THROW A WON OPENING: T60R3 15...Bxe4 left Nd7 loose (16.Qxd7), then 16...Bc6?? left Be7 loose (17.Qxe7). Every developing/bishop move: list MY undefended pieces and his queen/rook/bishop that reach them in ONE move.
- HITTING HIS QUEEN IS NOT AN ANSWER WHEN IT OPENS A CHECK (T55 Final 15...Be7 16.Bg6+!). List HIS checks on the NEW board before any tempo hit.
- OPEN FILE WITH HIS ROOK BEHIND IS DEATH: T56R3 14...exf5 15.gxf5 Bxf5 16.Rxf5.
- A PAWN THAT LEAVES ABANDONS ITS POST. In the Caro never ...f6 while my king is on e8/uncastled and e6 has no PIECE guard. In reversed QGD the c6-pawn guards d5: ...c5 only when d5 has a PIECE guard.
- A PINNED PAWN IS NOT A GUARD; MY OWN piece between his heavy piece and my destination is no shield.
- NEVER A KNIGHT ON A SQUARE HIS PIECE OR PAWN COVERS: retreat a d5-knight to b4/e7/b6/c7, never f6 while his e5-pawn lives.
- HIS UNDEFENDED PIECE IS FREE EVERY MOVE - scan HIS guards (pawns first): T61R2 won rook tempi then the queen off his unguarded Bc7/rooks; T61S2G1 26...Rd3?? 27.Rxd3; T60R1 32.Rc6?? ...bxc6. But check MINE first.
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5, d5<-c4/e4. A moved pawn still attacks; its NEXT PUSH hits too.
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and EVERY knight jump; a central jump needs EVERY recapturer. A FORK IS ONLY A FORK IF THE LANDING IS SAFE AND ITS TARGETS CANNOT STEP WITH TEMPO. MY PAWN HITTING TWO OF HIS UNITS = ONLY ONE CAN BE SAVED: T61S2G1 my d5-pawn hit his Qe6 and Nc6, he moved only the knight - 17.dxe6 won the queen.
- Rooks and knights only where GUARDED; before a ROOK CHECK ask can his king take. The recapturer must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH. A ROOK ON THE 6th/7th: list his a/b/c-pawn captures.
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY OTHER MOVE - T61Final 16.Ba3 hit my Ne7 (a3-b4-c5-d6-e7) and 16...fxe6?? ignored it: 17.Rxe6 Qf7 18.Rxe7 Qxe7 19.Bxe7 won my QUEEN.
- A TEMPO HIT BY A BISHOP/ROOK: list his checks and the pawn-covered squares beside my king.
- A SUPPORTED PAWN BREAK e5 (f4 guarding) FORKS QUEEN AND KNIGHT: move the knight or queen first.

## Rule 1b - mate first
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3 is luft. TWO ROOKS GUARDING EACH OTHER on f2+f3 stop ...Qh2+/...Qg2+ nets.
- T58: 8.Qb3?? let ...Qxh1; 9.Kf1?? Bh3+ 10.Ke1 Qxg1#.
- King g8 + rook f8 + g7 GONE: his Re8+ ...Rf8 block is Qg7# if his bishop covers g7/h8. Keep the g7-pawn.
- Back rank: keep a rank-1 blocker or luft. T61R1 38.Re8# - my only 8th-rank rook had walked to d8 and Kg8 had no luft. T61Final 30.Qa8+ Re8 31.Qxe8# - my last rook had to block on e8, undefended.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. QUEEN CHECKS: list EVERY block.
- WON POSITION: the forcing check beats a slow lift; Q+R: protected checks drive to the edge; Q vs K: knight's-move box, no stalemate. T61R2 model (up Q+R+N v K+3P): queen behind the passer, Rc8+/Rxe8 forcing dxe8=Q+ then Qe8#; check stalemate before quiet restrictions. T61S2G1 model (up Q+2R+B v pawns): take the free unit, trade his last rook, then h4-h5 + Qg8# with the bishop covering g8.
- BISHOP PINNED ON g1 + K h1: ...Rc1+ freezes it; his f3+h3 then threaten ...hxg2#.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. A BISHOP LANDING WITH TEMPO ON HER = she moves.
- QUEEN HIT BY A ROOK ALONG A FILE/RANK MUST LEAVE THAT FILE/RANK, NEVER MOVE ALONG IT: T61R3 18...Qe4 stayed under Re1 and 19.Rxe4+ = Q for R. With an uncastled king on an OPEN file, never stand a piece there: 16...Qxe5 -> 18.Rfe1 took her. T62R1: 12...Rd8 hit Qd2 on the d-file - the answer was Q moves off the file (or the bishop that stands on d4 takes the rook), never 13.Bxg7.
- GLM's LEAK, THREE TIMES: his queen on MY pawn's capture square - T61R1 29...Qd7?? cxd7; T61R2 31...Qd5?? exd5; T61S2G1 16...Qe6?? dxe6. Before every queen move LIST every enemy pawn on ranks 3-6 and its two capture squares, and name who can recapture.
- QUEEN NEVER ON AN ENEMY BISHOP'S DIAGONAL, KNIGHT JUMP SQUARE, OR PAWN'S CAPTURE SQUARE (LIST HIS PAWNS FIRST on any queen capture): T56R5 25...Qc5?? d4-pawn; T60S2G1 30.Qxc5?? dxc5 = Q for B.
- QUEEN RECAPTURE: walk EVERY enemy attacker of the landing square, not just the piece taken. T60F 22...Qxg5?? - White's Qd2 also hit g5.
- A QUEEN THAT IS THE ONLY GUARD OF A BISHOP'S RAY TO MY ROOK: T59 14...Ba6, 15.Qd2?? Bxf1.
- UP A QUEEN: no queen move onto any bishop diagonal or pawn square; force his last rook trade or mate - no grabs.
- BEFORE every queen move list what she defended where she stood AND every enemy knight/pawn hitting the destination. A BLOCKED GUARD IS NOT A GUARD.
- A QUEEN CAPTURE ON A SQUARE GUARDED BY A ROOK ON THE SAME FILE IS LOST: T59 22...Qxd3?? 23.Rxd3. QUEEN PAWN-GRABS OPEN HIS ROOK LINES: T59 my Qxb2/Qxc3 won pawn+knight but his rooks reached b7/e7/a7.

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing. ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE PIECE.
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P. A ROOK THAT GRABS IN HIS CAMP MUST BE DEFENDED.
- AFTER a capture that wins a piece rescan for MY loose units; after ANY trade re-count ALL my guards.
- UP THE EXCHANGE WITH QUEENS ON: no pawn-grabs with a rook, keep both rooks guarded, trade rooks on my terms.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE; rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND. T60R2: level after the d5 exchanges, then 13.Bd4?/14.Bxa7?? traded my QUEEN for a rook.
- LEVEL MATERIAL WITH A BROKEN KING IS LOST vs SF.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s a move, and CONSOLIDATE - keep every unit off his pawn squares (T61R1: up a knight but still let 26.exd5 and 30.cxd7 win pieces). T61R2: won by hitting loose units, then pushed the passer with the queen behind it into promotion. T61S2G1: up Q+2R+B, no grabs, took the free Rd3, traded his last rook, h4-h5 + Qg8#.
- UP A ROOK (2R v R, pawns level) IS A PROGRESS PROBLEM: T60R1 32...bxc6 then 20 shuffles = THREEFOLD DRAW. Plan: extra rook to an OPEN file/7th, offer a defended rook-for-rook trade, drive his king. PROGRESS TEST after every move: what does this threaten that the last move did not? Nothing = a shuffle, banned.
- DOWN A PIECE VS SF IS LOST: no pawn-grabbing with the queen, guard every unit, hunt ONE freeing trade, and KEEP THE KING BEHIND PAWNS - T61R3 my king walked Kd7-Ke6-Kd5-Kc5 and 37.Bb4# finished it. DOWN VS GLM IS NOT LOST: keep hitting his undefended pieces and he gives material back (T61R2, T61S2G1). T61Final: down Q for N after 19.Bxe7 I fought 12 more moves but SF mated cleanly. T62R1: down Q for R+B after 13...Rxd2 my two rooks and king alone vs Q+pieces = lost; never create that from a level position.
- AFTER A QUEEN TRADE, RECOUNT: if the recapture chain loses the queen, don't start it.

## Openings
- Caro B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies); then take on d4, bishop c5/b6, knight e7, castle. T60F: after 9.O-O Qc7 10.Na4, 10...Nf6?? was the game-loser (11.exf6, down N for P) - the e5-pawn owns f6; play ...Nbd7/...Bd7/...h6/...Qb6. Never ...f6 while e6 has no PIECE guard; retreat the bishop before f4-f5; never recapture ...Bxf5 on the open f-file (T56R3 16.Rxf5); recapture ...hxg6, never ...Nxg6; ...Be4 loses to Nxe4. T61R3: 11...exf5 left the e-file OPEN with my king still on e8 - NEVER place the queen on that file: 16...Qxe5 -> 18.Rfe1 19.Rxe4+ = Q for R. T61Final: 15...Qe8?! was passive after his 15.e6; 16.Ba3! hit my e7-KNIGHT and 16...fxe6?? lost my QUEEN (17.Rxe6 Qf7 18.Rxe7 Qxe7 19.Bxe7). Answer an attacked knight; never take e6 with the f-pawn while his rook owns the e-file.
- English as Black (reversed QGD; W T59R5.2, T60R3; D T60R1; L T61R1): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies); then bishop f5, knight bd7, queen b6 or c7, rook fc8. ...c5 ONLY when d5 has a PIECE guard: route the knight via bd7-b6 or e4 first. T60R1: ...c5 with the knight on d7 = Nxd5 won a pawn. T61R1: took 13.Ne5?? free but 19...Nf6?, 25...Nd5?? exd5 and 29...Qd7?? cxd7 gave it all back. BANS: no knight on his e4-pawn's d5/f5, no queen on d7 (his c6-pawn) or any pawn square, ...Na4?? bxa4, ...Bxa4?? Rxa4, ...Bd6?? onto Nf5's jump.
- Ruy Lopez as White, Classical 5...Bc5 (T61R2, T61S2G1, both WINS v GLM by mate): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15 plies); then bishop e6, d4 exd4 cxd4, bishop b6, knight c3, bishop g5 h6 bishop f6 queen f6, knight d5 queen e6, knight b6 cxb6, d5! - that pawn hits Qe6 and Nc6 together, so one of them falls (T61S2G1 16...Ne5?? 17.dxe6 won the QUEEN; 18.Nxe5 dxe5 19.Qd6, 21.Qxe6+ took the bishop). Keep 5-15 s: the book is safe, the discipline decides. Chigorin 5...Be7 mirror: same build, bishop b3, pawn d6, castle, then knight a5/bishop c2; keep the c1-rook, play Be3 (never Bd2 - it blocks Qd1's d4 recapture), no piece on a square his g6-pawn covers.
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then queen d7, rook fe8, pawn d5. If ...Bg4, Re1 and h3. T60S2G1 WIN v GLM: 16.Ba4! Qxa4?? 17.Qxa4! won her. BANS: 10.d4?!, queen on d5 while his f6-knight lives.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); then f4, Qd2, Rad1, Kh1. 9.f4 b5 10.e5! best; after ...Nd5 take it. BANS: 12.Qd2?? after ...Bc5, 15.Nd5??, 26.Rxa6??, 27.Qf4??.
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (15 plies); then queen g4. With my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8). T50R3: 11...g6?? 15.Qf6 won h8. T55 Final: 12...f6?? 13.Nxd5!/14.exf6.
- Dragon / Yugoslav as White (T37R7 L, T60R2 L, T62R1 L by mate): the Yugoslav build (Be3, f3, Qd2, long castling, bishop c4/b3) is only safe if NOTHING piles on the d-file with queens on, and vs SF it is a LOSING line - T62R1 12.Bd4?? walked the only d-file screen away and 12...Rd8/13...Rxd2 won my queen. Vs SF prefer the Be2/Be3/f4 Taimanov build or 5.c4 Maroczy; if the Yugoslav is on, move the queen off any file a rook can enter, and never a capture while she is hit.

## Opponents
- SF19: instant, zero errors. Punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares, every voluntary pawn loosening, and an ignored attacked piece. T60F: as White in the Caro Advance he played 11.exf6 the moment I put a knight on that pawn's square. T61R3: he opened the e-file with Rfe1 the moment my queen stood on e5 in front of my uncastled king. T61Final: his 15.e6 + 16.Ba3! won my queen off the e7-knight. T62R1: 12...Rd8 the moment my bishop left the d-file - he converts a level position in two moves. Give him no pawn break, no loose unit, no piece on his e5-pawn's f6/d6, no piece on an open file in front of my king; 10-15 s.
- GLM 5.3 Flash (15 wins): as Black v 1.e4 he plays the Ruy Classical 5...Bc5 and the Taimanov, as White the English/reversed QGD. Recurring leak: HIS QUEEN ON MY PAWN'S CAPTURE SQUARE (T61R1 29...Qd7?? cxd7; T61R2 31...Qd5?? exd5; T61S2G1 16...Qe6?? dxe6). Also leaves bishops/rooks undefended (T61R2 Bc7/Rb2/Rb7/Rb4; T61S2G1 26...Rd3?? 27.Rxd3). 1-5 illegal tries, up to 5 min on one move. Take every gift only AFTER the pawn/bishop capture list, then trade queens and count, 10-15 s. Punishes MY loose knight jumps (15.Nxc7??).
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded, converts cleanly and PUNISHES a piece or queen on his pawn's capture square. T61R1 (0-1): after I won a knight it played 26.exd5! and 30.cxd7!, then 38.Re8#. Take every loose unit only AFTER the pawn capture list, then CONVERT with a named plan, 5-10 s once ahead.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery; converts the moment I leave a piece on a pawn's capture square.
- Sonnet 5.5, GPT-6.1 Sol, Astra: take every unguarded unit, punish a loose queen or rook, no gifts; keep every unit guarded and bank clock.
- Haiku 5.5: solid Italian Pianissimo, fast; I forfeited and lost twice on the clock there - 10-15 s, bank time, check legality twice.
