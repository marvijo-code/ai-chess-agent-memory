# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B
- notes/qgd-white.md - QGD W: Carlsbad clamp, Colle drift, losses
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W: 5.d3, Berlin d3, Closed Chigorin, T86R2 draw
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
Tools: legal-list, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender, knight-exit, heavy-fork-scan, resend-guide, pace-watch, check-ledger.

## Rule 0 - board, legality, clock
- REFUSAL = LOSS: 3 refused tries on ONE move forfeits. READ THE REASON. A reason naming a PIECE, QUEEN, ROOK, EXCHANGE or MATE loss is REAL: send ONE different plainly sound keeper, 5-15 s. A reason naming ONLY A PAWN, or any refusal of a move that GIVES CHECK or starts a mate net, is NOISE: RESEND THE SAME UCI once (it goes through), 5-10 s. NEVER a variant of the same idea, never a third different move. T85R5 m30 Nh5+ mate net flagged as 1 pawn; T86R2 Qd6/Qa7 pawn flags resend passed.
- GATED SEND = STALE SQUARE: write the piece's REAL square from the FEN before every UCI. T85R2 ...Rfe8 cost 9:46 after a stale Nd5-f4 try.
- LOST POSITION = EVERY MOVE FLAGGED: pick ONE least-bad keeper and RESEND it ONCE.
- MATE DEFENCE IS A SQUARE LIST, ONE TRY: with Qg7#/Qh6+ on, name g7's covering rook squares (c7/d7/e7/f7), send in 5-15 s.
- CLOCK: level/down/lost = 5-15 s, ONE send. T86R3 v GLM: dead-level shell, my queen spent 5:18 on ...Qc7, 3:20 on ...Qb6 and 8:55 on ...Qb4 (17+ min of quiet queen steps SF marks ??/?!); ended 27:22 v his 50:50 and only HIS forfeit saved me. The written scan is the check; longer looks found nothing. Same class T84R5, T85R4, T86R2.
- Tool AVOID is not material: count queen for bishop/rook before obeying; in CHECK or while GIVING CHECK a pawn-loss flag is NOISE.
- Material from the board every move, W x / B y. Name my loose units and his lines to them before any quiet move.
- ONE HEAVY ON A FORK SQUARE IS A FORK: check BOTH heavy squares against every enemy knight jump before a queen move.

## Rule 1 - destination sweep
- A ROOK RETREAT SQUARE IN FRONT OF HIS ADVANCED PAWN IS A PAWN-FORK SQUARE: T86R2 25.Rd3?? ...e4! forked Rd3+Nf3. Before landing a rook on the d/e/f-file, list his one-step pawn pushes to that square.
- A PIECE ON AN OPEN FILE WITH HIS ROOK AT THE FAR END IS LOOSE: T84R4 24.Bc4?? in front of Rc8.
- WHEN HIS MOVE UNGUARDS A UNIT, HIT IT THAT MOVE: T81R7 27.Rce1 left c3 - ...Rxc3!.
- A PAWN BLOCK ON A BISHOP'S DIAGONAL IS NOT A WALL: T80R5 14...Rxb2! 15.Qxb2 Bxc3+.
- RECAPTURE WITH THE PIECE THAT DOES NOT OPEN A LINE: T77R5 31...Qxc3?? 32.Nxc3?? ...Bxf1 won the exchange.
- A GUARD MUST REACH IN ONE MOVE; a pinned guard guards nothing. AN ATTACKED PIECE GETS ITS RETREAT/EXCHANGE LIST BEFORE ANY QUIET MOVE.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; every knight jump; every bishop/rook line. AN ATTACK IS NOT A DEFENCE; my own piece on a line is my only screen.
- PAWN PUSHES: opening a file (T80R7 26.c4??); 'saving' a pawn creates a second target (T81R3 16...h5?? 17.Qh6); a 'clamp' can be hit (T82R5 28...a3??). KICKING HIS ROOK WITH ...g5/...f6 IN A LEVEL CLAMP IS DRIFT (T85R2 32...g5?? 33.Rg4). A DOUBLE PUSH CAN BE E.P. FORK (T82R1 ...d5?? exd6).
- LEVER ON A PINNED MINOR WINS A PIECE: T83R7 ...f4 won Be3.

## Rule 1b - mate first
- Ask what mates if I pass; keep a rank-1 blocker or luft; K on c8 with b7 empty is a mating net.
- HIS DARK BISHOP ON h6/f6 + HIS QUEEN = g7 IS THE MATE SQUARE: name g7's guard (rook c7/d7) THAT MOVE, or trade the bishop. T82R6 26...f5?? after 26.Bxh6.
- HIS ...h6 WITH K g8 = h7 IS A MATE SQUARE: with my bishop on c2/b1 guarding h7 and the d3-h7 diagonal clear, Qh7# (T84R2).
- HIS BISHOP ON f2/g3 + HIS QUEEN ON RANK 1 OR e1 = Qg1#/Qh2#: count it every move and answer with CHECKS only (T86R2 69...Bf2, only Qc8+ survived).
- AFTER ...gxh6, THE OPEN g/h-FILES ARE THE POSITION: T83R3 13...h6? and 15...gxf4?! lost. Play ...Qc7/...Rac8/...Bxd3, trade queens, keep ...f6/...e5 closed until the king has luft.
- BACK-RANK FINISHER: ...Rc1+ Rxd1+ Rxe1#. EVERY BLOCK IS A PIECE: T80R5 19...Rd8+ 20.Bd5 Rxd5+ 21.Bd4 Rxd4#.

## Rule 2 - queen
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. T78R1 33.Qd4?? in front of Rd8.
- BEFORE ANY QUEEN CAPTURE, WALK EVERY ENEMY KNIGHT JUMP TO HER LANDING: T81R6 Qxd6?? lost to Nxd6+.
- A QUEEN RAID ON THE OTHER WING IS NOT A DEFENCE: T82R6 ...Qb6+/...Qb3/...a5 emptied my kingside.
- HIS QUEEN WHO IS THE ONLY GUARD OF A LOOSE PIECE IS A FORK TARGET: T82R2 47.Nb3.
- QUEEN RECAPTURE: walk every attacker of the landing; name what she no longer guards.
- NO QUEEN SHUTTLE WITHOUT A NEW TARGET: T85R2 ...Qd6/...Qd5/...Qd6/...Qb6; T85R5 ...Qb6/...Qc7/...Qb6/...Qa5; T86R3 the ...Qd7-c7-b6-b4 tour took 17 min and SF marks the last three ??/?!. In a closed shell give her ONE new duty (back a lever, guard a break square) or trade her. A queen on b4/b6 'pressing' d4/a4 is only good if she takes something; T86R3 she never did and she blocked my own ...b5.

## Rule 3 - captures & trades
- RECOUNT AFTER EVERY EXCHANGE - MY NARRATIVE IS NOT THE BOARD: T80R5 I wrote 'clean pawn up' while material was LEVEL.
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET; MY PIECE ON HIS IS LOST.
- KNIGHT LANDS WITH NO EXIT = PIECE: T79SF2G1 17...Nb4? Rb1 trapped it. A KNIGHT THAT HITS NOTHING IS DRIFT (T85R5 17...Nb6).
- A CLEARLY EVEN PIECE TRADE IS GOOD EVEN IF A TOOL FLAGS A PAWN: T83R6 31...Bxg5 hxg5; T84R1 12...Bxd3 Qxd3; T85R2 25...Bxf4!. Resend once, then a legal keeper.
- WHICH PIECE RECAPTURES IS THE POSITION: T85R5 14.exf6+ Bxf6? turned my dark bishop into a shuttle; ...Nxf6 keeps it home.

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. UP = 5-10 s keepers, trade pieces not pawns; a repetition while ahead OR while his clock is under 2 min is MY loss.
- A WON POSITION IS ALSO A CLOCK GAME: T84R5 +3 at m26 and LOST ON TIME (10:22 Bc2, 7:06 Qb3, 5:07 f6). Up a piece: ONE plan, 5-15 s a move.
- LEVEL/LOST SHELL IS A CLOCK GAME: T82R5-R7, T83R6, T84R1/2/4/6/7, T85R1/2/4, T86R2, T86R3 all burned 2-13 min on quiet keepers. 5-15 s keepers; after a refusal a DIFFERENT legal keeper at once.
- A DEAD-LEVEL SHELL IS WON BY HIS FORFEIT, NEVER BY MY QUEEN TOUR: T86R3 v GLM, level to m26 with 30 min banked, I spent 8:55 on ...Qb4 and fell to 27:22 v his 50:50; he forfeited. Keep every unit guarded, make a NEW safe keeper every turn (rook to a new 8th square, K h7/g8, a guarded ...Rad8), never minutes on one quiet move.
- ...f6 IN A BLOCKED CARO/QGD SHELL NEEDS A CONCRETE PURPOSE: T86R3 20...f6? took e5/g5 from my own pieces and weakened e6/g6 with no break behind it (SF ?). Only with ...e5/...f5/...Nxf6 to follow, or to stop a knight landing.
- DOWN MATERIAL WITH QUEENS ON AND HIS MATE NET SHOWING: ONLY CHECKS SAVE. T86R2 Qc8+/Qf5+ perpetual at 2:56 v 53:31.
- UP TWO PAWNS IS A CONVERSION, NOT A SHUFFLE: T83R4 +2P lost to threefold. Name ONE new plan and make a NEW move every turn.
- DOWN A PIECE OR A PAWN IN A LOCKED CENTRE = THE SHELL: every unit guarded, rook on the one unattacked square, K h7/g8, 5-15 s. DOWN MATERIAL, A REPETITION IS MY SAVE.
- A CLEAN WIN = one plan, guarded units, fast safe moves; a level game against a slow/error-prone opponent is won by HIS forfeit (T78R7, T79R5, T80R2, T81R2, T81R5, T82R2, T82R3, T83R7, T84R1, T86R3), but no pure drift.
- AN EXCHANGE DOWN IS NOT A SHELL: keep d5 guarded, trade pieces not pawns.

## Openings
- QGD Carlsbad W (notes/qgd-white.md): the real clamp is c4 and the exchange on d5, then Bg5 against ...Be7, with e3, Bd3, Nf3, Qc2 and Rab1; the e4/f4/f5 clamp with Ne2; e6! opens Bg3-c7. The Colle-style build WITHOUT c4 gave nothing (T85R4). h4/h5 with queens on is drift; the win is Qxf7 plus central play.
- Ruy d3 W: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 b5 6.Bb3 Be7 7.c3 d6 8.O-O O-O (16). Re1/Bc2/Nf1-g3/d4. His ...Bd7/...Re8/...Bf8/...h6/...Ne7-g6/...Rc8; d4 exd4 cxd4, Be3, d5. After ...h6, Bc2+Qd3 = Qh7# threat (T84R2). T86R2 Breyer: level to m20; the loss was my clock plus 25.Rd3?? ...e4! fork; his ...d5/...dxe4 trades were fine.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no b4 while b5 holds.
- Scheveningen/Taimanov W: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (16). f4, Qd2 (NEVER Qd3: ...Bxe4!), a4, Rad1, Kh1, e5 break; before Nd5 count ...Bc5+; after ...e5 Nf5 hits Be7 but e4 must be guarded; ...b4 answered by Nd4-c6 forking Qb8+Be7.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O Be7 7.Nbd2 Nh6 8.Nb3 O-O (16). Then ...Bg6/...f6/...f5/...Qd7/...Rc8; ...c5 only with a piece on d5; no ...f6 while Bd3 is on. 9.Bxh6 gxh6!: keep the g-file quiet with ...Qc7/...Rac8, trade ...Bxd3, then ...f6/...Nxf6; 10...Bg5?! lost 2P. T85R1 v SF: trade bishops at once (...Bxd3), then the shell drew at -8. T85R5: with his Re1 count e6's guards before any break that leaves e6 loose.
- Caro Classical B/W: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). As Black ...Nd7/...Nf6/...Be7/...O-O/...Qc7; ...e5 needs Bd6+Nd7. T85R2 v Muse: trade bishops early, then ...c5/...Bd6/...Qc7/...c4/...b5 gave a sound level clamp; the only errors were pawn kicks at his Rh4 and ...bxc3??/...Rcd8??. T83R7 win: ...Re8 vs his Re1+Be3 then ...f4 won the bishop.
- English/Nimzo B: meet c4/Nc3/g3/Bg2 with a QGD reversed-Tarrasch: ...e6, ...d5, ...Be7, ...O-O, ...Re8, ...Nbd7, ...c6; keep d5 guarded, no pawn kicks, 5-15 s keepers. T86R3 v GLM level to m26. Watch his Na4-c5 hitting b7/d7; trade dark bishops or play ...Bd7/...Ne6/...Rad8. Answer Qa4+ with ...Nc6 or ...Bd6; meet Qb3 with ...Rb8 or ...Qb4.
- Other patterns: Ruy Classical 5...Bc5: c3/O-O/Re1/h3 then d4. Taimanov B: ...Bf8 vs 9.Qg4 clamp; no ...d6/...Nf6 while e5 stands; keep Q off c7. Dragon/Soltis B: never ...Qa5 where Nb3 hits. Dragon W v SF: O-O, f3, Qd2 BEFORE Bc4/Bb3 - ...Ng4 then ...Nxe3! wins the bishop pair. Italian W v Muse: d3/c3, Re1, Nbd2/Nb3, Bg5, Bd5-c6; name ONE target.

## Opponents
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rook files, knights with no exit, pieces on open files facing his rooks, plan drift. Accepts a threefold vs a sound shell even at +7/+8. T84R4 Dragon: ...Ng4xe3 trade, then ...e6/...Bd7/...Qh4/...g5.
- GLM 5.3 Flash: as White the English g3 build (c4, Nc3, g3, Bg2; then d3, Nf3, short castle; Re1, d4, Bf4, Rb1, Na4-c5; h4-h5 clamp); as Black QGD Carlsbad and Taimanov/Modern. Solid on the board; 3+ illegal tries, 1-9 min on quiet moves; forfeits after 3 invalid replies. T86R3: level blocked reversed-Tarrasch, he never cracked it and forfeited with 50+ min left; my 27 min was the only danger. Beat him on the board, never count on his clock: T85R4 he won because MY clock died.
- Sonnet 5.5: 40-56 min clock, zero/few illegal, punishes loose queen/rook/pawn grabs; Bxh6 then Bf6+Qg5. T86R2 Ruy d3/Breyer: level to m20, then his ...d5/...dxe4 trades and 25...e4! pawn fork made him -2; the perpetual still drew (2:56 v 53:31). Never offer mass simplification on draw odds.
- Muse Spark 1.3: patient 30s-4min early, 5-10s from move 15; banks clock, holds a locked shell, but gates/illegals when pressed. T85R2: level Classical Caro, my ...g5?!/...f6?? kicks were the only errors; threefold.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
