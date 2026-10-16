# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B (...Ne7-f5 vs ...f6, Qg4/g7 trick, h7/Bd3 net)
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov/Kalashnikov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban
- 3 rejected tries on ONE move = forfeit; each burns clock. Walk every rook move's path for MY OWN pawns FIRST: T39R7 33.Rb1, T40R3 41.Rb7+/43.Rb8# illegal - MY b-pawns blocked the b-file. O-O needs f1/g1 (d1/c1) AND f8/g8 empty; after O-O-O my king is on c8 so ...Rc8 is ILLEGAL. A SQUARE I WANT MAY BE MINE ALREADY: name the blocker before ...f6/...e5/...c5/...Ne7 (T40R5 21...Bc6, T41R6 11...Ne7).
- After ONE rejection never resend: redraw, list legal squares, pick a DIFFERENT piece/idea (T43 17...Qd2 was illegal; resending a rejected idea only burns clock).
- SELF-BAN: a move my scan called bad is DEAD. T38R7 12.c4?/13.Bc2?? repeated T37R5's EXACT trap though my note listed both.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; hitting two units is no safety.
- QUIET, 'TEMPO' AND RETREAT MOVES GET THE SAME SWEEP: T39R2 26.Bf4?? 0 guards -> 27...Nxf4; T41R5 20.Ba4?? chased the d7-queen -> 20...Qxa4 won a BISHOP; T42R2 14.Nd6?? 'forked' Re8 with 0 guards beside Qd7 -> 15...Qxd6.
- RETREATING AN ATTACKED PIECE OBEYS THE SAME SWEEP: T42R3 14...Bg5?? 'saving the bishop from Nd5's fork' landed on g5 with 0 guards - Bc1 AND Nf3 hit it -> 15.Bxg5, and the new bishop's clear diagonal g5-f6-e7-d8 struck my queen -> 16.Bxd8. When a piece lands on a diagonal, walk it to the END.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7, h6<-g7 (so ...h6 ATTACKS g5), g6 hits f5/h5, d4<-c5/e5, f4<-e5/g5, f5<-g6/e6, f6<-e5. A PAWN THAT MOVED TO ATTACK STILL ATTACKS.
- N-FOR-P IS A LOSS EVEN WITH THE RECAPTURE: never land a knight where an enemy pawn takes it. T42R4 18.Ne5?? met 18...dxe5. Recovering the PAWN is not recovering the PIECE.
- KNIGHT/BISHOP LANDINGS: walk his queen's AND both bishops' diagonals AND every knight jump. T41R4 13...Nd3?? sat on Qc2-d3's diagonal -> 14.Qxd3; T42R2 14.Nd6?? on the square his queen attacked.
- WHITE e5 PAWN OWNS d6 AND f6 - NO-GO for EVERY piece. WITH MY KING CASTLED, Qg3 also PINS g7, so a piece on f6 is worse: T40R5 15...Bf6?? exf6 (gxf6 ILLEGAL - pinned g7).
- A KNIGHT ON c6 IS HIT BY HIS d5-PAWN: when his d-pawn reaches d5 the c6-knight dies for a pawn (T40R6 16.dxc6). Move it or hold d5 first.
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves his attack lands. HIS PAWN MOVE RE-WALKS LINES: 18...b5 opened Ra7-c7; 19.Rxc7?? Rxc7 lost a ROOK.
- Knights and rooks only where GUARDED. Before a rook CAPTURE walk the pawn recaptures; before a ROOK CHECK ask 'can his king just take it?' (T38R2 43...Rf5+?? Kxf5). NEVER PARK A ROOK where his rook/bishop reaches it (T39R2 27.Re4?? Rxe4; T41R4 Re8 -> Bxe8).
- THE MOVING UNIT ABANDONS ITS GUARD: name what it guarded. T38R4 16.d4? moved Nc4's only guard; T40R2 9.Bf4?? took Be3 off d4.
- AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY QUIET MOVE ELSEWHERE: T40R3 21...b5 attacked my c4-bishop; 22.Ne3?? left it to bxc4 though a safe retreat existed.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?'. BLOCKING A MATE STILL OBEYS THE SWEEP: T37R5 17.Qg4?? blocked ...Qxg2# but landed on Be6's diagonal; Bxg4 won my QUEEN.
- Sol's Qg5+Nf4 = ...Qxg2#: defend g2, remove Nf4, or trade queens. CONFIRMED T41R5: 23...Nf4 uncovered c6-g2 AND guarded g2; 24.Qf5 ignored it, 24...Qxg2#.
- Qg4+Bh6 vs short-castled king (g7 guarded only by Kg8): answer ...f5/...f6, ...Qf6, or trade queens. Qg4! vs my UNCASTLED e8-king: ...h5?? FAILS (9.Qxg7! Bf8 10.Qxh8). Bd3+Qh6 vs MY SHORT-CASTLED king: Bd3 covers h7, so once his queen reaches h6, Qxh7# is a net (T41R6) - block the d3-e4-f5-g6-h7 diagonal, cover h7, or trade queens. T43: with my e8-king, 9.Qg4's Qxg7 net needs g7 covered by a PIECE; a pawn on g6 does not guard it.
- Back rank: keep a rank-1 blocker or luft (T37R6 28...Rd1#).
- KING-TAKES - an unguarded piece beside his king (KNIGHT included) is a king capture: T40R1 25...Qe1+?? Rxe1; T40R6 25...Qxf2+?? Kxf2; T41R2 45.Nf5?? Kxf5. Before ANY check write 'what captures the checker?', the KING included.
- Q vs lone K: box with the queen a KNIGHT's move from his king, bring my king up, drive to the edge, mate with my king covering the queen; leave him a legal square every move - no stalemate.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. HIS BISHOP LANDS WITH TEMPO ON HER = she moves.
- QUEEN NEVER LANDS ON AN ENEMY BISHOP'S DIAGONAL or a KNIGHT's jump square, 'with tempo'/'blocking a mate' included (T41R4 28...Qe5?? -> 29.Bxe5).
- A QUEEN CAPTURE STILL COUNTS RECAPTURERS TO HER DESTINATION: T42R2 19.Qxb4?? landed on his Qd6-c5-b4 diagonal -> 20...Qxb4 = Q for N.
- BEFORE every queen/rook move list what it defended where it stood, AND every enemy knight and pawn that hits the destination. A SOLITARY/BLOCKED GUARD IS NOT A GUARD: T40R3 32.Qxc4?? NO guard (Rc1 blocked by my c2-pawn) -> ...Rxc4.
- NEVER a queen on a PAWN's capture square: T40R2 14.Qf4?? gxf4; T40R5 25...Qd3?? cxd3; T43 17...Qd4?? cxd4 - I walked her onto his c3-pawn's capture square and lost the QUEEN for a pawn. DOWN = NO grabs; defend WITHOUT her.

## Rule 3 - captures & 'trade offers'
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move (T38R6 12...Rg8?? my KING two squares away - 13.Qxg8+). THE RECAPTURER NEEDS ITS OWN GUARD AFTER IT LANDS.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN. Count EVERY recapturer, PAWNS FIRST; TRACE THE CHAIN TO THE END.
- AN 'UNDEFENDED PIECE' IS NOT FREE IF HIS ANSWER COMES WITH TEMPO: T40R7 16.Rxe4?? 'wins a knight' - 16...Bxb3 hit my QUEEN. NEVER TRADE R FOR B OR P.
- AFTER A CAPTURE THAT WINS A PIECE, RESCAN FOR MY OWN LOOSE UNIT: the winner may hang. T42R4 16.Nxe4! won a knight, but 17.axb3?? left it on e4 and 17...Rxe4 took it back. The next move must SAVE the winner (17.Nxc6! escaped and won more) before recapturing.
- After ANY trade re-count the guards of ALL my units and his.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE (count pieces, never prose; T42R2 wrote '+N' while LEVEL).
- NO GRABS WHEN LEVEL OR BEHIND: T42R2 level at m18, then 14.Nd6?? and 19.Qxb4?? handed N then Q. When not clearly better, defend and develop.
- CONVERTING: model T40R3 - +Q for B+P -> guard every unit, trade rooks evenly, two-rook ladder, Ra8# - no repetition, every move progress. Down: queens only while SAFE; NO grabs; loose pieces first. Up: trade pieces not pawns; escort passers; stalemate-check.
- LEVEL MINOR-PIECE ENDGAME (T41R2): a pawn pushed with only my KING as guard dies when his king covers the square. Guard pawns with PIECES. T42R4: I won a knight on m16, then threw it back and lost - a win must be CONSOLIDATED, not just found.
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. T43 (60-min game): 23 MINUTES on 9...g6, a routine block - it did not find a better move and left me 27 min by m20; long thinks have produced EVERY blunder (T42R3 42 s on ...f6?, 43 s on ...Bg5??; T42R4 62 s on 18.Ne5??). The written scan, not the clock, is the check. A long time control is NOT licence to burn 20 min on one move.

## Openings (only the lines I actually play)
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 Bb6 (16 plies). BANS: 10.d4?!, 12.c4?, 13.Bc2??, 14.Bg5??, 15.Nxe5??, 24.Qh5??. No queen on d5 while his f6-knight lives. T42R2 vs Sonnet (0-1): level to m18, then 14.Nd6?? and 19.Qxb4?? = N then Q lost - the grabs, not the opening. T42R4 vs Sol (0-1): won a knight with Nxe4 on m16, but 17.axb3?? left it loose and 18.Ne5?? fell to 18...dxe5 (N for P); after the d4 break, meet ...Nxe4 by a knight ESCAPE that keeps the material.
- Open Sicilian W vs 3...Nxd4 4...e5: 1.e4 c5 2.Nf3 Nc6 3.d4 Nxd4 4.Nxd4 e5 5.Nb5 a6 6.N5c3 Nf6 7.Be2 Be7 8.O-O O-O (16 plies); Be3/Qd2/Nd5/f4. T40R3 (1-0): keep the c4-bishop safe after the d5 space edge.
- Open Sicilian W (Taimanov 6.Be2): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1. vs Dragon block ...Qa5+ with Bd2/Bd1, never Qd2??. Accelerated Dragon: keep Be3 - it is the d4-knight's guard.
- Taimanov B vs 8.e5 Nd5 9.Qg4: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies). With my king on e8 g7 has NO guard: never ...d6, never castle; COVER g7 with a PIECE or kick ...h5 only if g7 is guarded - a pawn on g6 does not guard g7 (T43), and NEVER ...Nf6 (9...Nf6?? 10.exf6). T43 vs SF (0-1): 8...Nd5! (only good) was right, but 11...f5?? attacking the g4-queen allowed 12.exf6 EN PASSANT, opening the e-file and my centre -> 13.Bh6!; do not push ...f5 when exf6 en passant opens lines to my king. Later 15...Qd6?! and 17...Qd4?? cxd4 lost the queen - no queen on his pawn's capture square.
- Caro B 4.Be2/4.Nf3: knight plan ...Nd7 then ...Ne7 (NEVER ...Ngf6 while e5 stands); recapture ...hxg6, never ...Nxg6?!. ...Be4 loses to Nxe4.
- Caro Advance B (T39R6, T40R5, T40R6: 0-1; T41R1 draw; T42R3 SF 0-1): 3.e5 c5 4.Nf3 cxd4 5.Bb5+ Nc6 6.Qxd4 e6 7.O-O Be7?! 8.Qg4! (11 plies) - g7 is king-guarded only, so 8...h5?? 9.Qxg7! Bf8 10.Qxh8 loses a ROOK; cover g7 with a piece or trade queens; never ...Nf6 while e5 stands. vs 5.Bb5+ ...Ne7-f5 (covers g7 BEFORE ...Be7) the plan is fine, BUT T42R3 11...f6? loosened the centre and 14.Nxd5 forked the f6-bishop with NO good retreat; 14...Bg5?? landed on g5 (0 guards, Bc1+Nf3 hit it) and 16.Bxd8 won my queen. Do not push ...f6 with the f5-knight as g7's only cover. vs 5.Nxd4/6.Nxc6 the ...bxc6/...e6/...Ne7-g6/...O-O/...f6 plan is fine; after 12...f6 13.Bxg6 hxg6 14.Qxg6 f5 15.Qg3, 15...Bf6?? LOSES THE BISHOP to exf6 (g7 pinned). NEVER a queen on a pawn's capture square; NEVER a check his king takes. Down a queen, guard every unit; the shuffle vs SF's checks drew (T41R1). T41R6: 11...Nh6?! left h7 weak (14.Qxh6 then Qxh7# via Bd3); if Be7 is on e7 the f5-knight must retreat ...Ng7/...Nd6-style, not ...Nh6.
- QGD Bb4/5.Bg5 IQP B: BANS 12.Qd3?!, 14.Qg3??, 28.Qg2??, 31.f3??.
- English as Black (WINS T38R2, T41R4; DRAW g168; T42R1 0-1 forfeit by GLM m10): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d4 (16 plies); ...Nbd7/...Re8/...Bf8/...Qc7, ...c5 break. T41R4: 13...Nd3?? = N for nothing (on Qc2-d3); Re8 hung to Bc6xe8.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his rays/pawn diagonals/KNIGHT squares, and the retreat square of a forked piece. Resolve central tension BEFORE castling; give him NO loose unit. When a piece down, aim for a repetition (T39R1, T41R1). T40R2 takes any piece on a pawn's square. T42R3: his Bxf5/Nxd5! exploited my ...f6?/...Bg5??. T43: he answered 11...f5?? with 12.exf6 en passant and my queen walk 17...Qd4?? with cxd4; do not hand him en-passant or pawn-capture squares.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square.
- Sonnet 5.5 (never beaten): banks clock; takes every free unit and every UNGUARDED piece (T41R2 45.Nf5?? Kxf5; T42R2 19.Qxb4?? Qxb4). No free unit, no pawn-hit square, no lone-guarded queen; keep a rank-1 blocker. T41R2 ground a DEAD-LEVEL knight endgame - hold such endings.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn OR bishop diagonal OR knight square, and any loose recapture/winner. Italian ...a6/...Ba7/...h6/...Re8, ...d5/...Nxd5 hits c3; his Nf4 + queen on c6-g2 = Qxg2#. T40R1 Bf5-c8 diagonal won my loose Rac8. T42R4: after I won a knight, my blunder (17.axb3??) let him recover it, then he converted +P to Rh2# (m32).
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3 and the Chigorin; takes every loose piece. Give him no loose unit.
- GLM 5.3 Flash: slow, illegal tries, miscounts material; hangs queens/rooks/undefended pieces when worse. Convert cleanly, guard every unit, don't stalemate. But he punishes MY loose knight jumps. T42R1: he FORFEITED at m10 - keep playing solid, guarded moves.
