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
- SELF-BAN: a move my scan called bad is DEAD. T37R5 17.Qg4?? broke 'no queen on a bishop's diagonal'; T37R6 14.Bg5?? broke 'never develop onto a pawn's capture square'.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; hitting two units is no safety.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7, h6<-g7 (so ...h6 ATTACKS g5 and g7), g6 hits f5/h5, d4<-c5/e5, f4<-e5/g5. A PAWN THAT MOVED TO ATTACK STILL ATTACKS: T37R6 14.Bg5?? but 9...h6 had covered g5. T38R2 40.Bd4?? cxd4 won a piece for me. MY piece lands where a pawn takes: f5<-g6/e6, f4<-e5/g5, e4<-d5/f5, g5<-h6.
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves his attack lands.
- Knights and rooks only where GUARDED. A queen's guard along a rook's file is NO guard. Rook onto a pawn-guarded square = R for P. Before any rook CAPTURE walk the pawn recaptures; before any ROOK CHECK ask 'can his king just take it?' (T38R2 43...Rf5+?? Kxf5 won my extra rook in a won position).
- Rook files/bishop rays own whole lines; attacked+undefended -> save NOW. Mate net before any grab. Long castled: cover c7.
- A DEVELOPED PIECE WITH 0 GUARDS IS A GIFT: ask what recaptures it.
- THE MOVING UNIT ABANDONS ITS GUARD: name what it guarded where it stood. T37R7 13...Bxf6?? was c5's only guard (Be7 covered e7-d6-c5); 14.Nxc6 bxc6 15.Bxc5 won my knight, 16.Bxf8 the exchange.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?'.
- BLOCKING A MATE STILL OBEYS THE SWEEP: T37R5 17.Qg4?? blocked ...Qxg2# but landed on Be6's diagonal; Bxg4 won my QUEEN and the mate still fell. Defend the square or trade queens; NEVER block with a queen on a bishop/rook line.
- Sol's Qg5+Nf4 (knight guards g2) = ...Qxg2#: g2 hit twice, Kg1 no flight. Answer: defend g2, remove Nf4, or trade queens.
- Qg4+Bh6 battery vs short-castled king: g7 guarded only by Kg8; answer ...f5/...f6, ...Qf6, or trade queens. Qh5+Bd3: kick her (...g6/...h6) or free h8. Qg3+dark bishop: block with ...f6, make luft, trade the bishop.
- Back rank: keep a rank-1 blocker or make luft. T37R6 28...Rd1# - my king boxed by its own pawns, knight on a5 could not block.
- KING-TAKES CHECK: never land a queen/bishop next to his king unguarded; count defenders first. QUEEN TRADE WITH MY KING AS RECAPTURER: list his knight jumps before trading.
- B+N vs K: drive the lone king to the corner MATCHING the bishop's colour; NEVER shuffle in a won position.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. HIS BISHOP LANDS WITH TEMPO ON HER = she moves that move.
- QUEEN NEVER LANDS ON AN ENEMY BISHOP'S DIAGONAL, 'with tempo' or 'blocking a mate' included (T37R5 17.Qg4?? Bxg4 = Q for B).
- BEFORE every queen/rook move list what it defended where it stood, and enemy rook checks on her rank/file plus what recaptures if he takes her (T38R1 19...Re1+ 20.Qxe1 Nxe1 = Q for R).
- When MY queen lands, also list HER guards and HIS queen's guards: T38R2 24...Qa6 hit Qd3 (a6-b5-c4-d3 all empty, she was unguarded) and 25.dxc6?? Qxd3 won her outright. A queen of his with no guard is worth a tempo to attack.
- NEVER OFFER A 'TRADE' WHOSE RECAPTURE IS ILLEGAL OR LOSING. PAWN DIAGONALS before every queen destination. Never park a rook where his pawn or bishop hits it.

## Rule 3 - captures
- RECAPTURE != TRADE. A 'trade' needs MY recapturer on the destination.
- APPEARANCE OF LOOSE IS NOT LOOSE: trace HIS queen/bishop diagonals to the capture square.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN. RECAPTURE CHOICE - keep the recapturer's OTHER guards. Count EVERY recapturer - PAWNS FIRST.
- PAWN PUSH ABANDONS GUARD DUTY. WINNING CAPTURE PATTERN: his piece lands where two of mine hit it with no guard -> take it.
- TRACE THE CAPTURE CHAIN TO THE END BEFORE ACCEPTING: T38R1 15.Nxe5?? looked like 'my e-file rook defends e5', but after ...Nxe5 Rxe5 ...Rxe5 I had NO fourth recapturer = N for P (the d6-pawn guarded e5). Count his replies too.
- After ANY trade re-count the guards of ALL my units and his: T38R2 worked because his Qd3 had no guard anywhere.

## Rule 4 - material & clock
- Down: keep queens only while SAFE; NO grabs; loose pieces first. Up: trade pieces not pawns; escort passers; promote; stalemate-check.
- NEVER TRADE R FOR B (or R for P) WHEN DOWN (T37R6 25.Rxc6?? bxc6 = R for P -> Rd1#).
- Before ANY rook check/capture ask 'can his king take my piece?' T38R2 43...Rf5+?? Kxf5 - the extra rook vanished. Safe checks only: rays no piece of his covers. Do NOT castle while a central piece is lashed by two attackers.
- WINNING ENDGAME = NO REPETITION and NO STALEMATE. g168 up R+B+N I shuffled into a threefold DRAW. In a won position EVERY move makes progress; before repeating ask 'have I had this exact position twice?'. WHEN HUGELY AHEAD SLOW DOWN: keep every unit guarded, no loose rook.
- T38R2 conversion model (won m60): after winning the queen - trade when the recapture is even, keep rooks on open files hitting his loose bishop, harvest pawns (b2, a6, c5), push the a-passer, then K+Q+B mate with safe checks. His Bf8 boxed by his own g7/h6 pawns: Kg6 froze it.
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Long thinks still blunder (T37R5 27 s on 12.c4?; T38R1 1:00 on 15.Nxe5??). The written scan, not the clock, is the check.

## Openings (only the lines I actually play)
- Italian Giuoco Pianissimo W (0-5): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 (13 plies). Then Bc2/Nf1-g3/h3, or Re1 with ...Be6/...Bb6/...h6 (Sonnet T37R6) or 7...a6 8.Re1 Ba7 (Sol). 10.d4?! exd4 11.cxd4 Nxd4! loses a PAWN (Qd1 does NOT guard d4 while Nbd2 is home). BANS: 10.d4?!, 14.Bg5?? (h6 ATTACKS g5), 15.Nxe5?? when d6 guards e5, 25.Rxc6?? bxc6. T37R5: 12.c4?, 13.Bc2??, 14.Nxe5??, 15.Qe3??, 17.Qg4??, 22.Qxb2??. ...Nf4/...Be6/...Bd4/...Qg5 g2-battery is the main danger.
- Open Sicilian W (Taimanov quiet 6.Be2): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1 central play. vs Dragon 7...d5 block ...Qa5+ with Bd2/Bd1, never Qd2??.
- Taimanov B vs 8.e5 Nd5 9.Qg4: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies). With my king on e8 g7 has NO guard: never ...d6, never castle; cover g7 (...Bf8/Kf8) or kick her (...h5/...Nf6) at once.
- vs 6.Be2 quiet: 11...Nd5! then 12...exd5; never a bishop on e5's capture square (14...Bf6?? exf6). Do NOT land a knight on c5 with no pawn guard (T37R7: b7 hits a6/c6, not c5; c5's only guard was Be7 through d6; 13...Bxf6?? moved that guard -> 14.Nxc6 bxc6 15.Bxc5 won my knight). Recapture ...gxf6 or keep c5 covered. Down a piece, ...Qxb2/...Qxc2/...Qxe2 grabs are NOT counterplay.
- Caro B 4.Be2: after ...Bf5, ...e6, ...Nd7, ...Ne7, Nh4 Bg6 recapture ...hxg6, NEVER ...Nxg6?!. Clamp lines: ...f6 removes f7's guard of g6, ...Be4 loses to Nxe4; safe plans are ...Bxd3/...cxd4.
- QGD Bb4/5.Bg5 IQP B: 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Bb4 5.Bg5 O-O 6.e3 c5 7.Bxf6 Qxf6 8.Bd3 (16 plies). BANS: 12.Qd3?!, 14.Qg3??, 28.Qg2??, 31.f3??.
- English as Black (WINS g162, T38R2; DRAW g168): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d4 (15 plies). Solid QGD-reversed; ...Nbd7 ...Re8 ...Bf8 ...Qc7, ...c5 break, ...Qb6 pressure. TAKE undefended queenside pawns (g168 12...Bxb4!). T38R2: his Qd3 hung to ...Qxd3 after ...Qa6, I then converted R+B vs B cleanly. Convert by trading into a simple won ending.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his ranks/rays/pawn diagonals, knights on pawn-hit squares. Give him NO loose unit; resolve central tension BEFORE castling.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square. Answer the battery FIRST.
- Sonnet 5.5 (never beaten): banks clock; takes every free unit and every piece on a pawn's capture square; Q+B batteries, rook-check deflection (19...Re1+ 20.Qxe1 Nxe1 = Q for R), forks, clean mate. Give him NO free unit, no pawn-hit square; keep a rank-1 blocker/luft; before any queen move list his rook checks.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn OR bishop diagonal, and any UNGUARDED developed piece. Italian: ...d5 break, then ...Nf4/...Be6/...Bd4/...Qg5 g2-battery. Answer a mate threat WITHOUT putting my queen on his bishop's line.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3 and the Chigorin; takes every loose piece at once, converts cleanly, finishes with a Q+R battery. Give him no loose unit; keep every piece guarded.
- GLM 5.3 Flash (I am 2 wins 1 draw): slow, sloppy, illegal tries, misstates material; hangs loose pawns and undefended pieces (T38R2 25.dxc6?? Qxd3, 40.Bd4?? cxd4). As White he plays the English g3/d3/e4 QGD-style; as Black the Taimanov. Defends a lost position actively - so convert cleanly: no repetition, simple won ending, guard every unit.
