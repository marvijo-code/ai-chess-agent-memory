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

## Rule 0 - legality & the one-move answer
- 3 rejected replies on ONE move = forfeit; empty = same. Walk EVERY move's path for MY OWN pieces FIRST: piece, ACTUAL square, occupant, destination, path, off the BOARD. After ONE rejection never resend: list the LEGAL moves, pick a DIFFERENT piece/idea. T53R1: 19 invalid (3 each on 20...Qf5, 23/25...Rf7, 26...Re7, 27...Re6, 40...Kf5), 10:04 on 14...Bxc3. Once rejected the move is DEAD.
- Position turns: write ONE-MOVE answer (recapture first, move the attacked piece), send within 15 s.
- SELF-BAN: a move my scan called bad is DEAD.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; two units hitting is not safety. Quiet/tempo/retreat same sweep.
- Screens: his own piece between his heavy piece and my destination is NO shield - he can move it, capture included. MY guard is void if my own piece stands between. T45R4 20...Qc7?? only Bc5 blocked Qc2-c7; 21.Bxf8/22.Qxc7 won my queen.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, a3/c3<-b4, e5<-d4/f4, f6<-e5, f5<-e6/g6, g5<-h6, d4<-c5/e5, h6<-g7. A moved pawn still attacks; a pawn's NEXT PUSH hits too. T52R3 25.Ra3?? bxa3 lost a rook. T53R1 13...Qxd4?? 14.c3 hit Qd4+Bb4 = piece for pawn; before a queen grab list every pawn push that hits her AND the other piece on its second capture square.
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and every knight jump; a central knight jump needs EVERY recapturer. A FORK IS ONLY A FORK IF THE LANDING IS SAFE AND ITS TARGETS CANNOT STEP WITH TEMPO (T50R4 15...Ne4?? Nd6).
- HIS KNIGHT ON A SQUARE WHOSE RECAPTURE HIS OWN PAWN BLOCKS IS FREE: T53R2 ...Nd5 hit my Bc4 but his d6 pawn blocked Qd8, so Bxd5 won a knight; his ...Nxd4?? then cxd4 won another piece.
- WHITE e5 PAWN OWNS d6 AND f6 - no-go for every piece, QUEEN included. With my king castled Qg3 also PINS g7.
- Rooks and knights only where GUARDED; before a rook CAPTURE walk pawn recaptures; before a ROOK CHECK ask can his king take. The recapturer must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH.
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY QUIET MOVE ELSEWHERE. T52S2A 20.Qd3?? was hit by ...Rfd8; 22.Bxb7?? ignored ...Rxd3 and lost the queen.
- TRADING A ROOK OFF MY KING'S RANK-2 SQUARE: name g2/h2's guards on the NEW board. T51R4 25.Rxf5? Qxf5 left g2 to the king alone; 27...Qxg2#.
- PAWN HITS TWO PIECES: move the MORE VALUABLE and count the recapture (T53R1 14...Bxc3?? bxc3).

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP. With my king on g1/g2 and his queen on d5/f5 plus his bishop on b7, ...Qxg2 is mate unless a rook/queen stands on f2 or h3 is luft - play the luft EARLY.
- Qg4+Bh6 vs short-castled king (g7 king-guarded only): answer ...f5/...f6, ...Qf6, or trade queens. With my e8-king the Qxg7 net needs a PIECE on g7, not a pawn. Bd3+Qh6 vs MY short-castled king: Qxh7#.
- MY SHORT-CASTLED g8-KING behind g6+g7: his Qf6+Bh6 = Qg7#. MY e8-KING + Bf8 covering g7: keep f8 guarded too; his Qf6 hits h8 down a1-h8 once g7 is empty, Bh6 then Qxf8# (T50R3 11...g6?? 15.Qf6). MY Bf8 covering d6 is void if my queen stands e7 (T51R1 14...Qe7?? 15.Nd6+).
- Back rank: keep a rank-1 blocker or luft. A rook that is the LAST guard of an entry square must not leave for a pawn.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. Before ANY check write what captures the checker, KING included.
- QUEEN CHECKS: list EVERY block. T51R3 25.Qd8+ allowed ...Bg8 as well as ...Bf8.
- WON POSITION: prefer the forcing check over a slow lift - T53R2 27.Re3 (6:09) aimed at Rh3 but 28.Rf3+ forced ...Rf7 and 29.Qxf7#. A rook check on the file where his block must land is the mating move.
- Q vs lone K: box with the queen a knight's move from his king, bring my king up, leave him a legal square every move - no stalemate.
- CONVERSION NET: with his king on g1, ...Rc2+ Kg1 ...Re1# wins when my bishop covers g1 (T52R5).

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. HIS BISHOP LANDING WITH TEMPO ON HER = she moves.
- QUEEN NEVER on an enemy bishop's diagonal or knight jump square, tempo/blocking a mate included. T53R2 his ...Qe6?? stepped onto my Bb3's diagonal: Bxe6 won her.
- A QUEEN CAPTURE STILL COUNTS RECAPTURERS to her destination; a check that does not cover the mate square is no defence.
- BEFORE every queen/rook move list what it defended where it stood AND every enemy knight/pawn that hits the destination. A BLOCKED GUARD IS NOT A GUARD. A pawn push is not loose because I can take it - count HIS recapture.
- NEVER a queen on a PAWN's capture square, or where a pawn push hits her next move. DOWN = NO grabs; defend WITHOUT her.
- HIS QUEEN IN MY CAMP: list every unguarded piece of mine she reaches next move (T51R4 ...Qxc2 then ...Qxe2). A queen hit by a rook must leave BOTH the file AND the rank (T52S2A 20.Qd3?? ...Rfd8).

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE PIECE. Count EVERY recapturer, PAWNS FIRST; trace the chain to the end (T53R2 Bxd5: his queen could not reach d5 through d6).
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P. NO ROOK TRADE WHILE BEHIND unless a piece comes back at once (T51R4 25.Rxf5?).
- AFTER A CAPTURE THAT WINS A PIECE, RESCAN FOR MY OWN LOOSE UNIT. After ANY trade re-count guards of ALL my units.
- QUEEN TRADE WHEN AHEAD: take his queen if she lands on my queen's ray/square (T51R5 18...Qxc5).

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE (count pieces, never prose; T51R4 'up' comments were false); rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND.
- CONVERTING UP: guard every unit, trade pieces not pawns, escort passers, stalemate-check. Model T53R2 (up Q+2R): keep the queen OFF his rook's rank, eat undefended pawns (Qb3/Qxb7+, Qxd7+, d6, c6, e6), then Rf3+ Rf7 Qxf7#. Others: T51R2 (up B+P: rook to 6th/7th, Rd8#); T52R1 (Qd8+/Rg3+/Qg8#); T52R5 (...Bf6, ...Rxe3, ...Rc2+ Kg1 ...Re1#).
- BIG LEAD = SIMPLIFY FAST: trade queens/rooks when safe, keep every unit guarded, make luft, avoid queen grabs; 5-10 s a move (T52S2A: up Q+2R+2B+N and flagged).
- CLOCK - 3600+10: cap 30 s, routine 10-15 s, <15 min left -> 5-10 s. QUIET moves get 5-15 s and the FULL sweep: T51R4 burned 7-9 min on 20.h3??/25.Rxf5??; T52R5 13:18 on 21...Qe5 (3 tries); T52R3/T53R1 3-10 min on plain moves. Long thinks never saved a move (T53R2 14.d4?! 2:08 and 27.Re3 6:09 - the 15 s check Rf3+ was the win). Armageddon White 10 min: 10-15 s from move 1, winning lead 5-8 s, under 3 min 3 s.

## Openings (only the lines I actually play)
- English as Black (WINS T38R2, T41R4, T45R4, T50R4, T51R5, T52R5; T49R2 L forfeit): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (16 plies); ...Bf5/...Nbd7/...Re8/...Qb6/...Rac8/...Nf8, then ...c5 only when d5 is guarded or ...Ne5 safe. His slow queen moves and ...h6/...Nf8 let me keep a big edge; his Bxh6?? met gxh6. Do not burn 13 min on ...Qe5. ...c5?! too early lets dxc5 and Qxd5 if d5 loses guards; ...Ne4 only with c5 safe and queen off the c-file.
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); ...Na5, Bc2, ...c5, d4, Nbd2, ...Qc7, ...cxd4 Nc6. As Black move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo; Qc7 'defended' by Rc8 is still Rxc7. As White keep Rc1; no piece on a square his g6-pawn covers (f5/h5); no check he can capture.
- Four Knights Spanish B v SF19 (T45R6 L; T53R1 L): ...Bb4 and castle; the ...Nd5 trade line runs ...e4, ...dxc6, ...exf3, ...Qxf3, ...dxc6 only; then ...d6/...Bf5/...Be6, keep d4 defended. T53R1: 13...Qxd4?? met 14.c3 (queen + bishop hit) = piece for pawn; BANS: ...Qf6 while his queen can take f6, ...Re8?? (Rxe8+), no queen grab onto a pawn's capture square.
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then ...Qd7/...Rfe8/...Bb6/...d5. Branch 7...Bg4 8.Re1 a6 9.h3 Bxf3 10.Qxf3 Qd7: Nb3/Bb6, Be3/Bxe3 Qxe3, then d4 with Re1/Rad1. T53R2 WIN v GLM: his ...Nd5 hit my Bc4 but his own d6 pawn blocked Qd8, so Bxd5 won a knight, his ...Nxd4?? cxd4 another piece, then ...Qe6?? Bxe6 won the queen; she ate b7/d7/d6/c6/e6 and 28.Rf3+ Rf7 29.Qxf7#. 14.d4?! was marked ?! - push it only after full development. BANS: 10.d4?!, 12.c4?, 13.Bc2??, 14.Bg5??, 15.Nxe5??, 24.Qh5??, b4 WHILE MY KNIGHT IS ON b3, queen on d5 while his f6-knight lives (T46R1 17.Ne4?? ...Nf4xd3; 23.Nh4?? ...Rxd2; T45R7 15.cxd4? IQP; 19.d5? ...Ne5; T44R2 25.Rc1 was d1's only guard).
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1. T51R2/T51R3/T52R1 WINS: after 9.f4 b5, 10.e5! works (...Nxd4 11.Qxd4; ...Nd5 12.Nxd5 exd5 13.Qxd5 wins a pawn, his c8-bishop cannot reach d5); then rooks to the 7th/8th, f5-f6, Rd8#; after ...Bc5 do NOT play 12.Qd2??. T51R4 LOSS vs mirror: his 9...Qc7 10...Nxd4 11...b5 12...Ne8 13...f6! held; 16.Qxd4 Qxc2! 17...Qxe2 won my loose Be2. vs Dragon block ...Qa5+ with Bd2/Bd1, never Qd2??. T52R3: 12.Rf3/13.Rh3 slow rook lift (6+ min); 21.Rxd7! won the knight but his 22...Bc6 forced 22.Rc7 Bxa4, then 25.Ra3?? bxa3 lost a rook; 19.f5?! was premature (2 invalid tries).
- Open Sicilian W vs 3...Nxd4 4...e5: 5.Nb5 a6 6.N5c3, then Nf6/Be2/Be7/short castle, Be3/Qd2/Nd5/f4; keep the c4-bishop safe.
- Alapin W vs mirror (T52S2A): after ...cxd4 recapture with cxd4 (never Nxd4 first); ...Nxd4?? loses a knight to Nxd4 when his d5-knight screens Qd6. A won position is still a clock position.
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies); 9.Qg4. With my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8); never ...f5 while exf6 e.p. opens lines to my king. T50R3: 9...Bf8 right, but 11...g6?? opened a1-h8 - 15.Qf6 won h8, 16...Qb6?? 17.Bh6 Qxf8#. After ...Bf8 the bishop STAYS; no ...g6, no queen pawn-grabs; plan ...c5/...Be6/...Qb6 and trade his d3-bishop. T51R1 vs SF: 14...Qe7?? after Bd2 BLOCKED Bf8's guard of d6 - 15.Nd6+! won. Never take Bg5 with the queen while Nf7+ forks her. T49R4: ...a6 BEFORE White's Nb5; 11...Re8? 12.Nb5 Bd7?? 13.Nc7!. T52S2G1 vs mirror: 18...Qxb2 19...Qc3! won a pawn; 21...c4?! lost the c-pawn after Rxc3/Rxc4 - keep ...c4 guarded or play ...Rc8/...Be7; with +P convert actively, no 6+ min thinks.
- Caro B 4.Be2/4.Nf3: 3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 7.Nh4 Bg6 8.O-O Nf5 (12 plies). ...Nd7 then ...Ne7 (NEVER ...Ngf6 while e5 stands); recapture ...hxg6, never ...Nxg6?!. ...Be4 loses to Nxe4. T52R2 vs SF: 12.f4 c5 13.g4! hits Bf5 - move it (...Bg6/...Bxf5) BEFORE ...cxd4; 13...cxd4?! 14.Nxd5! exd5 15.gxf5 and his d6/e6 pawns roll; a knight on c5 is kicked by b4; his d-pawns end in e8=Q+.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares. Give him NO loose unit; resolve central tension before castling. A piece down: aim for repetition. T45R6: took my hanging Re8 with check. T50R3: g7 covered by ...Bf8, then 11...g6?? let 15.Qf6 win h8. T50R5: Taimanov IQP level to 20; 20...d4?! lost the pawn, then passive moves lost the ending. T51R1: 14...Qe7?? screened Bf8 from d6; 15.Nd6+ won, 19...Qxg5?? 20.Nxf7+ won my queen. vs SF: no pawn push that becomes a target, keep d6/g7 covered by PIECES, 10-15 s. T52R2: his 13.g4! hit my Bf5, 14.Nxd5! gave him the d/e passers and mate m32. T53R1: Four Knights; 13...Qxd4?? into 14.c3 lost a piece, 19 invalid replies; he converted with Q+R.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square.
- Sonnet 5.5 (never beaten): banks clock, quiet space moves, then takes every UNGUARDED unit. T46R1: punished 17.Ne4?? with ...Nf4xd3, then 23.Nh4?? with ...Rxd2. 10-15 s from move 1, assume 60+ moves, keep a rank-1 blocker.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn/bishop diagonal or knight square, and any loose recapture. T44R2: +P in a rook ending, ...Rd1# when my c1-rook left d1. T45R2: punished my central knight jump and made two passers queen.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3, and the Chigorin; gives nothing loose.
- GLM 5.3 Flash (T53R2 I WON as White, Italian: he hung a knight to Bxd5, a second piece to ...Nxd4??, then his queen to Bxe6; 1 illegal; 1-8 min on quiet moves): slow, miscounts material, hangs queens/rooks/knights when worse or even, but punishes MY loose knight jumps. T51R5 (I won as Black, English): 18.Qxc5?? stepped into my Qd5 and lost his queen; I converted Q+R cleanly. T52R1 (I won as White): 13...Qxc3?? hung his queen to my Qd4. T52R5 (I won as Black): his Bxh6?? gxh6 dropped a bishop, then ...Rc2+ Kg1 ...Re1#. T50R1: I won his queen with Rxg6+! then FORFEITED m40 (five illegal tries + empty). vs GLM: 10-15 s sound moves, guard every unit, trade queens, take any queen on my ray and any piece whose recapture his own pawn blocks, ladder the rooks, NEVER an empty or illegal reply.
- Haiku 5.5: fast, solid Italian Pianissimo, no free material. T44R3 I FORFEITED (3 illegal tries) in a dead-equal position; T45R3 he beat me on the clock. 10-15 s a move, bank time, check legality twice.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov both ways, keeps units guarded. T50R2 I BEAT HIM (his 16.Qh6?? gxh6). T51R3 I won as White (e5 clamp, Nxb5!, Qf6# m29). T51R4 I LOST as White: his 9...Qc7 10...Nxd4 11...b5 12...Ne8 13...f6 held, then ...Qxc2/...Qxe2 won the loose Be2, Qd5+Bb7 mated g2 after I traded Rf2. T52R3 I LOST: 21.Rxd7! won a knight, his 22...Bc6 forced 22.Rc7 Bxa4, my 25.Ra3?? bxa3 lost a rook. T52S2G1 DRAW as Black: 18...Qxb2/19...Qc3 won a pawn, passive ...Rd8/...Ra8 let him draw. T52S2A LOSS as White (flagged +piece): his 8...Nxd4?? dropped a knight, then 16.Ne4 (3:45) let ...Rfd8/...Rxd3 win my queen. Win on legality, guard counts, active conversion; do not burn minutes.
