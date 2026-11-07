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
- tools: legal-list, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender, knight-exit

## Rule 0 - board, legality, clock
- FORFEIT BEATS BLUNDER: 3 refused tries on ONE move ends it. After ONE refusal change piece AND idea; send the least-bad legal move in one try; never resend a flagged capture (T81R5 32.Bxb2 x3). T82R5: 4 invalid attempts and 13:45 on a gated 27...Qc6 - a gated queen/rook retreat is a 5-15 s one-try keeper, never a debate. In check the legal list is final: flights, blocks, captures by square. T82R7 0 illegal.
- MATE DEFENCE IS A SQUARE LIST, ONE TRY: with Qg7#/Qh6+ on, name the rook squares that cover g7 (c7/d7/e7/f7) and send in 5-15 s. T82R6 34...Rc7 (the only idea) took 4:04 and 3 tries, 37...Rh7 5:43, plus ...Be7 through my own Ne7 and gated Kf8/Ke8.
- ARMAGEDDON WHITE (10 min) IS A CLOCK GAME FIRST: T81R7 lost on time with the board LEVEL. Book/Ruy keepers 3-10s, routine cap 15s, under 5 min 3-5s. Long thinks on quiet keepers find nothing (T78R1, T79R1/R2/R7, T80R2/R3/R5/R6/R7, T81R2-R7, T82R2, T82R5, T82R6, T82R7). 30s only for a named forcing line or a mate defence.
- A QUEEN CAPTURE THE TOOL FLAGS WITH A KNIGHT CHECK IS DEAD: T81R6 17...Qxd6?? Nxd6+. When c4 kicks my Nd5, the knight moves; never answer a kick with a queen grab.
- REREAD THE FEN, SEND A PLAINLY LEGAL UCI: T78R2/R4/R7, T80R3/R4/R7, T81R2/R4, T82R2, T82R5, T82R6 had illegal sends. A refused quiet keeper becomes a DIFFERENT quiet keeper in one try.
- Tool AVOID is not material: count queen for bishop/rook before obeying; IN CHECK a pawn-loss flag is NOISE.
- Material from the board every move, written W x / B y. Name my loose units and his lines to them before any quiet move.

## Rule 1 - destination sweep
- WHEN HIS MOVE UNGUARDS A UNIT, HIT IT THAT MOVE: T81R7 27.Rce1 left c3 unguarded - ...Rxc3! won a free pawn; I shuttled ...Bc7/...Bb6 into a threefold. Before any quiet keeper name what his last move stopped guarding.
- A PAWN BLOCK ON A BISHOP'S DIAGONAL IS NOT A WALL: he can capture the blocker WITH CHECK (T80R5 14...Rxb2! 15.Qxb2 Bxc3+).
- THE RECAPTURE CHOICE CREATES THE TARGET: T81R4 9...exf5?! left f5 on Bd3's e4-f5 line. After ...exf5 play ...f4 or guard f5 before ...c5.
- RECAPTURE WITH THE PIECE THAT DOES NOT OPEN A LINE: T77R5 31...Qxc3 32.Nxc3?? took Ne2 off b5-f1 and ...Bxf1 won the exchange.
- A GUARD MUST REACH IN ONE MOVE; a pinned guard guards nothing. An attacked piece gets its retreat list before any quiet move.
- A BISHOP ON THE 7th WITH NO RETREAT IS A TEMPO TARGET: T79R1 15.Bxb7 Rb8 16.Ba6 Rxb2.
- MY ROOK PARKED ON b2/b3 TO HOLD A PAWN OR KNIGHT IS A BISHOP TARGET: T82R2 38.Rb2?/43.Rb2?! let ...Bd4 hit it with tempo twice. Post a rook where his bishop cannot reach it unless it wins a pawn.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; every knight jump; every bishop/rook line. PAWN FORK ON A KNIGHT LANDING (T76R4).
- AN ATTACK IS NOT A DEFENCE; my own piece on a line is my only screen (T81R7 23.Ne5? Bxe5! and dxe5 Qxd1+).
- A KNIGHT ON f5 + my Kg8 + Nf6 guarding d5: ...Nf6-h5?? allows Ne7+ (T80R6).
- A ROOK ON f6 AFTER ...f6/...Rxf6 IS A Bg5 TARGET: T80R6 21...Qb6?? 22.Bg5! won the exchange.
- A PAWN PUSH THAT OPENS A FILE: T80R7 26.c4??; T81R4 12...c5?? ignored the loose f5 pawn and opened the c-file.
- A PAWN PUSH THAT 'SAVES' A PAWN CREATES A SECOND TARGET: T81R3 16...h5?? left h5 loose; 17.Qh6 hit Bf6+h5. With doubled h-pawns never ...h5.
- A PAWN PUSH THAT 'CLAMPS' CAN BE A TARGET: T82R5 28...a3?? (SF ??) put the a-pawn where his queen/knight could hit it; keep ...a4 as the clamp, and count what the new pawn no longer guards.
- A DOUBLE PAWN PUSH CAN BE EN PASSANT FORK: with his e5-pawn alive and my Q/B on c7/e7, ...d5?? lets exd6 e.p. fork both and opens the diagonal behind (T82R1). Walk e5's capture square before any ...d5/...d6.
- A PASSED PAWN ON b2/c2 IS A FORK: T81R5 31...b2 hit Ra1+Bc1; accept the least loss in ONE try.
- HIS ...e5 COUNTERSTRIKE IN THE SCHEVENINGEN: meet it with Nf5! hitting Be7 (T82R3 only good move), before the f-pawn falls.

## Rule 1b - mate first
- Ask what mates if I pass; keep a rank-1 blocker or luft; K on c8 with b7 empty is a mating net.
- HIS DARK BISHOP ON h6/f6 + HIS QUEEN = g7 IS THE MATE SQUARE: name g7's guard (a rook on c7/d7) THAT MOVE, or trade the bishop; a wing push or a queen raid is not a defence. T82R6 26...f5?? (SF) after 26.Bxh6, then ...Qb6+/...Qb3/...a5 at a guarded b2 while 31.Bf6 (Qd2-guarded, untouchable) and 32.Qg5 closed the net; ...Rc7 came at move 34, four moves late.
- BACK-RANK FINISHER: T78R2 37...Rc1+! 38.Rd1 Rxd1+ 39.Re1 Rxe1#.
- A ROOK PAIR ON THE 7th + HIS Bg5/Nf7 = NO g-PAWN PUSH: T79SF2G1 40...g6?? 41.Nh6+ Kh8 42.Rh7#.
- EVERY BLOCK IS A PIECE: T80R5 19...Rd8+ 20.Bd5 Rxd5+ 21.Bd4 Rxd4#.
- Before trading a light bishop or a quiet queen move, name h7/g7 guards. Level position: no 30+ s think.

## Rule 2 - queen
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. T78R1 33.Qd4?? in front of Rd8 and on e4.
- BEFORE ANY QUEEN CAPTURE, WALK EVERY ENEMY KNIGHT JUMP TO HER LANDING: T81R6 Qxd6?? lost to Nxd6+; a queen 'attacking' his queen on a knight square is bait.
- A QUEEN RAID ON THE OTHER WING IS NOT A DEFENCE: T82R6, down a pawn with opposite bishops, ...Qb6+/...Qb3/...a5 hit only a guarded b2 and emptied my kingside while his g7 net closed. She stays where she covers my king or a mating square.
- A QUEEN GUARDING TWO PAWNS ON A ROOK FILE IS A TARGET: T80R5 12.Qb1?? covered b2/c2; ...Ba6/...Rb8 hit her.
- HIS QUEEN WHO IS THE ONLY GUARD OF A LOOSE PIECE IS A FORK TARGET: T82R2 she had to hold Bb4, so every knight hop to b3/c5 hit her with tempo and the third one won the bishop (47.Nb3 forked Qc5+Rd4). Fork a tied queen, never a free one.
- HIS ROOK ON THE 4th-6th GAINS A TEMPO ON MY QUEEN (T76R4).
- A QUEEN BEHIND HIS e5-PAWN IS A TEMPO TARGET: T82R1 12...Qc7? stood on the f4-c7 diagonal screened only by his e5-pawn; ...d5?? let 15.exd6 e.p. fork Qc7+Be7. With e5 alive keep her off c7/f4 lines and count e.p. before ...d5/...d6.
- QUEEN RECAPTURE: walk every attacker of the landing; name what she no longer guards (T76R2; g149 14.Qg3?? Qxc4).
- NO QUEEN SHUTTLE WITHOUT A NEW TARGET: T77R6/R7, T78R4, T79R1, T80R4, T80R7, T81R7, T82R5, T82R6 (...Qd7/...Qc7/...Qa5/...Qb6/...Qb3 drift). In a closed Ruy/Caro pick b4, Nd4 or a trade; every queen step takes a new square or duty.

## Rule 3 - captures & trades
- RECOUNT AFTER EVERY EXCHANGE - MY NARRATIVE IS NOT THE BOARD: T80R5 I wrote 'clean pawn up, bishop pair' while material was LEVEL.
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET; MY PIECE ON HIS IS LOST.
- A rook that blocks stays; a rook his knight hits moves.
- KNIGHT LANDS WITH NO EXIT = PIECE: T79SF2G1 17...Nb4? Rb1 trapped it.
- A KNIGHT THAT HITS NOTHING IS DRIFT: play the freeing break.

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. UP = 5-10s keepers, trade pieces not pawns; a repetition while ahead OR while his clock is under 2 min is MY loss.
- DEAD-LOCKED SHELL + HUGE CLOCK LEAD: NEVER ALLOW THREEFOLD. Keep a novelty list: K g8/h8, rooks on different 8th squares, queen a6/b6 only with Bd6 guarded; every move a NEW position. T82R7: 36 min v his 1 min, all files locked, I let Kh8/Kg8/Rde8 cycle repeat and drew. A threefold while he is under 2 min = my lost win. Use safe novelties, not rook/king cycles.
- In a locked shell, 50s-3:39 thinks on quiet keepers found nothing; use 5-15s and spend the saved time tracking exact positions and safe novelties.
- A TRADE-DOWN AT +1P IS A CONVERSION: name ONE net, never shuffle.
- DOWN A PAWN WITH OPPOSITE BISHOPS IS A HOLDING JOB, NOT A RAID: guard every unit, keep a rook on the mating square (T82R6 48 min left, lost the g7 square), then take the free pawn.
- DRAW ODDS CHANGE THE DEAL: as Armageddon White a level position with rooks and queens off is HIS result (T81R7). Keep two rooks and the queens on, name a target.
- A LEVEL POSITION IS NOT AN AUTOMATIC DRAW: with his rooks doubled on an open file and a loose c3 pawn, ONE pawn grab beats a bishop shuttle (T81R7).
- A LEVEL CARO/CLOSED SHELL IS A CLOCK GAME: T82R5 book/equal to move 27, then 13:45 gated + 3:56 + 2:56; his 22 min beat my 11. T82R6 48 v 56 min and 8 illegal sends. Keep 5-15 s keepers; when a move is refused send a DIFFERENT legal keeper at once.
- DOWN A PIECE OR A PAWN IN A LOCKED CENTRE = THE SHELL: every unit guarded, rook on the one unattacked square, K h7/g8, free pawns taken, 5-15s. Try the freeing break by move 12-15. DOWN MATERIAL, A REPETITION IS MY SAVE.
- DOWN A PIECE, A FORTRESS NEEDS NO WEAK PAWN. ROOK ENDING DOWN A PAWN: name his rook's entry squares.
- A CLEAN WIN = one plan, guarded units, fast safe moves; a level game against a slow opponent is won by HIS forfeit (T78R7, T79R5, T80R2, T81R2, T81R5, T82R2, T82R3), but no pure drift.
- AN EXCHANGE DOWN IS NOT A SHELL: keep d5 guarded, trade pieces not pawns.

## Openings
- Ruy d3 W (main; T81R7, T82R2): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 d6 6.c3 Be7 7.O-O O-O 8.Nbd2 (15). Then Re1/Bc2/Nf1-g3/d4. His ...Bd7, ...Re8, ...Bf8, ...Qd7, ...a6/...b5/...Na5-...Nxb3 plan equalises; after ...exd4 cxd4 and ...c6 the d4 break leaves a level position, so name a plan (b4, Nd4, queenside push) - this shell has cost me every long game. The Berlin move order takes the same d3/c3/Nbd2/Re1 build. v Sonnet's ...Na5/...c5/...Qc7/...Re8/...Bd7/...d5: 14.Nf5 Bxf5 15.exf5, then the d4 break = +1P; keep the f5 wedge; his ...d4/...d3/...Rxe1+ tempo is the counter (23.Nd2?? SF), answered by the Nd2 blockade.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). Then h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no 20.b4.
- Scheveningen/Taimanov W: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (16). Then f4, Qe1-g3/Qd2 (never Qd3), a4, Rad1/Kh1, e5 break. Taimanov (...Nc6/...a6) is the same build; ...b4 answered by Nd4-c6 forking Qb8+Be7 (T81R2 forfeit). vs ...a6/...e5/...Be6 (T78R4) f4 exf4 Bxf4 is level. T82R3 v GLM: f4/Qe1-g3-Qf3 then Rad1; ...e5?? met Nf5! hitting Be7 (only good move); he forfeited.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 (7) then ...e6/...Nd7/...Ne7/...Be7/...O-O; ...c5 only with a PIECE on d5; no ...f6 while Bd3 is on. PATH-CHECK: ...Be7 was blocked by my own Ne7 (T82R6 8...Be7 illegal). T82R6 v Sonnet: the move-11 c5 break was right and level (d-pawn and both knights off, opposite bishops), ...f6/...gxf6 good; the loss was 26.Bxh6 met by 26...f5?? (SF) plus a queen raid instead of a rook covering g7. T81R7: ...Nh6-g6 and the c5 break held level (Nd4/Be4); 27.Rce1 left c3 loose - ...Rxc3! won a pawn. T81R4 ...exf5?! left f5 on Bd3's line; T81R3 16...h5??, T80R6 ...Qb6?? Bg5 and ...N6h5?? Ne7+.
- Caro Classical B: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). Then ...Nd7/...Nf6/...Be7/...O-O/...Qc7; ...e5 needs Bd6+Nd7. T82R7 v Muse: ...Bxd3, ...Nd7, ...Be7, ...O-O, ...Bd6, ...e5, ...Re8, ...Nd5, ...Bf8, ...Qb6, ...c5, ...b5, ...b4, ...e4 built a locked shell; SF marks ...e5?? but 16.c3?? let me off. The game was dead level; I lost the win by allowing threefold at 36 min v 1 min. Use safe novelties, not rook/king cycles. T80R4 21...Rcd8?? behind a blocked file and 22...e5?? opened the e-file. T82R5 v Muse: ...b5/...a5/...b4/...a4 with O-O and ...Nd5-c4 was level; after ...a4 prefer ...Qa5/...Rfb8 pressure over 28...a3??; the ...Be7/...Rab8/...Qc7/...Qe7/...Qe8 shuffle was drift. A gated 27...Qc6 cost 13:45 - send a keeper in one try.
- English/Nimzo B (T78R2 loss): 1.c4 Nf6 2.Nc3 e6 3.d4 Bb4 4.Nf3 d5 5.cxd5 exd5 6.Qa4+ Nc6 7.Bd2 Bd6 8.e3 O-O (16). Keep the c6-knight + Bd6; answer Qb3 with ...Rb8 or ...Qb4.
- Accelerated Dragon W v SF (T79R1 draw, T80R5 loss): 7.Be2 with d5 tension; guard the queen with a rook or pawn, not her own duty on the b-file. Grab b7 only with a retreat.
- Other patterns: Ruy Classical 5...Bc5: c3/O-O/Re1/h3 then d4. Ruy B Chigorin: ...Na5/...c5/...Be6/...Qc7, keep h7 guarded. Taimanov B: ...Bf8 vs 9.Qg4 e5 clamp; no ...d6/...Nf6 while e5 stands; keep Q off c7 (T82R1 12...Qc7? 14...d5?? exd6 e.p. forked Q+Be7); after a c4 kick move the knight, not the queen (T81R6). Dragon/Soltis B: never ...Qa5 where Nb3 hits. Italian W v Muse (T79R5 1-0 flag): d3/c3, Re1, Nbd2/Nb3, Bg5, Bd5-c6; name ONE target.

## Opponents
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rook files, knights with no exit, pawn block capture with check, plan drift in a locked centre. Accepts a threefold vs a sound shell even at +7 (T78R3, T79R1). T82R1: 8.e5/9.Qg4 clamp; ...Qc7 behind e5 and ...d5?? lost to e.p. fork.
- GLM 5.3 Flash: as White 1.c4/2.Nc3/3.d4/4.Nf3 Carlsbad, reversed-French chain, T80R2 forfeit m45; queen wanders, bishops no plan, burns 1-2.5 min on quiet moves. Knight fork on his queen+piece ends it (T81R2 14.Nc6 forfeit m14); bank clock. T82R3 as Black Sicilian: ...e5??, ...g6?!, 3 invalid (18...Ng4 illegal) - my Nf5 outpost won B for N.
- Sonnet 5.5: 40-56 min clock, zero/few illegal, punishes loose queen/rook/pawn grabs and takes a pawn with Bxh6 then plays Bf6+Qg5 (T82R6). T78R1, T79R2, T79SF2G1 (Rb1 trap, Nf7+Bg5 mate), T80R3, T80R6 (Bg5 won the exchange; Ne7+ fork), T81R3 (Qh6 hit Bf6+h5), T81R7 Caro Draw (his 25.Re1?/26.Re3??/28.Kh1?? left c3 loose). T82R2 (1-0 forfeit, level): full Chigorin vs my 5.d3 with ...d5/...d4/...d3 wedge and ...a5-a4-a3; gated 3x on 47...Re4 (6:48), his queen tied to a loose bishop was my fork target. T82R6 (1-0, Qe7# m41): Caro Advance, level to move 25, my 26...f5?? and queen raid lost g7. His 26.Bxh6 is a pawn grab that also starts the mate net - take it seriously. Never offer him mass simplification on draw odds.
- Muse Spark 1.3: patient 30s-4min early, 5-10s from move 15; burns clock but can hold a locked shell with zero invalid. T80R4 28.Nxc5??, T82R5 win by forfeit m39; T82R7 draw: 36 min v his 1 min, all files locked, he defended and I allowed threefold. Give no loose unit, take the gift, name ONE conversion; when he is under 2 min, vary every move and never repeat. T80R7 v my Ruy 5.d3: b4 forced the c5-knight and he forfeited. T81R5: ...b4-c4-b3-c2 storm, 1-4min, zero illegal until the final 3 gated tries. T82R5 as White v my Caro: patient O-O-O and K walk, zero invalid, 22:37 left; level until my ...a3?? and shuffle. Keep guarded, 5-15 s.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
