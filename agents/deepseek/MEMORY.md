# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W: 5.d3, Berlin d3, Closed Chigorin
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
- tools: legal-list, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender, knight-exit, heavy-fork-scan

## Rule 0 - board, legality, clock
- REFUSAL = LOSS: 3 refused tries on ONE move forfeits; a tool AVOID refuses once. Change piece AND idea, send the least-bad legal keeper in ONE try; never resend the flagged idea. T83R1: 6 invalid + 120 s quiet keepers, forfeited m61 with 13:44 left. T83R3: 4 invalid (2/3/2 tries on ...Bg6/...b6/...Nh5) forfeited m25 with 15:30 left. Gated send = 5-15 s.
- MATE DEFENCE IS A SQUARE LIST, ONE TRY: with Qg7#/Qh6+ on, name the rook squares covering g7 (c7/d7/e7/f7), send in 5-15 s.
- ARMAGEDDON WHITE (10 min) IS A CLOCK GAME FIRST: level board lost on time (T81R7). Book/Ruy keepers 3-10s, routine cap 15s, under 5 min 3-5s. 30s only for a named forcing line or a mate defence.
- A QUEEN CAPTURE THE TOOL FLAGS WITH A KNIGHT CHECK IS DEAD: T81R6 17...Qxd6?? Nxd6+. When c4 kicks my Nd5, the knight moves; never answer a kick with a queen grab.
- REREAD THE FEN, SEND A PLAINLY LEGAL UCI: T78R2/R4/R7, T80R3/R4/R7, T81R2/R4, T82R2, T82R5, T82R6, T83R1/R3 had illegal sends. A refused quiet keeper becomes a DIFFERENT quiet keeper in one try. T83R4: 21.Bg5 gated twice; still one illegal, not fatal.
- Tool AVOID is not material: count queen for bishop/rook before obeying; IN CHECK a pawn-loss flag is NOISE.
- Material from the board every move, written W x / B y. Name my loose units and his lines to them before any quiet move.
- ONE HEAVY ON A FORK SQUARE IS A FORK: T83R1 ...Qb6 and ...Rf8 both sat on the d7-knight's fork squares - 17.Nd7! took the exchange free. Before moving a queen with a rook on an open 8th/7th rank, check BOTH my heavy squares against every enemy knight jump.

## Rule 1 - destination sweep
- WHEN HIS MOVE UNGUARDS A UNIT, HIT IT THAT MOVE: T81R7 27.Rce1 left c3 unguarded - ...Rxc3! won a free pawn.
- A PAWN BLOCK ON A BISHOP'S DIAGONAL IS NOT A WALL: he captures the blocker WITH CHECK (T80R5 14...Rxb2! 15.Qxb2 Bxc3+). THE RECAPTURE CHOICE CREATES THE TARGET: T81R4 9...exf5?! left f5 on Bd3's line.
- RECAPTURE WITH THE PIECE THAT DOES NOT OPEN A LINE: T77R5 31...Qxc3 32.Nxc3?? took Ne2 off b5-f1 and ...Bxf1 won the exchange.
- A GUARD MUST REACH IN ONE MOVE; a pinned guard guards nothing. AN ATTACKED PIECE GETS ITS RETREAT/EXCHANGE LIST BEFORE ANY QUIET MOVE: T82R7.3 16.Ra1?? defended a2 while his Nb4 hit Bd3.
- A BISHOP ON THE 7th WITH NO RETREAT IS A TEMPO TARGET: T79R1 15.Bxb7 Rb8 16.Ba6 Rxb2. MY ROOK ON b2/b3 HOLDING A PAWN IS A BISHOP TARGET: T82R2 38.Rb2?/43.Rb2?! let ...Bd4 hit it twice.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; every knight jump; every bishop/rook line. PAWN FORK ON A KNIGHT LANDING (T76R4).
- AN ATTACK IS NOT A DEFENCE; my own piece on a line is my only screen (T81R7 23.Ne5? Bxe5! and dxe5 Qxd1+).
- A KNIGHT ON f5 + my Kg8 + Nf6 guarding d5: ...Nf6-h5?? allows Ne7+ (T80R6). A ROOK ON f6 AFTER ...f6/...Rxf6 IS A Bg5 TARGET: T80R6 21...Qb6?? 22.Bg5!.
- PAWN PUSHES: opening a file (T80R7 26.c4??; T81R4 12...c5??); 'saving' a pawn creates a second target (T81R3 16...h5?? 17.Qh6 hit Bf6+h5); a 'clamp' can be hit (T82R5 28...a3??, keep ...a4). A DOUBLE PUSH CAN BE E.P. FORK: with his e5-pawn alive and my Q/B on c7/e7, ...d5?? lets exd6 e.p. fork both (T82R1).
- A PASSED PAWN ON b2/c2 IS A FORK: T81R5 31...b2 hit Ra1+Bc1; accept the least loss in ONE try.
- HIS ...e5 COUNTERSTRIKE IN THE SCHEVENINGEN: meet it with Nf5! hitting Be7 (T82R3 only good move).

## Rule 1b - mate first
- Ask what mates if I pass; keep a rank-1 blocker or luft; K on c8 with b7 empty is a mating net.
- HIS DARK BISHOP ON h6/f6 + HIS QUEEN = g7 IS THE MATE SQUARE: name g7's guard (rook c7/d7) THAT MOVE, or trade the bishop; a wing push/queen raid is no defence. T82R6 26...f5?? (SF) after 26.Bxh6; ...Qb6+/...Qb3/...a5 hit only guarded b2 while Bf6+Qg5 closed the net.
- AFTER ...gxh6, THE OPEN g/h-FILES ARE THE POSITION: T83R3 13...h6? and 15...gxf4?! pushed the g5-pawn and opened both files; Kg8 stood naked, eval +3.5 to +5. The g5 pawn is not worth it: play ...Qe7/...Qd6/...Rfe8, trade queens, keep ...f6/...e5 closed until the king has luft. A recapture that opens a file to my king (12...hxg5) is not 'safe'.
- BACK-RANK FINISHER: T78R2 37...Rc1+! 38.Rd1 Rxd1+ 39.Re1 Rxe1#. EVERY BLOCK IS A PIECE: T80R5 19...Rd8+ 20.Bd5 Rxd5+ 21.Bd4 Rxd4#.
- A ROOK PAIR ON THE 7th + HIS Bg5/Nf7 = NO g-PAWN PUSH: T79SF2G1 40...g6?? 41.Nh6+ Kh8 42.Rh7#.
- Before trading a light bishop or a quiet queen move, name h7/g7 guards. Level position: no 30+ s think.

## Rule 2 - queen
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. T78R1 33.Qd4?? in front of Rd8 and on e4.
- BEFORE ANY QUEEN CAPTURE, WALK EVERY ENEMY KNIGHT JUMP TO HER LANDING: T81R6 Qxd6?? lost to Nxd6+.
- A QUEEN RAID ON THE OTHER WING IS NOT A DEFENCE: T82R6 ...Qb6+/...Qb3/...a5 hit only a guarded b2 and emptied my kingside while his g7 net closed. T82R7.3 20.Qg4?! same sortie habit.
- A QUEEN GUARDING TWO PAWNS ON A ROOK FILE IS A TARGET: T80R5 12.Qb1?? covered b2/c2; ...Ba6/...Rb8 hit her. HIS ROOK ON THE 4th-6th GAINS A TEMPO ON MY QUEEN (T76R4).
- HIS QUEEN WHO IS THE ONLY GUARD OF A LOOSE PIECE IS A FORK TARGET: T82R2 Bb4, so every knight hop to b3/c5 hit her with tempo and the third won the bishop (47.Nb3 forked Qc5+Rd4).
- A QUEEN BEHIND HIS e5-PAWN IS A TEMPO TARGET: T82R1 12...Qc7? on the f4-c7 diagonal screened by his e5-pawn; ...d5?? let 15.exd6 e.p. fork Qc7+Be7.
- QUEEN RECAPTURE: walk every attacker of the landing; name what she no longer guards (T76R2; g149 14.Qg3?? Qxc4).
- NO QUEEN SHUTTLE WITHOUT A NEW TARGET: T77-T83 many. In a closed Ruy/Caro pick b4, Nd4 or a trade; every queen step takes a new square or duty.

## Rule 3 - captures & trades
- RECOUNT AFTER EVERY EXCHANGE - MY NARRATIVE IS NOT THE BOARD: T80R5 I wrote 'clean pawn up, bishop pair' while material was LEVEL.
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET; MY PIECE ON HIS IS LOST. A rook that blocks stays; a rook his knight hits moves.
- KNIGHT LANDS WITH NO EXIT = PIECE: T79SF2G1 17...Nb4? Rb1 trapped it. A KNIGHT THAT HITS NOTHING IS DRIFT: play the freeing break.

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. UP = 5-10s keepers, trade pieces not pawns; a repetition while ahead OR while his clock is under 2 min is MY loss.
- UP TWO PAWNS IS A CONVERSION, NOT A SHUFFLE: T83R4 v Muse I was +2P (passed d5/b5, Qe4/Rg4/Be3) but shuffled Rg6/Rg4 and Be3/Bf2 until threefold at 2:39 v his 18:25. When his rooks double-defend g7, do not repeat: name ONE new plan (c5/d6 push, trade one rook, hit b6/e5, march K) and make a NEW move every turn; 5-10s keepers, no 1-2 min thinks in a won position.
- DEAD-LOCKED SHELL + HUGE CLOCK LEAD: NEVER ALLOW THREEFOLD. Novelty list: K g8/h8, rooks on different 8th squares, queen a6/b6 only with Bd6 guarded; every move a NEW position, 5-15s. T82R7: 36 min v his 1 min, all files locked, I let Kh8/Kg8/Rde8 cycle repeat and drew. A threefold while he is under 2 min = my lost win.
- A TRADE-DOWN AT +1P IS A CONVERSION: name ONE net, never shuffle.
- DOWN A PAWN WITH OPPOSITE BISHOPS IS A HOLDING JOB, NOT A RAID: guard every unit, keep a rook on the mating square (T82R6 48 min left, lost the g7 square), then take the free pawn.
- DRAW ODDS CHANGE THE DEAL: as Armageddon White a level position with rooks and queens off is HIS result (T81R7). Keep two rooks and the queens on, name a target.
- A LEVEL POSITION IS NOT AN AUTOMATIC DRAW: with his rooks doubled on an open file and a loose c3 pawn, ONE pawn grab beats a bishop shuttle (T81R7).
- A LEVEL CARO/CLOSED SHELL IS A CLOCK GAME: T82R5 book/equal to move 27, then 13:45 gated + 3:56 + 2:56; his 22 min beat my 11. T82R6 48 v 56 min and 8 illegal sends. T82R7.3 flagged m20 after 16.Ra1??/20.Qg4?! lost a pawn. Keep 5-15 s keepers; when a move is refused send a DIFFERENT legal keeper at once.
- A LOST POSITION IS STILL A CLOCK GAME: T83R3 8:42 on ...Nh5 at +7 and 10:07 on ...Bg6; use 5-10s keepers, not long thinks. T83R4 5:59 on 17.exd5, 5:49 on 18.Be4, 4:10 on 34.Bf2 while +2P, ended 2:39.
- DOWN A PIECE OR A PAWN IN A LOCKED CENTRE = THE SHELL: every unit guarded, rook on the one unattacked square, K h7/g8, free pawns taken, 5-15s. Try the freeing break by move 12-15. DOWN MATERIAL, A REPETITION IS MY SAVE.
- DOWN A PIECE, A FORTRESS NEEDS NO WEAK PAWN. ROOK ENDING DOWN A PAWN: name his rook's entry squares.
- A CLEAN WIN = one plan, guarded units, fast safe moves; a level game against a slow opponent is won by HIS forfeit (T78R7, T79R5, T80R2, T81R2, T81R5, T82R2, T82R3), but no pure drift.
- AN EXCHANGE DOWN IS NOT A SHELL: keep d5 guarded, trade pieces not pawns. T83R1: ...Nd5 blockaded d4 and e6/c6 held; the loss was the fork and 6 invalid sends, not the structure.

## Openings
- Ruy d3 W (main; T81R7, T82R2): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 d6 6.c3 Be7 7.O-O O-O 8.Nbd2 (15). Then Re1/Bc2/Nf1-g3/d4. His ...Bd7, ...Re8, ...Bf8, ...Qd7, ...a6/...b5/...Na5-...Nxb3 plan equalises; after ...exd4 cxd4 and ...c6 the d4 break leaves a level position, so name a plan (b4, Nd4, queenside push). The Berlin move order takes the same build. v Sonnet's ...Na5/...c5/...d5: 14.Nf5 Bxf5 15.exf5 then the d4 break = +1P; keep the f5 wedge; his ...d4/...d3/...Rxe1+ tempo is the counter (23.Nd2?? SF), answered by the Nd2 blockade.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). Then h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no 20.b4.
- Scheveningen/Taimanov W: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (16). Then f4, Qd2 (NEVER Qd3: blocks Be2-b5 and ...Bxe4! hits her), a4, Rad1/Kh1, e5 break. Before Nd5 count ...Bc5+! (T83R2 17.Nd5?? Bc5+ 18.Be3 Bxd5); after ...e5, Nf5 hits Be7 but e4 must stay truly guarded. Taimanov (...Nc6/...a6) same build; ...b4 answered by Nd4-c6 forking Qb8+Be7 (T81R2). vs ...a6/...e5/...Be6 (T78R4) f4 exf4 Bxf4 level. T82R3 v GLM: ...e5?? met Nf5!; T83R2 his ...e5! at m9 was fine, he flagged after 16:47/7:34 thinks. T83R4 v Muse: same build, 12.a4, 15.Bd3, 16.Rfe1, 17.exd5, 18.Be4, 19.f5, 20.Qd3 freed Nc3, 26.Nb5-27.Bg5 won B+h4 pawn = +2P. Then no conversion plan: convert, never repeat.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 (7) then ...e6/...Nd7/...Ne7/...Be7/...O-O; ...c5 only with a PIECE on d5; no ...f6 while Bd3 is on. PATH-CHECK: ...Be7 was blocked by my own Ne7 (T82R6 8...Be7 illegal). T82R6 v Sonnet: the move-11 c5 break was right and level; the loss was 26.Bxh6 met by 26...f5?? (SF) plus a queen raid instead of a rook covering g7. T81R7: 27.Rce1 left c3 loose - ...Rxc3! won a pawn. T81R3 16...h5??, T80R6 ...Qb6?? Bg5 and ...N6h5?? Ne7+. T83R3 v SF: 7...Nh6 8.Bxh6 gxh6! was fine, then 13...h6?/15...gxf4?! opened g/h files and lost; 10...Bg6 took 10:07 with 2 gated tries, 20...b6 3:09/3 tries, 24...Nh5 8:42/2 tries = 4 invalid and forfeit m25. After ...gxh6 no ...h6/...hxg5/...gxf4; queen trade and ...Qe7/...Rfe8 first. 5-15s keepers, never 8-min on a lost position.
- Caro Classical B/W: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). As Black then ...Nd7/...Nf6/...Be7/...O-O/...Qc7; ...e5 needs Bd6+Nd7. T82R7 v Muse: ...Bxd3, ...Nd7, ...Be7, ...O-O, ...Bd6 and the ...c5/...b5 shell was dead level; I lost the win by allowing threefold at 36 min v 1 min. T80R4 21...Rcd8?? behind a blocked file. T82R5 v Muse: ...b5/...a5/...b4/...a4 and ...Nd5-c4 was level; after ...a4 prefer ...Qa5/...Rfb8 pressure over 28...a3??; the ...Be7/...Rab8/...Qc7 shuffle was drift. A gated 27...Qc6 cost 13:45 - send a keeper in one try. AS WHITE T82R7.3: 9.Bd3 (trade if ...Bxd3), O-O, Bf4, Qe2, Ne5; ...Nb4 hits Bd3, so save/exchange it; 16.Ra1?? lost a pawn to ...Nxd3/...Bf6/...Qxd3.
- English/Nimzo B (T78R2 loss): 1.c4 Nf6 2.Nc3 e6 3.d4 Bb4 4.Nf3 d5 5.cxd5 exd5 6.Qa4+ Nc6 7.Bd2 Bd6 8.e3 O-O (16). Keep the c6-knight + Bd6; answer Qb3 with ...Rb8 or ...Qb4.
- Accelerated Dragon W v SF (T79R1 draw, T80R5 loss): 7.Be2 with d5 tension; guard the queen with a rook or pawn, not her own duty on the b-file. Grab b7 only with a retreat.
- Other patterns: Ruy Classical 5...Bc5: c3/O-O/Re1/h3 then d4. Taimanov B: ...Bf8 vs 9.Qg4 clamp; no ...d6/...Nf6 while e5 stands; keep Q off c7 (T82R1 12...Qc7?, ...d5?? exd6 e.p. forked Q+Be7); after a c4 kick move the knight (T81R6). Dragon/Soltis B: never ...Qa5 where Nb3 hits. Italian W v Muse: d3/c3, Re1, Nbd2/Nb3, Bg5, Bd5-c6; name ONE target.

## Opponents
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rook files, knights with no exit, pawn block capture with check, plan drift in a locked centre. Accepts a threefold vs a sound shell even at +7 (T78R3, T79R1). T82R1: 8.e5/9.Qg4 clamp; ...Qc7 behind e5 and ...d5?? lost to e.p. fork. T83R3: after 8.Bxh6 gxh6! he played h4/hxg5/f4/Qxf4/O-O-O and won the open g/h files; my ...h6?/...gxf4?! were the ?? marks. King exposure is enough for him.
- GLM 5.3 Flash: as White Carlsbad/reversed-French; queen wanders, burns 1-2.5 min on quiet moves; a knight fork on Q+piece ends it (T81R2 14.Nc6). As Black Sicilian: T82R3 ...e5??/...g6?! lost B for N; T83R2 Scheveningen ...e5! was fine, but 16:47 on ...Bxe4 and 7:34 on ...Re6 (3 gated each) flagged m32. My 16.Qd3?/17.Nd5??/18.Be3?? let ...Bc5+ take the d5 knight: keep Qd2, guard e4, bank.
- Sonnet 5.5: 40-56 min clock, zero/few illegal, punishes loose queen/rook/pawn grabs and takes a pawn with Bxh6 then plays Bf6+Qg5 (T82R6). T78R1, T79R2, T79SF2G1 (Rb1 trap, Nf7+Bg5 mate), T80R3, T80R6 (Bg5 won the exchange; Ne7+ fork), T81R3 (Qh6 hit Bf6+h5), T81R7 Caro Draw. T82R2 (1-0 forfeit, level): full Chigorin vs my 5.d3 with ...d5/...d4/...d3 wedge; his queen tied to a loose bishop was my fork target. T82R6 (1-0, Qe7# m41): Caro Advance, level to move 25, my 26...f5?? and queen raid lost g7. T83R1 (1-0 forfeit m61, 52:44 v 2:20): Caro Advance, he gave the exchange with 17.Nd7! hitting Qb6+Rf8, then level; 6 invalid sends and ...Ke7?? ended it. Never offer him mass simplification on draw odds; keep queen+rook off one knight's fork squares.
- Muse Spark 1.3: patient 30s-4min early, 5-10s from move 15; burns clock but holds a locked shell with zero invalid. T82R5 win by forfeit m39, T82R7 draw (36 min v 1 min; he defended, I allowed threefold), T82R7.3 1-0 flag m20 (0:39 v 7:07; my 16.Ra1?? lost a pawn). T83R4 draw: he double-defended g7 with Rf7/Rdd7 and Kh8/Kg8; I was +2P but repeated. He banks 18 min and does NOT flag when I am shorter: convert, never wait. Give no loose unit, take the gift, name ONE conversion; when he is under 2 min, vary every move and never repeat. T80R7 v my Ruy 5.d3: b4 forced the c5-knight and he forfeited. T81R5: ...b4-c4-b3-c2 storm, 1-4min, zero illegal until the final 3 gated tries. T82R5 as White v my Caro: patient O-O-O and K walk, 22:37 left; level until my ...a3?? and shuffle.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
