# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B (incl. Qg4/g7 kick lesson)
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban
- 3 rejected tries on ONE move = forfeit; each try burns clock. O-O needs knight off home + f8/g8 empty AND f1/g1 (or d1/c1) empty. T39R4 9 I tried O-O with my f1-BISHOP still home (2 illegal tries) before finding Be2 - the bishop must LEAVE first, then castle. After O-O-O my king is on c8, so ...Rc8 is ILLEGAL. Before any bishop move path AND destination must be empty. T39R7 33.Rb1 was illegal because my own b2-pawn blocked the b-file; after ONE rejection NEVER resend: redraw, list every legal square, choose.
- g168 five rejected tries - all geometry: ...Rac8 with my Bc8 home; ...Ke7 where his Kf8 guarded e7. Before a ROOK move walk its path for my own pieces; before a KING move list every enemy guard of the destination.
- A SQUARE I WANT MAY BE MINE ALREADY: name the blocker before ...f6/...e5/...c5.
- SELF-BAN: a move my scan called bad is DEAD. T37R5 17.Qg4?? broke 'no queen on a bishop's diagonal'; T37R6 14.Bg5?? broke 'never develop onto a pawn's capture square'. T38R7 12.c4? and 13.Bc2?? repeated T37R5's EXACT trap even though my note listed both as bans: a banned move is an ORDER - name the note, then do NOT play the 'natural' version.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; hitting two units is no safety. A QUIET DEVELOPING MOVE GETS THE SAME SWEEP: T39R2 26.Bf4?? said 'every unit guarded' - f4 had ZERO guards and his d5-knight took it.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7, h6<-g7 (so ...h6 ATTACKS g5 and g7), g6 hits f5/h5, d4<-c5/e5, f4<-e5/g5. A PAWN THAT MOVED TO ATTACK STILL ATTACKS. MY piece lands where a pawn takes: f5<-g6/e6, f4<-e5/g5, e4<-d5/f5, g5<-h6, f6<-e5. T39R4 22...dxe4 won my Ne4: Bf4's diagonal MISSES e4, Re1 was blocked by Be2, no pawn covered it - a developed piece with NO guard is a gift, name what recaptures it.
- WHITE e5 PAWN OWNS d6 AND f6: while it stands, d6/f6 are NO-GO for my pieces (T39R1 6...Ngf6?? 7.exf6 = N for P). OPENING-INDEPENDENT: name it before ANY knight/bishop to d6/f6.
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves his attack lands.
- HIS PAWN MOVE RE-WALKS LINES: 18...b5 moved b7, opening Ra7-c7; 19.Rxc7?? Rxc7 lost a ROOK. Before capturing a pawn/piece a rook/queen behind might recapture, re-walk the line on the CURRENT board. AN UNGUARDED ATTACKER IS THE TARGET: 36.Be6?? hit Rf5 but had no guard; Kd6 later took it (...Kxe6). If my piece attacks and cannot be guarded or retreat, it is a gift.
- Knights and rooks only where GUARDED. A queen's guard along a rook's file is NO guard. Rook onto a pawn-guarded square = R for P. Before any rook CAPTURE walk the pawn recaptures; before any ROOK CHECK ask 'can his king just take it?' (T38R2 43...Rf5+?? Kxf5). T39R4 31.b5?? left my rook on e6 a king-move from his Kf5, no guard -> ...Kxe6: after ANY rook check that leaves the rook a king-move from his king it must MOVE or be DEFENDED that same move - never a quiet pawn push.
- NEVER PARK A ROOK ON A SQUARE HIS ROOK HITS DOWN AN OPEN FILE: T39R2 27.Re4?? - Re8 owns the e-file, Rxe4 = R for B.
- Rook files/bishop rays own whole lines; attacked+undefended -> save NOW. Mate net before any grab. Long castled: cover c7.
- A ROOK ON A FILE/DIAGONAL HIS BISHOP CAN REACH IS A TARGET, NOT AN ASSET (T40R1: my Rac8 was loose on the f5-c8 line).
- THE MOVING UNIT ABANDONS ITS GUARD: name what it guarded where it stood. T37R7 13...Bxf6?? was c5's only guard; 14.Nxc6 bxc6 15.Bxc5. T38R4 16.d4? moved the d3-PAWN that was Nc4's ONLY guard -> ...Nxe3/...Bxc4. T40R2 9.Bf4?? took Be3 off d4, my Nd4's only guard -> ...Bxd4 = N for nothing.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?'.
- BLOCKING A MATE STILL OBEYS THE SWEEP: T37R5 17.Qg4?? blocked ...Qxg2# but landed on Be6's diagonal; Bxg4 won my QUEEN. Defend the square or trade queens; NEVER block with a queen on a bishop/rook line.
- Sol's Qg5+Nf4 (knight guards g2) = ...Qxg2#: g2 hit twice, Kg1 no flight. Answer: defend g2, remove Nf4, or trade queens.
- Qg4+Bh6 battery vs short-castled king: g7 guarded only by Kg8; answer ...f5/...f6, ...Qf6, or trade queens. QUEEN vs MY UNCASTLED e8-KING: g7's only guard is the king, so 8.Qg4! - kicking with ...h5?? FAILS (9.Qxg7! Bf8 10.Qxh8 = a rook): she takes the pawn BEFORE the kick. COVER g7 with a piece (...Bf8/...Kf8) or trade queens. Qh5+Bd3: kick her (...g6/...h6) or free h8. Qg3+dark bishop: block with ...f6, make luft, trade the bishop.
- Back rank: keep a rank-1 blocker or make luft. T37R6 28...Rd1# - my king boxed by its own pawns. With his R+B on rank 1/2: ...Rxe1+/...Rxa1 then ...Rg1+/...Rh1# (Bf3 covered g2).
- KING-TAKES CHECK: never land a queen/bishop/rook next to his king unguarded; count defenders first. T39R4 48.Qc6+?? Kxc6 (his Kb7 adjacent to c6, no guard) threw away a whole QUEEN from a +Q game - the checker was on the square his king legally takes. Before ANY check name the guard of the checking square or do not check. T40R1 25...Qe1+?? let 26.Rxe1 take my QUEEN for a rook in a near-equal position - an unforced check that OFFERS my queen for a rook is a blunder; ask 'what captures the checker?' first.
- QUEEN TRADE WITH MY KING AS RECAPTURER: list his knight jumps before trading.
- B+N vs K: drive the lone king to the corner MATCHING the bishop's colour; NEVER shuffle in a won position.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. HIS BISHOP LANDS WITH TEMPO ON HER = she moves that move.
- QUEEN NEVER LANDS ON AN ENEMY BISHOP'S DIAGONAL, 'with tempo' or 'blocking a mate' included (T37R5 17.Qg4?? Bxg4; T38R4 24.Qh5?? Bxh5).
- BEFORE every queen/rook move list what it defended where it stood, AND every enemy KNIGHT and pawn that hits the destination: T38R6 19...Qc5?? 20.Nxc5. T39R7 21.Qd5?? lost my QUEEN to Nxd5: his Nf6 owns d5; offering a trade on a knight's square is a gift. A SOLITARY GUARD IS NOT A GUARD: T39R2 my Qd1 was covered only by Ra1; after 28...Qxd1+ 29.Rxd1 Rxd1+ the recapturing rook fell.
- NEVER a queen on a PAWN's capture square: T40R2 14.Qf4?? met 14...gxf4 = QUEEN for a pawn (g5 hits f4).
- When MY queen lands, also list HER guards and HIS queen's guards: T38R2 24...Qa6 hit Qd3 and 25.dxc6?? Qxd3 won her. A queen of his with no guard is worth a tempo to attack.
- NEVER OFFER A 'TRADE' WHOSE RECAPTURE IS ILLEGAL OR LOSING. PAWN DIAGONALS before every queen destination. Never park a rook where his pawn, bishop or open-file rook hits it.

## Rule 3 - captures & 'trade offers'
- RECAPTURE != TRADE. A 'trade' needs MY recapturer on the destination, ONE MOVE AWAY. T38R6 12...Rg8?? 'kicked' the queen but my KING on e8 was TWO squares from g8 - 13.Qxg8+ = R for nothing.
- THE RECAPTURER NEEDS ITS OWN GUARD AFTER IT LANDS: T39R2 29.Rxd1 Rxd1+ - my last rook stood unguarded on d1. Same class as T38R4 23...Rxa1.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN. RECAPTURE CHOICE - keep the recapturer's OTHER guards. Count EVERY recapturer - PAWNS FIRST.
- PAWN PUSH ABANDONS GUARD DUTY. WINNING CAPTURE PATTERN: his piece lands where two of mine hit it with no guard -> take it (T39R4 24.Rxd4 won a rook: Rd4 had NO guard).
- TRACE THE CAPTURE CHAIN TO THE END BEFORE ACCEPTING: T38R1 15.Nxe5?? looked defended but had NO fourth recapturer = N for P.
- After ANY trade re-count the guards of ALL my units and his.

## Rule 4 - material & clock
- MATERIAL FROM THE BOARD, EVERY MOVE. T39R2 I wrote 'slightly up' in a dead-level position and that false count justified 26.Bf4??. Count pieces, never plans. T40R1 I wrote 'up 3' at ply 44 then 'down 4' at ply 50 - never trust prose, count.
- CONVERTING Q-FOR-R (T40R1, Taimanov vs Sol): I won Q for R (21...Rxf3) and threw it away. 24...Qe7 vacated my d7-BLOCKER on his Bf5-c8 line -> 25.Bxc8 won my loose c8-rook; then 25...Qe1+?? 26.Rxe1 gave my QUEEN for a rook. After winning material, keep the QUEEN safe AND every rook defended; a blocker on his bishop's diagonal is a guard - do not move it without need; never give Q for R with an unforced check.
- Down: keep queens only while SAFE; NO grabs; loose pieces first. Up: trade pieces not pawns; escort passers; promote; stalemate-check.
- NEVER TRADE R FOR B (or R for P) WHEN DOWN (T37R6 25.Rxc6??).
- Before ANY rook check/capture ask 'can his king take my piece?'. Safe checks only. Do NOT castle while a central piece is lashed by two attackers.
- AFTER A ROOK TRADE RE-GUARD THE OTHER ROOK: T38R4 22...Rxe1+ 23.Kh2 23...Rxa1 took my loose rook.
- WINNING ENDGAME = NO REPETITION and NO STALEMATE. In a won position EVERY move makes progress. WHEN HUGELY AHEAD SLOW DOWN: keep every unit guarded, no loose rook.
- K+Q vs K = MATE, NOT STALEMATE. T39R4 I stalemated a lone king from a whole queen up: my Kc6 faced his Kc8 with no check = stalemate. Procedure: keep the queen a KNIGHT'S MOVE from his king until he is on the edge; bring my king up; when his king is on the edge put my king directly opposite, then GIVE CHECK on the edge (queen covered by my king) = mate. Before EVERY quiet king/queen move in the endgame ask 'does his king still have a legal move?'; if not it MUST be check. My king directly facing his on a file/rank with no check is the stalemate trap.
- T38R2 conversion model (won m60): after winning the queen - trade when the recapture is even, rooks on open files hitting loose bishops, harvest pawns, push the a-passer, K+Q+B mate with safe checks.
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blunder (T38R7 52 s on 18.c5). The written scan, not the clock, is the check.

## Openings (only the lines I actually play)
- Italian Giuoco Pianissimo W (0-10): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 Bb6 (16 plies). Then Re1/Bc2/Nf1-g3 with ...h6/...Re8/...Qd7/...Rad8. T39R7 vs Sol: after ...d5/...Nxd5 and ...Bg4/...Bxe3/...Qe7 he regained the e-pawn; then 21.Qd5?? Nxd5 lost my queen. Do NOT put the queen on d5 while his f6-knight lives. Sonnet waited: 26.Bf4?? then 27.Re4?? lost B and R. BANS: 10.d4?!, 12.c4? after ...Nxd5, 13.Bc2??, 14.Bg5?? (h6 ATTACKS g5), 15.Nxe5?? when d6 guards e5, 25.Rxc6?? bxc6, 16.d4?, 24.Qh5?? (Bf7-g6-h5). ...Nf4/...Be6/...Bd4/...Qg5 g2-battery is the main danger. Pattern after his ...d5/...Nxd5: I end a pawn down; 18...b5 opened a7-c7 and 19.Rxc7?? Rxc7 lost a rook; later 36.Be6?? was unguarded (Kxe6). Re-walk every line a pawn move opens.
- Sol's Italian plan: his ...d5 break with ...Nxd5, then ...Nf4 hitting d3; ...Nxe3 + ...Bxc4 wins my loose Nc4 (its only guard is the d3-pawn). After his ...d5 do NOT push c4 (Nf4) and do NOT play Bc2 - keep d3 guarded and MANOEUVRE (Nf1/Ne4/Nb3/Re2), or accept the pawn trade with a safe knight.
- Open Sicilian W (Taimanov quiet 6.Be2): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1 central play. T39R4 vs GLM I reached the 4...Nxd4 5.Qxd4 e5 6.Qd3 line: 14...Nd5?? 15.exd5 won a knight and 16.dxe6 won a bishop - converts by trading, but I then fumbled it (Rules 1/1b/4). vs Dragon 7...d5 block ...Qa5+ with Bd2/Bd1, never Qd2??. Accelerated Dragon (4...g6): keep Be3 - it is the d4-knight's guard; 9.Bf4?? Bxd4 won a knight, so answer ...Ng4 with Qd2/Rad1, and never Nf6+ while his e7-pawn stands (T40R2).
- Taimanov B vs 8.e5 Nd5 9.Qg4: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (15 plies). With my king on e8 g7 has NO guard: never ...d6, never castle; COVER g7 (...Bf8/...Kf8) or kick her with ...h5 ONLY if g7 is also guarded by a piece. NEVER ...Nf6 (T38R6 9...Nf6?? 10.exf6).
- vs 6.Be2 quiet: 11...Nd5! then 12...exd5; never a bishop on e5's capture square (14...Bf6?? exf6). Do NOT land a knight on c5 with no pawn guard (T37R7). Recapture ...gxf6 or keep c5 covered. T40R1 vs Sol: the book (…d5/…Nxd4/…Bxf6/…Qxf6/…Nc5/…Qd4+/…Bd7) reached a LEVEL middlegame; I then won Q for R and lost it back (Rule 4).
- Caro B 4.Be2: knight plan ...Nd7 then ...Ne7 (NEVER ...Ngf6 while e5 stands: T39R1 6...Ngf6?? 7.exf6), Nh4 Bg6, recapture ...hxg6, never ...Nxg6?!. Clamp lines: ...f6 removes f7's guard of g6, ...Be4 loses to Nxe4; safe plans are ...Bxd3/...cxd4.
- Caro Advance B (T39R6 0-1): 3.e5 c5 4.Nf3 cxd4 5.Bb5+ Nc6 6.Qxd4 e6 7.O-O Be7?! 8.Qg4! - g7 is king-guarded only, so 8...h5?? 9.Qxg7! Bf8 10.Qxh8 loses a ROOK (a kick does not defend a target). Cover g7 or trade queens; never ...Qxd4/...Qd6 (Bf4 answers exd6), never ...Nf6/...Ngf6 while e5 stands. Once down material vs SF: no grabs, trade only safely.
- QGD Bb4/5.Bg5 IQP B: 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Bb4 5.Bg5 O-O 6.e3 c5 7.Bxf6 Qxf6 8.Bd3 (16 plies). BANS: 12.Qd3?!, 14.Qg3??, 28.Qg2??, 31.f3??.
- English as Black (WINS g162, T38R2; DRAW g168): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d4 (15 plies). Solid QGD-reversed; ...Nbd7 ...Re8 ...Bf8 ...Qc7, ...c5 break, ...Qb6 pressure, take undefended queenside pawns. T38R2: his Qd3 hung to ...Qxd3 after ...Qa6.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his ranks/rays/pawn diagonals/KNIGHT squares, takes any 'offered' piece when my recapturer cannot reach it. Give him NO loose unit; resolve central tension BEFORE castling. T39R1: down N for P I guarded every unit and forced a Kd8/Ke8 repetition - SF19 accepted the draw. When a piece down vs him, aim for a repetition: a half point is a save. T39R6: once I blundered a rook he converted without a slip - no repetition rescue when he is far ahead and can push. T40R2: takes any piece on a pawn's square (Bxd4, exf6, gxf4) - keep Be3 on the d4-knight and the queen off pawn squares.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square. Answer the battery FIRST.
- Sonnet 5.5 (never beaten): banks clock; takes every free unit, every piece on a pawn's capture square, and every UNGUARDED quiet development (T39R2 26.Bf4?? Nxf4, then 27.Re4?? Rxe4); rook-check deflection, forks, clean mate. Give him no free unit, no pawn-hit square, no lone-guarded queen; keep a rank-1 blocker/luft; list his rook checks before any queen move. As Black he mirrored my Giuoco Pianissimo and waited for the ...d5 break plus one loose move.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn OR bishop diagonal OR KNIGHT square, and any UNGUARDED developed piece. Italian: ...d5 break, then ...Nxd5 and ...Nf4 hits d3; ...Bxc4 wins a loose Nc4; ...Rxe1+/...Rxa1 and ...Rg1+/...Rh1# with Bf3 covering g2. T39R7: ...Bg4 pin, ...Bxe3, ...Qe7, ...e4, ...Nxe5/...Qxe5 won the e-pawn; later Nxd5 won my Qd5. T40R1 Taimanov 6.Be2: his Bf5-c8 diagonal won my loose Rac8 the moment my d7-blocker left, then a check took my queen for a rook - keep rooks defended and do not vacate a blocker on his bishop's line. Answer a mate threat WITHOUT putting my queen on his bishop's line; re-guard a knight before pushing its guarding pawn. T39R5 in my Pianissimo: ...a6/...Ba7/...Re8/...Bf5, ...Nxe3/...Qxd3/...Bxd3 won d3 and traded queens; ...b5 opened Ra7-c7 (19.Rxc7?? Rxc7); later ...Kxe6 won my unguarded Be6.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3 and the Chigorin; takes every loose piece at once, converts cleanly, finishes with a Q+R battery. Give him no loose unit.
- GLM 5.3 Flash (I have beaten him; T39R4 I DREW a winning game): slow, sloppy, illegal tries, misstates material; hangs loose pawns and undefended pieces. As White he plays the English g3/d3/e4 QGD-style; as Black the Taimanov / 4...Nxd4 5.Qxd4 e5 line. Defends a lost position ACTIVELY and waits for my one loose unit - so convert cleanly: no repetition, simple won ending, guard every unit, and MATE a lone king instead of stalemating it.
