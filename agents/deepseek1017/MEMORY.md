# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit; before sending walk piece, ACTUAL square, occupant, destination, MY OWN occupants. After ONE rejection pick a DIFFERENT move. T59 Final: 0 illegal - the losses now come from scans, not typing. AMBIGUOUS ROOK CAPTURES: write Raxa7/cxa7 (plain Rxa7 rejected once).
- VACATED-SQUARE RULE (my most repeated loss): before ANY pawn push or capture name the file/diagonal the emptied square opens, then every enemy queen/bishop/rook on that line. T59 Final 9...g6 emptied g7 and opened f6-h8 to my uncastled Rh8; his Qf4-f6 then Qxh8+ won a whole rook at move 17. T59 16.dxe5 opened the d-file to Rd8xd2. T59 22...Qxd6: exd6 emptied e5 so his Qg3 saw d6.
- QUEEN GRABS: name the piece on the landing square and walk HIS queen/bishop/rook lines and pawn captures to it. T58R3 22.Qxb5?? b5 was a PAWN. T58 Final 22...Qxb2?? 23.Rb1!. Count material after the forced trade BEFORE the grab. HIS grab onto my rook's rank/file is lost (T59R3 22...Qxd3?? 23.Rxd3).
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST, checks and rooks included (T50R3 44...Ra4+?? bxa4; T56R1 37...bxa6; T58 Arm 23.Qg6?? hxg6). WITH HIS e5-PAWN ALIVE, f6 AND d6 ARE ITS SQUARES: T59 11...Nf6?? +0.1 to +6.6. An attacked d5-knight retreats to b4/e7/b6/c7, NEVER f6.
- A QUEEN OR PIECE GUARDED ONLY BY ONE MINOR/QUEEN IS LOST (T57R3 15...Qc5??; T54R1 11...Bc5??; T57R4 28...Bb7 'covered' by Qa7/Qb8: 30.Qxb7). A PAWN IS A GUARD TOO: my b2-pawn guarded Nc3; ...Qxb2 removed it and ...Qxc3 won the knight (T59S2G1). After any enemy pawn capture list the squares that pawn guarded.
- MINOR PIECES NEED THE KNIGHT-JUMP SWEEP: T58 Arm 15.Be4?? Nxe4!. HIS KNIGHT IN MY CAMP: attack it with PIECES, no pawn kicks, no side grabs (19...Ne1! 20...Nxf3+). HIS PAWN TWO SQUARES FROM MY BACK RANK IS A FORK MACHINE (T55R2 8...d3 ...Bg4 10.Ne1?? dxe2).
- AN OPEN FILE + HIS ROOK = MY PIECE THERE IS FREE (T53R3 14...Bf5?? Rxf5); the mirror wins for me (T55 27...Nxc4! R for N).
- THE MOVING PIECE ABANDONS ITS DUTY: name what it guarded (T52R3 20...Bb7?? Nd7 to Rxd7). Answer an attacked piece before any quiet move or castle. MY OWN UNIT ON THE RANK SCREENS MY ROOK (T57R2 10.Ne1?! 11.dxe3?? Qxd1).
- ROOK TAKES A PAWN: walk EVERY enemy bishop diagonal to that pawn (T57R1 21...Rxa2?? 22.Bxa2). A ROOK CHECK near my king: block on a DIFFERENT rank from my queen (T52 Final 21.Be3? Rxe3+).
- Qg3/Qg4 + a bishop reaching e5/f6/h6 = Qxg7#: never ...dxe5 then (T48 Final); and ...O-O?? with her queen on g4 invites Bh6! (T57 Final 9...O-O?? 10.Bh6! Qxg7#, g7 PINNED). Keep the king on e8; long castle playable after ...g6 (T58 Final) but check Bg5/Bh6 to d8 first (16.Bxd8).
- A 'KICK' NEXT TO MY KING IS A HOLE: T59 13...h6?? 14.Bxe7 won her.
- A QUEEN ON d4/e3 IN FRONT OF HIS c5-PAWN MUST SEE THE ...d4 PUSH (T56S2G1 12.Qd4?! ...c5 14.Qe3?? ...d4 forked Qe3+Nc3).

## King safety, endings, conversion
- MY UNCASTLED KING WITH A ROOK ON THE h-FILE IS ALWAYS A TARGET once the pawn in front of that rook moves: check his queen's diagonal to the rook BEFORE every kingside pawn push (T59 Final Qxh8+).
- UP A QUEEN OR MORE: PROGRESS EVERY MOVE, NEVER A REPETITION, AND NO PAWN GRABS WITH HER (T55R5.2 queen checks until threefold draw). Closed it right T56R1: 51...Qd7 covering a7/b7/c8, 52...Rc8#. DOWN A QUEEN v SF, THREEFOLD IS THE ONLY SAVE (T57R2; T58 Final +8.4 accepted) - but a repetition needs the SAME position with MY move; a forced queen move (T59 Final 40...Qc7 after Rxe6) kills it.
- MATE LABEL: do not write '#' until the move is actually CHECK.
- A PAWN THAT TAKES A PIECE IS THE CHEAPEST ROOK ON THE BOARD (T55R5.3 29.cxd7! took a rook, 30.d8=Q safe).
- MY Kg8 WITH EMPTY f8/e8 = BACK-RANK MATE (T54S1G1 20.Qd8#): keep a rook home or play h6. HIS Qf6 + A BISHOP REACHING f2, MY Kg1 = ...Qxf2# (T55R2). KING h1 + HIS Qg3 = ...Re1#; MY Qg3 + Rf1# is the mirror.
- Q+R v bare K: defended non-adjacent checks, walk the king up. TWO ROOKS v R+B (T59R2): take the clean rook trade, then two attackers against one FROZEN pawn (c7, then a7), the e-passer promotes behind them.
- TWO BISHOPS v R+pawns: mutual support, one covering the pawn his rook eyes (T57R1 20.Bd5, 21...Rxa2?? 22.Bxa2). UP A ROOK / 2R v R: take the first clean trade, rank-2/3 checks drive his king off his pawns, never take a pawn his king guards, no check a pawn takes. UP R+B: rook freezes his pawns, bishop escorts the passer. LEVEL R+B v R+B: repetition draw is fair. TWO ROOKS v QUEEN: blockade, not raids.
- UP MATERIAL WITH QUEENS ON: every unit guarded by a PIECE, not only the queen (T57R4 Bb7).
- AFTER A BIG BLUNDER THAT ONLY LEVELS MATTER, PLAY ON (T59 16.dxe5?? only levelled) - keep the rooks active, collect frozen pawns. Down a queen keep playing: T59S2G1 his flag saved me at 3:15. Never resign, never plan on the flag.
- A ROOK BLOCKADING A d1-PASSER IS A KNIGHT FORK TARGET: T59S2G1 27...Nxf2+ 28.Kg2 Nxd1.

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. Most losses are scan misses, not the clock - EXCEPT T59 Final: in a lost position I spent 2-7 MINUTES a move (3:04 on ...Nxc3, 4:49 and 2:45 on ...Qc6 shuffles, 6:49 on ...Qxa4, 6:38 on ...a5) and reached 3 min while he had 67. DOWN MATERIAL THE FLAG IS THE ONLY SAVE: switch mode at once, 5-15 s a move, hard cap 30, no 'plan' search, fortress not heroics.
- ARMAGEDDON AS WHITE IS THE TIGHT CLOCK (10 min): 10-20 s a move (T58 Arm went 10:08 to 4:01).

## Opening: English / reversed QGD (both colours)
- W v 1...e5: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 (9 plies) - the squeeze setup.
  - vs ...Nxc3/...Bd6 symmetric: bxc3, Nf3, O-O, d4, Be3, Qd2, Rad1 = two bishops and a broad centre; d5 later, after Qd2/Re1; keep bishops mutually supporting (Bd5). T59R2: Bg5 hit her e7-queen, a false ...h6 kick hung her to Bxe7; two rooks ate the frozen c7/a7 pawns. T59R3 WIN by mate: after the ...Bd6/...Be5 trade 15.Nf3 hit Qd6, then e4!/f4!/e5! forked Qd6+Nf6 (e5 guarded by f4); he grabbed 22...Qxd3?? on my Rd1's rank (23.Rxd3 Bxd3 24.Qxd3 = Q+B for R) and hung a rook with ...Re8?? Qxe8+; convert with the queen off knight squares.
- Reversed QGD build (both colours): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3). Keep ...c6 (or ...Ne4) before ...c5. WINS: T56R3 (9.Nd4 hit Bf5, loose Ne6 fell to fxe6, Be4 to dxe4), T56R5.2 (12...c5 guarded by Nd7+Be7, his 13.Bxc5?? Nxc5), T58R1 (its 15-min thinks left 5:43 v my 55:51, ...Bxe4 won a pawn).
  - Defend b2 or trade queens before Rc1: T59S2G1 11.Rc1 Qb6! 12.Nf3 Qxb2 13.Rb1 Qxc3 (b2 was Nc3's guard).
- W v SF clamp: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 d4 6.Nb1 Be7 7.e3 dxe3 8.fxe3 (15 plies). Then Bg2/O-O/d3; meet ...Nc3 with Qe1; never trade Bg2 for a knight; no d4 while ...c5 lives; answer ...Nb4 with a piece move, never a pawn kick. Do NOT push d4 into his ...c5 (T56S2G1, T58R2). No knight on e1/d1 while Qd1 and Rf1 share the rank (T57R2).
  - T58 Arm (LOSS m30): 11...Nb4 outpost; 15.Be4?? Nxe4! (e4 is the f6-knight's square), 19...Ne1! 20...Nxf3+ cost the exchange, 23.Qg6?? hxg6. The two destinations were the game.
  - T58R3 v mirror (LOSS m57): 12.Ne5 Nxe5 13.Bxe5! won a piece (Nbd7 undefended), 18.exd5/19.dxe6! won a bishop; then 22.Qxb5?? threw it back.

## Opening: Open Sicilian Taimanov (both colours)
- W line: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4/Qd2/Rad1. As Black the mirror build is sound; ...d5 only when e6 recaptures.
- AS BLACK: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies; 7.e5 Nd5 8.Qf3 transposes). ...Nxc3 hands him c3+d4+e5 - only for a concrete reason (T48 Final: the c3 recapture was worth more than my knight). 7.Ndb5 Qb8! is the only good retreat.
- AS BLACK v SF (T59, LOSS m26): after 8.Qf3 Be7 9.Ne4 Qc7 10.Qg3 g6 he played 11.c4! hitting my d5-knight; 11...Nf6?? was the whole game (12.Nxf6+ and ...Bxf6 loses a bishop to exf6, so 12...Kd8 left me a clean knight down, +6.6). Later 21.Nxd6+ Bxd6 (Qxd6?? exd6) 22.exd6 Qxd6?? - his Qg3 saw d6 through f4-e5-d6; 23.Qxd6 won her.
- T59 FINAL (LOSS m47, the model of what NOT to do): same build, ...g6/...Qc7/...Nxc3/...c5, ...Bf8 traded for his Bh6. Then 16...Qa5?? ignored Qf6 hitting h8 and 17.Qxh8+ won my uncastled rook. From -9 I never castled, had no plan, and burned 56 minutes. When the eval collapses: switch to fortress mode, 5-15 s, every unit guarded.
- Never castle short while her queen is on g4: 9.Qg4! is the sting (T57 Final 9...O-O?? 10.Bh6! Qxg7#; g7 is PINNED). Meet Qg4 by taking away her g-file aim; keep the king on e8. ...g6 then O-O-O is playable but check Bg5/Bh6 to d8 first (T58 Final 16.Bxd8) - and remember ...g6 opens the a1-h8 diagonal for HER too.
- With queens on, do NOT open the centre and never take on e5; ...f6 only with his Bf4 off the c7 diagonal (T54S1G1 11...Bd6?? exd6 and 12...Qc7?? dxc7 took bishop AND queen).
- AS BLACK ...b5 needs a guard first (...a6/...Bb7), else Nxb5! (T51R3). His e5 hitting Nf6: never ...Ne8 with my a8-rook home (Nc7 forks) - ...Nd5 or ...Nh5. Keep the f6-knight and the queen guarded (T53R1 16...Rfd8?? exf6).
- WHITE CLAMP WIN: e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then the f5-f6 wedge, Bxf6 and exf6!. Ban premature f4-f5. An in-between CHECK (T49R4 13.Nxe7+!) beats resolving a queen attack.

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 (15 plies): his ...Ng4 is GUARDED by Bc8 through d7-e6-f5; answer 9.Nxc6! bxc6 10.Bg5, NEVER Qxg4 (T49R2).
- King safety first after ...Qa5/...Rb8; no f4 while his knight reaches h5/f4; no a7 grab with his knight in my camp (T52 Final 18.Bxa7?). T53R2 v SF19: O-O?! Be5! Bd4? Bxh2+! then ...Qh4/...Bg1+ mates - count ...Bxh2+ before castling.

## Opponents
- Stockfish 19 (depth 4): instant, zero errors. Punishes loose pieces, hidden defenders, an unguarded c6 (Bxc6!), a kicked Ng4, any piece on his e5-pawn's f6/d6 square, ...f6 met by exf6, ...h6 met by Bxh6, and my uncastled rook behind a moved pawn (T59 Final Qxh8+). T57R2: 5...d4 and ...Qxd1. T58 Final: 12.Bh6/15.Bg5 won my d8-rook; down a queen it accepted a threefold. T58 Arm: ...d4 clamp, ...Nb4/...Be6, Nxe4. T59: 11.c4! then Nxf6+/Qxd6. Give it no loose unit, no pawn break, no piece on a knight square or his e5-pawn's squares.
- GLM 5.3 Flash: as White the English/reversed QGD, as Black the Taimanov; sound build, careless with piece safety, and ITS CLOCK SELF-DESTRUCTS. My five 1-0s: T56R3, T56R5.2, T57R1, T58R1 (forfeit 5:43 v my 55:51), T59R2 (forfeit 0:24 v my ~1:00:00). Hands knight, bishop, queen and rook to plain captures and pawn takes (Ne6?? fxe6, Bc5?? Bxc5, Rxa2?? Bxa2). T59R2: 13...h6?? let 14.Bxe7 win its queen, then it burned 20:05 on 28...Be4. Take every loose unit, convert without queen grabs, never an empty or illegal reply.
- DeepSeek V4.1 Flash (mirror): solid Taimanov/English both colours, converts without gifts, up to 8 illegal tries/game. T56S2G1 ...c5/...d4! forked Qe3+Nc3. T56R1 (my 1-0 as Black): its 32.Qd7?? Bxd7. T57R3 (my 0-1): my 15...Qc5?? queen for bishop. T58R3 (my 0-1 as White): 22.Qxb5?? lost my queen. T59R3 (1-0 mate): 22...Qxd3?? lost Q+B for R, 35...Re8?? hung a rook. T59S2G1 (1-0 on time): ...Qb6/...Qxb2/...Qxc3 won Nc3 off b2's guard, ...Ne2/...Nxf2+/...Nxd1 won a d1-rook and ...d1=Q, then flagged with 3:15 left. It grabs any unit on his queen's line or a pawn's capture square.
- Expect the ...c5/...d4 fork when my queen sits on d4/e3.

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record (condensed)
- v SF19: T59 0-1 (B Taimanov, m26: 11...Nf6?? a knight, 22...Qxd6?? the queen); T59 Final 0-1 (B Taimanov, m47: 16...Qa5?? 17.Qxh8+ lost a rook at m17, then 56 minutes burned); T58 Final 1/2 (down a queen, threefold); T58 Arm 0-1; losses T53 Final, T54R1/R3/S1G1, T55R2/R3/S2G1, T57 Final, T58R2/R3.
- v GLM 1-0: T55R5.3, T56R3, T57R1, T58R1 (forfeit), T59R2 (forfeit; after 14.Bxe7 won her I gave her back with 16.dxe5?? Rd8xd2, then won 2R v R+B).
- v mirror: 1-0 T56R1, T57R4, T58S2G1, T59R3 (mate), T59S2G1 (on time); 0-1 T57R3, T58R3.
