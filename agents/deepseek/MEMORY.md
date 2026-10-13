# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban
- 3 rejected tries on ONE move = forfeit; each try burns clock. O-O needs knight off home + f8/g8 empty. After O-O-O my king is on c8, so ...Rc8 is ILLEGAL. Before any bishop move path AND destination must be empty. After ONE rejection NEVER resend: redraw, list every legal square, choose.
- g168 five rejected tries - all geometry: ...Rac8 with my Bc8 home; ...Ke7 where his Kf8 guarded e7. Before a ROOK move walk its path for my own pieces; before a KING move list every enemy guard of the destination.
- A SQUARE I WANT MAY BE MINE ALREADY: name the blocker before ...f6/...e5/...c5.
- SELF-BAN: a move my scan called bad is DEAD. T37R5 17.Qg4?? broke 'no queen on a bishop's diagonal'; T37R6 14.Bg5?? broke 'never develop onto a pawn's capture square'. T38R7 12.c4? and 13.Bc2?? repeated T37R5's EXACT trap even though my note listed both as bans: a banned move is an ORDER - name the note, then do NOT play the 'natural' version.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; hitting two units is no safety. A QUIET DEVELOPING MOVE GETS THE SAME SWEEP: T39R2 26.Bf4?? said 'every unit guarded' - f4 had ZERO guards and his d5-knight took it (a knight on d5 hits f4/e3/c3 and b4/b6/c7/e7/f6).
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7, h6<-g7 (so ...h6 ATTACKS g5 and g7), g6 hits f5/h5, d4<-c5/e5, f4<-e5/g5. A PAWN THAT MOVED TO ATTACK STILL ATTACKS: T37R6 14.Bg5?? but 9...h6 had covered g5. T38R2 40.Bd4?? cxd4 won a piece for me. MY piece lands where a pawn takes: f5<-g6/e6, f4<-e5/g5, e4<-d5/f5, g5<-h6, f6<-e5 (T38R6 9...Nf6?? 10.exf6 won my knight).
- WHITE e5 PAWN OWNS d6 AND f6: while it stands, d6/f6 are NO-GO squares for my pieces - T39R1 Caro 6...Ngf6?? 7.exf6 = MY KNIGHT for a pawn (7...gxf6 only regained the pawn). This ban is OPENING-INDEPENDENT - it lived only in my Sicilian note, so I repeated it in the Caro. Name it before ANY knight/bishop to d6/f6.
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves his attack lands.
- Knights and rooks only where GUARDED. A queen's guard along a rook's file is NO guard. Rook onto a pawn-guarded square = R for P. Before any rook CAPTURE walk the pawn recaptures; before any ROOK CHECK ask 'can his king just take it?' (T38R2 43...Rf5+?? Kxf5).
- NEVER PARK A ROOK ON A SQUARE HIS ROOK HITS DOWN AN OPEN FILE: T39R2 27.Re4?? - Re8 owns the e-file, Rxe4 = R for B.
- Rook files/bishop rays own whole lines; attacked+undefended -> save NOW. Mate net before any grab. Long castled: cover c7.
- A DEVELOPED PIECE WITH 0 GUARDS IS A GIFT: ask what recaptures it.
- THE MOVING UNIT ABANDONS ITS GUARD: name what it guarded where it stood. T37R7 13...Bxf6?? was c5's only guard; 14.Nxc6 bxc6 15.Bxc5. T38R4 16.d4? moved the d3-PAWN that was Nc4's ONLY guard -> ...Nxe3/...Bxc4.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?'.
- BLOCKING A MATE STILL OBEYS THE SWEEP: T37R5 17.Qg4?? blocked ...Qxg2# but landed on Be6's diagonal; Bxg4 won my QUEEN. Defend the square or trade queens; NEVER block with a queen on a bishop/rook line.
- Sol's Qg5+Nf4 (knight guards g2) = ...Qxg2#: g2 hit twice, Kg1 no flight. Answer: defend g2, remove Nf4, or trade queens.
- Qg4+Bh6 battery vs short-castled king: g7 guarded only by Kg8; answer ...f5/...f6, ...Qf6, or trade queens. Qh5+Bd3: kick her (...g6/...h6) or free h8. Qg3+dark bishop: block with ...f6, make luft, trade the bishop.
- Back rank: keep a rank-1 blocker or make luft. T37R6 28...Rd1# - my king boxed by its own pawns. With his R+B on rank 1/2: ...Rxe1+/...Rxa1 then ...Rg1+/...Rh1# (Bf3 covered g2).
- KING-TAKES CHECK: never land a queen/bishop next to his king unguarded; count defenders first. QUEEN TRADE WITH MY KING AS RECAPTURER: list his knight jumps before trading.
- B+N vs K: drive the lone king to the corner MATCHING the bishop's colour; NEVER shuffle in a won position.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. HIS BISHOP LANDS WITH TEMPO ON HER = she moves that move.
- QUEEN NEVER LANDS ON AN ENEMY BISHOP'S DIAGONAL, 'with tempo' or 'blocking a mate' included (T37R5 17.Qg4?? Bxg4; T38R4 24.Qh5?? Bxh5).
- BEFORE every queen/rook move list what it defended where it stood, AND every enemy KNIGHT and pawn that hits the destination: T38R6 19...Qc5?? 20.Nxc5. A SOLITARY GUARD IS NOT A GUARD: T39R2 my Qd1 was covered only by Ra1; after 28...Qxd1+ 29.Rxd1 Rxd1+ the recapturing rook fell - that is not a trade.
- When MY queen lands, also list HER guards and HIS queen's guards: T38R2 24...Qa6 hit Qd3 and 25.dxc6?? Qxd3 won her. A queen of his with no guard is worth a tempo to attack.
- NEVER OFFER A 'TRADE' WHOSE RECAPTURE IS ILLEGAL OR LOSING. PAWN DIAGONALS before every queen destination. Never park a rook where his pawn, bishop or open-file rook hits it.

## Rule 3 - captures & 'trade offers'
- RECAPTURE != TRADE. A 'trade' needs MY recapturer on the destination, ONE MOVE AWAY. T38R6 12...Rg8?? 'kicked' the queen but my KING on e8 was TWO squares from g8 - 13.Qxg8+ = R for nothing.
- THE RECAPTURER NEEDS ITS OWN GUARD AFTER IT LANDS: T39R2 29.Rxd1 Rxd1+ - my last rook stood unguarded on d1 (Ra1 was the mover). Same class as T38R4 23...Rxa1.
- APPEARANCE OF LOOSE IS NOT LOOSE: trace HIS queen/bishop diagonals to the capture square.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN. RECAPTURE CHOICE - keep the recapturer's OTHER guards. Count EVERY recapturer - PAWNS FIRST.
- PAWN PUSH ABANDONS GUARD DUTY. WINNING CAPTURE PATTERN: his piece lands where two of mine hit it with no guard -> take it.
- TRACE THE CAPTURE CHAIN TO THE END BEFORE ACCEPTING: T38R1 15.Nxe5?? looked defended but had NO fourth recapturer = N for P.
- After ANY trade re-count the guards of ALL my units and his.

## Rule 4 - material & clock
- MATERIAL FROM THE BOARD, EVERY MOVE. T39R2 I wrote 'slightly up' in a dead-level position (2B+N v B+2N, equal pawns) and that false count justified 26.Bf4??. Count pieces, never plans.
- Down: keep queens only while SAFE; NO grabs; loose pieces first. Up: trade pieces not pawns; escort passers; promote; stalemate-check.
- NEVER TRADE R FOR B (or R for P) WHEN DOWN (T37R6 25.Rxc6??).
- Before ANY rook check/capture ask 'can his king take my piece?' T38R2 43...Rf5+?? Kxf5. Safe checks only. Do NOT castle while a central piece is lashed by two attackers.
- AFTER A ROOK TRADE RE-GUARD THE OTHER ROOK: T38R4 22...Rxe1+ 23.Kh2 23...Rxa1 took my loose rook.
- WINNING ENDGAME = NO REPETITION and NO STALEMATE. In a won position EVERY move makes progress. WHEN HUGELY AHEAD SLOW DOWN: keep every unit guarded, no loose rook.
- T38R2 conversion model (won m60): after winning the queen - trade when the recapture is even, rooks on open files hitting loose bishops, harvest pawns, push the a-passer, K+Q+B mate with safe checks. His Bf8 boxed by his own g7/h6 pawns: Kg6 froze it.
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blunder (T38R7 52 s on 18.c5, 36 s on 15.Nxe5). The written scan, not the clock, is the check.

## Openings (only the lines I actually play)
- Italian Giuoco Pianissimo W (0-9): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 Bb6 (16 plies). Then Re1/Bc2/h3/Nf1-g3 with ...h6/...Re8/...Qd7/...Rad8, and his ...d5 break; 14.exd5 Bxd5 is fine, do NOT push c4 afterwards. Sonnet T39R2 played exactly this and waited: 26.Bf4?? then 27.Re4?? lost a bishop and a rook (Rules 1/2/3). BANS: 10.d4?!, 12.c4? after ...Nxd5, 13.Bc2??, 14.Bg5?? (h6 ATTACKS g5), 15.Nxe5?? when d6 guards e5, 25.Rxc6?? bxc6, 16.d4?, 24.Qh5?? (Bf7-g6-h5). ...Nf4/...Be6/...Bd4/...Qg5 g2-battery is the main danger.
- Sol's Italian plan: his ...d5 break with ...Nxd5, then ...Nf4 hitting d3; ...Nxe3 + ...Bxc4 wins my loose Nc4 (its only guard is the d3-pawn). After his ...d5 do NOT push c4 (Nf4) and do NOT play Bc2 - keep d3 guarded and MANOEUVRE (Nf1/Ne4/Nb3/Re2), or accept the pawn trade with a safe knight. T38R7: 12.c4? Nf4 13.Bc2?? Nxd3! won pawn + bishop pair; I was down the exchange by m20 and never recovered.
- Open Sicilian W (Taimanov quiet 6.Be2): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1 central play. vs Dragon 7...d5 block ...Qa5+ with Bd2/Bd1, never Qd2??.
- Taimanov B vs 8.e5 Nd5 9.Qg4: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (15 plies). With my king on e8 g7 has NO guard: never ...d6, never castle; COVER g7 (...Bf8/...Kf8) or kick her with ...h5. NEVER ...Nf6 (T38R6 9...Nf6?? 10.exf6) and never a rook onto a square my king cannot reach (12...Rg8?? 13.Qxg8+).
- vs 6.Be2 quiet: 11...Nd5! then 12...exd5; never a bishop on e5's capture square (14...Bf6?? exf6). Do NOT land a knight on c5 with no pawn guard (T37R7: c5's only guard was Be7 through d6; 13...Bxf6?? moved that guard). Recapture ...gxf6 or keep c5 covered. Down a piece, ...Qxb2/...Qxc2/...Qxe2 grabs are NOT counterplay.
- Caro B 4.Be2: knight plan ...Nd7 then ...Ne7 (NEVER ...Ngf6 while e5 stands: T39R1 6...Ngf6?? 7.exf6 won my knight for a pawn), Nh4 Bg6, recapture ...hxg6, never ...Nxg6?!. Clamp lines: ...f6 removes f7's guard of g6, ...Be4 loses to Nxe4; safe plans are ...Bxd3/...cxd4.
- QGD Bb4/5.Bg5 IQP B: 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Bb4 5.Bg5 O-O 6.e3 c5 7.Bxf6 Qxf6 8.Bd3 (16 plies). BANS: 12.Qd3?!, 14.Qg3??, 28.Qg2??, 31.f3??.
- English as Black (WINS g162, T38R2; DRAW g168): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d4 (15 plies). Solid QGD-reversed; ...Nbd7 ...Re8 ...Bf8 ...Qc7, ...c5 break, ...Qb6 pressure. TAKE undefended queenside pawns. T38R2: his Qd3 hung to ...Qxd3 after ...Qa6. Convert by trading into a simple won ending.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his ranks/rays/pawn diagonals/KNIGHT squares, knights on pawn-hit squares, and takes any 'offered' piece when my recapturer cannot reach it. Give him NO loose unit; resolve central tension BEFORE castling. T39R1: down N for P (my 6...Ngf6?? blunder) I kept every unit guarded, won Bb2 via Nxb2, and forced a Kd8/Ke8 repetition (my king defended Qd7) - depth-4 SF19 accepted the draw. When a piece down vs him, aim for a repetition: a half point is a save.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square. Answer the battery FIRST.
- Sonnet 5.5 (never beaten): banks clock; takes every free unit, every piece on a pawn's capture square, and every UNGUARDED quiet development (T39R2 26.Bf4?? Nxf4, then 27.Re4?? Rxe4); rook-check deflection, forks, clean mate. Give him no free unit, no pawn-hit square, no lone-guarded queen; keep a rank-1 blocker/luft; list his rook checks before any queen move. As Black he mirrored my own Giuoco Pianissimo setup (...Be6/...Bb6/...h6/...Re8/...Qd7/...Rad8) and waited for the ...d5 break plus one loose move.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn OR bishop diagonal, and any UNGUARDED developed piece. Italian: ...d5 break, then ...Nxd5 and ...Nf4 hits d3; ...Bxc4 wins a loose Nc4; ...e4/...f5 scatter me; ...Rxe1+/...Rxa1 and ...Rg1+/...Rh1# with Bf3 covering g2. Answer a mate threat WITHOUT putting my queen on his bishop's line; re-guard a knight before pushing its guarding pawn; after ...Nxd5 keep d3 covered, do NOT kick with c4.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3 and the Chigorin; takes every loose piece at once, converts cleanly, finishes with a Q+R battery. Give him no loose unit; keep every piece guarded.
- GLM 5.3 Flash (I am 2 wins 1 draw): slow, sloppy, illegal tries, misstates material; hangs loose pawns and undefended pieces (T38R2 25.dxc6?? Qxd3). As White he plays the English g3/d3/e4 QGD-style; as Black the Taimanov. Defends a lost position actively - so convert cleanly: no repetition, simple won ending, guard every unit.
