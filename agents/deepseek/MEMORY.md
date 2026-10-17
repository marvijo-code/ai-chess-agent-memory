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

## Rule 0 - legality & self-ban
- 3 rejected tries on ONE move = forfeit; each burns clock. Walk EVERY move's path for MY OWN pieces FIRST - pawns and knights included. T44R3 blew a level game on 'b4' with my own knight on b3. T45R4: I tried an illegal Rxa8+ before the legal Rxa2 - one rejection, clock lost. Name the exact piece, square and path before any capture. O-O needs f1/g1 (f8/g8) empty; after O-O-O my king is on c8. A SQUARE I WANT MAY BE MINE ALREADY: name the blocker before ...f6/...e5/...c5/...Ne7.
- After ONE rejection never resend: redraw, list the LEGAL moves from that board, pick a DIFFERENT piece/idea.
- SELF-BAN: a move my scan called bad is DEAD (T38R7; T45R3 14.Bf4?? repeated a listed trap).

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; hitting two units is no safety.
- QUIET, 'TEMPO' AND RETREAT MOVES GET THE SAME SWEEP: T41R5 20.Ba4?? -> 20...Qxa4; T42R2 14.Nd6?? -> 15...Qxd6; T42R3 14...Bg5?? -> 15.Bxg5, 16.Bxd8. A piece landing on a diagonal: walk it to the END.
- HIS OWN PIECE BETWEEN HIS HEAVY PIECE AND MY DESTINATION IS NO SHIELD - he can MOVE THE SCREEN, a capture included. T45R4 20...Qc7??: only White's own Bc5 separated Qc2 from c7, but 21.Bxf8 took my bishop off that file and 22.Qxc7 won my QUEEN. Before stationing my queen/rook opposite his queen/rook, list every piece between (HIS included) and ask which can leave with tempo. WHEN A SCREEN LEAVES, the queen moves THAT move - no other recapture first.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f6<-e5, f5<-e6/g6, g5<-h6/f6, d4<-c5/e5, h6<-g7. A PAWN THAT MOVED STILL ATTACKS: T45R3 14.Bf4?? onto his e5-pawn's capture square -> exf4 won a BISHOP. NEVER put TWO of my pieces on ONE pawn's capture-square pair (T44R5 21...e5 -> 22.fxe5).
- N-FOR-P IS A LOSS EVEN WITH THE RECAPTURE. A knight on c6 is hit by his d5-pawn.
- KNIGHT/BISHOP LANDINGS: walk his queen's AND both bishops' diagonals AND every knight jump. A central knight jump needs EVERY recapturer counted: T45R2 13...Nd5?? with Qd1 and Nc3 both hitting d5 = N for nothing.
- WHITE e5 PAWN OWNS d6 AND f6 - no-go for every piece, QUEEN included (T45R5 12...Qd6?? exd6 lost her). With my king castled, Qg3 also PINS g7.
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves his attack lands. HIS PAWN MOVE RE-WALKS LINES.
- Rooks and knights only where GUARDED. Before a rook CAPTURE walk the pawn recaptures; before a ROOK CHECK ask 'can his king just take it?' (T38R2 43...Rf5+?? Kxf5). NEVER PARK A ROOK on his rook/bishop's line.
- THE MOVING UNIT ABANDONS ITS GUARD: name what it guarded. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY QUIET MOVE ELSEWHERE.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?'. BLOCKING A MATE STILL OBEYS THE SWEEP (T37R5 17.Qg4?? landed on Be6's diagonal).
- Qg4+Bh6 vs short-castled king (g7 king-guarded only): answer ...f5/...f6, ...Qf6, or trade queens. With my e8-king the Qxg7 net needs g7 guarded by a PIECE, not a pawn. Bd3+Qh6 vs MY short-castled king: Qxh7#.
- MY SHORT-CASTLED g8-KING behind g6+g7: his Qf6+Bh6 = Qg7# (T44R4); with his Bf6, Qxg6+ Kf8 Qg7+ Ke8 Qg8# (T44R5).
- Back rank: keep a rank-1 blocker or luft (T37R6 28...Rd1#). A rook that is the LAST guard of an entry square must not leave for a pawn (T44R2 26.Rxc5?? -> 26...Rd1#).
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. Before ANY check write 'what captures the checker?', the KING and every piece included.
- Q vs lone K: box with the queen a knight's move from his king, bring my king up, leave him a legal square every move - no stalemate.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. HIS BISHOP LANDING WITH TEMPO ON HER = she moves.
- QUEEN NEVER on an enemy bishop's diagonal or a knight's jump square, 'tempo'/'blocking a mate' included (T41R4 28...Qe5?? -> 29.Bxe5).
- A QUEEN CAPTURE STILL COUNTS RECAPTURERS TO HER DESTINATION; a 'trade offer'/check that does not cover the mate square is no defence.
- BEFORE every queen/rook move list what it defended where it stood AND every enemy knight and pawn that hits the destination. A BLOCKED GUARD IS NOT A GUARD (T40R3 32.Qxc4?? -> Rxc4).
- NEVER a queen on a PAWN's capture square. DOWN = NO grabs; defend WITHOUT her.

## Rule 3 - captures & 'trade offers'
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN. Count EVERY recapturer, PAWNS FIRST; trace the chain to the end.
- AN 'UNDEFENDED PIECE' IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P.
- AFTER A CAPTURE THAT WINS A PIECE, RESCAN FOR MY OWN LOOSE UNIT (T42R4 17.axb3?? -> Rxe4). After ANY trade re-count the guards of ALL my units.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE (count pieces, never prose); rescan after every trade.
- NO GRABS WHEN LEVEL OR BEHIND.
- CONVERTING: guard every unit, trade rooks evenly, two-rook ladder, Ra8#. Up: trade pieces not pawns, escort passers, stalemate-check; quiet consolidation only. DOWN: trade pieces, keep the rook active, take the recapture - T45R4 I lost my QUEEN (20...Qc7??), traded bishops/knights/rooks, won her back with 27...Rxa7 and won the R+P ending on his flag.
- CLOCK - 3600+10. T45R1 and T45R3 flagged; T45R4 kept ~22 min and GLM flagged. HARD CAP 30 s ANY move, routine 10-15 s; clock <15 min -> 5-10 s. Long thinks have NEVER saved a move (T45R4 still burned 3-5 min on routine rook moves).

## Openings (only the lines I actually play)
- English as Black (WINS T38R2, T41R4, T45R4; T44R1 flag win vs GLM): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d4 (16 plies); ...Nbd7/...Re8/...Bf8/...Qc7, ...c5 break, then ...Ne5. T45R4: 12...c5 13.e3, then 13...Ne5?! let 14.Nxe5 Qxe5 15.f4 Qe6 16.Ba3 hit c5; play ...Ne5 only with c5 safe and my queen OFF the c-file (17...Qd6, later 20...Qc7?? cost the queen). T41R4 13...Nd3?? = N for nothing; Re8 hung to Bc6xe8. T44R1 ...c5/...Nb6/...Ne4/...Nxg5 won a knight but 24...Qd1+?? Rxd1 threw it back - no queen on open ranks/files when rooks are live.
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); ...Na5, Bc2, ...c5, d4, Nbd2, ...Qc7, ...cxd4 Nc6. As Black vs Rc1/Bb1 pins move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo; Qc7 'defended' by Rc8 is still Rxc7. As White keep Rc1; no piece on a square his g6-pawn covers (f5/h5); no check he can capture.
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 O-O 6.O-O d6 7.Nbd2 a6 8.Bb3 Ba7 (16 plies); vs 5...d6 same setup with ...Be6/...Bb6, vs 7...Bg4 8.h3 Bxf3 9.Nxf3. BANS: 10.d4?!, 12.c4?, 13.Bc2??, 14.Bg5??, 15.Nxe5??, 24.Qh5??, 14.Bf4?? (his e5-pawn takes it), b4 WHILE MY KNIGHT IS ON b3, queen on d5 while his f6-knight lives. T44R2 vs Sol: 25.Rc1 was d1's only guard; make luft (h3), never move the last rank-1 guard for a pawn.
- Open Sicilian W vs 3...Nxd4 4...e5: 1.e4 c5 2.Nf3 Nc6 3.d4 Nxd4 4.Nxd4 e5 5.Nb5 a6 6.N5c3 Nf6 7.Be2 Be7 8.O-O O-O (16 plies); Be3/Qd2/Nd5/f4; keep the c4-bishop safe after the d5 space edge.
- Open Sicilian W (Taimanov 6.Be2): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1. vs Dragon block ...Qa5+ with Bd2/Bd1, never Qd2??. Accelerated Dragon: keep Be3 - the d4-knight's guard; answer SF's 8...Ng4 with Bb3/h3, never 9.Bd5?! (9...Nxe3 fxe3 ...Ne5!).
- Taimanov B vs 8.e5 Nd5 9.Qg4: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies). With my king on e8 g7 has NO guard: never ...d6, never castle, never ...Nf6; cover g7 with a PIECE or kick ...h5 only if g7 is guarded. Never ...f5 while exf6 e.p. opens lines to my king. Trade or reroute the d5 knight when his c-pawn/Ne4 can hit it.
- Taimanov B vs quiet 6.Be2/9.f4: ...d6/...Nxd4/...e5 recapture is standard (12...dxe5! only good), but after Bxe5 do NOT jump ...Nd5?? (Qd1 + Nc3) - play ...Qc7/...Bd7/...Rac8. Two passers then queen.
- Caro B 4.Be2/4.Nf3: knight plan ...Nd7 then ...Ne7 (NEVER ...Ngf6 while e5 stands); recapture ...hxg6, never ...Nxg6?!. ...Be4 loses to Nxe4.
- Caro Advance B: ...Ne7-f5 covers g7 before ...Be7; ...h5?? before g7 is guarded loses to Qxg7. Never ...f6 when the f5-knight is g7's only cover. The ...f6 break is a TRAP when White has f4+Bd3+Qe1: T44R5 12...f6? 13.exf6 Rxf6 14.Qg3, then 21...e5?? left Rf6+Bd6 to 22.fxe5 and 26.Qxg6+ Kf8 27.Qg7+ Ke8 28.Qg8#. T45R5: after 10...Nxb3 11.Qxb3 my b7-pawn is hit down the b-file - defend b7 (...Qb6/...Rb8) BEFORE ...Nf5; 11...Nf5?? 12.Qxb7, then 12...Qd6?? 13.exd6 (e5-pawn owns d6) won my queen.
- QGD Bb4/5.Bg5 IQP B: BANS 12.Qd3?!, 14.Qg3??, 28.Qg2??, 31.f3??.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares, and a forked piece's retreat square. Resolve central tension BEFORE castling; give him NO loose unit. A piece down: aim for repetition. ...Ng4/...Ne5 wins the outpost - trade it WITHOUT giving up the dark bishop or opening the e-file.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square.
- Sonnet 5.5 (never beaten): banks clock; takes every free and UNGUARDED unit, including a queen on a pawn's capture square (T45R5 exd6). No free unit, no pawn-hit square, no lone-guarded queen; keep a rank-1 blocker. Holds dead-level endings; converts a won exchange cleanly (T44R5 ...Bxg6/Bd4, mate on g8).
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn/bishop diagonal or knight square, and any loose recapture. Italian ...a6/...Ba7/...h6/...Re8, ...d5/...Nxd5 hits c3; his Nf4 + queen on c6-g2 = Qxg2#. T44R2: with +P in a rook ending he mated ...Rd1# when my c1-rook left d1. T45R2: f4/Kh1/Bxd4 then e5; he punished my central knight jump and made two passers queen.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3 and the Chigorin; takes every loose piece. Give him no loose unit.
- GLM 5.3 Flash: slow, illegal tries, miscounts material; hangs queens/rooks/undefended pieces when worse, but punishes MY loose knight jumps. T45R4: 4 illegal tries, 5-15 min single thinks (19.dxc5 6:39, 32.Rc7+ 14:52) and he FLAGGED while I kept ~22 min. vs GLM: play 10-15 s sound moves, guard every unit, take free captures, trade queens, and let his clock run out.
- Haiku 5.5: fast (2-22 s), solid Italian Pianissimo; gives no free material. T44R3: I FORFEITED (3 illegal tries) in a dead-equal position. T45R3: BEAT ME ON THE CLOCK; vs Haiku play 10-15 s a move and bank time.
