# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B (Qg4/g7 trick, f6-piece ban, h7/Bd3 net)
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov/Kalashnikov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban
- 3 rejected tries on ONE move = forfeit; each burns clock. Walk every rook move's path for MY OWN pawns FIRST: T39R7 33.Rb1 and T40R3 41.Rb7+/43.Rb8# illegal - MY b-pawns (b2/b3/b4) blocked the b-file. O-O needs f1/g1 (d1/c1) AND f8/g8 empty; after O-O-O my king is on c8 so ...Rc8 is ILLEGAL. T39R4 9 tried O-O with my f1-BISHOP home (2 tries). ONE rejection: never resend - redraw, list legal squares, choose. T40R5 21...Bc6 illegal - my OWN c6-pawn on the d7-c6 path (played ...Be8). T41R6 11...Ne7 illegal - MY OWN Be7 sits on e7.
- A SQUARE I WANT MAY BE MINE ALREADY: name the blocker before ...f6/...e5/...c5/...Ne7.
- SELF-BAN: a move my scan called bad is DEAD. T38R7 12.c4?/13.Bc2?? repeated T37R5's EXACT trap though my note listed both: a banned move is an ORDER - name the note, do not play the 'natural' version.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; hitting two units is no safety. QUIET DEVELOPMENTS GET THE SAME SWEEP: T39R2 26.Bf4?? had ZERO guards, 27...Nxf4.
- AN 'ATTACKING'/'WITH TEMPO' MOVE GETS THE SAME SWEEP: T41R5 20.Ba4?? chased the d7-queen with ZERO guards -> 20...Qxa4 won a whole BISHOP. 0 guards + his capture = gift, however loud the tempo.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7, h6<-g7 (so ...h6 ATTACKS g5), g6 hits f5/h5, d4<-c5/e5, f4<-e5/g5, f5<-g6/e6, f6<-e5. A PAWN THAT MOVED TO ATTACK STILL ATTACKS.
- KNIGHT JUMPS LAND ONLY OFF EVERY ENEMY LINE: a tempo or an escape does not make a square safe. T41R4 13...Nd3?? stepped off the b4-pawn's path and hit b4/f2, but sat on Qc2-d3's DIAGONAL -> 14.Qxd3. Before ANY knight move walk his queen's AND both bishops' diagonals to the landing square.
- WHITE e5 PAWN OWNS d6 AND f6: while it stands d6/f6 are NO-GO. WITH MY KING CASTLED, Qg3 also PINS g7, so a piece on f6 is worse: T40R5 15...Bf6?? exf6 took the BISHOP, gxf6 was ILLEGAL (pinned g7). Never a piece on d6/f6 while e5 stands.
- A KNIGHT ON c6 IS HIT BY HIS d5-PAWN: when his d-pawn reaches d5 the c6-knight dies for a pawn. T40R6 14...Bxd5? 15.cxd5 16.dxc6 took my c6-KNIGHT. Move the c6-knight or hold d5 with a piece before his d-pawn lands.
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves his attack lands. HIS PAWN MOVE RE-WALKS LINES: 18...b5 opened Ra7-c7; 19.Rxc7?? Rxc7 lost a ROOK - re-walk on the CURRENT board before capturing.
- Knights and rooks only where GUARDED. A queen's guard along a rook's file is NO guard. Before a rook CAPTURE walk the pawn recaptures; before a ROOK CHECK ask 'can his king just take it?' (T38R2 43...Rf5+?? Kxf5). T39R4 31.b5?? left my rook on e6 a king-move from Kf5 -> ...Kxe6.
- NEVER PARK A ROOK ON A SQUARE HIS ROOK HITS DOWN AN OPEN FILE (T39R2 27.Re4?? Rxe4); a rook on a file/diagonal his BISHOP reaches is a TARGET (T40R1 Rac8 loose on f5-c8; T41R4 Re8 loose on the c6-bishop's diagonal -> Bxe8).
- THE MOVING UNIT ABANDONS ITS GUARD: name what it guarded. T38R4 16.d4? moved the d3-PAWN, Nc4's ONLY guard; T40R2 9.Bf4?? took Be3 off d4, my Nd4's only guard.
- AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY QUIET MOVE ELSEWHERE: T40R3 21...b5 attacked my c4-bishop; 22.Ne3?? left it to bxc4 though a safe retreat existed.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?'.
- BLOCKING A MATE STILL OBEYS THE SWEEP: T37R5 17.Qg4?? blocked ...Qxg2# but landed on Be6's diagonal; Bxg4 won my QUEEN.
- Sol's Qg5+Nf4 = ...Qxg2#: defend g2, remove Nf4, or trade queens. CONFIRMED T41R5: 23...Nf4 both uncovered c6-g2 (the d5-knight left) AND guarded g2; 24.Qf5 ignored it, 24...Qxg2#. When his knight lands on f4 and his queen can reach g2, answer THAT move.
- Qg4+Bh6 vs short-castled king (g7 guarded only by Kg8): answer ...f5/...f6, ...Qf6, or trade queens. Qg4! vs MY UNCASTLED e8-king: g7's only guard is the king; ...h5?? FAILS (9.Qxg7! Bf8 10.Qxh8). Qh5+Bd3: kick (...g6/...h6). Qg3+dark bishop: block ...f6, luft, trade the bishop.
- Bd3+Qh6 vs MY SHORT-CASTLED king: Bd3 covers h7, so once his queen reaches h6, Qxh7# is a net (T41R6 14.Qxh6 Qxh7#). Never let her reach h6: block the d3-e4-f5-g6-h7 diagonal (...f5/...Nf5), cover h7, or trade queens. An 'offer' (14...Bg5??) NEVER answers a mate threat on the board.
- Back rank: keep a rank-1 blocker or luft. T37R6 28...Rd1# - king boxed by its own pawns.
- KING-TAKES - an unguarded piece beside his king (KNIGHT included) is a king capture: T39R4 48.Qc6+?? Kxc6; T40R1 25...Qe1+?? Rxe1; T40R6 25...Qxf2+?? Kxf2; T41R2 45.Nf5?? Kxf5. Before ANY check write 'what captures the checker?', the KING included.
- QUEEN TRADE WITH MY KING AS RECAPTURER: list his knight jumps first.
- Q vs lone K (T41R4 done CLEANLY): box with the queen a KNIGHT'S move from his king, bring my king up, drive him to the edge, mate on the edge with my king covering the queen; leave him a legal square every move until mate - no stalemate. Same rule for B+N vs K (drive to the bishop's-colour corner).

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. HIS BISHOP LANDS WITH TEMPO ON HER = she moves.
- QUEEN NEVER LANDS ON AN ENEMY BISHOP'S DIAGONAL or a KNIGHT's jump square, 'with tempo'/'blocking a mate' included (T37R5 17.Qg4?? Bxg4; T38R6 19...Qc5?? Nxc5; T39R7 21.Qd5?? Nxd5; T41R4 28...Qe5?? landed on Bc3-d4-e5 -> 29.Bxe5 gave the whole queen back).
- BEFORE every queen/rook move list what it defended where it stood, AND every enemy knight and pawn that hits the destination. A SOLITARY/BLOCKED GUARD IS NOT A GUARD: T39R2 28...Qxd1+ 29.Rxd1 Rxd1+ fell; T40R3 32.Qxc4?? walked onto c4 with NO guard (Rc1 blocked by my own c2-pawn) -> ...Rxc4 = Q for R.
- NEVER a queen on a PAWN's capture square: T40R2 14.Qf4?? gxf4; T40R5 25...Qd3?? cxd3 while already DOWN a piece - DOWN = NO grabs; T41R1 9...Qd6?? exd6 'defending' - defend squares WITHOUT her.
- NEVER OFFER A 'TRADE' WHOSE RECAPTURE IS ILLEGAL OR LOSING.

## Rule 3 - captures & 'trade offers'
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move. T38R6 12...Rg8?? my KING on e8 was TWO squares away - 13.Qxg8+ = R for nothing.
- THE RECAPTURER NEEDS ITS OWN GUARD AFTER IT LANDS: T39R2 29.Rxd1 Rxd1+ - my last rook stood unguarded.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN. Count EVERY recapturer, PAWNS FIRST. TRACE THE CHAIN TO THE END (T38R1 15.Nxe5?? looked defended but had NO fourth recapturer = N for P).
- AN 'UNDEFENDED PIECE' IS NOT FREE IF HIS ANSWER COMES WITH TEMPO: T40R7 16.Rxe4?? 'wins a knight' - 16...Bxb3 hit my QUEEN, 17.axb3 Rxe4 took my rook. Walk every enemy tempo move / guard-clearing exchange first; 18.Rxa6?? = R for P (NEVER trade a ROOK for a PAWN).
- PAWN PUSH ABANDONS GUARD DUTY. His piece lands where two of mine hit it with no guard -> take it (T39R4 24.Rxd4 won a rook).
- After ANY trade re-count the guards of ALL my units and his.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE; count pieces, never prose (T40R7 wrote '+N' while LEVEL; T41R2/R4 my notes flipped through a dead-level knight endgame) - recount after every trade.
- CONVERTING: T40R1 won Q for R then threw it away. T40R3 is the model: +Q for B+P -> guarded every unit, traded rooks evenly, two-rook ladder (Rd7+/Rd8+), Ra8# - no repetition, every move progress.
- Down: keep queens only while SAFE; NO grabs; loose pieces first. Up: trade pieces not pawns; escort passers; promote; stalemate-check. NEVER TRADE R FOR B (or R for P) WHEN DOWN OR EVEN.
- AFTER A ROOK TRADE RE-GUARD THE OTHER ROOK: T38R4 22...Rxe1+ 23.Kh2 23...Rxa1 took my loose rook.
- LEVEL MINOR-PIECE ENDGAME (T41R2): a pawn pushed with only my KING as guard dies when his king also covers the square (37.b5? Nd6 38.Ka6 Nxb5); guard pawns with PIECES, trade pawns evenly, hold the draw.
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. The written scan, not the clock, is the check (T40R5/R6, T41R4 24-52 s and T41R5 38 s on 18.Bb3?! then 20.Ba4?? - all scan misses).

## Openings (only the lines I actually play)
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 Bb6 (16 plies); Re1/Bc2/Nf1-g3. BANS: 10.d4?!, 12.c4?, 13.Bc2??, 14.Bg5?? (h6 hits g5), 15.Nxe5?? (d6 guards e5), 24.Qh5?? (Bf7-g6-h5). No queen on d5 while his f6-knight lives. T41R2 vs Sonnet: level to m22 (...Bxb3/...Bxe3); the ...d5 break decides; HOLD the level knight endgame. T41R5 vs Sol (0-1): ...a6/Ba7/h6/Re8, ...d5/Nxd5 equalized; 20.Ba4?? (undefended, chasing Qd7) Qxa4, then Nf4/Qxg2#.
- Open Sicilian W vs 3...Nxd4 4...e5 (Kalashnikov/Sveshnikov-ish): 1.e4 c5 2.Nf3 Nc6 3.d4 Nxd4 4.Nxd4 e5 5.Nb5 a6 6.N5c3 Nf6 7.Be2 Be7 8.O-O O-O (15 plies); Be3/Qd2/Nd5/f4 vs ...Qc7/...b6/...Bb7/...f5/...e4. T40R3 vs GLM (1-0): Nd5/...Nxd5/exd5 space edge; ...b5 met 21.axb5 axb5, a passed pawn fell; then Ne3?? hung my c4-bishop to bxc4 - save an attacked piece first. +Q for B+P converted cleanly. Keep d5 guarded by Nc3.
- Open Sicilian W (Taimanov quiet 6.Be2): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1. vs Dragon block ...Qa5+ with Bd2/Bd1, never Qd2??. Accelerated Dragon (4...g6): keep Be3 - it is the d4-knight's guard; 9.Bf4?? Bxd4 won a knight; answer ...Ng4 with Qd2/Rad1; never Nf6+ while his e7-pawn stands.
- Taimanov B vs 8.e5 Nd5 9.Qg4: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (15 plies). With my king on e8 g7 has NO guard: never ...d6, never castle; COVER g7 or kick ...h5 ONLY if g7 is also guarded. NEVER ...Nf6 (T38R6 9...Nf6?? 10.exf6).
- Caro B 4.Be2 / 4.Nf3: knight plan ...Nd7 then ...Ne7 (NEVER ...Ngf6 while e5 stands: T39R1 6...Ngf6?? 7.exf6); recapture ...hxg6, never ...Nxg6?!. ...f6 removes f7's guard of g6; ...Be4 loses to Nxe4; safe plans ...Bxd3/...cxd4. EARLY ...c5 at move 6 held (T39R1).
- Caro Advance B (T39R6, T40R5, T40R6: 0-1; T41R1 draw): 3.e5 c5 4.Nf3 cxd4 5.Bb5+ Nc6 6.Qxd4 e6 7.O-O Be7?! 8.Qg4! (11 plies) - g7 is king-guarded only, so 8...h5?? 9.Qxg7! Bf8 10.Qxh8 loses a ROOK; cover g7 with a piece or trade queens; never ...Nf6/...Ngf6 while e5 stands. vs 5.Nxd4/6.Nxc6 the ...bxc6/...e6/...Ne7-g6/...O-O/...f6 plan is fine; after 12...f6 13.Bxg6 hxg6 14.Qxg6 f5 15.Qg3, 15...Bf6?? LOSES THE BISHOP to exf6 (g7 pinned). vs 5.Bb5+ 8.Re1: ...Ne7-f5 covers g7 BEFORE ...Be7; but 14...Bxd5? 15.cxd5 16.dxc6 won my c6-KNIGHT - hold d5 or move that knight. NEVER a queen on a pawn's capture square (25...Qd3?? cxd3; 9...Qd6?? exd6); NEVER a check his king takes (25...Qxf2+?? Kxf2). Down a queen, guard every unit; the shuffle vs SF's checks drew (T41R1). T41R6 vs SF: 7...Ne7 8...Nf5 9.Qd1 Be7 O-O 11...Nh6?! (12.Bxh6 gxh6) left h7 weak - 13.Qd2 Bd7? 14.Qxh6 and Qxh7# via Bd3. Save the f5-knight WITHOUT h6 (11...Ne7 was ILLEGAL - my own Be7 there); if Be7 is on e7 the f5-knight must accept Bxf5/exf5 or retreat ...Ng7/...Nd6-style, not ...Nh6.
- QGD Bb4/5.Bg5 IQP B: BANS 12.Qd3?!, 14.Qg3??, 28.Qg2??, 31.f3?? (every loss was a scan miss, not the opening).
- English as Black (WINS T38R2, T41R4; DRAW g168; T42R1 0-1 by GLM forfeit at m10): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d4 (15 plies); solid QGD-reversed, ...Nbd7/...Re8/...Bf8/...Qc7, ...c5 break, ...Qb6. T41R4 vs GLM (0-1): ...c5 forced ...Nxc5, but 13...Nd3?? landed on Qc2-d3's diagonal = N for nothing; Re8 hung to Bc6xe8. He gave it back (Qa6?? bxa6; Rxe5?? fxe5) and the up-queen mate ran clean.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his ranks/rays/pawn diagonals/KNIGHT squares. Give him NO loose unit; resolve central tension BEFORE castling. When a piece down vs him, aim for a repetition (T39R1, T41R1 accepted). T40R2 takes any piece on a pawn's square (Bxd4, exf6, gxf4). T40R6: his d5-outpost knight won my c6-knight (16.dxc6). T41R6: 11...Nh6?! + 13...Bd7? + 14...Bg5?? = mate - see Rule 1b.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square. Answer the battery FIRST.
- Sonnet 5.5 (never beaten): banks clock; takes every free unit, every piece on a pawn's capture square, every UNGUARDED piece - even a KNIGHT beside his king (T41R2 45.Nf5?? Kxf5). No free unit, no pawn-hit square, no lone-guarded queen; keep a rank-1 blocker. T41R2 as Black he mirrored my Giuoco Pianissimo, traded both bishops (8...Bxb3, 13...Bxe3), met queens+rooks off by m22, then ground a DEAD-LEVEL knight endgame to a win by taking every loose pawn and my knight - hold such endings, do not push into his king.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn OR bishop diagonal OR knight square. Italian: ...a6/...Ba7/...h6/...Re8, ...d5/...Nxd5 hits c3; his Nf4 + queen on the c6-g2 diagonal = Qxg2#; take any undefended piece chasing his queen (T41R5 20.Ba4?? Qxa4). T40R1 his Bf5-c8 diagonal won my loose Rac8. T40R7 Italian: 16...Bxb3 (tempo) 17...Rxe4 cleared the e-file and won my rook.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3 and the Chigorin; takes every loose piece at once. Give him no loose unit.
- GLM 5.3 Flash (T41R4 he won 1-0; T42R1 I won 0-1): slow, illegal tries, miscounts material; hangs queens/rooks/undefended pieces when worse. Convert cleanly (no repetition, guard every unit, mate a lone king - don't stalemate). But he punishes MY loose knight jumps (13...Nd3?? Qxd3): keep units off his queen's diagonals. T42R1: he FORFEITED at m10 (provider crash, 0 invalid moves) after 29 s on the passive 10...Qb6 - his floor is a crash, so just keep playing solid, guarded moves; no need to force anything.
