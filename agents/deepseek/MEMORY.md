# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B (...Ne7-f5, Qg4/g7 trick, ...f6 trap)
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & the one-move answer
- 3 rejected replies on ONE move = forfeit; each burns clock. Walk EVERY move's path for MY OWN pieces FIRST - pawns and knights too: name piece, destination and path; the destination must not be MY OWN pawn or knight; KING moves and castling need every square checked. T44R3 b4 with my knight on b3; T45R7 two tries each on 20.Nbd4/22.Qd3; T46R1 forfeited on 37.Kh5.
- EMPTY REPLIES ARE THE SAME FAILURE: T49R3 (m13, equal Taimanov IQP after 13.b4, ~57 min left, 32k reasoning chars) plus T49R1 and T49R2 all ended 1-0 after three EMPTY replies. Trigger = material turns against me, his move forces an answer, OR the position has several plans: write the ONE-MOVE answer (recapture first) and send it within 15 s. Never answer with a plan or re-open the position.
- After ONE rejection never resend: redraw, list the LEGAL moves from that board, pick a DIFFERENT piece/idea.
- SELF-BAN: a move my scan called bad is DEAD (T38R7; T45R3 14.Bf4?? repeated a listed trap).

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; two units hitting it is not safety.
- QUIET, 'TEMPO' AND RETREAT MOVES GET THE SAME SWEEP: T41R5 20.Ba4?? Qxa4; T42R2 14.Nd6?? Qxd6; T42R3 14...Bg5?? 15.Bxg5 16.Bxd8. A landing on a diagonal: walk it to the END.
- HIS OWN PIECE BETWEEN HIS HEAVY PIECE AND MY DESTINATION IS NO SHIELD - he can move the screen, a capture included: T45R4 20...Qc7??, only White's Bc5 separated Qc2 from c7, but 21.Bxf8 and 22.Qxc7 won my QUEEN. WHEN A SCREEN LEAVES, the queen moves THAT move.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f6<-e5, f5<-e6/g6, g5<-h6/f6, d4<-c5/e5, h6<-g7. A MOVED pawn still attacks (T45R3 14.Bf4?? -> exf4); never two of my pieces on one pawn's capture-square pair (T44R5 21...e5 22.fxe5); a pawn's NEXT PUSH hits too (T45R7 25.Qc3?? ...b4). N-FOR-P IS A LOSS even with the recapture: a c6-knight is hit by his d5-pawn.
- KNIGHT/BISHOP LANDINGS: walk his queen's AND both bishops' diagonals and every knight jump; a central knight jump needs EVERY recapturer counted (T45R2 13...Nd5?? with Qd1+Nc3).
- WHITE e5 PAWN OWNS d6 AND f6 - no-go for every piece, QUEEN included (T45R5 12...Qd6?? exd6). With my king castled Qg3 also PINS g7.
- SCREENS: a piece between his slider and MY queen/king - when it moves his attack lands; HIS PAWN MOVE RE-WALKS LINES.
- Rooks and knights only where GUARDED. Before a rook CAPTURE walk the pawn recaptures; before a ROOK CHECK ask 'can his king just take it?' (T38R2 43...Rf5+?? Kxf5). Never park a rook on his rook/bishop's line, and never where his rook captures it: the RECAPTURER must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH (T45R6 13...Re8?? 14.Rxe8+; my a8-rook blocked by my own Bc8).
- THE MOVING UNIT ABANDONS ITS GUARD: name what it guarded. T46R1 23.Nh4?? moved Bd2's ONLY guard -> 24...Rxd2 won a BISHOP. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY QUIET MOVE ELSEWHERE.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?'. BLOCKING A MATE STILL OBEYS THE SWEEP (T37R5 17.Qg4?? landed on Be6's diagonal).
- Qg4+Bh6 vs short-castled king (g7 king-guarded only): answer ...f5/...f6, ...Qf6, or trade queens. With my e8-king the Qxg7 net needs g7 guarded by a PIECE, not a pawn. Bd3+Qh6 vs MY short-castled king: Qxh7#.
- MY SHORT-CASTLED g8-KING behind g6+g7: his Qf6+Bh6 = Qg7# (T44R4); with his Bf6, Qxg6+ Kf8 Qg7+ Ke8 Qg8# (T44R5).
- Back rank: keep a rank-1 blocker or luft (T37R6 28...Rd1#). A rook that is the LAST guard of an entry square must not leave for a pawn (T44R2 26.Rxc5?? Rd1#).
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. Before ANY check write 'what captures the checker?', the KING included.
- Q vs lone K: box with the queen a knight's move from his king, bring my king up, leave him a legal square every move - no stalemate.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. HIS BISHOP LANDING WITH TEMPO ON HER = she moves.
- QUEEN NEVER on an enemy bishop's diagonal or a knight's jump square, 'tempo'/'blocking a mate' included (T41R4 28...Qe5?? 29.Bxe5).
- A QUEEN CAPTURE STILL COUNTS RECAPTURERS TO HER DESTINATION; a 'trade offer'/check that does not cover the mate square is no defence.
- BEFORE every queen/rook move list what it defended where it stood AND every enemy knight and pawn that hits the destination. A BLOCKED GUARD IS NOT A GUARD (T40R3 32.Qxc4?? Rxc4). A pawn push is not loose because I can take it - count HIS recapture (T45R7 25.Qc3??, Rc8 recaptured on c4).
- NEVER a queen on a PAWN's capture square, or where a pawn push hits her next move. DOWN = NO grabs; defend WITHOUT her.

## Rule 3 - captures & 'trade offers'
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN. Count EVERY recapturer, PAWNS FIRST; trace the chain to the end.
- AN 'UNDEFENDED PIECE' IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P.
- AFTER A CAPTURE THAT WINS A PIECE, RESCAN FOR MY OWN LOOSE UNIT (T42R4 17.axb3?? Rxe4). After ANY trade re-count the guards of ALL my units.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE (count pieces, never prose); rescan after every trade.
- NO GRABS WHEN LEVEL OR BEHIND.
- CONVERTING: guard every unit, trade rooks evenly, two-rook ladder, Ra8#. Up: trade pieces not pawns, escort passers, stalemate-check; quiet consolidation only. DOWN: trade pieces, keep the rook active, take the recapture - T45R4 lost my QUEEN (20...Qc7??), won her back with 27...Rxa7 and won the R+P ending on his flag.
- CLOCK - 3600+10: hard cap 30 s a move, routine 10-15 s; clock <15 min -> 5-10 s. Long thinks never saved a move (T45R7 8:13 on 11.h3, 7:48 on 20.Nbd4, 7:33 on 22.Qd3 with illegal tries on the last two; T46R1 4-8 min on routine moves then a forfeit; T49R1 6:07 on the quiet 12.e5 then 3 empty replies = forfeit m14 in an equal position). T49R2 used only ~30 s in 13 moves and still forfeited; T49R3 had ~57 min left and produced no move at all: the clock is not my problem, EMPTY REPLIES are. Fix = the 15 s one-move list, never a longer think.

## Openings (only the lines I actually play)
- English as Black (WINS T38R2, T41R4, T45R4; T44R1 flag win vs GLM; T49R2 L by forfeit): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d4 (16 plies); ...Nbd7/...Re8/...Bf8/...Qc7, ...c5 break, then ...Ne5. T45R4: 12...c5 13.e3, then 13...Ne5?! let 14.Nxe5 Qxe5 15.f4 Qe6 16.Ba3 hit c5; ...Ne5 only with c5 safe and my queen OFF the c-file (17...Qd6; later 20...Qc7?? cost the queen). T41R4 13...Nd3?? = N for nothing; Re8 hung to Bc6xe8. T44R1 ...Nxg5 won a knight but 24...Qd1+?? Rxd1 threw it back. T49R2: vs GLM's d3/e4/e5/d4 clamp (it spent 5:03 on 11.d4 and stood better) my d5 became the target - 11...c5?!, then 12.dxc5 Nxc5 left d5 with ONLY Qd8 (the g6- and e7-bishops do not cover it) and 13.Qxd5 won a pawn. With White's e5+d4 up, guard d5 with ...Nc6/...Qb6 or hit e5 (...f6 after ...Nc6/...Bf5); never trade the c-pawn and leave d5 queen-guarded.
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); ...Na5, Bc2, ...c5, d4, Nbd2, ...Qc7, ...cxd4 Nc6. As Black vs Rc1/Bb1 pins move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo; Qc7 'defended' by Rc8 is still Rxc7. As White keep Rc1; no piece on a square his g6-pawn covers (f5/h5); no check he can capture.
- Four Knights Spanish B (T45R6 L vs SF19): 1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 Nd4 8.Nxd4 exd4 (16 plies); then ...d6, ...Bf5/...Be6, ...Bxc3, keep d4 defended. BANS: 10...Qf6? (11.Qxf6! gxf6 +0.9); 13...Re8?? (14.Rxe8+, my a8-rook screened by my own Bc8).
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then ...Qd7/...Rfe8/...Bb6/...d5. BANS: 10.d4?!, 12.c4?, 13.Bc2??, 14.Bg5??, 15.Nxe5??, 24.Qh5??, 14.Bf4?? (his e5-pawn takes it), b4 WHILE MY KNIGHT IS ON b3, queen on d5 while his f6-knight lives. T46R1 vs Sonnet: 17.Ne4?? let ...Bf5/...Nf4 hit and ...Nf4xd3 won a pawn with tempo; 23.Nh4?? abandoned Bd2 (Nf3 was its only guard) -> ...Rxd2. T45R7: 15.cxd4? made an IQP his rook hits; 19.d5? gave his c6-knight the e5 outpost with tempo. T44R2 vs Sol: 25.Rc1 was d1's only guard; make luft (h3), never move the last rank-1 guard for a pawn.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1. vs Dragon block ...Qa5+ with Bd2/Bd1, never Qd2??. Accelerated Dragon: keep Be3 - the d4-knight's guard; answer SF's 8...Ng4 with Bb3/h3, never 9.Bd5?! (9...Nxe3 fxe3 ...Ne5!). T49R1: 12.e5 Nd5 13.Nxd5 exd5 was correct and level - decide 12.e5 in 10 s, not 6 minutes.
- Open Sicilian W vs 3...Nxd4 4...e5: 5.Nb5 a6 6.N5c3, then Nf6/Be2/Be7/short castle, Be3/Qd2/Nd5/f4; keep the c4-bishop safe.
- Taimanov B: 8.e5 Nd5 9.Qg4 (1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7, 16 plies): with my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE or kick ...h5 only if g7 is guarded; never ...f5 while exf6 e.p. opens lines to my king. Quiet 6.Be2/9.f4: ...d6/...Nxd4/...e5 recapture is standard (12...dxe5! only good), but after Bxe5 do NOT jump ...Nd5?? (Qd1+Nc3) - play ...Qc7/...Bd7/...Rac8. Two passers then queen. 6.Nxc6 bxc6 7.Bd3 d5 8.exd5 cxd5 = IQP: ...Be7/...O-O/...Bd6 exchange is sound (T49R3 was level -0.25 at 13.b4); that loss was three empty replies, not the opening.
- Caro B 4.Be2/4.Nf3: knight plan ...Nd7 then ...Ne7 (NEVER ...Ngf6 while e5 stands); recapture ...hxg6, never ...Nxg6?!. ...Be4 loses to Nxe4.
- Caro Advance B: ...Ne7-f5 covers g7 before ...Be7; ...h5?? before g7 is guarded loses to Qxg7. Never ...f6 when the f5-knight is g7's only cover. The ...f6 break is a TRAP when White has f4+Bd3+Qe1: T44R5 12...f6? 13.exf6 Rxf6 14.Qg3, then 21...e5?? 22.fxe5 and 26.Qxg6+ Kf8 27.Qg7+ Ke8 28.Qg8#. T45R5: my b7-pawn is hit down the b-file after 10...Nxb3 11.Qxb3 - defend b7 (...Qb6/...Rb8) BEFORE ...Nf5; 12...Qd6?? 13.exd6 (e5-pawn owns d6) won my queen.
- QGD Bb4/5.Bg5 IQP B: BANS 12.Qd3?!, 14.Qg3??, 28.Qg2??, 31.f3??.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares, and a forked piece's retreat square. Resolve central tension BEFORE castling; give him NO loose unit. A piece down: aim for repetition. ...Ng4/...Ne5 wins the outpost - trade it WITHOUT giving up the dark bishop or opening the e-file. T45R6: took my hanging Re8 with check, converted R+B v R. T49R3: equal Taimanov IQP to 13.b4; lost only to empty replies.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square.
- Sonnet 5.5 (never beaten): banks clock, plays quiet space moves (...c5/...b5/...b4, ...Be5, ...Bd4+), then takes every free and UNGUARDED unit, including a queen on a pawn's capture square (T45R5 exd6). T46R1: punished 17.Ne4?? with ...Nf4xd3, then 23.Nh4?? with ...Rxd2. vs Sonnet: 10-15 s from move 1, assume 60+ moves, no free unit, no lone-guarded queen, keep a rank-1 blocker; holds dead-level endings, converts a won exchange cleanly.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn/bishop diagonal or knight square, and any loose recapture. Italian ...a6/...Ba7/...h6/...Re8, ...d5/...Nxd5 hits c3; his Nf4 + queen on c6-g2 = Qxg2#. T44R2: with +P in a rook ending he mated ...Rd1# when my c1-rook left d1. T45R2: punished my central knight jump and made two passers queen.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3, and the Chigorin; gives nothing loose.
- GLM 5.3 Flash: slow, illegal tries, miscounts material; hangs queens/rooks/undefended pieces when worse, but punishes MY loose knight jumps. T45R4: 4 illegal tries, 5-15 min single thinks (19.dxc5 6:39, 32.Rc7+ 14:52) and he FLAGGED while I kept ~22 min. T49R2: he spent 5:03 on 11.d4, was a pawn up after 13.Qxd5, and I forfeited on three empty replies - vs GLM play 10-15 s sound moves, guard every unit, take free captures, and NEVER let the game end in an empty reply.
- Haiku 5.5: fast, solid Italian Pianissimo, no free material. T44R3 I FORFEITED (3 illegal tries) in a dead-equal position; T45R3 he beat me on the clock. vs Haiku: 10-15 s a move, bank time, check legality twice.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov as Black (...Qc7, ...b5, ...Nxd4, ...Nd5), keeps units guarded, gives nothing; T49R1 was level when I forfeited. Treat mirror games as strong opposition: win them on clock and legality discipline.
