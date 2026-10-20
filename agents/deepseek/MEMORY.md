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
- 3 rejected replies on ONE move = forfeit; empty = same. Walk EVERY move's path for MY OWN pieces FIRST: piece, ACTUAL square, occupant, destination, path, read off the BOARD. After ONE rejection never resend: list the LEGAL moves, pick a DIFFERENT piece/idea. T52R5 21...Qe5 needed 3 tries (2 invalid) after a 13:18 think in a won game; read the queen's destination and every occupant square by square. T53R1: 19 invalid attempts (3 on 20...Qf5, 23...Rf7, 25...Rf7, 26...Re7, 27...Re6, 40...Kf5) and 10:04 on 14...Bxc3 with 2 invalid - after ONE rejection the move is DEAD.
- Position turns: write ONE-MOVE answer (recapture first, move the attacked piece) and send within 15 s.
- SELF-BAN: a move my scan called bad is DEAD.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; two units hitting is not safety. Quiet/tempo/retreat same sweep.
- Screens: his own piece between his heavy piece and my destination is NO shield - he can move it, capture included. MY guard is void if my own piece stands between. T45R4 20...Qc7?? only Bc5 blocked Qc2-c7; 21.Bxf8/22.Qxc7 won my queen. T51R1 15.Nd6+.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, a3/c3<-b4, e5<-d4/f4, f6<-e5, f5<-e6/g6, g5<-h6, d4<-c5/e5, h6<-g7. A moved pawn still attacks; never two pieces on one pawn's capture-square pair; a pawn's NEXT PUSH hits too. T52R3 25.Ra3?? bxa3 lost a rook. T53R1 13...Qxd4?? allowed 14.c3 hitting Qd4 and Bb4 = piece for pawn; before a queen grab list every pawn push that hits her AND the other piece on its second capture square.
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and every knight jump; a central knight jump needs EVERY recapturer. A FORK IS ONLY A FORK IF THE LANDING IS SAFE AND ITS TARGETS CANNOT STEP WITH TEMPO (T50R4 15...Ne4?? Nd6).
- WHITE e5 PAWN OWNS d6 AND f6 - no-go for every piece, QUEEN included. With my king castled Qg3 also PINS g7.
- Rooks and knights only where GUARDED. Before a rook CAPTURE walk pawn recaptures; before a ROOK CHECK ask can his king take. The recapturer must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH.
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY QUIET MOVE ELSEWHERE. T52S2A 20.Qd3?? was hit by ...Rfd8; 22.Bxb7?? ignored ...Rxd3 and lost the queen.
- TRADING A ROOK OFF MY KING'S RANK-2 SQUARE: name g2/h2's guards on the NEW board. T51R4 25.Rxf5? Qxf5 left g2 to the king alone; his Qd5+Bb7 then 27...Qxg2#.
- PAWN HITS TWO PIECES: move the MORE VALUABLE one and count the recapture. T53R1 14...Bxc3?? bxc3 lost a bishop for a pawn; the queen on d4 was also hit - she moves, the bishop retreats.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP. With my king on g1/g2 and his queen on d5/f5 plus his bishop on b7, ...Qxg2 is mate unless a rook/queen stands on f2 or h3 is luft - play the luft EARLY.
- Qg4+Bh6 vs short-castled king (g7 king-guarded only): answer ...f5/...f6, ...Qf6, or trade queens. With my e8-king the Qxg7 net needs a PIECE on g7, not a pawn. Bd3+Qh6 vs MY short-castled king: Qxh7#.
- MY SHORT-CASTLED g8-KING behind g6+g7: his Qf6+Bh6 = Qg7#; with his Bf6, Qxg6+ Kf8 Qg7+ Ke8 Qg8#.
- MY e8-KING + MY Bf8 covering g7: keep f8 guarded too. His Qf6 hits h8 down a1-h8 once g7 is empty; his Bh6 then Qxf8# (Kxf8 illegal). T50R3 11...g6?? 15.Qf6 won h8; 16...Qb6?? 17.Bh6 Qxf8#. MY Bf8 covering d6 is void if my queen stands e7: T51R1 14...Qe7?? 15.Nd6+.
- Back rank: keep a rank-1 blocker or luft. A rook that is the LAST guard of an entry square must not leave for a pawn.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. Before ANY check write what captures the checker, KING included.
- QUEEN CHECKS: list EVERY block, not the one I expect. T51R3 25.Qd8+ allowed ...Bg8 as well as ...Bf8; Qxg8+ Kxg8 loses her. In a won position use the rook lift (Rf3-g3) instead of assuming mate in two.
- Q vs lone K: box with the queen a knight's move from his king, bring my king up, leave him a legal square every move - no stalemate.
- CONVERSION NET: with his king on g1, ...Rc2+ Kg1 ...Re1# wins when my bishop covers g1 (T52R5: ...Bf6/...Rxe3/...Rc2+ Kg1 ...Re1#, Bxd4 covering g1).

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. HIS BISHOP LANDING WITH TEMPO ON HER = she moves.
- QUEEN NEVER on an enemy bishop's diagonal or knight jump square, tempo/blocking a mate included.
- A QUEEN CAPTURE STILL COUNTS RECAPTURERS to her destination; a check that does not cover the mate square is no defence.
- BEFORE every queen/rook move list what it defended where it stood AND every enemy knight/pawn that hits the destination. A BLOCKED GUARD IS NOT A GUARD. A pawn push is not loose because I can take it - count HIS recapture.
- NEVER a queen on a PAWN's capture square, or where a pawn push hits her next move. DOWN = NO grabs; defend WITHOUT her.
- HIS QUEEN IN MY CAMP: list every unguarded piece of mine she reaches next move. T51R4 after ...Qxc2 she owned the 2nd rank and ...Qxe2 won my Be2 - I never listed e2. T51R5: his 18.Qxc5?? stepped onto my Qd5's capture square; I took her.
- A QUEEN HIT BY A ROOK MUST LEAVE BOTH THE FILE AND THE RANK. T52S2A 20.Qd3?? ...Rfd8; 22.Bxb7?? ignored ...Rxd3 and lost her.

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN. Count EVERY recapturer, PAWNS FIRST; trace the chain to the end.
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P.
- NO ROOK TRADE WHILE BEHIND IN MATERIAL unless a piece comes back at once: T51R4 25.Rxf5? only fed his queen and removed g2's guard.
- AFTER A CAPTURE THAT WINS A PIECE, RESCAN FOR MY OWN LOOSE UNIT. After ANY trade re-count guards of ALL my units.
- QUEEN TRADE WHEN AHEAD: take his queen if she lands on my queen's ray/square; T51R5 18...Qxc5 won her on c5, then Q+R conversion.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE (count pieces, never prose; my 'I remain up' comments in T51R4 were false after ...Qxe2); rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND.
- CONVERTING: guard every unit, trade rooks evenly, two-rook ladder, Ra8#. Up: trade pieces not pawns, escort passers, stalemate-check. DOWN: keep the rook active, take the recapture. T51R2 (up B+P): rook to the 6th/7th defended by bishop or pawn, eat loose h-/d-pawns, Rd8#. T51R3 (up Q+R): free pawns with queen checks, Nc7 fork, Qf6#. T52R1 (up Q+2R): Qd8+ Kg7 Rg3+ Kh7 Qg8# with Rg3 guarding g8. T52R5 (up Q+2R+2B+N): queens off, ...Bf6, rooks ate e3/d4, ...Rc2+ Kg1 ...Re1#; no need for long queen thinks.
- BIG LEAD = SIMPLIFY FAST: trade queens/rooks when safe, keep every unit guarded, make luft, avoid queen grabs; 5-10 s a move. T52S2A: up Q+2R+2B+N and flagged because 14-16 and 21-30 burned minutes.
- CLOCK - 3600+10: cap 30 s a move, routine 10-15 s, <15 min left -> 5-10 s. QUIET moves get 5-15 s and the FULL sweep: T51R4 burned 7-9 min on 20.h3??/25.Rxf5?? and was mated with 30 min left. T52R5: 13:18 on 21...Qe5 (3 tries, 2 invalid) and 4-6 min on other queen moves. T52R3/T52S2G1: 3-6 min on plain moves; T53R1: 10:04 on 14...Bxc3 with 19 invalid replies. Long thinks never saved a move. Armageddon White 10 min: 10-15 s from move 1, winning lead 5-8 s, under 3 min 3 s.

## Openings (only the lines I actually play)
- English as Black (WINS T38R2, T41R4, T45R4, T50R4, T51R5, T52R5; T49R2 L forfeit): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (16 plies); ...Bf5/...Nbd7/...Re8/...Qb6/...Rac8/...Nf8, then ...c5 only when d5 is guarded or ...Ne5 safe. T52R5 vs GLM: his slow queen moves and ...h6/...Nf8 let me keep a big edge; his Bxh6?? met gxh6 and won me a piece, then ...Qxd4/...Nxd5/...bxc6/...cxd5/...Bg6/...Qe5/...Qd6. Up Q+2R+2B+N I traded queens and finished ...Bf6/...Rxe3/...Rc2+ Kg1 ...Re1#. Do not burn 13 min on ...Qe5. Earlier: ...c5?! too early lets dxc5 and Qxd5 if d5 loses guards; ...Ne4 only with c5 safe and queen off c-file.
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); ...Na5, Bc2, ...c5, d4, Nbd2, ...Qc7, ...cxd4 Nc6. As Black move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo; Qc7 'defended' by Rc8 is still Rxc7. As White keep Rc1; no piece on a square his g6-pawn covers (f5/h5); no check he can capture.
- Four Knights Spanish B v SF19 (T45R6 L; T53R1 L): ...Bb4 and castle; the ...Nd5 trade line runs ...e4, ...dxc6, ...exf3, ...Qxf3, ...dxc6 only; then ...d6/...Bf5/...Be6, keep d4 defended. T53R1: 13...Qxd4?? met 14.c3 hitting Qd4+Bb4 = piece for pawn; BANS: ...Qf6 while his queen can take f6; ...Re8?? (Rxe8+); no queen grab onto a pawn's capture square.
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then ...Qd7/...Rfe8/...Bb6/...d5. BANS: 10.d4?!, 12.c4?, 13.Bc2??, 14.Bg5??, 15.Nxe5??, 24.Qh5??, 14.Bf4??, b4 WHILE MY KNIGHT IS ON b3, queen on d5 while his f6-knight lives. T46R1: 17.Ne4?? ...Nf4xd3; 23.Nh4?? ...Rxd2. T45R7: 15.cxd4? IQP; 19.d5? ...Ne5. T44R2: 25.Rc1 was d1's only guard.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1. T51R2 WIN: after 9.f4 b5, 10.e5! works - ...Nxd4 11.Qxd4, ...Nd5 12.Nxd5 exd5 13.Qxd5 wins a pawn because his c8-bishop cannot reach d5; then rooks to the 7th/8th, f5-f6 wedge, Rg7, Rd8#. T51R3 WIN: 9.f4 ...Nxd4/Bxd4 and ...b5 met by e5! and Nxb5!; his Qxc2?? lost the queen; Nc7 fork; Qf6#. T51R4 LOSS vs mirror: 9...Qc7 10...Nxd4 11...b5 12...Ne8 13...f6! held; 15.Ne4 Bxd4+ 16.Qxd4 Qxc2! 17...Qxe2 won my loose Be2. T52R1 WIN vs GLM: 9.f4 Qc7 10.e5! again; after ...Bc5 do NOT play 12.Qd2??; GLM hung his queen with 13...Qxc3?? Qxc3. vs Dragon block ...Qa5+ with Bd2/Bd1, never Qd2??. T52R3 vs mirror: 12.Rf3/13.Rh3 slow rook lift (6+ min); 21.Rxd7! won the knight, but 22...Bc6 double-attacked my d7-rook and a4-knight; 22.Rc7 Bxa4 made material level, then 25.Ra3?? bxa3 lost a whole rook. 19.f5?! was premature and had 2 invalid tries.
- Open Sicilian W vs 3...Nxd4 4...e5: 5.Nb5 a6 6.N5c3, then Nf6/Be2/Be7/short castle, Be3/Qd2/Nd5/f4; keep the c4-bishop safe.
- Alapin W vs mirror (T52S2A): after ...cxd4 recapture with cxd4 (never Nxd4 first); ...Nxd4?? loses a knight to Nxd4 when his d5-knight screens Qd6. A won position is still a clock position.
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies); 9.Qg4. With my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8); never ...f5 while exf6 e.p. opens lines to my king. T50R3: 9...Bf8 right, but 11...g6?? opened a1-h8 - 15.Qf6 won h8, 16...Qb6?? 17.Bh6 Qxf8#. After ...Bf8 the bishop STAYS; no ...g6, no queen pawn-grabs; plan ...c5/...Be6/...Qb6 and trade his d3-bishop. T51R1 vs SF: 14...Qe7?? after Bd2 BLOCKED Bf8's guard of d6 - 15.Nd6+! won. Never take Bg5 with the queen while Nf7+ forks her. T49R4: play ...a6 BEFORE White's Nb5; 11...Re8? 12.Nb5 Bd7?? 13.Nc7!. T52S2G1 vs mirror: 5...Qc7 6...a6 7...Nf6 8...Bb4 10...Bf8 11...c5?! 13...exd5!; 18...Qxb2 19...Qc3! won a pawn; 21...c4?! lost the c-pawn after Rxc3/Rxc4. Keep ...c4 guarded or play ...Rc8/...Be7; do not burn 6+ min on ...f6/...O-O, and with +P convert actively.
- Caro B 4.Be2/4.Nf3: 3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 7.Nh4 Bg6 8.O-O Nf5 (12 plies). ...Nd7 then ...Ne7 (NEVER ...Ngf6 while e5 stands); recapture ...hxg6, never ...Nxg6?!. ...Be4 loses to Nxe4. T52R2 vs SF: 12.f4 c5 13.g4! hits Bf5 - move it (...Bg6/...Bxf5) BEFORE ...cxd4; 13...cxd4?! 14.Nxd5! exd5 15.gxf5 and his d6/e6 pawns roll; a knight on c5 is kicked by b4; his d-pawns end in e8=Q+.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares. Give him NO loose unit; resolve central tension before castling. A piece down: aim for repetition. T45R6: took my hanging Re8 with check. T50R3: g7 covered by ...Bf8, then 11...g6?? let 15.Qf6 win h8. T50R5: Taimanov IQP level to 20; 20...d4?! lost the pawn, then passive moves lost the ending. T51R1: 14...Qe7?? screened Bf8 from d6; 15.Nd6+ won, 19...Qxg5?? 20.Nxf7+ won my queen. vs SF: no pawn push that becomes a target, keep d6/g7 covered by PIECES, 10-15 s. T52R2: his 13.g4! hit my Bf5, 14.Nxd5! gave him the d/e passers and mate m32 - trade or move the attacked bishop before opening the centre. T53R1: Four Knights; 13...Qxd4?? into 14.c3 (queen + bishop hit) lost a piece, and 19 invalid replies; he converted the piece with Q+R.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square.
- Sonnet 5.5 (never beaten): banks clock, quiet space moves, then takes every UNGUARDED unit. T46R1: punished 17.Ne4?? with ...Nf4xd3, then 23.Nh4?? with ...Rxd2. 10-15 s from move 1, assume 60+ moves, keep a rank-1 blocker.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn/bishop diagonal or knight square, and any loose recapture. T44R2: +P in a rook ending, ...Rd1# when my c1-rook left d1. T45R2: punished my central knight jump and made two passers queen.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3, and the Chigorin; gives nothing loose.
- GLM 5.3 Flash: slow, illegal tries, miscounts material; hangs queens/rooks when worse, but punishes MY loose knight jumps. T50R1: I won his queen with Rxg6+! then forfeited at m40 (five illegal tries + empty). T51R2 (I won m55): my 10.e5 clamp, 13.Qxd5!; 4 invalid tries from him. T51R5 (I won as Black, English): he played the reversed-QGD English, spent 4-59 s, 2 invalid tries at 12.Rad1, then 18.Qxc5?? stepped into my Qd5 and lost his queen; I converted Q+R vs pawns cleanly. T52R1 (I won as White, Taimanov): 13...Qxc3?? hung his queen to my Qd4; 0 invalid; Rf3/Qd8+/Rg3+/Qg8#. T52R5 (I won as Black, English): his Bxh6?? gxh6 dropped a bishop; I then took d4/d5/c6/d5, traded queens, and finished ...Rc2+ Kg1 ...Re1#. vs GLM: 10-15 s sound moves, guard every unit, trade queens, take a queen that steps onto my queen's square/ray, ladder the rooks, NEVER end in an empty or illegal reply.
- Haiku 5.5: fast, solid Italian Pianissimo, no free material. T44R3 I FORFEITED (3 illegal tries) in a dead-equal position; T45R3 he beat me on the clock. 10-15 s a move, bank time, check legality twice.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov both ways, keeps units guarded. T50R2 I BEAT HIM (his 16.Qh6?? gxh6, +Q for R converted with ...Qxd4, ...Bxf2+, ...Re1#). T51R3 I won as White (e5 clamp, Nxb5!, Qf6# m29). T51R4 I LOST as White: his 9...Qc7 10...Nxd4 11...b5 12...Ne8 13...f6 held, then ...Qxc2/...Qxe2 won pawns and the loose Be2, and Qd5+Bb7 mated g2 after I traded Rf2. T52R3 I LOST as White: mirror Taimanov; 21.Rxd7! won a knight, but his 22...Bc6 double attack forced 22.Rc7 Bxa4, then my 25.Ra3?? bxa3 lost a rook; he converted Q+R vs bare K. T52S2G1 DRAW as Black: 18...Qxb2/19...Qc3 won a pawn, but passive ...Rd8/...Ra8 repetition let him draw; 3 invalid on 19...Qc3, 6:23 on ...f6, 6:11 on ...O-O. T52S2A LOSS as White (Armageddon, flagged +piece): Alapin, his 8...Nxd4?? dropped a knight; I then burned 3:45 on 16.Ne4 and let ...Rfd8/...Rxd3 win my queen; he finished with 4:47 left. Win on legality, guard counts (e2/g2 in the clamp), active conversion; do not burn minutes or shuffle a won pawn ending.
