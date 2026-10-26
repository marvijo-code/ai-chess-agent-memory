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
- BOARD MAP FROM HIS LAST MOVE BEFORE ANY CAPTURE OR QUEEN MOVE. A piece that moved is not on its old square. T67R5.1 20...Qd4?? was played on a ghost board - the d4-knight had gone to c6 at move 19; 21.Nxd4 won my QUEEN and turned -4 into +9.7.
- 3 rejected replies on one move = forfeit. Walk piece, actual square, occupant, path, my own blockers. One rejection = different piece/idea. Castling: king/rook unmoved, f8/g8 empty, king not in check or through attacked square. T68R2 tried O-O with Ng8 still home (4 invalid tries); one rejection = change the move.
- His last move first, then my destination: 0 guards + his capture = gift. Quiets/retreats same sweep.
- CLOCK: routine 10-15 s, cap 30; up material 5-10; under 15 min 5-10; under 5 min 3-5; from move 20 never over 60. vs SF 10-15 routine, lost position 5-10. Long think never replaces the destination list. T67R5.1 burned ~45 min in 38 moves (3:04 ...Qc7, 3:07 ...cxd4, 3:15 ...Bxb3, 3:25 ...Bd4, 7:22 ...Bxh4 = winning a pawn) - book/structure moves are 5-15 s, the sweep is the spend. T66R5.2 up N+pawns wasted 2-5 min quiet. T68R1 up Q for B from m13, +Q+Q+R by m28, then 10:50 on 32.Rd8 and 6:18 on 35.Qd8+ = FLAG at 1:40. With a queen+ lead every move is 5-10 s; forcing checks first, no multi-minute plan. T68R2 down Q for N spent 12:16 on 28...Bg6 - lost position 5-10 s. T69R2 up a queen from m20 still spent 2:33 on 32.Qd6 and 3:06 on 36.Bxh6; won, but 5-10 s was correct.

## Rule 1 - destination sweep
- LIST HIS PAWN CAPTURES VS EVERY LANDING, KNIGHTS INCLUDED. White e5-pawn owns f6/d6; g4-pawn f5/h5. T61R1 25...Nd5?? e4; T66R2 16...Nf5?? gxf5; T62R2 14...Qd6?? exd6.
- MY OWN PIECE ON A LINE IS MY ONLY SCREEN; moving it exposes. T60R2 14.Bxa7?? ...Rxd2; T62R1 12.Bd4??; T67R3 19...Bxe3?? left Qc3 v Qc7 on the c-file, 20.Qxc7 won my queen. T68R2 the d5-pawn was Qd7's screen against Rfd1; 13...d4/14...dxe3 cleared the d-file, 15.Rfd1 hit her, 15...Qb7?? 16.Nd6+ forked Ke8/Qb7.
- TWO LOOSE UNITS IN A ROW THROW A WON OPENING. Every developing move: list my undefended pieces and his queen/rook/bishop reaching them in one.
- HITTING HIS QUEEN IS NOT AN ANSWER WHEN IT OPENS A CHECK.
- A PAWN THAT LEAVES ABANDONS ITS POST. Caro: never ...f6 while king e8/uncastled and e6 has no PIECE guard. QGD c6 guards d5: ...c5 only with a piece guard on d5. Pinned pawn is no guard.
- NEVER KNIGHT ON A SQUARE HIS PIECE/PAWN COVERS: d5-knight retreats b4/e7/b6/c7, never f6 while e5 lives, never f5 while g4 lives.
- DON'T KICK A DEFENDED CENTRAL KNIGHT WITH A PAWN. T67R3 17...e5?? gave 18.Ndf5 with tempo on my e7-bishop.
- POSITIVE PAWN-TAKE: his Ne4, my d5-pawn and Nf6 alive: ...dxe4! dxe4 Nxe4 wins N+P for P when only d3 recaptures. T66R5.2.
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5; g4-pawn hits f5/h5.
- KNIGHT/BISHOP LANDINGS: walk his queen/bishops' diagonals and every knight jump; a central jump needs every recapturer.
- ROOKS/KNIGHTS only where guarded; rook check: can his king just take. The mover abandons its guard - name it. An attacked piece needs an answer before any quiet move.
- A SUPPORTED PAWN BREAK e5 (f4 guarding) FORKS QUEEN AND KNIGHT: move knight or queen first.
- HIS KNIGHT LEAVING c6 CAN OPEN A BISHOP DIAGONAL TO HIS QUEEN: T68R1 12...Ne5?? vacated c6 and cleared a4-d7, 13.Bxd7 won the queen for a bishop. Before any knight move list what diagonal/file it opens to his queen, especially Qd7 behind c6.

## Rule 1b - mate first
- Ask what mates if I pass. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3 luft.
- King g8 + Rf8 + g7 gone: Re8+ ...Rf8 block is Qg7# if his bishop covers g7/h8. Keep the g7-pawn.
- Back rank: keep a rank-1 blocker or luft. T61R1 38.Re8#; T61Final 30.Qa8+ Re8 31.Qxe8#; T66R3 29.Rxd7+ 30.Re8#; T67R2 36...Rb1+ 37.Rc1 Rxc1#.
- A ROOK TRADE ON MY FIRST RANK LETS HIS QUEEN ARRIVE WITH CHECK AND EAT THE BLOCKERS. T67R5.1 34...Bf6?? (attacking Ne5) 35.Rxc8+ Rxc8 36.Qxc8+ Bd8 37.Qxd8+ Be8 38.Qxe8#; 34...Rxc7 was the move. Before any capture/trade on rank 8 walk his queen to every first-rank square.
- KING-TAKES: unguarded piece beside his king is a king capture.
- WON POSITION: a forcing check beats a slow lift; Q+R protected checks drive to the edge; Q vs K knight's-move box, no stalemate (T62R2, T62R3, T62R4.2).
- T66R5.2 finish: up N+pawns, king a3/a2: Qc2 covers a2/a4/b2/b3, c5-pawn b4, ...Nb5#. Check stalemate before c1=Q.
- T67R4.2 finish: up Q+N vs R, king b1/a1: Qc3+ Qe1# with knight on c2.
- TWO QUEENS + ROOK v bare king: one queen cuts, the other checks on the edge, bring king/rook; keep a pawn to avoid stalemate, but 5-10 s a move. Do not spend 10 min 'sealing' a won position (T68R1 flag).
- PROTECTED-QUEEN FINISH: with his king on g8/h8 and my bishop g7 guarded, Qf6+ Ke8 Qf8#; Bxh6 works when it hits a pinned g7 and the queen guards the bishop (T69R2).

## Rule 2 - queen
- QUEEN ON THE LONG DIAGONAL FACING HIS QUEEN/BISHOP IS GIFT. T66R4.2 31.Qf4?? Qxf4.
- QUEEN NEVER ON AN ENEMY PAWN'S CAPTURE SQUARE, A BISHOP DIAGONAL OR A KNIGHT JUMP SQUARE - and re-read his piece list first. T67R5.1 20...Qd4?? c6xd4 (ghost board). T62Final 21...Qb4?? cxb4. T69R2 GLM 19...Qd6?? on my Nf5's capture square, 20.Nxd6.
- TWO QUEENS FACING ON A FILE/RANK WITH MY PIECE BETWEEN: that piece is FROZEN - its 'trading' capture loses my queen (T67R3).
- HIT -> she moves that move, off every attacker ray. A bishop landing with tempo on her = she moves. T68R2 Qd7 hit by Rfd1; Qb7?? walked into Nd6+.
- QUEEN HIT BY A ROOK ALONG FILE/RANK MUST LEAVE THAT FILE/RANK. T61R3 18...Qe4 under Re1; T62R1 12...Rd8 hit Qd2.
- EVEN A CHECK PASSES THE ROOK-LINE SWEEP: T66R3 26...Qg5+?? 27.Rxg5+.
- PAWN-SQUARE LEAK BOTH WAYS: GLM five times; mine T62Final, T67R2 (...Qxb2 safe only because Rb8 backed it). Before every queen move list enemy pawns on ranks 3-6, both forward capture squares, and name the recapturer.
- QUEEN RECAPTURE: walk every enemy attacker of the landing square. T62R4.2 20...Qxd6?? 22.Rxd6.
- UP A QUEEN: no queen move onto a bishop diagonal or pawn square; force the last rook trade or mate. Up a knight, a queen trade on a safe square is good (T66R5.2 14...Qxd4).
- T67R4.2: after ...Qb6 and ...c5 the queen belongs on b6/c7; Qb5??/Qb4?!/Qa5?! let c4/b4 hit her with tempo.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach the destination in one move and stay guarded after landing.
- UNDEFENDED PIECE NOT FREE IF HIS ANSWER COMES WITH TEMPO. Never trade R for B/P. After a capture that wins a piece rescan my loose units; after any trade recount all guards. Up an exchange with queens on: no pawn grabs with the rook, keep both rooks guarded. T66R5.2 traded queens and rooks up a knight and converted.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD EVERY MOVE; rescan after every trade. No grabs when level or behind. Level material with a broken king is lost vs SF.
- DOWN A QUEEN VS SF: no rescue plan - 5-10 s defensive moves, every unit guarded, and keep the first rank solid, the mate usually comes from there (T67R5.1 m38). T68R2 12:16 on ...Bg6 down Q for N = wasted clock.
- DOWN Q FOR R: 2N v R+pawns is NOT a fortress - his rook and king pick the knights one at a time (T67R3). Keep knights guarded and off his king's/rook's approach squares.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, consolidate, keep units off his pawn squares. T61R2, T62R2, T62R4.2, T66R5.2 all wasted minutes up material.
- UP A QUEEN+ IS A MATE CLOCK: after each capture recount, then play the first forcing check/ladder; 5-10 s, cap 20. If no mate in 10 s, repeat a safe check or improve one piece. A long think while up a queen is the only way to lose (T68R1: +Q for B, then +Q+Q+R, flagged).
- UP TWO ROOKS: ladder cut/check/tighten 5-10 s. UP A ROOK (2R v R): a progress problem - extra rook to an open file/7th, offer a defended rook trade, drive his king; progress test after every move.
- DOWN A PIECE VS SF IS LOST: no queen pawn-grabbing, guard every unit, hunt one freeing trade, keep the king behind pawns. Down vs GLM not lost: hit undefended pieces.
- AFTER A QUEEN TRADE RECOUNT: if the recapture chain loses a queen, don't start it.

## Openings
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies); then take d4, bishop c5/b6, knight e7, castle. T66R1 v Muse level. T60F 10...Nf6?? exf6 (the e5-pawn owns f6). T67R5.1 v SF: book level to move 15 (...Qc7, ...cxd4, ...Bg6, ...Ba5); 12...Bb4? and 13...Ne7?! were the first soft moves, but 16...Nf5! 17...Nxe3! 18...Qxe3+! won a pawn - the e7-knight's route to f5 is the plan, keep it; then 20...Qd4?? lost the queen to a ghost board. T68R2 v SF: 12...Qd7 was level; 13...d4? cleared the d-file screen of Qd7, 14.Nb5, 14...dxe3?? 15.Rfd1 hit her, 15...Qb7?? 16.Nd6+ forked Ke8/Qb7. Never ...d4/...dxe3 while his Rfd1 can enter; a hit queen goes to Qe7/Qd8, not b7. Never ...f6 while e6 has no PIECE guard; never recapture ...Bxf5 on an open f-file; ...hxg6 not ...Nxg6.
- Caro Classical 3.Nc3 B (T67R3 L m60; T67R4.2 W m47): trade on e4, develop Bf5; meet h4-h5 with h6 and Bh7; then e6, Nf6, Be7, O-O, later Nbd7, Qc7, c5. T67R3: 17...e5?? kicked a defended Nd4; 19...Bxe3?? cleared the c-file (20.Qxc7). T67R4.2: keep the queen on b6/c7, not on b5/b4/a5. Down Q for R, 2N v R+pawns is lost. Structure moves 5-15 s.
- English as Black (reversed QGD): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies); then ...Bf5/...Nbd7/...Qb6/...Re8. ...c5 only when d5 has a PIECE guard. BANS: no knight on the e4-pawn's d5/f5, no queen on d7 or the c6-pawn, ...Na4?? bxa4, ...Bxa4?? Rxa4, ...Bd6?? Nf5. T66R5.2: 12.Ne4?? dxe4! dxe4 Nxe4 won a knight; 14...Qxd4 traded queens up; ...c5 kicked Nd4; ...Nb5#.
- Ruy Lopez as White, Classical 5...Bc5: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15 plies). Build ...Be6, d4, exd4 cxd4, ...Bb6, Nc3; Bg5 h6 Bxf6 Qxf6; Nd5 Qe6, Nxb6 cxb6, d5! forks Qe6/Nc6. T61S2G1 16...Ne5?? 17.dxe6 won a queen. T62R2 14...Qd6?? on my e5-pawn. T68R1 v GLM: 11...Qd7 12.d5! hit Nc6+Be6; 12...Ne5?? vacated c6, opened a4-d7, 13.Bxd7 won queen for B. Then convert 5-10 s, not 10-min plans. Chigorin 5...Be7: bishop b3, d6, castle, Na5/Bc2; keep the c1-rook, Be3 not Bd2; no piece on the g6-pawn square. Quiet 4.d3 setup worked vs GLM T69R2; details in notes/ruy-lopez-white.md.
- Italian Giuoco Pianissimo W: Nc6, Bc5, Nf6, d6, O-O, Be6, h6 setup; then Qd7, Re8, d5. If ...Bg4, Re1 and h3. T60S2G1 16.Ba4! Qxa4?? 17.Qxa4. Bans: 10.d4?!, queen d5 while the f6-knight lives.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4, Qd2, Rad1, Kh1. e5 hits Nf6; after ...Nd5 Nxd5 exd5 Bf3! hits d5/Nc6. T66R3: 12.e5 Nd5 13.Nxd5 exd5 14.Bf3! won a piece; 19.Bxf6 Bxf6 20.Qxd5+. BUT e5 only while the e5-pawn is DEFENDED after fxe5 (T62R4.2 12.e5?! dxe5 13.fxe5 Nxe5).
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies); then Qg4. With the king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8). T50R3 11...g6?? 15.Qf6 won h8.
- Dragon/Yugoslav W: the Yugoslav build vs SF is LOSING. Prefer Be2/Be3/f4 Taimanov or 5.c4 Maroczy; if Yugoslav is on, move the queen off rook files, no capture while she is hit.
- Maroczy Bind W v SF: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5 7.Nb3 Qd8 8.Be3 (15 plies), then Be2, castle, ...d6, Qd2. T67R2: 11...Ng4!, 13.Nd5 f5; 29.Bb6?? axb6; 34.Rc4?? dxc4; 36...Rb1+ 37.Rc1 Rxc1# with no h3. Never a rook on c4/d4/e4 where a d/e/f-pawn captures; h3 before the queen trade.

## Opponents
- SF19: instant, zero errors. Punishes loose units, passive retreats, queens on rays/pawn diagonals/knight squares, voluntary pawn loosening, ignored attacked pieces. T67R5.1: level through move 15, then one ghost-board queen blunder and one back-rank rook trade = mate m38. Give no pawn break, no loose unit, no piece on the e5-pawn's f6/d6 or the g4-pawn's f5/h5; 10-15 s; keep the first rank solid.
- Muse Spark 1.3: patient 30-90 s, ZERO illegal, banks clock. Takes every loose pawn/undefended piece, converts queen-up cleanly. Caro Advance waits ...Bf5/...Nd7/...Ne7/...Bg6/...Nf5 then hits b4/a4/h3. T67R3 took my queen when the c-file cleared; T67R4.2 played the h4-h5 shell and missed Qxa8?? (Qb4+ Qxc4). Do not gift b4/a4/h3 or a queen on her diagonal; do not spend 5+ min quiet while she banks time.
- GLM 5.3 Flash: as Black v 1.e4 Ruy Classical 5...Bc5 and Taimanov; as White English/reversed QGD. Leaks: HIS QUEEN ON MY PAWN'S OR KNIGHT'S CAPTURE SQUARE (five+ times), ON MY ROOK'S RANK (T66R3 26...Qg5+?? 27.Rxg5+), CENTRAL KNIGHT ON e4 EN PRISE TO ...dxe4 (T66R5.2), T68R1 11...Qd7 met 12.d5! ...Ne5?? 13.Bxd7, and T69R2 19...Qd6?? onto my Nf5's square, 20.Nxd6 won her. Also T69R2 14...Nh4?? hung a knight to Nxh4. 1-5 illegal tries, up to 5 min. Take every gift only AFTER the pawn/bishop capture list, then convert 5-15 s; GLM banks clock, so a won game still needs a clock.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded, punishes a piece/queen on his pawn's capture square. It hangs a queen when a recapture lands on a file an enemy rook controls. Convert with a named plan, 5-10 s once ahead.
- Fable 5.1, Sonnet 5.5, GPT-6.1 Sol, Astra: take every unguarded unit, punish loose queen/rook, no gifts; keep every unit guarded and bank clock. Haiku 5.5: solid Italian Pianissimo, fast; my clock losses there were self-inflicted - 10-15 s, bank time, check legality twice.
