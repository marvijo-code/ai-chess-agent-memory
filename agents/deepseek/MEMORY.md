# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance + Classical 3.Nc3 B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W (Classical + quiet 4.d3 + Four Knights 4...a6)
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
- tools/material-clock.py, clock-guard.py, repetition-guard.py, legal-list.py, fork-alert.py, queen-rook-safety.py - run before every move

## Rule 0 - board, legality, clock
- CLOCK IS MY #1 KILLER: T73R3 lost on time 0:55 vs 42:31 in a level/down-pawn rook ending after 4:29/3:09/4:22/3:23 thinks on quiet rook/queen shuffles. LEVEL OR WORSE AFTER MOVE 25: cap 15 s (8 s after move 40), pick ONE fortress plan and repeat it. Count minutes left vs moves left every move.
- INVALID TRIES COME AFTER HIS CAPTURES AND AFTER MY LONG THINKS: T72R5 four, T72S2G1 four, T72R3 five, T73R3 one (O-O illegal with Bf8+Ng8 unmoved). Rebuild squares from the FEN after EVERY his move; check the UCI with tools/legal-list.py. 3 tries on one move = forfeit. After ONE rejection pick a DIFFERENT piece AND idea.
- BOARD MAP FROM HIS LAST MOVE BEFORE ANY CAPTURE OR QUEEN MOVE; a piece that moved is not on its old square. T67R5.1 20...Qd4?? on a ghost board - the d4-knight had gone to c6 - 21.Nxd4 won my QUEEN.
- LEGALITY: walk the piece, its ACTUAL square, occupant, every path square, MY own blockers; a pinned pawn cannot recapture. Forced king reply: list legal flights once, then send. Two-step push: intermediate square empty.
- HIS last move first, then my destination: 0 guards + his capture = gift. Quiets and retreats get the same sweep.
- ONE MINOR MUST NOT MAKE FOUR MOVES: T72R3 13.Bf4-16.Bd4 bishop shuffles answered his knight dance and cost 8 min. When a piece is kicked, develop ANOTHER piece or trade it.

## Rule 1 - destination sweep
- AN ATTACKED PIECE IS THE MOVE: his knight/pawn lands hitting one of my pieces and nothing of mine recaptures there -> THAT piece moves now. T72R5 12.Ng3 hit my f5-bishop; 12...Bf8?? in 2:47 and 13.Nxf5 exf5 = -3, mate in 13. Free: ...Bg6/...Bd7/...g6.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, KNIGHTS INCLUDED. White e5-pawn owns f6/d6; g4-pawn f5/h5. T66R2 16...Nf5?? gxf5.
- AN ATTACK IS NOT A DEFENCE. T71R1 22.Bd5?? attacked his e6-bishop and NOTHING could recapture on d5: ...Bxd5 won a clean piece.
- MY OWN PIECE ON A LINE IS MY ONLY SCREEN; moving it exposes. T67R3 19...Bxe3?? 20.Qxc7; T68R2 the d5-pawn screened Qd7 from Rfd1.
- TWO LOOSE UNITS IN A ROW THROW A WON OPENING. Every developing move: list my undefended pieces and his queen/rook/bishop reaching them in one.
- HITTING HIS QUEEN IS NOT AN ANSWER WHEN IT OPENS A CHECK.
- A PAWN THAT LEAVES ABANDONS ITS POST: never ...f6 with my king on e8/f8 and e6 unguarded (T69R4 23.Nxe6#). QGD c6 guards d5: ...c5 only with a piece guard on d5. Caro: ...f6 only if ...g6/...gxf6 can hold f5 and e6 has a piece guard.
- NEVER KNIGHT ON A SQUARE HIS PIECE/PAWN COVERS: d5-knight retreats b4/e7/b6/c7, never f6 while e5 lives, never f5 while g4 lives, never h6 while his dark bishop lives (T69R3 13.Bxh6). NO BISHOP/QUEEN WHERE HIS KNIGHT FORKS IT WITH ANOTHER UNIT: T72R2 18...Bf3?? 19.Nd4 fork Qc6+Bf3.
- DON'T KICK A DEFENDED CENTRAL KNIGHT WITH A PAWN (T67R3 17...e5?? 18.Ndf5).
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5.
- ROOKS/KNIGHTS only where guarded; the mover abandons its guard - name it.
- HIS KNIGHT LEAVING c6 CAN OPEN A BISHOP DIAGONAL TO HIS QUEEN (T68R1 13.Bxd7 won queen for bishop).

## Rule 1b - mate first
- Ask what mates if I pass. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3 luft.
- Back rank: keep a rank-1 blocker or luft; T67R2 36...Rb1+ 37.Rc1 Rxc1#.
- A ROOK TRADE ON MY FIRST RANK LETS HIS QUEEN ARRIVE WITH CHECK AND EAT THE BLOCKERS (T67R5.1 34...Bf6??).
- KING-TAKES: an unguarded piece beside his king is a king capture.
- WON POSITION: a forcing check beats a slow lift; Q+R protected checks drive to the edge; check stalemate before promoting. TWO QUEENS + ROOK v bare king: one queen cuts, the other checks, bring the king; 5-10 s a move (T68R1 flag).
- PROTECTED-QUEEN FINISH: his king g8/h8 and my bishop g7 guarded: Qf6+ Ke8 Qf8#; Bxh6 works when it hits a pinned g7 (T69R2).

## Rule 2 - queen
- QUEEN NEVER ON AN ENEMY PAWN'S CAPTURE SQUARE, A BISHOP DIAGONAL OR A KNIGHT JUMP SQUARE. T69R2 19...Qd6?? on my Nf5's square, 20.Nxd6.
- A KNIGHT JUMP THAT COMES WITH CHECK KILLS HER: with my king on d8/d7/e8 a knight reaching c5 forks b7+ and a5/b6. T72R5 17...Qa5; 19.Nc5 20.Nb7+ won my queen with check. Every queen move: list the knight jumps that hit her AND the check on my king.
- QUEEN ON THE LONG DIAGONAL FACING HIS QUEEN/BISHOP IS GIFT (T66R4.2 31.Qf4?? Qxf4).
- A QUEEN ON e2/d2/d3 IN FRONT OF HIS KNIGHTS: ...Ne5/...Nf4 hits her with tempo (T72R3 10.Qe2??). Before a queen move list every knight jump onto her square and what she stops guarding.
- TWO QUEENS ON A FILE/RANK WITH MY PIECE BETWEEN: that piece is FROZEN - its 'trading' capture loses my queen.
- HIT -> she moves that move, off every attacker ray. HIT BY A ROOK ALONG FILE/RANK SHE LEAVES BOTH (T69R3 27...Qd6?? 28.Rd5; 28...Qd7?? 29.Qxd7#).
- EVEN A CHECK PASSES THE ROOK-LINE SWEEP (T66R3 26...Qg5+?? 27.Rxg5+).
- PAWN-SQUARE LEAK BOTH WAYS: list enemy pawns on ranks 3-6, both forward capture squares, and the recapturer.
- QUEEN RECAPTURE: walk every enemy attacker of the landing square.
- UP A QUEEN: no queen move onto a bishop diagonal or pawn square; force the last rook trade or mate.
- WANDERING QUEEN GRABS: two wing pawns are not worth letting his rook and bishop get active (T71R1 four queen moves for b7/a4 cost 22 min). T73R3 Qb6-Qa7-Qc7-Qd7-Qb6-Qa5 on the 5th-7th move of a quiet plan cost 10+ min and the game.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach the destination in one move and stay guarded after landing.
- UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. Never trade R for B/P. After a capture that wins a piece rescan my loose units; after any trade recount all guards.
- HIS PAWN SAC IS A LINE OPENER. T69R4 13.b4! offered a pawn to open the a6-c8 diagonal and the b-file against my king on c8; taking it lost.
- After long castling behind a doubled c6-pawn his b4-b5 hits the pawn that shields my king: answer with ...b5/...a5/...Kb8/...Rc8, never grab the pawn, never trade the dark bishop that covers my king.
- After such a trade walk the 7th-rank entry squares; a rook landing there with my king on e8/c8 is usually decisive.
- A BLOCKADED FORTRESS IS NOT CONVERTED BY REPETITION: T72R1 up a knight with my d6-pawn frozen by Bd7 looped Ne7/Nf5 for 30 moves. Name an opening file (g4/h4 or b4/a4) and use the king; do not repeat when up.
- A ROOK THAT BLOCKS IS A ROOK THAT STAYS: T73R3 Rc4 blocked c3-c4 and held d5; moving it to c6/f5 five times lost the bind and the clock. Name the blockade duty before moving a rook.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level or behind. Level material with a broken king is lost vs SF.
- DOWN A PIECE/QUEEN VS SF: 5-10 s defensive moves, every unit guarded, first rank solid, keep the king's pawn cover (T69R4; T71R1 m32). T72R2 down a piece: Rf8+Rc7 covering f7 twice, Be7-d8-b6, no ...f6/...Rxc3, threefold m31 - repetition is a real result. T72R5 down Q for N at m21: kept every unit guarded, ...a6/...Bg7, mate came only m26.
- DOWN Q FOR R: 2N v R+pawns is NOT a fortress (T67R3).
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, consolidate, keep units off his pawn squares, trade pieces not pawns. T71R2 up B for P: 5-9 min thinks -> 1:24 vs 16:36 and threefold. T71R3 up a pawn: 22.Qc2 11:25 and four 4-min thinks produced queen shuffles and threefold; name ONE conversion, never offer queen trades by repetition.
- UP A QUEEN+ IS A MATE CLOCK: after each capture recount, then the first forcing check/ladder; 5-10 s, cap 20. UP TWO ROOKS / UP A ROOK: ladder cut/check/tighten 5-10 s.
- AFTER A QUEEN TRADE RECOUNT: if the recapture chain loses a queen, don't start it.
- EXTRA PIECE IN A BLOCKED POSITION: first break the blockade plan (open a second front, attack the blockader, trade his last bishop), not a knight tour (T72R1).

## Openings
- Open Sicilian Taimanov W (play): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies). Then f4, Qd2, Rad1, Kh1; e5 hits Nf6; after ...Nd5 Nxd5 exd5 Bf3! hits d5/Nc6 (T66R3 won a piece). e5 only while the e5-pawn is defended after fxe5. AGAINST ...d6 TOO (T72R3 v Muse): play THIS build, never 5.Bb5?!. Also no 11.Rad1/12.d5 when his knight can jump to e5: 12...Ne5! hit my f3-knight and started the bishop shuffle. GLM T73R2 played 2...Nf6/...e6/...a6/...b5/...Bb7/...Be7/...O-O/...Qd7/...Rd7/...Qc6: same build with e5/f4/Bf3; his d-file queen+rook cluster is loose. Pattern: Bxf6! gxf6 Nxf6+ Kg7 Bxc6! (wins the queen) Bxc6 Nxd7 (wins the rook). Up Q+R for B+N, mate in 6. Do not shuffle Qd2/Qe2/Rfd1 for 3-4 min; calculate this tactic at once.
- Caro Advance B (play): 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies). Then take d4, bishop to c5/b6, castle; c6 guards d5. T69R4: 13.b4! - with my king on c8 never grab a wing pawn that opens a file; 21...f6 left e6 unguarded and 23.Nxe6 was mate. T72R2 v SF: ...Qxc6/...Be4/...Bxg2 equalized; 18...Bf3?? allowed the Nd4 fork, then the shell held to threefold. T72R5 v SF: after 9.O-O the f5-BISHOP IS THE WHOLE GAME - 9...Qc7?! (24 s) let 10.Na4 11.b3, 11...f6 (39 s) and 12.Ng3 hit f5; 12...Bf8?? lost it: 13.Nxf5 exf5, Qh5+, mate m26. Move the attacked bishop (...Bg6/...Bd7), then ...Nge7/...O-O; no ...f6 without ...g6 holding f5. T73R3 v Sonnet: 8...Rc8?! wasted a move because O-O was ILLEGAL (Bf8+Ng8) - play ...Nf6 and ...O-O first, or ...cxd4. The ...c4 clamp and ...Qb6 were fine; then ...Qa7/...Qc7/...Qd7/...Qb6 queen wander cost 48 s + 2:05 + 2:14 + 1:43. 16...exf5 was a TRADE (N for B), not a clean piece. With the king still on e8, a ...g5/...h5 hook let hxg6 and gxf7+ Kxf7 ended castling: keep f7 covered before any ...g5.
- Caro Classical 3.Nc3 B: play ...dxe4 and ...Bf5; meet h4-h5 with ...h6 and ...Bh7. Then ...e6, ...Nf6, ...Be7, O-O, ...Nbd7, ...Qc7 and only then ...c5. T71R2: 17...e4! won B for P, but four invalid tries and long thinks on ...b5/...c5 left 1:24 and a threefold. T72S2G1 v Muse: ...c5-c4 clamp, ...Nb6/...Nfd5, ...b4; ...bxc3+ Rxc3 wins N, ...Rxc2+ (Bh7 hits c2), ...Qc3+. 5-10 s; 2-4 min thinks were wasted.
- English as Black (reversed QGD, play): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies). Then ...Bf5, ...Nbd7, ...Qb6, ...Re8; ...c5 only when d5 has a PIECE guard. BANS: knight on the e4-pawn's d5/f5, queen on d7 or on the c6-pawn. T66R5.2 12.Ne4?? dxe4! won a knight.
- Ruy Lopez W, Classical 5...Bc5 (play): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15 plies). Then ...Be6 and d4. After exd4 cxd4, ...Bb6 and Nc3. Later Bg5 with ...h6 answered by Bxf6 ...Qxf6, then Nd5. T68R1 12...Ne5?? vacated c6 and 13.Bxd7 won queen for bishop.
- Ruy quiet 4.d3 W (worked v GLM T69R2): ...Bd6, O-O, c3, ...Re8; then Nbd2, h3, Re1, ...Bf8. Later Bc4 and Nf1-g3; avoid Bg5. Nf5 hits Bd6/g7. Finisher: Bxh6 with g7 pinned, Qf6+/Qf8#. Convert 5-10 s.
- Ruy Four Knights/Spanish 4...a6 W (play): 1.e4 e5 2.Nf3 Nf6 3.Nc3 Nc6 4.Bb5 a6 5.Ba4 b5 6.Bb3 Be7 7.O-O O-O 8.d3 d6 (16 plies). Then Be3, Qd2, Rad1, h3, d4; keep e4 guarded, no Nd5 while ...Bb7 stands. T71R3: level after ...Ne5/Bd5 trades, then up a pawn I shuffled the queen into threefold.
- Ruy 3...a6 4...d5 (T72R1 v GLM, 0-1 time): 5.exd5 b5 6.Bb3 Nd4 7.c3 Nxb3 8.Qxb3 gave me a pawn; his fortress held. Open a second front (g4/h4 or b4) and bring the king; do not repeat.
- Italian Giuoco Pianissimo W: ...Nc6/...Bc5/...Nf6, ...d6, castle, ...Be6, ...h6, ...Qd7/...Re8/...d5; if ...Bg4 Re1/h3. No 10.d4?! or queen on d5 while Nf6 lives.
- Accelerated Dragon W: vs ...c5/...Nc6/...g6/...d5 play the Taimanov build; after ...d5 exd5 Nxd5 Nxd5 Qxd5 Bf3 meet ...Qa5+ with c3, ...Nxd4 with Bxd4 (c3 pinned). No queen wander, no 22.Bd5?? with no recapture (T71R1).
- Open Sicilian Taimanov B: ...Nxc6/...bxc6 with Bd3 and Be7. The e5-clamp is answered only by ...Nd5 and ...Bf8. With my king on e8 g7 has NO guard: never ...d6, never castle, never ...Nf6 while e5 stands; cover g7 with a PIECE (...Bf8). After ...Bf8 no ...g6 and no ...h5 (T50R3 15.Qf6 won the h8-rook).
- Dragon/Yugoslav B: 13.Qxd5 -> 13...Qc7 ONLY and keep queens. Never move the last screen on a rank/file; walk every bishop diagonal to its edge before a rook swing.
- Maroczy Bind W: build c4, Nc3, Be2, Be3; then Qd2 and Rfd1. Watch ...Ng4, ...f5 and ...Qa5. 29.Bb6?? axb6; 36...Rb1+ 37.Rc1 Rxc1# with no h3. Never a rook on c4/d4/e4 where a d/e/f-pawn captures; h3 before the queen trade.

## Opponents
- SF19: instant, zero errors. Punishes loose units, passive retreats, queens on rays/pawn diagonals/knight squares, ignored attacked pieces, pawn sacs that open lines to my king, a piece attack with no recapture, a bishop/queen on a knight-fork square, and a piece his knight attacks that I leave standing. As Black v 1.e4 it plays Caro Advance; it hunts the f5-bishop with Ng3/Nxf5 and plays Qh5+/Bg5 against an uncastled king. 10-15 s; first rank solid; no queen raids for wing pawns. Down a piece a guarded shell can hold to threefold (T72R2).
- Muse Spark 1.3: patient 30 s-4 min, zero illegal, banks clock, takes every loose pawn and undefended piece. T71R2 drew while I was up a piece on my flag. T72R3: Sicilian ...d6/...c5, ...Ne5! hitting f3, grabbed the c3-pawn, then sat in a solid shell and won on MY flag with 8:37 v 1:23. T72S2G1: her clock collapsed after ...bxc3+/...Rxc3, ...Rxc2+, ...Qc3+; she forfeited. Against her the clock is the game: 5-10 s a move, no 7-minute thinks, no queen on her diagonal.
- GLM 5.3 Flash: HIS QUEEN ON MY PAWN'S OR KNIGHT'S CAPTURE SQUARE (five+ times: T69R2 ...Qd6?? 20.Nxd6). 1-7 illegal tries, often 3 on a check reply (T73R2 ...Kg7 and ...Kh8 each took 3). Take gifts only AFTER the pawn/bishop capture list, then convert 5-15 s. T71R3: declines queen trades when a pawn down; name a conversion. T72R1: down a knight he built an a5/b5/c6/e5 fortress with Bd7 blockading d6; I won only on his flag. T73R2: his ...Qd7/...Rd7/...Qc6 d-file cluster loses to a check on f6 plus Bxc6 hitting the queen; keep giving forcing checks.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded, punishes a piece/queen on his pawn's capture square and a queen on a rook file. Convert with a named plan.
- Sonnet 5.5: T73R3 took 40+ min of clock, zero illegal, punishes a loose queen/rook and every pawn grab; in a level ending he shuffles quietly and waits for a flag. Against him bank clock from move 1: 5-10 s book, 10-15 s quiet, never a 3-min think in a level position - he will outlast me on the clock and mate or flag.
- Fable 5.1, GPT-6.1 Sol, Astra: take every unguarded unit, punish loose queen/rook; keep every unit guarded and bank clock. Haiku 5.5: solid Italian Pianissimo, fast; my clock losses there were self-inflicted.
