# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance + Classical 3.Nc3 B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W (Classical + Chigorin)
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & clock
- 3 rejected replies on one move = forfeit. Walk piece, actual square, occupant, path, my own blockers. One rejection = different piece/idea. Castling: king/rook unmoved, f8/g8 empty, king not in check or through attacked square. T66R5.2 zero illegal; T66R2 illegal ...Kh8; T67R4.2 one illegal Qc7.
- His last move first, then my destination: 0 guards + his capture = gift. Quiets/retreats same sweep.
- CLOCK: routine 10-15 s, cap 30; up material 5-10; under 15 min 5-10; under 5 min 3-5; from move 20 never over 60. T66R5.2 up N+pawns wasted 2-5 min on quiet moves; T66R4.2 level board burned 47 min then queen. vs SF 10-15 routine, lost position 5-10. Long think never replaces destination list. T67R3 Caro Classical, level build: 4:51 on ...Nbd7, 2.5-3.5 min each on ...Qc7/...c5/...e5/...e4, ended 9:40 v 12:26 - structure/book moves are 5-15 s, the sweep is the spend.

## Rule 1 - destination sweep
- LIST HIS PAWN CAPTURES VS EVERY LANDING, KNIGHTS INCLUDED. White e5-pawn owns f6/d6; g4-pawn f5/h5. T61R1 25...Nd5?? e4; T66R2 16...Nf5?? gxf5; T62R2 14...Qd6?? exd6.
- MY OWN PIECE ON A LINE IS MY ONLY SCREEN; moving it exposes. T60R2 14.Bxa7?? ...Rxd2 won queen; T62R1 12.Bd4?? only unit between Rd8 and Qd2; T67R3 19...Bxe3?? moved my c5-bishop off the c-file, the only unit between his Qc3 and my Qc7 - 20.Qxc7 won my queen. Before moving a piece off a file/rank/diagonal, name what it screens (mine from HIS queen/rook).
- TWO LOOSE UNITS IN A ROW THROW A WON OPENING. Every developing move: list my undefended pieces and his queen/rook/bishop reaching them in one.
- HITTING HIS QUEEN IS NOT AN ANSWER WHEN IT OPENS A CHECK.
- A PAWN THAT LEAVES ABANDONS ITS POST. Caro: never ...f6 while king e8/uncastled and e6 has no PIECE guard. QGD c6 guards d5: ...c5 only when d5 has piece guard. Advance Caro b4/a4 need guards. Pinned pawn not a guard; own piece between heavy and destination is no shield.
- NEVER KNIGHT ON SQUARE HIS PIECE/PAWN COVERS: d5-knight retreats b4/e7/b6/c7, never f6 while e5 lives, never f5 while g4 lives. His undefended piece is free every move, but check mine first.
- DON'T KICK A DEFENDED CENTRAL KNIGHT WITH A PAWN. T67R3 17...e5?? attacked a defended Nd4, gave 18.Ndf5 with tempo on my e7-bishop and wrecked the queen's cover. Kick only when the knight must move and its retreat square is free.
- POSITIVE PAWN-TAKE: his Ne4, my d5-pawn and Nf6 alive: ...dxe4! dxe4 Nxe4 wins N+P for P when only d3 recaptures. T66R5.2.
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5; g4-pawn hits f5/h5. My piece on his pawn square lost; his on my pawn square free.
- KNIGHT/BISHOP LANDINGS: walk his queen/bishops' diagonals and every knight jump; central jump needs every recapturer. My pawn hitting two of his units = one saved.
- ROOKS/KNIGHTS only where guarded; rook check: can his king just take. Rook on 6th/7th: list a/b/c-pawn captures. The moving unit abandons its guard; name it. Attacked piece needs answer before any quiet move.
- A SUPPORTED PAWN BREAK e5 (f4 guarding) FORKS QUEEN AND KNIGHT: move knight or queen first. Passive retreat abandoning active piece loses tempo vs SF.

## Rule 1b - mate first
- Ask what mates if I pass. Blocking mate obeys sweep. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3 luft. Two rooks guarding each other f2+f3 stop ...Qh2/...Qg2.
- King g8 + Rf8 + g7 gone: Re8+ ...Rf8 block is Qg7# if his bishop covers g7/h8. Keep g7-pawn.
- Back rank: keep rank-1 blocker or luft. T61R1 38.Re8#; T61Final 30.Qa8+ Re8 31.Qxe8#; T66R3 29.Rxd7+ Kg8 30.Re8#. T67R2 36...Rb1+ 37.Rc1 Rxc1# with Kg1 and no h3. T67R3 60.Rg8# my Kg7 + rook on the g-file + no luft.
- KING-TAKES: unguarded piece beside his king (knight included) is a king capture.
- WON POSITION: forcing check beats slow lift; Q+R protected checks drive to edge; Q vs K knight's-move box, no stalemate. Models T62R2 Qb7/Qxd7, Rd8, Qf7+ Kh8 Bd4#; T62R3 Qh3/Ra1#; T62R4.2 Qe5 escort passer to h8=Q, Qbc7#.
- T66R5.2 finish: up N+pawns, king boxed a3/a2: Qc2 covers a2/a4/b2/b3, c5-pawn b4, ...Nb5#. Check stalemate before c1=Q; c1=R if needed.
- T67R4.2 finish: up Q+N vs R, king b1/a1: Qc3+ Qe1# with knight guarding c2. Keep queen active but avoid aimless checks; the mate net is standard.

## Rule 2 - queen
- QUEEN ON LONG DIAGONAL FACING HIS QUEEN/BISHOP IS GIFT. T66R4.2 31.Qf4?? Qxf4. Before any queen move walk both diagonals through her queen/bishops, then pawns. Attacking defended knight is not reason.
- TWO QUEENS FACING ON A FILE/RANK WITH MY PIECE BETWEEN: that piece is FROZEN - its 'trading' capture loses my queen (T67R3 ...Bc5-e3, Qxc7).
- HIT -> she moves that move, off every attacker ray. Bishop landing with tempo on her = she moves.
- QUEEN HIT BY ROOK ALONG FILE/RANK MUST LEAVE THAT FILE/RANK. T61R3 18...Qe4 under Re1; T62R1 12...Rd8 hit Qd2.
- EVEN A CHECK PASSES ROOK-LINE SWEEP: T66R3 26...Qg5+?? 27.Rxg5+.
- PAWN-SQUARE LEAK BOTH DIRECTIONS: GLM five times (Qd7?? cxd7; Qd5?? exd5; Qe6?? dxe6; Qd6?? exd6). Mine T62Final 21...Qb4?? cxb4; T67R2 ...Qxb2 was safe only because Rb8 backed it, but b2 grab still cost time. Before every queen move list enemy pawns ranks 3-6 and both forward capture squares, name recapturer.
- QUEEN NEVER ON ENEMY BISHOP DIAGONAL, KNIGHT JUMP SQUARE, OR PAWN CAPTURE SQUARE.
- QUEEN RECAPTURE: walk every enemy attacker of landing square. T62R4.2 20...Qxd6?? 22.Rxd6.
- UP A QUEEN: no queen move onto bishop diagonal/pawn square; force last rook trade or mate. Before queen move list what she defended and every enemy knight/pawn hitting destination. Blocked guard is not guard. Up a knight, queen trade on safe square good: T66R5.2 14...Qxd4, ...Bg6 kept Ne4 guarded; sweep first.
- T67R4.2: after ...Qb6 and ...c5, queen belongs b6/c7; Qb5??/Qb4?!/Qa5?! let c4/b4 hit her with tempo. Keep her on b6 or retreat to c7.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach destination in one move and stay guarded after landing.
- UNDEFENDED PIECE NOT FREE IF HIS ANSWER COMES WITH TEMPO. Never trade R for B/P. After capture that wins piece rescan my loose units; after any trade recount all guards. Up exchange with queens: no pawn grabs with rook, keep both rooks guarded, trade rooks on my terms. Trade when up only if resulting material clearly winning and every unit guarded. T66R5.2 traded queens/rooks up a knight, reached N+6p v 4p, converted.

## Rule 4 - material, conversion, clock
- MATERIAL FROM BOARD EVERY MOVE; rescan after every trade. No grabs when level/behind. Level material with broken king is lost vs SF.
- DOWN Q FOR R: 2N v R+pawns is NOT a fortress - his rook and king pick the knights one at a time (T67R3 Rxe3, Nxf5, Kxc5, mate m60). Keep knights guarded and off his king's/rook's approach squares; trade a knight for a pawn only to build a real passer.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, consolidate, keep units off his pawn squares. T61R2 hit loose units, passer with queen behind. T62R2 up queen forced rook trade and mated. T62R3 up exchange+2 took only free units, ran a-pawn with Ra7 behind. T62R4.2 up Q+B v B took a6/c6, ran passers, mated 52.Qbc7#. T66R3 up piece after e5/Bf3; 21.g4/24.Qd2 slow, 29.Rxd7+ 30.Re8# finished. T66R5.2 up knight: queen trade, ...Bg6, ...c5 kick, ...gxf6, Nd7 c5, king walk, ...Nb5#, but 20+ min wasted. T67R4.2 up Q+N vs R: queen wandering Qb5/Qb4/Qa5 wasted time; mate Qe1# still came.
- UP TWO ROOKS: ladder cut/check/tighten 5-10 s; T66R1 flagged after long thinks. UP A ROOK (2R v R, pawns level) is progress problem: T60R1 32...bxc6 then 20 shuffles = threefold draw. Extra rook to open file/7th, offer defended rook trade, drive his king. Progress test after every move.
- DOWN A PIECE VS SF IS LOST: no queen pawn-grabbing, guard every unit, hunt one freeing trade, keep king behind pawns. Down vs GLM not lost: hit undefended pieces. T62Final down queen to SF at m22 over in 12 moves; T66R2 down piece after 17.gxf5, rest 5-10 s defense.
- AFTER QUEEN TRADE RECOUNT: if recapture chain loses queen, don't start it. WON ENDING WITH PASSED C-PAWNS: knight guards c4/c5, king to b6, c-pawn advances when knight covers, promote with check; avoid stalemate.

## Openings
- Caro B: Advance 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies); then take d4, bishop c5/b6, knight e7, castle. T66R1 v Muse level; T66R4.2 as White in Advance: keep b4/a4 supported, no long h3/g4. T60F 10...Nf6?? exf6: e5-pawn owns f6. Never ...f6 while e6 has no PIECE guard; retreat bishop before f4-f5; never recapture ...Bxf5 on open f-file; ...hxg6 not ...Nxg6; ...Be4 loses Nxe4; open e-file no queen. T61Final 16.Ba3! hit Ne7 and ...fxe6?? lost queen. T62Final 17...Nc8?? passive knight +8.58; keep knight active/trade. T66R2 v SF: 9...c4?!, 12...Bf8 passive, 16...Nf5?? gxf5; clock.
- Caro Classical 3.Nc3 B (T67R3 v Muse lost m60; T67R4.2 v Muse won m47): normal build: trade on e4, develop Bf5. Meet h4-h5 with h6 and Bh7. Then play e6, Nf6, Be7, castle short. Later Nbd7, Qc7, c5. T67R3 errors: 17...e5?? kicked defended Nd4 (18.Ndf5 hit e7-bishop); 19...Bxe3?? cleared c-file between Qc3 and Qc7 (20.Qxc7 won queen). T67R4.2: build worked, but queen wandering Qb5/Qb4/Qa5 let c4/b4 hit her with tempo; keep her on b6/c7. Down Q for R, 2N v R+pawns is lost.
- English as Black (reversed QGD; W T59R5.2, T60R3; D T60R1; L T61R1; W T62R3; W T66R5.2): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies); then ...Bf5/...Nbd7/...Qb6/...Re8. ...c5 only when d5 has PIECE guard. BANS: no knight on e4-pawn's d5/f5, no queen d7/c6-pawn, ...Na4?? bxa4, ...Bxa4?? Rxa4, ...Bd6?? Nf5. T62R3 ...cxb5 removed c6 guard and ...Nfd7 removed Nf6 guard, Nxd5! free. Keep d5 guarded by c6 AND a piece. T66R5.2 v GLM: 12.Ne4?? dxe4! dxe4 Nxe4 won knight; 14...Qxd4 traded queens up; ...Bg6 kept e4 knight; f3 ...Bf6; ...c5 kicked Nd4; ...gxf6 kept Nd7 c5; king walk ...Nb5#. No 2-5 min quiet conversion.
- Ruy Lopez as White, Classical 5...Bc5: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15 plies). Build ...Be6, d4, exd4 cxd4, ...Bb6, Nc3; Bg5 h6 Bxf6 Qxf6; Nd5 Qe6, Nxb6 cxb6, d5! forks Qe6/Nc6. T61S2G1 16...Ne5?? 17.dxe6 won queen. T62R2 12.e5 Nd5 13.Nxd5 exd5 14.Bf3 hit d5/Nc6 and 14...Qd6?? on my e5-pawn. Keep 5-15 s. Chigorin 5...Be7: bishop b3, d6, castle, Na5/Bc2; keep c1-rook, Be3 not Bd2; no piece on g6-pawn square.
- Italian Giuoco Pianissimo W: Nc6, Bc5, Nf6, d6, O-O, Be6, h6 are the setup. Then Qd7, Re8, d5. If ...Bg4, Re1 and h3. T60S2G1 16.Ba4! Qxa4?? 17.Qxa4. Bans: 10.d4?!, queen d5 while f6-knight lives.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4, Qd2, Rad1, Kh1. e5 hits Nf6; after ...Nd5 Nxd5 exd5 Bf3! hits d5/Nc6. T66R3 v GLM: 12.e5 Nd5 13.Nxd5 exd5 14.Bf3! Bxd5/Bxd4 won piece; 19.Bxf6 Bxf6 20.Qxd5+ then trade rooks. BUT e5 only when e5-pawn DEFENDED after fxe5: T62R4.2 12.e5?! dxe5 13.fxe5 Nxe5. BANS: 12.Qd2?? after ...Bc5, 15.Nd5??, 26.Rxa6??, 27.Qf4??.
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies); then Qg4. With king e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with PIECE (...Bf8). T50R3 11...g6?? 15.Qf6 won h8.
- Dragon/Yugoslav W: Yugoslav build (Be3, f3, Qd2, O-O-O, Bc4/Bb3) vs SF is LOSING. Prefer Be2/Be3/f4 Taimanov or 5.c4 Maroczy; if Yugoslav is on, move queen off rook files, no capture while she is hit.
- Maroczy Bind W v SF: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5 7.Nb3 Qd8 8.Be3 (15 plies), then develop Be2, castle, ...d6, Qd2. T67R2 vs SF: 11...Ng4!; 12.Bxg4 Bxg4; 13.Nd5 f5 14.exf5?! Bxf5 gave Black activity (3:54 think). Keep bind; b2 is target after ...Qb7/...Rb8 - play Rab1/Qc3/h3 before Rfe1. 29.Bb6?? axb6 lost bishop. 34.Rc4?? dxc4 hung rook to d5-pawn. 36...Rb1+ 37.Rc1 Rxc1# with no h3. LESSON: in Maroczy never put a rook on c4/d4/e4 where a d/e/f-pawn captures; h3 before queen trade; don't trade Bxg4 if it leaves his bishop on g4 active and e4 weak.

## Opponents
- SF19: instant, zero errors. Punishes loose units, passive retreats, queens on rays/pawn diagonals/knight squares, voluntary pawn loosening, ignored attacked piece. T62Final 17...Nc8?? +8.58. T66R2 12...Bf8/16...Nf5?? gxf5; flagged after long defense. Give no pawn break, no loose unit, no piece on e5-pawn f6/d6 or g4-pawn f5/h5, no piece on open file in front of king; 10-15 s. T67R2 Maroczy: ...Ng4!, ...f5, ...Qb7/...Qxb2, ...Rb1#; keep luft and never a rook on a pawn's capture square.
- Muse Spark 1.3 (T66R1 D as Black; T66R4.2 L as White; T67R3 L as Black; T67R4.2 W as Black): patient 30-90 s, ZERO illegal, banks clock. Takes every loose pawn/undefended piece and converts queen-up cleanly. Caro Advance waits ...Bf5/...Nd7/...Ne7/...Bg6/...Nf5 then hits b4/a4/h3. T67R3: took my queen the moment the c-file cleared (20.Qxc7), gave her back for my a8-rook, then won R+K v 2N with mate - no screen between two queens, no gifts once she is ahead. T67R4.2: played h4-h5 shell, then shuffled; missed that Qxa8 was a blunder (Qb4+ Qxc4). Do not gift b4/a4/h3 or queen on her diagonal; do not spend 5+ min quiet while she banks time.
- GLM 5.3 Flash (18 wins; T66R5.2 W as Black): as Black v 1.e4 Ruy Classical 5...Bc5 and Taimanov; as White English/reversed QGD. Leaks: HIS QUEEN ON MY PAWN'S CAPTURE SQUARE (five times), ON MY ROOK'S RANK (T66R3 26...Qg5+?? 27.Rxg5+), and CENTRAL KNIGHT ON e4 EN PRISE TO ...dxe4 (T66R5.2 12.Ne4?? dxe4!). Also leaves bishops/rooks undefended. 1-3 illegal tries, up to 5 min. Take every gift only AFTER pawn/bishop capture list, then convert 5-15 s.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded, punishes piece/queen on his pawn's capture square. T62R3 and T62R4.2 I won by taking loose units after its quiet reroutes; it hangs a queen when a recapture lands on a file an enemy rook controls. Convert with named plan, 5-10 s once ahead.
- Fable 5.1, Sonnet 5.5, GPT-6.1 Sol, Astra: take every unguarded unit, punish loose queen/rook, no gifts; keep every unit guarded and bank clock. Haiku 5.5: solid Italian Pianissimo, fast; I forfeited and lost twice on clock there - 10-15 s, bank time, check legality twice.
