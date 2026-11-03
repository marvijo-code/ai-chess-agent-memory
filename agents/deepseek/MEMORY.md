# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B (T80R4)
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W incl. 5.d3 (T78R1, T80R3)
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W (T79R1 draw v SF)
- notes/sicilian-soltis-black.md - Soltis B
- tools: legal-list, clock-guard, material-clock, fork-alert, queen-rook-safety, repetition-guard, rep-material-watch, pinned-defender, knight-exit

## Rule 0 - board, legality, clock
- FORFEIT BEATS BLUNDER: 3 refused tries on ONE move end it. After ONE refusal change piece AND idea; if a tool flags my planned move, send the least-bad DIFFERENT legal move in ONE try. T80R4 33...Qe6: queen attacked, 3 gated tries cost 4:02 and the referee replayed best-so-far; list legal retreats once, send an unflagged one in 5 s. A flagged pawn is not a stop: accept the cheapest loss and send in one try (T80R3 51...Rb2). Under 10 min every move 3-5 s; never a think over 20 s.
- REREAD THE FEN, SEND A PLAINLY LEGAL UCI: T78R2 6 invalid; T78R4 41.Rf1/42.Rfe1; T78R7 13...Bf8 illegal; T80R3 16.Nb3, 24.Rad1, 26.Ng3, 37.N5d4, 38.e6, 40.Nexc6 each 2-3 tries; T80R4 17...N5f6 2 tries. A refused quiet keeper becomes a DIFFERENT quiet keeper in one try.
- Clock: routine 5-15 s; capture/check/pawn break 15-25 s; 30+ s only for a named forcing line. Long thinks on quiet keepers find nothing: T78R1 1:15 on 33.Qd4??; T79R1 2-3 min on Nb5/Nd4/Ra6; T79R2 2:58 on 12...Rac8; T79R7 8:51 on 29...Nf6; T80R2 2:05-4:32 on ...Ke7/...Ke5/...Rc5/...Rb3; T80R3 3:19/3:11/5:18/5:37/11:47 on Bc5/Nf5/e6/Nexc6/Kh2; T80R4 4:02 on 33...Qe6. From m15 level/worse cap 20 s; under 5 min 5 s; under 1 min 2 s and copy a legal UCI.
- In check/forced: read the FEN once, list every legal reply, send the exact UCI in 5-10 s; never a remembered square.
- Tool AVOID is not material: count queen for bishop/rook before obeying; obey pawn-capture and queen-loss flags. His last move first; legality actual square, occupant, path, own blockers, pinned pawn, castling flights.
- Material from the board every move, written W x / B y. Name my loose units and his queen/rook/bishop lines to them before any quiet move.

## Rule 1 - destination sweep
- RECAPTURE WITH THE PIECE THAT DOES NOT OPEN A LINE: T77R5 31...Qxc3 32.Nxc3?? took Ne2 off b5-f1 and ...Bxf1 won the exchange. Name the ray the mover leaves.
- A GUARD MUST REACH IN ONE MOVE; a pinned guard guards nothing (T77R3 17.Bd5?? Nxd5). An attacked piece gets its retreat list before any quiet move.
- A BISHOP ON THE 7th WITH NO RETREAT IS A TEMPO TARGET: T79R1 15.Bxb7 Rb8 16.Ba6 (forced, 9:21) 16...Rxb2 17.Ncb5 Qb6 18.Nxd6 Qxa6 - a free-looking pawn cost a bishop for a pawn. Name the bishop's retreat squares and his rook lift before grabbing a7/b7/c7.
- KING AND PIECE ON ONE RANK FACING HIS ROOK: T77R5 Ra3+Kf3 pinned Bc3; move the K off the rank or add a second guard.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included; every knight jump; every bishop/rook line. A pawn that leaves abandons its post.
- PAWN FORK ON A KNIGHT LANDING (T76R4 21...Ne5?? 22.dxe5); before a knight lands in his centre list his pawn captures.
- AN ATTACK IS NOT A DEFENCE; my own piece on a line is my only screen.

## Rule 1b - mate first
- Ask what mates if I pass; keep a rank-1 blocker or luft; K on c8 with b7 empty is a mating net. T79R2: Kg8 + h7 with his Ng5 and Qd3 = Qxh7#; the d3-h7 diagonal needs a blocker on f5/g6, not a bishop trade.
- BACK-RANK FINISHER (T78R2 37...Rc1+! 38.Rd1 Rxd1+ 39.Re1 Rxe1#): his king boxed on g1 and a rook that must block on the 1st rank. When his rooks are tied to pawns and my rook reaches the 1st rank WITH CHECK, play it.
- A ROOK PAIR ON THE 7th + HIS Bg5/Nf7 = NO g-PAWN PUSH: T79SF2G1 40...g6?? 41.Nh6+ Kh8 42.Rh7#.
- Before trading a light bishop or a quiet queen move, name h7/g7 guards. Finishers: Rc1#, Qg7#, heavy-piece box. Level position: no 30+ s think.

## Rule 2 - queen
- NEVER on an enemy pawn capture square, bishop diagonal, rook file or knight jump. T78R1 33.Qd4?? sat in front of Rd8 and on the e4 square his Qb7 covered.
- QUEEN HIT ON A FILE: she leaves the file AND the rank; never capture on the square his queen covers along her diagonal (b7-c6-d5-e4).
- HIS ROOK ON THE 4th-6th GAINS A TEMPO ON MY QUEEN (T76R4 Qa6??).
- QUEEN RECAPTURE: walk every attacker of the landing; name what she no longer guards (T76R2 30.Qxc1).
- VS PERPETUAL with a material lead: block or trade (T76R3).
- NO QUEEN SHUTTLE WITHOUT A NEW TARGET: T77R6 Qb6-Qc7-Qb6; T77R7 Qc6-Qd6-Qc6 drew up B for P; T78R4 Qe4-Qf5-Qe4-Qf4; T79R1 24.Qe2 cost 7:17. T80R4 up B for 2P I played Qb5-Qd5-Qb5 and drew threefold; a repetition while ahead is MY loss. A retreat must take a new duty or make one permanent change.
- QUEEN+KING KNIGHT FORK: Qd6 + Kg7 with his knight on h4/e5 = ...Nf5+ forking both (T78SF2G1 42.Nf5+ won the queen). Keep Q off d6 when a knight can reach f5.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach in one move and stay guarded; never rook for bishop/pawn.
- HIS PIECE ON MY PAWN'S CAPTURE SQUARE IS A TARGET (T76R4 30...fxe4).
- A rook that blocks stays; a rook his knight hits moves; a rook shuffle needs a target.
- Knight d6 guarded by e5 is a pivot; bishop on e4-d3-c2: ...Bxc2 wins R for B when Nd3 leaves.
- WING PAWN GRAB WITH A KNIGHT: T76SF1G1 37...Nxa5??; keep knights central; Bc3 after ...c5 is hit by ...b4.
- KNIGHT LANDS WITH NO EXIT = PIECE: T79SF2G1 17...Nb4? ...Na4? ...Nb2? - Rb1 trapped it. Before a knight enters his half name its retreat squares and his coverage of each.
- KNIGHT TRADES AND LANDINGS: T78R7 10...Nxc3? sharpened his chain; Nf6-e4-c5-e4-c6 was six ?/?! moves hitting only defended pawns. A knight that hits nothing is drift - play the ...c5 break.

## Rule 4 - material and conversion
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level/behind. Before trading queens count the pawns and diagonals it hands him (T77R5).
- A TRADE-DOWN AT +1P IS A CONVERSION (T78R2 31...Qxe2 32.Rxe2 then the back-rank mate). Name ONE net: the mate box or the passer; never shuffle.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, trade pieces not pawns, name ONE conversion; a repetition is MY loss - make one permanent change first. T80R4 v Muse: up B for 2P with Q+2R each, I played Qb5-Qd5-Qb5 and drew threefold; Stockfish marks ...Qb5?. Activate the extra bishop or play ...a6/...g6; no queen shuttle when ahead.
- DOWN A PIECE OR A PAWN IN A LOCKED CENTRE = THE SHELL: T79R1 (B for 2P, threefold m47) and T79R4 (P down, threefold m49) - every unit guarded, rook on the one unattacked square, K h7/g8, free pawns taken, 5-15 s, no captures offered. But the shell is the LAST resort: the freeing break (...c5, ...dxc4, ...e5 with two guards) must be tried by move 12-15.
- DOWN MATERIAL, A REPETITION IS MY SAVE (T77R3, T77R4); down v SF 5-10 s, every unit guarded, solid first rank. If every legal move loses a pawn, send the least-bad one in ONE try.
- DOWN A PIECE, A FORTRESS NEEDS NO WEAK PAWN: T78SF2G1 ...b5-b4 tied Qd6/Rb5 and set the Nf5+ fork; a wing expansion that leaves a permanent defended pawn is a target, not space.
- ROOK ENDING DOWN A PAWN (T80R3): the blockade (Rc1) is right, but name his rook's entry squares before settling - ...Rd2-...Rb2 won my loose b3 while my blockade rook could not defend it. Every pawn I keep must have a guard that is not the blockader; accept the one pawn and hold the rest.
- A KNIGHT WITH NO TARGET IS PLAN DRIFT: T78R1 20.Nh4?; T78R4 16.Nc5??; T79R1 12.Nde2-14.Nd4; T79R7 Nd5-b6-d7-d5-f6-e4, all ?/??; T80R3 26.Ng3?? 28.Rd3?? 29.a5?? 30.Ra1?? 37.N5d4?? with b4/b3 and c3/Qc2 frozen. In a frozen position pick ONE target (here e5/Nd6) or go straight to the ending - no rook/knight shuttles.
- A CLEAN WIN = one plan, guarded units, fast safe moves. VS A SHUFFLING OPPONENT WITH A CLOCK LEAD: 5-15 s keepers, ONE named target, never a 5-minute think. A level game against a slow opponent is won by HIS forfeit (T78R7, T79R5, T79R7, T80R2): legality and guarded keepers, but no pure drift.

## Openings
- Scheveningen W v GLM/Muse: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 (15). Then f4, Qe1-g3, a4, Rad1/Kh1; e5 break, exd6/Bxd6, Nxh6 when g7 empties.
- Scheveningen vs his ...a6/...e5/...Be6 (T78R4 v Muse): f4 exf4 Bxf4 is level and safe; Nc5 and Bf3 there are ?? once his rooks/queen come; the target is the bishop on g5/h6 (h4, Nxh6) or a trade on f6.
- Taimanov W: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16). Then f4/Qd2/Rad1/Kh1; e5 hits Nf6; Bxf6 gxf6 Nxf6+ vs his Qd7/Rd7 cluster.
- English/Nimzo B v GLM (T78R2, 1-0 Rxe1#): 1.c4 Nf6 2.Nc3 e6 3.d4 Bb4 4.Nf3 d5 5.cxd5 exd5 6.Qa4+ Nc6 7.Bd2 Bd6 8.e3 O-O (16). 6...Nc6! blocks the check AND covers b4. Then ...Bf5/...Be6, ...Qe7, ...Rab8+...a6, ...Nb4 hitting c2/d3, ...Bxf3 gxf3, ...Qxd4. Keep c6-knight + Bd6; answer Qb3 with ...Rb8 or ...Qb4.
- English B v 3.e4 (T78R7; T79R4 1/2; T80R2 0-1 forfeit): 1.c4 Nf6 2.Nc3 e6 3.e4 d5 4.e5 (7 plies) = reversed French. ...Ne4 then d3 kicks it; the ...Nxc3/bxc3 trade gives me ...c5/...Nc6/...Be7/...O-O, then ...f6 or ...Bd7/...Qc7. SF marks ...f6?!, ...Be4??, ...Bd5??; keep the bishop behind the c-pawn, no ...g6 while Bf6 can be taken. 5-15 s keepers, 2-4 min thinks are wasted.
- Caro Advance B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 (7 plies) then ...e6/...Be7/...Nd7/...Nh6/...O-O; ...c5 only with a PIECE on d5. T78R3: 10...f6?? lost to 11.Bxf5! exf5 12.e6!; keep f6 back until Bd3 is traded or e5 is gone. T79R2: after ...Bxd3/Qxd3, 14.Bg5! and 14...Bxg5?? 15.Nxg5 left Qxh7#/Nxh7; do not trade the dark bishop with Kg8/h7 when his Ng5+Qd3 can reach h7. Details notes/caro-advance-black.md.
- Caro Classical B: 1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16). Then ...Nd7/...Nf6/...Be7/...O-O/...Qc7; ...e5 needs Bd6+Nd7; ...c5 needs a d5 piece guard. T79R7 v Muse (0-1 time): a locked centre + my ...a6/...b5/...b4 storm opened nothing (SF ?!-??): play the freeing break or trade, not a wing storm; no 8-minute think on a keeper. T80R4 v Muse (1/2): level to m21; 21...Rcd8?? behind a blocked d-file and 22...e5?? opened the e-file for his Re1/Ne4; 23...Nf4?? Bxf4 exf4 gave him e4/g4. Keep e6 as a shield until ...c5 with pieces; don't play ...e5 while his Be3/Nf3 can take. His 28.Nxc5?? let ...Bxc5 win a knight; I then traded it for two pawns and repeated up B for 2P - convert, do not shuttle.
- Ruy W Closed Chigorin: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16). Then h3/Bc2 vs ...Na5, d4/Nbd2/Nf1-g3; keep Kg1 guarding f2 until queens off; no 20.b4.
- Ruy W 5.d3 (T78R1, T80R3 v Sonnet): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 d6 6.c3 Be7 7.O-O O-O 8.Nbd2 (15). Then Re1/Bc2/Nf1-g3/d4. His plan: ...Bd7 FIRST (Nc6 guarded) then ...b5, ...Bf8/...Re8, ...Nb4 trade, ...c5-c4-c3 clamp (Nd5+Qc7 guard c3), ...f5-f4; in the ending ...Rd2-...Rb2 on my b3. My e5 break, Ne4 and Nd6 outpost were SF '!'; the loss was 26.Ng3??/28.Rd3??/29.a5??/30.Ra1?? drift plus 3:32 v 41:06. Never take ...dxe4 with the queen (Qb7 covers e4). Details notes/ruy-lopez-white.md.
- Accelerated Dragon W v SF (T79R1, 1/2): after Nc3/Be3/Bc4/Bb3 he plays ...Ng4, and 9.O-O Nxe3 10.fxe3 is an even, safe trade. Nd4 in front of his Ne5/...e5 was SF '?'. Grab b7 only with a retreat (15.Bxb7 Rb8 16.Ba6 Rxb2 cost a bishop for a pawn).
- Other patterns: Ruy Classical 5...Bc5: c3/O-O/Re1/h3 then d4; Bb6/Nc3/Bg5/Nd5 after the exchange. Ruy B Chigorin: ...Na5/...c5/...Be6/...Qc7, keep h7 guarded. Taimanov B: ...Bf8 vs the e5 clamp, never castle/...d6/...Nf6 while e5 stands. Dragon/Soltis B: never ...Qa5 where Nb3 hits. Italian W v Muse (T79R5 1-0 flag): d3/c3, Re1, Nbd2/Nb3, Bg5, Bd5-c6; 5-10 s keepers, Nf5/Ng3 shuttles were SF ?! - name ONE target.

## Opponents
- GLM 5.3 Flash: as White 1.c4/2.Nc3/3.d4/4.Nf3 Carlsbad (T78R2), the reversed-French 3.e4 chain (T79R4) and T80R2 (forfeit m45: 5 invalid, his 5:40 v my 9:38); his queen wanders, his bishops have no plan, he burns 2-6 min on quiet moves. Take gifts only after the capture list; bank clock and keep every unit guarded.
- Sonnet 5.5: 40-50 min clock, punishes loose queen/rook/pawn grabs; T77R5 ...Re8/...Bf8/...Bf5/...b4 squeeze; T78R1 the same slow squeeze and my forfeit; T78SF2G1 punishes ...b4 expansion and Nf5+ fork; T79R2 Caro Advance: Bg5 offer with Qd3/Ng5 mate net; T79SF2G1 sets an Rb1 trap on a raiding knight and mates with Nf7+Bg5. T80R3 Ruy 5.d3: 40 min banked, no gifts, ...c4-c3 clamp, waits for drift, then wins the rook ending with ...Rd2-...Rb2 on a loose wing pawn. 5-10 s from move 1; queen off his pawn/bishop/rook squares; a frozen position goes to the ending, not to a shuttle.
- SF19: instant, zero errors; punishes loose units, passive retreats, queens on rays, knights with no exit and any plan drift in a locked centre. At +7.7 he accepted a threefold (T78R3 fortress) and again in T79R1 at +4 - the shell is a real result. The gated flood, not his play, cost those games.
- Muse Spark 1.3: patient 30 s-4 min early; banks clock; 5-10 s from move 15. T78R4 (1-0 forfeit m45), T79R5 (1-0 time, 53:05 v 0:41), T79R7 (0-1 time, 26:45 v 0:13) and T80R4 (1/2): he burns 1:31-5:46 on quiet moves all game and blunders material when pressed (T80R4 28.Nxc5?? lost a knight to ...Bxc5; 41.Nd2??/45.Nb3??). Give him no loose unit, take the gift, name ONE conversion, no queen shuttle; guarded keepers win on flag but Nf5/Ng3 shuttles and h4/h5/Qd3/Be3 were SF ?! drift.
- DeepSeek mirror, Fable 5.1, GPT-6.1 Sol, Astra: keep units guarded, bank clock, take every unguarded unit. Haiku 5.5: solid Italian Pianissimo, fast.
