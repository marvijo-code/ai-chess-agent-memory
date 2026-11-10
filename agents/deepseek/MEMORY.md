# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B
- notes/qgd-white.md - QGD/Nimzo W + reversed QGD/IQP B
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W: 5.d3, Berlin d3, Closed Chigorin
- notes/sicilian-black.md - Alapin/Taimanov B (e5-clamp, T89R3)
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
Tools: last-word, keeper-pick, legal-list, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender, knight-exit, heavy-fork-scan, resend-guide, pace-watch, check-ledger, drift-guard, pace-guard (prints material + clock budget, flags hanging pieces while not lost).

## Rule 0 - one move per turn, legality, clock
- ONE MOVE PER TURN: a forfeit beats any move. Pawn-only flag = RESEND SAME UCI once, 5-10 s; piece/queen/rook/exchange/mate flag = ONE plainly sound different keeper, 5-15 s; NEVER a third distinct move. Forfeits: T88R6 (3 tries, level), T88R1 (5), T88R3 (6), T88R4 (5), T89R1 (3 in check), T89R2 (3 + clock).
- IN CHECK the reply is a SQUARE LIST: escapes/blocks/captures with material kept, ONE keeper 5-15 s. T89R1 my only block Nd4 was flagged, three tries, forfeit.
- EMPTY REPLY = FORFEIT, from over-long reasoning (T88R4 after his queen grab). After move 20 send the UCI and ONE line.
- REFUSAL CLASSIFIER: piece/queen/rook/exchange/mate = REAL; wing-pawn flag, or any refusal of a check/mate-net move = NOISE, resend the same UCI once; a central-pawn flag with my king uncastled and queens on = REAL. After a SECOND refusal change piece AND idea at once.
- STALE SQUARE = my illegal tries: write the piece's REAL square from the current FEN before every UCI.
- TRY BUDGET: in a hopeless shell each keeper draws one pawn flag, so a move costs 2 tries; name the least-bad keeper and resend once.
- CLOCK: level/down/lost 5-15 s, ONE send; forced recapture 3-5 s. Every ?? in T88R2/3/4, T89R1/3 came from a 1-9 min think.
- LONG THINKS ARE THE LOSING MOVE: T89R2 (W +3 at m26) spent 4:27 Rf1, 7:44 Rc2, 11:00 g3, 5:05 Rf3 = ~37 min on keepers, flagged 12:07 v 43:36. T89R3 (B Taimanov v SF) spent 9:14 ...Nb4, 6:41 ...Nd5, 8:22 ...Qd7, 4:05 ...Ke8, 3:44 ...Qb7 = ~52 min by m26, flagged 8:05 v 1:04:29 - and every one of those long-think moves was marked ?/??. Level or worse: 5-15 s, ONE send, no 3-11 min "improvement".
- Tool AVOID is not material: count queen for bishop/rook before obeying; in check or while giving check a pawn flag is NOISE.
- MATERIAL from the board every move, W x / B y; name my loose units and his lines to them before any quiet move.
- ONE HEAVY ON A FORK SQUARE IS A FORK: check BOTH heavy squares against every enemy knight jump.

## Rule 1 - destination sweep
- A WING PAWN PUSH MUST FIRST LIST HIS CENTRAL PUSH THAT HITS TWO UNITS: T89R1 16.b4?? let ...d4! hit Nc3+Be3 (15.Be3?! had invited ...d5).
- HIS e5-PAWN OWNS e6 AND d6: before my knight lands on d5 against it, count Nxd5 exd5 e6! (T89R3 13...Nd5? 14.Nxd5 exd5 15.e6! = SF +2.8, and his Qg3/Bf4/Bc3/Rad1 clamp then beat ...f5).
- A ROOK RETREAT SQUARE IN FRONT OF HIS ADVANCED PAWN IS A PAWN-FORK SQUARE (T86R2 25.Rd3?? ...e4! forked Rd3+Nf3). Before landing a rook on the d/e/f-file, list his one-step pawn pushes to that square.
- A PIECE ON AN OPEN FILE WITH HIS ROOK AT THE FAR END IS LOOSE (T84R4 24.Bc4?? in front of Rc8).
- WHEN HIS MOVE UNGUARDS A UNIT, HIT IT THAT MOVE (T81R7 27.Rce1 left c3, ...Rxc3!).
- A GUARD MUST REACH IN ONE MOVE; a pinned guard guards nothing. An attacked piece gets its retreat/exchange list before any quiet move.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; every knight jump; every bishop/rook line. AN ATTACK IS NOT A DEFENCE.
- PAWN PUSHES: opening a file (T80R7 26.c4??); "saving" a pawn creates a second target (T81R3 16...h5?? 17.Qh6); a double push can be an e.p. fork (T82R1 ...d5?? exd6); a wedge f6 with no follow-up costs the e5 grip (T87R4 26.f6??). Kicking his rook with ...g5/...f6, or ...h6/...g6 bought to shield a loose bishop, is drift: move or trade the bishop.
- HIS ADVANCED UNDEFENDED PIECE WITH MY ROOK BEHIND ITS ATTACKER IS MINE (T87R3 10.Ne5, ...Bd6! won it).

## Rule 1b - king safety and mate first
- MY KING IS THE PIN'S ANCHOR: T88R2 36...Kg6 stood my K on rank 6 behind Ne6; 37.Rd6 pinned the knight to him and 38.Kd5 won it. Before any king step list his rooks/queens reaching the new rank/file THROUGH one of my pieces.
- Ask what mates if I pass; keep a rank-1 blocker or luft; K on c8 with b7 empty is a mating net.
- HIS DARK BISHOP ON h6/f6 + HIS QUEEN = g7 IS THE MATE SQUARE (T82R6 26...f5?? after 26.Bxh6); his ...h6 with Kg8 makes h7 a mate square on d3-h7 (T84R2).
- HIS QUEEN ON g3 WITH HIS LIGHT BISHOP ON g4/e4 = g-file clamp: ...f5 does not save it (T89R3 20...f5 was already +6; the e5-pawn wedge came first).
- HIS BISHOP ON f2/g3 + HIS QUEEN ON RANK 1 OR e1 = Qg1#/Qh2#: answer with CHECKS only (T86R2 69...Bf2, only Qc8+ survived).
- HIS ROOK ON e1 + HIS PAWN f3 + MY K h2 = ...Be5# (T86SF2 64...Be5#); luft does not save Kh2.
- AFTER ...gxh6 the open g/h files are the position: ...Qc7/...Rac8/...Bxd3, trade queens, keep ...f6/...e5 closed until the king has luft.
- BACK-RANK FINISHER ...Rc1+ Rxd1+ Rxe1#: every block is a piece (T80R5 19...Rd8+ 20.Bd5 Rxd5+ 21.Bd4 Rxd4#).

## Rule 2 - queen and the shuttle ban
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump (T78R1 33.Qd4?? in front of Rd8).
- BEFORE ANY QUEEN CAPTURE walk every enemy knight jump to her landing (T81R6 Qxd6?? Nxd6+).
- A QUEEN RAID ON THE OTHER WING IS NOT A DEFENCE (T82R6 ...Qb6+/...Qb3/...a5 emptied my kingside).
- NO SHUTTLE WITHOUT A NEW TARGET: T88R1 Nf5-Ne3-Nf5 five times, threefold; T87R4 Qe3-Qg3-Qf4-Qg3 while my clock died; T89R2 Qd3/Qc3/Qc5 re-centred the queen into ...Ba7 hitting her and pinning Nd4. When a hook is jammed twice, change the TARGET (trade on the hooked square, offer a rook trade, play a real pawn lever).
- THREE DIFFERENT PIECES IN A ROW WITH NO CAPTURE AND NO NAMED TARGET = DRIFT (T88R3 16...Bd6?? 18...Qb6?? 19...f6??; T88R7 bishop tour; T89R3 ...Nb4-...c5-...Bb7-...Bc6-...Nd5, five pieces, 25 min). When his queen sits on g3 over an e5-pawn, name ONE guard of g7 (...Be7/...Bf8) and ONE break by move 12, and play only those.

## Rule 3 - captures and trades
- HIS KNIGHT LANDING THAT HITS A MATE SQUARE AND A FORK: move the forked units first, prefer the step that also covers the mate square (T88R6 17.Ng5! hit h7 + Qc7/Rf8; 17...Qf7 covered h7 and left c7, while ...f5?! lost e6 to Nxe6).
- RECOUNT AFTER EVERY EXCHANGE - my narrative is not the board (T80R5 wrote "clean pawn up" while material was LEVEL).
- A KNIGHT LANDING WHERE HIS ROOK CAN TAKE IT: count the whole chain, forks included (T86SF2 29.Nd4? ...Rxd4 30.Bxd4 Nxf3+).
- THE ROOK RECAPTURES BEFORE THE QUEEN: list every recapturer, nearest first (T86R4 14.Bxa5??).
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET; MY PIECE ON HIS IS LOST.
- KNIGHT LANDS WITH NO EXIT = PIECE (T79SF2G1 17...Nb4? Rb1; T86R4). A knight that hits nothing is drift; HIS knight with no retreat is MY target (T87R3 Ng4 hunted by ...Be6).
- A KNIGHT HOP THAT HITS TWO UNITS IS THE PLAN (T87R3 ...Nc5/...Nd3; T88R4 23.Nb4! won Qa2; T88R7 ...Nb4-...Nd3 hit Bb2+Re1).
- A CLEARLY EVEN PIECE TRADE IS GOOD EVEN IF A TOOL FLAGS A PAWN: resend once, then a legal keeper (T83R6).
- WHICH PIECE RECAPTURES IS THE POSITION: ...Nxf6 keeps my dark bishop home; Bxf6 turns it into a shuttle (T85R5).

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. UP = 5-10 s keepers, trade pieces not pawns; a repetition while ahead OR while his clock is under 2 min is MY loss.
- UP: TAKE EACH LOOSE UNIT WITH A PIECE HOP, NOT A PAWN PUSH, and shield the hopper (T87R3).
- A LOCKED LEVEL SHELL WITH NO NAMED LEVER IS A THREEFOLD: T87R2 +1 at m30, 30 shuffling moves, threefold at 1:14 v 10:00; T83R4 +2P the same; T88R1 level, five repeats. NAME the lever by move 20-25 and make a NEW move every turn while ahead.
- A BLOCKADE OF A PAWN THAT CANNOT ADVANCE EARNS NOTHING (T87R5 22...Bd5 sat ten moves while his queen held b3).
- ...f6 / f4-f6 WEDGES IN A BLOCKED SHELL NEED A CONCRETE FOLLOW-UP (T86R3 20...f6?; T87R4 26.f6??; T88R3 19...f6??; T89R2 36.f4?? drove his bishop to b8 from where ...Ba7 later hit my queen).
- A LEVEL PAWN FORK IS NOT A WIN IF THE RESULTING OPEN FILE IS HIS (T88R3 40...e4?? 41.fxe4 Nxe4 42.Ne3, Rd8-d7).
- DOWN MATERIAL WITH QUEENS ON AND HIS MATE NET SHOWING: ONLY CHECKS SAVE (T86R2 Qc8+/Qf5+ perpetual).
- DOWN A PIECE OR A PAWN IN A LOCKED CENTRE = THE SHELL: every unit guarded, K h7/g8, 5-15 s; DOWN MATERIAL A REPETITION IS MY SAVE. HIS KING WALK IS THE FINISHER: guard the entry squares with the rook (T86SF2 Kf6-e4-d3-d2).
- AN EXCHANGE DOWN IS NOT A SHELL: keep the blockader guarded, trade pieces not pawns.
- MATERIAL UP WITH AN EXPOSED KING IS NOT AN ADVANTAGE (T87R1 9...Qh4+ 10.Ke3 e5! won Nd4).
- TRADING THE BLOCKADER IS ONLY GOOD IF HIS RECAPTURER LANDS WORSE (T87R2 23...Bxd4?? 24.Qxd4).
- A WIN BY HIS FORFEIT IS NOT A CHESS LESSON: note what I should have played, not the gift.

## Openings
- Nimzo-Indian W: ...e3/Bd3/O-O vs ...Bb4; plan e4 or Ne5-c6 then c5, not f4-f5-f6 with queens on.
- QGD Carlsbad W: 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 8.Nf3 c6 (16). Then O-O, Qc2, Rab1; Ne5 trade then e4/f4/f5 with Re1; e6! opens Bg3-c7; vs ...b6/...Bb7/...c5 the b4-b5 minority attack. 11.e4?! only when it wins a real e-file target; h4/h5 with queens on is drift.
- Reversed QGD/IQP as BLACK v his English: ...e6, ...d5, ...Be7, ...O-O, ...Re8, ...Nbd7 with d5 guarded by a piece, ...c6, ...Qe7 holding f6. Keep ...c5 back until ...Ne4/...Nc5/...Bd6 are ready (9...c5? gave him d4). Plan = knight hop at his loose advanced piece; no queen tour, no ...Bxd4??. T88R7 v GLM my ...Be6/...Be4/...Bd5 tour had no lever - play ...c5/...Ne4 by m15.
- Ruy d3 W: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 b5 6.Bb3 Be7 7.c3 d6 8.O-O O-O (16). Re1/Bc2/Nf1-g3/d4. After ...h6, Bc2+Qd3 = Qh7# threat (T84R2). 25.Rd3?? ...e4! pawn fork (T86R2). T89R2: the build was GOOD, +3 at m26; lost on my clock and 22.Qxb7??.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no b4 while b5 holds.
- Scheveningen/Taimanov W: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (16). f4, Qd2 (never Qd3: ...Bxe4!), a4, Rad1, Kh1, e5 break; before Nd5 count ...Bc5+; after ...e5 Nf5 hits Be7 but e4 must be guarded. T89R1: 10.Nf5?? lost to ...Bxf5 along c8-d7-e6-f5; 15.Be3?! and 16.b4?? let ...d4! hit Nc3+Be3.
- Taimanov B v his 7.e5 clamp: 7...Nd5 8.Qf3 Qc7?! 9.Qg3 - g7 needs a PIECE guard (...Be7/...Bf8) and ONE break named by m12; his e5-pawn owns e6/d6, so count Nxd5 exd5 e6! before my knight lands on d5. No five-piece tour (notes/sicilian-black.md, T89R3).
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O Be7 7.Nbd2 Nh6 8.Nb3 O-O (16). Then ...Bg6/...f6/...f5/...Qd7/...Rc8; ...c5 only with a piece on d5; no ...f6 while Bd3 is on. 9.Bxh6 gxh6!: keep the g-file quiet with ...Qc7/...Rac8, trade ...Bxd3, then ...f6/...Nxf6. Sound and level in T88R2/T88R6; those losses were the king walk and his 17.Ng5!.
- Caro Classical B: keep the light bishop on the h7 diagonal behind ...h6, develop ...e6/...Ngf6/...Be7/O-O, queen on c7, rooks on c8, then ...c5 with ...Nc5/...Nd5 support; trade ...Bxd3 in a quiet moment. Level through m25 both games.
- Dragon W: the 5.Nc3 Yugoslav (Be3, f3, Qd2, O-O-O) was FINE vs SF in T88R4 (+1.6 by m15). Use O-O, f3, Qd2 BEFORE Bc4/Bb3; never h3?! on ...Ng4. 5.c4 Maroczy is the quieter SF alternative.
- v SF 1.e4 c5 2.Nf3 Nc6: PLAY 3.d4, NOT 3.Bb5 (Rossolimo ...Nd4 hits; 6.Ne2?? ...Nxe4).

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on rook files, knights with no exit, pieces on open files facing his rooks, plan drift, wing-pawn grabs, and the e5-pawn advance e6!. Accepts a threefold vs a sound shell even at +7/+8. He never hurries (T89R3 1:04 left at m26 while I burned 52 min), so the clock gap is mine to lose. BUT IN QUIET MANOEUVRING HE BLUNDERS (T88R4 22...Qxa2 hung the queen): when a mark appears, find the concrete hit in 5-15 s and SEND.
- Sonnet 5.5: 40-56 min clock, few illegal, never flags; punishes loose queen/rook/pawn grabs, uses mate nets, pins and back-rank. T88R2: won a clean pawn, then in a LEVEL rooks-off ending his 37.Rd6/38.Kd5 king-pin won a knight. T88R6: his 17.Ng5! combined a mate square with a fork; I forfeited at m18. T89R2: after my +3 his 39...Ba7 (queen hit + Nd4 pin) was his only real try - the loss was my clock, not his play.
- Muse Spark 1.3: 1-6 min thinks, banks nothing, builds a locked shell and does NOT attack: shuffles king/rooks and takes any loose unit (...Ba4/...Bxc2, T87R4). HE CAN FLAG (12.9 s left at m50, T88R3). Beat plan: 5-15 s keepers, ONE named lever every 8-10 moves, trade a rook pair when ahead, do not burn my own clock.
- GLM 5.3 Flash: English c4/Nc3/e3 with b3-Bb2-Rc1 as White, QGD Carlsbad and Taimanov/Modern as Black. Gives real ?? (T88R1; T88R7 22.Ne3??; T89R1 18...Bc7??/20...Rab8?!) yet I only shuttled instead of hitting. 3+ illegal tries, 1-21 min on quiet moves, forfeits after 3 invalid replies - never count on his clock, but do not gift him a playable game.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
