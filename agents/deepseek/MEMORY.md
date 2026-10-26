# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance + Classical 3.Nc3 B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W (Classical + quiet 4.d3)
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - board, legality, clock
- BOARD MAP FROM HIS LAST MOVE BEFORE ANY CAPTURE OR QUEEN MOVE; a piece that moved is not on its old square. T67R5.1 20...Qd4?? on a ghost board - the d4-knight had gone to c6; 21.Nxd4 won my QUEEN.
- 3 rejected replies on one move = forfeit; ONE rejection = different piece AND idea. Walk piece, actual square, occupant, path, my own blockers. T69R4 1 illegal try (12...Nd7, a knight with no route) cost a minute.
- HIS last move first, then my destination: 0 guards + his capture = gift. Quiets/retreats get the same sweep.
- CLOCK: routine 10-15 s, cap 30; up material 5-10; lost position 5-10; never over 60 after move 20. T69R4 v SF spent 22 min in 23 moves (6:37 on ...Qxb7, 7:07 on ...f6, 3:21 on ...Rd7, ~1 min each on 9...Qc7/10...cxd4/13...Bxb4/14...Be7) and none of it found a defence. T68R1 flagged up two queens. The sweep is the spend, not the narrative.

## Rule 1 - destination sweep
- LIST HIS PAWN CAPTURES VS EVERY LANDING, KNIGHTS INCLUDED. White e5-pawn owns f6/d6; g4-pawn f5/h5. T66R2 16...Nf5?? gxf5; T62R2 14...Qd6?? exd6.
- MY OWN PIECE ON A LINE IS MY ONLY SCREEN; moving it exposes. T67R3 19...Bxe3?? 20.Qxc7 won my queen; T68R2 the d5-pawn screened Qd7 from Rfd1 and 13...d4/14...dxe3 cleared the d-file.
- TWO LOOSE UNITS IN A ROW THROW A WON OPENING. Every developing move: list my undefended pieces and his queen/rook/bishop reaching them in one.
- HITTING HIS QUEEN IS NOT AN ANSWER WHEN IT OPENS A CHECK.
- A PAWN THAT LEAVES ABANDONS ITS POST. Never ...f6 while my king is on e8/f8 and e6 has no piece guard - T69R4 21...f6 made an escape square but the f7-pawn had been e6's guard: 23.Nxe6 was MATE. QGD c6 guards d5: ...c5 only with a piece guard on d5.
- NEVER KNIGHT ON A SQUARE HIS PIECE/PAWN COVERS: d5-knight retreats b4/e7/b6/c7, never f6 while e5 lives, never f5 while g4 lives, never h6 while his dark bishop lives (T69R3 13.Bxh6).
- DON'T KICK A DEFENDED CENTRAL KNIGHT WITH A PAWN. T67R3 17...e5?? gave 18.Ndf5 with tempo on my e7-bishop.
- POSITIVE PAWN-TAKE: his Ne4, my d5-pawn and Nf6 alive: ...dxe4! dxe4 Nxe4 wins N+P for P.
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5; g4-pawn hits f5/h5.
- ROOKS/KNIGHTS only where guarded; rook check: can his king just take. The mover abandons its guard - name it. An attacked piece needs an answer before any quiet move.
- HIS KNIGHT LEAVING c6 CAN OPEN A BISHOP DIAGONAL TO HIS QUEEN. T68R1 12...Ne5?? cleared a4-d7: 13.Bxd7 won queen for bishop.

## Rule 1b - mate first
- Ask what mates if I pass. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3 luft.
- Back rank: keep a rank-1 blocker or luft; T67R2 36...Rb1+ 37.Rc1 Rxc1#.
- A ROOK TRADE ON MY FIRST RANK LETS HIS QUEEN ARRIVE WITH CHECK AND EAT THE BLOCKERS. T67R5.1 34...Bf6?? 35.Rxc8+ Rxc8 36.Qxc8+ Bd8 37.Qxd8+ Be8 38.Qxe8#; 34...Rxc7 was the move.
- KING-TAKES: an unguarded piece beside his king is a king capture.
- WON POSITION: a forcing check beats a slow lift; Q+R protected checks drive to the edge; Q vs K knight's-move box; check stalemate before promoting.
- TWO QUEENS + ROOK v bare king: one queen cuts, the other checks, bring the king; 5-10 s a move (T68R1 flag).
- PROTECTED-QUEEN FINISH: his king g8/h8 and my bishop g7 guarded: Qf6+ Ke8 Qf8#; Bxh6 works when it hits a pinned g7 (T69R2).

## Rule 2 - queen
- QUEEN NEVER ON AN ENEMY PAWN'S CAPTURE SQUARE, A BISHOP DIAGONAL OR A KNIGHT JUMP SQUARE. T69R2 19...Qd6?? on my Nf5's square, 20.Nxd6. T67R5.1 20...Qd4?? (ghost).
- QUEEN ON THE LONG DIAGONAL FACING HIS QUEEN/BISHOP IS GIFT. T66R4.2 31.Qf4?? Qxf4.
- TWO QUEENS ON A FILE/RANK WITH MY PIECE BETWEEN: that piece is FROZEN - its 'trading' capture loses my queen.
- HIT -> she moves that move, off every attacker ray. QUEEN HIT BY A ROOK ALONG FILE/RANK MUST LEAVE THAT FILE AND RANK, landing square's guards checked. T69R3 27...Qd6?? 28.Rd5, 28...Qd7?? stayed: 29.Qxd7#.
- EVEN A CHECK PASSES THE ROOK-LINE SWEEP. T66R3 26...Qg5+?? 27.Rxg5+.
- PAWN-SQUARE LEAK BOTH WAYS: list enemy pawns on ranks 3-6, both forward capture squares, and the recapturer.
- QUEEN RECAPTURE: walk every enemy attacker of the landing square.
- UP A QUEEN: no queen move onto a bishop diagonal or pawn square; force the last rook trade or mate.
- After ...Qb6 and ...c5 the queen belongs on b6/c7; Qb5/ Qb4/Qa5 let c4/b4 hit her with tempo (T67R4.2).

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach the destination in one move and stay guarded after landing.
- UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. Never trade R for B/P. After a capture that wins a piece rescan my loose units; after any trade recount all guards.
- HIS PAWN SAC IS A LINE OPENER. T69R4 13.b4! (+3.6) offered a pawn to open the a6-c8 diagonal and the b-file against my king on c8; 13...Bxb4 14.Bg5 Be7 15.Rab1 Bxg5 16.Qa6+ put his queen on my 7th, and after Kd7,Rb7! Qxb7 Qxb7+ the c6-pawn fell to Nxc6, Qc8+ drove my bishop to d8, Nc5 forced ...f6 and Nxe6 was mate.
- After long castling behind a doubled c6-pawn his b4-b5 hits the pawn that shields my king: answer with ...b5/...a5/...Kb8/...Rc8, never grab the pawn, and never trade the dark bishop that covers my king.
- After such a trade walk the 7th-rank entry squares; a rook landing there with my king on e8/c8 is usually decisive.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level or behind. Level material with a broken king is lost vs SF.
- DOWN A PIECE/QUEEN VS SF: 5-10 s defensive moves, every unit guarded, first rank solid, keep the king's pawn cover (T69R4 down Q for R, m23 mate).
- DOWN Q FOR R: 2N v R+pawns is NOT a fortress - his rook and king pick the knights (T67R3).
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, consolidate, keep units off his pawn squares.
- UP A QUEEN+ IS A MATE CLOCK: after each capture recount, then the first forcing check/ladder; 5-10 s, cap 20 (T68R1 flagged up two queens).
- UP TWO ROOKS / UP A ROOK: ladder cut/check/tighten 5-10 s; progress test after every move.
- AFTER A QUEEN TRADE RECOUNT: if the recapture chain loses a queen, don't start it.

## Openings
- Caro Advance B (play): 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7. Then take d4, bishop c5/b6, knight e7, castle; c6 guards d5. T69R4: book level to 12...O-O-O, then 13.b4! - see Rule 3; 21...f6 left e6 unguarded, 23.Nxe6#. Never open the a8-h1 diagonal or the c-file with my king on c8/d8 (T69R3 19...c5? 21.Qa8+).
- Caro Classical 3.Nc3 B: ...dxe4, ...Bf5; meet h4-h5 with ...h6 and ...Bh7; then ...e6, ...Nf6, ...Be7, O-O, ...Nbd7, ...Qc7, ...c5. 17...e5?? kicked a defended Nd4; 19...Bxe3?? cleared the c-file to Qc7. Keep the queen on b6/c7, not b5/b4/a5.
- English as Black (reversed QGD, play): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3. Then ...Bf5/...Nbd7/...Qb6/...Re8; ...c5 only when d5 has a PIECE guard. BANS: knight on the e4-pawn's d5/f5, queen on d7 or on the c6-pawn. T66R5.2 12.Ne4?? dxe4! won a knight.
- Ruy Lopez as White, Classical 5...Bc5 (play): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3. Then ...Be6, d4 exd4 cxd4, ...Bb6, Nc3; Bg5 h6 Bxf6 Qxf6; Nd5 Qe6, Nxb6 cxb6, d5! forks Qe6/Nc6. T68R1 12...Ne5?? vacated c6, 13.Bxd7 won queen for bishop; convert 5-10 s, not 10-min plans.
- Ruy quiet 4.d3 W (worked v GLM T69R2): ...Bd6, O-O, c3, ...Re8, Nbd2, h3, Re1, ...Bf8; then Bc4, Nf1-g3; avoid Bg5. Nf5 hits Bd6/g7. Finisher: Bxh6 with g7 pinned, Qf6+/Qf8#. Convert 5-10 s.
- Italian Giuoco Pianissimo W: ...Nc6, ...Bc5, ...Nf6, ...d6, O-O, ...Be6, ...h6; then ...Qd7, ...Re8, ...d5. If ...Bg4, Re1 and h3. Bans: 10.d4?!, queen on d5 while the f6-knight lives.
- Open Sicilian Taimanov W (play): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O. Then f4, Qd2, Rad1, Kh1; e5 hits Nf6; after ...Nd5 Nxd5 exd5 Bf3! hits d5/Nc6 (T66R3 won a piece). e5 only while the e5-pawn is defended after fxe5.
- Open Sicilian Taimanov B: ...Nxc6/...bxc6 with ...Bd3... no - with Bd3 and Be7, e5-clamp answered only by ...Nd5 and ...Bf8. With my king on e8 g7 has NO guard: never ...d6, never castle, never ...Nf6 while e5 stands; cover g7 with a PIECE (...Bf8). T50R3 11...g6?? 15.Qf6 won h8.
- Dragon/Yugoslav W: the Yugoslav build vs SF is LOSING. Prefer Be2/Be3/f4 Taimanov or 5.c4 Maroczy.
- Maroczy Bind W: c4, Nc3, Be2, Be3, Qd2, Rfd1; watch ...Ng4, ...f5, ...Qa5. 29.Bb6?? axb6; 36...Rb1+ 37.Rc1 Rxc1# with no h3. Never a rook on c4/d4/e4 where a d/e/f-pawn captures; h3 before the queen trade.

## Opponents
- SF19: instant, zero errors. Punishes loose units, passive retreats, queens on rays/pawn diagonals/knight squares, ignored attacked pieces, and PAWN SACS that open lines to my king (T69R4 13.b4!). T69R3: level to 9...Qc7, then ...Nh6?? Bxh6 and ...c5 opened a8/e6. Give no pawn break, no loose unit, no piece on e5's f6/d6 or g4's f5/h5; 10-15 s; first rank solid.
- Muse Spark 1.3: patient 30-90 s, zero illegal, banks clock; takes every loose pawn and undefended piece, converts queen-up cleanly. Do not gift b4/a4/h3 or a queen on her diagonal; do not spend 5+ min quiet while she banks time.
- GLM 5.3 Flash: HIS QUEEN ON MY PAWN'S OR KNIGHT'S CAPTURE SQUARE (five+ times: T69R2 ...Qd6?? 20.Nxd6; T68R1 11...Qd7 12.d5!). 1-5 illegal tries. Take gifts only AFTER the pawn/bishop capture list, then convert 5-15 s.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded, punishes a piece/queen on his pawn's capture square and a queen on a rook file. Convert with a named plan.
- Fable 5.1, Sonnet 5.5, GPT-6.1 Sol, Astra: take every unguarded unit, punish loose queen/rook; keep every unit guarded and bank clock. Haiku 5.5: solid Italian Pianissimo, fast; my clock losses there were self-inflicted.
