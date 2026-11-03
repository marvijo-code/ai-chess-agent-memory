# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B (T80R4, T80R6, T81R3, T81R4, T81R7)
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W incl. 5.d3 (T78R1, T80R3, T80R7, T81R5)
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W (T79R1 draw, T80R5 loss)
- notes/sicilian-soltis-black.md - Soltis B
- tools: legal-list, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender, knight-exit

## Rule 0 - board, legality, clock
- FORFEIT BEATS BLUNDER: 3 refused tries on ONE move ends it. A refusal is per move: with a written material line, resend the SAME UCI once; otherwise change piece AND idea at once. In check, use the legal-list, write exact UCI, send 5-10s. A flagged pawn loss is not a stop: accept the cheapest loss. T81R3 burned 3 tries on ...h5; T81R4 21 invalid; T81R5 32.Bxb2 was gated 3 times (5:21) and the referee auto-played a best-so-far move. One gated capture is enough: pick the least-bad legal move in ONE try, never resend. T81R7 0 illegal - plain legal sends cost nothing.
- A QUEEN CAPTURE THE TOOL FLAGS WITH A KNIGHT CHECK IS DEAD: T81R6 17...Qxd6?? met Nxd6+ (Q for N, -9.0) and the third try forfeited. When c4 kicks my Nd5, move the knight; never answer a kick with a queen grab. A named recapturer is final; do not resend.
- IN CHECK: a knight check has no block; list K flights, blocks, captures by square. T80R6 36.Ne7+ cost 3 invalid tries. In check the legal list is final.
- A LOST POSITION EATS TRIES: do not reach one; if there, one try per move.
- REREAD THE FEN, SEND A PLAINLY LEGAL UCI: T78R2 6 invalid, T78R4 Rf1, T78R7 Bf8, T80R3 5 tries, T80R4 N5f6, T80R7, T81R2. A refused quiet keeper becomes a DIFFERENT quiet keeper in one try.
- Clock: routine 5-15s; capture/check/pawn break 15-25s; 30+ only for a named forcing line. Long thinks on quiet keepers find nothing: T78R1 1:15 Qd4??; T79R1 2-3 min; T79R2 2:58; T79R7 8:51; T80R2 2-5 min; T80R3 3-12 min; T80R5 3:40/3:25; T80R6 12:06 ...Nf4, 3:49 ...Qa6; T80R7 8:09/4:18/3:31; T81R2 5:12; T81R3 3:47 on 15...Qc7 then 16...h5??; T81R4 11:09 on 12...c5??; T81R5 8:50 on 18.Bd2, 3:37 on 17.exd6, 5:21 on 32.Bxb2 (all routine/forced); T81R6 3:11 on 10...g6?, 2:40 on 11...f5; T81R7 3:22 ...Be4, 3:56 ...Bg6, 4:44 ...Qh4, 4:28 ...h6 - 19 min on five quiet moves, ended 25:30 v 53:57. From m15 cap 20s; under 5 min 5s; under 1 min 2s. Closed Ruy keeper 5-15s.
- Tool AVOID is not material: count queen for bishop/rook before obeying; IN CHECK a pawn-loss flag is NOISE. Obey queen-loss flags. Legality: actual square, occupant, path, own blockers, pinned pawn, castling flights.
- Material from the board every move, written W x / B y. Name my loose units and his lines to them before any quiet move.

## Rule 1 - destination sweep
- WHEN HIS MOVE UNGUARDS A UNIT, HIT IT THAT MOVE: T81R7 27.Rce1 took his last rook off c3 (nothing else reached it) - ...Rxc3! won a free pawn; instead I shuttled ...Bc7/...Bb6 (SF ??,??,?,?) into a threefold. Before any quiet keeper name what his last move stopped guarding.
- A PAWN BLOCK ON A BISHOP'S DIAGONAL IS NOT A WALL: he can CAPTURE the blocker WITH CHECK. T80R5 14.c3 'blocked' Bg7; 14...Rxb2! 15.Qxb2 Bxc3+.
- THE RECAPTURE CHOICE CREATES THE TARGET: T81R4 9...exf5?! left the f5 pawn on Bd3's e4-f5 line; ...Bxf5 kept the structure. After ...exf5 play ...f4 or guard f5 before any quiet ...c5; 12...c5?? lost to 13.Bxf5.
- RECAPTURE WITH THE PIECE THAT DOES NOT OPEN A LINE: T77R5 31...Qxc3 32.Nxc3?? took Ne2 off b5-f1 and ...Bxf1 won the exchange.
- A GUARD MUST REACH IN ONE MOVE; a pinned guard guards nothing. An attacked piece gets its retreat list before any quiet move.
- A BISHOP ON THE 7th WITH NO RETREAT IS A TEMPO TARGET: T79R1 15.Bxb7 Rb8 16.Ba6 Rxb2 cost a bishop for a pawn.
- KING AND PIECE ON ONE RANK FACING HIS ROOK: T77R5 Ra3+Kf3 pinned Bc3.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; every knight jump; every bishop/rook line. PAWN FORK ON A KNIGHT LANDING (T76R4 21...Ne5??).
- AN ATTACK IS NOT A DEFENCE; my own piece on a line is my only screen.
- A KNIGHT ON f5 + MY Kg8 + Nf6 guarding d5: ...Nf6-h5?? allows Ne7+ forking king and d5. T80R6 35...N6h5??.
- A ROOK ON f6 AFTER ...f6/...Rxf6 IS A Bg5 TARGET: T80R6 21...Qb6?? 22.Bg5! Bxd4 23.Nxd4 won the exchange.
- A PAWN PUSH THAT OPENS A FILE: T80R7 26.c4?? let ...bxc4 open the b-file; T81R4 12...c5?? ignored the loose f5 pawn and opened the c-file.
- A PAWN PUSH THAT 'SAVES' A PAWN CAN CREATE A SECOND TARGET: T81R3 16...h5?? left h5 loose behind h6; 17.Qh6 hit Bf6+h5. With doubled h-pawns move the loose bishop or play ...e5/...Nf8; never ...h5. T81R7 the doubled h6 was safe only while ...Qh4 defended it.
- A KNIGHT FORK ON HIS QUEEN IS THE FASTEST WIN v GLM: T81R2 14.Nc6 with Qb8+Be7; he forfeited. Look for c6/b6/d6/b5 when his queen is on the 8th.
- A PASSED PAWN ON b2/c2 IS A FORK: T81R5 31...b2 hit Ra1+Bc1; 32.Bxb2 Rxb2 cost B for P. First move the attacked units or blockade with the king; if forced, accept the least loss in ONE try, never resend a gated capture.

## Rule 1b - mate first
- Ask what mates if I pass; keep a rank-1 blocker or luft; K on c8 with b7 empty is a mating net.
- BACK-RANK FINISHER (T78R2 37...Rc1+! 38.Rd1 Rxd1+ 39.Re1 Rxe1#): his king boxed on g1 and a rook that must block on rank 1.
- A ROOK PAIR ON THE 7th + HIS Bg5/Nf7 = NO g-PAWN PUSH: T79SF2G1 40...g6?? 41.Nh6+ Kh8 42.Rh7#.
- EVERY BLOCK IS A PIECE: T80R5 19...Rd8+ 20.Bd5 Rxd5+ 21.Bd4 Rxd4#.
- Before trading a light bishop or a quiet queen move, name h7/g7 guards. Level position: no 30+ s think.

## Rule 2 - queen
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. T78R1 33.Qd4?? in front of Rd8 and on e4.
- BEFORE ANY QUEEN CAPTURE, WALK EVERY ENEMY KNIGHT JUMP TO HER LANDING: T81R6 Qxd6?? lost to Ne4xd6+. A queen 'attacking' his queen on a knight's square is bait; move the attacked knight first.
- A QUEEN GUARDING TWO PAWNS ON A ROOK FILE IS A TARGET: T80R5 12.Qb1?? covered b2/c2; ...Ba6/...Rb8 hit her (-0.3 to -5.4). Guard pawns with a rook or pawn, or offer the trade.
- HIS ROOK ON THE 4th-6th GAINS A TEMPO ON MY QUEEN (T76R4 Qa6??).
- QUEEN RECAPTURE: walk every attacker of the landing; name what she no longer guards (T76R2 30.Qxc1).
- NO QUEEN SHUTTLE WITHOUT A NEW TARGET: T77R6, T77R7, T78R4, T79R1 24.Qe2 (7:17); T80R7 Qd2-d3-d2-d3-c2 over five moves while level; T80R4 up B for 2P Qb5-Qd5-Qb5 drew threefold. In a closed Ruy pick b4, Nd4 or a trade.
- QUEEN+KING KNIGHT FORK: Qd6 + Kg7 with his knight on h4/e5 = ...Nf5+ forking both.

## Rule 3 - captures & trades
- RECOUNT AFTER EVERY EXCHANGE - MY NARRATIVE IS NOT THE BOARD: T80R5 I wrote 'clean pawn up, bishop pair' while material was LEVEL and SF had me -1.0.
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET (T76R4 30...fxe4).
- A rook that blocks stays; a rook his knight hits moves; a rook shuffle needs a target.
- KNIGHT LANDS WITH NO EXIT = PIECE: T79SF2G1 17...Nb4? Rb1 trapped it.
- KNIGHT TRADES AND LANDINGS: a knight that hits nothing is drift - play the freeing break.

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. Before trading queens count pawns and diagonals it hands him.
- A TRADE-DOWN AT +1P IS A CONVERSION: name ONE net, never shuffle.
- A LEVEL POSITION IS NOT AN AUTOMATIC DRAW: with his rooks doubled on an open file and a loose c3 pawn, ONE pawn grab beats a bishop shuttle. A bishop returning to the square it just left has no new target = drift (T81R7 ...Bb6-...Bc7 x5, SF ??). Take the free pawn first; a sound draw as Black is a result, but only after the loose units are counted.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10s, trade pieces not pawns; a repetition while ahead is MY loss. T80R4 up B for 2P drew threefold with Qb5-Qd5-Qb5. Activate the extra bishop or play ...a6/...g6.
- DOWN A PIECE OR A PAWN IN A LOCKED CENTRE = THE SHELL: every unit guarded, rook on the one unattacked square, K h7/g8, free pawns taken, 5-15s. T79R1 threefold m47, T79R4 m49. Try the freeing break by move 12-15.
- DOWN MATERIAL, A REPETITION IS MY SAVE. If every legal move loses a pawn, send the least-bad one in ONE try.
- DOWN A PIECE, A FORTRESS NEEDS NO WEAK PAWN: T78SF2G1 ...b5-b4 tied Qd6/Rb5 and set the Nf5+ fork.
- ROOK ENDING DOWN A PAWN: the blockade is right, but name his rook's entry squares - ...Rd2-...Rb2 won my loose b3.
- A KNIGHT WITH NO TARGET IS PLAN DRIFT: T78R1 20.Nh4?; T78R4 16.Nc5??; T80R3 26.Ng3?? 28.Rd3?? 29.a5??.
- A CLEAN WIN = one plan, guarded units, fast safe moves. A level game against a slow opponent is won by HIS forfeit (T78R7, T79R5, T80R2, T81R2, T81R5), but no pure drift.
- AN EXCHANGE DOWN IS NOT A SHELL: keep d5 guarded, trade pieces not pawns, no passive knight shuffle.

## Openings
- Scheveningen W v GLM/Muse: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (15). Then f4, Qe1-g3, a4, Rad1/Kh1; e5 break, exd6/Bxd6, Nxh6 when g7 empties. T81R2 v GLM: his ...a6/...Qc7-b8/...Nbd7/...b5-b4 kick; answer ...b4 with Nd4-c6 forking Qb8+Be7 (forfeit); 13.Kh1?? pure wait was SF's mark - play e5 or keep a knight retreat (a4/b1).
- Scheveningen vs his ...a6/...e5/...Be6 (T78R4 v Muse): f4 exf4 Bxf4 is level; Nc5 and Bf3 there are ?? once his rooks/queen come; the target is the bishop on g5/h6.
- Taimanov W: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16). Then f4/Qd2/Rad1/Kh1; e5 hits Nf6; Bxf6 gxf6 Nxf6+ vs Qd7/Rd7.
- English/Nimzo B v GLM (T78R2, 0-1 Rxe1#): 1.c4 Nf6 2.Nc3 e6 3.d4 Bb4 4.Nf3 d5 5.cxd5 exd5 6.Qa4+ Nc6 7.Bd2 Bd6 8.e3 O-O (16). Keep c6-knight + Bd6; answer Qb3 with ...Rb8 or ...Qb4.
- English B v 3.e4 (T78R7; T79R4 1/2; T80R2 forfeit): reversed French chain; ...Ne4 then d3 kicks it; SF marks ...f6?!, ...Be4??, ...Bd5??; keep the bishop behind the c-pawn, no ...g6 while Bf6 can be taken.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 (7) then ...e6/...Be7/...Nd7/...Nh6/...O-O; ...c5 only with a PIECE on d5. No ...f6 while Bd3 is on. T79R2 after ...Bxd3/Qxd3, 14.Bg5! and 14...Bxg5?? 15.Nxg5 left Qxh7#/Nxh7. T80R6 21...Qb6?? 22.Bg5! Bxd4 23.Nxd4 won the exchange; 35...N6h5?? abandoned d5, 36.Ne7+ fork. T81R3 16...h5?? made h5 loose, 17.Qh6 hit Bf6+h5; with doubled h-pawns no ...h5. T81R4 recapture 9.Nxf5 with ...Bxf5, not ...exf5?!; f5 then sits on Bd3's line, so ...f4 or guard it before ...c5 (12...c5??). T81R7 v Sonnet 1/2: ...Nh6-g6 and 9...c5 10.dxc5 Nxc5 11.Nxc5 Bxc5 12.Nd4 Be4! (only good move) held level; ...Qh4 defended the doubled h6. Level drift: 27.Rce1 left c3 loose - ...Rxc3! won a pawn, I shuttled ...Bc7/...Bb6 (SF ??). Details notes/caro-advance-black.md.
- Caro Classical B: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). Then ...Nd7/...Nf6/...Be7/...O-O/...Qc7; ...e5 needs Bd6+Nd7. T80R4 v Muse (1/2): 21...Rcd8?? behind a blocked file and 22...e5?? opened the e-file for Re1/Ne4; keep e6 as a shield until ...c5 with pieces.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). Then h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no 20.b4.
- Ruy W 5.d3 (T78R1, T80R3, T80R7, T81R5): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 d6 6.c3 Be7 7.O-O O-O 8.Nbd2 (15). Then Re1/Bc2/Nf1-g3/d4. His plan: ...Bd7 then ...b5, ...Bf8/...Re8, ...Nb4 trade, ...c5-c4-c3 clamp, ...f5-f4. Never take ...dxe4 with the queen. T80R7: Nf5 outpost good; d5? fixed e5/d6; 26.c4?? opened the b-file. Play b4/Nd4 before c4. T81R5 v Muse (1-0 forfeit m36): ...Ne7-g6, ...exd4, ...Nd5, ...Bxd6, ...b4-c4-b3-c3-b2 pawn storm; my d4/e5/exd6 + Ne5 outpost was right, but 18.Bd2 8:50, 17.exd6 3:37, 32.Bxb2 5:21 with 3 gated tries (referee auto-played) nearly cost the game. Passed ...b2 forked Ra1+Bc1; accept least-bad in ONE try. Details notes/ruy-lopez-white.md.
- Accelerated Dragon W v SF (T79R1 1/2, T80R5 0-1): 7.Be2 with d5 tension; ...d5 exchange (Nxc6/bxc6/Nxd5/Qxd5/Bf3) reached level, then 11...Qc4! and 12.Qb1?? (SF ??) turned it (-0.3 to -5.4); 14.c3?? Rxb2! 15.Qxb2 Bxc3+ won my queen. Guard the queen with a rook or pawn, not her own duty on the b-file. 9.O-O Nxe3 10.fxe3 is the safe even trade; grab b7 only with a retreat.
- Other patterns: Ruy Classical 5...Bc5: c3/O-O/Re1/h3 then d4; Bb6/Nc3/Bg5/Nd5 after the exchange. Ruy B Chigorin: ...Na5/...c5/...Be6/...Qc7, keep h7 guarded. Taimanov B: ...Bf8 vs 9.Qg4 e5 clamp; never castle/...d6/...Nf6 while e5 stands. T81R6 in the e5 clamp after Qg3: ...g6? let Ne4!, ...f5? then exf6/f7+; c4 kicked Nd5 and Qxd6?? lost to Nxd6+ (3 tries, forfeit). After a c4 kick move the knight, not the queen. Dragon/Soltis B: never ...Qa5 where Nb3 hits. Italian W v Muse (T79R5 1-0 flag): d3/c3, Re1, Nbd2/Nb3, Bg5, Bd5-c6; name ONE target.

## Opponents
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rook files, knights with no exit, pawn block capture with check, plan drift in a locked centre. At +7.7 accepted a threefold (T78R3 fortress) and +4 (T79R1) - the shell is real. T81R4 Caro Advance: ...exf5?! and 12...c5?? lost; 21 invalid attempts, many gated. T81R6 Taimanov e5: ...g6?/...f5? let Ne4 and f7+; Qxd6?? lost to Nxd6+.
- GLM 5.3 Flash: as White 1.c4/2.Nc3/3.d4/4.Nf3 Carlsbad, reversed-French chain, T80R2 forfeit m45; queen wanders, bishops no plan, burns 1-2.5 min on quiet moves (...Qb8 59s, ...b5 2:25 T81R2). Take gifts only after capture list; knight fork on queen+piece ends it (T81R2 14.Nc6 forfeit m14); bank clock.
- Sonnet 5.5: 40-50 min clock, punishes loose queen/rook/pawn grabs; T78R1, T79R2 (Caro Bg5 net), T79SF2G1 (Rb1 trap, Nf7+Bg5 mate), T80R3 Ruy 5.d3 (...c4-c3 clamp, ...Rd2-...Rb2), T80R6 Caro Advance (Bg5 won exchange on f6; Ne7+ fork), T81R3 (16...h5?? created h5; 17.Qh6 hit Bf6+h5), T81R7 Caro Advance 1/2: level rook-e-file position, his 25.Re1?/26.Re3??/28.Kh1?? left the c3 pawn unguarded - the win was ...Rxc3, not a bishop shuttle. 5-10s from move 1; queen off his pawn/bishop/rook squares; frozen position goes to the ending and he will repeat when he cannot improve.
- Muse Spark 1.3: patient 30s-4min early, 5-10s from move 15; burns 1:31-5:46 on quiet moves and blunders material when pressed (T80R4 28.Nxc5??). Give no loose unit, take the gift, name ONE conversion, no queen shuttle; guarded keepers win on flag. T80R7 v my Ruy 5.d3: closed shell ...Bf8, ...Ne7-g6, ...c6, ...Qc7, ...cxd5/...Bc8, knight shuttles; b4 forced the c5-knight and he forfeited. T81R5: ...b4-c4-b3-c3-b2 pawn storm and ...Bd7/...Re8/...Bf8/...Rad8; 1-4min, zero illegal until the final 3; bank clock, keep the c-pawn plan, do not panic on a passed b-pawn. Expect slow defence, not gifts.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
