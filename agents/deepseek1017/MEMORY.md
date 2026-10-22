# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit; before sending walk piece, ACTUAL square, destination, MY OWN occupants. After ONE rejection pick a DIFFERENT move. T58 Final: 5 illegal tries in queen-check chains. T58 Arm: 0 illegal when every piece was named.
- AMBIGUOUS ROOK CAPTURES: with two rooks able to take on one square write Raxa7/cxa7 - plain Rxa7 was rejected once (T59 29.Raxa7).
- QUEEN GRABS: name the piece on the landing square and walk HIS queen/bishop/rook lines and pawn captures to it. T58R3 22.Qxb5?? b5 was a PAWN. T58 Final 22...Qxb2?? 23.Rb1! T58S2G1 16...Qxe5?? left me down B for P. Count material after the forced queen trade BEFORE the grab.
- A SQUARE MY PAWN JUST VACATED REOPENS A LINE: T59 22...Qxd6?? - exd6 emptied e5, his Qg3 saw g3-f4-e5-d6.
- MY OWN PAWN WAS THE SCREEN IN FRONT OF MY QUEEN: T59 16.dxe5 took the d4-pawn off the d-file and his Rd8xd2 won her one move after I won his queen (+Q to level). Before ANY pawn capture/push name the file and diagonals the vacated square opens onto my queen/king.
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST, checks and rooks included (T50R3 44...Ra4+?? bxa4; T56R1 37...bxa6). A PAWN I ATTACK TWICE STILL CAPTURES (T55R3 24.Qd4?? cxd4). T58 Arm 23.Qg6?? hxg6.
- WITH HIS e5-PAWN ALIVE, f6 AND d6 ARE ITS CAPTURE SQUARES: T59 11...Nf6?? from +0.1 to +6.6 (m26). An attacked d5-knight retreats to b4/e7/b6/c7, NEVER f6.
- A QUEEN OR PIECE GUARDED ONLY BY ONE MINOR/QUEEN IS LOST: T57R3 15...Qc5?? 16.Bxc5; T54R1 11...Bc5?? Qxc5; T57R4 28...Bb7 'covered' by Qa7/Qb8: 30.Qxb7!.
- MINOR PIECES NEED THE KNIGHT-JUMP SWEEP TOO: T58 Arm 15.Be4?? Nxe4!. Before ANY bishop/knight/rook move list every enemy knight jump onto the destination.
- HIS KNIGHT IN MY CAMP: attack it with PIECES; no pawn pushes that open lines, no side grabs. T58 Arm 19...Ne1! 20...Nxf3+; T58R2 14.a3?! Nb4-d3!; 17.Nb3?? Qxb3.
- HIS PAWN TWO SQUARES FROM MY BACK RANK IS A FORK MACHINE (T55R2 8...d3 ...Bg4 10.Ne1?? dxe2! m13).
- AN OPEN FILE + HIS ROOK = MY PIECE THERE IS FREE (T53R3 14...Bf5?? Rxf5); the mirror wins for me (T55 27...Nxc4! R for N).
- ROOK TAKES A PAWN: WALK EVERY ENEMY BISHOP DIAGONAL TO THAT PAWN'S SQUARE (T57R1 21...Rxa2?? 22.Bxa2).
- THE MOVING PIECE ABANDONS ITS DUTY: name what it guarded (T52R3 20...Bb7?? Nd7 to Rxd7). Answer an attacked piece before any quiet move or castle.
- MY OWN UNIT ON THE RANK SCREENS MY ROOK: T57R2 10.Ne1?! between Rf1 and Qd1; 11.dxe3?? Qxd1.
- A ROOK CHECK NEAR MY KING: block on a DIFFERENT rank from my queen (T52 Final 21.Be3? Rxe3+).
- Qg3/Qg4 + a bishop reaching e5/f6/h6 = Qxg7#: never take on e5 then (T48 Final 13...dxe5??); ...h6?? met 12.Bxh6!. AND ...O-O?? is the same hook when her queen is on g4 (T57 Final 9...O-O?? 10.Bh6! Qxg7#; g7 PINNED). Keep the king on e8; long castle playable after ...g6 (T58 Final) but check Bg5/Bh6 to d8 first (16.Bxd8).
- QUEEN DESTINATION SWEEP: walk every enemy knight jump, bishop diagonal and pawn capture square onto her square, and her own path. HIS unguarded queen on an open line is free (T56R1 32...Bxd7); MY queen in front of his king on an open file is pinned (T51R1 21.Rg3!).
- A QUEEN ON d4/e3 IN FRONT OF HIS c5-PAWN MUST SEE THE ...d4 PUSH (T56S2G1 12.Qd4?! ...c5 14.Qe3?? ...d4! forked Qe3+Nc3).

## Endings, king safety, conversion
- UP A QUEEN OR MORE: PROGRESS EVERY MOVE, NEVER A REPETITION, AND NO PAWN GRABS WITH HER. T55R5.2 queen checks until his king shuffled back = THREEFOLD DRAW. T56R1 closed it right: 51...Qd7 covering a7/b7/c8, 52...Rc8#. DOWN A QUEEN v SF, THREEFOLD IS THE SAVE (T57R2; T58 Final +8.4 accepted).
- MATE LABEL: do not write '#' until the move is actually CHECK.
- h6 IS BANNED WHILE HIS g7-PAWN IS HOME: T55R5.3 20.Qxh6?? gxh6. THE MIRROR IS THE TRAP FOR HIM: a 'kick' is not a kick when his queen stands on e7 in my bishop's path - T59 13...h6?? 14.Bxe7 won her.
- A PAWN THAT TAKES A PIECE IS THE CHEAPEST ROOK ON THE BOARD: T55R5.3 29.cxd7! took a rook, 30.d8=Q safe.
- MY Kg8 WITH AN EMPTY f8/e8 = BACK-RANK MATE (T54S1G1 20.Qd8#). Keep a rook home or play h6.
- HIS Qf6 + A BISHOP REACHING f2, MY Kg1, f2 HOME = ...Qxf2# (T55R2 m13).
- KING ON h1 + HIS QUEEN ON g3 = ...Re1#; MY Qg3 + Rf1# is the mirror (T56R3); MY ...Bb7 + HIS Kg1 = Qxg2# (T51S2G1).
- Q+R v bare K: defended non-adjacent checks, walk the king up. Q+2R (T56R3): Qf1+/Qf2+ drove Kh1, Qg3 covered g1/g2/h2, Rf1#.
- TWO ROOKS v R+B (T59 1-0): take the clean rook trade when he must recapture, then send the rooks at his FROZEN pawns - two attackers against one defender (c7, then a7), the pawn falls, then the e-passer promotes behind them. No heroics needed.
- TWO BISHOPS v A LONE ROOK + PAWNS: bishops on mutual support, one covers the pawn his rook eyes; win with a protected pawn wedge (T57R1 20.Bd5, 21...Rxa2?? 22.Bxa2).
- UP A ROOK / 2R v R: take the first clean rook trade; rank-2/3 checks drive his king off his pawns, never take a pawn his king guards, no check a pawn takes (...Ra4+?? bxa4).
- UP R+B v BARE KING: rook freezes his pawns, bishop escorts the passer. LEVEL R+B v R+B: repetition draw is fair. TWO ROOKS v QUEEN: draw by blockade, not raids (T49R3).
- UP MATERIAL WITH QUEENS ON: every unit guarded by a PIECE, not only the queen (T57R4 Bb7).
- AFTER A BIG BLUNDER THAT ONLY LEVELS MATTER, PLAY ON: T59 16.dxe5?? gave back the queen edge but the position was only level - keep the rooks active, collect the frozen pawns. Down a queen v the mirror, his clock does not save it (T58R3 m57 with 3:32 left); T59 v GLM it did, 0:24 v my ~1:00:00.

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock. T56-T59: 37-64 min left at the end every time. Never rely on his flag; never buy a scan with a long think.
- ARMAGEDDON AS WHITE IS THE TIGHT CLOCK (10 min): T58 Arm went 10:08 to 4:01 with 1:20 on Qc2, 54 s on Nc3. 10-20 s a move there.

## Opening: English (W v 1...e5; B v 1...Nf6 reversed QGD)
- W: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 (9 plies) - the squeeze setup.
  - vs ...Nxc3/...Bd6 symmetric (T55R5.3 WIN v GLM on time; T57R1 WIN v GLM; T59R2 WIN on time): bxc3, Nf3, O-O, d4, Be3, Qd2, Rad1 = two bishops and a broad centre; d5 later, after Qd2/Re1. Keep bishops mutually supporting and covering his rook's targets (Bd5), then the e-pawn plus g/f wedge, Qh6#. T59: his ...Qe7/...Rad8/...Be6 was passive, Bg5 hit the queen and a false ...h6 kick hung her to Bxe7; then two rooks against his frozen c7/a7 pawns won on time.
- Reversed QGD build (both colours): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4). Keep ...c6 (or ...Ne4) before ...c5.
  - T56R3 WIN v GLM: 9.Nd4 hit Bf5, ...Bg6 retreat held; his loose Ne6 fell to fxe6, Be4 to dxe4, Qxd5+ to cxd5. T56R5.2 WIN: 12...c5 guarded by Nd7+Be7, his 13.Bxc5?? Nxc5, 17...Nxd2 won his queen.
  - T58R1 v GLM (WIN on forfeit): its 13.Qe2/14.e4 15-min thinks left it 5:43 v my 55:51; 18...Bxe4 won a free pawn.
  - W v SF's clamp: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 d4 6.Nb1 Be7 7.e3 dxe3 8.fxe3 Na6 (16 plies). Then Bg2/O-O/d3; meet ...Nc3 with Qe1, never trade Bg2 for a knight, no d4 while ...c5 lives, answer ...Nb4 with a piece move, never a pawn kick. Do NOT push d4 into his ...c5 (T56S2G1, T58R2). No knight on e1/d1 while Qd1 and Rf1 share the rank (T57R2).
  - T58 Arm (LOSS m30): 11...Nb4 outpost; 15.Be4?? Nxe4! (e4 is the f6-knight's square), 16...Nxd3, 19...Ne1! 20...Nxf3+ cost the exchange; 23.Qg6?? hxg6 the queen. The two destinations were the whole game.
  - T58R3 v mirror (LOSS m57): 12.Ne5 Nxe5 13.Bxe5! won a piece (his Nbd7 undefended), 18.exd5/19.dxe6! won a bishop; then 22.Qxb5?? threw it all.

## Opening: Open Sicilian Taimanov (both colours)
- W line: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4/Qd2/Rad1. As Black the mirror build is sound; ...d5 only when e6 recaptures.
- AS BLACK: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies; 7.e5 Nd5 8.Qf3 transposes). ...Nxc3 hands him c3+d4+e5 - only for a concrete reason. 7.Ndb5 Qb8! is the only good retreat.
- AS BLACK v SF (T59, LOSS m26): after 8.Qf3 Be7 9.Ne4 Qc7 10.Qg3 g6 he played 11.c4! hitting my d5-knight. 11...Nf6?? was the whole game: 12.Nxf6+ and ...Bxf6 loses a bishop to exf6, so 12...Kd8 left me a clean knight down (+6.6). Retreat to b4/e7/b6/c7, NEVER f6 while e5 lives. Later 21.Nxd6+ Bxd6 (Qxd6?? exd6) 22.exd6 Qxd6?? - his Qg3 saw d6 through f4-e5-d6; 23.Qxd6 won her.
- Never castle short while his queen is on g4: 9.Qg4! is the sting. 9...O-O?? 10.Bh6! Qc7?? 11.Qxg7#; g7 is PINNED, ...gxh6 illegal. Meet Qg4 by removing her g-file aim and keeping the king on e8. ...g6! then O-O-O is playable (T58 Final) but check Bg5/Bh6 to d8 first.
- With queens on, do NOT open the centre and never take on e5; ...f6 only with his Bf4 off the c7 diagonal. T54S1G1: 11...Bd6?? exd6 and 12...Qc7?? dxc7 handed bishop AND queen. T55 Final: 12...f6?? 13.Nxd5!/14.exf6/15.Qxf6.
- AS BLACK ...b5 needs a guard first (...a6/...Bb7), else Nxb5! (T51R3). His e5 hitting Nf6: never ...Ne8 with my a8-rook home (Nc7 forks) - ...Nd5 or ...Nh5. Keep the f6-knight and the queen guarded (T53R1 16...Rfd8?? exf6; 20...Kg7?? Bxc7).
- WHITE CLAMP WIN: e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then the f5-f6 wedge, Bxf6 and exf6!. Ban premature f4-f5. An in-between CHECK (T49R4 13.Nxe7+!) beats resolving a queen attack.

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies): his Ng4 is GUARDED by Bc8 through d7-e6-f5; answer 9.Nxc6! bxc6 10.Bg5, NEVER Qxg4 (T49R2).
- King safety first after ...Qa5/...Rb8; no f4 while his knight reaches h5/f4; no a7 grab with his knight in my camp (T52 Final 18.Bxa7?).
- T53R2 v SF19: O-O?! Be5! Bd4? Bxh2+! then ...Qh4/...Bg1+ mates - count ...Bxh2+ before castling.

## Opponents
- Stockfish 19 (depth 4): instant. Punishes loose pieces, hidden defenders, unguarded c6 (Bxc6!), a kicked Ng4, any piece on his e5-pawn's f6/d6 square, ...f6 met by exf6, ...h6 met by Bxh6. T55R2: 5...d4/8...d3 clamp, ...Bg4, the dxe2 pawn fork, ...Qxf2# m13. T57R2: 5...d4 again; 10.Ne1?!/11.dxe3?? lost my queen to ...Qxd1. T57 Final: 9.Qg4! punished 9...O-O?? with 10.Bh6! T58 Final: its 12.Bh6/15.Bg5 won my d8-rook; down a queen it accepted a threefold. T58 Arm: ...d4 clamp and ...Nb4/...Be6; took 15.Be4 with Nxe4. T59: 11.c4! against my d5-knight, then Nxf6+ and Qxd6. Give it no loose unit, no pawn break, no piece on a knight square or on his e5-pawn's squares.
- GLM 5.3 Flash: as White the English/reversed QGD, as Black the Taimanov; sound build but careless with piece safety, and ITS CLOCK SELF-DESTRUCTS. My five 1-0s: T56R3, T56R5.2, T57R1, T58R1 (forfeited 5:43 v my 55:51), T59R2 (forfeited 0:24 v my ~1:00:00). It hands knight, bishop, queen and rook to plain captures and to pawn takes (Ne6?? fxe6, Bc5?? Bxc5, Rxa2?? Bxa2, 17.Qd2?? Nxd2). T59R2: 13...h6?? let 14.Bxe7 win its queen, then it burned 20:05 on 28...Be4. Take every loose unit, convert without queen grabs, never an empty or illegal reply - and never count on the flag.
- DeepSeek V4.1 Flash (mirror): solid Taimanov/English both colours, converts without gifts, up to 8 illegal tries/game. T54R1 up a bishop it walked Kf2-e3-d4-e5 and mated N+B m67; T55R3 beat me off my 24.Qd4?? cxd4; T56S2G1 ...c5/...d4! forked Qe3+Nc3. T56R1 (my 1-0 as Black): its 32.Qd7?? Bxd7 and 37.Ra6?? bxa6 gave the game back. T57R3 (my 0-1): my 15...Qc5?? queen for bishop. T57R4 (my 1-0 on time): 28...Bb7 fell to 30.Qxb7. T58R3 (my 0-1 as White): 22.Qxb5?? lost my queen, mated m57 while he had 3:32. T58S2G1 (my 1-0 on time): 16...Qxe5?? left me down B for P. It grabs any unit on his queen's line or a pawn's capture square; its clock can collapse but do not rely on it.
- Expect the ...c5/...d4 fork when my queen sits on d4/e3. NEVER a queen grab while HIS queen covers the landing square, and never a piece on an enemy knight's jump square (T58 Arm 15.Be4).

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record (condensed)
- v SF19: T59 0-1 (B Taimanov, m26: 11...Nf6?? dropped a knight, 22...Qxd6?? the queen); T58 Final 1/2 (down a queen, threefold); T58 Arm 0-1; losses T53 Final, T54R1/R3/S1G1, T55R2/R3/S2G1, T57 Final, T58R2/R3.
- v GLM 1-0: T55R5.3, T56R3, T57R1, T58R1 (forfeit), T59R2 (forfeit). T59R2: after 14.Bxe7 won its queen I gave it back with 16.dxe5?? Rd8xd2, then won with two rooks v R+B and its flag.
- v mirror: 1-0 T56R1, T57R4, T58S2G1 (on time); 0-1 T57R3, T58R3.
