# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit; before sending walk piece, ACTUAL square, occupant, destination, MY OWN occupants. After ONE rejection pick a DIFFERENT move. T60R2 2 rejected tries (...Bf5 with c8 blocked, ...b5) burned clock for nothing. AMBIGUOUS ROOK CAPTURES: write Raxa7/cxa7.
- HIS PAWNS ARE CAPTURERS ON BOTH FORWARD DIAGONALS - list them BEFORE any piece lands, queen first. T60R2 14...Qc6?? his d5-PAWN owned c6 AND e6: 15.dxc6 won my QUEEN (I had scanned Bg2/Nc3/Nb5 and 1:26 of thought, not the pawn). T60R1 20.Bd3?? cxd3 (his c4-pawn owns b3+d3). Same class: T58 15.Be4?? Nxe4!. Say aloud 'his pawn on X owns Y and Z' for every enemy pawn on ranks 3-6 after each of his pushes.
- VACATED-SQUARE RULE (my most repeated loss): before ANY pawn push or capture name the file/diagonal the emptied square opens, then every enemy queen/bishop/rook on that line. T59 16.dxe5 opened the d-file to Rd8xd2; T59 22...Qxd6: exd6 emptied e5 so his Qg3 saw d6.
- QUEEN GRABS: name the piece on the landing square and walk HIS lines and pawn captures to it. Count material after the forced trade BEFORE the grab; his grab onto my rook's rank/file is lost (T59R3 22...Qxd3?? 23.Rxd3). A QUEEN MOVE THAT TAKES 1-2 MINUTES IS STILL A BLUNDER IF A PAWN HITS THE SQUARE (T60R2 ...Qc6).
- WITH HIS e5-PAWN ALIVE, f6 AND d6 ARE ITS SQUARES (T59 11...Nf6??); an attacked d5-knight retreats to b4/e7/b6/c7. A ROOK ON THE 6th/7th: list his a/b/c-pawn captures - T60R1 32.Rc6?? bxc6 lost a rook out of a LEVEL position.
- A QUEEN OR PIECE GUARDED ONLY BY ONE MINOR/QUEEN IS LOST (T54R1 11...Bc5??; T57R4 28...Bb7). A PAWN IS A GUARD TOO: ...Qxb2 removed Nc3's guard and ...Qxc3 won the knight (T59S2G1). After any enemy pawn capture list the squares that pawn guarded.
- MINOR PIECES NEED THE KNIGHT-JUMP SWEEP (T58 Arm 19...Ne1!). HIS PAWN TWO SQUARES FROM MY BACK RANK IS A FORK MACHINE (T55R2 8...d3 ...Bg4).
- AN OPEN FILE + HIS ROOK = MY PIECE THERE IS FREE (T53R3 14...Bf5?? Rxf5); the mirror wins for me (T55 27...Nxc4!).
- THE MOVING PIECE ABANDONS ITS DUTY: name what it guarded (T52R3 20...Bb7?? Nd7 to Rxd7). Answer an attacked piece before any quiet move or castle. An ATTACKED KNIGHT has 8 jumps - check them before it lands near my queen/rook.
- ROOK TAKES A PAWN: walk EVERY enemy bishop diagonal to that pawn (T57R1 21...Rxa2?? 22.Bxa2). A ROOK CHECK near my king: block on a DIFFERENT rank from my queen (T52 Final 21.Be3? Rxe3+).
- Qg3/Qg4 + a bishop reaching e5/f6/h6 = Qxg7#: never ...dxe5 then; ...O-O?? with her queen on g4 invites Bh6! (g7 PINNED). Keep the king on e8; ...g6 then O-O-O playable, but check Bg5/Bh6 to d8 first.
- A 'KICK' NEXT TO MY KING IS A HOLE: T59 13...h6?? 14.Bxe7 won her.
- A QUEEN ON d4/e3 IN FRONT OF HIS c5-PAWN MUST SEE THE ...d4 PUSH (T56S2G1 12.Qd4?! ...c5 14.Qe3?? ...d4 forked Qe3+Nc3).

## King safety, endings, conversion
- BACK RANK IS THE #1 MATE: Kg8 behind f7/g7/h7 with NO luft = a rook must stay on the 8th. T60R2 I was a BISHOP UP, played 24...Rb8 25...Rb5?? and 26.Rd8# - the only 8th-rank rook had walked off. UP MATERIAL, QUEENS OFF: h6/luft FIRST, then rook activity; never chase a wing pawn with the last back-rank rook. Model fortress: T56R1 51...Qd7, 52...Rc8#.
- MY UNCASTLED KING WITH A ROOK ON THE h-FILE IS A TARGET once the pawn in front of that rook moves (T59 Final Qxh8+). Up a queen: PROGRESS EVERY MOVE, never a repetition, no pawn grabs with her (T55R5.2).
- DOWN A QUEEN v SF, THREEFOLD is the only save (T57R2; T58 Final +8.4 accepted). A repetition needs the SAME position with MY move; a forced queen move kills it (T59 Final 40...Qc7 after Rxe6).
- MATE LABEL: do not write '#' until the move is actually CHECK.
- A PAWN THAT TAKES A PIECE IS THE CHEAPEST ROOK ON THE BOARD (T55R5.3 29.cxd7!).
- HIS Qf6 + a bishop reaching f2, my Kg1 = ...Qxf2#. KING h1 + HIS Qg3 = ...Re1#.
- Q+R v bare K: defended non-adjacent checks, walk the king up. TWO ROOKS v R+B: take the clean rook trade, then two attackers against one FROZEN pawn. TWO BISHOPS v R+pawns: mutual support covering the pawn his rook eyes. UP A ROOK / 2R v R: take the first clean trade, rank-2/3 checks drive his king off his pawns, never take a pawn his king guards, no check a pawn takes. UP R+B: rook freezes his pawns, bishop escorts the passer. LEVEL R+B v R+B: repetition draw is fair. TWO ROOKS v QUEEN: blockade, not raids.
- DOWN A ROOK WITH PAWNS ON THE BOARD IS NOT LOST: T60R1 held 2R v R for 25 moves and drew by threefold - my rook blockading his extra pawn (Rc4), king beside my pawn pair (Ke3/Kf3), a pawn on f5 taking e6/g6 away from his rooks, and NO rook trade. When a fortress leaves nothing to push the stronger side shuffles: shuffle the same squares and take the repetition. Never resign a rook down while his pawns can be frozen.
- UP MATERIAL BUT DOWN A BISHOP AND LOSING (T60R2): I chased b3/a5 with rooks and got mated. A piece up with queens off is a L U F T + trade-active-pieces problem, not a pawn-collecting problem.
- AFTER A BIG BLUNDER THAT ONLY LEVELS MATTER, PLAY ON (T59 16.dxe5?? only levelled). Down a queen keep playing and keep scanning: T60R2 after ...Qc6?? I won N/B back for 20 moves before the back-rank slip. Never resign, never plan on the flag.
- A ROOK BLOCKADING A d1-PASSER IS A KNIGHT FORK TARGET: T59S2G1 27...Nxf2+ 28.Kg2 Nxd1.

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. Most losses are scan misses, not the clock - a 1:26 think did NOT stop T60R2's ...Qc6?? queen hang; the LIST is the check, not the time. T60R1: 1-77 s a move, finished with 53 min v his 36 - the draw came from the fortress.
- ARMAGEDDON AS WHITE IS THE TIGHT CLOCK (10 min): 10-20 s a move.

## Opening: English / reversed QGD (both colours)
- Reversed QGD build: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3). Keep ...c6 (or ...Ne4) before ...c5. WINS: T56R3, T56R5.2, T58R1 (its clock gone), T60R1 (as White: 9.Nd4 hit Bf5, ...Bg6, then Qd2/Rad1, 13.Nxd5! Nxd5 14.Bxd5 = pawn up + bishop pair).
  - Defend b2 or trade queens before Rc1: T59S2G1 11.Rc1 Qb6! 12.Nf3 Qxb2 13.Rb1 Qxc3 (b2 was Nc3's guard).
  - AS BLACK, ...c5 with his e-pawn still on e3/e4 is a TRAP: T60R2 12...c5 met 13.e4! and his exd5, and my queen's c6/d6 squares were pawn-covered. ...c5 only after ...Nbd7-...Nb6 (a PIECE guarding d5) and never with a piece/queen left on c6.
- v 1...e5 the same squeeze with Bg2/Nf3/O-O/d4 (T59R3 WIN by mate: after the ...Bd6/...Be5 trade 15.Nf3 hit Qd6, then e4!/f4!/e5! forked Qd6+Nf6 - e5 guarded by f4; his 22...Qxd3?? 23.Rxd3 Bxd3 24.Qxd3 = Q+B for R).
- W v SF clamp: ...d4 6.Nb1 Be7 7.e3 dxe3 8.fxe3 (15 plies). Then Bg2/O-O/d3; meet ...Nc3 with Qe1; never trade Bg2 for a knight; no d4 while ...c5 lives; answer ...Nb4 with a piece move, never a pawn kick. T58 Arm (LOSS m30): 11...Nb4 outpost, 15.Be4?? Nxe4!, 19...Ne1! 20...Nxf3+ cost the exchange, 23.Qg6?? hxg6.

## Opening: Open Sicilian Taimanov (both colours)
- W line: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4/Qd2/Rad1. As Black the mirror build is sound; ...d5 only when e6 recaptures.
- AS BLACK: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies). ...Nxc3 hands him c3+d4+e5 - only for a concrete reason. 7.Ndb5 Qb8! is the only good retreat.
- AS BLACK v SF (T59, LOSS m26): 11...Nf6?? lost a knight to 12.Nxf6+ (and ...Bxf6 exf6). Later 22...Qxd6?? - his Qg3 saw d6 through f4-e5-d6.
- T59 FINAL (LOSS m47): 16...Qa5?? ignored Qf6 hitting h8, 17.Qxh8+ won my uncastled rook. From -9 no castle, no plan, 56 minutes burned.
- Never castle short while her queen is on g4: 9.Qg4! is the sting; g7 is PINNED. Keep the king on e8; ...g6 then O-O-O, after checking Bg5/Bh6 to d8.
- With queens on, do NOT open the centre and never take on e5; ...f6 only with his Bf4 off the c7 diagonal. AS BLACK ...b5 needs ...a6/...Bb7 first, else Nxb5!. His e5 hitting Nf6: ...Nd5 or ...Nh5, never ...Ne8 (Nc7 forks).
- WHITE CLAMP WIN: e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then f5-f6, Bxf6 and exf6!. Ban premature f4-f5. An in-between CHECK beats resolving a queen attack.
- Open Sicilian Dragon: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 (15 plies). His ...Ng4 is GUARDED by Bc8 through d7-e6-f5; answer Nxc6! bxc6 Bg5, NEVER Qxg4. King safety after ...Qa5/...Rb8; count ...Bxh2+ before castling; no a7 grab with his knight loose in my camp.

## Opponents
- Stockfish 19 (depth 4): instant, zero errors. Punishes loose pieces, hidden defenders, an unguarded c6, a kicked Ng4, any piece on his e5-pawn's f6/d6 square, ...f6 met by exf6, ...h6 met by Bxh6, and my uncastled rook behind a moved pawn (T59 Final Qxh8+). T57R2: 5...d4 and ...Qxd1. T58 Final: 12.Bh6/15.Bg5 won my d8-rook; down a queen it accepted a threefold. T59: 11.c4! then Nxf6+/Qxd6. Give it no loose unit, no pawn break, no piece on a knight square or his e5-pawn's squares.
- GLM 5.3 Flash: as White the English/reversed QGD, as Black the Taimanov; sound build, careless with piece safety, and ITS CLOCK SELF-DESTRUCTS. My 1-0s: T56R3, T56R5.2, T57R1, T58R1 (forfeit 5:43), T59R2 (forfeit 0:24). T60R2 (0-1): as White it played 8.e3/9.d3/10.b3/11.Bb2/12.Qd2, met my ...c5 with 13.e4! and 14.exd5, punished ...Qc6 with dxc6, and mated Rd8# the moment my last 8th-rank rook left. Hands knight/bishop/queen/rook to plain captures (Ne6?? fxe6, Bc5?? Bxc5, Rxa2?? Bxa2) - but take ITS loose units only after the pawn-capture list. Convert without queen grabs, never an empty or illegal reply.
- DeepSeek V4.1 Flash (mirror): solid Taimanov/English both colours, converts without gifts, up to 8 illegal tries/game. T56S2G1 ...c5/...d4! forked Qe3+Nc3. T56R1 its 32.Qd7?? Bxd7. T57R3 my 15...Qc5??. T58R3 22.Qxb5?? lost my queen. T59R3 22...Qxd3?? lost Q+B for R, 35...Re8?? hung a rook. T59S2G1 (1-0 on time): ...Qb6/...Qxb2/...Qxc3 won Nc3 off b2's guard, ...Nxf2+/...Nxd1 won a rook, then flagged. T60R1 (draw): as Black in the reversed QGD it plays ...c5/...Qc7/...Qd7 patiently and TAKES my piece on its pawn's capture square (20...cxd3); up a rook it shuffled rooks and king for 25 moves and let the threefold happen. It grabs any unit on his queen's line or a pawn's capture square - and it will take a piece I park on a pawn square.
- Expect the ...c5/...d4 fork when my queen sits on d4/e3.

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record (condensed)
- v SF19: T59 0-1 (11...Nf6?? a knight, 22...Qxd6?? the queen); T59 Final 0-1 (16...Qa5?? 17.Qxh8+); T58 Final 1/2 (down a queen, threefold); T58 Arm 0-1; losses T53 Final, T54R1/R3/S1G1, T55R2/R3/S2G1, T57 Final, T58R2/R3.
- v GLM 1-0: T55R5.3, T56R3, T57R1, T58R1 (forfeit), T59R2 (forfeit; after 14.Bxe7 won her I gave her back with 16.dxe5?? Rd8xd2, then won 2R v R+B). 0-1: T60R2 (14...Qc6?? dxc6 lost my queen, fought back to a bishop up with queens off, then 25...Rb5?? 26.Rd8#).
- v mirror: 1-0 T56R1, T57R4, T58S2G1, T59R3 (mate), T59S2G1 (on time); 1/2 T60R1 (piece down for 2 pawns, then a rook down - held with the Rc4 blockade, threefold); 0-1 T57R3, T58R3.
