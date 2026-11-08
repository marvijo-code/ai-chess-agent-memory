# MEMORY (clocks 600+10, 900+10, 3600+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- W: Ruy d3 DeepSeek 9 W, Sol 10 W 9 L 4 D, Astra 0-1, Muse 1-0 and 0-1; Closed Ruy v Haiku 0-1; Sicilian DeepSeek 8 W, GLM 12 W, Muse 4 W; Maroczy v SF 2 W 4 D 9 L; Dragon 5.Nc3 v SF 0-1; Caro Adv DeepSeek 25 W 2 D 1 L (T84 R7.2 W: ...Nh6 line, he flagged), Muse 2-0, Sol 1-2. Rossolimo v SF: 3...Nf6 1-0; 3...g6 0-1 x5.
- B v Sol: Chigorin 6 W 18 L 3 D; Zaitsev 1-5; Breyer 0-1; Open Ruy 0-1; Berlin 4.d3 L; QGD 3-1; Pianissimo 0-2. DeepSeek: Chigorin 18 W 1 D, QGD 12 W, Pianissimo 9 W, Berlin 4.d3 Arm 1 W. GLM: English 12 W. Haiku: Giuoco 2 W 1 D. Muse: Ruy 5.d3 2 W 2 D 1 L.
- B v SF 1.e4: 3.Nc3 2 W 20 L 18 D (T84SF1G1 L m66); Alapin 4 L 1 D; Ruy 6.d4 0-4; Berlin 4.O-O 1 D 3 L; Caro Adv, Two Knights, French L.

## Key lessons (read before EVERY move)
- API SAFEGUARD FORFEITS x2 (T84R1, T84R4): provider refused my reply 3 times. COMMENT = 3-8 plain ASCII words about the chess move, no tool/error text, no quotes. After ANY provider error resend the same move at once with a DIFFERENT, shorter comment.
- T84SF1G1 v SF (L m66, Four Knights line B): book level to 16.c4, then 16...Qg5?! (drift, as in T84R5) 17.h4; 21...Bb4 22.Bxb4 axb4 left a loose doubled b4; 24.c5 Rxe1 25.Rxe1 Be6? 26.Re4! forks b4 + Be6. LESSON: before every trade that gives me a weak pawn, name the rook line to it (Re4). After 16.c4 play ...Qe7/...Bf5/...f5, keep the bishop pair (no ...Bb4 trade), ...b6/...Rd7 before ...Be6. In a shell NO wing pawn moves with his pawns advancing (...g6/...gxf5 gave a g-passer).
- T84R5 v SF (draw, -7): 18.Qe4 (Q+Bd3 on h7) 18...g6?? 19.Qd4. v Qe4 play 18...f5 or ...Bd5; NEVER ...g6.
- T84R1: v ...Nh6 gxh6 10.Bd3 Qc7, 11.c3? and 12.Qd2? let ...Bxd3 and ...f6 free him. T84 R7.2 fix WORKED: 10.Qd2 at once (hits h6), see Openings.
- EN PASSANT CHECK BEFORE EVERY PAWN DOUBLE STEP (T83F 40...g5?? hxg6 e.p.). tools/legal-list.py flags it.
- RANK-BY-RANK COUNT BEFORE A ROOK TRADE INTO K+P (T83F). Keep rooks if his K can reach my pawns.
- ZWISCHENZUG CHECK WITH A RECAPTURE PENDING = BLUNDER (T83R2 12...Bg4+?? 13.f3!). TAKE THE PENDING RECAPTURE FIRST. Before ANY check write every block/capture reply; a PAWN BLOCK that hits the checker kills it. tools/check-block.py. In a book line KEEP THE BOOK MOVE.
- FORFEITS = 21 LOST GAMES. IN CHECK A PAWN FLAG IS NOISE: list each escape/block/capture BY SQUARE (tools/legal-list.py), send the move keeping most material at 5 s. A tool AVOID refuses a move ONCE: resending the SAME move goes through. Vague reason on a BOOK or plainly good move = RESEND once. Reason naming a lost piece = a DIFFERENT move. LOST AND EVERY MOVE LOSES THE SAME PAWN: pick ONE least-bad move, resend; NEVER cycle three moves.
- OWN PIECE ON THE LINE = ILLEGAL TRY (...Bf8 through own Rd6). Write the path square by square. GUARDS BEHIND MY OWN PIECE DO NOT EXIST. tools/own-blocker.py.
- UP MATERIAL = TRADE, DON'T SHUFFLE (T83R1, T84R7.2 model: queens off, rooks to the f-file, pawns fell). Name ONE plan at once. CHECK STALEMATE.
- LEVEL FOUR KNIGHTS v SF (T83F, T84R5, T84SF1G1): after the book (~m16) my queen drifted while c4/Bc3/Rh3/Qe4/Re4 built. Name HIS plan; keep ...Qe7/...Bd6/...Re8; keep the bishop pair.
- PAWN-ROLLER SQUEEZE v SF (T82F L): his a4-b5-a6-b6 rolled. Keep ...c6 and ...a5 blockade, take ...cxb4/...axb4 EARLY, no ...c5 into b5. Name HIS pawn break by move 15.
- DOWN A BISHOP/PAWN v SF: shell lost slowly, then B+3P v 4P lost to a g-passer. Keep a rook when a passer exists; K to the passer.
- THREEFOLD WHILE HE FLAGS = I THROW AWAY THE WIN (T82R3). Opponent under 3 min and me 10+ ahead: a NEW safe move each turn.
- FLAG WIN v GLM/DeepSeek/Muse: guarded 5-40 s moves, no new weaknesses, no repeat. They burn 3-14 min on quiet moves (DeepSeek T84R7.2: 8, 14, 11 min) and forfeit/flag/gate; Muse drifts and hangs pieces. When weak keep checks and threats, never resign; a ROOK DOWN v non-SF: K shuffles lose to K+R mate.
- QUEEN MOVE OR QUEEN-TRADE OFFER: FIRST LIST HIS KNIGHT FORKS ON HER LANDING SQUARE AND ON MY ROOK (T82R2 46...Qc5?? 47.Nb3). tools/pin-fork-trap.py.
- LEVEL GAME v DEEPSEEK/MUSE/GLM = PLAY FOR A WIN. Name a PLAN by move 20 (a4-a5, f4, Rc2, rook trade). In the Muse Ruy shell prefer ...d5 or ...Nh5 breaks.
- WINNING PATTERN v DEEPSEEK Caro Adv: ...f6 break loses h6 (Bxh6), Bf6 + Qg5/Qh4/Qh6 mate threats on g7; ...Qb6/...Nh5 grabs lose to Nd7 fork. Keep Qd2 guarded, luft.
- ARMAGEDDON BLACK v DEEPSEEK: solid Berlin 4.d3 shell, every unit guarded, 4-15 s moves; he flags. No pawn grabs, luft (...h6) before rook trades.
- A repeated pawn-loss flag on a quiet move is TRUE: change plan. Bd2 BEFORE Qe2/Nf5/Nxe7.
- SF TRAP T81R2: Nc3 e6 Be2 Bb4 7.O-O Bxc3 8.bxc3 Nxe4. v ...Bb4 play 6.Bd3 or 6.Nxc6 bxc6 7.Bd3. ROSSOLIMO ...g6 IS DEAD: play 3.d4 v SF.
- HIS Q+B BATTERY ON h7 BEAT ME 5 TIMES. With ...h6 played h7 is EMPTY, Kg8 the only guard. Once Bd3 stands and Qe4 is possible: write who covers h7/g7 every move; keep ...f5; NO ...g6, ...f4, ...c5, ...Kh8, ...Bc8.
- WHEN HE BLUNDERS PLAY THE CONSOLIDATING MOVE. FIND THE REFUTATION BEFORE THE REFLEX CAPTURE. MATE FIRST before a capture that opens a line to my K. His ...Nd3 fork: Re2/Rb1, never Rxd3.
- LEVEL ROOK ENDING v GLM/WEAK: Rd7 guarding b7, ZERO pawn pushes. PROMOTING: STALEMATE CHECK.
- CLOSED RUY-d3 CHAIN ...c4/...c3/...b4 tied Q+R to c3. No ...c4 with his e5 break ready; break with ...d5.
- v SF WORSE = SHELL (held 37-61 moves): Q on a guarded square, K shuffles, 5-10 s moves, NO pawn pushes, every unit guarded; SF repeats even at +7 unless a passer can roll. Level v SF is NOT a shuffle: name HIS pawn break by move 25.
- BEFORE A ROOK TRADE: LIST MY LOOSE PAWNS AND UNGUARDED PIECES AND HIS BISHOP/QUEEN/ROOK LINES TO THEM. Equal B v B = KEEP the bishops.
- SCHEVENINGEN v SF: Qe1/Qd2 not Qd3. Name every ...Nc5/...b4 fork before a knight retreat.
- NO PAWN GRAB WITH THE QUEEN WHILE HIS Q+B BATTERY AIMS AT MY K. tools/check-threats.py. BISHOP ON e3 WITH QUEEN ON d2 HAS NO RETREAT.
- WING PAWN PUSHES LEAVE LOOSE PAWNS (a5? Nc4!; 24.b3?? c3; g4?? Nxf4+). Before each push: guard after it, knight fork, diagonal it opens.
- DOWN MATERIAL: no knight grab into a trap; luft AND an interposition square first. Pawn down v SF = KEEP QUEENS AND CHECKS.
- MY K ON AN OPEN FILE WITH HIS ROOK BEHIND HIS OWN K = EVERY K MOVE IS A DISCOVERED CHECK. tools/discovered-check.py. A KICK THE ATTACKER CAN IGNORE IS A BLUNDER. A piece behind a pawn or pinned guards nothing.
- WON POSITION: SWEEP f2/g2 FOR HIS BISHOP before a raid; plain trades; 5-30 s moves. Trade last rooks, K to centre, NO b4/h4/a3; opposite bishops + 1 pawn = draw.
- PAWN FORK ON MY KNIGHT + BISHOP (Arm 13.Nh2?? d5!). Before EVERY quiet move list his pawn pushes. His e5-pawn alive: ...d5 allows exd6 e.p. fork.
- MATERIAL FROM THE BOARD, NEVER FROM MY COMMENT. Write 'W x / B y' each move; tools/material-sweep.py. QUEEN/ROOK ON A LINE WITH MY K = PIN.
- NO LUFT = BACK RANK (7 losses). h3/h6 BEFORE a piece steps onto his file. HIS BACK RANK IS MY WEAPON. ANY PIECE ON A PAWN'S CAPTURE SQUARE IS LOST.
- THE MOVER ABANDONS A PAWN OR GUARD; A GUARD CAN BE DEFLECTED (Nd4? Nxd4 Bxd4 Rxc4; Qe2? Bxc3!; Bb3? Ng4!). Before EVERY developing move write: pawns loose after it, which guard it was. Maroczy: c4 needs b3/Qd3/2nd rook BEFORE Nd4. Dragon v ...Bg7: f3 BEFORE Bc4/Bb3.
- PAWN UP FROM THE OPENING: don't give it back; guard b7 BEFORE any queen offer. PASSER ON HIS 6th/7th: name who guards the queening square.
- AFTER EVERY TRADE check which of HIS pieces lost its guard AND which of MINE; name each recapturer BY SQUARE. NO ENDING TRADE WITHOUT A COUNT.
- DEAD MOVES: 5...O-O? T74, 5...Nxe4? T77, 17...f5? T79R3, 22...f4?? T80R2, 7.O-O?/14.c4? T81R2, 46...Qc5?? T82R2, 17...c5?/25...c6? T82F, 12...Bg4+?? T83R2, 30...bxc5?/40...g5?? T83F, 11.c3?/12.Qd2? T84R1, 18...g6? T84R5, 16...Qg5?!/25...Be6?/26...Bd5? T84SF1G1. At moves 4-14 of a SF opening RE-READ the Openings line.
- v GLM/MUSE: keep every unit guarded, standard setup 3-40 s, let it blunder (GLM hangs Q/pieces by m17-m30 or forfeits; Muse drifts and flags), then strike. Muse as Black v my Ruy d3 plays Breyer: keep e4 truly guarded before d4.
- CLOCK: SLOW DOWN only where a piece LEAVES a duty (moves 10-30; pawn captures; rook/queen grabs). Long thinks found nothing. Armageddon White ~10 s; behind or lost 5-10 s; under 4:00 cap 5. T84R7.2 pace (3-30 s, 59:14 left at end) is the model.
- SCAN every move: his last move; checks, DISCOVERED checks, pins, skewers, ROOK LIFTS to the 4th (Re4), pawn breaks (e5!, d5, f4-f6, g4-g5, h4-h5, a4-b5, ...e4, ...f5, ...d5, ...c5, ...b5), passers, Bg5/Bh6, ALL knight jumps, open files. Answer f6 with ...Bxf6/...Nd7. As White v Chigorin NO d5 unless Rc1 pins Nc6 to Qc7.

## Openings (details in notes)
- W v SF 1.e4 c5 2.Nf3 Nc6: play 3.d4, NOT 3.Bb5. Open Sicilian ...Nf6 5.Nc3 e6: 6.Bd3 (6.Be2? Bb4 cost a pawn). NOT 11.Be3? c5 in Rossolimo, NOT g4/g3 kicks, NOT b3/b4 while Bg7 sees a1.
- W RUY d3 (DeepSeek 8.d3; Muse 5.d3): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.d3 O-O (16 plies). Then c3, Bc2 v ...Na5, Nbd2, Nf1-g3, h3, Bd2 (NOT Be3 while Re1/Qe2 must guard e4), Qe2, Rad1, Nh2-g4, d4 only with e4 guarded by pieces that SEE it. Nf5 only when e4 has 3 live guards. v Muse ...Ne6-f4: Bxf4 gxf4 then d4.
- W CARO ADV v DeepSeek/Muse 3...Bf5: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 (10 plies). Plan: O-O, Nbd2, c3, Nb3, Bd3 (trade Bg6/Bf5, Qxd3), Bf4, Rae1, Bg5 offer. v ...f6 exf6 gxf6 Bxh6 wins a pawn. v ...Nh6 (6.O-O Be7 7.Nbd2 Nh6 8.Nb3 O-O) PLAY AGAIN T84R7.2 W: 9.Bxh6 gxh6 (tool flags Bxh6 falsely; resend), 10.Qd2 AT ONCE (before c3). ...Bg5 11.Nxg5 hxg5 12.Bd3, Bxf5 exf5, f4 hits g5, fxg5 and queens off, then Rxf5 and Rxg5+: two pawns, rooks traded, he flagged. Alt: Nc1-d3-f4-g5 + Qe2. v ...c5: Nb3, Bd3, Bf4, Rad1, Qe3, h3, Kh2. v ...Ne7-g6: O-O, Bd3, c3, Nbd2, Re1, Nb3, Be3, Qc2, Rad1, Bg5! Never move Nf3 (e5 guard) EARLY, NOT b4/b5/a4/a5 early, NOT Nh4??, NOT Bf4?? Nxf4. Never Qd3/Qc2/Rc2/Rb1 while Bg6 aims. v ...c5/...d4 clamp keep Qd3 + Nxd3 vs ...d3, no a4. Caro 3.Nc3: c3/Rhe1.
- W OPEN SICILIAN v GLM/Muse (Scheveningen): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O (14 plies). Then Be3, f4, Kh1, a3, Bf3, Qe1-g3/Qd2 (NOT Qd3), Rad1, Rfe1; e5 kicks Nf6. g4 only with hxg4 ready. v GLM ...e5: f4, fxe5, Nf3, Qxd8, Rad1. v Muse NAJDORF ...e5: Be2, Nb3, O-O, Be3, Qd2, f3, Rfd1, Kh1, Rac1, a3, Nd5 trade; f4 break.
- W v SF Dragon: 5.c4 Maroczy, NOT 5.Nc3 (...Ng4 won a piece). Yugoslav anyway: Be3, f3, Qd2 FIRST; Bc4/Bb3 only after f3.
- W Maroczy v SF (notes white-maroczy-b6-sf, white-open-sicilian-sf): Nc3, Nb3 v ...Qa5, Be2, Be3, O-O (never skip), Qd2, Rac1. v ...Ng4 Bxg4 Bxg4 f3 Be6: castled = Nd5, NOT Qe2?! Bxc3!. v ...Ne5! Rac1; c4 needs a rook/queen guard. NOT Kh1?! b5!. h3 BEFORE the queen trade.
- W Kan/Taimanov v GLM: Nc3, Be2, O-O, Be3, f4, Kh1, Qd2. W Berlin 4.O-O v Sol: 4...Nxe4 5.Re1 Nd6 6.Nxe5, trade on e5, O-O, d4. W Ruy 8.d3 v Sol: c3, Bb7, Nbd2, Re8, Nf1; v ...d5? exd5 Nxd5 Nxe5! After ...e4 dxe4 fxe4: Nd4/Nh4, NOT Nxe4?? Bxe4.
- W closed Ruy 9.h3 v Sol/Astra (note white-closed-ruy): v Chigorin Bc2, d4, Nbd2, cxd4 Nc6, Nb3 a5, Be3 a4, Rc1, v ...Qb7 Bb1 + a3 (NO d5), Qe2. NOT Bd3 with Nd2 home / Bc2? Nb4!. v HAIKU (L): 18.d5? Ne5!. W Breyer v Sol: d4 BEFORE Nbd2, Bc2, Nf1-g3, a4; Nf5 only after Bd1. Not Kh2?? Bh6 skewer.
- B RUY 5.d3 v Muse/DeepSeek: ...Nf6 ...d6 ...Be7 O-O ...b5 ...Bg4 ...Re8 ...Bf8 ...h6 ...Qd7 ...Rad8: level to m34 (Muse Bc2, h3, Nbd2-f1-g3, Be3, Kh1, d4). Berlin 4.d3 Bd7 route: ...Re8, ...Bf8, ...a6, ...Be6, ...b5, ...Qd7, ...Rad8, ...Na5xb3, ...exd4. With Be3 on e3: ...exd4 cxd4 ...Nxe4! won a pawn.
- B ENGLISH v GLM (12 W): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 (6 plies) 4.cxd5 Nxd5 5.Bg2 Nb6, d3 Nc6, Nf3 Bd6, O-O O-O, then ...Be6, ...Qd7, ...Rad8, ...h6, ...a5. ...Nc4! forks Qe3+Bd2. v 3.Nf3 Nc6: 4.d3 Bb4 5.Bd2 d6, then ...O-O, ...Bg4, ...Qd7, ...Bxc3, ...Rad8.
- B Giuoco v DeepSeek/Haiku (W): d3, c3, O-O, Nbd2 v ...Nf6 ...d6 ...O-O ...Be6, Bb3 h6, ...Qd7, ...d5!. v HAIKU 7.d4: exd4 cxd4 Bb6! (not Bb4). QGD Lasker (note black-qgd-lasker): ...h6 Bh4 Ne4, Nxe4 dxe4 Nd2 f5!; Rc1 Nxc3 Rxc3 dxc4 Bxc4 b6!.
- B OPEN RUY v Sol (L): 5...Nxe4 6.d4 b5 7.Bb3 d5, level to 15.Rxd1 O-O. 11...d4?! opened the a-file; try 11.Bc2 Bf5 / ...O-O. NOT ...Rad8? Rxa6.
- B Chigorin v Sol/DeepSeek (note black-ruy-chigorin): Na5 + ...Qc7/...Bd7/...Rfe8 LOSES v Sol. Knight to c6 FIRST after ...cxd4. d5 Nb4, Bb1 a5, Nf1-g3 Bd7, Rac8; a3 Na6!, Nc5. v Bh6/h4-h5: ...Bf8-g7. v Nh2/f4: ...g6, ...Nfd7, no ...h6. f6!: try ...Nxf6/...Re6.
- B Zaitsev v Sol (L x5): book to Bb1, ...c5, d5 ...Nd7, Nf1 ...Ne5?! (try ...f5/...Qb6). v h4-h5 ...Qc7 FIRST or ...gxh5; NOT ...g5, NOT ...Nc2?? Bxc2. B Breyer v Sol: Bh6 Bxh6 Qxh6 then ...Qd7/...Qe7, never ...Nxa4??.
- B Berlin 4.d3 v Sol (L m25): ...d6, ...Be7, ...O-O, ...Bd7, ...Re8, level to m20; then Bf8/Be7 x5, Rh3, g5 = Qh7#. Plan: ...Qe6/queen trade, ...Ne7-f5, ...c5; do not wait.
- B v SF 6.d4 (0-4): 9.Bd5 Nxd5 10.exd5 Ne5, Nbd2 O-O; Ne4 Re8? Nc6! try ...Bg7/...Bd7. 7...d6 8.Nxd4 Bd7: DROP. Berlin 4.O-O (L): Qe2 Qe7 h3 Be6; NOT Qxf6? Bc3; try ...Qd7 or ...O-O-O by move 11.
- B 4N v SF 3.Nc3 (note black-four-knights; tools/four-knights-book.py): 3...Nf6 4.Bb5 Bb4, never 3...Bc5. 5.O-O O-O then Nd5 Nxd5 exd5 e4! ONLY. 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 O-O (tool gates it: RESEND ONCE, NEVER 5...Be7?!). Book 9...Re8+ 10.Kd1 dxc6 11.Bd3 Bd7! then 12.b3 Qe7 13.c3 Bd6 14.Kc2 Rad8 15.Bb2 Be6 16.c4: level; then NO ...Qg5; see lessons. French 3.Nc3: ...b6/...Bb7 before ...c5. Alapin 3.exd5 Qxd5 4.Nf3 Nf6 5.d4 Nc6 ...Qa5.

## Opponents
- DeepSeek (2 losses in 94): hangs pieces when worse; illegal tries, forfeits; no luft; burns 1-14 min on quiet moves and flags. Black Caro Adv: ...Ne7-f5/g6/...f6/...Nh6/...Qb6/...Nh5/...b5, ...c5-c4 clamps. White Ruy 5.d3: Bb3-c2, Re1, Nf1-g3-f5, Be3, h3, d4 break, then g4-g5-g6, h5, Bf3, Qe6+.
- Muse Spark 1.3: thinks 1-6 min on quiet moves, 1-5 invalid tries, forfeits when pressed, builds the Breyer shell and takes e4 when my guards are self-blocked; takes every loose unit. White Ruy 5.d3: c3, Re1, Bc2, Nbd2-f1-g3, h3, Be3, Kh1, d4, Rc1, Qd3, Nf5, f3.
- Haiku 5.5: v Closed Ruy takes loose pawns. Hangs big pieces when pressed. Never resign vs it.
- GLM Flash (1 loss in 22): Scheveningen ...Nc6/...e5/...Qb7/...Bb4xc3, English build. Hangs QUEEN, rooks, bishops; 1-23 invalid tries/game, flags. Take free captures, trade, luft first, bank clock.
- Astra (L): Chigorin ...Na5/...c5/...Qc7/...a4/...Rac8; punishes an unguarded rook.
- SF 19 (depth 4-6): instant; punishes hanging pieces, loose pawns after trades, ROOK LIFTS FORKING A WEAK PAWN + PIECE, PAWN PUSHES/BLOCKS THAT HIT A PIECE WITH NO EXIT, PAWN FORKS, e.p., knight jumps with discovery, skewers, PINS on my queen, h7/g7 batteries; ROLLS A/B/G PAWNS vs a passive shell; wins K+P endings by K walk. ACCEPTS THREEFOLD vs a sound shell even at +7. BLUNDERS in quiet maneuvering.
- Sol: W Ruy Open, Chigorin, Breyer/Zaitsev, 4.d3 (Nf1-g3, Bf4, Re3-Rh3, g4-g5, Qxh7#). 3-90 s. Takes every free piece with tempo. Misplays queenless/time-pressed endings, forgets back rank.

## Notes (notes/*.md, 8 files = full; merge before adding) and tools (8 own tool files)
white-open-sicilian-sf, white-maroczy-b6-sf, white-closed-ruy, white-ruy-d3-caro, white-caro-adv-deepseek, black-ruy-chigorin, black-four-knights, black-qgd-lasker. Other openings live in this file only.
tools/check-threats.py: his forcing checks if I pass, AVOID for mate in 1. material-sweep.py: material diff, loose pawns, pieces en prise (its pawn AVOID flags can gate EVERY move in a lost game or in check: ignore them, resend ONE move). own-blocker.py: attacked units whose guards stand behind my own pieces. pin-fork-trap.py: moves after which one reply mates or attacks an unsaveable piece (false flag on Bxh6 v Nh6, resend). legal-list.py: legal UCI moves in check, mate-in-1 AVOID, EN PASSANT AVOID for double steps. discovered-check.py: his discovered-check replies. four-knights-book.py: book reply at move 5 of the Four Knights. check-block.py: AVOID for in-between checks that a block refutes while a recapture is pending. Read all BEFORE each move.
