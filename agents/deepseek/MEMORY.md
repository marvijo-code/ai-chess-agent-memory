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
- FORFEIT BEATS BLUNDER: three refused tries on ONE reply end the game (T78R1 at 33...dxe4; T77R6 empty reply; T77R5 12 tries). After ONE refusal change piece AND idea. If a tool flags the move I planned, send the least-bad DIFFERENT legal move in ONE try and never resend it.
- TOOL FLOOD IS NOT THREE TRIES: T78R3 after 14.Nf5 hit h6, every legal reply lost at least a pawn; I tried three flagged moves and forfeited. T78SF2G1 v Sonnet: 13 invalid, five 3-try gated moves (26...Qd6 12:30, 31...Ra5 4:30, 41...g5 3:38, 42...Kh7, 45...Kf8); 30 min to 4 min in 16 moves. When all moves are flagged, the position is lost, not a search: read once, send the least-bad DIFFERENT legal move in ONE try at 5-10 s. A one-pawn loss is playable; a 12-minute gated think is not. T78R7 (level game): 4:44 on 14...g5 with 3 tries - a weakening pawn move is never worth that.
- EVEN A WON GAME PAYS FOR TRIES: T78R2 (1-0) 6 invalid attempts and 3 gated; T78R4 (1-0) 41.Rf1 and 42.Rfe1 each took 2 tries in a quiet keeper phase; T78R7 (0-1) 13...Bf8 illegal plus two malformed UCIs at 14...g5. Re-read the FEN and send a plainly legal UCI; when a quiet keeper move is refused, send a DIFFERENT legal quiet move (K shuffle) in one try.
- Clock: routine 5-15 s; capture/check/pawn break 15-25 s; 30+ s only for a named forcing line. Long thinks on quiet keepers find nothing: T78R1 1:15 on 33.Qd4??; T78R4 5:48 Kh2, 5:10 c4, 4:11 Qe4 - all SF ?/?!. From m15 level/worse cap 20 s; under 5 min 5 s; under 1 min 2 s and copy a legal UCI.
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
- BACK-RANK FINISHER (T78R2 37...Rc1+! 38.Rd1 Rxd1+ 39.Re1 Rxe1#): his king boxed on g1 by f2/g2/h2 and a rook that must block on the 1st rank; every block loses a rook, then mate. When his rooks are tied to pawns and my rook can reach the 1st rank WITH CHECK, play it.
- Before trading a light bishop or a quiet queen move, name h7/g7 guards. Finishers: Rc1#, Qg7#, heavy-piece box.
- Level position: no 30+ s think.

## Rule 2 - queen
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. T78R1 33.Qd4?? sat in front of Rd8 and on the e4 square his Qb7 covered.
- QUEEN HIT ON A FILE: she leaves the file AND the rank; never capture on the square his queen covers along her diagonal (b7-c6-d5-e4).
- HIS ROOK ON THE 4th-6th GAINS A TEMPO ON MY QUEEN (T76R4 Qa6??).
- QUEEN RECAPTURE: walk every attacker of the landing; name what she no longer guards (T76R2 30.Qxc1).
- VS PERPETUAL with a material lead: block or trade (T76R3).
- NO QUEEN SHUTTLE WITHOUT A NEW TARGET: T77R6 Qb6-Qc7-Qb6; T77R7 Qc6-Qd6-Qc6 drew up B for P; T78R4 Qe4-Qf5-Qe4-Qf4 over 8 moves, all SF ?/?!. A retreat must take a new duty, else play a rook/pawn plan.
- QUEEN+KING KNIGHT FORK: Qd6 + Kg7 with his knight on h4/e5 = ...Nf5+ forking both (T78SF2G1 42.Nf5+ won the queen). Before a quiet keeper, list his knight jumps to f5/e6/e8/h5; keep Q off d6 when a knight can reach f5, or move the king to h8/g8.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET (T76R4 30...fxe4).
- A rook that blocks stays; a rook his knight hits moves; a rook shuffle needs a target.
- Knight d6 guarded by e5 is a pivot; bishop on e4-d3-c2: ...Bxc2 wins R for B when Nd3 leaves.
- WING PAWN GRAB WITH A KNIGHT: T76SF1G1 37...Nxa5??; keep knights central; Bc3 after ...c5 is hit by ...b4.
- KNIGHT TRADES AND LANDINGS: T78R7 10...Nxc3? 11.bxc3 sharpened his c3/d4/e5 chain and left my bishop jobless (SF ?); Nf6-e4-c5-e4-c6 was six ?/?! moves whose landings hit only defended pawns. A knight that hits nothing is drift - play the ...c5 break; keep the tension unless the trade wins material.

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. Before trading queens count the pawns and diagonals it hands him (T77R5).
- A TRADE-DOWN AT +1P IS A CONVERSION (T78R2 31...Qxe2 32.Rxe2, rooks traded down, extra pawn kept, then the back-rank mate). Name ONE net: the mate box or the passer; never shuffle.
- DOWN v SF: 5-10 s, every unit guarded, solid first rank, fortress/threefold goal. If every legal move loses a pawn, send the least-bad one in ONE try.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, trade pieces not pawns, name ONE conversion; a repetition is MY loss - make one permanent change first.
- DOWN MATERIAL, A REPETITION IS MY SAVE (T77R3, T77R4).
- DOWN A PIECE, A FORTRESS NEEDS NO WEAK PAWN: T78SF2G1 ...b5-b4 left a b4 pawn that tied Qd6/Rb5 and set the Nf5+ fork; SF marked ...f6?! ...h6? ...c5?! ...cxb4?? ...Nb6?? ...Qd6?!. A wing expansion that leaves a permanent defended pawn (b4) is a target, not space; when down, keep pieces active and avoid a second weakness.
- A KNIGHT WITH NO TARGET IS PLAN DRIFT: T78R1 20.Nh4? then Nd4-Nf3 shuffles; T78R4 16.Nc5?? answered by ...Rb8/...Qc8, then N5e4-Ne2-Nd4-Ng3-Ndf5-Nd4-Ndf5-Nd4 over 12 moves, every one SF ?/??. If the knight has no square that hits something, trade it or play a rook/pawn plan.
- A CLEAN WIN = one plan, guarded units, fast safe moves. VS A SHUFFLING OPPONENT WITH A CLOCK LEAD: 10-20 s keepers, ONE plan (trade a piece pair, push the passer, h4 a trapped bishop), never a 5-minute think on a quiet keeper - my own clock buys nothing. A level game against a slow opponent is won by HIS forfeit (T78R7 'Rfc1' after 2 illegal + gated floods): legality, 5-15 s keepers, no ambition.

## Openings
- Scheveningen W v GLM/Muse: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (15). Then f4, Qe1-g3, a4, Rad1/Kh1; e5 break, exd6/Bxd6, Nxh6 when g7 empties.
- Scheveningen vs his ...a6/...e5/...Be6 (T78R4 v Muse): f4 exf4 Bxf4 is level and safe; his b7/e6 are covered once ...Rb8/...Qc8/...Rfe8 come, so Nc5 and Bf3 there are ?? - the target is the bishop on g5/h6 (h4, Nxh6) or a trade on f6.
- Taimanov W: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16). Then f4/Qd2/Rad1/Kh1; e5 hits Nf6; Bxf6 gxf6 Nxf6+ vs his Qd7/Rd7 cluster.
- English/Nimzo B v GLM (T78R2, 1-0 Rxe1#): 1.c4 Nf6 2.Nc3 e6 3.d4 Bb4 4.Nf3 d5 5.cxd5 exd5 6.Qa4+ Nc6 7.Bd2 Bd6 8.e3 O-O (16). 6...Nc6! blocks the check AND covers b4 (Qxb4 Nxb4). Then ...Bf5/...Be6, ...Qe7, ...Rab8+...a6 (b5 only when a6 AND Rb8 cover it), ...Nb4 hitting c2/d3, ...Bxf3 gxf3 leaves d4 guarded only by his queen, ...Qxd4 wins it. Keep c6-knight + Bd6 (b7 guards c6, so Bxc6 bxc6 is fine); answer Qb3 on b7/d5 with ...Rb8 or ...Qb4.
- English B when he plays 3.e4 (T78R7 v GLM): 1.c4 Nf6 2.Nc3 e6 3.e4 d5 4.e5 (7 plies) = French-Advance shape with colours reversed. Break with ...c5 on d4 (behind ...Nc6/...Nd7), develop ...Be7/...O-O/...Be6 or ...Bf5; NO ...Nxc3 trade, NO ...g5/...h6 in front of Kh8. Level to m30; my ?/?! were knight shuffles and those pawn pushes.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 (7 plies) then ...e6/...Be7/...Nd7/...Nh6/...O-O; ...c5 only with a PIECE on d5. T78R3 v SF: after ...O-O and Bd3, 10...f6?? with Bf5 still on and e5 alive lost to 11.Bxf5! exf5 12.e6! (Nd7->b8, then Nh4-Nf5 hits h6/g7); keep f6 back until Bd3 is traded or e5 is gone. T78SF2G1 v Sonnet: ...a5/...b5/...b4 became a liability (SF ?? at ...cxb4/...Nb6/...Qd6); ...b4 needs a piece guard and a trade plan. Loss was the gated flood and Nf5+ fork. Details notes/caro-advance-black.md.
- Caro Classical B: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). Then ...Nd7/...Nf6/...Be7/...O-O/...Qc7; ...e5 needs Bd6+Nd7; ...c5 needs a d5 piece guard. T77R7.3 active c4/c5/Be5/Ne4 won on time.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). Then h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no 20.b4.
- Ruy W 5.d3 (T78R1 v Sonnet): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 d6 6.c3 Be7 7.O-O O-O 8.Nbd2 (15). Then Re1/Bc2/Nf1-g3/d4. His plan: ...Na5/...c5/...Bb7/...Re8 and ...Nfg4 hitting Be3; after ...dxe4 never take with the queen (Qb7 covers e4) and never put her in front of Rd8.
- Other patterns: Ruy Classical 5...Bc5: c3/O-O/Re1/h3 then d4; Bb6/Nc3/Bg5/Nd5 after the exchange. Ruy B Chigorin: ...Na5/...c5/...Be6/...Qc7, keep h7 guarded. Taimanov B: ...Bf8 vs the e5 clamp, never castle/...d6/...Nf6 while e5 stands. Dragon/Soltis B: never ...Qa5 where Nb3 hits. Accelerated Dragon W: no h3?! kick of ...Ng4; O-O/Be2/f3/Bf2 first. Italian W v Muse: c4/b3, d3/c3, Re1/Rd1, Nbd2 then d4.

## Opponents
- GLM 5.3 Flash: as White 1.c4/2.Nc3/3.d4/4.Nf3 Carlsbad (T78R2); his queen wandered a4-b3-a4 and his bishops b3-d5-f3-g4 with no plan, he gave up d4 and both bishops, then his rooks were pinned to d6/b7 and Rc1+ mated him. 9 invalid tries. His queen sits on my pawn/knight capture squares (7+ times); take gifts only after the capture list. He steers a threefold when I am up (T77R2). T78R7 (0-1 forfeit): 1.c4/2.Nc3/3.e4 vs my ...e6/...d5, 2 illegal plus gated floods, forfeited on the illegal 'Rfc1'; 50:39 vs my 41:51 - he loses the legality war, not the chess.
- Sonnet 5.5: 40-50 min clock, punishes loose queen/rook/pawn grabs; T77R5 ...Re8/...Bf8/...Bf5/...b4 squeeze; T78R1 the same slow squeeze and my forfeit at 33...dxe4. T78SF2G1: punishes ...b4 expansion and Nf5+ fork; banks clock while I gated. 5-10 s from move 1; keep the queen off his pawn/bishop/rook squares.
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rays; fortress at +7.7 allowed threefold. T78R3: 10...f6?? met Bxf5 exf5 e6!; once Nf5 hits h6, accept the pawn and play one legal move, never burn tries.
- Muse Spark 1.3: patient 30 s-4 min early; banks clock; I must move 5-10 s from move 15. T77R7.3 won on time; T77R7 the queen shuttle drew up B for P. T78R4 (1-0 forfeit m45, 22:28 vs 0:00): he shuffled ...Rb8/...Qc8/...Qc7/...Rc7/...Re7 for the whole game and I won B for N twice by h4 trapping Bg5 and Nxh6; equal material to m30, the win was his flag. Give him no loose unit, keep queens, take 10-20 s keepers, and do not spend my own clock on quiet queenside/king shuffles.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
