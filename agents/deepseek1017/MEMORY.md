# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit; walk piece, ACTUAL square, occupant, path, MY OWN occupants. After ONE rejection pick a DIFFERENT move. A QUEEN GOES ONLY ON RANK/FILE/DIAGONAL (T61R5.2 rejected Qxg6 from e6, also Bxf3 and Be3). A rejection means my board picture is wrong.
- HIS PAWNS ARE CAPTURERS ON BOTH FORWARD DIAGONALS - list them BEFORE any piece lands, bishop and knight included, queen first. T60R2 14...Qc6?? his d5-pawn owned c6 AND e6: 15.dxc6 won my QUEEN. T60R1 20.Bd3?? cxd3; T60R5.2 14.Bf4?? exf4; T61R3 13...Bxe4?? 14.dxe4 (his d3-pawn). After each of his pushes say 'his pawn on X owns Y and Z' for every pawn on ranks 3-6, then check EVERY piece of mine within reach.
- MY BIGGEST LEAK IS THE FANTASY QUEEN TRADE: T61R4 13...Qxe5?? took a PAWN his Qe2 defended along the open e-file; no piece of mine reached e5 (+1.0 -> +8.1). Same disease: T60R3 ...Qxa4, T61R3 ...Qb4. When my queen captures near his queen, answer 'if he takes, WHICH OF MY PIECES TAKES BACK' and point at it; no named recapturer = the capture is a loss.
- LEAVING f6 ABANDONS d7: T61R3 12...Ne4 13.Nxe4 Bxe4 14.dxe4 dxe4 15.Qxd7! Before a knight leaves f6/b6/e7 name every square it guarded.
- MY PAWNS CAPTURE TOO - sweep MY pawn map against HIS units every move: T61R1 26.exd5! won his Nd5, 30.cxd7 his QUEEN off my c6-pawn; T61R5.2 my e6-pawn cost him a knight and Bxc6/Bxd7/Bxe8/Bxa8 ate pawn, bishop, rook and rook.
- VACATED-SQUARE RULE: before ANY pawn push or capture name the file/diagonal the emptied square opens, then every enemy queen/bishop/rook on it. T59 16.dxe5 opened the d-file to Rd8xd2; T60S1G1 20...hxg6 emptied h7 for his Rf3; T61R2 17.e4?? opened d4-e3-f2 - 18.Kg1 Qd4+ 19.Kf1 Qf2#.
- A PIECE ON MY GUARD LINE CUTS IT: T61R2 ...Nd3+ stood on c2-d3-e4-f5, so Qc2 no longer guarded Nf5. Name every square between my queen/bishop and the piece it guards.
- QUEEN GRABS: name the piece on the landing square and walk HIS lines - rank, file, both diagonals - and his pawn captures to it. After ANY of his a/b/c/d pawn pushes write its two capture squares before a queen or bishop lands. A QUEEN MOVE THAT TOOK 1-2 MINUTES IS STILL A BLUNDER IF A PAWN HITS THE SQUARE.
- A KICK AT A BISHOP STANDING ON MY QUEEN'S LINE LOSES HER: T61R5.2 10...h6?? 11.Bxd8 (my Bg5 on g5-f6-e7-d8, his queen still on d8). Mirror of T59 13...h6?? 14.Bxe7. Before any h3/h6/...g6 kick, walk the kicked bishop's line to my queen.
- WITH HIS e5-PAWN ALIVE, f6 AND d6 ARE ITS SQUARES (T59 11...Nf6??); an attacked d5-knight retreats to b4/e7/b6/c7. A ROOK ON THE 6th/7th: list his a/b/c-pawn captures - T60R1 32.Rc6?? bxc6.
- A PIECE GUARDED ONLY BY ONE MINOR/QUEEN IS LOST (T54R1 11...Bc5??; T57R4 28...Bb7). A PAWN IS A GUARD TOO: ...Qxb2 removed Nc3's guard, ...Qxc3 won the knight (T59S2G1). After any enemy pawn capture list the squares that pawn guarded.
- HIS KNIGHTS HAVE A ROUTE: a knight on a6/b6/c6 aims at b4/c4/d4, and with MY QUEEN on c2 that is ...Nb4! (T61R2 13.Bg2?? Nb4! 14.Qb1 Nd3+ 15.Kf1 Bxf5). An enemy knight on d3/e2/f2 beside my uncastled king forks - CASTLE early, keep my queen off c2/b1 when his knight is loose.
- A KNIGHT LANDS ONLY WHERE NO ENEMY KNIGHT OR PAWN COVERS IT: T61R1 13.Ne5?? - his Nbd7 owned e5. HIS PAWN TWO SQUARES FROM MY BACK RANK IS A FORK MACHINE (T55R2 8...d3).
- A KNIGHT GUARDED ONLY BY HIS QUEEN WITH NO RETREAT = WON FOR A PAWN: T61R1 19.f4! 20.fxe5.
- HIS PIECE WITH NO RETREAT IS A TARGET - count its exit squares the moment it lands on the rim. T62R1 18.Nh4 had f3/g2 filled by his own pieces: after 18...Bh7! (covering f5, g6 and e4) 19...g5! won the knight for a pawn. Mirror: keep MY knights off rim squares his pawns can step onto once the exits are gone.
- AN OPEN FILE + HIS ROOK = MY PIECE THERE IS FREE (T53R3 14...Bf5?? Rxf5); the mirror wins for me (T55 27...Nxc4!).
- THE MOVING PIECE ABANDONS ITS DUTY: name what it guarded (T52R3 20...Bb7?? Nd7 to Rxd7). Answer an attacked piece before any quiet move or castle. An ATTACKED KNIGHT has 8 jumps - check them before it lands near my queen/rook.
- ROOK TAKES A PAWN: walk EVERY enemy bishop diagonal to that pawn (T57R1 21...Rxa2?? 22.Bxa2). A ROOK CHECK near my king: block on a DIFFERENT rank from my queen (T52 Final 21.Be3? Rxe3+).
- Qg3/Qg4 + a bishop reaching e5/f6/h6 = Qxg7#; never ...dxe5 then. Keep the king on e8; ...g6 then O-O-O playable, but check Bg5/Bh6 to d8 first.
- A QUEEN ON d4/e3 IN FRONT OF HIS c5-PAWN MUST SEE THE ...d4 PUSH (T56S2G1 12.Qd4?! ...c5 14.Qe3?? ...d4 forked Qe3+Nc3).

## King safety, endings, conversion
- CASTLED Kg8 WITH MY g6-PAWN AND HIS h5-PAWN = THE h-FILE MATE: T60S1G1 20...hxg6?? 21.hxg6 fxg6 22.Qxg6+ Kh8 23.Rh3#. Take on g6 with the F-pawn or keep a PIECE there.
- MY f-PAWN ON e3 LEAVES f2 EMPTY: his Nd3 guards f2 and ...Qd4+/...Qf2# - T61R2. With queens on, name f2's guard every move.
- BACK RANK IS THE #1 MATE: Kg8 behind f7/g7/h7 with NO luft = a rook stays on the 8th. T60R2 I was a BISHOP UP, played 24...Rb8 25...Rb5?? 26.Rd8#. UP MATERIAL, QUEENS OFF: h6/luft FIRST. Model fortress: T56R1 51...Qd7, 52...Rc8#.
- THE ROOK-GUARDED g7 MATE IS MY STANDARD FINISHER: T61R5.2 28.Rxe7! (covers g7) 29.Qxg7#; T61R1 37.Qxd7! Rxd7 38.Re8#. Whenever his g7-pawn is defended by the king alone, look for it at once.
- MY QUEEN ON h4 + A KNIGHT TO e2 = Ne2# when his king sits on g1 with f1 and g2 blocked by his own pieces: T62R1 46...Qh4+ 47.Kg1 Ne2# (she cut f2/g3/h1/h2, the checker covered g1). When his Kg1 has no flight and I am heavy up, play the CHECK first, then the knight.
- MY UNCASTLED KING WITH A ROOK ON THE h-FILE IS A TARGET once the pawn in front of that rook moves (T59 Final Qxh8+). Up a queen: PROGRESS EVERY MOVE, no repetition, no pawn grabs with her.
- DOWN A QUEEN v SF, THREEFOLD is the only save (T57R2; T58 Final +8.4). A repetition needs the SAME position with MY move. HIS Qf6 + a bishop reaching f2, my Kg1 = ...Qxf2#. KING h1 + HIS Qg3 = ...Re1#.
- Q+R v bare K: defended non-adjacent checks, walk the king up. TWO ROOKS v R+B: take the clean rook trade, then two attackers against one FROZEN pawn. TWO BISHOPS v R+pawns: mutual support covering the pawn his rook eyes. UP A ROOK / 2R v R: take the first clean trade, rank-2/3 checks drive his king off his pawns, no check a pawn takes. UP R+B: rook freezes his pawns, bishop escorts the passer. LEVEL R+B v R+B: repetition draw is fair. TWO ROOKS v QUEEN: blockade, not raids.
- UP THE EXCHANGE WITH QUEENS ON AND HIS ATTACK LIVE IS A NO-GRAB STATE: T60R3 17...Bc5 18...Bxe3 (+4.7) died to my own queen grab; T60S1G1 19...Qb6 with his Qh6/Rf3 clamp. Guard every unit, meet his pushes, no sorties.
- DOWN A ROOK WITH PAWNS ON THE BOARD IS NOT LOST: T60R1 held 2R v R for 25 moves and drew by threefold - rook blockading his extra pawn (Rc4), king beside my pawn pair, a pawn on f5 taking e6/g6 from his rooks, NO rook trade. Never resign a rook down while his pawns can be frozen.
- AFTER A BLUNDER, PLAY ON: T61R1 lost a clean knight at move 13 and mated 25 moves later; T61R4 gave a queen for a pawn and forced SF to find 39.Rf7#. Never resign, never plan on the flag.

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. Most losses are scan misses, not the clock: 1:26 did NOT stop T60R2's ...Qc6??; 47 s did not stop T61R4's 13...Qxe5??. Time goes on the DESTINATION LIST, never on why the move is nice.
- CONVERTING A WON POSITION IS 5-15 s A MOVE: T62R1 I was a piece up from move 20 and still spent 2:19 (...h6), 1:34 (...Bd6), 1:34 (...h5), 2:24 (...Bh7), 2:54 (...Qc5), 2:20 (...Qxa3), 3:25 (...Qe3), 3:22 (...c5) - 37 of 60 minutes used in a game with no counterplay. The long thinks found nothing the sweep finds.
- Long thinks on a raid that leaves my king on e1 buy nothing: T61R2 69 s on 10.Nd4, 80 s on 12.Nf5. Castle and complete development in 5-15 s.
- ARMAGEDDON AS WHITE IS THE TIGHT CLOCK (10 min): 10-20 s a move.

## Opening: English / reversed QGD (both colours)
- Reversed QGD build: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3). Keep ...c6 (or ...Ne4) before ...c5. WINS: T56R3, T56R5.2, T58R1, T60R1, T61R1, T62R1.
  - T62R1 (v GLM, mate): ...Nbd7 ...Re8 ...Qc7 ...Nb6 ...Bf5 ...h6 ...Rab8 ...Bd6 ...Qd7 was level and safe; the win came from his rim knight (18...Bh7! 19...g5!). No ...c5 while his e3-pawn can play e4!; no ...Nc4/...Ne4 with his b3/d3 pawns home.
  - With his ...Nbd7 played, e5 is HIS square - never an outpost there (T61R1 13.Ne5??).
  - Defend b2 or trade queens before Rc1: T59S2G1 11.Rc1 Qb6! 12.Nf3 Qxb2 13.Rb1 Qxc3.
  - AS BLACK, ...c5 with his e-pawn on e3/e4 is a TRAP: T60R2 12...c5 met 13.e4!. ...c5 only after ...Nbd7-...Nb6.
  - T61R3 LOSS (m29, Rd1#): 12...Ne4 abandoned d7, 13...Bxe4?? stood on his d3-pawn's square, 21...Qb4?? on his a3-pawn's square.
- Symmetric English v GLM (1-0 mate T60R5.2; 1-0 T61R5.2): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nxc3 6.bxc3 Bd6 7.Nf3 O-O 8.O-O Nc6 (16 plies), then d3/Be3/Qd2/Rfe1, e4 and d4.
  - T60R5.2: 22.Bd5! and 23.Rxf7! won. T61R5.2: 10.Bg5 with his queen still on d8 - 10...h6?? 11.Bxd8 = queen for bishop; then e4/d4/Ne5 and Bxc6-Bxd7-Bxe8-Bxa8 collected everything.
- v 1...e5 the same squeeze with Bg2/Nf3/O-O/d4 (T59R3 WIN by mate: e4!/f4!/e5! forked Qd6+Nf6 - e5 guarded by f4; his 22...Qxd3?? 23.Rxd3 = Q+B for R).
- W v SF clamp: ...d4 6.Nb1 Be7 7.e3 dxe3 8.fxe3 (15 plies). Then Bg2/O-O/d3; meet ...Nc3 with Qe1; never trade Bg2 for a knight; no d4 while ...c5 lives; CASTLE before any knight raid. T61R2 LOSS m19: his ...Na6/...Bf5/...Bg4 build, my 13.Bg2?? then ...Nb4! ...Nd3+ ...Bxf5 lost a clean knight; 17.e4?? opened d4-e3-f2 and ...Qd4+/...Qf2# mated me.

## Opening: Open Sicilian Taimanov (both colours)
- W line: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4/Qd2/Rad1. As Black the mirror build is sound; ...d5 only when e6 recaptures.
- AS BLACK: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies). ...Nxc3 hands him c3+d4+e5 - only for a concrete reason. 7.Ndb5 Qb8! is the only good retreat.
- v 9.Qg4 (T60R3, T60S1G1, T61R4): ...g6! is correct - it kills Qxg7/Bh6 nets and lets me castle BECAUSE the g6-pawn blocks the g-file; ...Qc7 then ...O-O; ...Re8 once his bishop reaches h6. T61R4: after 10...O-O 11.Bh6 NOTHING defends my Be7, so Bxf8 wins the exchange - fix the bishop BEFORE any queen sortie; 11...Qc7?! hitting e5 on the c7-d6-e5 diagonal set up 13...Qxe5??. His h4-h5/Qh6/Rf3 clamp is the whole game: answer it with a CONCRETE move, not a bishop wander (T60S1G1 14...Bb7?! +0.8 -> +2.55).
- AS BLACK v SF (T59, LOSS m26): 11...Nf6?? lost a knight to 12.Nxf6+ (and ...Bxf6 exf6). Later 22...Qxd6?? - his Qg3 saw d6 through f4-e5-d6. T59 FINAL: 16...Qa5?? ignored Qf6 hitting h8, 17.Qxh8+ won my uncastled rook.
- With queens on, do NOT open the centre and never take on e5; ...f6 only with his Bf4 off the c7 diagonal. AS BLACK ...b5 needs ...a6/...Bb7 first. His e5 hitting Nf6: ...Nd5 or ...Nh5, never ...Ne8 (Nc7 forks).
- WHITE CLAMP WIN: e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then f5-f6, Bxf6 and exf6!. Ban premature f4-f5. An in-between CHECK beats resolving a queen attack.
- Open Sicilian Dragon: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 (15 plies). His ...Ng4 is GUARDED by Bc8 through d7-e6-f5; answer Nxc6! bxc6 Bg5, NEVER Qxg4. King safety after ...Qa5/...Rb8; count ...Bxh2+ before castling; no a7 grab with his knight loose in my camp.

## Opponents
- Stockfish 19 (depth 4): instant, zero errors. Punishes loose pieces, hidden defenders, an unguarded c6, a kicked Ng4, any piece on his e5-pawn's f6/d6 square, ...f6 met by exf6, ...h6 met by Bxh6, my uncastled rook behind a moved pawn (T59 Final Qxh8+), and any shield pawn I recapture with a pawn that opens a file to my castled king (T60S1G1 Rh3#). It builds the 9.Qg4 + h4-h5 + Re3/Rae1 attack, plays 5...d4 in the English then ...Nb4/...Nd3+ (...Qd4+/...Qf2# on the f2 hole), and takes any 'offer' I cannot recapture. Give it no loose unit, no pawn break, no piece on a knight square; castle early.
- GLM 5.3 Flash: as White the English/reversed QGD, as Black the Taimanov/Modern; sound build but it checks pawn lines hard - T61R3 it took my bishop on e4 with its d3-pawn and my queen on b4 with its a3-pawn, and it CONVERTS (28.Bc4+ 29.Rd1#). Leaks: plain captures win its undefended pieces, its QUEEN fell to a bishop kick on the d8 line (T61R5.2 10...h6?? 11.Bxd8), and in T62R1 its rim Nh4 (f3/g2 its own pieces) fell to 18...Bh7! 19...g5!. 6 illegal tries in T62R1 and clock collapses (T58R1 forfeit 5:43, T59R2 forfeit 0:24) - but it thought 6:19 on one move and still had 46 min, so never count on its flag. My 1-0s: T56R3, T56R5.2, T57R1, T58R1, T59R2, T60R5.2, T61R5.2, T62R1 (Ne2#); lost T60R2, T61R3. Take loose units only after the pawn-capture list; never park anything on its pawn diagonals.
- DeepSeek V4.1 Flash (mirror): solid Taimanov/English both colours, converts without gifts. T61R1 (my 1-0 mate): as Black in the reversed QGD it walked its queen onto my c6-pawn (30...Qd7??) and its knight onto my e-pawn (25...Nd5??); down a queen it gave 37.Qxd7! 38.Re8#. Other: T56S2G1 ...c5/...d4! forked Qe3+Nc3; T58R3 22.Qxb5??; T59S2G1 ...Qxb2/...Qxc3 then flagged. T60R1 (draw) it took 20...cxd3 and shuffled to threefold. It parks pieces on MY pawns' capture squares - sweep MY pawn map every move.

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record (condensed)
- v SF19 (0-1 unless noted): T61R4 (13...Qxe5?? Q for P; m39 Rf7# after 26 moves of resistance); T61R2 (m19, Qf2#); T60S1G1 (h-file, Rh3#); T60R3 20...Qxa4??; T59 11...Nf6??/22...Qxd6??; T59 Final 16...Qa5??; T58 Final 1/2 (down a queen, threefold); T58 Arm; losses T53 Final, T54R1/R3/S1G1, T55R2/R3/S2G1, T57 Final, T58R2/R3.
- v GLM 1-0: T55R5.3, T56R3, T57R1, T58R1 (forfeit), T59R2 (forfeit), T60R5.2 (mate), T61R5.2 (10...h6?? 11.Bxd8; 28.Rxe7! 29.Qxg7#), T62R1 (reversed QGD level to m19, then 18...Bh7! 19...g5! won Nh4; 46...Qh4+ 47.Kg1 Ne2#). 0-1: T60R2 (14...Qc6?? dxc6, 25...Rb5?? 26.Rd8#), T61R3 (13...Bxe4?? dxe4; 21...Qb4?? axb4; m29 Rd1#).
- v mirror: 1-0 T56R1, T57R4, T58S2G1, T59R3 (mate), T59S2G1 (on time), T61R1 (mate after 13.Ne5??); 1/2 T60R1 (Rc4 blockade, threefold); 0-1 T57R3, T58R3.
