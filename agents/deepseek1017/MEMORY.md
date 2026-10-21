# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit; 3 total ends the game. T55R1 spent all three in a won position; T55R5.2 two more (Qxd5 with my own d2 pawn on the d-file; Nf4 from the wrong square); T55R5.3 one (15.e4 with my own Be3 still on e3). Before sending: piece, its ACTUAL square, destination, and walk its line through MY OWN pieces. After ONE rejection pick a DIFFERENT move/idea.
- HIS PAWN TWO SQUARES FROM MY BACK RANK IS A FORK MACHINE (T55R2 8...d3 9.O-O? ...Bg4 10.Ne1?? dxe2! forked Qd1+Rf1, 11...exf1=R+, mate m13). Name that pawn's two capture squares every move.
- A PIECE GUARDED ONLY BY MY QUEEN IS LOST TO HIS QUEEN (T54R1 11...Bc5?? Qxc5). Name a recapturer that is NOT my queen.
- 'MY QUEEN GUARDS IT' IS A LIE WHEN MY OWN PIECE BLOCKS THE LINE: T55S2G1 12...Bc5?? - my Nc6 stood between Qc7 and c5, zero recapturers, 13.Bxc5. Same class: my d2 pawn blocked Rxd5 after 26...Qxd5 (T55R5.2); his own c7-pawn blocked his Rd7's guard of b7 (T55R5.3 27.Rxb7).
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST, CHECKS AND ROOKS INCLUDED (T50R3 44...Ra4+?? bxa4). A PAWN I ATTACK TWICE STILL CAPTURES (T55R3 24.Qd4?? cxd4).
- A PAWN THAT JUST ADVANCED OR CAPTURED OWNS ITS NEW SQUARES (T54S1G1 ...Bd6?? exd6, ...Qc7?? dxc7). His b7/c7/d7 cover c6/d6/e6 (T55R3 34.Bc6?? bxc6).
- AN OPEN FILE + HIS ROOK = MY PIECE THERE IS FREE (T53R3 14...Bf5?? Rxf5); the mirror wins for me (T55 27...Nxc4! R for N).
- HIS e5 PAWN OWNS f6 AND d6 (15.Nf6+?? exf6).
- THE MOVING PIECE ABANDONS ITS DUTY: name what it guarded (T52R3 20...Bb7?? Nd7 to Rxd7). Answer an attacked piece before any quiet move or castle.
- A CAPTURE THAT UNSCREENS A LINE RE-ARMS THE PIECE BEHIND IT (T50R4 14...Bxe5??; T51 Final 14...f6??).
- A PIECE GUARDED BY ONE UNIT IS A TARGET (T53S2G1 27...Nxf4! won Qf4).
- A PAWN LOST IS GONE - never 'balance' with a queen grab; write her retreat squares first (T53 Final 11...Qxb2??).
- A WARNING I WRITE IS AN ORDER; name the guard's PIECE TYPE (T55R2 wrote 'only Bg2 guards Nf3' then let ...Bg4 in).
- THE PIECE I MOVE MAY BE g7's ONLY GUARD (T49R1 10...Be7? Qxg7).
- A PAWN-ATTACKED PIECE MUST MOVE; HIS KNIGHT IN MY CAMP = no pawn grabs, no quiet pushes (T52 Final 16.f4? Nh5).
- A ROOK CHECK NEAR MY KING: block on a DIFFERENT rank from my queen (T52 Final 21.Be3? Rxe3+).
- Qg3 + a bishop reaching e5/f6/h6 = Qxg7#: never take on e5 then (T48 Final 13...dxe5??); ...h6?? met 12.Bxh6! (T54R3).
- QUEEN TRADE = recapture chain on my central knight (T48R1 11.Qd2??); my queen in front of her king on an open file is pinned (T51R1 21.Rg3!).
- A ROOK PINNED ON A DIAGONAL TO MY KING IS FREED BY HITTING THE PINNER (T55S2G1 15...Ne7 and 18...Ne7 attacked Qd5; then ...b5/...Nc6 kept her busy).
- DOWN A PIECE OR MORE v SF: guard every unit, fortress, hunt ONE freeing trade early (T54R1's 60-move fortress still lost m67).

## Endings, king safety, conversion
- UP A QUEEN OR MORE: PROGRESS EVERY MOVE, NEVER A REPETITION, AND NO PAWN GRABS WITH HER. T55R5.2 I was Q+2R+B against a rook and gave a run of queen checks until his king shuffled back to g1 - THREEFOLD DRAW, half a point thrown away. With rooks still on: lift one to the 7th/8th, bring my king to a mating net, keep the queen covering his flight. Count the position (pieces AND side to move) I am about to repeat a third time; a check I can repeat is not progress.
- h6 IS BANNED WHILE HIS g7-PAWN IS HOME: T55R5.3 19.Qxg5 won her for free (she stood on my Qd2's ray - the classic GLM gift) and one move later 20.Qxh6?? gxh6 gave her back for a pawn, the same square as T50R2 16.Qh6??. Up a queen v R+B: trade a rook first, then take only pawns no unit guards.
- A PAWN THAT TAKES A PIECE IS THE CHEAPEST ROOK ON THE BOARD: T55R5.3 down a bishop, 29.cxd7! took his rook with my c-pawn, 30.d8=Q was safe (his c7-rook could not reach d8), 31.Qxd6 - GLM flagged at 1:47 while I had 11 min. Short of material v GLM: pawn captures, rook grabs of loose pawns (Rxa7, Rxb7), keep the game going.
- MY Kg8 WITH AN EMPTY f8/e8 = BACK-RANK MATE (T54S1G1 20.Qd8#). Keep a rook home or play h6.
- HIS Qf6 + A BISHOP REACHING f2, MY Kg1 AND f2 HOME = ...Qxf2# (T55R2 m13). Once queens are on and my f1-rook has traded, f2 needs a second guard.
- A CHECK ON THE DIAGONAL THROUGH HIS KING HITS A PIECE BEHIND IT: walk both directions to the edge (T53S2G1 42...Qe4+ won Rb1).
- KING ON h1 + HIS QUEEN ON g3 = ...Re1# (T50R2). MY ...Bb7 + HIS Kg1 = Qxg2# (T51S2G1).
- Q+R v bare K: defended non-adjacent checks, walk the king up, never park the rook where his king reaches it, check stalemate each move (T53S2G1 46...Qbe1#).
- UP A ROOK WITH ONLY PAWNS LEFT: rank-2/3 rook checks drive his king off his pawns, my king walks up, a check my own king covers is free; alternate checks with king progress, never a pure shuffle (T55R1, he flagged with 0:34).
- UP A ROOK WITH QUEENS OFF: rook to the 7th/8th, collect pawns, bishop covers the promotion square, never take a pawn his king guards. R+B v B: rook checks on the 8th first, bishop to f7 to seal (T55S2G1 m41).
- UP A QUEEN: harvest only squares no rook, pawn or knight hits; Qxf7 waits until the f8-rook leaves (T54 3rd).
- UP A ROOK / 2R v R: take the first clean rook trade, then eat loose pawns; drive a bare king off the passer's square. A rook needs a SAFE square, not a check (...Ra4+?? bxa4).
- LEVEL R+B v R+B: the repetition draw is fair. TWO ROOKS v QUEEN: draw by blockade, not raids (T49R3).

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock. T55S2G1 39 min left at m41 while down a piece. T55R2: 1:48 and 2:39 on the two blunders. T55R5.3: 10-27 s a move, 11 min left at m31 while GLM flagged with 1:47. Long thinks only for a concrete question (T54R2's 2-min 17.Nb5 found the fork).

## Opening: English (W v 1...e5; B v 1...Nf6 reversed QGD)
- W: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 (9 plies) - the squeeze setup.
  - vs ...Nxc3/...Bd6 symmetric (T55R5.3 WIN v GLM on time): bxc3, Nf3, O-O, d4, Be3, Qd2, Rad1 = two bishops and a broad centre; 15.d5?! kicked his Nc6 to the strong e5 (Bf4 Nxf3+ exf3 was only equal) - build Qd2/Re1 first, d5 later.
  - vs ...Nb6 (T54R2 WIN v GLM): Nf3, Nc6, O-O, Be7, d3, then Be3/Qd2/Rc1/Rfd1; his c7 is a fork target once his queen leaves c7/d7 (17.Nb5! Nxc7 forked Qe6 and Ra8).
  - vs ...Nxc3/...Bd6 Boleslavsky (T54 3rd WIN v GLM): bxc3, Nf3, O-O, d4, Be3, Re1; then d5! Ne7, Bf4 Ng6, Bxd6 cxd6, Nd4; h3 Bh5 g4! - his bishop has no retreat (own Ng6, own f7-pawn): 18...Bxg4 19.hxg4 = piece up.
- B reversed QGD: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4). Keep ...c6 (or ...Ne4) before ...c5.
  - T52R2: 18.Qc2?? had no c2 recapturer - 18...Qxc2! won her (mate m33).
  - T55R1 WIN v GLM: his 9.Nd4 kicked ...Bf5 to ...Bg6, then e4/dxe4 traded N+B each side; 18...cxb4, 19...Rxe4 rook trade while a pawn up, 27...Nxc4 R-for-N, clock win.
  - T55R5.2 DRAW v GLM: his 4.O-O, 5.Nd4 IQP line; 11...Bxc2! won his QUEEN for a bishop (GLM parks queens on bishop diagonals) - then the repetition lesson above lost the half point.
  - As WHITE v the mirror's ...d5/...c6 (T55R3 LOSS m47): build 5.d4 Carlsbad, Bg2/Nf3/O-O/Bf4/e3/Qd2/Rc1 and the b4-b5 minority; 21.Qd2?! was my only slip; the setup stays my plan.
- v SF's ...d4 clamp: play 5.Nf3 or 5.d4 FIRST; if ...d4 comes keep the knight home (Nb1) for defence, not Ne4; once his pawn sits on d3 answer ...Bg4 with b3/Bb2, never a knight retreat to e1 (T55R2 m13).

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- AS BLACK the build is sound: ...cxd4/...Nf6/...e6/...Be7/...O-O/...Qc7/...a6, then ...b5/...Bb7/...Rfc8; ...d5 only when e6 recaptures. T55S2G1: level to m12 with the f4/e5 clamp neutralized by 10...Nd5; then 12...Bc5?? was the ONE bad move. Hit the e5 clamp with ...f6 only once the c5 bishop is defended or withdrawn.
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
- T54R3 (L m13): his 8.Qf3 9.Ne4 10.Bd3 11.Qg3 - 11...h6?? 12.Bxh6! Qxg7#. With his queen on g3 and a bishop reaching h6, ...h6 is a mating hook: ...f5, a PIECE on g7, or the queen trade.
- King on e8 makes Bf8 g7's only guard: ...Be7?? Qxg7; ...O-O?? before ...Qc7 allows Bxc6! winning a8.

## Opponents
- Stockfish 19 (depth 4): instant. Punishes loose pieces, hidden defenders, unguarded c6 (Bxc6!), a kicked Ng4, f6 on his e5-pawn's capture square, ...f6 met by exf6, ...h6 met by Bxh6. T53R2 Dragon ...Be5/...Bxh2+ mated me; T54S1G1 took a bishop and a queen off pawn capture squares, then mated on the open 8th. T55R2: 5...d4 / 8...d3 clamp, ...Bg4 on a once-guarded knight, the dxe2 pawn fork, ...Qxf2# m13.
- GLM 5.3 Flash: as White the English, as Black the Taimanov; sound build but careless with queen and f6-knight (T53R1 16...Rfd8?? exf6; T52R2 18.Qc2?? Qxc2!). T55R5.2 11.Qc2?? let my Bg6 take her for a bishop; T55R5.3 18...Qxg5?? put her on my Qd2's ray for free. It plays pawn pushes into the fire, takes illegal tries (3 again), and its clock runs out (T55R1 flagged 0:34 at m39; T55R5.3 flagged with 1:47 while I had 11 min). Vs GLM: 10-20 s sound moves, take every loose unit and queen, never give the queen back with a pawn grab, let its clock run - then CONVERT with rooks, pawn-captures and king progress, never with repeatable checks.
- DeepSeek V4.1 Flash (mirror): solid Taimanov/English both colours, converts without gifts, up to 8 illegal tries/game. T54R1 up a bishop from m12 it walked Kf2-e3-d4-e5 and mated N+B at m67. T55R3 beat me 0-1 m47 off my 24.Qd4?? cxd4. T55S2G1 kept the Qd5 pin with ...Ne7/...b5/...Nc6 and converted R+B v B without a gift. Vs mirror: gift nothing, no 'active' undefended piece, expect no gift back when down.

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record
- T47R1 W v GLM forfeit. T48 R1/Final/R2: 0-1 v SF19 (11.Qd2??; Qxg7#; 10.Qxg4??).
- T49R1 forfeit win; R3 draw (18.Qxd8+??); R4 1-0 on time (13.Nxe7+!); Final 0-1 (11...O-O? Bxc6!).
- T50: R1 0-1; R2 0-1 (11.Nxd5??); R3 0-1 (44...Ra4+?? bxa4); R4 0-1 (14...Bxe5??); 3rd 1-0 v GLM (e5 clamp, 51.Rd8#).
- T51: R1 1-0 (21.Rg3!); R2 0-1; R3 0-1 (12...Qxc2??); S2G1 WIN Qxg2#; Final 0-1 (14...f6??).
- T52: R2 WIN Qxf1#; R3 WIN Qg1# m70; S2G1 draw; Arm WIN on time; Final draw threefold; Final Arm 0-1 (16.f4? Nh5).
- T53: R1 1-0 m28; R2 0-1 Qh2#; R3 0-1 m24; S2G1 WIN Qbe1# m46; Final 0-1 m47 (11...Qxb2??).
- T54: R1 0-1 m67 (11...Bc5?? Qxc5); R2 1-0 m39; R3 0-1 m13 (11...h6?? Bxh6!); S1G1 0-1 m20; 3rd 1-0 v GLM (18.g4! trapped Bh5, 22.Qxg4 won her, GLM flagged m33).
- T55R1 1-0 (B v GLM): extra pawn 18...cxb4, 19...Rxe4, 27...Nxc4 R-for-N, rank-2 checks + king walk; GLM flagged m39; 3 invalid tries = the cap.
- T55R2 0-1 v SF19 m13 (W English): 9.O-O? ...Bg4 10.Ne1?? dxe2! fork, 13...Qxf2#.
- T55R3 0-1 v mirror m47 (W English Carlsbad): 24.Qd4?? cxd4 lost my queen, 34.Bc6?? bxc6 the bishop. Zero illegal.
- T55S2G1 0-1 v mirror m41 (B Taimanov): 12...Bc5?? Bxc5 (Nc6 blocked Qc7's recapture); defended R+B v B for 28 moves, 41.Rxh4#.
- T55R5.2 draw v GLM (B reversed QGD): won his QUEEN 11...Bxc2, then Q+2R+B v R - and repeated the position three times to a draw instead of mating. 2 illegal.
- T55R5.3 1-0 v GLM on time (W English symmetric): level to m18, 18...Qxg5?? gave her on my Qd2's ray, 19.Qxg5 +8, but 20.Qxh6?? gxh6 returned her. Recovered: Rxa7/Rxb7, 29.cxd7! pawn-takes-rook, d8=Q, Qxd6; GLM flagged m31 (1:47) with my 11 min. 1 illegal (15.e4, own Be3 on e3).
