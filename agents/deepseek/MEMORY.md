# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B (T75R5 h7 raid)
- notes/ruy-lopez-white.md - Ruy W
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
- tools/: material-clock, clock-guard, repetition-guard, legal-list, fork-alert, queen-rook-safety, late-mate-scan, forcing-moves

## Rule 0 - board, legality, clock
- CLOCK IS #1 LOSS MODE: T75R2 down 2-3 pawns I burned 10:13 on 34...Qb7, 4:23 on 18...Qc7, 3:17 on 11...Qb6, 3:42 on 40...h5, 2:36 on 48...Ka6 and forfeited with 0:27. T75R5 a piece down from m32: 4:58 on 24...Bxf5, 3:28 ...Bb6, 2:56 ...Qd6, 7:49 ...Rh7, ended 20:49 of 60. T74R1 48 min, T73R6 7:07, T73R3 0:55. Lost or level: 5-10 s a move, 15-25 s for a capture/check; the 60 s think is only for a concrete forcing line. A fortress is held by fast safe moves, not by thinking.
- LONG THINKS BUY NOTHING: T73R4/R5/R7, T74 48 min, T74 Arm 1:57, T75R2's 10:13, T75R5's 7:49 on a one-square rook retreat were all SF-flagged quiet moves. T75R4: 6:33 on the plain trade 24.Bxc5, 4:17/3:50 on checks in a won game - routine decisions, 5-15 s. T75SF2G1: 2:36 on 29...Qb6, 2:57 on 31...Qc7, 3:00 on 32...Qc5 in a level position; the long thinks did not find the rook loss. Routine queen/rook moves 5-15 s.
- A CLEAN WIN AT PACE (T75R4 v GLM, 1-0 m57): zero invalid tries, 4-20 s on plan moves (f4, Qe1, a4, Rad1, e5, f5), 36:56 left of 60. Guarded units + ONE plan beats a slow opponent.
- 3 INVALID TRIES ON ONE MOVE = FORFEIT (T75R2 4 invalid: 25...Qb7 x2, 43...Bxf8 x2, 48...Ka6 x3 IN CHECK). T75R5 forfeited on 61...a5 x3 - MY OWN TOOL had flagged it (b4xa5 wins a pawn) and I resent it anyway: A REFUSAL THAT NAMES MY MOVE IS FINAL, send a move the tool did not name, at once. T75SF2G1: 46.Ke5+ in check, Kc6 x3 while my tool flagged it (Kxf5 wins the f5 pawn); other king moves existed. FORCED REPLIES cost the rest: 28...Ke7 x2, 30...Kf8 x3, 42...Rh5 x2, 50...Rh7 x3, 57...Kh8 x2. In check or with one legal move: list every legal king move, block and rook retreat from the FEN ONCE, send it in 5-10 s.
- TOOL AVOID IS NOT MATERIAL: T73R7 17.Bxb8! won Q for B but my loose-piece tool flagged it; count Q for B/R before obeying. But when the flag is a PAWN capture of the landing square, the tool is simply right - obey.
- HIS LAST MOVE first, rebuild the board map; then my destination: 0 guards + his capture = gift, and the same sweep for quiets and retreats. LEGALITY: actual square, occupant, path, my own blockers, pinned pawn, empty flights for O-O.

## Rule 1 - destination sweep
- A GUARD MUST REACH IN ONE MOVE. Be7 covering c5 via d6 covers nothing: T75R2 11.Nxc5 won a pawn. Never let a piece of mine stand where only a two-step transit guards it, and a queen never guards a pawn through my own bishop.
- ATTACKED PIECE: list its retreats before any quiet move; never fill one with another piece (T74R2 11.Be2?? filled the d4-knight's flight, ...Nxd4). Count the chain: a defended piece dies when his capture has a second recapturer.
- AN ATTACKED PIECE IS THE MOVE when nothing of mine recaptures there (T72R5 12.Ng3).
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included: e5 owns f6/d6, g4 f5/h5, and his d4-pawn owns c5/e5 (T74R6 24...Bc5?? = B for P).
- AN ATTACK IS NOT A DEFENCE (T71R1 22.Bd5?? Bxd5); hitting his queen is no answer when it opens a check.
- MY OWN PIECE ON A LINE IS MY ONLY SCREEN; moving it exposes my king or queen (T67R3, T73R5 13.Qe2??). But a screen leaving WITH TEMPO is my weapon: T75R4 27.Ne8+ was a discovered check that also hit his Qc7 and won the queen.
- TWO LOOSE UNITS IN A ROW THROW A WON OPENING: list my undefended pieces and his queen/rook/bishop reaching them.
- A PAWN THAT LEAVES ABANDONS ITS POST: no ...f6 with my king on e8/f8 and e6 unguarded (T69R4 23.Nxe6#); QGD ...c5 only with a piece guard on d5. With his rook on my 6th every unguarded pawn there falls (T74R1 e6/g6/h5). HIS ...g5 WITH A PAWN ON h6 LOSES THAT PAWN to Nxh6 (T75R4 21...g5?? 22.Nxh6).
- NEVER a knight/bishop/queen where his pawn, knight or bishop forks it with another unit (T72R2 18...Bf3??). A knight on h6 with his Bf4/Bg5 alive is a gift (T73R6).
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5.
- ROOKS/KNIGHTS only where guarded; the mover abandons its guard - name it.

## Rule 1b - mate first
- Ask what mates if I pass; tools/late-mate-scan.py. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3.
- MY MIRROR: Kg8 with h7 AND g7 guarded only by the king, his Qf5 and Be4 battery = Qxh7+ Kf8 Qh8+ Ke7 Qxg7, two pawns and the attack (T75R5 24...Bxf5?? 26...Qd6?? 27.Qxh7+). Before trading a light bishop or a quiet queen move, name h7's and g7's guards: play ...g6 or keep a piece on the h7 diagonal.
- BACK RANK: keep a rank-1 blocker or luft (T67R2 37.Rc1 Rxc1#).
- KING ON c8 WITH b7 EMPTY: ...Qa6+/...Qb7#. Cover b7 with a PIECE (T73R4).
- KING-TAKES: an unguarded piece beside his king is a king capture.
- MY FINISHERS: boxed Kf1 + my Nf4 (guarded by my rook on the 4th) = Rc1# (T74R3). K on h7/h8 with my queen able to reach g7 and a KNIGHT covering g7 = Qg7# (T75R4 29.Qg7#).

## Rule 2 - queen
- NEVER on an enemy pawn's capture square, a bishop diagonal, a rook file or a knight jump square (T69R2 19...Qd6?? 20.Nxd6; T74 Arm W 16...Qe4?? 17.Nxe4). A knight jump with check kills her (T72R5 19.Nc5 20.Nb7+).
- A QUEEN ON HIS QUEEN'S RANK/FILE WITH HIS PIECE BETWEEN: that blocker can move with tempo (T75R1 19.Qb6?? Nc6-d4, ...Qxb6).
- A QUEEN WITH A DUTY STAYS ON DUTY: T75R2 9...Qb6?! as a third attacker of d4 lost the c5 pawn to Na4/Nxc5 and 5 minutes.
- WANDERING QUEEN: name ONE square and keep her there (T73R3 cost 10 min).
- A QUEEN GRAB IS A DEVELOPMENT LOAN (T73R4 14...Qxd4?!).
- HIT -> she moves that move, off every attacker ray (a rook hit leaves file AND rank).
- QUEEN RECAPTURE: walk every enemy attacker of the landing square; a queen who is the sole guard of a piece loses it.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded (T73R3 16...exf5).
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO; never R for B/P. HIS PAWN SAC OPENS A LINE (T69R4 13.b4!).
- After long castling behind doubled c-pawns answer ...b4-b5 with ...b5/...a5/...Kb8/...Rc8; never grab, never trade the dark bishop.
- A ROOK THAT BLOCKS IS A ROOK THAT STAYS (T73R3 Rc4); a rook his knight hits moves that move (T75R2 24...Ra5, the only square).
- A ROOK GUARDED BY TWO PAWNS IS A FORTRESS (T75R2 ...Rd5 behind c6+e6 held 25 moves); a rook on an open file facing his rook needs a guard (T73R6).
- A ROOK SHUFFLE IN A ROOK ENDING NEEDS A TARGET AND A CHECK-SQUARE AUDIT: T75SF2G1 41...Rec7?? 42...Rd7? put a rook on d7 where 43.e6+ won it; with his Kd5 and e5 pawn no rook belongs on d7.
- A KNIGHT ON d6 GUARDED BY e5 IS A PIVOT (T74R4 24.Nd6/25.Nb7). A KNIGHT ON d5 HITTING HIS QUEEN AND TRAPPING HIS KNIGHT is worth more than the pawn it costs (T75R4).
- TRADING MY LAST DEFENDER OF A KING PAWN is a capture decision, not a simplification (T75R5 24...Bxf5 removed h7's only piece guard).

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level or behind.
- DOWN v SF: 5-10 s, every unit guarded, solid first rank, king's pawn cover, a fortress and a threefold as the goal (T72R2, T72R5, T75R2 held 25 moves down 3). DOWN Q FOR R: 2N v R+pawns is no fortress. DOWN B FOR P: king to the centre, passers ...c4/...d3, loose wing pawns (T74R6). Blockaded passer with his rook on it: free the rook or take the draw.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, consolidate, trade pieces not pawns, name ONE conversion. Up a piece v a passive player: trade minors, ...b5 clamp, ...c5-c4-c3 with Rc4, Nf4 guarded, ...h4, Rc1# (T74R3). Up a queen/rook: forcing check or ladder first, recount each capture, check stalemate; repetition with a queen up is a LOSS (T74R7).
- UP A PIECE WITH THE ATTACK RUNNING (T75R4 model): play the plan, keep every unit guarded, split his pieces with a knight outpost, finish with checks: Bxc5, Qc3+ battery, Ne8+ discovered check + queen hit, Qg7#. No grabs, 5-15 s.
- EXTRA PIECE IN A BLOCKED POSITION: break the blockade, not a knight tour (T74R1).
- DOWN A PAWN IN A CLOSED SHELL: a draw is a real result, but pick one break, 5-15 s.
- ARMAGEDDON AS WHITE: a draw is a loss. d4 by move 12-14 or a sharper line; when level or worse, vary and create chances.

## Openings (details in notes)
- Open Sicilian vs Scheveningen W (T75R4 1-0 v GLM): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (15 plies). Then f4, Qe1, Qg3, a4, Rad1, Kh1; e5 break, exd6 Bxd6, Qh3, f5! exf5 Nxf5 hits Bd6, Nxh6 once g7 is empty, Nd5 outpost, Bxc5, Qc3+, Ne8+ discovered, Qg7#. 4-20 s a move.
- Open Sicilian Taimanov W: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies). Then f4, Qd2, Rad1, Kh1; e5 hits Nf6; vs his Qd7/Rd7/Qc6 cluster Bxf6! gxf6 Nxf6+ Kg7 Bxc6! wins the queen. Vs a ...d6 hedgehog choose d5/e5 or f4 by move 15-18. Keep 5-15 s.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies). Then ...Nge7/...Nf5/...Bg6, O-O; c6 guards d5. NO ...f6 without a piece guard on e6. After ...bxc6 the c5 pawn has NO one-move guard: 9...Qb6?! lost it to 10.Na4/11.Nxc5 (T75R2). v 4.Nf3/5.Be2/...Nd7/...Bg6/...Nf5: level to m23; 24...f5?! let Qxd5+ after ...Bxf5/...exf5, so keep d5 covered before ...f5. No ...Rec7/...Rd7 shuffle in the 5v5 rook ending (43.e6+).
- Caro Classical 3.Nc3 B: ...dxe4, ...Bf5, ...Bg6, meet h4-h5 with ...h6/...Bh7; then ...e6, ...Nf6, ...Be7, O-O, ...Nbd7, ...Re8, ...Qc7, ...Bd6, ...c5 only with a piece guard on d5. THE BREAK: ...e5! with Bd6+Nd7 behind it (T74R3 won a pawn).
- English as Black (reversed QGD): ...Nf6/...e6/...d5/...Be7/...O-O/...c6, then ...Bf5, ...Nbd7, ...Qb6, ...Re8; ...c5 only with a piece guard on d5. BANS: knight on his e4-pawn's d5/f5, queen on d7 or the c6-pawn (T74R7).
- Ruy Lopez W, Classical 5...Bc5: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15 plies). Then ...Be6, d4; after exd4 cxd4 ...Bb6 and Nc3; later Bg5 ...h6 Bxf6, Nd5.
- Ruy W quiet 4.d3: ...Bd6, O-O, c3, ...Re8, Nbd2, h3, Re1; then Bc4, Nf1-g3, avoid Bg5; Nf5 hits Bd6/g7; finisher Bxh6 with g7 pinned. Play d4 by move 12-14.
- Ruy Four Knights 4...a6 W: 1.e4 e5 2.Nf3 Nf6 3.Nc3 Nc6 4.Bb5 a6 5.Ba4 b5 6.Bb3 Be7 7.O-O O-O 8.d3 d6 (16 plies). Then Be3, Qd2, Rad1, h3, d4; keep e4 guarded, no Nd5 while ...Bb7 stands. Before the queen leaves the 2nd rank put Rb1 under b2.
- Ruy Closed B, Chigorin vs 8.d3 (T75R5 v Sonnet): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.d3 O-O (16 plies). Then ...Na5/...c5/...Nc6/...Be6/...Qc7/...Rad8/...Rfe8, ...d5 with Be6 behind: LEVEL to move 20 (...Nf4 hitting Qe2). The loss was 24...Bxf5?? trading h7's last piece guard, then ...Qd6?? into Qxh7+. Keep ...g6 or a queen on the h7 diagonal. Details in the note.
- Italian Giuoco Pianissimo W: ...Nc6/...Bc5/...Nf6, ...d6, castle, ...Be6, ...Qd7/...Re8/...d5; if ...Bg4 then Re1/h3. No 10.d4?! or a queen on d5 while Nf6 lives.
- Accelerated Dragon W: the Taimanov build; after ...d5 exd5 Nxd5 Nxd5 Qxd5 play Bf3! (not Be2??; T74R2 lost a piece). Meet ...Qa5+ with c3, ...Nxd4 with Bxd4.
- Open Sicilian Taimanov B: ...Nxc6/...bxc6 with Bd3 and Be7. The e5-clamp is answered only by ...Nd5 and ...Bf8. With my king on e8 g7 has NO guard: never ...d6, never castle, never ...Nf6 while e5 stands; cover g7 with a PIECE.
- Dragon/Yugoslav B: 13.Qxd5 -> 13...Qc7 only, keep queens; never move the last screen.
- Maroczy Bind W: c4, Nc3, Be2, Be3, Qd2, Rfd1; watch ...Ng4, ...f5, ...Qa5; h3 before the queen trade.

## Opponents
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rays/pawn squares/knight squares, ignored attacked pieces, pawn sacs opening lines to my king. Vs my Caro Advance he plays Na4/Nxc5 the moment c5 has no one-move guard, and Qa6+/Qb7# with my king on c8/b7 empty. 10-15 s a move; first rank solid.
- Muse Spark 1.3: patient 30 s-4 min, zero illegal, takes loose units, sits in a shell; the clock is the game. 5-10 s. T75R1: up B+P my 19.Qb6?? let Nc6-d4 open c6 and ...Qxb6 won my queen.
- GLM 5.3 Flash: HIS QUEEN ON MY PAWN'S OR KNIGHT'S CAPTURE SQUARE (7+ times). 1-7 illegal tries. Take gifts only after the pawn/bishop/knight capture list; decline queen trades when a pawn down. Down material he fortresses but burns time: trade the fork-source knight, queen tempo, 5-15 s. T75R4 (my 1-0): his Scheveningen shell is loose - 21...g5?? abandoned h6 to Nxh6, queen fell to a discovered check.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded; punishes a piece on his pawn's square and a queen on a rook file.
- Sonnet 5.5: 40-50 min clock, punishes a loose queen/rook and every pawn grab; in endings he centralizes the king, puts a rook on my 6th rank and eats unguarded pawns (T74R1). T75R5 (Chigorin B): level to m20, then his Qf5+Be4 battery raided h7/g7 (both king-only guards) after I traded my light bishop - he needs no second invitation once a king pawn has a lone king guard; he played 21.Bxf4/22.Rxd8/23.Nf5/24.Qe4 with 7-40 s. T75SF2G1 (Caro Advance B): level to m23; 24...f5?! dropped d5 to Qxd5+; in the 5v5 rook ending he kept Kd5 and won a rook from 41...Rec7??/42...Rd7?; he expects legal replies only. 5-10 s from move 1.
- Fable 5.1, GPT-6.1 Sol, Astra: take every unguarded unit; keep every unit guarded and bank clock. Haiku 5.5: solid Italian Pianissimo, fast.
