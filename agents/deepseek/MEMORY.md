# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & clock (CLOCK IS #1)
- 3 rejected replies on ONE move = forfeit. Walk MY OWN pieces' paths FIRST: piece, ACTUAL square, occupant, destination, path, off board. ONE rejection = redraw a DIFFERENT piece/idea, never resend. T59: one illegal try on 20...Nd4 (Kxe7 from g8); T58: 6 illegal tries burned ~6 min.
- His last move first, then MY destination: 0 guards + his capture = gift. Quiet, retreat and tempo moves get the same sweep.
- CLOCK: routine 10-15 s, cap 30; UP MATERIAL 5-10 s; under 15 min 5-10 s; under 5 min 3-5 s; under 2 min 1-3 s. From move 20 never over 60 s. T59: burned 5-9 min on 9...Nbd7, 20...Nd4, 23...Ne2+, 24...Rd8, 25...d2 (9:31), 26...Ng4 (5:14), 27...Nxf2+ (5:18), then flagged after making a queen with 32...d1=Q+. T58S2G1 flagged +B+2P with 2:48; T58R5.2: 2 illegal in a routine mate.

## Rule 1 - destination sweep
- A CAPTURE LANDS WHERE MY OTHER PIECE ALREADY STANDS: T58 12...Nxe5?? his Bf4 took the knight. Before ANY capture name every guard of the landing square on the resulting board, HIS pieces included.
- HITTING HIS QUEEN IS NOT AN ANSWER WHEN IT OPENS A CHECK (T55 Final 15...Be7 16.Bg6+!). Before a tempo hit list HIS checks on the NEW board.
- OPEN FILE WITH HIS ROOK BEHIND IS DEATH: T56R3 14...exf5 15.gxf5 Bxf5 16.Rxf5; T58 6.Nd5?? Nxd5 7.Bxd5 Qxd5!.
- A PAWN THAT LEAVES ABANDONS ITS POST. In the Caro never ...f6 while my king is on e8/uncastled and e6 has no PIECE guard (T56R5 11...f6?!). In reversed QGD the c6-pawn guards d5: ...c5 only when d5 has a PIECE guard (T57R5.2 11...c5?! 12.Nxd5!).
- A PINNED PAWN IS NOT A GUARD; MY OWN piece between his heavy piece and my destination is no shield.
- HIS UNGUARDED BISHOP ON AN OPEN LINE FALLS; HIS QUEEN ON A PAWN'S CAPTURE SQUARE IS FREE. A knight landing hitting a loose piece is answered first; a pawn kick is not an answer. Before ...Ng4/...Nf5/...Nd4/...Nc4 list the guards of EVERY piece it hits.
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, a3/c3<-b4, e5<-d4/f4, f5<-e6/g6, f6<-e5, g5<-f4/h4. A moved pawn still attacks; its NEXT PUSH hits too. A black e4-pawn hits d3/f3; d4 hits c3/e3. T58R5.2: 13...exf3! won a knight. T57R5.2 19...Na4?? bxa4; 22...Bxa4?? Rxa4.
- A PAWN THAT JUST CAPTURED OWNS ITS NEW SQUARES: T56 15...dxc6 made c6 hit d5 AND b5; 16.Bd4?? ...cxd5 won the other bishop.
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and EVERY knight jump; a central jump needs EVERY recapturer. A FORK IS ONLY A FORK IF THE LANDING IS SAFE AND ITS TARGETS CANNOT STEP WITH TEMPO. HIS KNIGHT ON A SQUARE WHOSE RECAPTURE HIS OWN PAWN BLOCKS IS FREE.
- WHITE'S e5 PAWN OWNS d6 AND f6 - no-go for every piece, QUEEN included. An attacked d5-knight retreats to b4/e7/b6/c7, NEVER f6 (T59 11...Nf6??).
- Rooks and knights only where GUARDED; walk pawn recaptures; before a ROOK CHECK ask can his king take. The recapturer must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH. A ROOK ON THE 6th/7th RANK: list his a/b/c-pawn captures (T56 37.Ra6?? bxa6).
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY OTHER MOVE. Trading off my king's rank-2 rook: name g2/h2's guards on the NEW board.
- A TEMPO HIT BY A BISHOP/ROOK: list his checks and the pawn-covered squares beside my king. T59 Kh3 + h4-pawn: 44.Bd7?? allowed Rxc3+! 45.bxc3 Qg3# (h4 guards g3).
- A SUPPORTED PAWN BREAK e5 (f4 guarding) FORKS QUEEN AND KNIGHT: move the knight or queen before the break. T59 21.e5 forked Qd6+Nf6; 20...Qe7 or ...Nfd7 first.

## Rule 1b - mate first (after EVERY his move, quiet ones too)
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3 is luft - play the luft EARLY. TWO ROOKS GUARDING EACH OTHER on f2+f3 stop ...Qh2+/...Qg2+ nets.
- T58: 8.Qb3?? let ...Qxh1; 9.Kf1?? Bh3+ 10.Ke1 Qxg1#. Walk HIS queen's diagonals before a queen move; list checks/corner captures before a king step.
- f6 WITH MY KING ON e8 IS A HOLE: T55 Final 12...f6?? 13.Nxd5! cxd5 14.exf6. f6 only when g7 AND h8 are PIECE-covered and his queen is off g5/f4. Qg4+Bh6 vs short castled king: ...f5, ...Qf6 or trade queens.
- King g8 + rook f8 + g7 GONE: his Re8+ ...Rf8 block is Qg7# if his bishop covers g7/h8 (T57R1). Keep the g7-pawn or forbid that bishop.
- Back rank: keep a rank-1 blocker or luft; a rook that is the LAST guard of an entry square must not leave for a pawn. g3 with my king on g2 and his Be5 = pinned hook for ...h5-h4.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. Before ANY check write what captures the checker, KING included; QUEEN CHECKS: list EVERY block.
- WON POSITION: prefer the forcing check over a slow lift. Q+N+R: Ra8/Ne5/Qg6#. Q+B: Qc1+/Qd2+/Qd1#. Q+R: protected checks drive to edge, Qc2/Qd1. Q vs K: knight's-move box, king up, no stalemate.
- BISHOP PINNED ON g1 + K h1: ...Rc1+ freezes it; his f3+h3 pawns then threaten ...hxg2# (T58S2G1). A frozen bishop is not material. Stop collecting; remove the f3 guard (Rxf3+) or give material to open h2/g2.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. A BISHOP LANDING WITH TEMPO ON HER = she moves.
- QUEEN NEVER ON AN ENEMY BISHOP'S DIAGONAL, KNIGHT JUMP SQUARE, OR PAWN'S CAPTURE SQUARE: T56R5 25...Qc5?? d4-pawn = 26.dxc5. In the Caro c5 is the d4-pawn's square. T59 19...Qf5?? hung to Nh4 (h4-f5); 20.Nxf5 won her.
- A QUEEN THAT IS THE ONLY GUARD OF A BISHOP'S RAY TO MY ROOK: T59 14...Ba6 aimed a6-f1; 15.Qd2?? moved her off e2, ...Bxf1 won the exchange. Before ANY queen move list what she guards on every diagonal/file to my rooks (f1/f2/e2/d1).
- UP A QUEEN: NO queen move onto ANY bishop diagonal or pawn square (T56 32.Qd7?? Bxd7 returned her). Force his last rook trade or mate - no grabs.
- BEFORE every queen move list what she defended where she stood AND every enemy knight/pawn hitting the destination. A BLOCKED GUARD IS NOT A GUARD. Write the ATTACKER'S ACTUAL SQUARE: T58 8.Qb3?? ignored Qd5-h1.
- DOWN = no grabs; HIS QUEEN IN MY CAMP: list every unguarded piece she reaches next move; a queen hit by a rook must leave BOTH the file AND the rank.
- HIS QUEEN GRABBING A PAWN WITH TEMPO IS STILL TRADABLE: if my queen recaptures safely, take it (T57R2 ...Qxd3?? 23.Qxd3).
- A QUEEN CAPTURE ON A SQUARE GUARDED BY A ROOK ON THE SAME FILE IS LOST: T59 22...Qxd3?? 23.Rxd3 won her (d3 guarded by Rd1 AND Qc3). List EVERY guard of the landing square, including rooks/queens on the same file/rank.
- QUEEN PAWN-GRABS OPEN HIS ROOK LINES: T59 my Qxb2/Qxc3 won pawn+knight but his rooks reached b7/e7/a7 and his bishop reached d6/f8. Before a queen grab count his rook files and bishop rays, not just the pawn.

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing. ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE PIECE: count EVERY recapturer, PAWNS FIRST, trace the chain to the end (T56 16.Bxd6! Qxd6?? 17.Qxd6; T57R3 16.Bxc5! won her).
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P. A ROOK THAT GRABS IN HIS CAMP MUST BE DEFENDED.
- AFTER a capture that wins a piece rescan for MY loose units; after ANY trade re-count ALL my guards.
- UP THE EXCHANGE WITH QUEENS ON: no pawn-grabs with a rook, keep both rooks guarded, trade rooks on my own terms, then bank. PIECE FOR TWO PAWNS can be right when it removes his active bishop and leaves his queen loose (T57R2 14...d5!).
- T58: 6.Nd5?? was not a winning fork - after ...Nxd5 my only guard Bg2 recaptured and his queen recaptured the bishop. A jump supported by ONE piece is a trade only if the chain ends with me not losing material.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE; rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND. KEEP THE WON QUEEN off his rook's rank/file, off every bishop diagonal and pawn capture square to mate.
- LEVEL MATERIAL WITH A BROKEN KING IS LOST vs SF: count my king's guards and pinned pawns too.
- UP A QUEEN + ROOK vs R+B: trade his last rook first, then mate with Q+R (T56 32.Qd7?? lost exactly there). BIG LEAD = SIMPLIFY FAST; a clearance pawn move can open my bishop to his rook (T56R4 ...d3! Bxa1).
- UP MATERIAL IS A CLOCK PROBLEM TOO (T57 +N+P flagged; T58S2G1 +B+2P flagged with 2:48 left after 26.Bf2 12:16; T59 +Q after 32...d1=Q+ flagged): simplify, play the first sound move, under 5 min 3-5 s; once queens are off cap 10 s. The win is the safe trade, not the perfect placement. Once ahead, 5-10 s and checks/mate.
- DOWN A PIECE VS SF IS LOST: no pawn-grabbing with the queen, guard every unit, hunt ONE freeing trade, 5-10 s a move. T59: down the exchange after 15.Qd2?? Bxf1, then 9:07 on 17.Qf2, 7:42 on 18.Rd1, 6:09 on 32.Nxd5, ended 1:36. Once down material vs SF, cap 5-10 s and play the first safe move.
- Conversions: Qxf4/Qxb1 then Q+R mate (T58R3); rook takes loose pawns then h-pawn promotes (T58R5.2); T59 Q+2R v 2R: Qc3, Qxe3/Qxf2, Rd8#. Simplify, no fancy plan, 5-10 s.
- AFTER A QUEEN TRADE, RECOUNT: T59 24.Qxd3 left me down Q+B for R; if the recapture chain loses the queen, don't start it.

## Openings (only the lines I actually play)
- English as Black (wins many; L T54R3; T59S2G1 lost on time): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies). Then ...Bf5, ...Nbd7, ...Qc7/...Qb6, ...Rfc8; ...c5 only when d5 has a PIECE guard. T59: ...Bf5/...Bg6/...Nbd7/...Qb6; his Nd4 hit Bf5 and Rc1 pressed c6/d5. My queen grabs of b2/c3 won pawn+knight but his rooks ran b7-e7-a7 and his bishop reached d6/f8; count his rook activity before a queen grab. If White plays 8.d4, ...Bf5/...Nbd7/...Ne4, then ...dxe4! makes an e4-pawn hitting f3/d3; his 13.b3?? left Nf3 there, ...exf3! won a knight (T58R5.2). BANS: ...Na4?? bxa4, ...Bxa4?? Rxa4; ...Bd6?? onto Nf5's jump (T57R5.2). As White vs 5...d4: 6.Nb1!, NOT 6.Nd5?? (...Nxd5/...Qxd5 wins B for N, T58).
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); then ...Na5 with Bc2, ...c5 and d4/Nbd2. As Black move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo; Qc7 defended by Rc8 is still Rxc7. As White keep Rc1; no piece on a square his g6-pawn covers (f5/h5). BANS: ...Qxd4?? c3, ...Qf6 while his queen takes f6, ...Re8?? Rxe8+. T59 W WIN vs GLM: vs a ...Bc5/...Bb6 setup (Black ...O-O, ...d6, ...h6, ...Be6, ...Qd7, ...Rfe8, ...Bxb3, ...d5), play c3/d4/Nc3/Be3/Qd2/Rad1; meet ...d5 with e5!; after ...Ne4 trade Nxe4 dxe4, then Nh4 hits f5/g6. 19...Qf5?? 20.Nxf5 won her. BAN Nbd2 before d4 (1 illegal T59).
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then ...Qd7, ...Rfe8, ...d5. If ...Bg4 comes, Re1 and h3. T53R2 WIN: Bxd5 won a knight; his ...Nxd4 allowed cxd4 and ...Qe6 hung the bishop to Bxe6. T56R2 WIN v GLM: 15...c6?! 16.Bxd6! Qxd6?? 17.Qxd6. Keep Bf4 for a real d6 target. BANS: 10.d4?!, b4 WHILE MY KNIGHT IS ON b3, queen on d5 while his f6-knight lives.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); then f4, Qd2, Rad1, Kh1. 9.f4 b5 10.e5! best; after ...Nd5 take it; if ...exd5 hit d5 with Bf3/Qd2/Rf2 before Nf5. WIN T55S2G1, T54S2G1, T54R1, T53R3, T57R3. BANS: 12.Qd2?? after ...Bc5, 15.Nd5?? (Nf6 recaptures), 26.Rxa6??, 27.Qf4?? Nxf4. T57 LOSS was the clock: +B+P then +N+P, flagged with 23.Qd3/16.Nf5/14.Bxd5 thinks; keep Nd6, simplify, 5-10 s moves.
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies); 9.Qg4. With my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8); never ...f5 while exf6 opens lines. T50R3: 11...g6?? 15.Qf6 won h8, 17.Bh6 Qxf8#. T51R1: 14...Qe7?? screened Bf8 from d6 - 15.Nd6+!. T49R4: ...a6 BEFORE White's Nb5. T55 Final: 12...f6?? let 13.Nxd5!/14.exf6/15.Qxf6.
- Caro B (T56R5 L; T57R1 L v SF19): 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies); then ...cxd4/...Bc5/...Bb6/...Ne7/O-O. With king g8, rook f8 and g7 gone, 28.Re8+ ...Rf8 29.Qg7#. Never ...f6 while e6 has no PIECE guard; retreat the bishop before f4-f5; never recapture ...Bxf5 on the open f-file (T56R3 16.Rxf5); recapture ...hxg6, never ...Nxg6?!; ...Be4 loses to Nxe4; no ...Ngf6 while e5 stands.
- Other: vs ...Nc6/...g6 with Bc3/Bc4 (T55 L v SF19): 9.h3?? let ...Nxe3. If ...Ng4 comes defend/move e3 FIRST (Qd2, Bd4, or trade with recapture); kick h3 only when e3 is guarded twice. T59 vs SF19 Dragon (1...c5 ...Nc6 ...g6 ...Bg7 ...Nf6 ...d6 ...Ng4): 8.O-O and 10.h3?? let ...Nxe3; after ...O-O/...Rb8/...Qa5/...Ba6 Black was +1.77 by m11. Play O-O-O/f3/Qd2 or a Be2 setup; BAN 15.Qd2?? while a bishop aims at f1.

## Opponents
- SF19: instant, zero errors, never repeats while progressing. Punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares, every voluntary pawn loosening. T55 Final: 13.Nxd5!/14.exf6/15.Qxf6 off 12...f6??. T56R3: Caro +0.4, then 14.f5! mate 22. T57R1: Caro fine to 18...Qd6; 19...b5?! and 22...Qb6? let 23.Bxg7! and Qg7#. T58: English; 5...d4! 6.Nd5?? Nxd5 7.Bxd5 Qxd5!, 8.Qb3?? Qxh1, 9.Kf1?? Bh3+ 10.Ke1 Qxg1#. T59: Dragon ...g6/...Bg7/...Nf6/...d6/...Ng4; 8.O-O/10.h3 met ...Nxe3; 15.Qd2?? Bxf1 won the exchange; later Kh3 + h4-pawn = Qg3#; my 9-7-6 min thinks while losing fixed nothing. Give him no pawn break and no loose unit; 10-15 s.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square. Sonnet 5.5 (never beaten): banks clock, quiet space moves, then takes every UNGUARDED unit; 10-15 s from move 1, keep a rank-1 blocker. GPT-6.1 Sol: fast, takes every free piece incl. a queen on any pawn/bishop diagonal or knight square. GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3 and the Chigorin; gives nothing loose.
- GLM 5.3 Flash (wins T51R5, T52R1, T52R5, T53R2, T53R5, T54S2G1, T56R2, T57R2, T57R5.2, T58R5.2, T59R1; T54R3 L on time): slow, miscounts material, hangs queens/rooks/knights when worse or even, but punishes MY loose knight jumps. T58R5.2: its 13.b3?? left Nf3 on the e4-pawn's capture square, ...exf3! won a knight; 5 illegal tries. T59R1: Ruy ...Bc5/...Bb6, ...d5; 19...Qf5?? hung its queen to Nh4; 3 illegal tries. 10-15 s, guard every unit, take every loose unit, never an empty or illegal reply.
- Haiku 5.5: fast, solid Italian Pianissimo, no free material; I forfeited T44R3 and lost T45R3 on the clock. 10-15 s, bank time, check legality twice.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded but leaves an active piece loose and can put a piece on my queen/pawn's capture square. Won T50R2, T51R3, T51S2G1, T53R3, T54R1, T55R3, T55S2G1, T56R4, T57R3, T58R3; lost T51R4, T52R3, T52S2A, T53S2G1, T56R1, T57, T58S2G1, T59R3. T57R3: as White Taimanov I took 15...Qc5?? with 16.Bxc5! then 20...Rc3?? bxc3, Qc8#. T57: +N+P but flagged; it had 47 min left. T58R3 (won as Black): 12...Nxe5?? dropped a piece, I won it back off loose pawns and both rooks (Qxf4/Qxb1), 57...Qc2#. T58S2G1 (lost as White on time): Open Sicilian, +B+2P by m31, queens off; its ...Rc1+ pinned my Bg1 and ...f3/...h3 threatened ...hxg2#; I flagged with 2:48. T59R3 (lost as Black): English reversed QGD; it played e4/f4/e5 fork, and 22...Qxd3?? 23.Rxd3 won my queen. T59S2G1 (lost as Black on time): English reversed QGD; my queen took b2 and c3 but its rooks ran b7-e7-a7; later I won a rook and made a queen with 32...d1=Q+ but had burned 5-9 min on 9...Nbd7, 20...Nd4, 23...Ne2+, 24...Rd8, 25...d2, 26...Ng4, 27...Nxf2+ and flagged. It builds slowly, then uses supported pawn breaks. Take every loose unit, convert FAST, and once material is banked play 5-10 s moves - its clock is not the weapon, mine was.
