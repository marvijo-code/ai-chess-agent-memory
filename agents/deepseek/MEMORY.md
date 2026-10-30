# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
- tools: legal-list first, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard

## Rule 0 - board, legality, clock
- THE CLOCK LOSES MY GAMES, NOT HIS. Routine 5-15 s; capture/check/pawn break 15-25 s; 30+ s ONLY for a named forcing line. Long-think record: T75R2 10:13, T76R1 6:28, T76R2 4:51, T76R3 3:11, T76R4 5:43, T76SF1G1 24...Ng6 7:33, 37...Nxa5?? 4:24, 40...Qxb5 6:17, 43...Qf5 4:41, 45...Qd3 3:16 (ended 1:06 vs 37:00, forfeit). From move 15 level/worse: 10 s a move, hard cap 20. Under 5 min: 5 s; under 1 min: 2 s and copy a legal UCI.
- INVALID REPLIES: 3 tries on ONE move = forfeit. T76SF1G1: illegal tries at 5... (Nc6 onto own c6 pawn) and 7... (Ne7 onto own bishop) were warnings; final move 3 invalid with 1:03 left ended it. Every send: read the legal list, destination empty or enemy, path clear. After ONE rejection change piece AND idea; a refusal naming my move is final and that SQUARE stays banned for the game.
- In check/forced: read the FEN once, list every legal reply, send the exact UCI in 5-10 s; never send a remembered king square.
- Tool AVOID is not material: count Q for B/R before obeying; obey pawn-capture flags. His last move first; rebuild board; legality actual square, occupant, path, own blockers, pinned pawn, O-O flights.
- Material from board every move. Name my loose units and his queen/rook/bishop reaching them before any quiet move.

## Rule 1 - destination sweep
- A GUARD MUST REACH IN ONE MOVE. Be7 covering c5 via d6 covers nothing. An attacked piece: list retreats before quiet; never fill its flight with another piece. A defended piece dies when his capture has a second recapturer; if nothing recaptures, move it.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; all knight jumps; every bishop/rook line. My piece on his pawn's capture square is lost. A pawn that leaves abandons its post: no ...f6 with Ke8/f8 and e6 loose; ...c5 only with a d5 piece guard; ...g5 vs h6 loses h6 to Nxh6.
- PAWN FORK ON A KNIGHT LANDING: with his d4/e4 pawns alive, my knight on e5 stands on d4's capture square with my queen (d6) and knight (f6) behind it - dxe5 hits both. T76R4 21...Ne5?? 22.dxe5 won a knight. Before a knight lands in his centre list d4xe5/e4xd5/c4xd5.
- Never a piece where his pawn, knight or bishop forks it with another unit. Rooks/knights only guarded; name the guard the mover abandons. A checking piece near his king: count king capture; a check is safe only if guarded or king cannot take.
- AN ATTACK IS NOT A DEFENCE. My own piece on a line is my only screen; moving it exposes king/queen. A screen leaving with tempo is a weapon.

## Rule 1b - mate first
- Ask what mates if I pass. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3. Keep rank-1 blocker or luft. K on c8 with b7 empty = ...Qa6+/...Qb7#; cover b7 with a piece.
- Before trading a light bishop or a quiet queen move, name h7/g7 guards. My finishers: boxed Kf1 + Nf4 + rook on 4th = Rc1#; K h7/h8 + queen reaching g7 + knight covering g7 = Qg7#; up R+B+N roll a pawn, keep flights covered, avoid stalemate.
- With queens off and level, N vs B is not a loss if my clock is safe; keep bishop/king active, but no long think.

## Rule 2 - queen
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. Hit -> she moves that move off every ray. Queen with a duty stays on duty. His piece between my queen and his rook can move with tempo.
- HIS ROOK ON THE 4th-6th GAINS A TEMPO ON MY QUEEN ON ITS RANK OR FILE: T76R4 80.Qa6?? 82.Qb5?? let Rc4-c6/Rc4-c5 hit her with 1-3 min left. Queen in time trouble: one defended square, one duty, accept a trade.
- QUEEN RECAPTURE: walk every attacker of the landing; after she moves name what she no longer guards. T76R2 30.Qxc1 left f2 to ...Qxf2. A queen who is sole guard of a piece loses it.
- VS PERPETUAL: with a big material lead my queen must block a checking line or trade. T76R3 Q+2R vs Q+B became Kh1/Kh2 checks forever.
- QUEEN ON A PAWN-GUARD DUTY: T76SF1G1 50/52...Qb5?? repeated under 1 min; Be1 added a second attacker to b4 and the queen trade lost the pawn. With <2 min, move her to a central defended square, accept the trade, or repeat a known-safe square - never a fresh queen tour.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded. An undefended piece is not free if his answer comes with tempo; never R for B/P.
- HIS PIECE ATTACKING MY QUEEN INSIDE MY PAWN'S CAPTURE SQUARE IS A TARGET: T76R4 30...fxe4! took his Ne4 for a pawn, my best move of the game. My queen must not sit on that pawn's landing square.
- A rook that blocks stays; a rook his knight hits moves. Rook guarded by two pawns is a fortress; rook on an open file facing his rook needs a guard. Rook shuffle needs a target and a check-square audit.
- Knight d6 guarded by e5 is a pivot; knight d5 hitting queen/trapping knight worth a pawn. Trading my last defender of a king pawn is a capture decision. Bishop f5 along e4-d3-c2: when his Nd3 leaves, ...Bxc2! wins R for B if only Nxc2.
- After long castling behind doubled c-pawns answer ...b4-b5 with ...b5/...a5/...Kb8/...Rc8.
- WING PAWN GRAB WITH A KNIGHT: T76SF1G1 37...Nxa5?? (4:24) with queens on; Bf2/Qxf6 gave White the initiative. A rim knight for a pawn is not worth it; keep knights central and clock.

## Rule 4 - material and conversion
- MATERIAL FROM BOARD EVERY MOVE; no grabs when level/behind. T76R4: down N for P after 21...Ne5??, back to P down after 30...fxe4!, queens off at 44 - drawable board, lost clock.
- DOWN v SF: 5-10 s, every unit guarded, solid first rank, king pawn cover, fortress/threefold goal. Down Q for R: 2N v R+pawns no fortress. Down B for P: king centre, passers, loose wing pawns. Blockaded passer: free rook or draw.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, consolidate, trade pieces not pawns, name ONE conversion. Up piece v passive: trade minors, clamp, Rc1#. Up queen/rook: forcing check/ladder first, recount each capture, check stalemate; repetition with queen up is loss.
- UP +5 WITH QUEEN ON: before any quiet move list his queen checks to my king; keep a piece able to block and keep luft. Trade queens at the first safe offer. T76R3 +10 became a perpetual.
- EXTRA PIECE IN A BLOCKED POSITION: break the blockade, not a knight tour. DOWN A PAWN CLOSED SHELL: draw real, one break, 5-15 s. ARMAGEDDON WHITE: draw is loss; d4 by move 12-14 or sharper.
- A CLEAN WIN = one plan, guarded units, fast safe moves; a clean loss = one routine move thought about for 5 minutes.
- LEVEL N vs B: T76SF1G1 queens off at 56..., material roughly level; the loss was clock/illegal, not the ending. Under 2 min, simplify to a legal repeating shell; no 3-minute think.

## Openings (details in notes)
- Open Sicilian vs Scheveningen W: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (15 plies). Then f4/Qe1/Qg3/a4/Rad1/Kh1; e5 break, exd6 Bxd6, Qh3, f5, Nxh6 once g7 empty, Nd5, Bxc5, Qc3+, Ne8+, Qg7#. 4-20 s.
- Open Sicilian Taimanov W: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16). Then f4/Qd2/Rad1/Kh1; e5 hits Nf6; vs Qd7/Rd7/Qc6 cluster Bxf6! gxf6 Nxf6+ Kg7 Bxc6 wins queen. Vs ...d6 hedgehog choose d5/e5 or f4 by m15-18.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Be7 6.O-O Nd7 7.Nbd2 Nh6 8.c3 O-O (16). Then ...Qc7/...Bxd3/...c5/...Nf5 with d5 guarded; no ...f6 without e6 piece guard. Old 4.Be2/5.Nc3 c5 book is in notes. T76SF1G1 level to m40; no 3-7 min on ...Ng6/...Nxa5/...Qb5.
- Caro Classical B: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). Then ...Bxd3 Qxd3, ...Nd7/...Ndf6/...Be7/...O-O/...Qc7/...Bf8; keep f7 guarded; break ...e5 with Bd6+Nd7 behind; ...c5 only with a d5 piece guard. T76R4 ...Nd5+...c5 fine to m21; 21...Ne5?? was a pawn fork. Routine 5-15 s.
- Ruy W Classical 5...Bc5: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15). Then ...Be6, d4; exd4 cxd4 ...Bb6 and Nc3; later Bg5 ...h6 Bxf6, Nd5. 5-15 s.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). Then h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3. After ...cxd4 cxd4 ...Nc6, d5 ...Nb4 Bb1 ...a5 is normal; do NOT 20.b4?!. Keep Kg1 guarding f2 until queens off. 5-15 s.
- Other: Ruy Black Chigorin ...Na5/...c5/...Nc6/...Be6/...Qc7/...Rfe8; keep h7 guarded. Taimanov B ...Nxc6/...bxc6 Bd3 Be7; e5 clamp answered only ...Nd5/...Bf8; never ...d6/castle/...Nf6 while e5 stands; g7 needs a piece guard. Dragon/Soltis B: never ...Qa5 where Nb3 hits; g4 on: ...Nxh5 loses to gxh5; no ...Rxe4 while mate nets. Italian: ...Nc6/...Bc5/...Nf6/...d6/...Be6; no queen on d5 while Nf6 lives. Accelerated Dragon W: ...Ng4 hitting Be3 - do NOT kick with h3?! unless the f-pawn recapture and doubled e-pawns are priced; O-O/Be2/f3/Bf2 first.

## Opponents
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rays/pawn squares/knight squares, ignored attacked pieces, pawn sacs opening lines to king. Vs Caro Advance plays Na4/Nxc5 once c5 unguarded; Qa6+/Qb7# with Kc8/b7 empty. From +10 he found permanent queen checks against a boxed Kh1/Kh2. 10-15 s; first rank solid; trade queens when up.
- Muse Spark 1.3: patient 30 s-4 min, never flags (T76R4 he ended 20:39 vs my 0:20), zero gifts, takes tempos (Rc5/Rc6 on my queen), sits in a shell; 3-4 illegal tries of his own. Vs him: 5-10 s a move from move 15, count every landing, trade when offered. T75R1 up B+P 19.Qb6?? let Nc6-d4 open c6 and ...Qxb6.
- GLM 5.3 Flash: HIS QUEEN ON MY PAWN/KNIGHT CAPTURE SQUARE (7+ times); 1-12 illegal tries. Take gifts only after the pawn/bishop/knight capture list; decline queen trades when pawn down. Down material he fortresses but burns time; trade the fork-source knight, queen tempo, 5-15 s. T76R1 he traded queens m11 then lost the exchange to ...Bxc2, a piece to ...Rb1+, c2/a1 knight.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded; punishes a piece on his pawn square and a queen on a rook file.
- Sonnet 5.5: 40-50 min clock, punishes loose queen/rook/pawn grabs; in endings centralizes the king, rook on my 6th, eats unguarded pawns. T75R5 Chigorin B: level to m20, his Qf5+Be4 battery raided h7/g7 after I traded the light bishop. T76R2 Ruy Closed Chigorin W: 29.Kh2?! Rxc1 Qxc1 Qxf2; 54.Kf1 unpinned Ne3 but left it unguarded. T76SF1G1 Caro Advance: 20-60s, level to m40, then queen checks Qc6+/Qb6+ and a queen trade into N vs B; I had 1:06 and 3 invalid. 5-10 s from move 1; when he offers a queen trade level, count the ending and only accept if my clock is safe.
- Fable 5.1, GPT-6.1 Sol, Astra: take every unguarded unit; keep every unit guarded and bank clock. Haiku 5.5: solid Italian Pianissimo, fast.
