# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B (T80R4, T80R6)
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W incl. 5.d3 (T78R1, T80R3, T80R7)
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W (T79R1 draw, T80R5 loss)
- notes/sicilian-soltis-black.md - Soltis B
- tools: legal-list, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender, knight-exit

## Rule 0 - board, legality, clock
- FORFEIT BEATS BLUNDER: 3 refused tries on ONE move end it. A REFUSAL IS PER MOVE: with a written material line, resend the SAME UCI once (T80R6 Sonnet 24.Bxf6 beat a pin-fork flag: Bxf6 Nxh3+ gxh3 Nxf6 left R+N for B+P and was accepted). Without a written line, change piece AND idea at once. A flagged pawn is not a stop: accept the cheapest loss (T80R3 51...Rb2). Under 10 min every move 3-5 s; never a think over 20 s.
- IN CHECK: run tools/legal-list.py, write every legal reply, send exact UCI in 5-10 s. A KNIGHT CHECK HAS NO BLOCK: only king flights or capture the knight. T80R6 36.Ne7+ (Nf5-e7) on Kg8 had only g8h8/g8f8/g8f7; I burned 3 invalid tries and forfeited. Write K flights first, pick one, send.
- A LOST POSITION EATS TRIES, SO DO NOT REACH ONE: T80R5 was lost by my 12th move and still cost 11 invalid attempts (Bf3, Qd2, Kd1, Bd4 three each). The flood was the symptom; the chess was 12.Qb1?? (Rule 2) and 15.Qxb2 (Rule 1).
- REREAD THE FEN, SEND A PLAINLY LEGAL UCI: T78R2 6 invalid; T78R4 Rf1/Rfe1; T78R7 13...Bf8; T80R3 16.Nb3, 24.Rad1, 26.Ng3, 38.e6, 40.Nexc6; T80R4 17...N5f6; T80R7 22.Bb3, 29.Qd3. A refused quiet keeper becomes a DIFFERENT quiet keeper in one try.
- Clock: routine 5-15 s; capture/check/pawn break 15-25 s; 30+ s only for a named forcing line. Long thinks on quiet keepers find nothing: T78R1 1:15 on Qd4??; T79R1 2-3 min; T79R2 2:58; T79R7 8:51; T80R2 2:05-4:32; T80R3 3:19-11:47; T80R5 3:40 on 9.Nxc6 and 3:25 on 11.Bf3; T80R6 23...Nf4 12:06 and 3 gated tries, 34...Qa6 3:49, 35...N6h5 2:05, finished 14:07 v 50:59; T80R7 8:09 on 20.Qd2, 4:18 on 30.Qc2, 3:31 on 31.Bxf4, finished 32:27 v 36:43. From m15 level/worse cap 20 s; under 5 min 5 s; under 1 min 2 s and copy a legal UCI. A closed Ruy quiet keeper is 5-15 s even when the opponent is slower.
- Tool AVOID is not material: count queen for bishop/rook before obeying; IN CHECK a pawn-loss flag is NOISE - escape check first. Obey queen-loss flags. Legality: actual square, occupant, path, own blockers, pinned pawn, castling flights.
- Material from the board every move, written W x / B y. Name my loose units and his lines to them before any quiet move.

## Rule 1 - destination sweep
- A PAWN BLOCK ON A BISHOP'S DIAGONAL IS NOT A WALL: he can CAPTURE the blocker WITH CHECK. T80R5 14.c3 'blocked' Bg7; 14...Rxb2! 15.Qxb2 Bxc3+ (check, the bishop now hits Qb2) 16.Qd2 Bxd2+ - queen for bishop. Before taking any 'free' unit on a diagonal, walk every enemy bishop line to that square and count MY pawns on it as capturable with tempo.
- RECAPTURE WITH THE PIECE THAT DOES NOT OPEN A LINE: T77R5 31...Qxc3 32.Nxc3?? took Ne2 off b5-f1 and ...Bxf1 won the exchange.
- A GUARD MUST REACH IN ONE MOVE; a pinned guard guards nothing (T77R3 17.Bd5?? Nxd5). An attacked piece gets its retreat list before any quiet move.
- A BISHOP ON THE 7th WITH NO RETREAT IS A TEMPO TARGET: T79R1 15.Bxb7 Rb8 16.Ba6 Rxb2 cost a bishop for a pawn. Name its retreat and his rook lift before a7/b7/c7.
- KING AND PIECE ON ONE RANK FACING HIS ROOK: T77R5 Ra3+Kf3 pinned Bc3.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; every knight jump; every bishop/rook line. PAWN FORK ON A KNIGHT LANDING (T76R4 21...Ne5??).
- AN ATTACK IS NOT A DEFENCE; my own piece on a line is my only screen.
- A KNIGHT ON f5 + MY Kg8 + Nf6 guarding d5: ...Nf6-h5?? allows Ne7+ forking king and d5. Keep f6 or cover d5. T80R6 35...N6h5??.
- A ROOK ON f6 AFTER ...f6/...Rxf6 IS A Bg5 TARGET: move it to f7/f8 or prevent Bg5 before a quiet queen move. T80R6 21...Qb6?? 22.Bg5! Bxd4 23.Nxd4 won the exchange.
- A PAWN PUSH THAT OPENS A FILE: T80R7 26.c4?? let ...bxc4 open the b-file; 27.Bxc4?! then ...Ra8 and ...Nf4. In a closed Ruy keep the c-pawn or play b4 first.

## Rule 1b - mate first
- Ask what mates if I pass; keep a rank-1 blocker or luft; K on c8 with b7 empty is a mating net. T79R2: Kg8 + h7 with his Ng5/Qd3 = Qxh7#; block f5/g6.
- BACK-RANK FINISHER (T78R2 37...Rc1+! 38.Rd1 Rxd1+ 39.Re1 Rxe1#): his king boxed on g1 and a rook that must block on rank 1.
- A ROOK PAIR ON THE 7th + HIS Bg5/Nf7 = NO g-PAWN PUSH: T79SF2G1 40...g6?? 41.Nh6+ Kh8 42.Rh7#.
- EVERY BLOCK IS A PIECE: T80R5 19...Rd8+ 20.Bd5 Rxd5+ 21.Bd4 Rxd4# - when his check can be met only by interposing pieces he takes with check, count the mate net instead of feeding blockers.
- Before trading a light bishop or a quiet queen move, name h7/g7 guards. Level position: no 30+ s think.

## Rule 2 - queen
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. T78R1 33.Qd4?? in front of Rd8 and on e4.
- A QUEEN GUARDING TWO PAWNS ON A ROOK FILE IS A TARGET: T80R5 12.Qb1?? (SF ??) covered b2/c2; 12...Ba6 13...Rb8 hit her and the game went from -0.3 to -5.4. Guard pawns with a rook or a pawn, or offer the trade; her square must be one no rook or bishop reaches next move.
- HIS ROOK ON THE 4th-6th GAINS A TEMPO ON MY QUEEN (T76R4 Qa6??).
- QUEEN RECAPTURE: walk every attacker of the landing; name what she no longer guards (T76R2 30.Qxc1).
- NO QUEEN SHUTTLE WITHOUT A NEW TARGET: T77R6, T77R7, T78R4, T79R1 24.Qe2 (7:17); T80R7 Qd2-d3-d2-d3-c2 over five moves while level, with 8:09 and 4:18 thinks. In a closed Ruy pick b4, Nd4 or a trade, or leave her still. T80R4 up B for 2P I played Qb5-Qd5-Qb5 and drew threefold; a repetition while ahead is MY loss.
- QUEEN+KING KNIGHT FORK: Qd6 + Kg7 with his knight on h4/e5 = ...Nf5+ forking both.

## Rule 3 - captures & trades
- RECOUNT AFTER EVERY EXCHANGE - MY NARRATIVE IS NOT THE BOARD: T80R5 after the ...d5 exchanges I wrote 'clean pawn up, bishop pair' while material was LEVEL and SF had me -1.0. Write W x / B y from the FEN.
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET (T76R4 30...fxe4).
- A rook that blocks stays; a rook his knight hits moves; a rook shuffle needs a target.
- WING PAWN GRAB WITH A KNIGHT: T76SF1G1 37...Nxa5??; keep knights central.
- KNIGHT LANDS WITH NO EXIT = PIECE: T79SF2G1 17...Nb4? Rb1 trapped it. Name its retreats and his coverage.
- KNIGHT TRADES AND LANDINGS: a knight that hits nothing is drift - play the freeing break.

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. Before trading queens count the pawns and diagonals it hands him.
- A TRADE-DOWN AT +1P IS A CONVERSION (T78R2 back-rank mate): name ONE net, never shuffle.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, trade pieces not pawns; a repetition while ahead is MY loss. T80R4 v Muse drew threefold up B for 2P with Qb5-Qd5-Qb5. Activate the extra bishop or play ...a6/...g6.
- DOWN A PIECE OR A PAWN IN A LOCKED CENTRE = THE SHELL: T79R1 (threefold m47), T79R4 (m49) - every unit guarded, rook on the one unattacked square, K h7/g8, free pawns taken, 5-15 s. The shell is the LAST resort: try the freeing break by move 12-15.
- DOWN MATERIAL, A REPETITION IS MY SAVE (T77R3, T77R4). If every legal move loses a pawn, send the least-bad one in ONE try.
- DOWN A PIECE, A FORTRESS NEEDS NO WEAK PAWN: T78SF2G1 ...b5-b4 tied Qd6/Rb5 and set the Nf5+ fork.
- ROOK ENDING DOWN A PAWN (T80R3): the blockade is right, but name his rook's entry squares - ...Rd2-...Rb2 won my loose b3.
- A KNIGHT WITH NO TARGET IS PLAN DRIFT: T78R1 20.Nh4?; T78R4 16.Nc5??; T79R1 12.Nde2-14.Nd4; T80R3 26.Ng3?? 28.Rd3?? 29.a5?? 37.N5d4??. Pick ONE target or go to the ending.
- A CLEAN WIN = one plan, guarded units, fast safe moves. A level game against a slow opponent is won by HIS forfeit (T78R7, T79R5, T80R2), but no pure drift. T80R7 was level in a closed Ruy; b4 forced the c5-knight and he forfeited. Keep units guarded and let him burn clock.
- AN EXCHANGE DOWN IS NOT A SHELL: keep d5 guarded, trade pieces not pawns, no passive knight shuffle. T80R6 lost the exchange on f6 and then drifted with ...Qd6/...Ng6/...Qb6.

## Openings
- Scheveningen W v GLM/Muse: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (15). Then f4, Qe1-g3, a4, Rad1/Kh1; e5 break, exd6/Bxd6, Nxh6 when g7 empties.
- Scheveningen vs his ...a6/...e5/...Be6 (T78R4 v Muse): f4 exf4 Bxf4 is level; Nc5 and Bf3 there are ?? once his rooks/queen come; the target is the bishop on g5/h6.
- Taimanov W: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16). Then f4/Qd2/Rad1/Kh1; e5 hits Nf6; Bxf6 gxf6 Nxf6+ vs Qd7/Rd7.
- English/Nimzo B v GLM (T78R2, 0-1 Rxe1#): 1.c4 Nf6 2.Nc3 e6 3.d4 Bb4 4.Nf3 d5 5.cxd5 exd5 6.Qa4+ Nc6 7.Bd2 Bd6 8.e3 O-O (16). Keep c6-knight + Bd6; answer Qb3 with ...Rb8 or ...Qb4.
- English B v 3.e4 (T78R7; T79R4 1/2; T80R2 forfeit): reversed French chain; ...Ne4 then d3 kicks it; SF marks ...f6?!, ...Be4??, ...Bd5??; keep the bishop behind the c-pawn, no ...g6 while Bf6 can be taken.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 (7) then ...e6/...Be7/...Nd7/...Nh6/...O-O; ...c5 only with a PIECE on d5. No ...f6 while Bd3 is on; T79R2: after ...Bxd3/Qxd3, 14.Bg5! and 14...Bxg5?? 15.Nxg5 left Qxh7#/Nxh7. T80R6 v Sonnet: ...Ne7-g6 and ...f6/...Rxf6 was level until 21...Qb6?? allowed 22.Bg5! Bxd4 23.Nxd4 winning the exchange; a rook on f6 is a Bg5 target. 35...N6h5?? abandoned d5 and allowed 36.Ne7+ forking Kg8/d5. Details notes/caro-advance-black.md.
- Caro Classical B: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). Then ...Nd7/...Nf6/...Be7/...O-O/...Qc7; ...e5 needs Bd6+Nd7. T80R4 v Muse (1/2): 21...Rcd8?? behind a blocked file and 22...e5?? opened the e-file for Re1/Ne4; keep e6 as a shield until ...c5 with pieces.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). Then h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no 20.b4.
- Ruy W 5.d3 (T78R1, T80R3 v Sonnet, T80R7 v Muse): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 d6 6.c3 Be7 7.O-O O-O 8.Nbd2 (15). Then Re1/Bc2/Nf1-g3/d4. His plan: ...Bd7 then ...b5, ...Bf8/...Re8, ...Nb4 trade, ...c5-c4-c3 clamp, ...f5-f4. Never take ...dxe4 with the queen (Qb7 covers e4). T80R7: Nf5 outpost good; d5? fixed e5/d6 and removed its targets; 26.c4?? opened the b-file. Play b4/Nd4 before c4. Details notes/ruy-lopez-white.md.
- Accelerated Dragon W v SF (T79R1 1/2, T80R5 0-1): 7.Be2 with the d5 tension; the ...d5 exchange (Nxc6/bxc6/Nxd5/Qxd5/Bf3) reached level play, then 11...Qc4! and 12.Qb1?? (SF ??) turned it (-0.3 to -5.4); 14.c3?? Rxb2! 15.Qxb2 Bxc3+ won my queen. Guard the queen with a rook or pawn, not with her own duty on the b-file. 9.O-O Nxe3 10.fxe3 is the safe even trade (T79R1); grab b7 only with a retreat (15.Bxb7 Rb8 16.Ba6 cost a bishop for a pawn).
- Other patterns: Ruy Classical 5...Bc5: c3/O-O/Re1/h3 then d4; Bb6/Nc3/Bg5/Nd5 after the exchange. Ruy B Chigorin: ...Na5/...c5/...Be6/...Qc7, keep h7 guarded. Taimanov B: ...Bf8 vs the e5 clamp, never castle/...d6/...Nf6 while e5 stands. Dragon/Soltis B: never ...Qa5 where Nb3 hits. Italian W v Muse (T79R5 1-0 flag): d3/c3, Re1, Nbd2/Nb3, Bg5, Bd5-c6; name ONE target.

## Opponents
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rook files, knights with no exit, a pawn block he can capture with check, and any plan drift in a locked centre. At +7.7 he accepted a threefold (T78R3 fortress) and again in T79R1 at +4 - the shell is a real result. The gated flood, not his play, cost those games.
- GLM 5.3 Flash: as White 1.c4/2.Nc3/3.d4/4.Nf3 Carlsbad (T78R2), the reversed-French chain (T79R4) and T80R2 (forfeit m45); his queen wanders, his bishops have no plan, he burns 2-6 min on quiet moves. Take gifts only after the capture list; bank clock.
- Sonnet 5.5: 40-50 min clock, punishes loose queen/rook/pawn grabs; T78R1, T79R2 (Caro Bg5 net), T79SF2G1 (Rb1 trap, Nf7+Bg5 mate), T80R3 Ruy 5.d3 (...c4-c3 clamp, ...Rd2-...Rb2), T80R6 Caro Advance (Bg5 won the exchange on f6; Ne7+ fork on Kg8/d5). 5-10 s from move 1; queen off his pawn/bishop/rook squares; a frozen position goes to the ending.
- Muse Spark 1.3: patient 30 s-4 min early, 5-10 s from move 15; burns 1:31-5:46 on quiet moves and blunders material when pressed (T80R4 28.Nxc5??). Give him no loose unit, take the gift, name ONE conversion, no queen shuttle; guarded keepers win on flag. T80R7 v my Ruy 5.d3: closed shell ...Bf8, ...Ne7-g6, ...c6, ...Qc7, ...cxd5/...Bc8, knight shuttles Ne4-c5; b4 forced the c5-knight and he forfeited. Expect slow defence, not gifts.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
