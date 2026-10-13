# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B (Qg4/g7 trick, f6-piece ban)
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov/Kalashnikov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban
- 3 rejected tries on ONE move = forfeit; each burns clock. O-O needs f1/g1 (d1/c1) AND f8/g8 empty, knight off home. T39R4 9 tried O-O with my f1-BISHOP home (2 tries); after O-O-O my king is on c8 so ...Rc8 is ILLEGAL. T39R7 33.Rb1 and T40R3 41.Rb7+/43.Rb8# were illegal - MY OWN b-pawns (b2/b3/b4) blocked the b-file. Walk every rook move's path for MY OWN pawns FIRST. ONE rejection: never resend - redraw, list legal squares, choose. T40R5 21...Bc6 illegal - my OWN c6-pawn sat on the d7-c6 path (played ...Be8).
- A SQUARE I WANT MAY BE MINE ALREADY: name the blocker before ...f6/...e5/...c5.
- SELF-BAN: a move my scan called bad is DEAD. T38R7 12.c4?/13.Bc2?? repeated T37R5's EXACT trap though my note listed both: a banned move is an ORDER - name the note, do not play the 'natural' version.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; hitting two units is no safety. QUIET DEVELOPMENTS GET THE SAME SWEEP: T39R2 26.Bf4?? had ZERO guards, 27...Nxf4.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7, h6<-g7 (so ...h6 ATTACKS g5), g6 hits f5/h5, d4<-c5/e5, f4<-e5/g5, f5<-g6/e6, f6<-e5. A PAWN THAT MOVED TO ATTACK STILL ATTACKS.
- KNIGHT JUMPS LAND ONLY OFF EVERY ENEMY LINE: a tempo or an escape does not make a square safe. T41R4 13...Nd3?? stepped off the b4-pawn's path and hit b4/f2, but sat on Qc2-d3's DIAGONAL -> 14.Qxd3 = N for nothing. Before ANY knight move walk his queen's AND both bishops' diagonals to the landing square.
- WHITE e5 PAWN OWNS d6 AND f6: while it stands d6/f6 are NO-GO (T39R1 6...Ngf6?? 7.exf6 = N for P). WITH MY KING CASTLED, Qg3 also PINS g7 (g4/g5/g6 empty), so a piece on f6 is even worse: T40R5 15...Bf6?? exf6 took the BISHOP and gxf6 was ILLEGAL (pinned g7 pawn). Never a piece on d6/f6 while e5 stands.
- A KNIGHT ON c6 IS HIT BY HIS d5-PAWN: when his d-pawn reaches d5 the c6-knight dies for a pawn (b7xc6 recaptures only the pawn). T40R6 14...Bxd5? 15.cxd5 16.dxc6 took my c6-KNIGHT. Move the c6-knight or hold d5 with a piece before his d-pawn lands.
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves his attack lands. HIS PAWN MOVE RE-WALKS LINES: 18...b5 opened Ra7-c7; 19.Rxc7?? Rxc7 lost a ROOK - re-walk on the CURRENT board before capturing.
- Knights and rooks only where GUARDED. A queen's guard along a rook's file is NO guard. Before a rook CAPTURE walk the pawn recaptures; before a ROOK CHECK ask 'can his king just take it?' (T38R2 43...Rf5+?? Kxf5). T39R4 31.b5?? left my rook on e6 a king-move from Kf5 -> ...Kxe6.
- NEVER PARK A ROOK ON A SQUARE HIS ROOK HITS DOWN AN OPEN FILE (T39R2 27.Re4?? Rxe4); a rook on a file/diagonal his BISHOP reaches is a TARGET (T40R1 Rac8 loose on f5-c8; T41R4 Re8 loose on the c6-bishop's diagonal -> Bxe8).
- THE MOVING UNIT ABANDONS ITS GUARD: name what it guarded. T38R4 16.d4? moved the d3-PAWN, Nc4's ONLY guard; T40R2 9.Bf4?? took Be3 off d4, my Nd4's only guard.
- AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY QUIET MOVE ELSEWHERE: T40R3 21...b5 attacked my c4-bishop; 22.Ne3?? left it to bxc4 = B for P though a safe retreat existed.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?'.
- BLOCKING A MATE STILL OBEYS THE SWEEP: T37R5 17.Qg4?? blocked ...Qxg2# but landed on Be6's diagonal; Bxg4 won my QUEEN.
- Sol's Qg5+Nf4 = ...Qxg2#: defend g2, remove Nf4, or trade queens.
- Qg4+Bh6 vs short-castled king (g7 guarded only by Kg8): answer ...f5/...f6, ...Qf6, or trade queens. Qg4! vs MY UNCASTLED e8-king: g7's only guard is the king; ...h5?? FAILS (9.Qxg7! Bf8 10.Qxh8 = a rook) - COVER g7 with a piece or trade queens. Qh5+Bd3: kick (...g6/...h6). Qg3+dark bishop: block ...f6, luft, trade the bishop.
- Back rank: keep a rank-1 blocker or luft. T37R6 28...Rd1# - king boxed by its own pawns.
- KING-TAKES - ANY PIECE NEXT TO HIS KING, UNGUARDED, IS A KING CAPTURE: never land a queen/rook/bishop/KNIGHT beside his king without a guard. T39R4 48.Qc6+?? Kxc6; T40R1 25...Qe1+?? Rxe1; T40R6 25...Qxf2+?? Kxf2; T41R2 45.Nf5?? Kxf5 - an unguarded KNIGHT dies the same way. Before ANY check write 'what captures the checker?', the KING included.
- QUEEN TRADE WITH MY KING AS RECAPTURER: list his knight jumps first.
- B+N vs K: drive the king to the bishop's-colour corner; NEVER shuffle in a won position.
- Q vs lone K (T41R4 done CLEANLY): box with the queen a KNIGHT'S move from his king, bring my king up, drive him to the edge, mate on the edge with my king covering the queen. Leave him a legal square every move until mate - no stalemate.

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
- MATERIAL FROM THE BOARD, EVERY MOVE. Count pieces, never prose - T40R7 I wrote '+N' but it was LEVEL; T41R2 my notes flip-flopped ('up a rook' -> 'level') through a dead-level knight endgame; T41R4 swung N-for-nothing -> queen -> level -> rook several times - recount after every trade.
- CONVERTING: T40R1 won Q for R then threw it away. T40R3 is the model: +Q for B+P -> guarded every unit, traded rooks evenly, two-rook ladder (Rd7+/Rd8+), Ra8# - no repetition, every move progress.
- Down: keep queens only while SAFE; NO grabs; loose pieces first. Up: trade pieces not pawns; escort passers; promote; stalemate-check. NEVER TRADE R FOR B (or R for P) WHEN DOWN OR EVEN.
- AFTER A ROOK TRADE RE-GUARD THE OTHER ROOK: T38R4 22...Rxe1+ 23.Kh2 23...Rxa1 took my loose rook.
- LEVEL MINOR-PIECE ENDGAME (T41R2, K+N each, level pawns): a pawn pushed with only my KING as guard dies when his king also covers the square - 37.b5? Nd6 38.Ka6 Nxb5 (his Kc4 covered b5, no recapture); 34.Kb5?! wandering king then lost more pawns. Guard pawns with PIECES, trade pawns evenly, hold the draw; no pushes into his king+knight reach.
- K+Q vs K = MATE, NOT STALEMATE (T39R4 stalemated from a whole queen up; T41R4 did it right). Keep the queen a KNIGHT'S MOVE from his king until he is on the edge; bring my king up; when his king is on the edge put my king directly opposite, then check on the edge (queen covered by my king) = mate.
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. The written scan, not the clock, is the check. T40R5/R6 had long thinks, all scan misses. T41R2 ended with 20 min left, 0 illegal - the endgame pawn pushes were evaluation misses, not clock. T41R4 long thinks (24-52 s) still produced the Nd3??/Qe5?? blunders - the scan is the check.

## Openings (only the lines I actually play)
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 Bb6 (16 plies); Re1/Bc2/Nf1-g3. BANS: 10.d4?!, 12.c4?, 13.Bc2??, 14.Bg5?? (h6 hits g5), 15.Nxe5?? (d6 guards e5), 24.Qh5?? (Bf7-g6-h5). No queen on d5 while his f6-knight lives. T41R2 vs Sonnet: level through the middlegame (...Bxb3/...Bxe3, queens+rooks off by m22); the ...d5 break plus one over-valued capture decides these games. Then HOLD the resulting level knight endgame.
- Open Sicilian W vs 3...Nxd4 4...e5 (Kalashnikov/Sveshnikov-ish): 1.e4 c5 2.Nf3 Nc6 3.d4 Nxd4 4.Nxd4 e5 5.Nb5 a6 6.N5c3 Nf6 7.Be2 Be7 8.O-O O-O (15 plies); Be3/Qd2/Nd5/f4 vs ...Qc7/...b6/...Bb7/...f5/...e4. T40R3 vs GLM (1-0): Nd5/...Nxd5/exd5 space edge; ...b5 met 21.axb5 axb5, a passed pawn fell; then Ne3?? hung my c4-bishop to bxc4 - save an attacked piece first. +Q for B+P converted cleanly. Keep d5 guarded by Nc3.
- Open Sicilian W (Taimanov quiet 6.Be2): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1. vs Dragon block ...Qa5+ with Bd2/Bd1, never Qd2??. Accelerated Dragon (4...g6): keep Be3 - it is the d4-knight's guard; 9.Bf4?? Bxd4 won a knight; answer ...Ng4 with Qd2/Rad1; never Nf6+ while his e7-pawn stands.
- Taimanov B vs 8.e5 Nd5 9.Qg4: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (15 plies). With my king on e8 g7 has NO guard: never ...d6, never castle; COVER g7 or kick ...h5 ONLY if g7 is also guarded. NEVER ...Nf6 (T38R6 9...Nf6?? 10.exf6).
- Caro B 4.Be2 / 4.Nf3: knight plan ...Nd7 then ...Ne7 (NEVER ...Ngf6 while e5 stands: T39R1 6...Ngf6?? 7.exf6); recapture ...hxg6, never ...Nxg6?!. ...f6 removes f7's guard of g6; ...Be4 loses to Nxe4; safe plans ...Bxd3/...cxd4. EARLY ...c5 at move 6 held (T39R1). Down N for P guard every unit to force the Kd8/Ke8 repetition SF accepted.
- Caro Advance B (T39R6, T40R5, T40R6: 0-1; T41R1 draw): 3.e5 c5 4.Nf3 cxd4 5.Bb5+ Nc6 6.Qxd4 e6 7.O-O Be7?! 8.Qg4! (11 plies) - g7 is king-guarded only, so 8...h5?? 9.Qxg7! Bf8 10.Qxh8 loses a ROOK; cover g7 with a piece or trade queens; never ...Nf6/...Ngf6 while e5 stands. vs 5.Nxd4/6.Nxc6 the ...bxc6/...e6/...Ne7-g6/...O-O/...f6 plan is fine; after 12...f6 13.Bxg6 hxg6 14.Qxg6 f5 15.Qg3, 15...Bf6?? LOSES THE BISHOP to exf6 (g7 pinned). vs 5.Bb5+ 8.Re1: ...Ne7-f5 covers g7 BEFORE ...Be7; but 14...Bxd5? 15.cxd5 16.dxc6 won my c6-KNIGHT - hold d5 or move that knight. NEVER a queen on a pawn's capture square (25...Qd3?? cxd3; 9...Qd6?? exd6); NEVER a check his king takes (25...Qxf2+?? Kxf2). Down a queen, guard every unit; the shuffle vs SF's checks drew (T41R1).
- QGD Bb4/5.Bg5 IQP B: BANS 12.Qd3?!, 14.Qg3??, 28.Qg2??, 31.f3?? (every loss was a scan miss, not the opening).
- English as Black (WINS T38R2, T41R4; DRAW g168): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d4 (15 plies); solid QGD-reversed, ...Nbd7 ...Re8 ...Bf8 ...Qc7, ...c5 break, ...Qb6 pressure. T41R4 vs GLM (0-1): the ...c5 break forced ...Nxc5, but 13...Nd3?? landed my knight on Qc2-d3's diagonal = N for nothing; my Re8 later hung to Bc6xe8. His Qa6?? (bxa6) and Rxe5?? (fxe5) gave the material back, and the up-queen mate ran clean. His Qd3 hung to ...Qxd3 after ...Qa6 in g168.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his ranks/rays/pawn diagonals/KNIGHT squares. Give him NO loose unit; resolve central tension BEFORE castling. When a piece down vs him, aim for a repetition (T39R1, T41R1 accepted). T40R2 takes any piece on a pawn's square (Bxd4, exf6, gxf4). T40R6: his d5-outpost knight won my c6-knight (16.dxc6).
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square. Answer the battery FIRST.
- Sonnet 5.5 (never beaten): banks clock; takes every free unit, every piece on a pawn's capture square, every UNGUARDED piece - even a KNIGHT beside his king (T41R2 45.Nf5?? Kxf5). No free unit, no pawn-hit square, no lone-guarded queen; keep a rank-1 blocker. T41R2 as Black he mirrored my Giuoco Pianissimo, traded both bishops (8...Bxb3, 13...Bxe3), met queens+rooks off by m22, then ground a DEAD-LEVEL knight endgame to a win by taking every loose pawn and my knight - hold such endings, do not push into his king.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn OR bishop diagonal OR knight square. Italian: ...d5/...Nxd5, ...Nf4 hits d3; ...Bxc4 wins a loose Nc4; ...Rxe1+/...Rxa1 and ...Rg1+/...Rh1#. T40R1 his Bf5-c8 diagonal won my loose Rac8. T40R7 Italian: 16...Bxb3 (tempo) 17...Rxe4 cleared the e-file and won my rook.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3 and the Chigorin; takes every loose piece at once. Give him no loose unit.
- GLM 5.3 Flash (2 wins, 1 draw; T39R4 I drew a WINNING game; T41R4 0-1 I won): slow, sloppy, illegal tries, misstates material; hangs loose pawns, rooks, queens, undefended pieces (T41R4 25.Qa6?? bxa6 won his QUEEN; 40.Rxe5?? fxe5 won his rook). Defends a lost position ACTIVELY but hangs pieces when worse - convert cleanly: no repetition, guard every unit, MATE a lone king instead of stalemating it. But he also punishes MY loose knight jumps (T41R4 13...Nd3?? Qxd3) - keep every unit off his queen's diagonals.
