# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B (...Ne7-f5, Qg4/g7 trick, ...f6 trap)
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & the one-move answer
- 3 rejected replies on ONE move = forfeit; an empty reply is the same. Walk EVERY move's path for MY OWN pieces FIRST - piece, ACTUAL square, destination, path, read off the BOARD. T50R1 FIVE invalid tries while +Q for R; T50R5 2 invalid. After ONE rejection never resend: list the LEGAL moves, pick a DIFFERENT piece/idea. T51R2 one invalid at move 11, cost nothing; T51R3/T51R4/T51R5 0 invalid.
- Position turns: write ONE-MOVE answer (recapture first, move the attacked piece) and send within 15 s.
- SELF-BAN: a move my scan called bad is DEAD.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; two units hitting is not safety. Quiet/tempo/retreat same sweep.
- Screens: his own piece between his heavy piece and my destination is NO shield - he can move it, capture included. T45R4 20...Qc7?? only his Bc5 blocked Qc2-c7; 21.Bxf8 and 22.Qxc7 won my QUEEN. MY guard is void if my own piece stands between: a queen on e7 in front of Bf8 leaves d6 unguarded (T51R1 15.Nd6+).
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f6<-e5, f5<-e6/g6, g5<-h6, d4<-c5/e5, h6<-g7. A moved pawn still attacks; never two pieces on one pawn's capture-square pair; a pawn's NEXT PUSH hits too. N-for-P is a loss.
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and every knight jump; a central knight jump needs EVERY recapturer. A FORK IS ONLY A FORK IF THE LANDING IS SAFE (T50R4 15...Ne4?? Nd6 took it) AND ITS TARGETS CANNOT STEP WITH TEMPO: T51R4 19.Nb6 Rb8 20.h3?? Bb7 - both targets escaped and the bishop came with a ...Bxg2 threat.
- WHITE e5 PAWN OWNS d6 AND f6 - no-go for every piece, QUEEN included. With my king castled Qg3 also PINS g7.
- Rooks and knights only where GUARDED. Before a rook CAPTURE walk pawn recaptures; before a ROOK CHECK ask can his king take. The recapturer must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH.
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY QUIET MOVE ELSEWHERE.
- TRADING A ROOK OFF MY KING'S RANK-2 SQUARE: name g2/h2's guards on the NEW board. T51R4 25.Rxf5? Qxf5 left g2 to the king alone; his Qd5+Bb7 then 27...Qxg2#.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP. With my king on g1/g2 and his queen on d5/f5 plus his bishop on b7, ...Qxg2 is mate unless a rook/queen stands on f2 or h3 is luft - play the luft EARLY, not at move 20.
- Qg4+Bh6 vs short-castled king (g7 king-guarded only): answer ...f5/...f6, ...Qf6, or trade queens. With my e8-king the Qxg7 net needs a PIECE on g7, not a pawn. Bd3+Qh6 vs MY short-castled king: Qxh7#.
- MY SHORT-CASTLED g8-KING behind g6+g7: his Qf6+Bh6 = Qg7#; with his Bf6, Qxg6+ Kf8 Qg7+ Ke8 Qg8#.
- MY e8-KING + MY Bf8 covering g7: keep f8 guarded too. His Qf6 hits h8 down a1-h8 once g7 is empty; his Bh6 then Qxf8# (Kxf8 illegal). T50R3 11...g6?? 15.Qf6 won h8; 16...Qb6?? 17.Bh6 Qxf8#. MY Bf8 covering d6 is void if my queen stands e7: T51R1 14...Qe7?? 15.Nd6+.
- Back rank: keep a rank-1 blocker or luft. A rook that is the LAST guard of an entry square must not leave for a pawn.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. Before ANY check write what captures the checker, KING included.
- QUEEN CHECKS: list EVERY block, not the one I expect. T51R3 25.Qd8+ allowed ...Bg8 as well as ...Bf8; Qxg8+ Kxg8 loses her. In a won position use the rook lift (Rf3-g3) instead of assuming mate in two.
- Q vs lone K: box with the queen a knight's move from his king, bring my king up, leave him a legal square every move - no stalemate.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. HIS BISHOP LANDING WITH TEMPO ON HER = she moves.
- QUEEN NEVER on an enemy bishop's diagonal or knight jump square, tempo/blocking a mate included.
- A QUEEN CAPTURE STILL COUNTS RECAPTURERS to her destination; a check that does not cover the mate square is no defence.
- BEFORE every queen/rook move list what it defended where it stood AND every enemy knight/pawn that hits the destination. A BLOCKED GUARD IS NOT A GUARD. A pawn push is not loose because I can take it - count HIS recapture.
- NEVER a queen on a PAWN's capture square, or where a pawn push hits her next move. DOWN = NO grabs; defend WITHOUT her.
- HIS QUEEN IN MY CAMP: list every unguarded piece of mine she reaches next move. T51R4 after ...Qxc2 she owned the 2nd rank and ...Qxe2 won my Be2 - I never listed e2. T51R5: his 18.Qxc5?? stepped onto my Qd5's capture square; I simply took her.

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN. Count EVERY recapturer, PAWNS FIRST; trace the chain to the end.
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P.
- NO ROOK TRADE WHILE BEHIND IN MATERIAL unless a piece comes back at once: T51R4 25.Rxf5? only fed his queen and removed g2's guard.
- AFTER A CAPTURE THAT WINS A PIECE, RESCAN FOR MY OWN LOOSE UNIT. After ANY trade re-count guards of ALL my units.
- QUEEN TRADE WHEN AHEAD: take his queen if she lands on my queen's ray/square; T51R5 18...Qxc5 won her on c5, then Q+R conversion.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE (count pieces, never prose; my 'I remain up' comments in T51R4 were false after ...Qxe2); rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND.
- CONVERTING: guard every unit, trade rooks evenly, two-rook ladder, Ra8#. Up: trade pieces not pawns, escort passers, stalemate-check. DOWN: keep the rook active, take the recapture. T51R2 pattern (up B+P): rook to the 6th/7th defended by bishop or pawn, eat loose h-/d-pawns, Rd8#. T51R3 (up Q+R): free pawns with queen checks, Nc7 fork, Qf6#. T51R5 (up Q+R): keep Re8 blocking rank checks, queen eats a2/b2/b1, then Rxf2+g4/Qe3+/Kh4/Rxh2# pattern.
- CLOCK - 3600+10: cap 30 s a move, routine 10-15 s, <15 min left -> 5-10 s. QUIET moves (luft, knight dance, rook shuffle) get 5-15 s and the FULL sweep: T51R4 burned 7:09 on 20.h3?? and 7:04 on 25.Rxf5??, was mated by move 27 with 30 min left to his 51. Long thinks never saved a move (T50R5 10:58 on ...Qe5; T50R4 10:01 on ...Ne4??). Fix = 15 s one-move list.

## Openings (only the lines I actually play)
- English as Black (WINS T38R2, T41R4, T45R4, T50R4, T51R5; T49R2 L by forfeit): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d4 (16 plies); ...Nbd7/...Re8/...Bf8/...Qc7/...Qb6, then ...c5 break or ...Ne5. T45R4: that break let Nxe5 Qxe5 f4 and Ba3 hit c5; ...Ne5 only with c5 safe and queen OFF the c-file (20...Qc7?? cost the queen). T49R2: 11...c5?! 12.dxc5 left d5 only Qd8, 13.Qxd5 won a pawn; guard d5 with ...Nc6/...Qb6. T50R4: a second ...Ne4 at move 15 lost a piece - play ...c5/...Qb6 first. T51R5: 11...c5?! was again inaccurate but GLM did not punish; ...Bf8/...Qb6 held, and after 16.Nxd5 Nxd5 17.Bxd5 Qxd5 18.Qxc5?? Qxc5 I won his queen. Keep Qd5 safe by checking his Rd1/blockers first (his d3 pawn blocked it here).
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); ...Na5, Bc2, ...c5, d4, Nbd2, ...Qc7, ...cxd4 Nc6. As Black move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo; Qc7 'defended' by Rc8 is still Rxc7. As White keep Rc1; no piece on a square his g6-pawn covers (f5/h5); no check he can capture.
- Four Knights Spanish B v SF19 (T45R6 L): ...Bb4 and castle; the ...Nd5 trade line runs ...e4, ...dxc6, ...exf3, ...Qxf3, ...dxc6 only; then ...d6/...Bf5/...Be6/...Bxc3, keep d4 defended. BANS: ...Qf6 while his queen can take f6; ...Re8?? (Rxe8+).
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then ...Qd7/...Rfe8/...Bb6/...d5. BANS: 10.d4?!, 12.c4?, 13.Bc2??, 14.Bg5??, 15.Nxe5??, 24.Qh5??, 14.Bf4??, b4 WHILE MY KNIGHT IS ON b3, queen on d5 while his f6-knight lives. T46R1: 17.Ne4?? ...Nf4xd3; 23.Nh4?? ...Rxd2. T45R7: 15.cxd4? IQP; 19.d5? ...Ne5. T44R2: 25.Rc1 was d1's only guard.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1. T51R2 WIN (m55): after 9.f4 b5, 10.e5! works - ...Nxd4 11.Qxd4, ...Nd5 12.Nxd5 exd5 13.Qxd5 wins a pawn because his c8-bishop cannot reach d5; 13...Bb7?? 14.Qxb7 Qc8 15.Qxc8 Raxc8 = +B+P, then rooks to the 7th/8th, f5-f6 wedge, Rg7, Rd8#. T51R3 WIN (m29): 9.f4 ...Nxd4/Bxd4 and ...b5 met by e5! and Nxb5!; his Qxc2?? lost the queen; Nc7 fork; Qf6#. T51R4 LOSS vs mirror: 9...Qc7 10...Nxd4 11...b5 12...Ne8 13...f6! held, then 15.Ne4 Bxd4+ 16.Qxd4 Qxc2! 17...Qxe2 won my loose Be2 (e2 and g2 are the targets once his queen sits on c7/c2) - the clamp works only while e2/g2 are guarded and his queen is not loose in my camp. vs Dragon block ...Qa5+ with Bd2/Bd1, never Qd2??. T50R1: early 13.f5?! before Bf3/Rf2 let ...exf5/...g6; 20.Bb6?? allowed ...Bc5+.
- Open Sicilian W vs 3...Nxd4 4...e5: 5.Nb5 a6 6.N5c3, then Nf6/Be2/Be7/short castle, Be3/Qd2/Nd5/f4; keep the c4-bishop safe.
- Taimanov B: 8.e5 Nd5 9.Qg4 (1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7, 16 plies): with my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8); never ...f5 while exf6 e.p. opens lines to my king. T50R3: 9...Bf8 right, but 11...g6?? opened a1-h8 - 15.Qf6 won h8, 16...Qb6?? 17.Bh6 Qxf8#. After ...Bf8 the bishop STAYS; no ...g6, no queen pawn-grabs; plan ...c5/...Be6/...Qb6 and trade his d3-bishop. T51R1 vs SF: 14...Qe7?? after Bd2 BLOCKED Bf8's guard of d6 - 15.Nd6+! won the game; keep d6 covered by a PIECE. Never take Bg5 with the queen while Nf7+ forks her. T49R4: play ...a6 BEFORE White's Nb5 (Nb5-c7 forks a8+e8); 11...Re8? 12.Nb5 Bd7?? 13.Nc7!.
- Caro B 4.Be2/4.Nf3: 3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 (12 plies). ...Nd7 then ...Ne7 (NEVER ...Ngf6 while e5 stands); recapture ...hxg6, never ...Nxg6?!. ...Be4 loses to Nxe4.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares. Give him NO loose unit; resolve central tension before castling. A piece down: aim for repetition. T45R6: took my hanging Re8 with check. T50R3: g7 covered by ...Bf8, then 11...g6?? let 15.Qf6 win h8. T50R5: Taimanov IQP level to 20; 20...d4?! lost the pawn, then passive moves lost the ending (0 illegal, 0 empty). T51R1: 14...Qe7?? screened Bf8 from d6; 15.Nd6+ won, 19...Qxg5?? 20.Nxf7+ won my queen. vs SF: no pawn push that becomes a target, keep d6/g7 covered by PIECES, 10-15 s.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square.
- Sonnet 5.5 (never beaten): banks clock, quiet space moves, then takes every UNGUARDED unit. T46R1: punished 17.Ne4?? with ...Nf4xd3, then 23.Nh4?? with ...Rxd2. 10-15 s from move 1, assume 60+ moves, keep a rank-1 blocker.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn/bishop diagonal or knight square, and any loose recapture. T44R2: +P in a rook ending, ...Rd1# when my c1-rook left d1. T45R2: punished my central knight jump and made two passers queen.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3, and the Chigorin; gives nothing loose.
- GLM 5.3 Flash: slow, illegal tries, miscounts material; hangs queens/rooks when worse, but punishes MY loose knight jumps. T50R1: I won his queen with Rxg6+! then forfeited at m40 (five illegal tries + empty). T51R2 (I won m55): my 10.e5 clamp, 13.Qxd5!; 4 invalid tries from him. T51R5 (I won as Black, English): he played the reversed-QGD English, spent 4-59 s, 2 invalid tries at 12.Rad1, then 18.Qxc5?? stepped into my Qd5 and lost his queen; I converted Q+R vs pawns cleanly (0 invalid, ~51 min left). vs GLM: 10-15 s sound moves, guard every unit, trade queens, take a queen that steps onto my queen's square/ray, ladder the rooks, NEVER end in an empty or illegal reply.
- Haiku 5.5: fast, solid Italian Pianissimo, no free material. T44R3 I FORFEITED (3 illegal tries) in a dead-equal position; T45R3 he beat me on the clock. 10-15 s a move, bank time, check legality twice.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov both ways, keeps units guarded. T50R2 I BEAT HIM (his 16.Qh6?? gxh6, +Q for R converted with ...Qxd4, ...Bxf2+, ...Re1#). T51R3 I won as White (e5 clamp, Nxb5!, Qf6# m29). T51R4 I LOST as White: his 9...Qc7 10...Nxd4 11...b5 12...Ne8 13...f6 held, then ...Qxc2/...Qxe2 won pawns and the loose Be2, and Qd5+Bb7 mated g2 after I traded Rf2. Win on legality, guard counts (e2/g2 in the clamp) and simple conversion; do not burn 40 min on routine moves.
