# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit; walk piece, ACTUAL square, occupant, destination, MY OWN occupants. After ONE rejection pick a DIFFERENT move. T61R1 rejected Bg5/Rad1 and e4 twice; T61R2 one invalid (16.Qc2); T61R4 one invalid (Kxf8). A rejection means my board picture is wrong.
- HIS PAWNS ARE CAPTURERS ON BOTH FORWARD DIAGONALS - list them BEFORE any piece lands, bishop and knight included, queen first. T60R2 14...Qc6?? his d5-PAWN owned c6 AND e6: 15.dxc6 won my QUEEN. T60R1 20.Bd3?? cxd3; T60R5.2 14.Bf4?? exf4; T58 15.Be4?? Nxe4!; T61R3 13...Bxe4?? - his d3-pawn had owned e4 all game: 14.dxe4. After each of his pushes say 'his pawn on X owns Y and Z' for every pawn on ranks 3-6, then check EVERY piece of mine within reach.
- MY BIGGEST LEAK IS THE FANTASY QUEEN TRADE: T61R4 13...Qxe5?? took a PAWN his Qe2 defended along the open e-file - no piece of mine reached e5, so it was Q for P (+1.0 -> +8.1). Same disease: T60R3 ...Qxa4, T61R3 ...Qb4. When my queen captures anything near his queen, answer 'if he takes, WHICH OF MY PIECES TAKES BACK' and point at it on the board; no named recapturer = the capture is a loss. A pawn his queen defends is the most expensive pawn on the board.
- LEAVING f6 ABANDONS d7: T61R3 12...Ne4 (from f6) 13.Nxe4 Bxe4 14.dxe4 dxe4 15.Qxd7! - his Qd2 reached d7 down the line my Nf6 had guarded. Before a knight leaves f6/b6/e7 name every square it was guarding.
- MY PAWNS CAPTURE TOO - sweep MY pawn map against HIS units every move: T61R1 26.exd5! won his Nd5, 30.cxd7 won his QUEEN off my c6-pawn, 25.Qe3 set up 26.e5! forking Bd6+Nf6.
- VACATED-SQUARE RULE (my most repeated loss): before ANY pawn push or capture name the file/diagonal the emptied square opens, then every enemy queen/bishop/rook on that line. T59 16.dxe5 opened the d-file to Rd8xd2; T60S1G1 20...hxg6 emptied h7 for his Rf3; T61R2 17.e4?? opened d4-e3-f2 to his queen on d4 - 18.Kg1 Qd4+ 19.Kf1 Qf2# (his Nd3 guarded f2).
- A PIECE LANDING ON MY GUARD LINE CUTS IT: T61R2 ...Nd3+ checked AND stood on the c2-d3-e4-f5 line, so Qc2 no longer guarded Nf5 and ...Bxf5 won the knight. Name every square between my queen/bishop and the piece it guards.
- QUEEN GRABS: name the piece on the landing square and walk HIS lines - rank, file AND both diagonals - and his pawn captures to it. Count material after the forced trade BEFORE the grab. A QUEEN MOVE THAT TAKES 1-2 MINUTES IS STILL A BLUNDER IF A PAWN HITS THE SQUARE (T60R2 ...Qc6). T61R3 21...Qb4?? landed on his a3-pawn's b4 square right after his a3 kick: 22.axb4. After ANY of his a/b/c/d pawn pushes write its two capture squares before a queen or bishop lands.
- WITH HIS e5-PAWN ALIVE, f6 AND d6 ARE ITS SQUARES (T59 11...Nf6??); an attacked d5-knight retreats to b4/e7/b6/c7. A ROOK ON THE 6th/7th: list his a/b/c-pawn captures - T60R1 32.Rc6?? bxc6.
- A QUEEN OR PIECE GUARDED ONLY BY ONE MINOR/QUEEN IS LOST (T54R1 11...Bc5??; T57R4 28...Bb7). A PAWN IS A GUARD TOO: ...Qxb2 removed Nc3's guard and ...Qxc3 won the knight (T59S2G1). After any enemy pawn capture list the squares that pawn guarded.
- HIS KNIGHTS HAVE A ROUTE TOO: a knight on a6/b6/c6 aims at b4/c4/d4, and with MY QUEEN on c2 that is ...Nb4! (T61R2 13.Bg2?? Nb4! 14.Qb1 Nd3+ 15.Kf1 Bxf5 lost a clean knight). An enemy knight on d3/e2/f2 beside my uncastled king is a fork machine - CASTLE before any knight raid, keep my queen off c2/b1 when his knight is loose.
- A KNIGHT LANDS ONLY WHERE NO ENEMY KNIGHT OR PAWN COVERS IT: T61R1 13.Ne5?? - his Nbd7 owned e5. HIS PAWN TWO SQUARES FROM MY BACK RANK IS A FORK MACHINE (T55R2 8...d3).
- A KNIGHT GUARDED ONLY BY HIS QUEEN WITH NO RETREAT = WON FOR A PAWN: T61R1 19.f4! (Qe2 covered c4/d3/f3/g4), 20.fxe5.
- AN OPEN FILE + HIS ROOK = MY PIECE THERE IS FREE (T53R3 14...Bf5?? Rxf5); the mirror wins for me (T55 27...Nxc4!).
- THE MOVING PIECE ABANDONS ITS DUTY: name what it guarded (T52R3 20...Bb7?? Nd7 to Rxd7). Answer an attacked piece before any quiet move or castle. An ATTACKED KNIGHT has 8 jumps - check them before it lands near my queen/rook.
- ROOK TAKES A PAWN: walk EVERY enemy bishop diagonal to that pawn (T57R1 21...Rxa2?? 22.Bxa2). A ROOK CHECK near my king: block on a DIFFERENT rank from my queen (T52 Final 21.Be3? Rxe3+).
- ROOK LANDS ON f7/f2 ONLY IF I GUARD IT: name MY OWN piece covering the landing square. T60R5.2 23.Rxf7! worked only because Bd5 covered f7; 22.Bd5! forked Qe6 and Nc6.
- Qg3/Qg4 + a bishop reaching e5/f6/h6 = Qxg7#: never ...dxe5 then; ...O-O?? with her queen on g4 invites Bh6! Keep the king on e8; ...g6 then O-O-O playable, but check Bg5/Bh6 to d8 first.
- A 'KICK' NEXT TO MY KING IS A HOLE: T59 13...h6?? 14.Bxe7 won her.
- A QUEEN ON d4/e3 IN FRONT OF HIS c5-PAWN MUST SEE THE ...d4 PUSH (T56S2G1 12.Qd4?! ...c5 14.Qe3?? ...d4 forked Qe3+Nc3).

## King safety, endings, conversion
- CASTLED Kg8 WITH MY g6-PAWN AND HIS h5-PAWN = THE h-FILE MATE: T60S1G1 20...hxg6?? 21.hxg6 fxg6 22.Qxg6+ Kh8 23.Rh3#. Take on g6 with the F-pawn or keep a PIECE there; once his Qh6+Rf3+h5 stand, get the king off g8.
- MY f-PAWN SITTING ON e3 (from fxe3 in the ...d4 clamp) LEAVES f2 EMPTY: his Nd3 guards f2, and his queen reaching d4/f4 mates - T61R2 18...Qd4+ 19.Kf1 Qf2#. With queens on, name f2's guard every move, castle early.
- BACK RANK IS THE #1 MATE: Kg8 behind f7/g7/h7 with NO luft = a rook stays on the 8th. T60R2 I was a BISHOP UP, played 24...Rb8 25...Rb5?? and 26.Rd8#. UP MATERIAL, QUEENS OFF: h6/luft FIRST, then rook activity. Model fortress: T56R1 51...Qd7, 52...Rc8#.
- R+R MUTUAL DEFENCE ON A RANK + HIS BOXED Kg8 = TACTIC: T61R1 37.Qxd7! Rxd7 38.Re8#. Before taking on a rook-defended square, check my rook reaching e8/d8.
- MY UNCASTLED KING WITH A ROOK ON THE h-FILE IS A TARGET once the pawn in front of that rook moves (T59 Final Qxh8+). Up a queen: PROGRESS EVERY MOVE, no repetition, no pawn grabs with her (T55R5.2).
- DOWN A QUEEN v SF, THREEFOLD is the only save (T57R2; T58 Final +8.4 accepted). A repetition needs the SAME position with MY move.
- HIS Qf6 + a bishop reaching f2, my Kg1 = ...Qxf2#. KING h1 + HIS Qg3 = ...Re1#.
- Q+R v bare K: defended non-adjacent checks, walk the king up. TWO ROOKS v R+B: take the clean rook trade, then two attackers against one FROZEN pawn. TWO BISHOPS v R+pawns: mutual support covering the pawn his rook eyes. UP A ROOK / 2R v R: take the first clean trade, rank-2/3 checks drive his king off his pawns, never take a pawn his king guards, no check a pawn takes. UP R+B: rook freezes his pawns, bishop escorts the passer. LEVEL R+B v R+B: repetition draw is fair. TWO ROOKS v QUEEN: blockade, not raids.
- UP THE EXCHANGE WITH QUEENS ON AND HIS ATTACK LIVE IS A NO-GRAB STATE: T60R3 17...Bc5 18...Bxe3 (+4.7) died to my own queen grab; T60S1G1 19...Qb6 with his Qh6/Rf3 clamp. Exchange up or attack live = guard every unit, meet his pushes, no sorties.
- DOWN A ROOK WITH PAWNS ON THE BOARD IS NOT LOST: T60R1 held 2R v R for 25 moves and drew by threefold - rook blockading his extra pawn (Rc4), king beside my pawn pair, a pawn on f5 taking e6/g6 from his rooks, NO rook trade. Never resign a rook down while his pawns can be frozen.
- AFTER A BLUNDER, PLAY ON: T61R1 lost a clean knight at move 13 and mated 25 moves later; T61R4 down a QUEEN for a pawn I kept a c6/c4/e6 chain, captured only with traced recapturers, and forced SF to find 39.Rf7# at move 39. Never resign, never plan on the flag.

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. Most losses are scan misses, not the clock - 1:26 did NOT stop T60R2's ...Qc6??, 47 s did not stop T61R4's 13...Qxe5??. Time goes on the DESTINATION LIST, never on why the move is nice.
- Long thinks on a raid that leaves my king on e1 buy nothing: T61R2 69 s on 10.Nd4, 80 s on 12.Nf5, piece lost to a 0-second reply. Castle and complete development in 5-15 s.
- ARMAGEDDON AS WHITE IS THE TIGHT CLOCK (10 min): 10-20 s a move.

## Opening: English / reversed QGD (both colours)
- Reversed QGD build: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3). Keep ...c6 (or ...Ne4) before ...c5. WINS: T56R3, T56R5.2, T58R1 (its clock gone), T60R1, T61R1.
  - With his ...Nbd7 played, e5 is HIS square - never an outpost there (T61R1 13.Ne5??).
  - Defend b2 or trade queens before Rc1: T59S2G1 11.Rc1 Qb6! 12.Nf3 Qxb2 13.Rb1 Qxc3 (b2 was Nc3's guard).
  - AS BLACK, ...c5 with his e-pawn on e3/e4 is a TRAP: T60R2 12...c5 met 13.e4!. ...c5 only after ...Nbd7-...Nb6 (a PIECE guarding d5).
  - T61R3 LOSS (m29, Rd1#): 12...Ne4 abandoned d7 (15.Qxd7) and 13...Bxe4?? stood on his d3-pawn's square; 21...Qb4?? stood on his a3-pawn's square. Sweep e4/c4/b4 BEFORE a piece lands.
- v 1...e5 the same squeeze with Bg2/Nf3/O-O/d4 (T59R3 WIN by mate: 15.Nf3 hit Qd6, then e4!/f4!/e5! forked Qd6+Nf6 - e5 guarded by f4; his 22...Qxd3?? 23.Rxd3 = Q+B for R).
- Symmetric English v GLM T60R5.2 (1-0 mate): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nxc3 6.bxc3 Bd6 7.Nf3 O-O 8.O-O Nc6 (16 plies), then d3/...Be6/c4/Qb3/Bg5. The win came from 22.Bd5! and 23.Rxf7!.
- W v SF clamp: ...d4 6.Nb1 Be7 7.e3 dxe3 8.fxe3 (15 plies). Then Bg2/O-O/d3; meet ...Nc3 with Qe1; never trade Bg2 for a knight; no d4 while ...c5 lives; CASTLE before any knight raid. T61R2 LOSS m19: 8...Na6 9.Nc3 Bf5 10.Nd4 Bg4 11.Qc2 c5 12.Nf5 O-O 13.Bg2?? Nb4! 14.Qb1 Nd3+ 15.Kf1 Bxf5; 17.e4?? opened d4-e3-f2 and ...Qd4+ ...Qf2# mated me.

## Opening: Open Sicilian Taimanov (both colours)
- W line: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4/Qd2/Rad1. As Black the mirror build is sound; ...d5 only when e6 recaptures.
- AS BLACK: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies). ...Nxc3 hands him c3+d4+e5 - only for a concrete reason. 7.Ndb5 Qb8! is the only good retreat.
- v 9.Qg4 (T60R3, T60S1G1, T61R4): ...g6! is correct - it kills Qxg7/Bh6 nets and lets me castle BECAUSE the g6-pawn blocks the g-file; ...Qc7 then ...O-O; ...Re8 once his bishop reaches h6. T61R4: after 10...O-O 11.Bh6 NOTHING defends my Be7 (Kg8 does not reach e7), so Bxf8 wins the exchange - fix the bishop (retreat or trade) BEFORE any queen sortie; 11...Qc7?! hitting e5 on the c7-d6-e5 diagonal was the inaccuracy that set up 13...Qxe5??. Then his h4-h5/Qh6/Rf3 clamp is the whole game: answer it with a CONCRETE move, not a bishop wander - T60S1G1 14...Bb7?! took +0.8 to +2.55.
- AS BLACK v SF (T59, LOSS m26): 11...Nf6?? lost a knight to 12.Nxf6+ (and ...Bxf6 exf6). Later 22...Qxd6?? - his Qg3 saw d6 through f4-e5-d6. T59 FINAL (LOSS m47): 16...Qa5?? ignored Qf6 hitting h8, 17.Qxh8+ won my uncastled rook.
- With queens on, do NOT open the centre and never take on e5; ...f6 only with his Bf4 off the c7 diagonal. AS BLACK ...b5 needs ...a6/...Bb7 first. His e5 hitting Nf6: ...Nd5 or ...Nh5, never ...Ne8 (Nc7 forks).
- WHITE CLAMP WIN: e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then f5-f6, Bxf6 and exf6!. Ban premature f4-f5. An in-between CHECK beats resolving a queen attack.
- Open Sicilian Dragon: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 (15 plies). His ...Ng4 is GUARDED by Bc8 through d7-e6-f5; answer Nxc6! bxc6 Bg5, NEVER Qxg4. King safety after ...Qa5/...Rb8; count ...Bxh2+ before castling; no a7 grab with his knight loose in my camp.

## Opponents
- Stockfish 19 (depth 4): instant, zero errors. Punishes loose pieces, hidden defenders, an unguarded c6, a kicked Ng4, any piece on his e5-pawn's f6/d6 square, ...f6 met by exf6, ...h6 met by Bxh6, my uncastled rook behind a moved pawn (T59 Final Qxh8+), and any shield pawn I recapture with a pawn that opens a file to my castled king (T60S1G1 Rh3#). It builds the 9.Qg4 + h4-h5 + Re3/Rae1 attack, plays 5...d4 in the English then ...Nb4/...Nd3+ against my uncastled king (...Qd4+/...Qf2# on the f2 hole), and takes any 'offer' I cannot recapture (T60R3 ...Qxa4). Give it no loose unit, no pawn break, no piece on a knight square or his e5-pawn's squares, no unanswered 'offer'; castle early.
- GLM 5.3 Flash: as White the English/reversed QGD, as Black the Taimanov; sound build but it checks pawn lines hard - T61R3 it took my bishop on e4 with its d3-pawn and my queen on b4 with its a3-pawn, and it CONVERTS (28.Bc4+ 29.Rd1#). It still hands pieces to plain captures (Ne6?? fxe6, Rxa2?? Bxa2) and ITS CLOCK SELF-DESTRUCTS (T58R1 forfeit 5:43, T59R2 forfeit 0:24). My 1-0s: T56R3, T56R5.2, T57R1, T58R1, T59R2, T60R5.2 (mate, 54 min used, did not flag); lost T60R2 (13.e4!/14.exd5, 26.Rd8#) and T61R3. Take loose units only after the pawn-capture list; never park anything on its pawn diagonals.
- DeepSeek V4.1 Flash (mirror): solid Taimanov/English both colours, converts without gifts. T61R1 (my 1-0 mate): as Black in the reversed QGD it walked its queen onto my c6-pawn (30...Qd7??) and its knight onto my e-pawn (25...Nd5??), and its e5-knight fell to 19.f4!; down a queen it gave 37.Qxd7! 38.Re8#. Other: T56S2G1 ...c5/...d4! forked Qe3+Nc3; T58R3 22.Qxb5??; T59S2G1 ...Qxb2/...Qxc3 then flagged. T60R1 (draw) it patiently took 20...cxd3 and shuffled to threefold. It parks pieces on MY pawns' capture squares - sweep MY pawn map every move.

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record (condensed)
- v SF19 (0-1 unless noted): T61R4 (13...Qxe5?? Q for P; m39 Rf7# after 26 moves of resistance); T61R2 (m19, 5...d4 clamp, ...Nb4/...Nd3+, Qf2#); T60S1G1 (h-file, Rh3#); T60R3 20...Qxa4??; T59 11...Nf6??/22...Qxd6??; T59 Final 16...Qa5??; T58 Final 1/2 (down a queen, threefold); T58 Arm; losses T53 Final, T54R1/R3/S1G1, T55R2/R3/S2G1, T57 Final, T58R2/R3.
- v GLM 1-0: T55R5.3, T56R3, T57R1, T58R1 (forfeit), T59R2 (forfeit), T60R5.2 (mate). 0-1: T60R2 (14...Qc6?? dxc6, 25...Rb5?? 26.Rd8#), T61R3 (13...Bxe4?? dxe4; 21...Qb4?? axb4; m29 Rd1#).
- v mirror: 1-0 T56R1, T57R4, T58S2G1, T59R3 (mate), T59S2G1 (on time), T61R1 (mate after 13.Ne5??); 1/2 T60R1 (Rc4 blockade, threefold); 0-1 T57R3, T58R3.
