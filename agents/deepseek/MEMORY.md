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
- 3 rejected replies on ONE move = forfeit; empty = same. Walk MY OWN pieces' paths FIRST: piece, ACTUAL square, occupant, destination, path, off the board. After ONE rejection never resend: pick a DIFFERENT piece/idea. T53R1: 19 invalid, 10:04 on 14...Bxc3.
- Position turns: write the ONE-MOVE answer (recapture first, move the attacked piece), send within 15 s.
- SELF-BAN: a move my scan called bad is DEAD.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; two attackers is not safety. Quiet/retreat/tempo same sweep.
- Screens: his own piece between his heavy piece and my destination is NO shield - he can move it, capture included. MY guard is void if my own piece stands between. T45R4 20...Qc7?? only Bc5 blocked Qc2-c7; 21.Bxf8/22.Qxc7 won my queen.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, a3/c3<-b4, e5<-d4/f4, f6<-e5, f5<-e6/g6, g5<-h6, d4<-c5/e5, h6<-g7. A moved pawn still attacks; a pawn's NEXT PUSH hits too. T52R3 25.Ra3?? bxa3 lost a rook. T53R1 13...Qxd4?? 14.c3 hit Q+bishop = piece for pawn.
- HIS QUEEN ON A PAWN'S CAPTURE SQUARE IS FREE: T53R3 his ...Qe6?? dxe6 (Q for P). Same for any piece he 'activates' onto a pawn diagonal.
- HIS UNGUARDED BISHOP ON AN OPEN LINE FALLS: T53R3 ...Bf5?? had no guard and my rook owned the f-file: Rxf5 won a piece.
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and EVERY knight jump; a central jump needs EVERY recapturer. A FORK IS ONLY A FORK IF THE LANDING IS SAFE AND ITS TARGETS CANNOT STEP WITH TEMPO (T50R4 15...Ne4?? Nd6; T53R3 15.Nd5?? Nf6 recaptured).
- HIS KNIGHT ON A SQUARE WHOSE RECAPTURE HIS OWN PAWN BLOCKS IS FREE: T53R2 ...Nd5 hit Bc4 but his d6 pawn blocked Qd8, so Bxd5 won a knight; his ...Nxd4?? then cxd4 won another piece.
- A CENTRAL KNIGHT ON d5 COVERS e3, f4, c3, b4, b6, c7, e7, f6 - NEVER a queen on one of those. T53S2G1 27.Qf4?? Nxf4 won my queen; his Nd5 had already hit Qe3 once.
- WHITE e5 PAWN OWNS d6 AND f6 - no-go for every piece, QUEEN included.
- Rooks and knights only where GUARDED; before a rook CAPTURE walk pawn recaptures; before a ROOK CHECK ask can his king take. The recapturer must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH.
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY QUIET MOVE ELSEWHERE. T52S2A 20.Qd3?? was hit by ...Rfd8; 22.Bxb7?? ignored ...Rxd3.
- TRADING A ROOK OFF MY KING's rank-2 square: name g2/h2's guards on the NEW board. T51R4 25.Rxf5? Qxf5, 27...Qxg2#.
- PAWN HITS TWO PIECES: move the MORE valuable and count the recapture.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP. King on g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2 mate unless a rook stands f2 or h3 is luft - play the luft EARLY.
- Qg4+Bh6 vs short-castled king (g7 guarded only by the king): answer ...f5/...f6, ...Qf6, or trade queens. With my e8-king the Qxg7 net needs a PIECE on g7, not a pawn. Bd3+Qh6 vs MY short-castled king: Qxh7#.
- MY SHORT-CASTLED g8-KING behind g6+g7: his Qf6+Bh6 = Qg7#. MY e8-KING + Bf8 covering g7: keep f8 guarded too; his Qf6 hits h8 down a1-h8 once g7 empties, Bh6 then Qxf8# (T50R3). Bf8's guard of d6 is void if my queen stands e7 (T51R1 14...Qe7?? 15.Nd6+).
- Back rank: keep a rank-1 blocker or luft. A rook that is the LAST guard of an entry square must not leave for a pawn.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. Before ANY check write what captures the checker, KING included.
- QUEEN CHECKS: list EVERY block. T51R3 25.Qd8+ allowed ...Bg8 as well as ...Bf8.
- WON POSITION: prefer the forcing check over a slow lift - T53R2 28.Rf3+ Rf7 29.Qxf7#.
- Q vs lone K: box with the queen a knight's move from his king, bring my king up, leave him a legal square every move - no stalemate.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. HIS BISHOP LANDING WITH TEMPO ON HER = she moves.
- QUEEN NEVER on an enemy bishop's diagonal or knight jump square, tempo/blocking a mate included. T53R2 his ...Qe6?? stepped onto my Bb3's diagonal: Bxe6 won her; 27.Qf4?? into his Nd5's jump square lost her.
- BEFORE every queen/rook move list what it defended where it stood AND every enemy knight/pawn that hits the destination. A BLOCKED GUARD IS NOT A GUARD. A pawn push is not loose because I can take it - count HIS recapture.
- NEVER a queen on a PAWN's capture square, or where a pawn push hits her next move. DOWN = NO grabs; defend WITHOUT her.
- HIS QUEEN IN MY CAMP: list every unguarded piece of mine she reaches next move (T51R4 ...Qxc2 then ...Qxe2). A queen hit by a rook must leave BOTH the file AND the rank.

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE PIECE. Count EVERY recapturer, PAWNS FIRST; trace the chain to the end (T53R2 Bxd5: his queen could not reach d5 through d6).
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P. NO ROOK TRADE WHILE BEHIND unless a piece comes back at once (T51R4 25.Rxf5?).
- A ROOK THAT GRABS IN HIS CAMP MUST BE DEFENDED: T53S2G1 26.Rxa6?? Qxa6 = a whole rook for a pawn. Before any grab there count his recapturers on that square, QUEEN included; self-justifying 'it must be mate' prose is not a count.
- AFTER A CAPTURE THAT WINS A PIECE, RESCAN FOR MY OWN LOOSE UNIT; after ANY trade (or capture that unscreens a line) re-count guards of ALL my units (T50R4 14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5).
- QUEEN TRADE WHEN AHEAD: take his queen if she lands on my queen's ray/square (T51R5 18...Qxc5).
- UP THE EXCHANGE WITH QUEENS ON: no pawn-grabs with a rook, keep both rooks guarded, trade rooks on my own terms, then bank. T53S2G1: up R for N at move 24, then Rxa6?? and Qf4?? gave back rook AND queen.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE (count pieces, never prose); rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND. KEEP THE WON QUEEN off his rook's rank/file and off pawn capture squares all the way to mate (T53R3).
- CONVERTING UP: guard every unit, trade pieces not pawns, escort passers, stalemate-check, 5-15 s a move. Models: T53R3 (trade his last rook WITH CHECK, check again on the open file, queen double attack on his loose bishop+pawn, mate - 5-15 s a move); T53R2 (Rf3+ Rf7 Qxf7#); T52R1 (Qd8+/Rg3+/Qg8#); T52R5 (...Rc2+ Kg1 ...Re1#).
- BIG LEAD = SIMPLIFY FAST: trade queens/rooks when safe, keep every unit guarded, make luft, 5-10 s a move (T52S2A: up Q+2R+2B+N and flagged).
- CLOCK - 3600+10: cap 30 s, routine 10-15 s, <15 min left -> 5-10 s. QUIET moves get 5-15 s and the FULL sweep: T53S2G1 burned 5:20 on 17.Bf3, 9:14 on 20.Nc5, 5:05 on 21.Rd6, 3:41 on 18.Bxb7, 3:22 on 27.Qf4?? - the losing queen move took 1 s for him to refute. Long thinks never saved a move (T53R2 14.d4?! 2:08; T53R3 3:21 on the ...Bf5?? that hung). Armageddon White 10 min: 10-15 s from move 1, winning lead 5-8 s, under 3 min 3 s.

## Openings (only the lines I actually play)
- English as Black (WINS T38R2, T41R4, T45R4, T50R4, T51R5, T52R5; T49R2 L forfeit): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (16 plies); ...Bf5/...Nbd7/...Re8/...Qb6/...Rac8/...Nf8, then ...c5 only when d5 is guarded or ...Ne5 safe. His slow queen moves and ...h6/...Nf8 let me keep a big edge; his Bxh6?? met gxh6. ...c5?! too early lets dxc5 and Qxd5 if d5 loses guards; ...Ne4 only with c5 safe and queen off the c-file.
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); ...Na5, Bc2, ...c5, d4, Nbd2, ...Qc7, ...cxd4 Nc6. As Black move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo; Qc7 'defended' by Rc8 is still Rxc7. As White keep Rc1; no piece on a square his g6-pawn covers (f5/h5); no check he can capture.
- Four Knights Spanish as Black (T45R6 L, T53R1 L): ...Bb4 and castle; in the ...Nd5 trade line the order ...e4/...dxc6/...exf3/...Qxf3/...dxc6 is the only safe one; then ...d6/...Bf5/...Be6, keep d4 defended. T53R1 13...Qxd4?? met 14.c3 (queen + bishop hit) = piece for pawn; BANS: ...Qf6 while his queen can take f6, ...Re8?? (Rxe8+), no queen grab onto a pawn's capture square.
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then ...Qd7/...Rfe8/...Bb6/...d5. Branch 7...Bg4 8.Re1 a6 9.h3 Bxf3 10.Qxf3 Qd7: Nb3/Bb6, Be3/Bxe3 Qxe3, then d4 with Re1/Rad1. T53R2 WIN v GLM: his ...Nd5 hit my Bc4 but his own d6 pawn blocked Qd8, so Bxd5 won a knight, his ...Nxd4?? cxd4 another piece, then ...Qe6?? Bxe6 won the queen; 28.Rf3+ Rf7 29.Qxf7#. 14.d4?! marked ?! - push it only after full development. BANS: 10.d4?!, 12.c4?, 13.Bc2??, 14.Bg5??, 15.Nxe5??, 24.Qh5??, b4 WHILE MY KNIGHT IS ON b3, queen on d5 while his f6-knight lives.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1/Kh1. T53R3 WIN v mirror (0 invalid): his ...Qc7/...Nxd4/...a6/...e5 break was sound and level; the win came from his loose units - ...Bf5?? Rxf5, ...Qe6?? dxe6, then Rxf8+/Rf1+/Qd7 hit Be7+b7, Rxa8 and mate. 15.Nd5?? was my only mark: it hit Qc7+Be7 but his Nf6 recaptured. T53S2G1 LOSS v mirror: 11.e5! Ne8 (his best) 12.Qd2 Bc5 13.Be3 gave me a big edge, and 24.Nxf8 Rxf8 left me up the exchange with queens on - then 26.Rxa6?? Qxa6 and 27.Qf4?? Nxf4 threw it away. When up the exchange here: Rc6-c4/Rd4+Re1, trade rooks on my terms, never grab a6, never a queen on his d5-knight's squares. T51R2/T51R3/T52R1 WINS: after 9.f4 b5, 10.e5! (...Nxd4 11.Qxd4; ...Nd5 12.Nxd5 exd5 13.Qxd5 wins a pawn, his c8-bishop cannot reach d5); then rooks to the 7th/8th, f5-f6, Rd8#; after ...Bc5 do NOT play 12.Qd2??. T51R4 LOSS vs mirror: his 9...Qc7 10...Nxd4 11...b5 12...Ne8 13...f6! held; 16.Qxd4 Qxc2! 17...Qxe2 won my loose Be2. T52R3: 25.Ra3?? bxa3 lost a rook; 19.f5?! premature.
- Sicilian W, his ...Nxd4 + ...e5: Nb5 with a6 answered by N5c3, then Nf6/Be2/Be7/short castle, Be3/Qd2/Nd5/f4; keep the c4-bishop safe.
- Alapin W vs mirror (T52S2A): after ...cxd4 recapture with cxd4 (never Nxd4 first); ...Nxd4?? loses a knight to Nxd4 when his d5-knight screens Qd6. A won position is still a clock position.
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies); 9.Qg4. With my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8); never ...f5 while exf6 e.p. opens lines to my king. T50R3: 11...g6?? opened a1-h8 - 15.Qf6 won h8, 16...Qb6?? 17.Bh6 Qxf8#. T51R1 vs SF: 14...Qe7?? after Bd2 BLOCKED Bf8's guard of d6 - 15.Nd6+! won. Never take Bg5 with the queen while Nf7+ forks her. T49R4: ...a6 BEFORE White's Nb5; 11...Re8? 12.Nb5 Bd7?? 13.Nc7!. T52S2G1 vs mirror: 18...Qxb2 19...Qc3! won a pawn; keep ...c4 guarded.
- Caro B 4.Be2/4.Nf3: 3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 7.Nh4 Bg6 8.O-O Nf5 (12 plies). ...Nd7 then ...Ne7 (NEVER ...Ngf6 while e5 stands); recapture ...hxg6, never ...Nxg6?!. ...Be4 loses to Nxe4. T52R2 vs SF: 12.f4 c5 13.g4! hits Bf5 - move it (...Bg6/...Bxf5) BEFORE ...cxd4; 13...cxd4?! 14.Nxd5! exd5 15.gxf5 and his d6/e6 pawns roll.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares. Give him NO loose unit; resolve central tension before castling. A piece down: aim for repetition. T45R6: took my hanging Re8 with check. T50R3: g7 covered by ...Bf8, then 11...g6?? let 15.Qf6 win h8. T51R1: 14...Qe7?? screened Bf8 from d6; 15.Nd6+ won, 19...Qxg5?? 20.Nxf7+ won my queen. T52R2: his 13.g4! hit my Bf5, 14.Nxd5! gave him the d/e passers. T53R1: Four Knights; 13...Qxd4?? into 14.c3 lost a piece, 19 invalid replies. vs SF: no pawn push that becomes a target, keep d6/g7 covered by PIECES, 10-15 s.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square.
- Sonnet 5.5 (never beaten): banks clock, quiet space moves, then takes every UNGUARDED unit. T46R1: punished 17.Ne4?? with ...Nf4xd3, then 23.Nh4?? with ...Rxd2. 10-15 s from move 1, assume 60+ moves, keep a rank-1 blocker.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn/bishop diagonal or knight square, and any loose recapture. T44R2: +P in a rook ending, ...Rd1# when my c1-rook left d1.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3, and the Chigorin; gives nothing loose.
- GLM 5.3 Flash (T53R2, T51R5, T52R1, T52R5 all my wins; T50R1 I forfeited): slow, miscounts material, hangs queens/rooks/knights when worse or even, but punishes MY loose knight jumps. 10-15 s sound moves, guard every unit, trade queens, take any queen on my ray and any piece whose recapture his own pawn blocks, NEVER an empty or illegal reply.
- Haiku 5.5: fast, solid Italian Pianissimo, no free material; I forfeited T44R3 and lost T45R3 on the clock. 10-15 s a move, bank time, check legality twice.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov both ways; keeps units guarded but leaves an 'active' piece loose (...Bf5??) and can put his queen on my pawn's capture square (...Qe6??). I won T50R2, T51R3, T51S2G1, T53R3; I lost T51R4, T52R3, T52S2A, T53S2G1. T53S2G1: I was up the exchange at move 24 and then Rxa6??/Qf4?? gave back rook and queen - against him convert with guarded rooks and a queen off every knight/pawn square, no grabs, no 5-9 minute thinks. Win on legality, guard counts, active conversion.
