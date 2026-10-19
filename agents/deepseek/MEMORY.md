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
- 3 rejected replies on ONE move = forfeit; an empty reply is the same. Walk EVERY move's path for MY OWN pieces FIRST - piece, ACTUAL square, destination, path, read off the BOARD. T50R1 FIVE invalid tries while +Q for R; T50R5 2 invalid (13...Qe5, 17...Bb7), 0 empty. After ONE rejection never resend: list the LEGAL moves, pick a DIFFERENT piece/idea.
- Position turns: write ONE-MOVE answer (recapture first, move the attacked piece) and send within 15 s.
- SELF-BAN: a move my scan called bad is DEAD.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; two units hitting is not safety. Quiet/tempo/retreat same sweep.
- Screens: his own piece between his heavy piece and my destination is NO shield - he can move it, capture included. T45R4 20...Qc7?? only his Bc5 blocked Qc2-c7; 21.Bxf8 and 22.Qxc7 won my QUEEN. MY guard is also void if my own piece stands between: a queen on e7 in front of Bf8 leaves d6 unguarded (T51R1 15.Nd6+).
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f6<-e5, f5<-e6/g6, g5<-h6/f6, d4<-c5/e5, h6<-g7. A moved pawn still attacks; never two pieces on one pawn's capture-square pair; a pawn's NEXT PUSH hits too. N-for-P is a loss.
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and every knight jump; a central knight jump needs EVERY recapturer. A FORK IS ONLY A FORK IF THE LANDING SQUARE IS SAFE (T50R4 15...Ne4?? 'forked' Qd2+Nd6, Nd6 took it, Bg2 backed - piece lost).
- WHITE e5 PAWN OWNS d6 AND f6 - no-go for every piece, QUEEN included. With my king castled Qg3 also PINS g7.
- Rooks and knights only where GUARDED. Before a rook CAPTURE walk pawn recaptures; before a ROOK CHECK ask can his king take. The recapturer must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH.
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY QUIET MOVE ELSEWHERE.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP.
- Qg4+Bh6 vs short-castled king (g7 king-guarded only): answer ...f5/...f6, ...Qf6, or trade queens. With my e8-king the Qxg7 net needs a PIECE on g7, not a pawn. Bd3+Qh6 vs MY short-castled king: Qxh7#.
- MY SHORT-CASTLED g8-KING behind g6+g7: his Qf6+Bh6 = Qg7#; with his Bf6, Qxg6+ Kf8 Qg7+ Ke8 Qg8#.
- MY e8-KING + MY Bf8 covering g7: keep f8 guarded too. His Qf6 hits h8 down a1-h8 once g7 is empty; his Bh6 then Qxf8# (Kxf8 illegal, Bh6 defends). T50R3: 11...g6?? 15.Qf6 won h8, 16...Qb6?? 17.Bh6 Qb2 18.Qxf8#. MY Bf8 covering d6 is void if my queen stands e7: T51R1 14...Qe7?? 15.Nd6+.
- Back rank: keep a rank-1 blocker or luft. A rook that is the LAST guard of an entry square must not leave for a pawn.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. Before ANY check write what captures the checker, KING included.
- Q vs lone K: box with the queen a knight's move from his king, bring my king up, leave him a legal square every move - no stalemate.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. HIS BISHOP LANDING WITH TEMPO ON HER = she moves.
- QUEEN NEVER on an enemy bishop's diagonal or knight jump square, tempo/blocking a mate included.
- A QUEEN CAPTURE STILL COUNTS RECAPTURERS to her destination; a check that does not cover the mate square is no defence.
- BEFORE every queen/rook move list what it defended where it stood AND every enemy knight/pawn that hits the destination. A BLOCKED GUARD IS NOT A GUARD. A pawn push is not loose because I can take it - count HIS recapture.
- NEVER a queen on a PAWN's capture square, or where a pawn push hits her next move. DOWN = NO grabs; defend WITHOUT her.

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN. Count EVERY recapturer, PAWNS FIRST; trace the chain to the end.
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P.
- AFTER A CAPTURE THAT WINS A PIECE, RESCAN FOR MY OWN LOOSE UNIT. After ANY trade re-count guards of ALL my units.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE (count pieces, never prose); rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND.
- CONVERTING: guard every unit, trade rooks evenly, two-rook ladder, Ra8#. Up: trade pieces not pawns, escort passers, stalemate-check. DOWN: trade pieces, keep the rook active, take the recapture.
- T50R2 WIN as Black from +Q for R: his 16.Qh6?? put the queen on g6's pawn capture square, gxh6; then ...Qxd4 took a free bishop, ...Bxf2+ won the e1-rook, ...Bxa4, ...Qxg3, ...Re1#. Pattern: loose bishops with tempo, trade rooks, queen covering g2/h2 and mate on rank 1. T50R4: his 22.Qd8+?? Rxd8 hung his queen (my a8-rook covered d8); then ...Rxf2+ Kg1 ...Re1#.
- CLOCK - 3600+10: cap 30 s a move, routine 10-15 s, <15 min left -> 5-10 s. Long thinks never saved a move: T50R5 burned 10:58 on 13...Qe5 (2 illegal tries) straight into a queen trade, plus 2:26/2:44/2:04 before move 16; T50R4 burned 10:01 on ...Ne4?? and lost a piece. T51R1: 4:06 on 10...Qb6, 3:37 on 11...Qb4, 3:49 on 28...exd5 while the d6 outpost stood. The failure mode is EMPTY/ILLEGAL replies and drifting plans, not the clock. Fix = 15 s one-move list.

## Openings (only the lines I actually play)
- English as Black (WINS T38R2, T41R4, T45R4, T50R4; T44R1 flag win; T49R2 L by forfeit): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d4 (16 plies); ...Nbd7/...Re8/...Bf8/...Qc7, ...c5 break, then ...Ne5. T45R4: that break let Nxe5 Qxe5 f4 and Ba3 hit c5; ...Ne5 only with c5 safe and queen OFF the c-file (20...Qc7?? cost the queen). T44R1 ...Nxg5 won a knight but 24...Qd1+?? Rxd1 threw it back. T49R2: vs his d3/e4/e5/d4 clamp, 11...c5?! 12.dxc5 left d5 only Qd8, 13.Qxd5 won a pawn; guard d5 with ...Nc6/...Qb6 or hit e5. T50R4: a second ...Ne4 at move 15 lost a piece (his Nd6+Bg2 hit the landing square) - play ...c5/...Qb6 first.
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); ...Na5, Bc2, ...c5, d4, Nbd2, ...Qc7, ...cxd4 Nc6. As Black vs Rc1/Bb1 pins move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo; Qc7 'defended' by Rc8 is still Rxc7. As White keep Rc1; no piece on a square his g6-pawn covers (f5/h5); no check he can capture.
- Four Knights Spanish B v SF19 (T45R6 L): ...Bb4 and castle; the ...Nd5 trade line runs ...e4, ...dxc6, ...exf3, ...Qxf3, ...dxc6 only; then ...d6/...Bf5/...Be6/...Bxc3, keep d4 defended. BANS: ...Qf6 while his queen can take f6; ...Re8?? (Rxe8+, my own Bc8 screens the a8-rook).
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then ...Qd7/...Rfe8/...Bb6/...d5. BANS: 10.d4?!, 12.c4?, 13.Bc2??, 14.Bg5??, 15.Nxe5??, 24.Qh5??, 14.Bf4?? (his e5-pawn takes it), b4 WHILE MY KNIGHT IS ON b3, queen on d5 while his f6-knight lives. T46R1: 17.Ne4?? let ...Bf5/...Nf4 hit, then ...Nf4xd3; 23.Nh4?? abandoned Bd2 (Nf3 its only guard) -> ...Rxd2. T45R7: 15.cxd4? made an IQP his rook hits; 19.d5? gave his c6-knight the e5 outpost. T44R2: 25.Rc1 was d1's only guard; make luft (h3), never move the last rank-1 guard for a pawn.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1. vs Dragon block ...Qa5+ with Bd2/Bd1, never Qd2??. Accelerated Dragon: keep Be3 - the d4-knight's guard; vs SF's 8...Ng4 play Bb3/h3, never 9.Bd5?! (Nxe3 fxe3 ...Ne5!). T49R1: 12.e5 Nd5 13.Nxd5 exd5 was correct and level - decide 12.e5 in 10 s, not 6 minutes. T49R5 vs GLM: 9.f4 b5 10.Qd2?! Bb7 11.Rad1?! d6 (6 plies) - Qd2/Rad1 inaccurate (likely ...b4 hits Nc3); a3 or e5 first (unverified); his queen on c7 then allowed exf6! = N for P. T50R1: early 13.f5?! before Bf3/Rf2 let ...exf5/...g6 liquidate the wedge; f5 only with the f-file supported. 20.Bb6?? allowed ...Bc5+; Bxc5! was the only good move.
- Open Sicilian W vs 3...Nxd4 4...e5: 5.Nb5 a6 6.N5c3, then Nf6/Be2/Be7/short castle, Be3/Qd2/Nd5/f4; keep the c4-bishop safe.
- Taimanov B: 8.e5 Nd5 9.Qg4 (1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7, 16 plies): with my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8) or kick ...h5 only if g7 is guarded; never ...f5 while exf6 e.p. opens lines to my king. T50R3: 9...Bf8 was right, but 11...g6?? opened a1-h8 - 15.Qf6! won h8, 16...Qb6?? 17.Bh6 Qb2 18.Qxf8#. After ...Bf8 the bishop STAYS (never back to e7 while his queen is near); no ...g6, no queen pawn-grabs; plan ...c5/...Be6/...Qb6 and trade his d3-bishop or queens. T51R1 vs SF: 9...Bf8 right, but 10...Qb6/11...Qb4 drifted and 14...Qe7?? after Bd2 BLOCKED Bf8's guard of d6 - 15.Nd6+! won c8/f7 and the game; the e5-pawn-backed d6 outpost is the whole attack, so keep d6 covered by a PIECE and remove Ne4/e5 (...Nxe4/...f6) before it lands. Never take Bg5 with the queen while Nf7+ forks her (19...Qxg5?? 20.Nxf7+). The 6.Nxc6 bxc6 7.Bd3 with ...d5 IQP (...Be7/...O-O/...Bd6 exchange) is sound: T49R3 level at 13.b4, T50R5 level to move 20. There 20...d4?! only made a target - his Nc4 and Re4 won the pawn and the game rolled on. In a blockade do NOT push the pawn into his blockaders; keep ...Bc6 and improve slowly. T49R4: play ...a6 BEFORE White's Nb5 (Nb5-c7 forks a8+e8; Bf4 guards c7, so ...Qxc7 loses the queen); 11...Re8? 12.Nb5 Bd7?? 13.Nc7! +2.7. T50R2 vs mirror: same Taimanov, my 9...d5 break and 12...Nxd4 were fine; his 16.Qh6?? gxh6 was the game.
- Caro B 4.Be2/4.Nf3: 3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 (12 plies). ...Nd7 then ...Ne7 (NEVER ...Ngf6 while e5 stands); recapture ...hxg6, never ...Nxg6?!. ...Be4 loses to Nxe4.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares, and a forked piece's retreat square. Give him NO loose unit; resolve central tension before castling. A piece down: aim for repetition. T45R6: took my hanging Re8 with check. T49R3: equal Taimanov IQP to 13.b4, lost only to empty replies. T50R3: g7 covered by ...Bf8, then 11...g6?? let 15.Qf6 win h8 and ...Qb6?? 17.Bh6 Qxf8#. T50R5: Taimanov IQP level to 20; 20...d4?! lost the pawn, then 50 passive moves lost the ending (0 illegal, 0 empty). T51R1: Taimanov 9...Bf8 fine, but 14...Qe7?? screened Bf8 from d6; 15.Nd6+ won, and 19...Qxg5?? 20.Nxf7+ won my queen. vs SF: no pawn push that becomes a target, no queen trade without counting, keep d6/g7 covered by PIECES, 10-15 s.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square.
- Sonnet 5.5 (never beaten): banks clock, quiet space moves, then takes every UNGUARDED unit. T46R1: punished 17.Ne4?? with ...Nf4xd3, then 23.Nh4?? with ...Rxd2. 10-15 s from move 1, assume 60+ moves, keep a rank-1 blocker.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn/bishop diagonal or knight square, and any loose recapture. ...a6/...Ba7/...h6/...Re8, ...d5/...Nxd5 hits c3; his Nf4 + queen on c6-g2 = Qxg2#. T44R2: +P in a rook ending, ...Rd1# when my c1-rook left d1. T45R2: punished my central knight jump and made two passers queen.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3, and the Chigorin; gives nothing loose.
- GLM 5.3 Flash: slow, illegal tries, miscounts material; hangs queens/rooks when worse, but punishes MY loose knight jumps. T45R4: 4 illegal tries, huge thinks, he FLAGGED while I kept ~22 min. T49R2: 5:03 on 11.d4, a pawn up after 13.Qxd5, and I forfeited on three empty replies. T49R5: I forfeited at m16 while up N for P after four invalid tries. T50R1: I won his queen with Rxg6+! then forfeited at m40 on five illegal tries plus an empty reply. T50R4 (I won by mate): his 22.Qd8+?? Rxd8 hung his queen; he had 3 invalid tries, I had 1 illegal on 15...Ne4. vs GLM: 10-15 s sound moves, guard every unit, take free captures, NEVER end in an empty or illegal reply.
- Haiku 5.5: fast, solid Italian Pianissimo, no free material. T44R3 I FORFEITED (3 illegal tries) in a dead-equal position; T45R3 he beat me on the clock. 10-15 s a move, bank time, check legality twice.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov as Black, keeps units guarded; T50R2 I BEAT HIM (his 16.Qh6?? gxh6, +Q for R converted with ...Qxd4, ...Bxf2+, ...Re1#). Treat mirror games as strong opposition: win on legality, guard counts and simple conversion; do not burn 40 min on routine moves.
