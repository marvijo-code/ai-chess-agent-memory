# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit; 3 total ends the game. Before sending: piece, its ACTUAL square, destination, and MY OWN occupant of every path square. After ONE rejection pick a DIFFERENT move/idea.
- HIS PAWN TWO SQUARES FROM MY BACK RANK IS A FORK MACHINE (T55R2 8...d3 9.O-O? ...Bg4 10.Ne1?? dxe2! forked Qd1+Rf1, mate m13). Name that pawn's two capture squares every move.
- A PIECE GUARDED ONLY BY MY QUEEN IS LOST TO HIS QUEEN, AND 'MY QUEEN GUARDS IT' IS A LIE WHEN MY OWN PIECE BLOCKS THE LINE: T54R1 11...Bc5?? Qxc5; T55S2G1 12...Bc5?? - my Nc6 stood between Qc7 and c5; T55R5.2 my d2 pawn blocked Rxd5.
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST, CHECKS AND ROOKS INCLUDED (T50R3 44...Ra4+?? bxa4; T56R1 37...bxa6 won his rook for a pawn). A PAWN I ATTACK TWICE STILL CAPTURES (T55R3 24.Qd4?? cxd4).
- A PAWN THAT JUST ADVANCED OR CAPTURED OWNS ITS NEW SQUARES (T54S1G1 ...Bd6?? exd6, ...Qc7?? dxc7). His b7/c7/d7 cover c6/d6/e6; his e5 covers d6/f6.
- AN OPEN FILE + HIS ROOK = MY PIECE THERE IS FREE (T53R3 14...Bf5?? Rxf5); the mirror wins for me (T55 27...Nxc4! R for N).
- THE MOVING PIECE ABANDONS ITS DUTY: name what it guarded (T52R3 20...Bb7?? Nd7 to Rxd7). Answer an attacked piece before any quiet move or castle.
- A CAPTURE THAT UNSCREENS A LINE RE-ARMS THE PIECE BEHIND IT (T50R4 14...Bxe5??; T51 Final 14...f6??).
- A PIECE GUARDED BY ONE UNIT IS A TARGET (T53S2G1 27...Nxf4! won Qf4).
- A PAWN LOST IS GONE - never 'balance' with a queen grab (T53 Final 11...Qxb2??).
- THE PIECE I MOVE MAY BE g7's ONLY GUARD (T49R1 10...Be7? Qxg7).
- HIS KNIGHT IN MY CAMP: attack it with pieces; no pawn pushes that open lines to my king, no side grabs (T52 Final 16.f4? Nh5; T56R2 17.Qc1? ...Nxe3!).
- A ROOK CHECK NEAR MY KING: block on a DIFFERENT rank from my queen (T52 Final 21.Be3? Rxe3+).
- Qg3 + a bishop reaching e5/f6/h6 = Qxg7#: never take on e5 then (T48 Final 13...dxe5??); ...h6?? met 12.Bxh6! (T54R3).
- A QUEEN MOVE ONTO A SQUARE HIS QUEEN ATTACKS NEEDS A NAMED RECAPTURER OF MINE THERE: T56R1 29...Qe4?? 30.Qxe4; T52R2 18.Qc2?? Qxc2. Mirror: HIS queen unguarded on an open line is free (T56R1 32...Bxd7). My queen in front of her king on an open file is pinned (T51R1 21.Rg3!).
- A ROOK PINNED ON A DIAGONAL TO MY KING IS FREED BY HITTING THE PINNER (T55S2G1 ...Ne7 attacked Qd5).
- DOWN A PIECE OR MORE v SF: guard every unit, fortress, hunt ONE freeing trade early (T54R1's 60-move fortress still lost m67).

## Endings, king safety, conversion
- UP A QUEEN OR MORE: PROGRESS EVERY MOVE, NEVER A REPETITION, AND NO PAWN GRABS WITH HER. T55R5.2 queen checks until his king shuffled back = THREEFOLD DRAW. Count the position (pieces AND side to move) I am about to repeat a third time. T56R1 closed it right: rook check cut the file, 51...Qd7 covering a7/b7/c8, Rc8#.
- h6 IS BANNED WHILE HIS g7-PAWN IS HOME: T55R5.3 20.Qxh6?? gxh6; same square as T50R2 16.Qh6??.
- A PAWN THAT TAKES A PIECE IS THE CHEAPEST ROOK ON THE BOARD: T55R5.3 29.cxd7! took his rook with my c-pawn, 30.d8=Q safe.
- MY Kg8 WITH AN EMPTY f8/e8 = BACK-RANK MATE (T54S1G1 20.Qd8#). Keep a rook home or play h6.
- HIS Qf6 + A BISHOP REACHING f2, MY Kg1, f2 HOME = ...Qxf2# (T55R2 m13). f2 needs a second guard once queens are on.
- A CHECK ON THE DIAGONAL THROUGH HIS KING HITS A PIECE BEHIND IT: walk both directions to the edge (T53S2G1 42...Qe4+ won Rb1).
- KING ON h1 + HIS QUEEN ON g3 = ...Re1# (T50R2). MY ...Bb7 + HIS Kg1 = Qxg2# (T51S2G1).
- Q+R v bare K: defended non-adjacent checks, walk the king up, never park the rook where his king reaches it, stalemate check each move (T56R1 50...Rc1+ cut, 51...Qd7, 52...Rc8#).
- UP A ROOK WITH ONLY PAWNS LEFT: rank-2/3 rook checks drive his king off his pawns, my king walks up; alternate checks with king progress, never a pure shuffle (T55R1, he flagged with 0:34).
- UP A ROOK WITH QUEENS OFF: rook to the 7th/8th, collect pawns, bishop covers the promotion square, never take a pawn his king guards.
- UP A ROOK / 2R v R: take the first clean rook trade, then eat loose pawns; a rook needs a SAFE square, not a check (...Ra4+?? bxa4).
- UP R+B v BARE KING: rook freezes his pawns, bishop escorts the passer, promote with the rook still covering g1, then mate (T56R1 34...gxf6 to 48...a1=Q+ with no gift).
- LEVEL R+B v R+B: the repetition draw is fair. TWO ROOKS v QUEEN: draw by blockade, not raids (T49R3).

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock. T56R2: 15-40 s a move, 55 min left at mate - the clamp loss was positional.

## Opening: English (W v 1...e5; B v 1...Nf6 reversed QGD)
- W: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 (9 plies) - the squeeze setup.
  - vs ...Nxc3/...Bd6 symmetric (T55R5.3 WIN v GLM on time): bxc3, Nf3, O-O, d4, Be3, Qd2, Rad1 = two bishops and a broad centre; 15.d5?! kicked his Nc6 to e5 - build Qd2/Re1 first, d5 later.
  - vs ...Nb6 (T54R2 WIN v GLM): Nf3, Nc6, O-O, Be7, d3, then Be3/Qd2/Rc1/Rfd1; his c7 is a fork target (17.Nb5!).
- W v SF's reversed-QGD clamp: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 d4 6.Nb1 Be7 7.Bg2 O-O 8.O-O c5 (16 plies). 6.Nb1 is right, but T56R2 showed the follow-up b3/Bb2/Nbd2/e3 fails: 11...Nc3! (fork Qd1+e2) forced Qe1, then ...Nd5/...Nb4!/...Nc2!/...Nxe3/...Nxg2 - a knight tour in my camp won pawns AND my Bg2. Fix: play e3 EARLY (before b3) to fix the pawn, meet ...Nc3 with Qe1 then hit it, and never trade Bg2 for a knight.
- B reversed QGD: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4). Keep ...c6 (or ...Ne4) before ...c5.

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- AS BLACK the build is sound: ...cxd4/...Nf6/...e6/...Be7/...O-O/...Qc7/...a6, then ...b5/...Bb7/...Rfc8; ...d5 only when e6 recaptures. T56R1: 10...Nd5 11...exd5 correct, then 12...f6?? let 13.Bxd5+ Kh8 14.exf6 and I was a pawn down; the f6 strike needs d5 defended AND g7 covered - use ...Bf8, ...g6/...f5 prep or the queen trade first.
- AS BLACK ...b5 needs a guard first (...a6/...Bb7), else Nxb5! (T51R3). His e5 hitting Nf6: never ...Ne8 with my a8-rook home (Nc7 forks) - ...Nd5 (count guards) or ...Nh5.
- AS BLACK keep the f6-knight and the queen guarded (T53R1 16...Rfd8?? exf6; 20...Kg7?? Bxc7).
- T53R3: with HIS d-pawn passed on d5, c6/e6 are banned for every piece AND the queen; ...Qd6 blockade is fine.
- WHITE CLAMP WIN (T50 3rd, T51R1, T53R1): e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then the f5-f6 wedge, Bxf6 and exf6!. Ban premature f4-f5.
- AS BLACK an in-between CHECK (T49R4 13.Nxe7+!) beats resolving a queen attack; before my queen leaves the 2nd rank check ...Qxc2/...Qxb2.

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies): his Ng4 is GUARDED by Bc8 through d7-e6-f5; answer 9.Nxc6! bxc6 10.Bg5, NEVER Qxg4 (T49R2).
- King safety first after ...Qa5/...Rb8; no f4 while his knight reaches h5/f4; no a7 grab with his knight in my camp (T52 Final 18.Bxa7?).
- T53R2 v SF19: O-O?! Be5! Bd4? Bxh2+! then ...Qh4/...Bg1+ mates - count ...Bxh2+ before castling.

## Opening: Taimanov as BLACK v Stockfish
- 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies; 7.e5 Nd5 8.Qf3 transposes). ...Nxc3 hands him c3+d4+e5 - only for a concrete reason.
- 7.Ndb5 Qb8! is the only good retreat. With queens on, do NOT open the centre and never take on e5 (14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5); ...f6 only with his Bf4 off the c7 diagonal.
- T54S1G1 (L m20): sound to 8...Nd5; 9.Qg4 forced ...Kf8; then 11...Bd6?? exd6 and 12...Qc7?? dxc7 handed bishop AND queen, 20.Qd8#. The Taimanov is good; pawn-capture-square discipline is what is missing.
- T54R3 (L m13): 11...h6?? 12.Bxh6! Qxg7#. With his queen on g3 and a bishop reaching h6, ...h6 is a mating hook: ...f5, a PIECE on g7, or the queen trade.
- King on e8 makes Bf8 g7's only guard: ...Be7?? Qxg7; ...O-O?? before ...Qc7 allows Bxc6! winning a8.

## Opponents
- Stockfish 19 (depth 4): instant. Punishes loose pieces, hidden defenders, unguarded c6 (Bxc6!), a kicked Ng4, f6 on his e5-pawn's capture square, ...f6 met by exf6, ...h6 met by Bxh6. T53R2 Dragon ...Be5/...Bxh2+ mated me; T54S1G1 took a bishop and a queen off pawn capture squares, then mated on the open 8th. T55R2: 5...d4 / 8...d3 clamp, ...Bg4 on a once-guarded knight, the dxe2 pawn fork, ...Qxf2# m13. T56R2: the early ...d4 clamp plus a knight tour (...Nc3/...Nb4/...Nc2/...Nxe3/...Nxg2) won pawns and my Bg2 - his clamp is a real plan, not just a pawn.
- GLM 5.3 Flash: as White the English, as Black the Taimanov; sound build but careless with queen and f6-knight (T53R1 16...Rfd8?? exf6; T52R2 18.Qc2?? Qxc2!). T55R5.2 11.Qc2?? let my Bg6 take her; T55R5.3 18...Qxg5?? put her on my Qd2's ray. It plays pawn pushes into the fire, takes illegal tries, and its clock runs out (T55R1 flagged 0:34 m39; T55R5.3 flagged with 1:47 while I had 11 min). Vs GLM: 10-20 s sound moves, take every loose unit and queen, never give her back with a pawn grab, let its clock run - then CONVERT with rooks, pawn-captures and king progress, never with repeatable checks.
- DeepSeek V4.1 Flash (mirror): solid Taimanov/English both colours, converts without gifts, up to 8 illegal tries/game. T54R1 up a bishop it walked Kf2-e3-d4-e5 and mated N+B at m67; T55R3 beat me 0-1 m47 off my 24.Qd4?? cxd4; T55S2G1 kept the Qd5 pin and converted R+B v B. T56R1 (my 1-0 as Black): its 32.Qd7?? Bxd7 and 37.Ra6?? bxa6 gave the game back. Vs mirror: gift nothing, no 'active' undefended piece; it DOES hand back a loose queen under pressure.

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record
- T47-T51 v SF19: mated off ONE loose move each. Wins: T50 3rd v GLM, T51R1 (21.Rg3!), T51S2G1, T49R4 on time.
- T52-T55: wins T52R2/R3, T53S2G1, T54R2, T54 3rd, T55R1, T55R5.3; losses T53 Final, T54R1/R3/S1G1, T55R2 (SF clamp fork m13), T55R3, T55S2G1; T55R5.2 draw after winning her queen.
- T56R1 1-0 v mirror (B Taimanov): 12...f6?? cost a pawn but his 32.Qd7?? Bxd7 and 37.Ra6?? bxa6 returned the game; 52...Rc8#.
- T56R2 0-1 v SF19 m33 (W English ...d4 clamp): 6.Nb1 right, then b3/Bb2/e3 allowed the ...Nc3/...Nb4/...Nc2/...Nxe3/...Nxg2 tour; 18.Re1? traded Bg2 and opened my king. 55 min left - not clock.
