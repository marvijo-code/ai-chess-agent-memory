# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B; T77R6 empty-reply, T77R7 drew up B, T77R7.3 won on time
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
- tools: legal-list first, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender

## Rule 0 - board, legality, clock
- THE CLOCK LOSES GAMES, AND SO DO INVALID TRIES: T77R5 clock fine (46:55 vs 43:30) yet 12 invalid tries burned 2:56 on 34.Bd2, 1:47 on 40.Ng3, 2:41 on 51.e8=Q+. Routine 5-15 s; capture/check/pawn break 15-25 s; 30+ s ONLY for a named forcing line. Long-think offenders: T75R2, T76R1, T76SF1G1 (7:33 and 4:24 thinks, ended 1:06 vs 37:00), T77R4 (3:38 on 16...f4). From move 15 level/worse: 10 s a move, cap 20. Under 5 min: 5 s; under 1 min: 2 s and copy a legal UCI. T77R7.3: Armageddon White won on time (11:37 vs 0:17): active plan, 5-10 s from m15, no queen shuttle; gated tries at 16.Rad1/18.c5/23.Qe2 were survivable because I kept the next legal UCI ready.
- INVALID REPLIES: 3 tries on ONE move = forfeit; an EMPTY reply is a try (T77R6: 0 illegal yet forfeit at 19.Bf4 after 3 empty attempts). Every send: legal list, destination empty/enemy, path clear, own blockers. At a quiet turn pre-list 3 sound UCIs; if one is refused/unavailable, send the next. After ONE rejection change piece AND idea; a refusal naming my move is final. Promotions and check replies get the same check as any other move.
- In check/forced: read the FEN once, list every legal reply, send exact UCI in 5-10 s; never send a remembered king square.
- Tool AVOID is not material: count Q for B/R before obeying; obey pawn-capture flags. His last move first; legality actual square, occupant, path, own blockers, pinned pawn, O-O flights.
- Material from board every move. Name my loose units and his queen/rook/bishop reaching them before any quiet move.

## Rule 1 - destination sweep
- RECAPTURE WITH THE PIECE THAT DOES NOT OPEN A LINE: T77R5 31...Qxc3 32.Nxc3?? took the e2-knight off the b5-f1 diagonal and 32...Bxf1 won the exchange; 32.bxc3 keeps Ne2 blocking it. Before any recapture, name the ray the mover leaves and his bishop/rook at its end.
- A GUARD MUST REACH IN ONE MOVE. Be7 covering c5 via d6 covers nothing. An attacked piece: list retreats before quiet; never fill its flight with another piece. A defended piece dies when his capture has a second recapturer.
- A PINNED GUARD DOES NOT GUARD: check a pawn/piece is not pinned to my queen/king before relying on it. T77R3 17.Bd5?? Nxd5: Bg6 pinned e4 to Qc2.
- KING AND PIECE ON ONE RANK FACING HIS ROOK: T77R5 Ra3 + Kf3 pinned Bc3; its only guard Ne2 left (40.Ng3??) and 40...Bxc3 won it. Move the KING off the rank or add a SECOND guard; never move the pinned piece's sole guard.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; all knight jumps; every bishop/rook line. A pawn that leaves abandons its post: no ...f6 with Ke8/f8 and e6 loose; ...g5 vs h6 loses h6 to Nxh6.
- PAWN FORK ON A KNIGHT LANDING: with his d4/e4 pawns alive my knight on e5 sits on d4's capture square (T76R4 21...Ne5?? 22.dxe5). Before a knight lands in his centre list d4xe5/e4xd5/c4xd5.
- Never a piece where his pawn, knight or bishop forks it with another unit. A checking piece near his king: count king capture; a check is safe only if guarded or king cannot take.
- AN ATTACK IS NOT A DEFENCE. My own piece on a line is my only screen; moving it exposes king/queen.

## Rule 1b - mate first
- Ask what mates if I pass. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3. Keep rank-1 blocker or luft. K on c8 with b7 empty = ...Qa6+/...Qb7#.
- Before trading a light bishop or a quiet queen move, name h7/g7 guards. My finishers: boxed Kf1 + Nf4 + rook on 4th = Rc1#; K h7/h8 + queen reaching g7 + knight covering g7 = Qg7#; up R+B+N roll a pawn, keep flights covered, avoid stalemate.
- Do not trade a strong central knight for a passive bishop without a concrete pawn/bishop gain: T76R7 11.Nxf6+?? freed ...c5/...b4.
- Q+R v 3 pawns is lost: do not count a promotion into a rook covering the queening square (T77R5 51.e8=Q+ Rxe8).
- Queens off and level, N vs B is not a loss if my clock is safe; keep bishop/king active, but no long think.

## Rule 2 - queen
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. Hit -> she moves that move off every ray. Queen with a duty stays on duty.
- HIS ROOK ON THE 4th-6th GAINS A TEMPO ON MY QUEEN on its rank or file: T76R4 80.Qa6?? 82.Qb5??. Queen in time trouble: one defended square, one duty, accept a trade.
- QUEEN RECAPTURE: walk every attacker of the landing; after she moves name what she no longer guards. T76R2 30.Qxc1 left f2 to ...Qxf2.
- VS PERPETUAL: with a big material lead my queen must block a checking line or trade (T76R3 Q+2R vs Q+B became forever checks).
- QUEEN ON A PAWN-GUARD DUTY: T76SF1G1 50/52...Qb5?? under 1 min. With <2 min move her to a central defended square or accept the trade.
- HIS QUEEN ON THE E-FILE, MY BISHOP PINS: ...Re8 won a tempo twice (T77R2); blocking a check with a developing move that attacks her was best (14...Bf7! after Qe6+). Use these tempos.
- DO NOT SHUTTLE THE QUEEN WITH NO NEW TARGET: T77R6 12...Qb6?! 13...Qc7?! 15...Qb6 again (SF ?! both) wasted tempi in a level Caro. T77R7 up B for P, Qc6-Qd6-Qc6 drew; T77R7.3 active play won on time. A queen retreat must take a new duty; otherwise play a rook/pawn plan.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded. An undefended piece is not free if his answer comes with tempo; never R for B/P.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET: T76R4 30...fxe4! took Ne4 for a pawn. My queen must not sit on that square.
- A rook that blocks stays; a rook his knight hits moves. Rook on an open file facing his rook needs a guard. Rook shuffle needs a target and a check-square audit.
- Knight d6 guarded by e5 is a pivot; knight d5 hitting queen worth a pawn. Bishop f5 along e4-d3-c2: when his Nd3 leaves, ...Bxc2! wins R for B.
- After long castling behind doubled c-pawns answer ...b4-b5 with ...b5/...a5/...Kb8/...Rc8.
- WING PAWN GRAB WITH A KNIGHT: T76SF1G1 37...Nxa5?? with queens on; keep knights central. Bc3 after ...c5 is hit by ...b4 (T76R7 15.Bc3??): prefer Be3/Bf2 or a concrete trade.

## Rule 4 - material and conversion
- MATERIAL FROM BOARD EVERY MOVE; no grabs when level/behind. T77R5 the loss came from the queen trade that opened a bishop diagonal, then his rook took b3/a3: before trading queens count the pawns and diagonals it hands him.
- DOWN v SF: 5-10 s, every unit guarded, solid first rank, fortress/threefold goal. Down Q for R: 2N v R+pawns no fortress. Down B for P: king centre, passers. Blockaded passer: free rook or draw.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, consolidate, trade pieces not pawns, name ONE conversion. Up piece v passive: trade minors, clamp, Rc1#. Up queen/rook: forcing check/ladder first, recount each capture, check stalemate.
- UP A PAWN, HE STEERS THE THREEFOLD: T77R2 I was +1 with a big clock lead and repeated until he drew. T77R7 up B for P at 54:06 vs 17:36, my queen shuttled Qc6-Qd6-Qc6 (SF ?? Qc7/Be7/Qc6) and he drew. Up material a repetition is MY loss: before repeating, make ONE permanent change - pawn break, rook lift, queen activation, or trade queens/rooks.
- DOWN MATERIAL, A REPETITION IS MY SAVE: T77R3 fortress Qd2/Qe2 held; T77R4 Ne6+Qd7+Re8/Rf8 drew vs SF +7.7. Do not refuse a draw when down; keep every unit guarded.
- UP +5 WITH QUEEN ON: before any quiet move list his queen checks to my king; keep a piece to block and keep luft. Trade queens at the first safe offer. T76R3 +10 became a perpetual.
- EXTRA PIECE IN A BLOCKED POSITION: break the blockade, not a knight tour. DOWN A PAWN CLOSED SHELL: draw real, one break, 5-15 s. ARMAGEDDON WHITE: draw is loss; d4 by move 12-14 or sharper. T77R7.3 Classical Caro: c4/c5/Be5/Ne4 active, no queen shuffle, won on time. When he is under 1 min, every move must force an answer or guard a loose unit.
- A CLEAN WIN = one plan, guarded units, fast safe moves; a clean loss = one routine move thought about for 5 minutes.
- VS MUSE LOW CLOCK: T76R7 banked 44:58 vs 1:07; solid 5-10 s, keep the blockade, no repetition. T77R7.3 banked 11:37 vs 0:17 and won.

## Openings (details in notes)
- Open Sicilian Scheveningen W: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (15). Plan f4, Qe1-g3, a4, Rad1/Kh1; the e5 break, exd6/Bxd6, Qh3/f5 and Nxh6 (once g7 is empty) are the attacking ideas; finishers include Nd5, Bxc5, Qc3+, Ne8+ and Qg7#. 4-20 s.
- Open Sicilian Taimanov W: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16). Plan f4/Qd2/Rad1/Kh1; e5 hits Nf6; vs Qd7/Rd7/Qc6 cluster Bxf6! gxf6 Nxf6+ Kg7 Bxc6 wins queen. Vs ...d6 hedgehog choose d5/e5 or f4 by m15-18.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Be7 6.O-O Nd7 7.Nbd2 Nh6 8.c3 O-O (16). Plan ...Qc7/...Bxd3/...Nf5 with d5 guarded; no ...f6 without an e6 piece guard; ...c5 only with a PIECE guard on d5 (T77R4 10...c5?? 11.Bxf5! exf5 12.Nxd5 = -2P).
- Caro Classical B: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). Plan: trade the d3 bishop, develop Nd7/Ngf6/Be7, castle, then Qc7/Bf8; keep f7 guarded; ...e5 only with Bd6+Nd7 behind; ...c5 only with a d5 piece guard. T77R7 drew up B for P by queen shuttle Qc6-Qd6-Qc6; T77R7.3 won on time with c4/c5/Be5/Ne4. Convert by trading queens/rooks or one pawn break.
- Ruy W Classical 5...Bc5: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15). Plan ...Be6 and d4; after the central exchange put the bishop on b6 and the knight on c3, then use Bg5/Nd5. 5-15 s.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). Plan h3/Bc2 against ...Na5, d4/Nbd2/Nf1-g3; after central exchanges use d5/...Nb4/Bb1/...a5; do NOT 20.b4?!. Keep Kg1 guarding f2 until queens off. 5-15 s.
- English reversed-QGD B: 1.c4 Nf6 2.Nc3 e6 3.e4 d5 with ...exd5/...Be7/...O-O was level (T77R2 draw). Slack: the ...Bg4/...Bh5/...Bg6 retreat and ...f6 against his e5; keep the light bishop active, hold d5 with ...Bf7 when Nxd5 looms. Up a pawn, never steer the threefold.
- Other: Ruy B Chigorin ...Na5/...c5/...Nc6/...Be6/...Qc7/...Rfe8; keep h7 guarded. Taimanov B: e5 clamp answered only ...Nd5/...Bf8, never ...d6/castle/...Nf6 while e5 stands; g7 needs a piece guard. Dragon/Soltis B: never ...Qa5 where Nb3 hits; with g4 on, ...Nxh5 loses to gxh5. Italian: ...Nc6/...Bc5/...Nf6/...d6/...Be6; no queen on d5 while Nf6 lives. Accelerated Dragon W: ...Ng4 hitting Be3 - no h3?! kick; O-O/Be2/f3/Bf2 first. Ruy W 5.Nc3: d3/Be3/O-O/Re1, keep Nd5, no Nxf6+, Bc3 invites ...b4. Italian W v Muse: c4/b3 bishops, d3/c3 pawns, Re1/Rd1, Nbd2 then d4; watch ...Bg4 and ...Bg6 pins (17.Bd5?? Nxd5 lost a piece).

## Opponents
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rays/pawn squares/knight squares, ignored attacked pieces, pawn sacs opening lines to king. Vs Caro Advance plays Na4/Nxc5 once c5 unguarded; Qa6+/Qb7# with Kc8/b7 empty. From +10 permanent queen checks against a boxed Kh1/Kh2. In a blocked d6/e6 fortress at +7.7 he allowed threefold (T77R4). 10-15 s; trade queens when up.
- Muse Spark 1.3: patient 30 s-4 min early; T76R7 he burned to 1:07 and forfeited (I 44:58), but T76R4 he flagged me. Zero gifts, takes tempos (Rc5/Rc6 on my queen), sits in a shell; 2-4 illegal tries. Vs him: 5-10 s from move 15, count every landing, bank clock. T77R3 (Italian, draw): I lost a piece to 17.Bd5??, then Qd2/Qe2 fortress held and his clock fell to 0:52. T77R7 (Caro Classical, draw): I was up B for P with a huge clock lead; he steered a queen-shuffle threefold. Up material, break the loop. T77R7.3 (Caro Classical, 1-0 on time): active c4/c5/Be5/Ne4 plan, no queen shuttle; he flagged 0:17 vs 11:37.
- GLM 5.3 Flash: HIS QUEEN ON MY PAWN/KNIGHT CAPTURE SQUARE (7+ times); 1-12 illegal tries. Take gifts only after the capture list; decline queen trades when pawn down. Down material he fortresses but burns time. T77R2 (English, draw): down a pawn he steered knight shuffles into a threefold and I cooperated - when up, break the loop.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded; punishes a piece on his pawn square and a queen on a rook file.
- Sonnet 5.5: 40-50 min clock, punishes loose queen/rook/pawn grabs; in endings centralizes the king, rook on my 3rd, eats unguarded pawns. T77R5 (Closed Ruy 5.Nc3, 0-1): waiting ...Re8/...Bf8/...Bf5/...b4 squeeze with tempo on my pieces, then the queen trade that opened b5-f1 (32.Nxc3?? Bxf1) and his Ra3 pinning Bc3 to Kf3 (40.Ng3?? Bxc3). T77R6 (Caro Advance, 0-1 forfeit m19): level to 19.Bf4, queen shuttling Qc7-Qb6 cost tempi, then an empty reply after 3 attempts lost. 5-10 s from move 1; before any queen trade count the pawns and diagonals it hands him.
- Fable 5.1, GPT-6.1 Sol, Astra: take every unguarded unit; keep every unit guarded and bank clock. Haiku 5.5: solid Italian Pianissimo, fast.
