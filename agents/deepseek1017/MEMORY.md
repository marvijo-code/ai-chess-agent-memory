# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit; 3 total ends the game. Before sending: piece, its ACTUAL square, destination, and MY OWN occupant of every path square. After ONE rejection pick a DIFFERENT move/idea. T57R3: illegal Rxf4 blocked by my own d4-pawn. T57R4: 4 illegal tries, all on quiet QUEEN retreats (Qc7/Qa7 tried twice each) - a rejected square stays dead; walk the queen's own path and destination occupancy.
- A QUEEN DEFENDED BY ONLY ONE MINOR IS LOST TO A MINOR: queen for bishop, no compensation. T57R3 15...Qc5?? 16.Bxc5! Bxc5 17.Qxc5. Before any queen move list his attackers of the square AND their piece value.
- HIS PAWN TWO SQUARES FROM MY BACK RANK IS A FORK MACHINE (T55R2 8...d3 9.O-O? ...Bg4 10.Ne1?? dxe2! forked Qd1+Rf1, mate m13). Name that pawn's two capture squares every move.
- A PIECE GUARDED ONLY BY MY QUEEN IS LOST TO HIS QUEEN - AND SO IS IT WHEN HIS PIECE ALSO GUARDS THE RECAPTURE SQUARE (T54R1 11...Bc5?? Qxc5; T55S2G1 12...Bc5?? my Nc6 stood between Qc7 and c5; T57R4 28...Bb7 'covered' by Qa7/Qb8: 30.Qxb7! Qxb7 31.Nxb7 = bishop for a pawn). Before trusting a one-queen guard, name HIS guards of the recapture square.
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST, CHECKS AND ROOKS INCLUDED (T50R3 44...Ra4+?? bxa4; T56R1 37...bxa6 won his rook). A PAWN I ATTACK TWICE STILL CAPTURES (T55R3 24.Qd4?? cxd4). A PAWN THAT JUST ADVANCED OR CAPTURED OWNS ITS NEW SQUARES.
- AN OPEN FILE + HIS ROOK = MY PIECE THERE IS FREE (T53R3 14...Bf5?? Rxf5); the mirror wins for me (T55 27...Nxc4! R for N).
- ROOK TAKES A PAWN: WALK EVERY ENEMY BISHOP DIAGONAL TO THAT PAWN'S SQUARE, even remote (T57R1 21...Rxa2?? 22.Bxa2 - Bd5 covered a2).
- THE MOVING PIECE ABANDONS ITS DUTY: name what it guarded (T52R3 20...Bb7?? Nd7 to Rxd7). Answer an attacked piece before any quiet move or castle.
- MY OWN UNIT ON THE RANK SCREENS MY ROOK: T57R2 10.Ne1?! put the knight between Rf1 and Qd1; 11.dxe3?? Qxd1. T57R3 my d4-pawn made Rxf4 illegal. Before a knight reroute or rook lift walk the rank AND the file to its destination.
- A CAPTURE THAT UNSCREENS A LINE RE-ARMS THE PIECE BEHIND IT (T50R4 14...Bxe5??; T51 Final 14...f6??).
- A ROOK CHECK NEAR MY KING: block on a DIFFERENT rank from my queen (T52 Final 21.Be3? Rxe3+).
- HIS KNIGHT IN MY CAMP: attack it with pieces; no pawn pushes that open lines to my king, no side grabs (T52 Final 16.f4? Nh5; T56R2 17.Qc1? ...Nxe3!).
- Qg3 OR Qg4 + a bishop reaching e5/f6/h6 = Qxg7#: never take on e5 then (T48 Final 13...dxe5??); ...h6?? met 12.Bxh6! (T54R3). AND ...O-O?? is the same hook when his queen is on g4: g7 is PINNED to Kg8, so ...gxh6 is illegal and 10.Bh6! Qxg7# (T57 Final 9...O-O?? 10...Qc7?? 11.Qxg7#). Keep the king on e8, meet Qg4 by removing her g-file aim, and never castle until g7 has a PIECE guard and her queen is off g4.
- QUEEN DESTINATION SWEEP: walk every enemy knight jump, bishop diagonal and pawn capture square onto her square, and her own path. A queen on a square his queen attacks needs a named recapturer (T56R1 29...Qe4?? 30.Qxe4); HIS unguarded queen on an open line is free (T56R1 32...Bxd7); MY queen in front of her king on an open file is pinned (T51R1 21.Rg3!).
- A QUEEN ON d4/e3 IN FRONT OF HIS c5-PAWN MUST SEE THE ...d4 PUSH: T56S2G1 12.Qd4?! ...c5 14.Qe3?? ...d4! forked Qe3+Nc3. Before Qd4/Qe3/Qc4 list ...c5, ...cxd4, ...d4; keep an exit square.
- A ROOK PINNED ON A DIAGONAL TO MY KING IS FREED BY HITTING THE PINNER (T55S2G1 ...Ne7 attacked Qd5).
- DOWN A PIECE OR MORE v SF: guard every unit, fortress, hunt ONE freeing trade early (T54R1's 60-move fortress still lost m67).

## Endings, king safety, conversion
- UP A QUEEN OR MORE: PROGRESS EVERY MOVE, NEVER A REPETITION, AND NO PAWN GRABS WITH HER. T55R5.2 queen checks until his king shuffled back = THREEFOLD DRAW; count the position I am about to repeat a third time. T56R1 closed it right: 51...Qd7 covering a7/b7/c8, 52...Rc8#. T56R3 Q+2R v bare K: Qf1+/Qf2+ drove Kh1, Qg3 covered g1/g2/h2, Rf1#. T56R5.2 30...Qe1+ 31.Bf1 Qxf1#. DOWN A QUEEN v SF, THREEFOLD IS THE SAVE (T57R2). The queen behind a bare 8th rank mates at once (T57R3 26.Qc8#).
- MATE LABEL: do not write '#' until the move is actually CHECK. T56R3 27...Qxg3 vs Kh1 was not check; Rf1# came later. Name the checking line and every flight.
- h6 IS BANNED WHILE HIS g7-PAWN IS HOME: T55R5.3 20.Qxh6?? gxh6; T50R2 16.Qh6??.
- A PAWN THAT TAKES A PIECE IS THE CHEAPEST ROOK ON THE BOARD: T55R5.3 29.cxd7! took a rook, 30.d8=Q safe.
- MY Kg8 WITH AN EMPTY f8/e8 = BACK-RANK MATE (T54S1G1 20.Qd8#). Keep a rook home or play h6.
- HIS Qf6 + A BISHOP REACHING f2, MY Kg1, f2 HOME = ...Qxf2# (T55R2 m13). f2 needs a second guard once queens are on.
- KING ON h1 + HIS QUEEN ON g3 = ...Re1#; MY Qg3 + Rf1# is the mirror (T56R3); MY ...Bb7 + HIS Kg1 = Qxg2# (T51S2G1).
- Q+R v bare K: defended non-adjacent checks, walk the king up, never park the rook where his king reaches it, stalemate check each move.
- TWO BISHOPS v A LONE ROOK + PAWNS: bishops on mutual support, one covers the pawn his rook eyes; win with a protected pawn wedge (T57R1 20.Bd5 covered a2, 21...Rxa2?? 22.Bxa2; e-pawn plus g/f wedge, Qh6#).
- UP A ROOK / 2R v R: take the first clean rook trade; rank-2/3 rook checks drive his king off his pawns, my king walks up, rook to the 7th/8th, collect pawns, never take a pawn his king guards, no check a pawn takes (...Ra4+?? bxa4).
- UP R+B v BARE KING: rook freezes his pawns, bishop escorts the passer, promote with the rook still covering g1.
- LEVEL R+B v R+B: the repetition draw is fair. TWO ROOKS v QUEEN: draw by blockade, not raids (T49R3).
- UP MATERIAL WITH QUEENS ON: every unit guarded by a PIECE, not only the queen; his queen+minor battery takes queen-guarded pieces off (T57R4 Bb7).

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock. T56R2: 15-40 s a move, 55 min left at mate. T57R3 57 min left at mate; long thinks on quiet queen moves buy nothing. T57R4: 5-20 s a move, 47 min left when he flagged at 2 min - banking clock won a game where I was down material. T58: 1-4 s a move, 55 min left at forfeit while GLM spent 15 min on 13.Qe2 and 14.e4.

## Opening: English (W v 1...e5; B v 1...Nf6 reversed QGD)
- W: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 (9 plies) - the squeeze setup.
  - vs ...Nxc3/...Bd6 symmetric (T55R5.3 WIN v GLM on time; T57R1 WIN v GLM): bxc3, Nf3, O-O, d4, Be3, Qd2, Rad1 = two bishops and a broad centre; d5 later, after Qd2/Re1. In the ending keep bishops mutually supporting and covering his rook's targets (Bd5), then the e-pawn plus g/f wedge, Qh6#.
  - vs ...Nb6 (T54R2 WIN v GLM): Nf3, Nc6, O-O, Be7, d3, then Be3/Qd2/Rc1/Rfd1; his c7 is a fork target (17.Nb5!).
- Reversed QGD build (both colours): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4). Keep ...c6 (or ...Ne4) before ...c5.
  - T56R3 WIN v GLM: 9.Nd4 hit Bf5, ...Bg6 retreat held; his loose Ne6 fell to fxe6, Be4 to dxe4, Qxd5+ to cxd5.
  - T56R5.2 WIN v GLM: 12...c5 guarded by Nd7+Be7; his 13.Bxc5?? Nxc5, then 17...Nxd2 won his queen; Q+R converted m31.
  - T58 v GLM (WIN on forfeit): White played b3/Bb2/Bg2, e3/d3, Nc3/Qd2/Rad1/Qe2. Level to m13; my ...c5 (guarded by Bb7+Nbd7), then ...dxe4, after dxe4 the freeing ...e5 (Nxe5 Nxe5 Bxe5 Qxe5 wins a piece). When its queen left e4 (18.Qd2) 18...Bxe4 won a free pawn. My ...h6 luft there was needless. Same build works; keep every unit guarded and bank clock.
  - W v SF's clamp (5...d4): 6.Nb1 right, then e3 EARLY before b3, meet ...Nc3 with Qe1, never trade Bg2 for a knight (T56R2). T57R2: no knight on e1/d1 while Qd1 and Rf1 share the rank (10.Ne1?! 11.dxe3?? Qxd1). Do NOT push d4 into his ...c5 (T56S2G1 8.d4).

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4/Qd2/Rad1 (White) or as Black ...cxd4/...Nf6/...e6/...Be7/...O-O/...Qc7/...a6 then ...b5/...Bb7/...Rfc8.
- AS BLACK the build is sound; ...d5 only when e6 recaptures. T56R1: 12...f6?? let 13.Bxd5+ and exf6; the f6 strike needs d5 defended AND g7 covered.
- T57R4 (WIN on time v mirror): ...Nb4/...Bc5 hitting Be3 worked (13...Bc5! 14.Bxd5?? Bxe3+ won a piece) but 12...Nb4? was loose once his Nf5 arrived; with a4+b5 tension ...bxa4?! hands him the a-file and an active rook. THE c8-BISHOP ON b7 WITH QUEENS ON IS A TARGET: keep a PIECE on b7 or leave the bishop home.
- AS BLACK ...b5 needs a guard first (...a6/...Bb7), else Nxb5! (T51R3). His e5 hitting Nf6: never ...Ne8 with my a8-rook home (Nc7 forks) - ...Nd5 or ...Nh5.
- AS BLACK keep the f6-knight and the queen guarded (T53R1 16...Rfd8?? exf6; 20...Kg7?? Bxc7).
- T53R3: with HIS d-pawn passed on d5, c6/e6 are banned for every piece AND the queen; ...Qd6 blockade is fine.
- WHITE CLAMP WIN: e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then the f5-f6 wedge, Bxf6 and exf6!. Ban premature f4-f5.
- AS BLACK an in-between CHECK (T49R4 13.Nxe7+!) beats resolving a queen attack.

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies): his Ng4 is GUARDED by Bc8 through d7-e6-f5; answer 9.Nxc6! bxc6 10.Bg5, NEVER Qxg4 (T49R2).
- King safety first after ...Qa5/...Rb8; no f4 while his knight reaches h5/f4; no a7 grab with his knight in my camp (T52 Final 18.Bxa7?).
- T53R2 v SF19: O-O?! Be5! Bd4? Bxh2+! then ...Qh4/...Bg1+ mates - count ...Bxh2+ before castling.

## Opening: Taimanov as BLACK v Stockfish
- 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies; 7.e5 Nd5 8.Qf3 transposes). ...Nxc3 hands him c3+d4+e5 - only for a concrete reason.
- 7.Ndb5 Qb8! is the only good retreat. With queens on, do NOT open the centre and never take on e5; ...f6 only with his Bf4 off the c7 diagonal.
- T57 Final (L m11): in the 7.Bd3 Be7 8.e5 Nd5 line, 9.Qg4! is the sting. Do NOT answer ...O-O: 9...O-O?? 10.Bh6! Qc7?? 11.Qxg7#. The g7-pawn is PINNED to Kg8 by Qg4, so ...gxh6 is illegal. Meet Qg4 by removing her g-file aim and keep the king on e8; no castle until g7 has a PIECE guard and her queen is off g4.
- T54S1G1 (L m20): 11...Bd6?? exd6 and 12...Qc7?? dxc7 handed bishop AND queen, 20.Qd8#. T54R3 (L m13): 11...h6?? 12.Bxh6! With his queen on g3 and a bishop reaching h6, ...h6 is a mating hook: ...f5, a PIECE on g7, or the queen trade. King on e8 makes Bf8 g7's only guard.

## Opponents
- Stockfish 19 (depth 4): instant. Punishes loose pieces, hidden defenders, unguarded c6 (Bxc6!), a kicked Ng4, f6 on his e5-pawn's capture square, ...f6 met by exf6, ...h6 met by Bxh6. T55R2: 5...d4 / 8...d3 clamp, ...Bg4, the dxe2 pawn fork, ...Qxf2# m13. T56R2: the early ...d4 clamp plus a knight tour (...Nc3/...Nb4/...Nc2/...Nxe3/...Nxg2) won pawns and Bg2. T57R2: 5...d4 again; 10.Ne1?!/11.dxe3?? lost my queen to ...Qxd1. T57 Final: after ...bxc6/...Be7/...Nd5, 9.Qg4! punished 9...O-O?? with 10.Bh6! 11.Qxg7# (g7 pinned).
- GLM 5.3 Flash: as White the English/reversed QGD (b3/Bb2 or symmetric), as Black the Taimanov; sound build but careless with piece safety. T56R3/R5.2/T57R1/T58 (my four 1-0): it hands knight, bishop, queen and rook to plain captures and to pawn takes (Ne6?? fxe6, Bc5?? Bxc5, Rxa2?? Bxa2, 17.Qd2?? Nxd2, 18.Qd2?? Bxe4 free pawn), shuffles in lost endings. ITS CLOCK SELF-DESTRUCTS: 13.Qe2 15:11, 14.e4 15:22 in T58, forfeited with 5:43 v my 55:51. Take every loose unit and queen; convert without waiting; never an empty or illegal reply.
- DeepSeek V4.1 Flash (mirror): solid Taimanov/English both colours, converts without gifts, up to 8 illegal tries/game. T54R1 up a bishop it walked Kf2-e3-d4-e5 and mated N+B m67; T55R3 beat me off my 24.Qd4?? cxd4; T56S2G1 played ...c5/...d4! forking Qe3+Nc3. T56R1 (my 1-0 as Black): its 32.Qd7?? Bxd7 and 37.Ra6?? bxa6 gave the game back. T57R3 (my 0-1 as Black): level Taimanov, then my 15...Qc5?? walked her onto his Bd4 (queen for bishop) and Q+2R mated 26.Qc8#. T57R4 (my 1-0 as Black on time): level Taimanov, ...Bc5!/...Bxe3+ won a piece, then I handed the b7-bishop back to 30.Qxb7; he flagged 2 min vs my 47 - bank clock, guard every unit by a PIECE, no illegal concern remains my own.
- Expect the ...c5/...d4 fork when my queen sits on d4/e3.

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record
- T47-T55 v SF19: mated off ONE loose move each. Wins T50 3rd, T51R1 (21.Rg3!), T51S2G1, T52R2/R3, T53S2G1, T54R2, T54 3rd, T55R1, T55R5.3; losses T53 Final, T54R1/R3/S1G1, T55R2/R3/S2G1; T55R5.2 draw after winning her queen.
- T56R1 1-0 v mirror (B Taimanov): 12...f6?? cost a pawn but his 32.Qd7?? Bxd7 and 37.Ra6?? bxa6 returned the game; 52...Rc8#.
- T56R2 0-1 v SF19 m33 (W English ...d4 clamp): 6.Nb1 right, then b3/Bb2/e3 allowed the knight tour; 18.Re1? traded Bg2. 55 min left.
- T56R3 1-0 v GLM (B English reversed QGD): his Ne6??, Be4??, Qxd5+??, Rxd7??, Re1?? gave knight, bishop, queen and rook; Rf1# after a false 'Qxg3#' note.
- T56S2G1 0-1 v mirror (W English reversed QGD): 8.d4 into his ...c5, 12.Qd4?!, 14.Qe3?? ...d4! forked Q+N; lost R+B+3P at m56. Keep the queen off d4/e3 while his c5-pawn lives.
- T56R5.2 1-0 v GLM (B English reversed QGD): 12...c5 defended by Nd7/Be7; his 13.Bxc5?? Nxc5, 17...Nxd2 won his queen; Q+R m31.
- T57R1 1-0 v GLM (W English symmetric): his Nxd4?? Bxd4, Bc5?? Bxc5, Rxa2?? Bxa2; B+B converted with e-pawn, king walk, g/f wedge, Qh6#. 64 min left.
- T57R2 1/2 v SF19 (W English, 5...d4 clamp): 6.Nb1/e3 correct, then 10.Ne1?! screened Rf1-d1 and 11.dxe3?? Qxd1; down a queen I forced a threefold with Bb8/Be5 vs Rd7/Rd5.
- T57R3 0-1 v mirror (B Taimanov): sound to 14...Bb7; 15...Qc5?? on Bd4's square = queen for bishop, then his Q+2R mated 26.Qc8#. One illegal Rxf4 through my own d4-pawn. A queen defended by one minor is lost.
- T57R4 1-0 v mirror (B Taimanov, he flagged): ...Bc5!/...Bxe3+ won a piece, but 28...Bb7 was indefensible with queens on (30.Qxb7) and 4 illegal tries on quiet queen retreats. Won on clock 47 min v 2.
- T57 Final 0-1 v SF19 m11 (B Taimanov): 8...Nd5 9.Qg4! 9...O-O?? 10.Bh6 Qc7?? 11.Qxg7#; g7 was pinned to Kg8 so ...gxh6 illegal. Keep king e8, remove her g-file aim, g7 piece-guarded before castling.
- T58R1 1-0 v GLM (B English reversed QGD, forfeit): level to m17; its 13.Qe2/14.e4 15-min thinks and 18.Qd2 5:01 left it 5:43 v my 55:51; 18...Bxe4 won a free pawn; 14.e4 dxe4 15.Nxe4 Nxe4 16.dxe4 e5 all sound. No illegal tries of mine.
