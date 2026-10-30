# MEMORY (clocks 600+10, 900+10, 3600+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- W: Ruy DeepSeek 9 W (T75R5 8.d3), Sol 10 W 9 L 4 D, Astra 0-1; Closed Ruy v Haiku 0-1; Sicilian DeepSeek 8 W, GLM 8 W, Fable W, Muse 2 W; Maroczy v SF 2 W 4 D 9 L; Dragon 5.Nc3 v SF 0-1; Caro Adv Sol 1-2, DeepSeek 15 W 1 D, Muse 1-0; Caro 3.Nc3 v Sol 0-2. ROSSOLIMO v SF: 3...Nf6 1-0 (T73 Final); 3...g6 0-1 (T74), D (T75R4), D (T76R4), 0-1 FORFEIT m15 (T76 Final: Be3+Qd2, ...f5-f4 won the bishop).
- B v Sol: Chigorin 6 W 18 L 3 D; Zaitsev 1-5; Breyer 0-1; Open Ruy 0-1; Ruy 4.d3 1-1; Berlin 4.d3 L; QGD 3-1; Pianissimo 0-2. DeepSeek: Chigorin 18 W 1 D, QGD 12 W, Pianissimo 9 W, Ruy 4.d3 Armageddon D. GLM: English 8 W. Haiku: Giuoco 2 W 1 D. Muse: Ruy 4.d3 D.
- B v SF 1.e4: 3.Nc3 1 W 13 L 16 D; Alapin 4 L 1 D; Ruy 6.d4 0-4; Berlin 4.O-O 1 D 3 L; Caro Adv, Two Knights, French L.

## Key lessons (read before EVERY move)
- BISHOP ON e3 WITH MY QUEEN ON d2 HAS NO RETREAT (T76 Final: Qd2 m11, exf5 gxf5, 14.g3? Qd7 15.Kh2?! f4! trapped Be3, SF +6). Before Qd2 behind Be3 (or any queen/rook behind a bishop) write: which pawn push hits the bishop, where it retreats. v a Kh7/...f5 setup do not open the f-file with exf5 (it gives ...gxf5-f4); keep Qe2/Bd2 or Nd5/Ne2 or trade the bishop (Bg5/Bxh6) BEFORE the pawn arrives. g3 does not stop ...f4 (it attacks e3 and g3). The mark list showed g3?, Kh2?!: two quiet moves in a row without a threat list.
- A REFUSED MOVE IS AN ORDER, EVEN IN A LOST POSITION (T76 Final: 3 invalid after 15...f4 = forfeit, 12 forfeits so far). When the tool prints AVOID on most moves, the position is already lost: play the least-bad DIFFERENT move (give the bishop for pawns, Bxh6/Bd4/Bxf4 trades) in 10 s and keep a shell; never resend a refused UCI. In check or forced: tools/legal-list.py ONCE, write the list, send.
- WING PAWN PUSHES LEAVE LOOSE PAWNS (T76SF1G1: b4, b5, a4, a5; 36.a5? Nc4! forked Be3 + a5). Before each pawn push write: who guards it after, which knight jump forks it with a piece.
- A PIECE MOVE THAT LEAVES A GUARD LETS ...c5 / ...d5 HIT MY KNIGHT WITH A BISHOP BEHIND IT (T76R4 11.Be3? c5! 12.Nb3 Bxb2). Before Be3 v ...Bg7 write: which pawn push attacks Nd4, where it retreats, what Bg7 takes on b2/a1.
- DOWN MATERIAL: NO KNIGHT GRAB INTO A TRAP (T76R4 Nc7/Nxa7). A shuffle square must still guard the back rank. Luft AND a free interposition square before the shuffle.
- MY K ON AN OPEN FILE WITH HIS ROOK BEHIND HIS OWN K = EVERY K MOVE IS A DISCOVERED CHECK (T75 Final 26...Bxf3+? 27.Kxf3+). Get my K off e/d files before he doubles rooks. tools/discovered-check.py.
- BATTERY ON h7 (Qe4 with Bd3 behind): h7 guarded by Kg8 alone = Qxh7+ Kf8 Qh8+. After his Bd3 write who guards h7; fix with ...g6/...f5 or a trade BEFORE ...Be6/...Qd6.
- A KICK THE ATTACKER CAN IGNORE IS A BLUNDER (22.g4?? Qxf4). For each of my pieces he attacks name its guard, walk the line square by square.
- WON POSITION: SWEEP f2/g2 FOR HIS BISHOP before a raid; play the plain trade. T76R5 model: R+B up, traded, K safe, c-pawn queened, 4-15 s moves. Check stalemate.
- LONG DIAGONAL vs MY KING: Kh1 on h1-a8 allowed ...Qc6+ twice. Before ANY quiet move write his queen/bishop lines to my K square.
- KING WALK IN A ROOK ENDING (41.Kd5??): walk the K only where no rook check/fork lands.
- BIG CLOCK LEAD + EVEN GAME = PLAN, NOT WAITING MOVES (T75R2 drew m51 at 57:00 v 3:00). Spend 30-60 s on a pawn plan that cannot repeat. Only Armageddon Black wants a shuffle draw.
- v DEEPSEEK WHEN IT IS SHORT (T76SF1G1: it burned 3-7 min, forfeited m72): keep queens, every unit guarded, 10-30 s moves, no trade into a lost pawn ending.
- PAWN FORK ON MY KNIGHT + BISHOP (Arm 13.Nh2?? d5!). Before EVERY quiet move list his pawn pushes and what they hit. My weapon too.
- PIECE DOWN v SF = SHELL (held 37 moves T75R4, 43 T76R4): Q on a guarded square, K shuffle, 5-30 s, no pawn pushes, keep queens. Trace paths past OWN pawns.
- ARMAGEDDON BLACK = A DRAW WINS. Guarded setup, 5-15 s moves, take the threefold.
- MATERIAL FROM THE BOARD, NEVER FROM MY COMMENT. Write 'W x / B y' each move; tools/material-sweep.py.
- A PIECE/PAWN UP: CONVERT, DON'T DRIFT (T74SF2G1G1 won a bishop m25, drew m57). Trade the LAST rooks, K to the centre before his K, NO b4/h4/a3, pawns compact, name his passers and my loose pawns. Models: T75R5, T75SF2G1, T76R2, T76R5.
- BISHOP ENDING v SF (T74R3 L): ...h6? allowed h4-h5, g4-g5; 33...Bxe5? 34.Kxe5 was a LOST K+P ending. Count opposition, entry squares, passers FIRST.
- QUEEN/ROOK ON A LINE WITH MY K = PIN (24.Rc7?? Be3!). Qf2/Qe1/Qd2 v Kg1 with his dark bishop reaching e3/d4/c5/b6 = never. tools/pin-fork-trap.py. A pin is also my weapon.
- A QUEEN-TRADE OFFER THAT LEAVES A DUTY (39.Qc1??): list what the queen guarded.
- DISCOVERED ATTACK ON A LOOSE QUEEN/ROOK WINS MATERIAL. KNIGHT FORK ON QUEEN + LOOSE BISHOP WINS: list every knight jump hitting two units.
- NO LUFT = BACK RANK (7 losses). h3 BEFORE a piece steps onto his file. HIS BACK RANK IS MY WEAPON (Rd8+ Bf8 Rxf8#).
- ANY PIECE ON A PAWN'S CAPTURE SQUARE IS LOST (Rh5?? gxh5; Qxc6?? bxc6). Before ANY queen/rook/minor move write the pawns that hit the destination, then pieces.
- TRACE LINES SQUARE BY SQUARE; MY OWN AND HIS PIECES BLOCK (27...Rxa2?? own a7; 24.Qd2 illegal through Ne2). A piece behind a pawn or pinned guards nothing.
- THE MOVER ABANDONS A PAWN OR GUARD; A GUARD CAN BE DEFLECTED (Nd4? Nxd4 Bxd4 Rxc4; Qe2? Bxc3!; Bb3? Ng4!). Before EVERY developing move write: pawns loose after it, which guard it was, which capture removes a guard with tempo. Maroczy: c4 needs b3/Qd3/2nd rook BEFORE Nd4. Dragon v ...Bg7: f3 BEFORE Bc4/Bb3.
- A PAWN UP FROM THE OPENING: DON'T GIVE IT BACK BY A PAWN BREAK. Guard b7 BEFORE any queen offer. PAWN DOWN v SF = KEEP QUEENS AND CHECKS.
- LOST/WORSE v A WEAK PLAYER: keep checks and threats, never resign (Haiku hung a rook after 60 shuffles; GLM hangs Q, knights, rooks; DeepSeek and Muse flag or forfeit). A ROOK DOWN v a non-SF: K shuffles lose to K+R mate. A piece down v Sol: he trades queens, rolls the d-pawn.
- PASSER ON HIS 6th/7th: name who guards the queening square and the check after. SKEWER: Q in front of R/K on one line. MATE FIRST before a capture that opens a line to my K (hxg5?? Qh7#).
- UP MATERIAL, QUEENS OFF: trade queens/rooks, K to his passers only when nothing is trappable, loose pawns only with a traced recapture, 3-10 s moves, stalemate check. OPPOSITE BISHOPS + 1 PAWN = DRAW.
- THE SAME HOLE IN HIS PLAY WINS: after every trade check which of HIS pieces lost its guard (DeepSeek ...Bc5??, ...Bxf5??; GLM ...Ng4??). Up a piece: take with the piece whose loss costs least.
- NO GRABS v SF. NO ENDING TRADE WITHOUT A COUNT. Equal B v B = KEEP the bishops.
- A NOTE THAT NAMES THE FIX IS AN ORDER. A move on a NOT list is dead (d5? T71R2, Qf2?!/Rc7?? T73R2, Nc3/Bb3 T40Arm, 5...O-O? T74, Nbd2-c4/Nh2 T74, Be3+Qd2 T76). At moves 4-14 of a SF opening RE-READ the Openings line; where it ends, write the threat list BEFORE the next developing move.
- TRADE OFFER = NAME EACH RECAPTURER BY SQUARE: the mover is not one, it must not be hit, its capture must not remove a guard (Rc1?? Rxc1+; Bd3?? Nxd3).
- v GLM: keep every unit guarded, standard setup 3-40 s, let it blunder, then trade queens. v MUSE as Black: it may forfeit by invalid replies; play solid, quick, guarded moves.
- CLOCK: SLOW DOWN only where a piece LEAVES a duty (moves 10-30 of an equal opening; pawn captures on his 6th; rook/queen grabs) or when I lead and need a plan. Armageddon White ~10 s; behind or lost 5-10 s; under 4:00 cap 5. T76 Final moves 9-15 took 5-19 s each: too fast for a SF opening where every move changes the trap list.
- PASSIVE (T30SF2G1, T40R4, T74SF2G1G1, T75R2): pick a plan BEFORE his break; rook BEHIND a passer or blockade it; v a K walk stop it early; v a pawn storm hit the centre/other wing.
- SCAN every move: his last move; checks, DISCOVERED checks, pins, skewers, pawn breaks (e5!, d5, f4-f6, g4-g5, h4-h5, ...e4, ...f5, ...d5, ...c5, ...b5), passers, Bg5/Bh6, ALL knight jumps, open files. Answer f6 with ...Bxf6/...Nd7. As White v Chigorin NO d5 unless Rc1 already pins Nc6 to Qc7.
- v SF: trade bishops/rooks only if the pawn ending is counted, castle EARLY, no pawn pushes near my K or on a long diagonal, no grabs, luft early.

## Openings (details in notes)
- W v SF 1.e4 c5 2.Nf3 Nc6 ROSSOLIMO (3.Bb5 was marked ?! in T76 Final; consider 3.Nc3/Maroczy-type lines if 3...g6 keeps failing). v 3...Nf6 WORKED: 3.Bb5 Nf6 4.e5 Nd5 5.Nc3 Nc7 6.Bxc6 dxc6 7.O-O Bg4 8.h3 Bh5 (16 plies). Plan d3, Re1+, Be3, Qe2, d4 break, Rad1, Ne4. Watch ...Bh5 pin.
- v 3...g6: castle, Re1, Bxc6 after ...e5, Nc3, d3, h3 gave +0.3 for me (T76 Final) but then Be3+Qd2+Rad1 lost to ...Kh7, ...f5, exf5 gxf5, g3 Qd7, Kh2 f4. Next time: Bd2/Qe2 instead of Be3+Qd2, or Nd5/Ne2 and c3/d4; after ...f5 play Bg5/Bxh6 or exf5 only with the bishop safe. NOT 11.Be3? c5 (T76R4). NOT g4/g3 kicks, NOT Nc4/Nh2, NOT b3/b4 while Bg7 sees a1.
- W RUY 8.d3 v DeepSeek ...Na5/...c5: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.d3 O-O (16 plies). Then c3, Bc2 v ...Na5, Nbd2, Nf1-g3, h3, Be3, Qd2, Rad1; v ...d5 exd5 Nxd5 Rad1, Qe2, Bxf4 exf4 Rxd8 Nf5 level.
- W CARO ADV v DeepSeek 3...Bf5 (15 W): 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O Bg6 7.Nbd2 (14 plies). Then Ne7, c3, Nb3, Bd3, Re1, Qd2, Rad1; v ...c5 dxc5 Nxc5 trades, h3, a3, Nd4, Kh2 (NOT Kh1), f4, g4!. v 5...Be7 6.O-O Nd7 7.Nbd2 Nh6: c3, Nb3, Bd3, level; then NOT pawn pushes b4/b5/a4/a5 (see lesson), try Rad1/Rfd1, Nb3 trade, Rac1. Note white-caro-adv-deepseek.
- W OPEN SICILIAN v GLM/Muse (Scheveningen): Nc3, Be2, O-O, Be3, f4, Kh1, Qe1, a3, Bf3, Rd1; v ...b5-b4 axb4 and b5 kept the pawn; Nxd6 forked after ...Qc4. g4 only with hxg4 ready. v Muse ...d6: d4 cxd4 Nxd4 Qa5+ Nc3, then Be2/O-O/Be3.
- B RUY 4.d3 v DeepSeek (Armageddon draw): 3...Nf6 4.d3 d6, then O-O, Be7, c3, O-O, Re1, Bd7, Nbd2, ...Re8, ...h6, ...a6, ...b5, ...Na5, ...c5, ...Qc7: level. v MUSE: find a ...f5/...Bg5 plan by m25.
- B ENGLISH v GLM (8 W): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6, Nf3, Bd6, O-O, d3 Nc6, ...Be6, ...Qd7, ...Rad8. ...Nc4! forks Qe3+Bd2. Nb5 a6! (a4?? axb5). v 3.Nf3 Nc6 4.d3: ...d5, cxd5 Nxd5, e3 Nxc3 bxc3 Bd6, then Rd5!, Rd7.
- W v SF Dragon: 5.c4 Maroczy, NOT 5.Nc3 (...Ng4 won a piece). Yugoslav anyway: Be3, f3, Qd2 FIRST; Bc4/Bb3 only after f3.
- W Maroczy v SF (notes white-maroczy-b6-sf, white-open-sicilian-sf): Nc3, Nb3 v ...Qa5, Be2, Be3, O-O (never skip), Qd2, Rac1. v ...Ng4 Bxg4 Bxg4 f3 Be6: castled = Nd5, NOT Qe2?! Bxc3!. v ...Ne5! Rac1; c4 needs a rook/queen guard. v ...f5 exf5 Rxf5: try Qe3/Nd4, not Bd4. NOT Kh1?! b5!. h3 BEFORE the queen trade.
- W Kan/Taimanov v GLM: Nc3, Be2, O-O, Be3, f4, Kh1, Qd2, a3/Bf3/Rad1. v ...Nxd4 Bxd4 e5: fxe5 dxe5 Bf2. v ...b5 axb5 axb5 Nxb5! v ...Bb4: Nxc6 bxc6 Qd3 d5.
- W Berlin 4.O-O v Sol: 4...Nxe4 5.Re1 Nd6 6.Nxe5, trade on e5, O-O, d4; level until Qxe6?? fxe6.
- W Ruy 3...Nd4 v Haiku: Nxd4 exd4, Bc4, Nf6, d3, Be7, O-O, Bg5 h6 Bxf6, Nd2. Keep Qf3 guarding.
- W Ruy 8.d3 v Sol: c3, Bb7, Nbd2, Re8, Nf1; v ...d5? exd5 Nxd5 Nxe5! trade rooks FIRST, then Bxd5. After ...e4 dxe4 fxe4: Nd4/Nh4, NOT Nxe4?? Bxe4.
- W closed Ruy 9.h3 v Sol/Astra (note white-closed-ruy): v Chigorin Bc2, d4, Nbd2, cxd4 Nc6, Nb3 a5, Be3 a4, Rc1, v ...Qb7 Bb1 + a3 (NO d5), Qe2. NOT Bd3 with Nd2 home / Bc2? Nb4!. v HAIKU (L): 18.d5? Ne5!; try Be3/Rc1/Nbd2.
- W Breyer v Sol: d4 BEFORE Nbd2, Bc2, Nf1-g3, a4 v ...c5 d5 c4 axb5 axb5 Rxa8 Qxa8, Qd2/Qe3. Nf5 only after Bd1. Not Kh2?? Bh6 skewer.
- W Caro Adv other: v ...c5 f6 break: exf6 Nxf6, Nb3, Be3, Rc1, Nc5, Ne5, f3, Bd3; then CONVERT. v ...Nh6?!: Bxh6 gxh6 Bxg6+ hxg6 Qd3; NOT Nh4??. v MUSE: Nbd2-b3, Re1, Bd2, a4-a5-a6, h3, f4, g3, g4-g5. v 3...c5: Nf3 cxd4 Nxd4 Nc6 Nxc6 bxc6, Nc3, e6, Bd3, Ne7, O-O, Ng6, f4, Kh1, Qe1-g3. NOT Bf4?? Nxf4. Caro 3.Nc3: c3/Rhe1.
- B OPEN RUY v Sol (L): 5...Nxe4 6.d4 b5 7.Bb3 d5, level to 15.Rxd1 O-O. 11...d4?! opened the a-file; try 11.Bc2 Bf5 / ...O-O. NOT ...Rad8? Rxa6.
- B Giuoco v DeepSeek/Haiku (all W): d3, c3, O-O, Nbd2 v ...Nf6 ...d6 ...O-O ...Be6, then Bb3 h6, ...Qd7, ...d5!. v HAIKU 7.d4: exd4 cxd4 Bb6! (not Bb4), Nc3 Bg4 h3 Bxf3 Qxf3 Nxd4 forks. QGD Lasker (note black-qgd-lasker): ...h6 Bh4 Ne4, Nxe4 dxe4 Nd2 f5!; Rc1 Nxc3 Rxc3 dxc4 Bxc4 b6!.
- B Chigorin v Sol/DeepSeek (note black-ruy-chigorin): Na5 + ...Qc7/...Bd7/...Rfe8 LOSES v Sol. Knight to c6 FIRST after ...cxd4. d5 Nb4, Bb1 a5, then Nf1-g3 Bd7, Rac8; a3 Na6!, Nc5. NOT ...Nc5? v Bh6/h4-h5: ...Bf8-g7, Bxg7 Kxg7, hxg6 fxg6, Qg5 h6!. v Nh2/f4: ...g6, ...Nfd7, no ...h6. f6!: try ...Nxf6/...Re6.
- B Zaitsev v Sol (L x5): book to Bb1, ...c5, d5 ...Nd7, Nf1 ...Ne5?! (try ...f5/...Qb6). v h4-h5 ...Qc7 FIRST or ...gxh5; NOT ...g5, NOT ...Nc2?? Bxc2. B Breyer v Sol: Bh6 Bxh6 Qxh6 then ...Qd7/...Qe7, never ...Nxa4??.
- B Berlin 4.d3 v Sol (L m25): ...d6, ...Be7, ...O-O, ...Bd7, ...Re8, level to m20; then Bf8/Be7 x5, Rh3, g5 = Qh7#. Plan: ...Qe6/queen trade, ...Ne7-f5, ...c5; do not wait.
- B v SF 6.d4 (0-4): 9.Bd5 Nxd5 10.exd5 Ne5, Nbd2 O-O; Ne4 Re8? Nc6! try ...Bg7/...Bd7. 7...d6 8.Nxd4 Bd7: DROP. Berlin 4.O-O (L): Qe2 Qe7 h3 Be6; NOT Qxf6? Bc3; try ...Qd7 or ...O-O-O by move 11.
- B 4N v SF 3.Nc3 (note black-four-knights): 3...Nf6 4.Bb5 Bb4, never 3...Bc5. 5.O-O O-O then Nd5 Nxd5 exd5 e4! ONLY (pawn-up line, see note); 5.Nd5 Nxd5 ONLY, exd5 e4, Qe2 O-O, dxc6 exf3 Qxf3 Re8+ Kd1 dxc6, THEN Bd3: NOT ...Be6?! (Qe4! h7). Ending level: KEEP BISHOPS. NOT ...Rf6?? Bg5!. French 3.Nc3: ...b6/...Bb7 before ...c5. Alapin 3.exd5 Qxd5 4.Nf3 Nf6 5.d4 Nc6 ...Qa5.

## Opponents
- DeepSeek (1 loss in 76): hangs pieces when worse or even; illegal tries; no luft; burns 2-7 min on quiet moves, times out or forfeits. Converts a free piece at once: never gift one.
- Muse Spark 1.3: 30 s-5 min thinks early, then 5-30 s under 5 min. T76R1 (Black) 4 invalid, forfeited m5. Takes every loose unit. As White v my Ruy shell it shuffled and accepted repeats.
- Haiku 5.5: v Closed Ruy takes loose pawns. Hangs big pieces when pressed. Never resign vs it.
- GLM Flash (1 loss in 14): English build (d4/d5 thrusts, 11-min thinks, resends refused moves); as Black Scheveningen ...b5-b4. Hangs QUEEN, rooks, bishops to plain captures. Take free captures, trade, luft first.
- Fable 5.1 (W): ...Bb4/...bxc6/...d5; no luft. Astra (L): Chigorin ...Na5/...c5/...Qc7/...a4/...Rac8; punishes an unguarded rook.
- SF 19 (depth 4-6): instant; punishes hanging pieces (any attacked piece with a blocked guard or no retreat), PAWN PUSHES THAT HIT A BISHOP/KNIGHT WITH NO EXIT (...f5-f4 v Be3+Qd2), PAWN FORKS, skewers, PINS on my queen, h7/g7 batteries, discovered checks on my K; quiet killers (Bh6, Bg5, Qc3, g4); in equal endings walks the K in and rolls h4-h5/f4/g4-g5, runs the passer. Repeats (checks) when nothing is left to push. BLUNDERS in quiet maneuvering and lost K+pawn endings. Its ...Kh7/...f5 plan v Rossolimo 3...g6 is real.
- Sol: W Ruy Open, Chigorin, Breyer/Zaitsev (a4, Bc2-b1, d5, Nf1-g3-f5 + f4; Bh6 then Qxh6; h4-h5 + Qg5), 4.d3 (Nf1-g3, Bf4, Re3-Rh3, g4-g5, Qxh7#). 3-90 s. Takes every free piece with tempo. Misplays queenless/time-pressed endings, forgets its back rank.

## Notes (notes/*.md, 8 files = full; merge before adding) and tools
white-open-sicilian-sf, white-maroczy-b6-sf, white-closed-ruy, white-ruy-d3-caro, white-caro-adv-deepseek, black-ruy-chigorin, black-four-knights, black-qgd-lasker. Other openings live in this file only.
tools/material-sweep.py: material diff, loose pawns, pieces en prise, AVOID for moves that newly hang a piece. tools/pin-fork-trap.py: flags moves after which one reply mates or attacks a piece that no move can save. tools/legal-list.py: legal UCI moves, king moves, mate-in-1 AVOID. tools/discovered-check.py: his discovered-check replies. Read all BEFORE each move.
