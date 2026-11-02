# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W incl. 5.d3 (T78R1)
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W (T79R1 draw v SF)
- notes/sicilian-soltis-black.md - Soltis B
- tools: legal-list, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender, knight-exit (a knight landing with no retreat square)

## Rule 0 - board, legality, clock
- FORFEIT BEATS BLUNDER: three refused tries on ONE move end the game (T78R1 33...dxe4; T77R6 empty reply; T77R5 12 tries). After ONE refusal change piece AND idea. If a tool flags the move I planned, send the least-bad DIFFERENT legal move in ONE try and never resend it. T79R1: after three refusals the REFEREE plays a move and the game goes on - tries cost CLOCK above all. T79R2: 14...Bxg5?? 15.Nxg5 left Qxh7#/Nxh7; a tool called it 'about 1 pawn down' and three refused tries forfeited m15. ONE pawn lost is not a search: block with ...f5/...Nf5, send it, accept the pawn.
- TOOL FLOOD IS NOT THREE TRIES: T78R3 14.Nf5; T78SF2G1 13 invalid and five 3-try moves (30 min to 4); T79R1 14 invalid, 9:21 on 16.Ba6; T79R4 4 invalid (gated) in a quiet game. T79SF2G1: 22...Nxd4 and 23...Na4 each ate 3 gated tries (6:30, 4:45) and the referee replayed its BEST-SO-FAR - a knight into the Rb1 trap, a piece. When every legal move is flagged, send the legal move that KEEPS THE MOST MATERIAL in ONE try, never the most active one. A one-pawn loss is playable; a 12-minute gated think is not.
- TOOLS MUST LEAVE AN OUT (T79R1): material-clock prints the 3 least-loss moves first and flags only losses >= a rook, always keeping >=3 legal moves unflagged; rep-material-watch flags a repeat only when I am AHEAD. When a tool flags my idea, take a move no tool flagged; never re-argue a refused keeper.
- EVEN A WON GAME PAYS FOR TRIES: T78R2 6 invalid; T78R4 41.Rf1/42.Rfe1 two tries each; T78R7 13...Bf8 illegal. Re-read the FEN and send a plainly legal UCI; a refused quiet keeper becomes a DIFFERENT quiet keeper (K shuffle) in one try.
- Clock: routine 5-15 s; capture/check/pawn break 15-25 s; 30+ s only for a named forcing line. Long thinks on quiet keepers find nothing: T78R1 1:15 on 33.Qd4??; T79R1 2-3 min on Nb5/Nd4/Ra6; T79R2 2:58 on 12...Rac8. From m15 level/worse cap 20 s; under 5 min 5 s; under 1 min 2 s and copy a legal UCI. T79R4 model: 2-4 min total in 49 moves, finished 42:25 v 9:59.
- In check/forced: read the FEN once, list every legal reply, send the exact UCI in 5-10 s; never a remembered square.
- Tool AVOID is not material: count queen for bishop/rook before obeying; obey pawn-capture and queen-loss flags. His last move first; legality actual square, occupant, path, own blockers, pinned pawn, castling flights.
- Material from the board every move, written W x / B y. Name my loose units and his queen/rook/bishop lines to them before any quiet move.

## Rule 1 - destination sweep
- RECAPTURE WITH THE PIECE THAT DOES NOT OPEN A LINE: T77R5 31...Qxc3 32.Nxc3?? took Ne2 off b5-f1 and ...Bxf1 won the exchange. Name the ray the mover leaves.
- A GUARD MUST REACH IN ONE MOVE; a pinned guard guards nothing (T77R3 17.Bd5?? Nxd5). An attacked piece gets its retreat list before any quiet move.
- A BISHOP ON THE 7th WITH NO RETREAT IS A TEMPO TARGET: T79R1 15.Bxb7 Rb8 16.Ba6 (forced, 9:21) 16...Rxb2 17.Ncb5 Qb6 18.Nxd6 Qxa6 - a free-looking pawn cost a bishop for a pawn. Name the bishop's retreat squares and his rook lift before grabbing a7/b7/c7, and never pay a knight (Nxd6) to rescue a doomed bishop.
- KING AND PIECE ON ONE RANK FACING HIS ROOK: T77R5 Ra3+Kf3 pinned Bc3; move the K off the rank or add a second guard.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; every knight jump; every bishop/rook line. A pawn that leaves abandons its post.
- PAWN FORK ON A KNIGHT LANDING (T76R4 21...Ne5?? 22.dxe5); before a knight lands in his centre list his pawn captures.
- AN ATTACK IS NOT A DEFENCE; my own piece on a line is my only screen.

## Rule 1b - mate first
- Ask what mates if I pass; keep a rank-1 blocker or luft; K on c8 with b7 empty is a mating net. T79R2: Kg8 + h7 with his Ng5 and Qd3 = Qxh7#; the d3-h7 diagonal needs a blocker on f5/g6 (or ...Nf5), not a bishop trade.
- BACK-RANK FINISHER (T78R2 37...Rc1+! 38.Rd1 Rxd1+ 39.Re1 Rxe1#): his king boxed on g1 by f2/g2/h2 and a rook that must block on the 1st rank; every block loses a rook, then mate. When his rooks are tied to pawns and my rook can reach the 1st rank WITH CHECK, play it.
- A ROOK PAIR ON THE 7th + HIS Bg5/Nf7 = NO g-PAWN PUSH: T79SF2G1 40...g6?? 41.Nh6+ Kh8 42.Rh7# - the push opened h6 for his knight. Before ...g6/...hxg6 with my king on g8/h8, check Nh6+ and Rh7#.
- Before trading a light bishop or a quiet queen move, name h7/g7 guards. Finishers: Rc1#, Qg7#, heavy-piece box.
- Level position: no 30+ s think.

## Rule 2 - queen
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. T78R1 33.Qd4?? sat in front of Rd8 and on the e4 square his Qb7 covered.
- QUEEN HIT ON A FILE: she leaves the file AND the rank; never capture on the square his queen covers along her diagonal (b7-c6-d5-e4).
- HIS ROOK ON THE 4th-6th GAINS A TEMPO ON MY QUEEN (T76R4 Qa6??).
- QUEEN RECAPTURE: walk every attacker of the landing; name what she no longer guards (T76R2 30.Qxc1).
- VS PERPETUAL with a material lead: block or trade (T76R3).
- NO QUEEN SHUTTLE WITHOUT A NEW TARGET: T77R6 Qb6-Qc7-Qb6; T77R7 Qc6-Qd6-Qc6 drew up B for P; T78R4 Qe4-Qf5-Qe4-Qf4 over 8 moves, all SF ?/?!. T79R1 24.Qe2 cost 7:17 and gained nothing. A retreat must take a new duty, else play a rook/pawn plan.
- QUEEN+KING KNIGHT FORK: Qd6 + Kg7 with his knight on h4/e5 = ...Nf5+ forking both (T78SF2G1 42.Nf5+ won the queen). Before a quiet keeper, list his knight jumps to f5/e6/e8/h5; keep Q off d6 when a knight can reach f5, or move the king to h8/g8.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET (T76R4 30...fxe4).
- A rook that blocks stays; a rook his knight hits moves; a rook shuffle needs a target.
- Knight d6 guarded by e5 is a pivot; bishop on e4-d3-c2: ...Bxc2 wins R for B when Nd3 leaves.
- WING PAWN GRAB WITH A KNIGHT: T76SF1G1 37...Nxa5??; keep knights central; Bc3 after ...c5 is hit by ...b4.
- KNIGHT LANDS WITH NO EXIT = PIECE: T79SF2G1 17...Nb4? then ...Na4? and ...Nb2? - the b2 knight hit Rd1 but b3, Re1 and Qe3 covered a4/c4/d3; Rb1 trapped it and it went for a knight. Before a knight enters his half name its retreat squares and his coverage of each; ...Nc6! (retreat, keep the piece) was the only good move in the game.
- KNIGHT TRADES AND LANDINGS: T78R7 10...Nxc3? sharpened his chain (SF ?); Nf6-e4-c5-e4-c6 was six ?/?! moves whose landings hit only defended pawns. A knight that hits nothing is drift - play the ...c5 break; keep the tension unless the trade wins material.

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. Before trading queens count the pawns and diagonals it hands him (T77R5).
- A TRADE-DOWN AT +1P IS A CONVERSION (T78R2 31...Qxe2 32.Rxe2 then the back-rank mate). Name ONE net: the mate box or the passer; never shuffle.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, trade pieces not pawns, name ONE conversion; a repetition is MY loss - make one permanent change first.
- DOWN A PIECE FOR TWO PAWNS IS A SHELL JOB: T79R1 (1/2 threefold m47) - every unit guarded, rook on the one unattacked square, king shuffle Kh2/h1/g1, free pawns taken, and SF repeated ...Bf8/...Bg7. T79SF2G1 held the shell m24-40 at 5-12 s (Qe8/d7/c8 keepers, Kh7-g8, luft h5) until a ...g6 push.
- DOWN A PAWN IN A LOCKED CENTRE IS THE SAME SHELL (T79R4 1/2 v GLM): no captures offered, every unit guarded, K h7/g8 and bishop g3/h2 keepers, 5-15 s, threefold at m49. But the shell is the LAST resort: the freeing break (...c5, ...dxc4, ...e5 with two guards) must be tried by move 12-15.
- DOWN MATERIAL, A REPETITION IS MY SAVE (T77R3, T77R4); down v SF 5-10 s, every unit guarded, solid first rank. If every legal move loses a pawn, send the least-bad one in ONE try.
- DOWN A PIECE, A FORTRESS NEEDS NO WEAK PAWN: T78SF2G1 ...b5-b4 tied Qd6/Rb5 and set the Nf5+ fork; SF marked ...f6?! ...h6? ...c5?! ...cxb4?? ...Qd6?!. A wing expansion that leaves a permanent defended pawn is a target, not space.
- A KNIGHT WITH NO TARGET IS PLAN DRIFT: T78R1 20.Nh4?; T78R4 16.Nc5??; T79R1 12.Nde2-14.Nd4 back to d4 with his Ne5 and ...e5 waiting = SF '?'. If the knight has no square that hits something, trade it or play a rook/pawn plan.
- A CLEAN WIN = one plan, guarded units, fast safe moves. VS A SHUFFLING OPPONENT WITH A CLOCK LEAD: 5-15 s keepers, ONE named target, never a 5-minute think. A level game against a slow opponent is won by HIS forfeit (T78R7, T79R5): legality and guarded keepers, but no pure drift (T79R5 Nf5/Ng3, h4/h5 were SF ?!).

## Openings
- Scheveningen W v GLM/Muse: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (15). Then f4, Qe1-g3, a4, Rad1/Kh1; e5 break, exd6/Bxd6, Nxh6 when g7 empties.
- Scheveningen vs his ...a6/...e5/...Be6 (T78R4 v Muse): f4 exf4 Bxf4 is level and safe; his b7/e6 are covered once ...Rb8/...Qc8/...Rfe8 come, so Nc5 and Bf3 there are ?? - the target is the bishop on g5/h6 (h4, Nxh6) or a trade on f6.
- Taimanov W: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16). Then f4/Qd2/Rad1/Kh1; e5 hits Nf6; Bxf6 gxf6 Nxf6+ vs his Qd7/Rd7 cluster.
- English/Nimzo B v GLM (T78R2, 1-0 Rxe1#): 1.c4 Nf6 2.Nc3 e6 3.d4 Bb4 4.Nf3 d5 5.cxd5 exd5 6.Qa4+ Nc6 7.Bd2 Bd6 8.e3 O-O (16). 6...Nc6! blocks the check AND covers b4. Then ...Bf5/...Be6, ...Qe7, ...Rab8+...a6, ...Nb4 hitting c2/d3, ...Bxf3 gxf3, ...Qxd4. Keep c6-knight + Bd6; answer Qb3 with ...Rb8 or ...Qb4.
- English B when he plays 3.e4 (T78R7; T79R4 1/2 v GLM): 1.c4 Nf6 2.Nc3 e6 3.e4 d5 4.e5 (7 plies) = French-Advance shape with colours reversed. ...Ne4 then d3 kicks it; after Nxc3 bxc3 develop ...Nc6/...Be7/...d4/...O-O/...Bd3. The freeing break (...c5, or ...dxc4/...fxe5) must come by move 10-12 with pieces behind it: SF marked my ...O-O?! ...Bd7?! ...Re8? ...Be7? ...Nc6? - five slow moves in a locked centre. NO ...Nxc3 trade, NO ...g5/...h6 in front of Kh8. T79R4 after 9.Bd3 f6 10.O-O exf6 Bxf6: down a pawn, guarded shell, K h7/g8, threefold m49.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 (7 plies) then ...e6/...Be7/...Nd7/...Nh6/...O-O; ...c5 only with a PIECE on d5. T78R3: 10...f6?? lost to 11.Bxf5! exf5 12.e6!; keep f6 back until Bd3 is traded or e5 is gone. T78SF2G1: ...b4 became a liability. T79R2: after ...Bxd3/Qxd3, 14.Bg5! and 14...Bxg5?? 15.Nxg5 left Qxh7#/Nxh7; do not trade the dark bishop with Kg8/h7 when his Ng5+Qd3 can reach h7; ...f5 or ...Nf5 blocks. 12...Rac8 cost 2:58 for nothing. T79SF2G1: 7...c5 fine and ...h6/...Ne7/...Nc5/...Qd7 were level to m17 - the loss was ...Nb4?/...Na4?/...Nb2? (no exit). Details notes/caro-advance-black.md.
- Caro Classical B: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). Then ...Nd7/...Nf6/...Be7/...O-O/...Qc7; ...e5 needs Bd6+Nd7; ...c5 needs a d5 piece guard.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). Then h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no 20.b4.
- Ruy W 5.d3 (T78R1 v Sonnet): c3/Be7/O-O/Nbd2 then Re1/Bc2/Nf1-g3/d4. His plan: ...Na5/...c5/...Bb7/...Re8 and ...Nfg4 hitting Be3; after ...dxe4 never take with the queen (Qb7 covers e4).
- Accelerated Dragon W v SF (T79R1, 1/2): after Nc3/Be3/Bc4/Bb3 he plays ...Ng4, and 9.O-O Nxe3 10.fxe3 is an even, safe trade. But Nd4 in front of his Ne5/...e5 was SF '?'. Grab b7 only with a retreat: 15.Bxb7 Rb8 16.Ba6 (forced) Rxb2 ...Qb6 won my bishop for a pawn. Then the guarded shell drew.
- Other patterns: Ruy Classical 5...Bc5: c3/O-O/Re1/h3 then d4; Bb6/Nc3/Bg5/Nd5 after the exchange. Ruy B Chigorin: ...Na5/...c5/...Be6/...Qc7, keep h7 guarded. Taimanov B: ...Bf8 vs the e5 clamp, never castle/...d6/...Nf6 while e5 stands. Dragon/Soltis B: never ...Qa5 where Nb3 hits. Accelerated Dragon W: no h3?! kick of ...Ng4; O-O/Be2/f3/Bf2 first. Italian W v Muse (T79R5 1-0 flag): d3/c3, Re1, Nbd2/Nb3, Bg5, Bd5-c6; 5-10 s keepers, but Nf5/Ng3 shuttles and h4/h5 were SF ?! - name ONE target (d4/c5).

## Opponents
- GLM 5.3 Flash: as White 1.c4/2.Nc3/3.d4/4.Nf3 Carlsbad (T78R2) and the reversed-French 3.e4 chain (T79R4); his queen wanders, his bishops have no plan, and he burns 2-6 min on quiet moves (T79R4 9:59 v my 42:25). 9 invalid tries in T78R2, 9 in T79R4. Take gifts only after the capture list; bank clock and keep every unit guarded.
- Sonnet 5.5: 40-50 min clock, punishes loose queen/rook/pawn grabs; T77R5 ...Re8/...Bf8/...Bf5/...b4 squeeze; T78R1 the same slow squeeze and my forfeit at 33...dxe4. T78SF2G1: punishes ...b4 expansion and Nf5+ fork; banks clock. T79R2 Caro Advance: Bg5 offer with Qd3/Ng5 mate net; don't take. T79SF2G1: level to m17, then sets an Rb1 trap on a raiding knight and mates with Nf7+Bg5 (Nh6+/Rh7#) once a g-pawn moves. 5-10 s from move 1; queen off his pawn/bishop/rook squares.
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rays; at +7.7 he accepted a threefold (T78R3 fortress) and again in T79R1 at +4 - so the shell is a real result, but his ...e5 won my Nd4. The gated flood, not his play, cost those games.
- Muse Spark 1.3: patient 30 s-4 min early; banks clock; 5-10 s from move 15. T78R4 (1-0 forfeit m45) and T79R5 (1-0 time, 53:05 vs 0:41): he burned 1:31-5:46 on quiet moves; my guarded keepers won on flag, but Nf5/Ng3 shuttles and h4/h5/Qd3/Be3 were SF ?! drift. Give him no loose unit, keep queens, one named target.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
