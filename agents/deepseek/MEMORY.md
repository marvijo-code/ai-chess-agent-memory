# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W incl. 5.d3 (T78R1)
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
- tools: legal-list, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender

## Rule 0 - board, legality, clock
- FORFEIT BEATS BLUNDER: three refused tries on ONE reply end the game (T78R1 at 33...dxe4 with 58 min left; T77R6 empty reply; T77R5 12 tries). After ONE refusal change piece AND idea. If a tool flags the move I planned, send the least-bad DIFFERENT legal move in ONE try and never resend it.
- Clock: routine 5-15 s; capture/check/pawn break 15-25 s; 30+ s only for a named forcing line. T78R1's only long think (1:15 on 33.Qd4??) was the game's only ?? move. From m15 level/worse cap 20 s; under 5 min 5 s; under 1 min 2 s and copy a legal UCI.
- In check/forced: read the FEN once, list every legal reply, send the exact UCI in 5-10 s; never a remembered square.
- Tool AVOID is not material: count queen for bishop/rook before obeying; obey pawn-capture and queen-loss flags. His last move first; legality actual square, occupant, path, own blockers, pinned pawn, castling flights.
- Material from the board every move. Name my loose units and his queen/rook/bishop lines to them before any quiet move.

## Rule 1 - destination sweep
- RECAPTURE WITH THE PIECE THAT DOES NOT OPEN A LINE: T77R5 31...Qxc3 32.Nxc3?? took Ne2 off b5-f1 and ...Bxf1 won the exchange. Name the ray the mover leaves.
- A GUARD MUST REACH IN ONE MOVE; a pinned guard guards nothing (T77R3 17.Bd5?? Nxd5). An attacked piece gets its retreat list before any quiet move.
- KING AND PIECE ON ONE RANK FACING HIS ROOK: T77R5 Ra3+Kf3 pinned Bc3; move the K off the rank or add a second guard.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; every knight jump; every bishop/rook line. A pawn that leaves abandons its post.
- PAWN FORK ON A KNIGHT LANDING (T76R4 21...Ne5?? 22.dxe5); before a knight lands in his centre list his pawn captures.
- AN ATTACK IS NOT A DEFENCE; my own piece on a line is my only screen.

## Rule 1b - mate first
- Ask what mates if I pass; keep a rank-1 blocker or luft; K on c8 with b7 empty is a mating net.
- Before trading a light bishop or a quiet queen move, name h7/g7 guards. Finishers: Rc1#, Qg7#, heavy-piece box.
- Level position: no 30+ s think.

## Rule 2 - queen
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. T78R1 33.Qd4?? sat in front of Rd8 and on the e4 square his Qb7 covered; 33...dxe4 forced her off and every try was refused.
- QUEEN HIT ON A FILE: she leaves the file AND the rank; never capture on the square his queen covers along her diagonal (b7-c6-d5-e4).
- HIS ROOK ON THE 4th-6th GAINS A TEMPO ON MY QUEEN (T76R4 Qa6??).
- QUEEN RECAPTURE: walk every attacker of the landing; name what she no longer guards (T76R2 30.Qxc1).
- VS PERPETUAL with a material lead: block or trade (T76R3).
- NO QUEEN SHUTTLE WITHOUT A NEW TARGET: T77R6 Qb6-Qc7-Qb6; T77R7 Qc6-Qd6-Qc6 drew up B for P. A retreat must take a new duty, else play a rook/pawn plan.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET (T76R4 30...fxe4).
- A rook that blocks stays; a rook his knight hits moves; a rook shuffle needs a target.
- Knight d6 guarded by e5 is a pivot; bishop on e4-d3-c2: ...Bxc2 wins R for B when Nd3 leaves.
- WING PAWN GRAB WITH A KNIGHT: T76SF1G1 37...Nxa5??; keep knights central; Bc3 after ...c5 is hit by ...b4.

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. Before trading queens count the pawns and diagonals it hands him (T77R5).
- DOWN v SF: 5-10 s, every unit guarded, solid first rank, fortress/threefold goal.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, trade pieces not pawns, name ONE conversion; a repetition is MY loss - make one permanent change first.
- DOWN MATERIAL, A REPETITION IS MY SAVE (T77R3, T77R4).
- A KNIGHT WITH NO TARGET IS PLAN DRIFT: T78R1 20.Nh4? 21.Nhf5 (kicked by ...g6/...h5), then Nd4-Nf3-Nd4-Nf3; 31.Nf3? let ...Nxf3+ wreck f2/g2 and ...d5 came. If the knight has no square that hits something, play a rook/pawn plan.
- A CLEAN WIN = one plan, guarded units, fast safe moves; a clean loss = one routine move thought about for 5 minutes.

## Openings
- Scheveningen W v GLM/Muse: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (15). Then f4, Qe1-g3, a4, Rad1/Kh1; e5 break, exd6/Bxd6, Nxh6 when g7 empties.
- Taimanov W: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16). Then f4/Qd2/Rad1/Kh1; e5 hits Nf6; Bxf6 gxf6 Nxf6+ vs his Qd7/Rd7 cluster.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Be7 6.O-O Nd7 7.Nbd2 Nh6 8.c3 O-O (16). Then ...Qc7/...Bxd3/...Nf5; ...c5 only with a PIECE on d5 (T77R4 10...c5??).
- Caro Classical B: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). Then ...Nd7/...Nf6/...Be7/...O-O/...Qc7; ...e5 needs Bd6+Nd7; ...c5 needs a d5 piece guard. T77R7.3 active c4/c5/Be5/Ne4 won on time.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). Then h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no 20.b4.
- Ruy W 5.d3 (T78R1 v Sonnet): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 d6 6.c3 Be7 7.O-O O-O 8.Nbd2 (15). Then Re1/Bc2/Nf1-g3/d4. Level to move 30 in T78R1; ...Na5/...c5/...Bb7/...Re8 and ...Nfg4 hitting Be3 are his plan; after ...dxe4 never take with the queen (Qb7 covers e4) and never put her in front of Rd8.
- Other patterns: Ruy Classical 5...Bc5: c3/O-O/Re1/h3 then d4 and ...Be6; Bb6/Nc3/Bg5/Nd5 after the exchange. Ruy B Chigorin: ...Na5/...c5/...Be6/...Qc7, keep h7 guarded. Taimanov B: ...Bf8 vs the e5 clamp, never castle/...d6/...Nf6 while e5 stands. Dragon/Soltis B: never ...Qa5 where Nb3 hits. Accelerated Dragon W: no h3?! kick of ...Ng4; O-O/Be2/f3/Bf2 first. Italian W v Muse: c4/b3, d3/c3, Re1/Rd1, Nbd2 then d4.

## Opponents
- Sonnet 5.5: 40-50 min clock, punishes loose queen/rook/pawn grabs; T77R5 ...Re8/...Bf8/...Bf5/...b4 squeeze; T78R1 the same slow squeeze and my forfeit at 33...dxe4. 5-10 s from move 1; keep the queen off his pawn/bishop/rook squares.
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rays; fortress at +7.7 allowed threefold.
- Muse Spark 1.3: patient 30 s-4 min early; banks clock; I must move 5-10 s from move 15. T77R7.3 won on time; T77R7 the queen shuttle drew up B for P.
- GLM 5.3 Flash: his queen on my pawn/knight capture square (7+ times); take gifts only after the capture list; T77R2 he steered a threefold when I was up.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
