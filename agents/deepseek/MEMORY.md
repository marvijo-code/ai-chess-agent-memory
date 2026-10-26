# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W (Classical + Chigorin)
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & clock (CLOCK IS #1)
- 3 rejected replies on ONE move = forfeit. Walk MY OWN pieces' paths FIRST: piece, ACTUAL square, occupant, destination, path. ONE rejection = redraw a DIFFERENT piece/idea, never resend. CASTLING: king/rook unmoved, f8/g8 empty, king not in check and not passing through an attacked square. T66R1 one illegal try (a rook check); T62R1 5 tries, T62R4.2 3, T62Final 4.
- His last move first, then MY destination: 0 guards + his capture = gift. Quiet, retreat and tempo moves get the same sweep.
- CLOCK: routine 10-15 s, cap 30; UP MATERIAL 5-10 s; under 15 min 5-10 s; under 5 min 3-5 s; from move 20 never over 60 s. T66R1: UP 2R+B v K+P I FLAGGED - 5:44 on 15...cxd4, 4:50 on 23...Qc7, 3:15 on 25...Qc7, 2:36 on 50...f5 in a won position; a two-rook mate is a 5 s/move ladder, not a think. Every flag was a clock game; T62R1's loss was a QUEEN HANG, not the clock.

## Rule 1 - destination sweep
- LIST HIS PAWNS' CAPTURE SQUARES AGAINST EVERY PIECE LANDING, KNIGHTS INCLUDED: T61R1 25...Nd5?? his e4-PAWN took it; T61R2 15.Nxc7?? his b6-BISHOP guards c7. A FORK ON A SQUARE ANY ENEMY PAWN/BISHOP/ROOK GUARDS IS A GIFT.
- WITH WHITE's e5-PAWN ALIVE, f6 AND d6 ARE ITS CAPTURE SQUARES FOR EVERY PIECE, KNIGHTS INCLUDED. Before ANY knight move list every enemy pawn on ranks 3-6 and BOTH its forward capture squares. T62R2 mirror: GLM's 14...Qd6 stood on my e5-pawn's square - exd6 won her.
- MY OWN PIECE ON A LINE IS MY ONLY SCREEN - moving it exposes whatever it hid. T60R2 14.Bxa7?? unplugged the d-file, ...Rxd2 won my QUEEN. T62R1 12.Bd4?? was the only unit between his Rd8 and my Qd2.
- TWO LOOSE UNITS IN A ROW THROW A WON OPENING: T60R3 15...Bxe4 left Nd7 loose, 16...Bc6?? left Be7 loose. Every developing move: list MY undefended pieces and his queen/rook/bishop that reach them in ONE move.
- HITTING HIS QUEEN IS NOT AN ANSWER WHEN IT OPENS A CHECK.
- A PAWN THAT LEAVES ABANDONS ITS POST. In the Caro never ...f6 while my king is on e8/uncastled and e6 has no PIECE guard. In reversed QGD the c6-pawn guards d5: ...c5 only when d5 has a PIECE guard.
- A PINNED PAWN IS NOT A GUARD; MY OWN piece between his heavy piece and my destination is no shield.
- NEVER A KNIGHT ON A SQUARE HIS PIECE OR PAWN COVERS: a d5-knight retreats to b4/e7/b6/c7, never f6 while his e5-pawn lives. HIS UNDEFENDED PIECE IS FREE EVERY MOVE - but check MINE first.
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5, d5<-c4/e4.
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and EVERY knight jump; a central jump needs EVERY recapturer. MY PAWN HITTING TWO OF HIS UNITS = ONLY ONE CAN BE SAVED.
- Rooks and knights only where GUARDED; before a ROOK CHECK ask can his king just take. The recapturer must ACTUALLY REACH it. A ROOK ON THE 6th/7th: list his a/b/c-pawn captures.
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY OTHER MOVE.
- A SUPPORTED PAWN BREAK e5 (f4 guarding) FORKS QUEEN AND KNIGHT: move the knight or queen first.

## Rule 1b - mate first
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3 is luft. TWO ROOKS GUARDING EACH OTHER on f2+f3 stop ...Qh2+/...Qg2+ nets.
- King g8 + rook f8 + g7 GONE: his Re8+ ...Rf8 block is Qg7# if his bishop covers g7/h8. Keep the g7-pawn.
- Back rank: keep a rank-1 blocker or luft. T61R1 38.Re8#; T61Final 30.Qa8+ Re8 31.Qxe8#.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture.
- WON POSITION: the forcing check beats a slow lift; Q+R: protected checks drive to the edge; Q vs K: knight's-move box, no stalemate. T62R2 model: Qb7 and Qxd7 won pawns with the queen safe, Rd8 forced the last rook trade, then Qf7+ Kh8 Bd4#. T62R3: Qh3 covers h1/h2/g2, Ra1#. T62R4.2: Qe5 seals the e-file, escort a passer to h8=Q, then Qbc7#.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. A BISHOP LANDING WITH TEMPO ON HER = she moves.
- A QUEEN HIT BY A ROOK ALONG A FILE/RANK MUST LEAVE THAT FILE/RANK: T61R3 18...Qe4 stayed under Re1; T62R1 12...Rd8 hit Qd2 - the answer was Q off the file, never 13.Bxg7.
- THE PAWN-SQUARE LEAK, BOTH DIRECTIONS: GLM five times (29...Qd7?? cxd7; 31...Qd5?? exd5; 16...Qe6?? dxe6; T62R2 14...Qd6?? exd6). MY OWN: T62Final 21...Qb4?? cxb4. Before EVERY queen move, quiet ones included, LIST every enemy pawn on ranks 3-6 and BOTH its forward capture squares, and name who recaptures.
- QUEEN NEVER ON AN ENEMY BISHOP'S DIAGONAL, KNIGHT JUMP SQUARE, OR PAWN'S CAPTURE SQUARE.
- QUEEN RECAPTURE: walk EVERY enemy attacker of the landing square. T62R4.2 mirror: 20...Qxd6 recaptured onto the open d-file and 22.Rxd6 took her.
- UP A QUEEN: no queen move onto any bishop diagonal or pawn square; force his last rook trade or mate - no grabs.
- BEFORE every queen move list what she defended where she stood AND every enemy knight/pawn hitting the destination. A BLOCKED GUARD IS NOT A GUARD.

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing.
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P.
- AFTER a capture that wins a piece rescan for MY loose units; after ANY trade re-count ALL my guards.
- UP THE EXCHANGE WITH QUEENS ON: no pawn-grabs with a rook, keep both rooks guarded, trade rooks on my terms.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE; rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND.
- LEVEL MATERIAL WITH A BROKEN KING IS LOST vs SF.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s a move, CONSOLIDATE, keep every unit off his pawn squares. T61R2: hit loose units, pushed the passer with the queen behind it. T62R2: up a queen, forced the rook trade and mated. T62R3: up exchange+2, took only FREE units, ran the a-pawn with Ra7 BEHIND it. T62R4.2: up Q+B v B, took a6/c6, ran two passers, mated 52.Qbc7#.
- UP TWO ROOKS: the ladder (cut, check, tighten) is a 5-10 s routine; T66R1 2R+B v K+P flagged after long thinks on a won board (draw, insufficient material).
- UP A ROOK (2R v R, pawns level) IS A PROGRESS PROBLEM: T60R1 32...bxc6 then 20 shuffles = THREEFOLD DRAW. Plan: extra rook to an OPEN file/7th, offer a defended rook trade, drive his king. PROGRESS TEST after every move.
- DOWN A PIECE VS SF IS LOST: no pawn-grabbing with the queen, guard every unit, hunt ONE freeing trade, KEEP THE KING BEHIND PAWNS. DOWN VS GLM IS NOT LOST: keep hitting his undefended pieces. T62Final: down a queen to SF at m22, over in 12 moves - the lesson is the blunder.
- AFTER A QUEEN TRADE, RECOUNT: if the recapture chain loses the queen, don't start it.

## Openings
- Caro B: 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies); then take on d4, bishop c5/b6, knight e7, castle. T66R1 v Muse: after ...Nd7/...Bxd3/...e6/...Ngf6/...Be7/...O-O the ...c5 break with ...Qb6/...Qb4 was LEVEL - the failure was my clock. T60F: after 10.Na4, 10...Nf6?? lost the game (11.exf6) - the e5-pawn owns f6. Never ...f6 while e6 has no PIECE guard; retreat the bishop before f4-f5; never recapture ...Bxf5 on the open f-file; recapture ...hxg6, never ...Nxg6; ...Be4 loses to Nxe4; with the e-file open never put the queen on it. T61Final: 16.Ba3! hit my e7-KNIGHT and 16...fxe6?? lost my QUEEN. T62Final: 17...Nc8?? dropped +0.13 to +8.58 - keep a stalled knight active or trade it.
- English as Black (reversed QGD; W T59R5.2, T60R3; D T60R1; L T61R1; W T62R3): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies); then bishop f5, knight bd7, queen b6 or c7, rook fc8. ...c5 ONLY when d5 has a PIECE guard. BANS: no knight on his e4-pawn's d5/f5, no queen on d7 (his c6-pawn) or any pawn square, ...Na4?? bxa4, ...Bxa4?? Rxa4, ...Bd6?? onto Nf5's jump. T62R3: ...cxb5 removed the c6-pawn from d5's guard, then ...Nfd7?! removed Nf6's guard of d5, so Nxd5! won the pawn free. KEEP d5 guarded by c6 AND a piece.
- Ruy Lopez as White, Classical 5...Bc5 (T61R2, T61S2G1, T62R2 - all WINS v GLM by mate): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15 plies). Build: his Be6, then d4; after exd4 cxd4 play ...Bb6; Nc3; then Bg5 h6 and Bxf6; Nd5 and ...Qe6, then Nxb6 cxb6, and now d5! forks his Qe6 and Nc6 so one falls (T61S2G1 16...Ne5?? 17.dxe6 won the QUEEN). T62R2: 12.e5 Nd5 13.Nxd5 exd5, then 14.Bf3 hit the undefended d5-pawn and Nc6, and 14...Qd6?? walked her onto my e5-pawn. Keep 5-15 s. Chigorin 5...Be7: same build with bishop b3, pawn d6, castle, then knight a5/bishop c2; keep the c1-rook, play Be3 (never Bd2 - it blocks Qd1's d4 recapture), no piece on a square his g6-pawn covers.
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then queen d7, rook fe8, pawn d5. If ...Bg4, Re1 and h3. T60S2G1 WIN v GLM: 16.Ba4! Qxa4?? 17.Qxa4!. BANS: 10.d4?!, queen on d5 while his f6-knight lives.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4, Qd2, Rad1, Kh1. Then e5 hits Nf6; after ...Nd5 Nxd5 exd5 Bf3! hits the undefended d5-pawn and Nc6. BUT e5 only when the e5-pawn is DEFENDED after fxe5: T62R4.2 12.e5?! dxe5 13.fxe5 Nxe5. BANS: 12.Qd2?? after ...Bc5, 15.Nd5??, 26.Rxa6??, 27.Qf4??.
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (15 plies); then queen g4. With my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8). T50R3: 11...g6?? 15.Qf6 won h8.
- Dragon / Yugoslav as White (3 losses to SF): the Yugoslav build (Be3, f3, Qd2, long castling, bishop c4/b3) vs SF is a LOSING line. Prefer the Be2/Be3/f4 Taimanov build or 5.c4 Maroczy; if the Yugoslav is on, move the queen off any file a rook can enter, and never a capture while she is hit.

## Opponents
- Muse Spark 1.3 (T66R1 D as Black): Caro/English solidity, 30-90 s quiet moves, zero illegal; one blunder (...Re4?? let me take her queen) then defended a lost 2R v K board for 40 moves. Take the gift, then finish FAST: a winning board still needs a mating plan and a disciplined clock.
- SF19: instant, zero errors. Punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares, every voluntary pawn loosening, and an ignored attacked piece. T62Final: after my 17...Nc8?? his eval leapt to +8.58 in one move. Give him no pawn break, no loose unit, no piece on his e5-pawn's f6/d6, no piece on an open file in front of my king; 10-15 s.
- GLM 5.3 Flash (16 wins): as Black v 1.e4 the Ruy Classical 5...Bc5 and the Taimanov, as White the English/reversed QGD. Leak: HIS QUEEN ON MY PAWN'S CAPTURE SQUARE (five times). Also leaves bishops/rooks undefended. 1-5 illegal tries, up to 5 min on one move. Take every gift only AFTER the pawn/bishop capture list, then convert, 5-15 s.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded, punishes a piece or queen on his pawn's capture square. T62R3 and T62R4.2: I won by taking loose units after its quiet reroutes; it hangs a queen when a recapture lands on a file an enemy rook controls. CONVERT with a named plan, 5-10 s once ahead.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery; converts the moment I leave a piece on a pawn's capture square.
- Sonnet 5.5, GPT-6.1 Sol, Astra: take every unguarded unit, punish a loose queen or rook, no gifts; keep every unit guarded and bank clock.
- Haiku 5.5: solid Italian Pianissimo, fast; I forfeited and lost twice on the clock there - 10-15 s, bank time, check legality twice.
