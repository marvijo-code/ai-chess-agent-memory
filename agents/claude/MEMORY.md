# MEMORY (clocks 600+10, 900+10, 3600+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- W: Ruy d3 DeepSeek 9 W, Sol 10 W 9 L 4 D, Astra 0-1, Muse 1-0 0-1; Closed Ruy v Haiku 0-1; Sicilian DeepSeek 8 W, GLM 13 W, Muse 4 W; Maroczy v SF 2 W 4 D 9 L; Dragon 5.Nc3 v SF 0-1; Caro Adv DeepSeek 27 W 2 D 1 L, Muse 2-0, Sol 1-2. Rossolimo v SF: 3...Nf6 1-0; 3...g6 0-1 x5.
- B v Sol: Chigorin 6 W 18 L 3 D; Zaitsev 1-5; Breyer 0-1; Open Ruy 0-1; Berlin 4.d3 L; QGD 3-1; Pianissimo 0-2. DeepSeek: Chigorin 18 W 1 D, QGD 12 W, Pianissimo 9 W, Berlin 4.d3 Arm 1 W, Ruy 5.d3 D+W. GLM: English 12 W. Haiku: Giuoco 2 W 1 D. Muse: Ruy 5.d3 3 W 2 D 1 L.
- B v SF 1.e4: 3.Nc3 2 W 22 L 19 D (T88R3 L mate m19); Alapin 4 L 1 D; Ruy 6.d4 0-4; Berlin 4.O-O 1 D 3 L; Caro Adv, Two Knights, French L.

## Key lessons (read before EVERY move)
- API SAFEGUARD FORFEITS x2: COMMENT = 3-8 plain ASCII words about the chess move, no tool/error text, no quotes. After ANY provider error resend the same move at once with a DIFFERENT, shorter comment.
- T88R3 L (Four Knights B v SF, mate m19, level book to move 15): ...h6? Qf5 and ...Be6?? Qh7+ Kf8 Qh8#. My OWN Qe7 blocked the K flight e7. MATE-IN-2 SCAN BEFORE EVERY MOVE v Qh3/Qf5/Qh5 + Bd3: write his queen checks on h7/g7, each K flight, and which of MY pieces block it. Do not play luft ...h6 that hands the queen h7. Fix: ...Qe6/...f5 or a queen trade. tools/check-threats.py now flags mate in 1 and forced mate in 2. Notes/black-four-knights.md.
- T86 FINAL L (Four Knights): no ...b5/...a5 while his rooks double on the e-file; answer Be4 with ...Bf5/...f5/...Rd7 BEFORE it. g7 hole again after Qg3 f6 Bxf6.
- T88R2 W (Caro Adv v DeepSeek, model): Bxh6 gxh6, Qd2 at once, queen trade, then Nc5/Nd3-e5, f3-f4 kick, Rac1 trade, Bxf5, K to e4, Rd7+/Rd6 pin. He grabbed pawns and forfeited on illegal tries. Guarded units, 6-30 s moves.
- T86SF2G1 W (Breyer v DeepSeek): level shell, queen trade, his Nd4?? Rxd4 Bxd4 Nxf3+ fork. He hangs pieces when his pawns break: attack the wrecked pawn.
- T86R2 D (piece up m26, perpetual m74): my queen grabbed b3/a3/c3 far from my K; Q+B v Q with naked K is a DRAW. Piece up = queen near my K, cover 8th rank, trade QUEENS by force, no wing grabs. List his Qc8+/Qf5+ shuttle. Avoiding threefold needs a SAFE new move.
- MODEL GAMES: T85R5.2 v DeepSeek (Caro Adv), T85R6.2 v GLM (Scheveningen), T85R4 v Muse (B Ruy 5.d3 Breyer), T88R2. Guarded units + one threat per move.
- Rook ending a pawn down: K near queenside pawns / rook behind his passers; NO king march, no ...g6/...a6. v Qe4 play ...f5 or ...Bd5, NEVER ...g6. After c4 play ...Qe7/...Bf5/...f5, keep the bishop pair.
- EN PASSANT CHECK BEFORE EVERY PAWN DOUBLE STEP (40...g5?? hxg6 e.p.). tools/legal-list.py.
- RANK-BY-RANK COUNT BEFORE A ROOK TRADE INTO K+P. Keep rooks if his K can reach my pawns. Equal B v B = KEEP the bishops.
- ZWISCHENZUG CHECK WITH A RECAPTURE PENDING = BLUNDER (12...Bg4+?? 13.f3!). TAKE THE PENDING RECAPTURE FIRST. Before ANY check write every block/capture reply; a PAWN BLOCK that hits the checker kills it. tools/check-block.py.
- FORFEITS = 21 LOST GAMES. IN CHECK a pawn flag is noise: list each escape/block/capture BY SQUARE (tools/legal-list.py), send the move keeping most material at 5 s. A tool AVOID refuses a move ONCE: resending the SAME move goes through. Vague reason on a BOOK or plainly good move = RESEND once. Reason naming a lost piece = a DIFFERENT move. LOST AND EVERY MOVE LOSES THE SAME PAWN: pick ONE least-bad move, resend; NEVER cycle three moves.
- OWN PIECE ON THE LINE = ILLEGAL TRY (...Bf8 through own Rd6). Write the path square by square. GUARDS BEHIND MY OWN PIECE DO NOT EXIST. tools/own-blocker.py.
- UP MATERIAL = TRADE, DON'T SHUFFLE. Name ONE plan at once. CHECK STALEMATE. THREEFOLD WHILE HE FLAGS = I THROW AWAY THE WIN: opponent under 3 min and me 10+ ahead = a NEW safe move each turn.
- PAWN-ROLLER SQUEEZE v SF: his a4-b5-a6-b6 rolled. Keep ...c6/...a5 blockade, take ...cxb4/...axb4 EARLY. Name HIS pawn break by move 15 / 25.
- DOWN A BISHOP/PAWN v SF: shell lost slowly. Keep a rook when a passer exists; K to the passer.
- FLAG WIN v GLM/DeepSeek/Muse: guarded 5-40 s moves, no new weaknesses, no repeat. They burn 3-14 min on quiet moves. When weak keep checks and threats, never resign; a ROOK DOWN v non-SF: K shuffles lose to K+R mate.
- QUEEN MOVE OR QUEEN-TRADE OFFER: FIRST LIST HIS KNIGHT FORKS ON HER LANDING SQUARE AND ON MY ROOK (46...Qc5?? Nb3). tools/pin-fork-trap.py.
- LEVEL GAME v DEEPSEEK/MUSE/GLM = PLAY FOR A WIN. Name a PLAN by move 20 (a4-a5, f4, Rc2, rook trade). In the Muse Ruy shell prefer ...d5 or ...Nh5 breaks.
- Caro Adv v DeepSeek: ...f6 break loses h6/e6 (Bxh6, Rxe6); Bf6 + Qg5/Qh4/Qh6 mate threats on g7; ...Qb6/...Nh5 grabs lose to Nd7 fork. v ...Nh6 gxh6: Qd2 at once.
- ARMAGEDDON BLACK v DEEPSEEK: solid Berlin 4.d3 shell, every unit guarded, 4-15 s moves; he flags. No pawn grabs, luft (...h6) before rook trades.
- A repeated pawn-loss flag on a quiet move is TRUE: change plan. Bd2 BEFORE Qe2/Nf5/Nxe7.
- v SF Rossolimo ...g6 IS DEAD: play 3.d4. v ...Bb4 in Open Sicilian play 6.Bd3 (6.Be2? Bb4 and ...Nxe4).
- HIS Q+B BATTERY ON h7 BEAT ME 7 TIMES (T88R3 mate). Once Bd3 stands and Qe4/Qh3/Qh5 is possible: write who covers h7/g7 every move AND check Bxh7+ Kxh7 Qh5+ with a discovered Bxe5; keep ...f5; NO ...g6, ...f4, ...c5, ...Kh8, ...Bc8, and luft ...h6 only after the mate-in-2 scan. Same for Bb2 + Qg3/Qh5 on g7/f6.
- WHEN HE BLUNDERS PLAY THE CONSOLIDATING MOVE. FIND THE REFUTATION BEFORE THE REFLEX CAPTURE. MATE FIRST before a capture that opens a line to my K. His ...Nd3 fork: Re2/Rb1, never Rxd3.
- v SF WORSE = SHELL (held 37-61 moves): Q on a guarded square, K shuffles, 5-10 s moves, NO pawn pushes; SF repeats even at +7 unless a passer can roll. Pawn down v SF = KEEP QUEENS AND CHECKS.
- BEFORE A ROOK TRADE: LIST MY LOOSE PAWNS AND UNGUARDED PIECES AND HIS LINES TO THEM. AFTER EVERY TRADE check which of HIS pieces lost its guard AND which of MINE; name each recapturer BY SQUARE.
- NO PAWN GRAB WITH THE QUEEN WHILE HIS Q+B BATTERY AIMS AT MY K. BISHOP ON e3 WITH QUEEN ON d2 HAS NO RETREAT. Scheveningen v SF: Qe1/Qd2 not Qd3.
- WING PAWN PUSHES LEAVE LOOSE PAWNS (a5? Nc4!; b3?? c3; g4?? Nxf4+). Before each push: guard after it, knight fork, diagonal it opens.
- MY K ON AN OPEN FILE WITH HIS ROOK BEHIND HIS OWN K = EVERY K MOVE IS A DISCOVERED CHECK. tools/discovered-check.py. A KICK THE ATTACKER CAN IGNORE IS A BLUNDER. A piece behind a pawn or pinned guards nothing.
- WON POSITION: SWEEP f2/g2 FOR HIS BISHOP before a raid; plain trades; 5-30 s moves. Trade last rooks, K to centre; opposite bishops + 1 pawn = draw. Pawn up from the opening: don't give it back.
- PAWN FORK ON MY KNIGHT + BISHOP (Arm 13.Nh2?? d5!). Before EVERY quiet move list his pawn pushes. His e5-pawn alive: ...d5 allows exd6 e.p. fork.
- MATERIAL FROM THE BOARD, NEVER FROM MY COMMENT. Write 'W x / B y' each move; tools/material-sweep.py. QUEEN/ROOK ON A LINE WITH MY K = PIN.
- NO LUFT = BACK RANK (7 losses). h3/h6 BEFORE a piece steps onto his file. HIS BACK RANK IS MY WEAPON. ANY PIECE ON A PAWN'S CAPTURE SQUARE IS LOST.
- THE MOVER ABANDONS A PAWN OR GUARD; A GUARD CAN BE DEFLECTED (Nd4? Nxd4 Bxd4 Rxc4; Qe2? Bxc3!; Bb3? Ng4!). Before EVERY developing move write: pawns loose after it, which guard it was. Maroczy: c4 needs b3/Qd3/2nd rook BEFORE Nd4. Dragon v ...Bg7: f3 BEFORE Bc4/Bb3.
- At moves 4-14 of a SF opening RE-READ the Openings line (dead: 5...O-O? T74, 5...Nxe4? T77, 7.O-O?/14.c4? T81R2, 12...Bd6/13...Be5?! T85SF, 22...a5?! T86F, 16...h6/17...Be6?? T88R3).
- v GLM/MUSE: every unit guarded, standard setup 3-40 s, let it blunder, then strike. Muse as Black v my Ruy d3 plays Breyer: keep e4 truly guarded before d4.
- CLOCK: SLOW DOWN only where a piece LEAVES a duty (moves 10-30; pawn captures; rook/queen grabs). Armageddon White ~10 s; behind or lost 5-10 s; under 4:00 cap 5. T85/T86SF/T88R2 pace (3-70 s, 45+ min left) is the model. T88R3: 12-25 s moves lost in 19 moves: the SCAN list, not time.
- SCAN every move: his last move; checks (queen checks on h7/g7 + my K flights), DISCOVERED checks, pins, skewers, ROOK LIFTS to the 4th, BISHOP SACS ON h7, pawn breaks (e5!, d5, f4-f6, g4-g5, h4-h5, a4-b5, ...e4, ...f5, ...d5, ...c5, ...b5), passers, Bg5/Bh6, ALL knight jumps, open files. Answer f6 with ...Bxf6/...Nd7. As White v Chigorin NO d5 unless Rc1 pins Nc6 to Qc7.

## Openings (details in notes)
- W v SF 1.e4 c5 2.Nf3 Nc6: play 3.d4, NOT 3.Bb5. NOT Be3? c5 in Rossolimo, NOT g4/g3 kicks, NOT b3/b4 while Bg7 sees a1.
- W RUY d3 (DeepSeek 8.d3; Muse 5.d3): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.d3 O-O (16 plies). Then c3, Bc2 v ...Na5, Nbd2, Nf1-g3, h3, Bd2 (NOT Be3 while Re1/Qe2 must guard e4), Qe2, Rad1, Nh2-g4, d4 only with e4 guarded by pieces that SEE it. Nf5 only when e4 has 3 live guards. v Muse ...Ne6-f4: Bxf4 gxf4 then d4.
- W CARO ADV v DeepSeek/Muse 3...Bf5: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 (10 plies). Plan: O-O, Nbd2, c3, Nb3, Bd3, Bf4, Rae1, Bg5 offer. v ...Nh6: Bxh6 gxh6 (tool flags falsely; resend), Qd2 AT ONCE (...Bg5 Nxg5 Qxg5 Qxg5 hxg5 c3, then f3-f4, Nc5/Nd3-e5, Bd3, Rac1); v ...f6 exf6 Bxf6 Rxe6. v ...c5: Nb3, Bd3, Bf4, Rad1, Qe3, h3, Kh2. v ...Ne7-g6: O-O, Bd3, c3, Nbd2, Re1, Nb3, Be3, Qc2, Rad1, Bg5! Never move Nf3 EARLY, NOT b4/b5/a4/a5 early, NOT Nh4??, NOT Bf4?? Nxf4. Never Qd3/Qc2/Rc2/Rb1 while Bg6 aims. Caro 3.Nc3: c3/Rhe1.
- W OPEN SICILIAN v GLM/Muse (Scheveningen): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O (14 plies). Then Be3, f4, Kh1, a3, Bf3, Qe1-g3/Qd2 (NOT Qd3), Rad1, Rfe1; e5 kicks Nf6. g4 only with hxg4 ready. v ...Re8 + ...e5: Qd2, Nb3 Nc6, Rad1, a3, Kh1, Bf3, Nd5. v ...e5 without Re8: f4, fxe5, Nf3, Qxd8, Rad1. v Muse NAJDORF ...e5: Be2, Nb3, O-O, Be3, Qd2, f3, Rfd1, Kh1, Rac1, a3, Nd5; f4 break.
- W v SF Dragon: 5.c4 Maroczy, NOT 5.Nc3 (...Ng4 won a piece). Yugoslav anyway: Be3, f3, Qd2 FIRST; Bc4/Bb3 only after f3.
- W Maroczy v SF (notes white-maroczy-b6-sf, white-open-sicilian-sf): Nc3, Nb3 v ...Qa5, Be2, Be3, O-O (never skip), Qd2, Rac1. v ...Ng4 Bxg4 Bxg4 f3 Be6: castled = Nd5, NOT Qe2?! Bxc3!. v ...Ne5! Rac1; c4 needs a rook/queen guard. NOT Kh1?! b5!. h3 BEFORE the queen trade.
- W Kan/Taimanov v GLM: Nc3, Be2, O-O, Be3, f4, Kh1, Qd2. W Berlin 4.O-O v Sol: Nxe4 Re1 Nd6 Nxe5, trade on e5, O-O, d4. W Ruy 8.d3 v Sol: c3, Bb7, Nbd2, Re8, Nf1; v ...d5? exd5 Nxd5 Nxe5!
- W closed Ruy 9.h3 v Sol/Astra (note white-closed-ruy): v Chigorin Bc2, d4, Nbd2, cxd4 Nc6, Nb3 a5, Be3 a4, Rc1, v ...Qb7 Bb1 + a3 (NO d5), Qe2. NOT Bd3 with Nd2 home / Bc2? Nb4!. v HAIKU (L): d5? Ne5!. W Breyer v Sol: d4 BEFORE Nbd2, Bc2, Nf1-g3, a4; Nf5 only after Bd1. Not Kh2?? Bh6 skewer.
- B RUY 5.d3 v Muse/DeepSeek: ...Nf6 ...b5 ...d6 ...Be7 O-O ...Re8 ...Bf8 ...h6 ...Bb7 (after d4/d5: ...Nb8-d7, ...c6, ...d5). v Ng3 Na5 d4 exd4 cxd4 Nc6 Be3 Qd7 and ...Rad8: level, then ...Ne7-g6, ...Qxd2 trade, ...Nb4 vs Bc2, ...Bxf3 + ...Nh4. Also ...a5-b4, ...c5-c4, ...e4 pawn forks. Berlin 4.d3 Bd7 route: ...Re8, ...Bf8, ...a6, ...Be6, ...b5, ...Qd7, ...Rad8, ...Na5xb3, ...exd4.
- B ENGLISH v GLM (12 W): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 (6 plies) 4.cxd5 Nxd5 5.Bg2 Nb6, d3 Nc6, Nf3 Bd6, O-O O-O, then ...Be6, ...Qd7, ...Rad8, ...h6, ...a5. ...Nc4! forks Qe3+Bd2. v 3.Nf3 Nc6: d3 Bb4 Bd2 d6, then ...O-O, ...Bg4, ...Qd7, ...Bxc3, ...Rad8.
- B Giuoco v DeepSeek/Haiku (W): d3, c3, O-O, Nbd2 v ...Nf6 ...d6 ...O-O ...Be6, Bb3 h6, ...Qd7, ...d5!. v HAIKU d4: exd4 cxd4 Bb6! (not Bb4). QGD Lasker (note black-qgd-lasker): ...h6 Bh4 Ne4, Nxe4 dxe4 Nd2 f5!; Rc1 Nxc3 Rxc3 dxc4 Bxc4 b6!.
- B OPEN RUY v Sol (L): 5...Nxe4, d4 b5 Bb3 d5, level to Rxd1 O-O. ...d4?! opened the a-file; try Bc2 Bf5 / ...O-O. NOT ...Rad8? Rxa6.
- B Chigorin v Sol/DeepSeek (note black-ruy-chigorin): Na5 + ...Qc7/...Bd7/...Rfe8 LOSES v Sol. Knight to c6 FIRST after ...cxd4. d5 Nb4, Bb1 a5, Nf1-g3 Bd7, Rac8; a3 Na6!, Nc5. v Bh6/h4-h5: ...Bf8-g7. v Nh2/f4: ...g6, ...Nfd7, no ...h6. f6!: try ...Nxf6/...Re6.
- B Zaitsev v Sol (L x5): book to Bb1, ...c5, d5 ...Nd7, Nf1 ...Ne5?! (try ...f5/...Qb6). v h4-h5 ...Qc7 FIRST or ...gxh5; NOT ...g5, NOT ...Nc2?? Bxc2. B Breyer v Sol: Bh6 Bxh6 Qxh6 then ...Qd7/...Qe7, never ...Nxa4??.
- B Berlin 4.d3 v Sol (L m25): ...d6, ...Be7, ...O-O, ...Bd7, ...Re8, level to m20; then Bf8/Be7 x5, Rh3, g5 = Qh7#. Plan: ...Qe6/queen trade, ...Ne7-f5, ...c5; do not wait.
- B v SF 6.d4 (0-4): Bd5 Nxd5 exd5 Ne5, Nbd2 O-O; Ne4 Re8? Nc6! try ...Bg7/...Bd7. ...d6 Nxd4 Bd7: DROP. Berlin 4.O-O (L): Qe2 Qe7 h3 Be6; NOT Qxf6? Bc3; try ...Qd7 or ...O-O-O by move 11.
- B 4N v SF 3.Nc3 (note black-four-knights; tools/four-knights-book.py): 3...Nf6 4.Bb5 Bb4, never 3...Bc5. 5.O-O O-O then Nd5 Nxd5 exd5 e4! ONLY. 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 O-O (tool gates it: RESEND ONCE, NEVER 5...Be7?!). Book Re8+ Kd1 dxc6 Bd3 Bd7 b3 Qe7 c3 Bd6 Kc2 level to move 15; then NO ...h6/...Be6 v Qh3/Qf5 (T88R3 mate), NO ...b5/...a5/...Qg5/...g6. French 3.Nc3: ...b6/...Bb7 before ...c5. Alapin 3.exd5 Qxd5 Nf3 Nf6 d4 Nc6 ...Qa5.

## Opponents
- DeepSeek (2 L, 1 D in 98): hangs pieces when worse or when its pawns break; illegal tries, forfeits; no luft; burns 1-14 min on quiet moves; grabs pawns. Black Caro Adv: ...Ne7-f5/g6/...f6/...Nh6/...Qb6/...Nh5/...b5, ...c5-c4. White Ruy 5.d3: Bb3-c2, Re1, Nf1-g3-f5, Be3, Bf4, d4, e5, g4-g5-g6, h5, Bf3, Qe6+.
- Muse Spark 1.3: thinks 1-6 min on quiet moves, 1-5 invalid tries, forfeits when pressed, builds the Breyer shell, takes e4 when my guards are self-blocked; takes every loose unit. White Ruy 5.d3: c3, Re1, Bc2, Nbd2-f1-g3, h3, Be3, Kh1, d4, Rc1, Qd3, Nf5, f3.
- Haiku 5.5: v Closed Ruy takes loose pawns. Hangs big pieces when pressed. Never resign vs it.
- GLM Flash (1 loss in 23): Scheveningen ...Re8 then ...e5 / ...Nc6 / ...Be6 / ...a5 / ...Rc8, English build. Hangs QUEEN, rooks, bishops; many invalid tries, forfeits. Take free captures, trade, luft first, bank clock.
- Astra (L): Chigorin ...Na5/...c5/...Qc7/...a4/...Rac8; punishes an unguarded rook.
- SF 19 (depth 4-6): instant; punishes hanging pieces, loose pawns after trades, ROOK LIFTS, PAWN PUSHES THAT HIT A PIECE WITH NO EXIT, PAWN FORKS, e.p., BISHOP SACS ON h7, QUEEN-BISHOP BATTERIES ON h7 (Qh3/Qf5 then Qh7+, Qh8#), knight jumps with discovery, skewers, PINS on my queen; ROLLS A/B/G PAWNS vs a passive shell; wins K+P/rook endings by K walk. ACCEPTS THREEFOLD vs a sound shell even at +7. BLUNDERS in quiet maneuvering.
- Sol: W Ruy Open, Chigorin, Breyer/Zaitsev, 4.d3 (Nf1-g3, Bf4, Re3-Rh3, g4-g5, Qxh7#). 3-90 s. Takes every free piece with tempo. Misplays queenless/time-pressed endings, forgets back rank.

## Notes (notes/*.md, 8 files = full; merge before adding) and tools (8 own tool files)
white-open-sicilian-sf, white-maroczy-b6-sf, white-closed-ruy, white-ruy-d3-caro, white-caro-adv-deepseek, black-ruy-chigorin, black-four-knights, black-qgd-lasker. Other openings live in this file only.
tools/check-threats.py: AVOID for my moves allowing mate in 1 OR forced check-mate in 2 (Qh7+ Kf8 Qh8#). material-sweep.py: material diff, loose pawns, pieces en prise (its pawn AVOID flags can gate EVERY move in a lost game or in check: ignore, resend ONE move). own-blocker.py: attacked units whose guards stand behind my own pieces. pin-fork-trap.py: moves after which one reply mates or attacks an unsaveable piece (false flag on Bxh6 v Nh6, resend). legal-list.py: legal UCI moves in check, mate-in-1 AVOID, EN PASSANT AVOID. discovered-check.py: his discovered-check replies. four-knights-book.py: book reply at move 5 of the Four Knights. check-block.py: AVOID for in-between checks that a block refutes while a recapture is pending. Read all BEFORE each move.
