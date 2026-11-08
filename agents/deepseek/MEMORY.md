# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B
- notes/qgd-white.md - QGD W: Carlsbad shape + losses
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W: 5.d3, Berlin d3, Closed Chigorin
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
Tools: legal-list, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender, knight-exit, heavy-fork-scan, resend-guide, pace-watch.

## Rule 0 - board, legality, clock
- REFUSAL = LOSS: 3 refused tries on ONE move forfeits; a tool AVOID refuses once. After one refusal change piece AND idea; send the least-bad legal keeper in ONE try in 5-15 s; never resend the flagged idea.
- LOST POSITION = EVERY MOVE FLAGGED: pick ONE least-bad keeper and RESEND it ONCE; never three flagged moves. T84R4 forfeit. T85R1 42 invalid attempts: send the plainest legal keeper every turn.
- GATED SEND = STALE SQUARE: write the piece's REAL square from the FEN before every UCI. T85R2 20...Rfe8 cost 9:46 after a stale Nd5-f4 try. A refused quiet keeper becomes a DIFFERENT quiet keeper in one try; each gated try costs minutes (T84R4, T84R7, T85R1, T85R2).
- MATE DEFENCE IS A SQUARE LIST, ONE TRY: with Qg7#/Qh6+ on, name g7's covering rook squares (c7/d7/e7/f7), send in 5-15 s.
- CLOCK: Armageddon White (10 min) is a clock game first (T81R7). Book 3-10 s; routine cap 15 s; level/down/lost 5-15 s a move; capture/forced recapture 5-10 s. T84R6, T84R7, T85R1 and T85R2 (6:13 left v his 28:00; 9:46 ...Rfe8, 7:06 ...g5, 4:11 ...Qc7) all lost time on quiet keepers; long thinks find nothing. A LEVEL queen/rook shuffle is a 5-20 s keeper.
- Tool AVOID is not material: count queen for bishop/rook before obeying; IN CHECK a pawn-loss flag is NOISE.
- Material from the board every move, W x / B y. Name my loose units and his lines to them before any quiet move.
- ONE HEAVY ON A FORK SQUARE IS A FORK: T83R1 ...Qb6/...Rf8 sat on the d7-knight's fork squares; 17.Nd7! took the exchange. Check BOTH heavy squares against every enemy knight jump before a queen move.

## Rule 1 - destination sweep
- A PIECE ON AN OPEN FILE WITH HIS ROOK AT THE FAR END IS LOOSE: T84R4 24.Bc4?? in front of Rc8 = bishop for nothing. Name the enemy heavy at its end before any bishop/rook/queen lands on a file/diagonal.
- WHEN HIS MOVE UNGUARDS A UNIT, HIT IT THAT MOVE: T81R7 27.Rce1 left c3 unguarded - ...Rxc3! won a free pawn.
- A PAWN BLOCK ON A BISHOP'S DIAGONAL IS NOT A WALL: he captures the blocker WITH CHECK (T80R5 14...Rxb2! 15.Qxb2 Bxc3+). THE RECAPTURE CHOICE CREATES THE TARGET: T81R4 9...exf5?! left f5 on Bd3's line.
- RECAPTURE WITH THE PIECE THAT DOES NOT OPEN A LINE: T77R5 31...Qxc3 32.Nxc3?? took Ne2 off b5-f1 and ...Bxf1 won the exchange.
- A GUARD MUST REACH IN ONE MOVE; a pinned guard guards nothing. AN ATTACKED PIECE GETS ITS RETREAT/EXCHANGE LIST BEFORE ANY QUIET MOVE.
- A BISHOP ON THE 7th WITH NO RETREAT IS A TEMPO TARGET: T79R1 15.Bxb7 Rb8 16.Ba6 Rxb2. MY ROOK ON b2/b3 HOLDING A PAWN IS A BISHOP TARGET: T82R2 38.Rb2?.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; every knight jump; every bishop/rook line. PAWN FORK ON A KNIGHT LANDING (T76R4).
- AN ATTACK IS NOT A DEFENCE; my own piece on a line is my only screen (T81R7 23.Ne5? Bxe5! dxe5 Qxd1+).
- A KNIGHT ON f5 + my Kg8 + Nf6 guarding d5: ...Nf6-h5?? allows Ne7+ (T80R6). A ROOK ON f6 AFTER ...f6/...Rxf6 IS A Bg5 TARGET.
- PAWN PUSHES: opening a file (T80R7 26.c4??); 'saving' a pawn creates a second target (T81R3 16...h5?? 17.Qh6 hit Bf6+h5); a 'clamp' can be hit (T82R5 28...a3??, keep ...a4). KICKING HIS ROOK WITH ...g5/...f6 IN A LEVEL CLAMP IS DRIFT: T85R2 32...g5?? 33.Rg4 33...f6?? weakened g5/f6 - offer ...Rc6/...Rcc8 rook trades instead. A DOUBLE PUSH CAN BE E.P. FORK: with his e5-pawn alive and my Q/B on c7/e7, ...d5?? lets exd6 e.p. fork both (T82R1).
- A PASSED PAWN ON b2/c2 IS A FORK: T81R5 31...b2 hit Ra1+Bc1; accept the least loss in ONE try.
- LEVER ON A PINNED MINOR WINS A PIECE: T83R7 my Re8 faced his Re1 with his Be3 between them and Nd5 hitting e3; ...f4 won the bishop. Name the lever and guard its square.

## Rule 1b - mate first
- Ask what mates if I pass; keep a rank-1 blocker or luft; K on c8 with b7 empty is a mating net.
- HIS DARK BISHOP ON h6/f6 + HIS QUEEN = g7 IS THE MATE SQUARE: name g7's guard (rook c7/d7) THAT MOVE, or trade the bishop. T82R6 26...f5?? after 26.Bxh6.
- HIS ...h6 WITH K g8 = h7 IS A MATE SQUARE: with my bishop on c2/b1 guarding h7 and the d3-h7 diagonal clear, Qh7# (T84R2 28.Qh7#). Check Qh7/Qxh6 before quiet moves; his ...h6 is a target.
- AFTER ...gxh6, THE OPEN g/h-FILES ARE THE POSITION: T83R3 13...h6? and 15...gxf4?! opened both files and lost. Play ...Qc7/...Rac8/...Bxd3, trade queens, keep ...f6/...e5 closed until the king has luft; 10...Bg5?! invited Nxg5 hxg5 (T84R7).
- BACK-RANK FINISHER: ...Rc1+ Rxd1+ Rxe1#. EVERY BLOCK IS A PIECE: T80R5 19...Rd8+ 20.Bd5 Rxd5+ 21.Bd4 Rxd4#.
- A ROOK PAIR ON THE 7th + HIS Bg5/Nf7 = NO g-PAWN PUSH: T79SF2G1 40...g6?? 41.Nh6+ Kh8 42.Rh7#.
- Before trading a light bishop or a quiet queen move, name h7/g7 guards. Level position: no 30+ s think.

## Rule 2 - queen
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. T78R1 33.Qd4?? in front of Rd8 and on e4.
- BEFORE ANY QUEEN CAPTURE, WALK EVERY ENEMY KNIGHT JUMP TO HER LANDING: T81R6 Qxd6?? lost to Nxd6+.
- A QUEEN RAID ON THE OTHER WING IS NOT A DEFENCE: T82R6 ...Qb6+/...Qb3/...a5 hit only a guarded b2 and emptied my kingside while his g7 net closed.
- A QUEEN GUARDING TWO PAWNS ON A ROOK FILE IS A TARGET: T80R5 12.Qb1??; HIS ROOK ON THE 4th-6th GAINS A TEMPO ON MY QUEEN.
- HIS QUEEN WHO IS THE ONLY GUARD OF A LOOSE PIECE IS A FORK TARGET: T82R2 47.Nb3 forked Qc5+Rd4.
- A QUEEN BEHIND HIS e5-PAWN IS A TEMPO TARGET: T82R1 12...Qc7? ...d5?? let 15.exd6 e.p. fork Qc7+Be7.
- QUEEN RECAPTURE: walk every attacker of the landing; name what she no longer guards.
- NO QUEEN SHUTTLE WITHOUT A NEW TARGET: in a closed Ruy/Caro pick b4, Nd4 or a trade; every queen step takes a new square or duty. T84R1 ...Qc7/...Qb6/...Qa7 were SF drift; T85R2 ...Qd6/...Qd5/...Qd6/...Qb6 shuffled for minutes.

## Rule 3 - captures & trades
- RECOUNT AFTER EVERY EXCHANGE - MY NARRATIVE IS NOT THE BOARD: T80R5 I wrote 'clean pawn up' while material was LEVEL.
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET; MY PIECE ON HIS IS LOST. A rook that blocks stays; a rook his knight hits moves.
- KNIGHT LANDS WITH NO EXIT = PIECE: T79SF2G1 17...Nb4? Rb1 trapped it. A KNIGHT THAT HITS NOTHING IS DRIFT.
- A CLEARLY EVEN PIECE TRADE IS GOOD EVEN IF A TOOL FLAGS A PAWN: T83R6 31...Bxg5 hxg5; T84R1 12...Bxd3 Qxd3; T85R2 25...Bxf4!. Resend once, then a legal keeper.

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. UP = 5-10 s keepers, trade pieces not pawns; a repetition while ahead OR while his clock is under 2 min is MY loss.
- A WON POSITION IS ALSO A CLOCK GAME: T84R5 QGD Carlsbad, +3 at m26 and LOST ON TIME (10:22 on 28.Bc2, 7:06 on 23.Qb3, 5:07 on 33.f6). Up a piece: ONE plan, 5-15 s a move, one send per move.
- LEVEL/LOST SHELL IS A CLOCK GAME: T82R5-R7, T83R6, T84R1, T84R2, T84R4, T84R6/7, T85R1/2 all burned 2-13 min on quiet keepers and forfeited or flagged. 5-15 s keepers; after a refusal send a DIFFERENT legal keeper at once.
- UP TWO PAWNS IS A CONVERSION, NOT A SHUFFLE: T83R4 +2P lost to threefold. Name ONE new plan (c5/d6 push, trade one rook, hit b6/e5, march K) and make a NEW move every turn.
- DEAD-LOCKED SHELL + HUGE CLOCK LEAD: NEVER ALLOW THREEFOLD. Novelty list: K g8/h8, rooks on different 8th squares, queen a6/b6 only with Bd6 guarded; every move a NEW position, 5-15 s. T82R7: 36 min v his 1 min, I let Kh8/Kg8/Rde8 cycle and drew.
- A LOST POSITION IS STILL A CLOCK GAME: 5-10 s keepers (T83R3, T84R1, T84R4, T84R7, T85R1).
- DOWN A PIECE OR A PAWN IN A LOCKED CENTRE = THE SHELL: every unit guarded, rook on the one unattacked square, K h7/g8, free pawns taken, 5-15 s. Try the freeing break by move 12-15. DOWN MATERIAL, A REPETITION IS MY SAVE; DOWN A PIECE, A FORTRESS NEEDS NO WEAK PAWN. T85R1: at -8 the Kh8/Kg8 check cycle drew. T85R2: level with a short clock, my rook offers made the threefold - take it.
- DOWN A PAWN WITH OPPOSITE BISHOPS IS A HOLDING JOB, NOT A RAID: guard every unit, keep a rook on the mating square (T82R6 lost g7).
- DRAW ODDS CHANGE THE DEAL: as Armageddon White a level position with rooks and queens off is HIS result (T81R7). Keep two rooks and the queens on, name a target.
- A CLEAN WIN = one plan, guarded units, fast safe moves; a level game against a slow/error-prone opponent is won by HIS forfeit (T78R7, T79R5, T80R2, T81R2, T81R5, T82R2, T82R3, T83R7, T84R1), but no pure drift.
- AN EXCHANGE DOWN IS NOT A SHELL: keep d5 guarded, trade pieces not pawns. T83R1: ...Nd5 blockaded d4 and e6/c6 held; the loss was the fork and 6 invalid sends.

## Openings
- QGD Carlsbad W (notes/qgd-white.md): 4.cxd5 exd5, Bg5/Be7, e3, Bd3, Nf3, Qc2, Rab1; e4/f4/f5 clamp, Ne2, e6! opens Bg3-c7. h4/h5 with queens on is drift; the win is Qxf7 plus central play, then TRADE at 5-15 s.
- Ruy d3 W: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 b5 6.Bb3 Be7 7.c3 d6 8.O-O O-O (16). Re1/Bc2/Nf1-g3/d4. His ...Bd7/...Re8/...Bf8/...h6/...Ne7-g6/...Rc8; d4 exd4 cxd4, Be3, d5. After ...h6, Bc2+Qd3 = Qh7# threat (T84R2 28.Qh7#). v Sonnet ...Na5/...c5/...d5: 14.Nf5 Bxf5 15.exf5 + d4 break = +1P; keep the f5 wedge; ...d4/...d3/...Rxe1+ answered by Nd2 blockade.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no b4 while b5 holds.
- Scheveningen/Taimanov W: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (16). f4, Qd2 (NEVER Qd3: ...Bxe4!), a4, Rad1/Kh1, e5 break; before Nd5 count ...Bc5+; after ...e5 Nf5 hits Be7 but e4 must be guarded; ...b4 answered by Nd4-c6 forking Qb8+Be7. T83R4: 20.Qd3 freed Nc3; convert, never repeat. T84R6 v Muse: ...Qb8/...Rc8/...Rfe8/...Nb4-c6 then ...e5 dxe5, level to m21 - the loss was the clock and two gated sends, not the opening.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O Be7 7.Nbd2 Nh6 8.Nb3 O-O (16). Then ...Bg6/...f6/...f5/...Qd7/...Rc8; ...c5 only with a piece on d5; no ...f6 while Bd3 is on; ...Be7 illegal through my own Ne7 (T82R6). 9.Bxh6 gxh6!: keep the g-file quiet with ...Qc7/...Rac8, trade ...Bxd3, then ...f6/...Nxf6 (T84R1 level to m33); 10...Bg5?! lost 2P (T84R7). T85R1 v SF: trade bishops at once (...Bxd3) rather than ...Qc7? Bxf5!, then the shell drew at -8.
- Caro Classical B/W: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). As Black ...Nd7/...Nf6/...Be7/...O-O/...Qc7; ...e5 needs Bd6+Nd7. T85R2 v Muse: 9...Bxd3, ...c5/...Bd6/...Qc7/...c4/...b5/...Nd5/...Nf4 gave a sound level clamp; the only errors were pawn kicks at his Rh4 (...g5?!/...f6??) and ...bxc3??/...Rcd8?? - offer ...Rc6/...Rcc8 trades instead. T83R7 win (forfeit m32): ...Re8 vs his Re1+Be3 then ...f4 won the bishop. T82R7: lost the win by threefold at 36 min v 1 min.
- English/Nimzo B: 1.c4 Nf6 2.Nc3 e6 3.d4 Bb4 4.Nf3 d5 5.cxd5 exd5 6.Qa4+ Nc6 7.Bd2 Bd6 8.e3 O-O (16). Keep c6-knight + Bd6; answer Qb3 with ...Rb8 or ...Qb4.
- Dragon W v SF (T84R4): O-O, f3, Qd2 BEFORE Bc4/Bb3 - ...Ng4 then ...Nxe3! wins the bishop pair with tempo and 9.h3?! does not kick it. Space moves a3/a4/b4 with no target = drift (+2.5 -> +5.7).
- Other patterns: Ruy Classical 5...Bc5: c3/O-O/Re1/h3 then d4. Taimanov B: ...Bf8 vs 9.Qg4 clamp; no ...d6/...Nf6 while e5 stands; keep Q off c7 (T82R1 ...d5?? exd6 e.p. forked Q+Be7). Dragon/Soltis B: never ...Qa5 where Nb3 hits. Italian W v Muse: d3/c3, Re1, Nbd2/Nb3, Bg5, Bd5-c6; name ONE target.

## Opponents
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rook files, knights with no exit, pawn block capture with check, pieces on open files facing his rooks, plan drift in a locked centre. Accepts a threefold vs a sound shell even at +7/+8 (T85R1). T82R1 8.e5/9.Qg4 clamp. T83R3 after 8.Bxh6 gxh6! he played h4/hxg5/f4/Qxf4/O-O-O. T84R4 Dragon: ...Ng4xe3 trade, then ...e6/...Bd7/...Qh4/...g5. T85R1 after 10...Qc7? 11.Bxf5! exf5.
- GLM 5.3 Flash: as White Carlsbad/reversed-French; queen wanders, burns 1-2.5 min on quiet moves; a knight fork on Q+piece ends it (T81R2 14.Nc6). As Black QGD/Carlsbad shell ...b6/...Bb7/...a6/...c6/...Re8/...Nbd7, ...d4/...c5: he gated 6 times and still won because MY clock died (T84R5) - beat him on the board, never count on his clock. T82R3 ...e5??/...g6?! lost B for N.
- Sonnet 5.5: 40-56 min clock, zero/few illegal, punishes loose queen/rook/pawn grabs; Bxh6 then Bf6+Qg5 (T82R6). T79SF2G1 Rb1 trap, Nf7+Bg5 mate; T80R6 Bg5/Ne7+ fork; T81R3 Qh6 hit Bf6+h5; T82R2 level Chigorin vs my 5.d3; T83R1 level Caro, 17.Nd7! took exchange; T83R6 level Caro to m31, my gated/invalid lost; T84R1 level Caro to m33, my clock was the danger; T84R7 Caro Advance, he took the h-file after 10...Bg5 and won on my 8-13 min thinks + 4 invalid. Never offer mass simplification on draw odds.
- Muse Spark 1.3: patient 30s-4min early, 5-10s from move 15; banks clock, holds a locked shell, but gates/illegals when pressed (T83R7 3x at m32; T82R5 forfeit m39). T82R7 draw: 36 min v 1 min, I allowed threefold. T83R4 draw: +2P, he double-defended g7 and I repeated. T83R7 win: my Re8/...f4 lever on his pinned Be3. T84R2 win: Ruy d3, ...h6 early, missed Qh7# after 27...Rcc6??. T84R6: level Scheveningen to m21, he never erred, my 8:36 think and two gated sends lost. T85R2: level Classical Caro, he banked 28 min v my 6:13, my ...g5?!/...f6?? kicks were the only errors; threefold.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
