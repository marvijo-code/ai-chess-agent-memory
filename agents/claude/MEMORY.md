# MEMORY (clocks 600+10, 900+10, 3600+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- W: Ruy DeepSeek 8 W, Sol 10 W 9 L 4 D, Astra 0-1; Closed Ruy v Haiku 0-1; Sicilian DeepSeek 8 W, GLM 8 W (T75R3 Scheveningen mate m35), Fable W, Muse W; Maroczy v SF 2 W 4 D 9 L; Dragon 5.Nc3 v SF 0-1; Caro Adv Sol 1-2, DeepSeek 13 W 1 D, Muse 1-0; Caro 3.Nc3 v Sol 0-2. ROSSOLIMO v SF: 3...Nf6 1-0 (T73 Final); 3...g6 0-1 (T74 Final Arm).
- B v Sol: Chigorin 6 W 18 L 3 D; Zaitsev 1-5; Breyer 0-1; Open Ruy 0-1; Ruy 4.d3 1-1; Berlin 4.d3 L; QGD 3-1; Pianissimo 0-2. DeepSeek: Chigorin 17 W 1 D, QGD 12 W, Pianissimo 9 W, Ruy 4.d3 Armageddon DRAW. GLM: English 7 W. Haiku: Giuoco 2 W 1 D. Muse: Ruy 4.d3 T75R2 DRAW m51.
- B v SF 1.e4: 3.Nc3 1 W 12 L 16 D; Alapin 4 L 1 D; Ruy 6.d4 0-4; Berlin 4.O-O 1 D 3 L; Caro Adv, Two Knights, French L.

## Key lessons (read before EVERY move)
- BIG CLOCK LEAD + EVEN GAME = PLAY A PLAN, NOT WAITING MOVES (T75R2 v Muse, drew m51 at 57:00 v 3:00). 20 moves of K/rook shuffles at 5-10 s; SF marked Kh7?, Re7?, Bf6??. Muse plays 5-30 s when short and the +10 keeps it at 3-4 min: it does not flag. When ahead on the clock spend 30-60 s on a pawn plan that cannot repeat (...f5, ...a4, ...Bg5 trades), keep every unit guarded, count repeats by position. Only Armageddon Black wants a shuffle draw.
- PAWN FORK ON MY KNIGHT + BISHOP (T74 Final Arm, lost m15): Nc4 + Be3 + Nh2 wander; 13.Nh2?? d5! then ...d4. Before EVERY quiet move list his pawn pushes (d5, d4, e4, f5, b5) and what they hit. No Nc4 while ...d5 is possible; build with c3/d4 or Nf1-g3.
- FOUR KNIGHTS 5.Nd5: ONLY 5...Nxd5 (5...O-O? 6.Bxc6!). At moves 4-8 of a SF opening RE-READ the Openings line and play it. A piece-down shell held 75 moves: Qf7/Qf8 + Rd8, K shuffle, 5-30 s moves.
- ARMAGEDDON BLACK = A DRAW WINS (DeepSeek 4.d3 shell, pawn up, Qd3/Qd2 repeat). Guarded setup, 5-15 s moves, take the threefold. DeepSeek burns its clock.
- MATERIAL FROM THE BOARD, NEVER FROM MY COMMENT. Write 'W x / B y' each move; tools/material-sweep.py. A PAWN FORK FIRST NEEDS HIS IN-BETWEEN MOVE.
- A PIECE UP: CONVERT, DON'T DRIFT (T74SF2G1G1 won a bishop m25, drew m57). Trade the LAST rooks, K to the centre before his K, NO b4/h4/a3, pawns compact, name his passers and my loose pawns. Repetition with a 5x clock lead is a failure (except Armageddon Black).
- BISHOP ENDING v SF (T74R3 L): ...h6? allowed h4-h5, g4-g5; 33...Bxe5? 34.Kxe5 was a LOST K+P ending. Never trade last bishops while his K is central and his pawns are further on. K+P trade = count opposition, entry squares, passers FIRST.
- QUEEN/ROOK ON A LINE WITH MY K = PIN (24.Rc7?? Be3!). Qf2/Qe1/Qd2 v Kg1 with his dark bishop reaching e3/d4/c5/b6 = never. tools/pin-fork-trap.py.
- A QUEEN-TRADE OFFER THAT LEAVES A DUTY (39.Qc1??): list what the queen guarded before shuffles. 47.g5?? cut my own chain.
- A TOOL-REFUSED CAPTURE IS AN ORDER. Change piece AND idea; never resend. ILLEGAL x3 = forfeit (10 times).
- PROVIDER ERROR / INVALID TRIES (T74 Final Arm: 2 tries on EVERY move from m33, forfeit m37 with 1:51 left): send a SHORT comment with explicit from-to squares; a 20-50 s think in a lost game costs the clock.
- LEGAL KING MOVES: Q v K gave 18 invalid tries. Run tools/legal-list.py, play ONLY a listed move; it flags mate in 1.
- DISCOVERED ATTACK ON A LOOSE QUEEN/ROOK WINS MATERIAL (T73 Final 23.Bc3! Rd3). KNIGHT FORK ON A QUEEN + LOOSE BISHOP WINS (T74R2 ...Nc4): list every knight jump hitting two units.
- NO LUFT = BACK RANK (7 losses: Rc6?? Rb1+; 31.Nd4?? Nd7 pinned to the back rank). Kg1 behind f2/g2/h2 + a file his heavy piece reaches = mate; h3 BEFORE a piece steps onto his file. HIS BACK RANK IS MY WEAPON (T75R3 Rd8+ Bf8 Rxf8# with Rg3 covering g7/g8).
- ANY PIECE ON A PAWN'S CAPTURE SQUARE IS LOST (Rh5?? gxh5; Qxc6?? bxc6; Qd1?? cxd1=Q+). Before ANY queen/rook/minor move write the pawns that hit the destination, then pieces.
- TRACE LINES SQUARE BY SQUARE; MY OWN AND HIS PIECES BLOCK (27...Rxa2?? own a7). A piece behind a pawn or pinned guards nothing.
- THE MOVER ABANDONS A PAWN OR GUARD; A GUARD CAN BE DEFLECTED (Nd4? Nxd4 Bxd4 Rxc4; Qe2? Bxc3!; Bb3? Ng4!; Nh4? fxe5). Before EVERY developing/knight/rook move write: pawns loose after it, which guard it was, which capture removes a guard with tempo. Maroczy: c4 needs b3/Qd3/2nd rook BEFORE Nd4. Dragon v ...Bg7: f3 BEFORE Bc4/Bb3.
- A PAWN UP FROM THE OPENING: DON'T GIVE IT BACK BY A PAWN BREAK (28.b3?! cxb3). Guard b7 BEFORE any queen offer.
- PAWN DOWN v SF = KEEP QUEENS AND CHECKS; queen trade only after counting his passers by file and my K distance.
- LOST/WORSE v A WEAK PLAYER: keep checks and threats, never resign (Haiku hung a rook after 60 shuffles; GLM hangs Q and knights; DeepSeek and Muse flag).
- DOWN MATERIAL v SF: fortress, not counterplay; never open a file or push a pawn; 5-10 s moves. A THREEFOLD IS A RESULT: never resign. EQUAL ENDING v SF DRIFTS: pick a plan at once, compact pawns.
- PASSER ON HIS 6th/7th: name who guards the queening square and the check after (Rxb2?? d8=Q+). SKEWER: Q in front of R/K on one line (Kh2?? Bh6!).
- UP MATERIAL, QUEENS OFF: trade queens/rooks, K to his passers only when nothing is trappable, loose pawns only with a traced recapture, 3-10 s moves, stalemate check. OPPOSITE BISHOPS + 1 PAWN = DRAW. Models: T39F, T44R2, T73 Final, T74R1, T75R3.
- MATE FIRST BEFORE A CAPTURE THAT OPENS A LINE TO MY K (hxg5?? Qh7#).
- THE SAME HOLE IN HIS PLAY WINS: after every trade check which of HIS pieces lost its guard (DeepSeek ...Bc5??; GLM ...Ng4?? hung to Bxg4 with Nd7 blocking its queen; 28.Qb2?? ...Nxe3). RECAPTURE ORDER WHEN UP A PIECE: take with the piece whose loss costs least. ATTACKED PIECE = LIST RETREATS BEFORE ANY 'TEMPO' SAC. ALL KNIGHT JUMPS before a rook/piece lands (Re1?? Nxe1).
- NO GRABS v SF. NO ENDING TRADE WITHOUT A COUNT. Equal B v B = KEEP the bishops.
- A PAWN MOVE OPENS A LINE AND HIS SCREEN PIECE MOVES WITH TEMPO (b3?? Nxc4!; b3?? Rxb3; Bf4?? Nxf4): list the line and each capture his blocker can make.
- A NOTE THAT NAMES THE FIX IS AN ORDER. A move on a NOT list is dead (d5? T71R2, Qf2?!/Rc7?? T73R2, Nc3/Bb3 T40Arm, 5...O-O? T74). Re-read the Openings line BEFORE 'improving'.
- TRADE OFFER = NAME EACH RECAPTURER BY SQUARE: the mover is not one, it must not be hit, its capture must not remove a guard (Rc1?? Rxc1+; Bd3?? Nxd3).
- HIS PAWNS GET LOOSE WHEN HIS PIECES STACK ON ONE WING: count attackers v guards, take one with a clean recapture.
- v GLM (T75R3): keep every unit guarded, play the standard setup 3-40 s, let it blunder (it dropped a knight, then the exchange to a Nxd6 fork on Qc4/Rc8/Bb7), then trade queens and use its king box. Before my own pawn-up capture check the b-pawn fork: axb4 then b5 kept the pawn.
- CLOCK: SLOW DOWN only where a piece LEAVES a duty (moves 15-30 of an equal opening; captures with a pawn on his 6th; rook/queen grabs) or when I lead and need a plan. Armageddon White ~10 s; behind or lost 5-10 s; under 4:00 cap 5. DeepSeek and Muse burn their clocks: bank time, but a lead does not flag Muse.
- PASSIVE (T30SF2G1, T40R4, T74SF2G1G1, T75R2): pick a plan BEFORE his break; rook BEHIND a passer or blockade it; v a K walk stop it early; v a pawn storm hit the centre/other wing.
- SCAN every move: his last move; checks, discovered attacks, pins, skewers, pawn breaks (e5!, d5, f4-f6, g4-g5, h4-h5, ...e4, ...f5, ...d5, ...b5), passed pawns, Bg5/Bh6, ALL knight jumps, open files. Answer f6 with ...Bxf6/...Nd7. As White v Chigorin NO d5 unless Rc1 already pins Nc6 to Qc7.
- v SF: trade bishops/rooks only if the pawn ending is counted, castle EARLY, no pawn pushes near my K or on a long diagonal, no grabs, luft early.
- DOWN v others: DeepSeek/GLM/Fable/Haiku hang pieces when worse or even; Sol too. A piece down v Sol: he trades queens, rolls the d-pawn and converts. A ROOK DOWN v a non-SF: K shuffles lose to K+R mate.

## Openings (details in notes)
- W v SF 1.e4 c5 2.Nf3 Nc6: ROSSOLIMO v 3...Nf6 WORKED: 3.Bb5 Nf6 4.e5 Nd5 5.Nc3 Nc7 6.Bxc6 dxc6 7.O-O Bg4 8.h3 Bh5 (16 plies). Plan d3, Re1+, Be3, Qe2, d4 break, Rad1, Ne4. Watch ...Bh5 pin. v 3...g6 (L): 4.O-O Bg7 5.Re1 e5 6.Bxc6 bxc6, NOT Nbd2-c4/Nh2 (...d5! forks). Unverified: c3 and d4, Nbd2-f1; Be3 only after ...d5 is stopped.
- W OPEN SICILIAN v GLM/Muse (Scheveningen, T75R3 W): Nc3, Be2, O-O, Be3, f4, Kh1, Qe1, a3, Bf3, Rd1; v ...b5-b4 axb4 and b5 kept the pawn; Nxd6 forked after ...Qc4. Every unit guarded, g4 only with hxg4 ready. Muse sits in a shell and flags.
- B RUY 4.d3 v DeepSeek (Armageddon draw): 1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 d6 5.O-O Be7 6.c3 O-O 7.Re1 Bd7 8.Nbd2 Re8 (16 plies). Then ...h6, ...a6, ...b5, ...Na5, ...c5, ...Qc7: level; keep ...Bd7/...Rac8. v MUSE (T75R2 draw): level to m30; then find a ...f5/...Bg5 plan by m25, do not wait.
- W v SF Sicilian ...Nc6 ...g6 (Dragon): 5.c4 Maroczy, NOT 5.Nc3 (...Ng4 won a piece). Yugoslav anyway: Be3, f3, Qd2 FIRST; Bc4/Bb3 only after f3.
- W Maroczy v SF (notes white-maroczy-b6-sf, white-open-sicilian-sf): Nc3, Nb3 v ...Qa5, Be2, Be3, O-O (never skip), Qd2, Rac1, Rfd1. v ...Ng4 Bxg4 Bxg4 f3 Be6: castled = 14.Nd5, NOT 14.Qe2?! Bxc3!. v ...Ne5! Rac1; c4 needs a rook/queen guard, never b3 while Bg7 sees a1. v ...f5 exf5 Rxf5: 18.Bd4 is MARKED ?; try 18.Qe3/18.Nd4. NOT Kh1?! b5!. h3 BEFORE the queen trade.
- W Kan/Taimanov v GLM: Nc3, Be2, O-O, Be3, f4, Kh1, Qd2, then a3/Bf3/Rad1. v ...Nxd4 Bxd4 e5: fxe5 dxe5 Bf2 (NOT Be3?! exf4). v ...b5 axb5 axb5 Nxb5! v ...Bb4: Nxc6 bxc6 Qd3 d5.
- W Berlin 4.O-O v Sol: 4...Nxe4 5.Re1 Nd6 6.Nxe5 Be7 7.Bf1, trade on e5, O-O, d4; level until Qxe6?? fxe6.
- W Ruy 3...Nd4 v Haiku: 4.Nxd4 exd4 5.Bc4 Nf6 6.d3, Be7, O-O, Bg5 h6 Bxf6, Nd2. Keep Qf3 guarding.
- W Ruy 8.d3 v Sol: c3, Bb7, Nbd2, Re8, Nf1; v ...d5? exd5 Nxd5 Nxe5! trade rooks FIRST, then Bxd5. After ...e4 dxe4 fxe4: Nd4/Nh4, NOT Nxe4?? Bxe4.
- W closed Ruy 9.h3 v Sol/Astra (note white-closed-ruy): v Chigorin Bc2, d4, Nbd2, cxd4 Nc6, Nb3 a5, Be3 a4, Rc1, v ...Qb7 Bb1 + a3 (NO d5), trade c-file rooks, Qe2. NOT Bd3 with Nd2 home / Bc2? Nb4!. v HAIKU (L): 18.d5? Ne5!; try 18.Be3/Rc1/Nbd2.
- W Breyer v Sol: d4 BEFORE Nbd2, Bc2, Nf1-g3, a4 v ...c5 d5 c4 axb5 axb5 Rxa8 Qxa8, Qd2/Qe3, Nd2. Nf5 only after Bd1. Won 2 pawns once, then Kh2?? Bh6 skewer.
- W Caro Adv v DeepSeek/Muse (note white-caro-adv-deepseek): v 3...Bf5 Nf3, e6, Be2, Be7, O-O, Nd7, Nbd2 BEFORE c3, c3, Nb3. v ...c5 f6 break: exf6 Nxf6, Nb3, Be3, Rc1, Nc5, Ne5, f3, Bd3; then CONVERT. v ...Nh6?!: Bxh6 gxh6 Bxg6+ hxg6 Qd3; NOT Nh4??. v MUSE: Nbd2-b3, Re1, Bd2, a4-a5-a6, h3, f4, g3, g4-g5, Rh1, h5, Qh4. v 3...c5: Nf3 cxd4 Nxd4 Nc6 Nxc6 bxc6, Nc3 e6 Bd3 Ne7 O-O Ng6, f4, Kh1, Qe1-g3, Be3. NOT Bf4?? Nxf4. Caro 3.Nc3: c3/Rhe1.
- B ENGLISH v GLM (7 W): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 6.Nf3 Bd6 7.O-O O-O 8.d3 Nc6 (16 plies). Then ...Be6, h3 ...Qd7, Be3 ...Rad8, Qd2 ...h6. ...Nc4! forks Qe3+Bd2. Nb5 a6! (a4?? axb5).
- B OPEN RUY v Sol (L): 5...Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6, Nbd2 Nc5 c3: level to 15.Rxd1 O-O. 11...d4?! opened the a-file; try 11.Bc2 Bf5 / ...O-O (unverified). NOT ...Rad8? Rxa6.
- B Giuoco v DeepSeek/Haiku (all W): d3, c3, O-O, Nbd2 v ...Nf6 ...d6 ...O-O ...Be6, then Bb3 h6, ...Qd7, ...d5!. v HAIKU 7.d4: exd4 cxd4 Bb6! (not Bb4) Nc3 Bg4 h3 Bxf3 Qxf3 Nxd4 Qe3 Nc2 fork. QGD Lasker (note black-qgd-lasker): ...h6 Bh4 Ne4, Nxe4 dxe4 Nd2 f5!; Rc1 Nxc3 Rxc3 dxc4 Bxc4 b6!.
- B Chigorin v Sol (note black-ruy-chigorin): Na5 + ...Qc7/...Bd7/...Rfe8 LOSES. Knight to c6 FIRST after ...cxd4. W T38R5, T39R4: d5 Nb4 Bb3 a5 a3 Na6! then Bd7, g6, Qc7, Rac8, Rfe8. NOT ...Nc5? (Bxc5 dxc5 Nxe5). v Bh6/h4-h5: ...Bf8-g7, Bxg7 Kxg7, hxg6 fxg6, Qg5 h6!. v Nh2/f4: ...g6, ...Nfd7, no ...h6. f6!: try ...Nxf6/...Re6.
- B Zaitsev v Sol (L x5): book to Bb1, ...c5, d5 ...Nd7, Nf1 ...Ne5?! (try ...f5/...Qb6, unverified). v h4-h5 ...Qc7 FIRST or ...gxh5; NOT ...g5, NOT ...Nc2?? Bxc2. B Breyer v Sol: Bh6 Bxh6 Qxh6 then ...Qd7/...Qe7, never ...Nxa4??.
- B Berlin 4.d3 v Sol (L m25): ...d6, ...Be7, ...O-O, ...Bd7, ...Re8, ...exd4 d5, e5 Ne4, ...Bf5 level to m20; then Bf8/Be7 x5, Rh3, g5 = Qh7#. Plan: ...Qe6/queen trade, ...Ne7-f5, ...c5; do not wait.
- B v SF 6.d4 (0-4): 9.Bd5 Nxd5 10.exd5 Ne5 11.Nbd2 O-O; Ne4 Re8? Nc6! try ...Bg7/...Bd7. 7...d6 8.Nxd4 Bd7: DROP. Berlin 4.O-O (L): Qe2 Qe7 h3 Be6; NOT Qxf6? Bc3; try ...Qd7 or ...O-O-O by move 11.
- B 4N v SF 3.Nc3 (note black-four-knights): 3...Nf6 4.Bb5 Bb4, never 3...Bc5. 5.O-O O-O, Nd5 Nxd5 exd5 e4! ONLY, dxc6 exf3 Qxf3 dxc6 ONLY; 10.Bc4 Bd6!, 11.d4 Qh4! 12.g3 Qxd4 = pawn up. 5.Nd5 Nxd5 ONLY, 6.exd5 e4 7.Qe2 O-O! 8.dxc6 exf3 9.Qxf3 Re8+ 10.Kd1 dxc6: keep queens. Ending level: plan, K/pawns compact, KEEP BISHOPS. NOT ...Rf6?? Bg5!. French 3.Nc3: ...b6/...Bb7 before ...c5. Alapin 3.exd5 Qxd5 4.Nf3 Nf6 5.d4 Nc6 ...Qa5.

## Opponents
- DeepSeek (1 loss in 72): hangs pieces when worse or even (...Bc5??, ...Kf7??, 28.Qb2??); illegal tries; no luft; burns 2-7 min on quiet moves, times out. Converts a free piece at once: never gift one.
- Muse Spark 1.3: 30 s-5 min thinks early (2-3 min on moves 13-37), then 5-30 s under 5 min: the +10 keeps it near 3-4 min, no flag from a shuffle. Zero invalid usually. Takes every loose unit. As White v my Ruy shell it shuffled and accepted repeats. Play solid guarded moves quickly early, then a PLAN.
- Haiku 5.5: v Closed Ruy takes loose pawns. Hangs big pieces when pressed. Never resign vs it.
- GLM Flash (1 loss in 13): English g3 build (13.d4 crack, e4-e5 thrusts that hang pieces); as Black Scheveningen ...b5-b4 (T75R3 hung Ng4 and the exchange, 8 min think on ...Ng4); illegal tries, forfeits. Hangs QUEEN and rooks to plain captures. Take free captures, trade, luft first.
- Fable 5.1 (W): ...Bb4/...bxc6/...d5; no luft. Astra (L): Chigorin ...Na5/...c5/...Qc7/...a4/...Rac8; punishes an unguarded rook.
- SF 19 (depth 4-6): instant; punishes hanging pieces, PAWN FORKS (...d5/...d4 on Nc4+Be3), skewers, PINS on my queen; quiet killers (Bh6, Bg5, Qc3, g4 trapping a rook); in equal endings walks the K in and rolls h4-h5/f4/g4-g5, DEFLECTS a guard, runs the passer. Repeats when nothing is left to push. BLUNDERS in quiet maneuvering and lost K+pawn endings.
- Sol: W Ruy Open, Chigorin, Breyer/Zaitsev (a4, Bc2-b1, d5, Nf1-g3-f5 + f4; Bh6 then Qxh6; h4-h5 + Qg5), 4.d3 (Nf1-g3, Bf4, Re3-Rh3, g4-g5, Qxh7#). 3-90 s. Takes every free piece with tempo. Misplays queenless/time-pressed endings, forgets its back rank.

## Notes (notes/*.md, 8 files = full; merge before adding) and tools
white-open-sicilian-sf, white-maroczy-b6-sf, white-closed-ruy, white-ruy-d3-caro, white-caro-adv-deepseek, black-ruy-chigorin, black-four-knights, black-qgd-lasker. Other openings live in this file only.
tools/material-sweep.py: material diff, my loose pawns, pieces en prise, AVOID for moves that newly hang a piece. tools/pin-fork-trap.py: 2-ply, flags moves after which one reply mates or attacks a piece of mine that no move can save. tools/legal-list.py: legal UCI moves, king moves, mate-in-1 AVOID. Read all BEFORE each move.
