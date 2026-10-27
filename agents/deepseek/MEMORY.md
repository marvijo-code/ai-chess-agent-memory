# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance + Classical 3.Nc3 B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W (Classical + quiet 4.d3 + Four Knights 4...a6)
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W (SF ...g6/...d5)
- notes/sicilian-soltis-black.md - Soltis B
- tools/material-clock.py - material, clock, loose-unit readout before each move
- tools/repetition-guard.py - warns when a move repeats the position while material is up

## Rule 0 - board, legality, clock
- BOARD MAP FROM HIS LAST MOVE BEFORE ANY CAPTURE OR QUEEN MOVE; a piece that moved is not on its old square. T67R5.1 20...Qd4?? on a ghost board - the d4-knight had gone to c6 - and 21.Nxd4 won my QUEEN.
- LEGALITY: walk the piece, its ACTUAL square, the occupant, every path square, MY own blockers. A PINNED PAWN CANNOT RECAPTURE: T71R1 tried cxd4 to 12...Nxd4 while the c3-pawn was pinned on the a5-e1 diagonal (1 illegal try). 3 rejected tries in a game = forfeit (T71R1 had 3, one on a 'forced' king move). After ONE rejection pick a DIFFERENT piece AND idea.
- TWO-STEP PAWN PUSH: the intermediate square must be EMPTY. T71R2 25...b5 blocked by my own Nb6 on b6; 27...c5 blocked by my own c6-pawn: 4 invalid tries that game. Check own pieces on the path before every two-step push.
- HIS last move first, then my destination: 0 guards + his capture = gift. Quiets and retreats get the same sweep.
- CLOCK: routine 10-15 s, cap 30; never over 60 after move 20. T71R1 v SF spent 5:21, 6:15, 4:46, 6:01 and 8:28 on five quiet queen/bishop moves - none found a defence and the 8:28 move (22.Bd5??) was the losing blunder; 3 min left at move 30. T69R4 the same pattern. The sweep is the spend, not the narrative.

## Rule 1 - destination sweep
- LIST HIS PAWN CAPTURES VS EVERY LANDING, KNIGHTS INCLUDED. White e5-pawn owns f6/d6; g4-pawn f5/h5. T66R2 16...Nf5?? gxf5.
- AN ATTACK IS NOT A DEFENCE. T71R1 22.Bd5?? attacked his e6-bishop and NOTHING of mine could recapture on d5 (queen on f6, rooks on rank 1): ...Bxd5 won a clean piece, +0.2 -> +5.1. Before hitting a minor with a minor, name MY recapture on that square; if there is none, it is a gift.
- MY OWN PIECE ON A LINE IS MY ONLY SCREEN; moving it exposes. T67R3 19...Bxe3?? 20.Qxc7; T68R2 the d5-pawn screened Qd7 from Rfd1.
- TWO LOOSE UNITS IN A ROW THROW A WON OPENING. Every developing move: list my undefended pieces and his queen/rook/bishop reaching them in one.
- HITTING HIS QUEEN IS NOT AN ANSWER WHEN IT OPENS A CHECK.
- A PAWN THAT LEAVES ABANDONS ITS POST: never ...f6 with my king on e8/f8 and e6 unguarded (T69R4 23.Nxe6#). QGD c6 guards d5: ...c5 only with a piece guard on d5.
- NEVER KNIGHT ON A SQUARE HIS PIECE/PAWN COVERS: d5-knight retreats b4/e7/b6/c7, never f6 while e5 lives, never f5 while g4 lives, never h6 while his dark bishop lives (T69R3 13.Bxh6).
- DON'T KICK A DEFENDED CENTRAL KNIGHT WITH A PAWN (T67R3 17...e5?? 18.Ndf5 with tempo).
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5.
- ROOKS/KNIGHTS only where guarded; the mover abandons its guard - name it. An attacked piece needs an answer before any quiet move.
- HIS KNIGHT LEAVING c6 CAN OPEN A BISHOP DIAGONAL TO HIS QUEEN (T68R1 13.Bxd7 won queen for bishop).

## Rule 1b - mate first
- Ask what mates if I pass. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3 luft.
- Back rank: keep a rank-1 blocker or luft; T67R2 36...Rb1+ 37.Rc1 Rxc1#.
- A ROOK TRADE ON MY FIRST RANK LETS HIS QUEEN ARRIVE WITH CHECK AND EAT THE BLOCKERS (T67R5.1 34...Bf6??).
- KING-TAKES: an unguarded piece beside his king is a king capture.
- WON POSITION: a forcing check beats a slow lift; Q+R protected checks drive to the edge; check stalemate before promoting.
- TWO QUEENS + ROOK v bare king: one queen cuts, the other checks, bring the king; 5-10 s a move (T68R1 flag).
- PROTECTED-QUEEN FINISH: his king g8/h8 and my bishop g7 guarded: Qf6+ Ke8 Qf8#; Bxh6 works when it hits a pinned g7 (T69R2).

## Rule 2 - queen
- QUEEN NEVER ON AN ENEMY PAWN'S CAPTURE SQUARE, A BISHOP DIAGONAL OR A KNIGHT JUMP SQUARE. T69R2 19...Qd6?? on my Nf5's square, 20.Nxd6.
- QUEEN ON THE LONG DIAGONAL FACING HIS QUEEN/BISHOP IS GIFT (T66R4.2 31.Qf4?? Qxf4).
- TWO QUEENS ON A FILE/RANK WITH MY PIECE BETWEEN: that piece is FROZEN - its 'trading' capture loses my queen.
- HIT -> she moves that move, off every attacker ray. HIT BY A ROOK ALONG FILE/RANK SHE LEAVES BOTH (T69R3 27...Qd6?? 28.Rd5; 28...Qd7?? 29.Qxd7#).
- EVEN A CHECK PASSES THE ROOK-LINE SWEEP (T66R3 26...Qg5+?? 27.Rxg5+).
- PAWN-SQUARE LEAK BOTH WAYS: list enemy pawns on ranks 3-6, both forward capture squares, and the recapturer.
- QUEEN RECAPTURE: walk every enemy attacker of the landing square.
- UP A QUEEN: no queen move onto a bishop diagonal or pawn square; force the last rook trade or mate.
- WANDERING QUEEN GRABS: two wing pawns are not worth letting his rook and bishop get active (T71R1 four queen moves for b7/a4 cost 22 min and gave ...Rb4-...Rxb2 with tempo; she then had no safe home).

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach the destination in one move and stay guarded after landing.
- UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. Never trade R for B/P. After a capture that wins a piece rescan my loose units; after any trade recount all guards.
- HIS PAWN SAC IS A LINE OPENER. T69R4 13.b4! offered a pawn to open the a6-c8 diagonal and the b-file against my king on c8; taking it lost.
- After long castling behind a doubled c6-pawn his b4-b5 hits the pawn that shields my king: answer with ...b5/...a5/...Kb8/...Rc8, never grab the pawn, never trade the dark bishop that covers my king.
- After such a trade walk the 7th-rank entry squares; a rook landing there with my king on e8/c8 is usually decisive.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level or behind. Level material with a broken king is lost vs SF.
- DOWN A PIECE/QUEEN VS SF: 5-10 s defensive moves, every unit guarded, first rank solid, keep the king's pawn cover (T69R4; T71R1 m32).
- DOWN Q FOR R: 2N v R+pawns is NOT a fortress (T67R3).
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, consolidate, keep units off his pawn squares. T71R2 up B for P but 24...Nd5 5:38, 25...b5 9:28, 27...c5 8:11 -> 1:24 vs 16:36 and threefold. Trade pieces not pawns; do not let his rook shuffles draw you into repetition. T71R3 up a pawn: 22.Qc2 11:25 and four 4-min thinks (Rb1/Nxa4/c4/Nf5) produced queen shuffles Qa6/Qb5/Qc6/Qb7 and threefold; name one conversion (Rc1, d5-d6, trade a piece with recapture, king walk), never offer queen trades by repetition - GLM declines them when down.
- UP A QUEEN+ IS A MATE CLOCK: after each capture recount, then the first forcing check/ladder; 5-10 s, cap 20.
- UP TWO ROOKS / UP A ROOK: ladder cut/check/tighten 5-10 s.
- AFTER A QUEEN TRADE RECOUNT: if the recapture chain loses a queen, don't start it.

## Openings
- Caro Advance B (play): 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies). Then take d4, bishop to c5/b6, knight e7, castle; c6 guards d5. T69R4: book level to 12...O-O-O, then 13.b4! - with my king on c8 never grab a wing pawn that opens a file or diagonal; 21...f6 left e6 unguarded and 23.Nxe6 was mate.
- Caro Classical 3.Nc3 B: play ...dxe4 and ...Bf5; meet h4-h5 with ...h6 and ...Bh7. Then develop ...e6, ...Nf6, ...Be7, O-O. Later ...Nbd7, ...Qc7 and only then ...c5. 17...e5?? kicked a defended Nd4; 19...Bxe3?? cleared the c-file to Qc7. Keep the queen on b6/c7, never b5/b4/a5. T71R2: 17...e4! won B for P, but four invalid tries and long thinks on ...b5/...c5 left 1:24 and a threefold; convert at 5-10 s.
- English as Black (reversed QGD, play): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies). Then ...Bf5, ...Nbd7, ...Qb6, ...Re8; ...c5 only when d5 has a PIECE guard. BANS: knight on the e4-pawn's d5/f5, queen on d7 or on the c6-pawn. T66R5.2 12.Ne4?? dxe4! won a knight.
- Ruy Lopez W, Classical 5...Bc5 (play): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15 plies). Then ...Be6 and d4. After exd4 cxd4, ...Bb6 and Nc3. Later Bg5 with ...h6 answered by Bxf6 ...Qxf6, then Nd5. The d5! push forks Qe6/Nc6. T68R1 12...Ne5?? vacated c6 and 13.Bxd7 won queen for bishop.
- Ruy quiet 4.d3 W (worked v GLM T69R2): ...Bd6, O-O, c3, ...Re8; then Nbd2, h3, Re1, ...Bf8. Later Bc4 and Nf1-g3; avoid Bg5. Nf5 hits Bd6/g7. Finisher: Bxh6 with g7 pinned, Qf6+/Qf8#. Convert 5-10 s.
- Ruy Four Knights/Spanish 4...a6 W (play): 1.e4 e5 2.Nf3 Nf6 3.Nc3 Nc6 4.Bb5 a6 5.Ba4 b5 6.Bb3 Be7 7.O-O O-O 8.d3 d6 (16 plies). Then Be3, Qd2, Rad1, h3, d4; keep e4 guarded, no Nd5 while ...Bb7 stands. T71R3: level after ...Ne5/Bd5 trades, then up a pawn I shuffled the queen into threefold. Convert 5-15 s.
- Italian Giuoco Pianissimo W: ...Nc6, ...Bc5 and ...Nf6; ...d6, castle, ...Be6, ...h6. Then ...Qd7, ...Re8, ...d5. If ...Bg4, Re1 and h3. Bans: 10.d4?!, queen on d5 while the f6-knight lives.
- Open Sicilian Taimanov W (play): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies). Then f4, Qd2, Rad1, Kh1; e5 hits Nf6; after ...Nd5 Nxd5 exd5 Bf3! hits d5/Nc6 (T66R3 won a piece). e5 only while the e5-pawn is defended after fxe5.
- Accelerated Dragon W (T71R1 v SF, 0-1 m32): SF answered 1.e4 with ...c5, ...Nc6, ...g6, ...d5. Level to move 21: after ...d5 exd5 Nxd5 Nxd5 Qxd5 Bf3 (6 plies) his ...Qa5+ is met by c3, and ...Nxd4 by Bxd4 because the c3-pawn is PINNED. Then ...Rd8 freezes Bd4 against Qd1 (Qe2 frees it) and ...Bxd4 cxd4 Rxd4 gives e7 back. From there my queen wandered (17.Qxb7, 19.Qe7, 20.a4, 21.Qf6 - four queen moves, 22 min), his rook went Rb4-b2, and 22.Bd5?? - a bishop attack with NO recapture - lost a piece to ...Bxd5. Play the Taimanov build against ...Nc6/...g6; no wing-pawn grabs while his rook and bishop are unopposed.
- Open Sicilian Taimanov B: ...Nxc6/...bxc6 with Bd3 and Be7. The e5-clamp is answered only by ...Nd5 and ...Bf8. With my king on e8 g7 has NO guard: never ...d6, never castle, never ...Nf6 while e5 stands; cover g7 with a PIECE (...Bf8). After ...Bf8, no ...g6 and no ...h5 (T50R3 15.Qf6 won the h8-rook).
- Dragon/Yugoslav B: 13.Qxd5 -> 13...Qc7 ONLY and keep queens (14...Qxc5? lets Bxc5 use the clear c5-e7-f8 line). Never move the last screen on a rank/file; walk every bishop diagonal to its edge before a rook swing.
- Maroczy Bind W: build c4, Nc3, Be2, Be3; then Qd2 and Rfd1. Watch ...Ng4, ...f5 and ...Qa5. 29.Bb6?? axb6; 36...Rb1+ 37.Rc1 Rxc1# with no h3. Never a rook on c4/d4/e4 where a d/e/f-pawn captures; h3 before the queen trade.

## Opponents
- SF19: instant, zero errors. Punishes loose units, passive retreats, queens on rays/pawn diagonals/knight squares, ignored attacked pieces, pawn sacs that open lines to my king (T69R4 13.b4!), and a piece attack with no recapture (T71R1 22.Bd5??). As Black v 1.e4 it alternates Caro and Accelerated Dragon (...Nc6, ...g6, ...d5, ...Qa5+, ...Rd8/...Rc8, ...Be6). 10-15 s; first rank solid; no queen raids for wing pawns.
- Muse Spark 1.3: patient 30-90 s, zero illegal, banks clock; takes every loose pawn and undefended piece. T71R2 drew while I was up a piece: she had 16:36 left, I had 1:24 after long ...b5/...c5 thinks, then rook/queen shuffles and threefold. Do not gift b4/a4/h3 or a queen on her diagonal; when up, 5-10 s and no repetition.
- GLM 5.3 Flash: HIS QUEEN ON MY PAWN'S OR KNIGHT'S CAPTURE SQUARE (five+ times: T69R2 ...Qd6?? 20.Nxd6). 1-5 illegal tries. Take gifts only AFTER the pawn/bishop capture list, then convert 5-15 s. T71R3: declines queen trades when a pawn down; do not offer by repetition - name a conversion.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded, punishes a piece/queen on his pawn's capture square and a queen on a rook file. Convert with a named plan.
- Fable 5.1, Sonnet 5.5, GPT-6.1 Sol, Astra: take every unguarded unit, punish loose queen/rook; keep every unit guarded and bank clock. Haiku 5.5: solid Italian Pianissimo, fast; my clock losses there were self-inflicted.
