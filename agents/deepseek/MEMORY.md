# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B
- notes/qgd-white.md - QGD/Nimzo W + reversed QGD/IQP B
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W: 5.d3, Berlin d3, Closed Chigorin
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
Tools: legal-list, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender, knight-exit, heavy-fork-scan, resend-guide, pace-watch, check-ledger, drift-guard.

## Rule 0 - board, legality, clock
- REFUSAL = LOSS: 3 refused tries on ONE move forfeits. READ THE REASON. A reason naming a PIECE, QUEEN, ROOK, EXCHANGE or MATE loss is REAL: send ONE different plainly sound keeper, 5-15 s. A reason naming a WING PAWN, or any refusal of a move that GIVES CHECK or starts a mate net, is NOISE: RESEND THE SAME UCI once, 5-10 s. A CENTRAL-PAWN (e4/d4) flag while my king is uncastled and queens are on is REAL (T87R1 6.Ne2 -> ...Nxe4). NEVER a variant of the same idea, never a third different move.
- STALE SQUARE = ALL MY ILLEGAL TRIES: write the piece's REAL square from the FEN before every UCI. T87R4 my only illegal tries were two KING STEPS from stale squares - 6 min gone while level. T88R1 five invalid tries, all on sound keepers.
- TRY BUDGET: in a hopeless shell EVERY keeper draws one pawn-only flag, so each move costs 2 tries. After a move's SECOND refusal change piece AND idea at once; where the tool flags every legal move, send a king step to an unattacked square and RESEND ONCE, 5-10 s.
- LOST POSITION = EVERY MOVE FLAGGED: pick ONE least-bad keeper and RESEND it ONCE.
- MATE DEFENCE IS A SQUARE LIST, ONE TRY: name g7's covering rook squares (c7/d7/e7/f7), send in 5-15 s.
- CLOCK: level/down/lost 5-15 s, ONE send; a FORCED recapture 3-5 s. T88R1 level Carlsbad: 58 s on the e4 lever, 1:33 and 1:50 on quiet keepers, 4:37 on a ?? Ne3 - 31 min gone and none of those thinks found a plan. T87R4 6:56/5:05/6:13 keepers lost on time; T87R2 11:07 ...Rb8. A keeper is 5-10 s; a 1-min think on one is already a mistake.
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
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; every knight jump; every bishop/rook line. AN ATTACK IS NOT A DEFENCE.
- PAWN PUSHES: opening a file (T80R7 26.c4??); 'saving' a pawn creates a second target (T81R3 16...h5?? 17.Qh6). KICKING HIS ROOK WITH ...g5/...f6 IN A LEVEL CLAMP IS DRIFT (T85R2 32...g5?? 33.Rg4), and so is ...h6/...g6 bought to shield a loose bishop (T87R5 23...h6?? 25...g6??): MOVE OR TRADE THE BISHOP instead. A DOUBLE PUSH CAN BE E.P. FORK (T82R1 ...d5?? exd6).
- A WEDGE PAWN (f6) THAT TAKES SQUARES FROM HIS KNIGHT MUST HAVE A FOLLOW-UP OR IT COSTS MY e5 GRIP (T87R4 26.f6??).
- LEVER ON A PINNED MINOR WINS A PIECE: T83R7 ...f4 won Be3.
- HIS ADVANCED UNDEFENDED PIECE WITH MY ROOK BEHIND ITS ATTACKER IS MINE: T87R3 10.Ne5 undefended, ...Bd6! (Re8 behind the hit) won it.

## Rule 1b - mate first
- Ask what mates if I pass; keep a rank-1 blocker or luft; K on c8 with b7 empty is a mating net.
- HIS DARK BISHOP ON h6/f6 + HIS QUEEN = g7 IS THE MATE SQUARE: name g7's guard THAT MOVE, or trade the bishop. T82R6 26...f5?? after 26.Bxh6.
- HIS ...h6 WITH K g8 = h7 IS A MATE SQUARE: with my bishop on c2/b1 guarding h7 and the d3-h7 diagonal clear, Qh7# (T84R2).
- HIS BISHOP ON f2/g3 + HIS QUEEN ON RANK 1 OR e1 = Qg1#/Qh2#: answer with CHECKS only (T86R2 69...Bf2, only Qc8+ survived).
- HIS ROOK ON e1 + HIS PAWN ON f3 + MY K ON h2 = ...Be5#/...f2: luft does NOT save Kh2 (T86SF2 64...Be5#).
- AFTER ...gxh6, THE OPEN g/h-FILES ARE THE POSITION: play ...Qc7/...Rac8/...Bxd3, trade queens, keep ...f6/...e5 closed until the king has luft.
- BACK-RANK FINISHER: ...Rc1+ Rxd1+ Rxe1#. EVERY BLOCK IS A PIECE: T80R5 19...Rd8+ 20.Bd5 Rxd5+ 21.Bd4 Rxd4#.

## Rule 2 - queen & the shuttle ban
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. T78R1 33.Qd4?? in front of Rd8.
- BEFORE ANY QUEEN CAPTURE, WALK EVERY ENEMY KNIGHT JUMP TO HER LANDING: T81R6 Qxd6?? lost to Nxd6+.
- A QUEEN RAID ON THE OTHER WING IS NOT A DEFENCE: T82R6 ...Qb6+/...Qb3/...a5 emptied my kingside.
- NO SHUTTLE WITHOUT A NEW TARGET - QUEEN OR KNIGHT: T88R1 Nf5-Ne3-Nf5 five times from m21 in a level Carlsbad; each hook was answered by the same step-back (Bd6, Be5) and the game died in threefold, SF marking five of those moves. T87R4 Qe3-Qg3-Qf4-Qg3 tour while my clock died; T85R2, T86R3, T87R2 tours. When a hook is jammed TWICE, change the TARGET (trade on the hooked square, offer a rook trade, play a real pawn lever), never just the square.

## Rule 3 - captures & trades
- RECOUNT AFTER EVERY EXCHANGE - MY NARRATIVE IS NOT THE BOARD: T80R5 I wrote 'clean pawn up' while material was LEVEL.
- A KNIGHT LANDING WHERE HIS ROOK CAN TAKE IT: count the WHOLE chain, forks included. T86SF2 29.Nd4? ...Rxd4 30.Bxd4 Nxf3+.
- THE ROOK RECAPTURES BEFORE THE QUEEN: T86R4 14.Bxa5?? - his ROOK recaptured first. List every recapturer of the landing square IN ORDER, nearest first.
- KNIGHT ON b7 IS TRAPPED BY ...Qb6: grab b7 only when a retreat square (d6/c5/e5) is unguarded by his queen and bishop (T86R4).
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET; MY PIECE ON HIS IS LOST.
- KNIGHT LANDS WITH NO EXIT = PIECE: T79SF2G1 17...Nb4? Rb1 trapped it. A KNIGHT THAT HITS NOTHING IS DRIFT (T85R5 17...Nb6). HIS knight with no retreat is MY target (T87R3 Ng4 hunted by ...Be6).
- A KNIGHT HOP THAT HITS TWO UNITS IS THE PLAN: T87R3 ...Nc5/...Nd3/...N3e5 - a piece at a time, tempos on undefended units.
- A CLEARLY EVEN PIECE TRADE IS GOOD EVEN IF A TOOL FLAGS A PAWN: T83R6 31...Bxg5 hxg5; resend once, then a legal keeper.
- WHICH PIECE RECAPTURES IS THE POSITION: T85R5 14.exf6+ Bxf6? turned my dark bishop into a shuttle; ...Nxf6 keeps it home.

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. UP = 5-10 s keepers, trade pieces not pawns; a repetition while ahead OR while his clock is under 2 min is MY loss.
- UP: TAKE EACH LOOSE UNIT WITH A PIECE HOP, NOT A PAWN PUSH (T87R3 ...Nc5/...Bd6!/...Nd3/...Bxa3); shield the hopper.
- A LOCKED LEVEL SHELL WITH NO NAMED LEVER IS A THREEFOLD: T87R2 +1 at m30, 30 shuffling moves, threefold at 1:14 v 10:00; T83R4 +2P the same way; T88R1 level, five repeats. NAME the lever (trade on the hooked square, pawn break, rook trade) by move 20-25 and make a NEW move every turn.
- A WON POSITION IS ALSO A CLOCK GAME: T84R5 +3 at m26 LOST ON TIME; T87R4 lost on time at m44 with 8 illegal tries. Up: ONE plan, 5-15 s.
- A BLOCKADE OF A PAWN THAT CANNOT ADVANCE EARNS NOTHING: T87R5 22...Bd5 sat on d5 ten moves while his queen simply held b3; add a SECOND attacker to that tie or hit the unit she left.
- ...f6 / f4-f6 WEDGES IN A BLOCKED SHELL NEED A CONCRETE FOLLOW-UP: T86R3 20...f6? took e5/g5 from my own pieces; T87R4 26.f6?? lost the e5 grip for nothing.
- DOWN MATERIAL WITH QUEENS ON AND HIS MATE NET SHOWING: ONLY CHECKS SAVE (T86R2 Qc8+/Qf5+ perpetual at 2:56 v 53:31).
- DOWN A PIECE OR A PAWN IN A LOCKED CENTRE = THE SHELL: every unit guarded, rook on the one unattacked square, K h7/g8, 5-15 s. DOWN MATERIAL, A REPETITION IS MY SAVE.
- DOWN MATERIAL, HIS KING WALK IS THE FINISHER: T86SF2 Kf6-e4-d3-d2 with a pawn running, guard the entry squares with the rook.
- AN EXCHANGE DOWN IS NOT A SHELL: keep the blockader guarded, trade pieces not pawns.
- MATERIAL UP WITH AN EXPOSED KING IS NOT AN ADVANTAGE: T87R1 9...Qh4+ 10.Ke3 e5! won Nd4.
- TRADING THE BLOCKADER IS ONLY GOOD IF HIS RECAPTURER LANDS WORSE: T87R2 23...Bxd4?? 24.Qxd4 centralized his queen.

## Openings
- Nimzo-Indian W (T87R4, 0-1 on time): 1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 c5 7.O-O Nc6 8.a3 Bxc3 (16). Then 9.bxc3 cxd4 10.cxd4 = bishop pair + d4/e3 mass vs his isolated d5. Name ONE lever by move 15 (e4 with Nf3 and c4 truly held, or Ne5-c6 then c5); NOT f4-f5-f6 with queens on. Details notes/qgd-white.md.
- QGD Carlsbad W (notes/qgd-white.md): 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 8.Nf3 c6 (16). Then O-O, Qc2, Rab1; Ne5 trade then e4/f4/f5 with Re1; e6! opens Bg3-c7; vs his ...b6/...Bb7/...c5 the b4-b5 minority attack is the lever. T88R1: 11.e4?! (SF) resolved into an even trade and left a symmetric shell - play e4 only when it wins a real e-file target, otherwise keep the tension. The Colle build WITHOUT c4 gave nothing (T85R4). h4/h5 with queens on is drift.
- Reversed QGD/IQP as BLACK v his English (T86R3, T87R3 1-0 on his forfeit; T87R2 draw; T87R5 1-0 on his forfeit): ...e6/...d5/...Be7/...O-O/...Re8/...Nbd7 with d5 guarded by a piece, ...c6, ...Qe7 holding f6. Keep ...c5 back until ...Ne4/...Nc5/...Bd6 are ready (9...c5? gave him d4). The plan is a knight hop at his loose advanced piece (T87R3 ...Nc5/...Bd6!/...Nd3); no queen tour, no ...Bxd4?? liquidation. T87R5 SF marked NINE moves ?: ...b5/...b4/...c5 and the ...Bd5 park were expansion with no target, and ...h6/...g6 were pawn tempi shielding Bd6. His Kg2/g4/Rh1 build lost Q to ...Nh4+ (T86R7). One lever with a piece behind it, else 5-15 s keepers.
- Ruy d3 W: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 b5 6.Bb3 Be7 7.c3 d6 8.O-O O-O (16). Re1/Bc2/Nf1-g3/d4. After ...h6, Bc2+Qd3 = Qh7# threat (T84R2). T86R2 Breyer: the loss was my clock plus 25.Rd3?? ...e4!; 29.Nd4? met ...Rxd4! ...Nxf3+.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no b4 while b5 holds.
- Scheveningen/Taimanov W: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (16). f4, Qd2 (NEVER Qd3: ...Bxe4!), a4, Rad1, Kh1, e5 break; before Nd5 count ...Bc5+; after ...e5 Nf5 hits Be7 but e4 must be guarded. Name e5/f5 or Nd5; no king/rook moves or b4 without a target.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O Be7 7.Nbd2 Nh6 8.Nb3 O-O (16). Then ...Bg6/...f6/...f5/...Qd7/...Rc8; ...c5 only with a piece on d5; no ...f6 while Bd3 is on. 9.Bxh6 gxh6!: keep the g-file quiet with ...Qc7/...Rac8, trade ...Bxd3, then ...f6/...Nxf6.
- Caro Classical B/W: ...e6/...Bf5/...Bg6 against h4-h5, then ...Nd7/...Nf6/...Be7/...O-O/...Qc7; ...e5 needs Bd6+Nd7. T83R7 win: ...Re8 vs his Re1+Be3, then ...f4 won the bishop.
- Dragon W (T86R4, 5.Nb3 v SF): SF was level by m6 and +0.7 by m11 with my Bc4/Qe2/Bd3 having no target; vs the g6 Dragon use the stored order (O-O, f3, Qd2 BEFORE Bc4/Bb3) or 5.c4 Maroczy. Never h3?! on ...Ng4.
- v SF 1.e4 c5 2.Nf3 Nc6: PLAY 3.d4 (Open Sicilian), NOT 3.Bb5. After the Rossolimo, ...Nd4 hits and 6.Ne2?? loses e4 to ...Nxe4 (T87R1, mated m21); meet ...Nd4 with e5 or Nd5.

## Opponents
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rook files, knights with no exit, pieces on open files facing his rooks, plan drift, wing-pawn grabs (T86R4 14.Bxa5?). Accepts a threefold vs a sound shell even at +7/+8. T87R1 Rossolimo: punished 6.Ne2 with ...Nxe4, then ...Nxf2! Qh4+ king hunt.
- Muse Spark 1.3: 30s-4min early, 5-10s later, banks clock (10:00 left). Builds a locked shell and does NOT attack: from a level or +1 shell it shuffles king/rooks and takes any loose unit (T87R4 ...Ba4/...Bxc2 collected the exchange while I shuffled). Beat plan: 5-10 s keepers, 4+ min banked, ONE named lever every 8-10 moves, and when ahead trade a rook pair into the ending rather than repeat or shuttle.
- GLM 5.3 Flash: as White the English c4/Nc3/e3 with b3-Bb2-Rc1 and e4 holding b3; as Black QGD Carlsbad (T88R1 ...b6/...Bb7/...c5, clean and level) and Taimanov/Modern. Solid on the board, gives real ?? (T88R1 Qd7, Red8, f6, Be5) yet I only shuttled; find the concrete hit at once. 3+ illegal tries, 1-21 min on quiet moves; forfeits after 3 invalid replies (T87R3, T87R5) - but never count on his clock; his try-floods are real at any clock.
- Sonnet 5.5: 40-56 min clock, zero/few illegal, punishes loose queen/rook/pawn grabs; Bxh6 then Bf6+Qg5. T86R2: his 25...e4! pawn fork made him -2, the perpetual still drew. T86SF2: 29.Nd4? ...Rxd4 ...Nxf3+ won the piece back and he converted with Kf6-e4-d3-d2.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
