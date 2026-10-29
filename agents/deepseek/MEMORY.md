# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W (new T76R2)
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
- tools/: material-clock, clock-guard, repetition-guard, legal-list, fork-alert, queen-rook-safety, late-mate-scan, forcing-moves

## Rule 0 - board, legality, clock
- CLOCK: routine 5-15 s; capture/check/pawn break 15-30 s; 60 s only concrete forcing line. Long thinks found nothing: T75R2 10:13, T75R5 7:49, T76R1 6:28, T76R2 4:51/5:04 while down. Lost/level/fortress 5-10 s. A clean win = one plan, guarded units, fast safe moves.
- 3 invalid tries on ONE move = forfeit. After ONE rejection change piece AND idea; a refusal naming my move is final, send another. In check/forced: list every legal reply from FEN once, send in 5-10 s.
- Tool AVOID is not material: count Q for B/R before obeying; obey pawn-capture flags. His last move first; rebuild board; legality actual square, occupant, path, own blockers, pinned pawn, O-O flights. A knight from d7 has no g4 jump.
- Material from board every move. Name my loose units and his queen/rook/bishop reaching them before any quiet move.

## Rule 1 - destination sweep
- A GUARD MUST REACH IN ONE MOVE. Be7 covering c5 via d6 covers nothing. An attacked piece: list retreats before quiet; never fill its flight with another piece. A defended piece dies when his capture has a second recapturer; if nothing recaptures, move it.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; all knight jumps; every bishop/rook line. My piece on his pawn's capture square is lost. A pawn that leaves abandons its post: no ...f6 with Ke8/f8 and e6 loose; ...c5 only with d5 piece guard; ...g5 vs h6 loses h6 to Nxh6.
- Never a piece where his pawn, knight or bishop forks it with another unit. Rooks/knights only guarded; name the guard the mover abandons. A checking piece near his king: count king capture; a check is safe only if guarded or king cannot take.
- AN ATTACK IS NOT A DEFENCE. My own piece on a line is my only screen; moving it exposes king/queen. A screen leaving with tempo is a weapon.

## Rule 1b - mate first
- Ask what mates if I pass. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3. Keep rank-1 blocker or luft. K on c8 with b7 empty = ...Qa6+/...Qb7#; cover b7 with a piece.
- Before trading a light bishop or quiet queen move, name h7/g7 guards. My finishers: boxed Kf1 + Nf4 + rook on 4th = Rc1#; K h7/h8 + queen reaching g7 + knight covering g7 = Qg7#; up R+B+N roll a pawn, keep flights covered, avoid stalemate.

## Rule 2 - queen
- NEVER on enemy pawn capture square, bishop diagonal, rook file or knight jump. Hit -> she moves that move off every ray (rook hit leaves file AND rank). Queen with a duty stays on duty. A queen on his queen's rank/file with his piece between: that blocker can move with tempo.
- QUEEN RECAPTURE: walk every attacker of landing; after she moves name what she no longer guards. T76R2 30.Qxc1 left f2 to ...Qxf2; the king on g1 would have guarded it. A queen who is sole guard of a piece loses it.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded. An undefended piece is not free if his answer comes with tempo; never R for B/P. After long castling behind doubled c-pawns answer ...b4-b5 with ...b5/...a5/...Kb8/...Rc8.
- A rook that blocks stays; a rook his knight hits moves. Rook guarded by two pawns is a fortress; rook on open file facing his rook needs guard. Rook shuffle needs target and check-square audit.
- Knight d6 guarded by e5 is a pivot; knight d5 hitting queen/trapping knight worth pawn. Trading my last defender of a king pawn is a capture decision. Bishop f5 along e4-d3-c2: when his Nd3 leaves, ...Bxc2! wins R for B if only Nxc2.

## Rule 4 - material and conversion
- MATERIAL FROM BOARD EVERY MOVE; no grabs when level/behind.
- DOWN v SF: 5-10 s, every unit guarded, solid first rank, king pawn cover, fortress/threefold goal. Down Q for R: 2N v R+pawns no fortress. Down B for P: king centre, passers, loose wing pawns. Blockaded passer: free rook or draw.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, consolidate, trade pieces not pawns, name ONE conversion. Up piece v passive: trade minors, clamp, Rc1#. Up queen/rook: forcing check/ladder first, recount each capture, check stalemate; repetition with queen up is loss. Up a piece with attack: keep every unit guarded, finish with checks.
- EXTRA PIECE IN BLOCKED POSITION: break blockade, not knight tour. DOWN A PAWN CLOSED SHELL: draw real, pick one break, 5-15 s. ARMAGEDDON WHITE: draw is loss; d4 by move 12-14 or sharper.

## Openings (details in notes)
- Open Sicilian vs Scheveningen W: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (15 plies). Then f4/Qe1/Qg3/a4/Rad1/Kh1; e5 break, exd6 Bxd6, Qh3, f5, Nxh6 once g7 empty, Nd5, Bxc5, Qc3+, Ne8+, Qg7#. 4-20 s.
- Open Sicilian Taimanov W: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16). Then f4/Qd2/Rad1/Kh1; e5 hits Nf6; vs Qd7/Rd7/Qc6 cluster Bxf6! gxf6 Nxf6+ Kg7 Bxc6 wins queen. Vs ...d6 hedgehog choose d5/e5 or f4 by m15-18.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16). Then ...Nge7/...Nf5/...Bg6, O-O; c6 guards d5. NO ...f6 without piece guard on e6; after ...bxc6 c5 has no one-move guard (9...Qb6?! Na4/Nxc5). Keep d5 covered before ...f5. No ...Rec7/...Rd7 shuffle in 5v5 rook ending.
- Caro Classical B: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). Then ...Bxd3 Qxd3, ...Nd7/...Ndf6/...Be7/...O-O-O/...Qc7/...Bf8; keep f7 guarded; break ...e5 with Bd6+Nd7 behind; ...c5 only with d5 piece guard. Routine 5-15 s.
- Ruy W Classical 5...Bc5: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15). Then ...Be6, d4; exd4 cxd4 ...Bb6 and Nc3; later Bg5 ...h6 Bxf6, Nd5. Keep 5-15 s.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). Then h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3. After ...cxd4 cxd4 ...Nc6, d5 ...Nb4 Bb1 ...a5 is normal; do NOT 20.b4?! ( ...axb4 ...bxa3 opens a-file and loses pawn). Keep Kg1 guarding f2 until queens off; Kf1 unguards e3. 5-15 s.
- Other: Ruy Black Chigorin ...Na5/...c5/...Nc6/...Be6/...Qc7/...Rfe8; keep h7 guarded (no ...Bxf5 trading last h7 guard). Taimanov B ...Nxc6/...bxc6 Bd3 Be7; e5 clamp answered only ...Nd5/...Bf8; never ...d6/castle/...Nf6 while e5 stands; g7 needs piece guard. Dragon/Soltis B: never ...Qa5 where Nb3 hits; g4 on: ...Nxh5 loses to gxh5; no ...Rxe4 while mate nets. Italian: ...Nc6/...Bc5/...Nf6/...d6/...Be6; no queen on d5 while Nf6 lives.

## Opponents
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rays/pawn squares/knight squares, ignored attacked pieces, pawn sacs opening lines to king. Vs Caro Advance plays Na4/Nxc5 once c5 unguarded; Qa6+/Qb7# with Kc8/b7 empty. 10-15 s; first rank solid.
- Muse Spark 1.3: patient 30 s-4 min, zero illegal, takes loose units, sits in shell; clock is game. 5-10 s. T75R1 up B+P my 19.Qb6?? let Nc6-d4 open c6 and ...Qxb6. Classical Caro level to m30; keep units guarded.
- GLM 5.3 Flash: HIS QUEEN ON MY PAWN/KNIGHT CAPTURE SQUARE (7+ times); 1-12 illegal tries. Take gifts only after pawn/bishop/knight capture list; decline queen trades when pawn down. Down material he fortresses but burns time; trade fork-source knight, queen tempo, 5-15 s. T75R4 his Scheveningen shell loose: 21...g5?? abandoned h6 to Nxh6, queen fell to discovered check. T76R1 he traded queens m11 then lost exchange to ...Bxc2, piece to ...Rb1+, c2/a1 knight.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded; punishes piece on his pawn square and queen on rook file.
- Sonnet 5.5: 40-50 min clock, punishes loose queen/rook/pawn grabs; in endings centralizes king, rook on my 6th, eats unguarded pawns. T75R5 Chigorin B: level to m20, his Qf5+Be4 battery raided h7/g7 after I traded light bishop. T75SF2G1 Caro Advance: 24...f5?! dropped d5; 5v5 rook ending 41...Rec7??/42...Rd7? lost rook. T76R2 Ruy Closed Chigorin W: solid; after 29.Kh2?! Rxc1 Qxc1 Qxf2 won f2; 54.Kf1 unpinned Ne3 but unguarded it, ...Bxe3; converts. 5-10 s from move 1.
- Fable 5.1, GPT-6.1 Sol, Astra: take every unguarded unit; keep every unit guarded and bank clock. Haiku 5.5: solid Italian Pianissimo, fast.
