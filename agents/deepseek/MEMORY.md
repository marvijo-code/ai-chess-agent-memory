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

## Rule 0 - legality & clock
- 3 rejected replies on ONE move = forfeit; empty = same. Walk MY OWN pieces' paths FIRST: piece, ACTUAL square, occupant, destination, path, off board. ONE rejection = redraw a DIFFERENT move, never resend the idea.
- Turns: write the ONE-MOVE answer (recapture first, move the attacked piece), send within 15 s. SELF-BAN: a move my scan called bad is DEAD.
- CLOCK: routine 10-15 s, cap 30 s; DOWN MATERIAL 5-10 s. Long thinks on retreats and quiet moves changed nothing (T56R5, T57R1, T57R3 3:40 on 15.Qe3?!). The written list is the check, not the think.
- His last move first, then MY destination: 0 guards + his capture = gift; two attackers is not safety. Quiet, retreat and tempo moves get the same sweep.

## Rule 1 - destination sweep
- HITTING HIS QUEEN IS NOT AN ANSWER WHEN IT OPENS A CHECK: T55 Final 15...Be7 16.Bg6+! Kd8 17.Qxh8+ Bf8 18.Qxf8#. Before any tempo hit on his queen, list HIS checks on the NEW board.
- OPEN FILE WITH HIS ROOK BEHIND IS DEATH: T56R3 14...exf5 15.gxf5 Bxf5 16.Rxf5. Before a capture/recapture on an open file, name his rook on it and the guards of MY landing square.
- WHITE f4+g4 vs MY Bg6: f4-f5 hits g6 AND e6. Retreat the bishop BEFORE f5 (h7-class; h5 is the g4-pawn's square) or meet f5 with ...f6; ...c5 does not stop it (T56R3 13...c5?! 14.f5!).
- A PAWN THAT LEAVES ABANDONS ITS POST. T56R5: 11...f6?! vacated f7, e6's ONLY guard; exf6/Bxf6/dxc5/d4/Rxe6 followed. In the Caro never ...f6 while my king is on e8/uncastled and e6 has no PIECE guard.
- A PINNED PAWN IS NOT A GUARD. His own piece between his heavy piece and my destination is no shield; MY guard is void if my own piece stands between.
- HIS ATTACKING BISHOP WITH NO GUARD IS FREE; count its guards before retreating. A knight landing hitting a loose piece is answered first; a pawn kick is not an answer. Before ...Ng4/...Nf5/...Nd4/...Nc4 list the guards of EVERY piece it hits.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, a3/c3<-b4, e5<-d4/f4, f5<-e6/g6, g5<-f4/h4, d4<-c5/e5, h6<-g7, f4<-e5/g5. A moved pawn still attacks; its NEXT PUSH hits too.
- A PAWN THAT JUST CAPTURED OWNS ITS NEW SQUARES: T56 15...dxc6 made c6 hit d5 AND b5; 16.Bd4?? moved the OTHER bishop and ...cxd5 won it. The attacked piece moves first.
- HIS QUEEN ON A PAWN'S CAPTURE SQUARE IS FREE. HIS UNGUARDED BISHOP ON AN OPEN LINE FALLS.
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and EVERY knight jump; a central jump needs EVERY recapturer. A FORK IS ONLY A FORK IF THE LANDING IS SAFE AND ITS TARGETS CANNOT STEP WITH TEMPO. HIS KNIGHT ON A SQUARE WHOSE RECAPTURE HIS OWN PAWN BLOCKS IS FREE.
- WHITE'S e5 PAWN OWNS d6 AND f6 - no-go for every piece, QUEEN included.
- Rooks and knights only where GUARDED; before a rook CAPTURE walk pawn recaptures; before a ROOK CHECK ask can his king take. The recapturer must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH.
- A ROOK ON THE 6th/7th RANK: list his a/b/c-pawn captures (T56 37.Ra6?? bxa6; T52R3 25.Ra3?? b4xa3).
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY OTHER MOVE. A pawn that leaves a square stops guarding it.
- TRADING A ROOK OFF MY KING's rank-2 square: name g2/h2's guards on the NEW board. PAWN HITS TWO PIECES: move the MORE valuable and count the recapture.

## Rule 1b - mate first (after EVERY his move, quiet ones too)
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP. King on g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2 mate unless a rook stands f2 or h3 is luft - play the luft EARLY.
- f6 WITH MY KING ON e8 IS A HOLE, NOT SPACE: T55 Final 12...f6?? (2:47) 13.Nxd5! cxd5 14.exf6 gxf6 15.Qxf6. Push f6 only when g7 AND h8 are covered by PIECES and his queen is off g5/f4.
- TWO ROOKS GUARDING EACH OTHER on f2+f3 stop ...Qh2+/...Qg2+ nets.
- g3 WITH MY KING ON g2/h2 AND HIS BISHOP ABLE TO REACH e5: g3 is PINNED (e5-h2) = a hook for ...h5-h4 and ...Qh4+.
- Qg4+Bh6 vs short-castled king: answer ...f5/...f6, ...Qf6, or trade queens. With my e8-king the Qxg7 net needs a PIECE on g7; if Bf8 sits on g7 then f8 must stay guarded too.
- King g8 + rook f8 + g7 GONE: his Re8+ ...Rf8 block is Qg7# if his bishop covers g7/h8 (T57R1). Keep the g7-pawn or do not allow that bishop.
- Back rank: keep a rank-1 blocker or luft. A rook that is the LAST guard of an entry square must not leave for a pawn.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. Before ANY check write what captures the checker, KING included. QUEEN CHECKS: list EVERY block.
- KING-HUNT WITH R+B: ...Rh3+ with my Bf5/e6 guarding h3 boxes Kg5; ...Be6, then ...f6#/...h6#.
- WON POSITION: prefer the forcing check over a slow lift; Q+N+R v lone K: Ra8 covers g8/h8, Ne5 covers g6/f7, Qg6# defended. T57R2: queen forked rook and a7, then Qe8# on the empty back rank.
- Q+B vs bare king: Qc1+ Ke2 Qd2+ Kf1 Qd1#. Q vs lone K: box with the queen a knight's move away, walk my king up, leave him a legal square - no stalemate. T57R3: Q+R v bare K, Qc8# after removing pawns.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. A BISHOP LANDING WITH TEMPO ON HER = she moves.
- QUEEN NEVER on an enemy bishop's diagonal or knight jump square, tempo included. NEVER on a PAWN's capture square: T56R5 25...Qc5?? with his d4-pawn alive = 26.dxc5, Q for P. In the Caro, c5 is the d4-pawn's capture square.
- UP A QUEEN: NO QUEEN MOVE ONTO ANY BISHOP'S DIAGONAL OR PAWN SQUARE. T56 32.Qd7?? Bxd7 returned her. Force his last rook trade or mate - no grabs.
- BEFORE every queen move list what she defended where she stood AND every enemy knight/pawn hitting the destination. A BLOCKED GUARD IS NOT A GUARD. Count HIS recapture on a pawn push.
- BEFORE A QUEEN MOVE WRITE THE ATTACKER'S ACTUAL SQUARE: a queen on his rook's file/rank is lost unless one of MY pieces blocks it; name that blocker from the board.
- DOWN = NO grabs; defend WITHOUT her.
- HIS QUEEN IN MY CAMP: list every unguarded piece she reaches next move. A queen hit by a rook must leave BOTH the file AND the rank.
- QUEEN BEHIND A SCREEN ON AN OPEN FILE IS LOST when the screen is pinned. Queen + rook/king on one line = skewer: separate them BEFORE the quiet move.
- HIS QUEEN GRABBING A PAWN WITH TEMPO IS STILL TRADABLE: if my queen recaptures safely, take it (T57R2 ...Qxd3?? 23.Qxd3).

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE PIECE. Count EVERY recapturer, PAWNS FIRST; trace the chain to the end. T56 16.Bxd6! Qxd6?? 17.Qxd6. T57R3 16.Bxc5! Qxc5?? (only Bxc5 guard) won her; 17.Qxc5.
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P. A ROOK THAT GRABS IN HIS CAMP MUST BE DEFENDED.
- AFTER A CAPTURE THAT WINS A PIECE, RESCAN FOR MY OWN LOOSE UNIT; after ANY trade re-count the guards of ALL my units.
- QUEEN TRADE WHEN AHEAD: take his queen if she lands on my queen's ray/square. UP THE EXCHANGE WITH QUEENS ON: no pawn-grabs with a rook, keep both rooks guarded, trade rooks on my own terms, then bank.
- PIECE FOR TWO PAWNS can be right when it removes his active bishop and leaves his queen loose: T57R2 14...d5?? 15.exd5 Nxd5 16.cxd5 Bxd5 17.Bb3 won a knight for two pawns; then trade his bishop and simplify.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE; rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND. KEEP THE WON QUEEN off his rook's rank/file, off every bishop diagonal and pawn capture square all the way to mate.
- LEVEL MATERIAL WITH A BROKEN KING IS LOST vs SF: count my king's guards and pinned pawns too.
- UP A QUEEN + ROOK vs R+B: trade his last rook first, then mate with Q+R; T56 lost exactly there (32.Qd7??).
- CONVERTING UP: guard every unit, trade pieces not pawns, escort passers, stalemate-check, 5-15 s a move. BIG LEAD = SIMPLIFY FAST. A clearance pawn move can open my bishop to his rook (T56R4 ...d3! cleared f6-a1, Bxa1).
- DOWN A PIECE VS SF IS LOST: no pawn-grabbing with the queen, guard every unit, hunt ONE freeing trade, 5-10 s a move. T56R5 at -2 pawns from move 14: long thinks on retreats changed nothing; the 10 s move and the guard scan are what matter.
- 3600+10: cap 30 s, routine 10-15 s, <15 min left -> 5-10 s. T54R3 LOST ON TIME; T56R5 burned 33 min and blundered anyway; T57R1 4:10 on ...Qb6? changed nothing; T57R3 3:40 on 15.Qe3?! bought nothing.

## Openings (only the lines I actually play)
- English as Black (WINS T38R2, T41R4, T45R4, T50R4, T51R5, T52R5, T53R5, T55R3, T56R4; LOSS T54R3): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (16 plies); then ...Bf5, ...Nbd7, ...Re8, ...Qb6; ...c5 only when d5 is guarded. vs d4/e3/Bf4 (T55R3 WIN): same build; ...Qb6?! gives Na4 tempo (use ...Qc7/...Qd6); ...c5 once his Bg2 is blocked. T56R4 vs 8.d4 Bf4 Ne5 Qd4: ...c5! kicked the queen; after 14.Qe3?? ...d4! forked Qe3+Nc3. Then trade pieces, no grabs, convert. T54R3: ...a5/...a4 with White b3 is a gift (23.bxa4).
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); then ...Na5 with Bc2, ...c5 and d4/Nbd2. As Black move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo; Qc7 'defended' by Rc8 is still Rxc7. As White keep Rc1; no piece on a square his g6-pawn covers (f5/h5). Four Knights Spanish as Black: ...Bb4 after his 4.Bb5, castle, ...Nd5 then exd5, ...Nd4 with tempo; after 11.a3 RETREAT and keep the pin. BANS: ...Qxd4?? c3, ...Qf6 while his queen takes f6, ...Re8?? Rxe8+.
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then ...Qd7, ...Rfe8 and ...d5. If ...Bg4 comes, meet it with Re1 and h3. T53R2 WIN: Bxd5 won a knight; his ...Nxd4 allowed cxd4 and ...Qe6 hung the bishop to Bxe6. T56R2 WIN v GLM: ...Qd7/...Bxb3 axb3/...Rfe8; 15...c6?! 16.Bxd6! Qxd6?? 17.Qxd6 won her. Keep Bf4 for a real d6 target. T57R2 WIN v GLM: ...d5?? met cxd5! won a knight for two pawns; trade his active bishop, then simplify. BANS: 10.d4?!, b4 WHILE MY KNIGHT IS ON b3, queen on d5 while his f6-knight lives.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); then f4, Qd2, Rad1, Kh1. 9.f4 b5 10.e5! is best; after ...Nd5 take it; if ...exd5, hit d5 with Bf3/Qd2/Rf2 before Nf5. WIN T55S2G1, T54S2G1, T54R1, T53R3, T57R3. BANS: 12.Qd2?? after ...Bc5, 15.Nd5?? (Nf6 recaptures), 26.Rxa6??, 27.Qf4?? Nxf4; when up the exchange use Rc6-c4/Rd4/Re1.
  T57R3 WIN v mirror: 15.Qe3?! (3:40) then 15...Qc5??; 16.Bxc5! (only Bxc5 guard) Bxc5 17.Qxc5 won her. Up a queen: trade the last rook, 20...Rc3?? bxc3, Bxb7/Bxa8, Qxc3, Qc8#. T56R1 LOSS mirror: 16.Bd4?? left the d5-bishop on the c6-pawn's square; 30.Qxe4 won his queen but 32.Qd7?? Bxd7 returned her, 37.Ra6?? bxa6 the rook. Up a queen: trade the last rook, queen off every diagonal.
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies); 9.Qg4. With my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8); never ...f5 while exf6 opens lines. T50R3: 11...g6?? 15.Qf6 won h8, 17.Bh6 Qxf8#. T51R1: 14...Qe7?? screened Bf8 from d6 - 15.Nd6+!. T49R4: ...a6 BEFORE White's Nb5. T55 Final: 12...f6?? lost to 13.Nxd5/14.exf6/15.Qxf6.
- Caro B (T56R5 LOSS m40; T57R1 L m29 v SF19): 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies); then ...cxd4/...Bc5/...Bb6/...Ne7/O-O. T57R1: keep the queen off d6 when his Bb2 can land e5 (21.Be5 hit Qd6+g7); 19...b5?! 20.a4! b4 21.Be5! 22...Qb6? 23.Bxg7! hit Rf8. With king g8, rook f8 and g7 gone, 28.Re8+ forced ...Rf8 and 29.Qg7#. T56R5: never ...f6 while e6 has no PIECE guard and my king is on e8/uncastled; 11...f6?! was fatal. Retreat the bishop before f4-f5 or meet f5 with ...f6 only then; never recapture ...Bxf5 on the open f-file (T56R3 ...Bxf5?? 16.Rxf5, mate 22); recapture ...hxg6, never ...Nxg6?!; ...Be4 loses to Nxe4; no ...Ngf6 while e5 stands.
- Other: vs ...Nc6/...g6 with Bc3/Bc4 (T55 L v SF19): opening was fine; the loss was 9.h3?? letting ...Nxe3. If ...Ng4 comes defend/move e3 FIRST (Qd2, Bd4, or trade with recapture); kick h3 only when e3 is guarded twice.

## Opponents
- SF19: instant, zero errors, never repeats while progressing. Punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares, and every voluntary pawn loosening. T54R2: up Q+R v B it took a threefold only when its rook was attacked every move. T55 Final: level Taimanov, then 13.Nxd5!/14.exf6/15.Qxf6 off 12...f6??. T56R3: Caro Advance +0.4, then 14.f5! broke through, mate 22. T56R5: punished 11...f6?! and every unit I left hanging after that. T57R1: Caro Advance fine to 18...Qd6; 19...b5?! and 22...Qb6? (4:10) let 23.Bxg7! and Qg7# after Re8+ ...Rf8. Give him no pawn break and no loose unit; no queenside pawn push while a4/a5 is available; queen off d6 when Bb2-e5 is possible; 10-15 s.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square.
- Sonnet 5.5 (never beaten): banks clock, quiet space moves, then takes every UNGUARDED unit. 10-15 s from move 1, assume 60+ moves, keep a rank-1 blocker.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn/bishop diagonal or knight square, and any loose recapture.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3, and the Chigorin; gives nothing loose.
- GLM 5.3 Flash (wins T51R5, T52R1, T52R5, T53R2, T53R5, T54S2G1, T56R2, T57R2; T54R3 L on time): slow, miscounts material, hangs queens/rooks/knights when worse or even, but punishes MY loose knight jumps. T56R2 as Black Italian: ...Bxb3/...Rfe8, then 15...c6?! 16.Bxd6! Qxd6?? 17.Qxd6 - it recaptured with its only guard and lost her; 2 illegal tries. T57R2 as Black Italian: 14...d5?? 15.exd5! Nxd5 16.cxd5 Bxd5 17.Bb3 won N for 2P; 22...Qxd3?? 23.Qxd3 won her; 1 illegal ...Rd2 (own d4-pawn blocked). Vs it: 10-15 s, guard every unit, take every loose unit/queen, never an empty or illegal reply.
- Haiku 5.5: fast, solid Italian Pianissimo, no free material; I forfeited T44R3 and lost T45R3 on the clock. 10-15 s, bank time, check legality twice.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded but leaves an active piece loose and can put a piece on my queen/pawn's capture square. Won T50R2, T51R3, T51S2G1, T53R3, T54R1, T55R3, T55S2G1, T56R4, T57R3; lost T51R4, T52R3, T52S2A, T53S2G1, T56R1. T56R1: he handed me his queen but then took the piece I left on d5 (16...cxd5) and the queen I left on his bishop's line (32...Bxd7) - he never refuses a gift. T57R3: as White Taimanov I took 15...Qc5?? with 16.Bxc5! (only Bxc5 guard), then 20...Rc3?? bxc3, Bxb7/Bxa8, Qxc3, Qc8#; it had 1 illegal try (...Rxf4). Take every loose unit, then convert: trade his last rook, no queen grabs, no 5-9 minute thinks.
