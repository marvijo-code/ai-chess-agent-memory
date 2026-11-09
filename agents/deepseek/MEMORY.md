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
Tools: last-word (top-3 material keepers + the one-send rule), keeper-pick, legal-list, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender, knight-exit, heavy-fork-scan, resend-guide, pace-watch, check-ledger, drift-guard.

## Rule 0 - one move per turn, legality, clock
- ONE MOVE PER TURN: A FORFEIT IS WORSE THAN ANY MOVE. If the refusal names only a PAWN (or says 'about 1 pawn'), RESEND THE SAME UCI ONCE, always, 5-10 s - the second send passes. T88R6 level Caro at m18: my tool said 'about 1 pawn down, Ng5 takes e6'; I answered with THREE different moves and lost 0-1 by forfeit in a playable game. Same shape T88R1 (5 tries), T88R3 (6), T88R4 (5). NEVER a third distinct move.
- EMPTY REPLY = FORFEIT, AND IT COMES FROM OVER-LONG REASONING: T88R4 his 22...Qxa2 hung the queen (23.Nb4! wins her) and my 24 743-char analysis returned an EMPTY reply = 0-1. After move 20 reply with the UCI and ONE line.
- REFUSAL CLASSIFIER: reason naming a PIECE, QUEEN, ROOK, EXCHANGE or MATE is REAL: send ONE different plainly sound keeper, 5-15 s. A reason naming a WING PAWN, or any refusal of a move that GIVES CHECK or starts a mate net, is NOISE: RESEND THE SAME UCI once. A CENTRAL-PAWN (e4/d4) flag while my king is uncastled and queens are on is REAL (T87R1 6.Ne2 -> ...Nxe4). NEVER a variant of the same idea.
- STALE SQUARE = ALL MY ILLEGAL TRIES: write the piece's REAL square from the FEN before every UCI. T88R6 ...Rac8 x2 and ...f5 x3 (3:59 spent on the pawn push); T88R3 six gated tries incl. FORCED recaptures (48...Re8, 49...Qxe8) - even a forced move costs a try; T88R4 five: 15.Be3 x3, 16.Rde1, 20.h4 x3.
- TRY BUDGET: in a hopeless shell EVERY keeper draws one pawn-only flag, so each move costs 2 tries. After a move's SECOND refusal change piece AND idea at once; where the tool flags every legal move, name the least-bad keeper and RESEND ONCE, 5-10 s.
- LOST POSITION = EVERY MOVE FLAGGED: T88R2 my tool flagged every reply while a pinned knight fell and I sent THREE different moves - forfeit in a LEVEL rook ending. Run tools/last-word.py and tools/keeper-pick.py, take the keeper, SEND it 5-15 s, resend the same once.
- MATE DEFENCE IS A SQUARE LIST, ONE TRY: name g7's covering rook squares (c7/d7/e7/f7), send in 5-15 s.
- CLOCK: level/down/lost 5-15 s, ONE send; a FORCED recapture 3-5 s. T88R4 24 min gone by move 22 in a +2 position. T88R2 32:10 v 56:53. T88R3 every ?? came from a 1-7 min think; ended 1:39 v 0:12. T87R4 keepers lost on time. His clock under 5 min: 5-10 s keepers ONLY.
- Tool AVOID is not material: count queen for bishop/rook before obeying; in CHECK or while GIVING CHECK a pawn-loss flag is NOISE.
- Material from the board every move, W x / B y. Name my loose units and his lines to them before any quiet move.
- ONE HEAVY ON A FORK SQUARE IS A FORK: check BOTH heavy squares against every enemy knight jump before a queen move.

## Rule 1 - destination sweep
- A ROOK RETREAT SQUARE IN FRONT OF HIS ADVANCED PAWN IS A PAWN-FORK SQUARE: T86R2 25.Rd3?? ...e4! forked Rd3+Nf3. Before landing a rook on the d/e/f-file, list his one-step pawn pushes to that square.
- A PIECE ON AN OPEN FILE WITH HIS ROOK AT THE FAR END IS LOOSE: T84R4 24.Bc4?? in front of Rc8.
- WHEN HIS MOVE UNGUARDS A UNIT, HIT IT THAT MOVE: T81R7 27.Rce1 left c3 - ...Rxc3!.
- A GUARD MUST REACH IN ONE MOVE; a pinned guard guards nothing. AN ATTACKED PIECE GETS ITS RETREAT/EXCHANGE LIST BEFORE ANY QUIET MOVE.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; every knight jump; every bishop/rook line. AN ATTACK IS NOT A DEFENCE.
- PAWN PUSHES: opening a file (T80R7 26.c4??); 'saving' a pawn creates a second target (T81R3 16...h5?? 17.Qh6). KICKING HIS ROOK WITH ...g5/...f6 IN A LEVEL CLAMP IS DRIFT (T85R2 32...g5?? 33.Rg4), and so is ...h6/...g6 bought to shield a loose bishop: MOVE OR TRADE THE BISHOP instead. A DOUBLE PUSH CAN BE E.P. FORK (T82R1 ...d5?? exd6).
- A WEDGE PAWN (f6) THAT TAKES SQUARES FROM HIS KNIGHT MUST HAVE A FOLLOW-UP OR IT COSTS MY e5 GRIP (T87R4 26.f6??).
- HIS ADVANCED UNDEFENDED PIECE WITH MY ROOK BEHIND ITS ATTACKER IS MINE: T87R3 10.Ne5 undefended, ...Bd6! (Re8 behind the hit) won it.

## Rule 1b - king safety and mate first
- MY KING IS THE PIN'S ANCHOR: T88R2 36...Kg6 stood my K on rank 6 behind Ne6; 37.Rd6 pinned the knight to it and 38.Kd5 attacked it = -3 and the forfeit. Before any king step list his rooks/queens reaching the new rank/file THROUGH one of my pieces. Unpin (Kg7/Kh7) BEFORE his king walks up.
- Ask what mates if I pass; keep a rank-1 blocker or luft; K on c8 with b7 empty is a mating net.
- HIS DARK BISHOP ON h6/f6 + HIS QUEEN = g7 IS THE MATE SQUARE: name g7's guard THAT MOVE, or trade the bishop. T82R6 26...f5?? after 26.Bxh6. His ...h6 with K g8 makes h7 a mate square on the d3-h7 diagonal (T84R2).
- HIS BISHOP ON f2/g3 + HIS QUEEN ON RANK 1 OR e1 = Qg1#/Qh2#: answer with CHECKS only (T86R2 69...Bf2, only Qc8+ survived).
- HIS ROOK ON e1 + HIS PAWN ON f3 + MY K ON h2 = ...Be5#/...f2: luft does NOT save Kh2 (T86SF2 64...Be5#).
- AFTER ...gxh6, THE OPEN g/h-FILES ARE THE POSITION: play ...Qc7/...Rac8/...Bxd3, trade queens, keep ...f6/...e5 closed until the king has luft.
- BACK-RANK FINISHER: ...Rc1+ Rxd1+ Rxe1#. EVERY BLOCK IS A PIECE: T80R5 19...Rd8+ 20.Bd5 Rxd5+ 21.Bd4 Rxd4#.

## Rule 2 - queen & the shuttle ban
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. T78R1 33.Qd4?? in front of Rd8.
- BEFORE ANY QUEEN CAPTURE, WALK EVERY ENEMY KNIGHT JUMP TO HER LANDING: T81R6 Qxd6?? lost to Nxd6+.
- A QUEEN RAID ON THE OTHER WING IS NOT A DEFENCE: T82R6 ...Qb6+/...Qb3/...a5 emptied my kingside.
- NO SHUTTLE WITHOUT A NEW TARGET - QUEEN OR KNIGHT: T88R1 Nf5-Ne3-Nf5 five times in a level Carlsbad; each hook answered by the same step-back (Bd6, Be5) and the game died in threefold. T87R4 Qe3-Qg3-Qf4-Qg3 tour while my clock died. When a hook is jammed TWICE, change the TARGET (trade on the hooked square, offer a rook trade, play a real pawn lever), never just the square.
- THREE DIFFERENT PIECES MOVING IN A ROW WITH NO CAPTURE AND NO NAMED TARGET = DRIFT: T88R3 16...Bd6?? 18...Qb6?? 19...f6?? in a level shell; 43...Re7 45...Kh7 46...Qe6 walked my king into his rook. In a level shell replay the same TWO verified keepers; do not rotate pieces to look active.
- A BISHOP TOUR IN A LOCKED CENTRE IS DRIFT TOO: T88R7 16...Be6?!/18...Be4?!/19...Bd5?! with no lever; name ...c5 or ...Ne4 by move 15, not a light-bishop rotation.

## Rule 3 - captures & trades
- HIS KNIGHT LANDS ON A SQUARE HITTING TWO OF MY UNITS (mate square + fork): MOVE THE FORKED UNITS FIRST, and prefer the step that also covers the mate square. T88R6 17.Ng5! hit h7 (Qd3-h7 mate) and forked Qc7 with Rf8; 17...Qf7 covers h7 along the empty 7th rank AND leaves c7, while ...f5?! blocked with a pawn and left e6 hanging to Nxe6 = my forfeit.
- RECOUNT AFTER EVERY EXCHANGE - MY NARRATIVE IS NOT THE BOARD: T80R5 I wrote 'clean pawn up' while material was LEVEL.
- A KNIGHT LANDING WHERE HIS ROOK CAN TAKE IT: count the WHOLE chain, forks included. T86SF2 29.Nd4? ...Rxd4 30.Bxd4 Nxf3+.
- THE ROOK RECAPTURES BEFORE THE QUEEN: T86R4 14.Bxa5?? - his ROOK recaptured first. List every recapturer IN ORDER, nearest first.
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET; MY PIECE ON HIS IS LOST.
- KNIGHT LANDS WITH NO EXIT = PIECE: T79SF2G1 17...Nb4? Rb1 trapped it; b7 only with an unguarded retreat (T86R4). A KNIGHT THAT HITS NOTHING IS DRIFT (T85R5). HIS knight with no retreat is MY target (T87R3 Ng4 hunted by ...Be6).
- A KNIGHT HOP THAT HITS TWO UNITS IS THE PLAN: T87R3 ...Nc5/...Nd3/...N3e5; T88R4 23.Nb4! hit Qa2+Nc6 and won the queen; T88R7 ...Nb4-...Nd3 hit Bb2+Re1.
- A CLEARLY EVEN PIECE TRADE IS GOOD EVEN IF A TOOL FLAGS A PAWN: T83R6 31...Bxg5 hxg5; resend once, then a legal keeper.
- WHICH PIECE RECAPTURES IS THE POSITION: T85R5 14.exf6+ Bxf6? turned my dark bishop into a shuttle; ...Nxf6 keeps it home.

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. UP = 5-10 s keepers, trade pieces not pawns; a repetition while ahead OR while his clock is under 2 min is MY loss.
- UP: TAKE EACH LOOSE UNIT WITH A PIECE HOP, NOT A PAWN PUSH (T87R3 ...Nc5/...Bd6!/...Nd3/...Bxa3); shield the hopper.
- A LOCKED LEVEL SHELL WITH NO NAMED LEVER IS A THREEFOLD: T87R2 +1 at m30, 30 shuffling moves, threefold at 1:14 v 10:00; T83R4 +2P the same way; T88R1 level, five repeats. NAME the lever by move 20-25 and make a NEW move every turn.
- A WON POSITION IS ALSO A CLOCK GAME: T84R5 +3 at m26 LOST ON TIME; T87R4 lost on time at m44 with 8 illegal tries; T88R4 +4 at m22 forfeited on an empty reply. Up: ONE plan, 5-15 s.
- A BLOCKADE OF A PAWN THAT CANNOT ADVANCE EARNS NOTHING: T87R5 22...Bd5 sat ten moves while his queen held b3.
- ...f6 / f4-f6 WEDGES IN A BLOCKED SHELL NEED A CONCRETE FOLLOW-UP: T86R3 20...f6?; T87R4 26.f6??; T88R3 19...f6??.
- A LEVEL PAWN FORK IS NOT A WIN IF THE RESULTING OPEN FILE IS HIS: T88R3 40...e4?? 41.fxe4 Nxe4 42.Ne3 gave him Rd8-d7 and the initiative.
- DOWN MATERIAL WITH QUEENS ON AND HIS MATE NET SHOWING: ONLY CHECKS SAVE (T86R2 Qc8+/Qf5+ perpetual).
- DOWN A PIECE OR A PAWN IN A LOCKED CENTRE = THE SHELL: every unit guarded, K h7/g8, 5-15 s. DOWN MATERIAL, A REPETITION IS MY SAVE.
- DOWN MATERIAL, HIS KING WALK IS THE FINISHER: T86SF2 Kf6-e4-d3-d2, guard the entry squares with the rook.
- AN EXCHANGE DOWN IS NOT A SHELL: keep the blockader guarded, trade pieces not pawns.
- MATERIAL UP WITH AN EXPOSED KING IS NOT AN ADVANTAGE: T87R1 9...Qh4+ 10.Ke3 e5! won Nd4.
- TRADING THE BLOCKADER IS ONLY GOOD IF HIS RECAPTURER LANDS WORSE: T87R2 23...Bxd4?? 24.Qxd4.
- A WIN BY HIS FORFEIT IS NOT A CHESS LESSON: T88R7 the game was level and my own moves were SF ?/?!; note what I should have played, not the gift.

## Openings
- Nimzo-Indian W (T87R4): 1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 c5 7.O-O Nc6 8.a3 Bxc3 (16). Then 9.bxc3 cxd4 10.cxd4 = bishop pair + d4/e3 mass vs isolated d5. Name ONE lever by move 15 (e4 with Nf3 and c4 held, or Ne5-c6 then c5); NOT f4-f5-f6 with queens on. Details notes/qgd-white.md.
- QGD Carlsbad W: 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 8.Nf3 c6 (16). Then O-O, Qc2, Rab1; Ne5 trade then e4/f4/f5 with Re1; e6! opens Bg3-c7; vs ...b6/...Bb7/...c5 the b4-b5 minority attack. T88R1: 11.e4?! resolved into an even trade and a symmetric shell - play e4 only when it wins a real e-file target. h4/h5 with queens on is drift.
- Reversed QGD/IQP as BLACK v his English (T87R3 win, T87R2 draw): ...e6, ...d5, ...Be7, ...O-O, ...Re8, ...Nbd7 with d5 guarded by a piece, ...c6, ...Qe7 holding f6. Keep ...c5 back until ...Ne4/...Nc5/...Bd6 are ready (9...c5? gave him d4). Plan = knight hop at his loose advanced piece (...Nc5/...Bd6!/...Nd3); no queen tour, no ...Bxd4??. T87R5 nine SF-marked ?: ...b5/...b4/...c5 and the ...Bd5 park were expansion with no target. T88R7 v GLM: level to m14, then my ...Be6/...Be4/...Bd5 bishop tour (SF ?!) had no lever; the win was his forfeit after 22.Ne3?? ...Nb4 ...Nd3. Play ...c5/...Ne4 by m15.
- Ruy d3 W: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 b5 6.Bb3 Be7 7.c3 d6 8.O-O O-O (16). Re1/Bc2/Nf1-g3/d4. After ...h6, Bc2+Qd3 = Qh7# threat (T84R2). T86R2 Breyer: 25.Rd3?? ...e4! pawn fork; 29.Nd4? ...Rxd4! ...Nxf3+.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no b4 while b5 holds.
- Scheveningen/Taimanov W: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (16). f4, Qd2 (NEVER Qd3: ...Bxe4!), a4, Rad1, Kh1, e5 break; before Nd5 count ...Bc5+; after ...e5 Nf5 hits Be7 but e4 must be guarded. Name e5/f5 or Nd5; no king/rook moves or b4 without a target.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O Be7 7.Nbd2 Nh6 8.Nb3 O-O (16). Then ...Bg6/...f6/...f5/...Qd7/...Rc8; ...c5 only with a piece on d5; no ...f6 while Bd3 is on. 9.Bxh6 gxh6!: keep the g-file quiet with ...Qc7/...Rac8, trade ...Bxd3, then ...f6/...Nxf6. T88R6: that whole plan (.Qc7/.Rac8/.Bxd3/.c5, .Nxc5/.Bxc5) was LEVEL - the loss was his 17.Ng5! (see Rule 3: move the forked queen/rook first). T88R2: ...f6/...Ne4/...c5/...cxd4 was sound and level - the loss was the king walk, not the opening.
- Caro Classical B (T88R3 1-0 on time v Muse, T85R2 draw): keep the light bishop on the h7 diagonal behind ...h6, develop ...e6/...Ngf6/...Be7/O-O, put the queen on c7 and rooks on c8, then play ...c5 with ...Nc5/...Nd5 support; trade ...Bxd3 in a quiet moment. Level through m25 both games. Details notes/caro-advance-black.md.
- Dragon W: the 5.Nc3 Yugoslav (Be3, f3, Qd2, O-O-O) was FINE vs SF in T88R4: +1.6 by move 15 and his 22...Qxa2 hung the queen to Nb4 - the loss was my empty reply. Use O-O, f3, Qd2 BEFORE Bc4/Bb3; never h3?! on ...Ng4 (it takes Be3). If his king is uncastled and h5 is out, no Bh6 tricks. 5.c4 Maroczy is the quieter alternative vs SF.
- v SF 1.e4 c5 2.Nf3 Nc6: PLAY 3.d4, NOT 3.Bb5. After the Rossolimo ...Nd4 hits and 6.Ne2?? loses e4 to ...Nxe4 (T87R1); meet ...Nd4 with e5 or Nd5.

## Opponents
- SF19: instant in the opening; punishes loose units, passive retreats, queens on rook files, knights with no exit, pieces on open files facing his rooks, plan drift, wing-pawn grabs (T86R4 14.Bxa5?). Accepts a threefold vs a sound shell even at +7/+8. BUT IN QUIET MANOEUVRING HE BLUNDERS: T88R4 22...Qxa2 hung the queen to Nb4 (+4). When a mark appears, find the concrete hit in 5-15 s and SEND. T87R1 Rossolimo: punished 6.Ne2 with ...Nxe4, then ...Nxf2! Qh4+ king hunt.
- Sonnet 5.5: 40-56 min clock, zero/few illegal, punishes loose queen/rook/pawn grabs; Bxh6 then Bf6+Qg5. T88R2: took a clean pawn with Nxg5, then in a LEVEL rooks-off ending his 37.Rd6/38.Kd5 king-pin won a knight. T88R6: his 17.Ng5! combined a mate square with a queen/rook fork; I forfeited at m18 with 3 invalid tries.
- Muse Spark 1.3: 1-6 min thinks on quiet moves both sides of the board, banks nothing, builds a locked shell and does NOT attack: shuffles king/rooks and takes any loose unit (T87R4 ...Ba4/...Bxc2 collected the exchange). HE CAN FLAG: T88R3 he was winning material at m50 with 12.9 s left. Beat plan: 5-15 s keepers, ONE named lever every 8-10 moves, trade a rook pair when ahead, and do not burn my own clock.
- GLM 5.3 Flash: English c4/Nc3/e3 with b3-Bb2-Rc1 as White, QGD Carlsbad and Taimanov/Modern as Black. Gives real ?? (T88R1 Qd7, Red8, f6, Be5; T88R7 22.Ne3??) yet I only shuttled; find the concrete hit at once. 3+ illegal tries, 1-21 min on quiet moves, forfeits after 3 invalid replies - never count on his clock, but do not gift him a playable game either.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
