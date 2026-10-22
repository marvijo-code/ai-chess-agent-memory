# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit; before sending walk piece, ACTUAL square, destination, MY OWN occupants. After ONE rejection pick a DIFFERENT move. T58 Final: 5 illegal tries in queen-check chains; check every king step against the queen's actual lines. T58 Arm: 0 illegal when every piece was named - keep that walk.
- QUEEN GRABS: name the piece on the landing square and walk HIS queen/bishop/rook lines and pawn captures to it. T58R3 22.Qxb5?? b5 was a PAWN, his Qe5 covered it. T58 Final 22...Qxb2?? 23.Rb1! 24.Rxb2 lost my queen. T58S2G1 16...Qxe5?? left me down B for P. Count material after forced queen trade BEFORE the grab.
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST, checks and rooks included (T50R3 44...Ra4+?? bxa4; T56R1 37...bxa6 won his rook). A PAWN I ATTACK TWICE STILL CAPTURES (T55R3 24.Qd4?? cxd4). A PAWN THAT JUST ADVANCED OR CAPTURED OWNS ITS NEW SQUARES. T58 Arm 23.Qg6?? hxg6: g6/g5 belong to the h7-pawn - name the pawn that hits every queen/bishop destination.
- A QUEEN OR PIECE GUARDED ONLY BY ONE MINOR/QUEEN IS LOST: T57R3 15...Qc5?? 16.Bxc5. T54R1 11...Bc5?? Qxc5. T55S2G1 12...Bc5?? T57R4 28...Bb7 'covered' by Qa7/Qb8: 30.Qxb7!.
- MINOR PIECES NEED THE KNIGHT-JUMP SWEEP TOO: T58 Arm 15.Be4?? Nxe4! (the f6-knight's square, nothing else guarded the bishop), 16.Nxe4 Nxd3! and SF was +6. Before ANY bishop/knight/rook move list every enemy knight jump onto the destination, not only for queens.
- HIS KNIGHT IN MY CAMP: attack it with PIECES; no pawn pushes that open lines to my king, no side grabs. T58 Arm 16...Nxd3 lived to 19...Ne1! 20...Nxf3+ (R for B): its jumps were e1/f2/b2/c1. Before a rook lift to f3 name the knight's jumps and what they hit. T52 Final 16.f4? Nh5; T56R2 17.Qc1? ...Nxe3!. KNIGHT DESTINATIONS: a pawn kick that sends it to a better square is a gift (T58R2 14.a3?! Nb4-d3!); a knight to b3/b6 with his queen on that file is lost (T58R2 17.Nb3?? Qxb3).
- HIS PAWN TWO SQUARES FROM MY BACK RANK IS A FORK MACHINE (T55R2 8...d3 9.O-O? ...Bg4 10.Ne1?? dxe2! forked Qd1+Rf1, m13). Name that pawn's two capture squares every move.
- AN OPEN FILE + HIS ROOK = MY PIECE THERE IS FREE (T53R3 14...Bf5?? Rxf5); the mirror wins for me (T55 27...Nxc4! R for N).
- ROOK TAKES A PAWN: WALK EVERY ENEMY BISHOP DIAGONAL TO THAT PAWN'S SQUARE, even remote (T57R1 21...Rxa2?? 22.Bxa2).
- THE MOVING PIECE ABANDONS ITS DUTY: name what it guarded (T52R3 20...Bb7?? Nd7 to Rxd7). Answer an attacked piece before any quiet move or castle.
- MY OWN UNIT ON THE RANK SCREENS MY ROOK: T57R2 10.Ne1?! put the knight between Rf1 and Qd1; 11.dxe3?? Qxd1. Before a knight reroute or rook lift walk the rank AND the file to its destination.
- A CAPTURE THAT UNSCREENS A LINE RE-ARMS THE PIECE BEHIND IT (T50R4 14...Bxe5??; T51 Final 14...f6??).
- A ROOK CHECK NEAR MY KING: block on a DIFFERENT rank from my queen (T52 Final 21.Be3? Rxe3+).
- Qg3/Qg4 + a bishop reaching e5/f6/h6 = Qxg7#: never take on e5 then (T48 Final 13...dxe5??); ...h6?? met 12.Bxh6! (T54R3). AND ...O-O?? is the same hook when his queen is on g4: g7 is PINNED to Kg8, so ...gxh6 is illegal and 10.Bh6! Qxg7# (T57 Final 9...O-O??). Keep the king on e8, remove her g-file aim, no SHORT castle until g7 has a PIECE guard and her queen is off g4. LONG castle is playable after ...g6: T58 Final 9...g6! 10...O-O-O; but before O-O-O check his Bg5/Bh6 line to d8 (16.Bxd8 won my d8-rook).
- QUEEN DESTINATION SWEEP: walk every enemy knight jump, bishop diagonal and pawn capture square onto her square, and her own path. HIS unguarded queen on an open line is free (T56R1 32...Bxd7); MY queen in front of his king on an open file is pinned (T51R1 21.Rg3!).
- A QUEEN ON d4/e3 IN FRONT OF HIS c5-PAWN MUST SEE THE ...d4 PUSH: T56S2G1 12.Qd4?! ...c5 14.Qe3?? ...d4! forked Qe3+Nc3. Keep an exit square.

## Endings, king safety, conversion
- UP A QUEEN OR MORE: PROGRESS EVERY MOVE, NEVER A REPETITION, AND NO PAWN GRABS WITH HER. T55R5.2 queen checks until his king shuffled back = THREEFOLD DRAW; count the position I am about to repeat a third time. T56R1 closed it right: 51...Qd7 covering a7/b7/c8, 52...Rc8#. DOWN A QUEEN v SF, THREEFOLD IS THE SAVE (T57R2; T58 Final: king and bishop mutually defended, legal shuffles, SF accepted at +8.4).
- MATE LABEL: do not write '#' until the move is actually CHECK. Name the checking line and every flight.
- h6 IS BANNED WHILE HIS g7-PAWN IS HOME: T55R5.3 20.Qxh6?? gxh6; T50R2 16.Qh6??.
- A PAWN THAT TAKES A PIECE IS THE CHEAPEST ROOK ON THE BOARD: T55R5.3 29.cxd7! took a rook, 30.d8=Q safe.
- MY Kg8 WITH AN EMPTY f8/e8 = BACK-RANK MATE (T54S1G1 20.Qd8#). Keep a rook home or play h6.
- HIS Qf6 + A BISHOP REACHING f2, MY Kg1, f2 HOME = ...Qxf2# (T55R2 m13). f2 needs a second guard once queens are on.
- KING ON h1 + HIS QUEEN ON g3 = ...Re1#; MY Qg3 + Rf1# is the mirror (T56R3); MY ...Bb7 + HIS Kg1 = Qxg2# (T51S2G1).
- Q+R v bare K: defended non-adjacent checks, walk the king up, never park the rook where his king reaches it, stalemate check each move. Q+2R (T56R3): Qf1+/Qf2+ drove Kh1, Qg3 covered g1/g2/h2, Rf1#.
- TWO BISHOPS v A LONE ROOK + PAWNS: bishops on mutual support, one covers the pawn his rook eyes; win with a protected pawn wedge (T57R1 20.Bd5, 21...Rxa2?? 22.Bxa2; e-pawn plus g/f wedge, Qh6#).
- UP A ROOK / 2R v R: take the first clean rook trade; rank-2/3 rook checks drive his king off his pawns, my king walks up, rook to the 7th/8th, collect pawns, never take a pawn his king guards, no check a pawn takes (...Ra4+?? bxa4).
- UP R+B v BARE KING: rook freezes his pawns, bishop escorts the passer, promote with the rook still covering g1. LEVEL R+B v R+B: the repetition draw is fair. TWO ROOKS v QUEEN: draw by blockade, not raids (T49R3).
- UP MATERIAL WITH QUEENS ON: every unit guarded by a PIECE, not only the queen (T57R4 Bb7).
- DOWN A QUEEN VS THE MIRROR: 35 moves of shuffling never flags him (T58R3 he mated at m57 with 3:32 left). Guard everything and stay legal, but the game was lost at the blunder, not saved by his clock.

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock. T56R2/R3, T57R3/R4, T58R1/R2/R3: 37-64 min left at the end every time. Never buy a scan with a long think; never rely on his flag.
- ARMAGEDDON AS WHITE IS THE TIGHT CLOCK (10 min): T58 Arm went 10:08 to 4:01 with 1:20 on Qc2, 54 s on Nc3, 47 s on Qf5 in a settled defence. 10-20 s a move there; spend the time on the destination sweep, not on the plan.

## Opening: English (W v 1...e5; B v 1...Nf6 reversed QGD)
- W: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 (9 plies) - the squeeze setup.
  - vs ...Nxc3/...Bd6 symmetric (T55R5.3 WIN v GLM on time; T57R1 WIN v GLM): bxc3, Nf3, O-O, d4, Be3, Qd2, Rad1 = two bishops and a broad centre; d5 later, after Qd2/Re1. In the ending keep bishops mutually supporting and covering his rook's targets (Bd5), then the e-pawn plus g/f wedge, Qh6#.
- Reversed QGD build (both colours): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4). Keep ...c6 (or ...Ne4) before ...c5.
  - T56R3 WIN v GLM: 9.Nd4 hit Bf5, ...Bg6 retreat held; his loose Ne6 fell to fxe6, Be4 to dxe4, Qxd5+ to cxd5. T56R5.2 WIN: 12...c5 guarded by Nd7+Be7, his 13.Bxc5?? Nxc5, 17...Nxd2 won his queen.
  - T58R1 v GLM (WIN on forfeit): its 13.Qe2/14.e4 15-min thinks left it 5:43 v my 55:51; 18...Bxe4 won a free pawn.
  - W v SF's clamp: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 d4 6.Nb1 Be7 7.e3 dxe3 8.fxe3 Na6 (16 plies). Then Bg2/O-O/d3; meet ...Nc3 with Qe1, never trade Bg2 for a knight, no d4 while ...c5 lives, answer ...Nb4 with a piece move, never a pawn kick. Do NOT push d4 into his ...c5 (T56S2G1, T58R2 11.d4). No knight on e1/d1 while Qd1 and Rf1 share the rank (T57R2).
  - T58 Arm (LOSS m30): that clamp build held but SF crept to +1; 11...Nb4 outpost, 12.Ne5/13.Nc3/14.Nc4 built an active knight, then 15.Be4?? Nxe4! lost a bishop (e4 is the f6-knight's square) and 16...Nxd3, 19...Ne1! 20...Nxf3+ cost the exchange; 23.Qg6?? hxg6 the queen. Nothing else was loose - the two destinations were the whole game.
  - T58R3 v mirror (LOSS m57): 12.Ne5 Nxe5 13.Bxe5! won a piece (his Nbd7 undefended), 18.exd5/19.dxe6! won a bishop; then 22.Qxb5?? threw it all. Convert without a queen grab.

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4/Qd2/Rad1 (White) or as Black ...cxd4/...Nf6/...e6/...Be7/...O-O/...Qc7/...a6 then ...b5/...Bb7/...Rfc8.
- AS BLACK the build is sound; ...d5 only when e6 recaptures. T56R1: 12...f6?? let 13.Bxd5+ and exf6.
- T57R4 (WIN on time v mirror): ...Nb4/...Bc5 hitting Be3 worked (13...Bc5! 14.Bxd5?? Bxe3+) but 12...Nb4? was loose once his Nf5 arrived; with a4+b5 tension ...bxa4?! hands him the a-file. THE c8-BISHOP ON b7 WITH QUEENS ON IS A TARGET: keep a PIECE on b7 or leave the bishop home.
- AS BLACK ...b5 needs a guard first (...a6/...Bb7), else Nxb5! (T51R3). His e5 hitting Nf6: never ...Ne8 with my a8-rook home (Nc7 forks) - ...Nd5 or ...Nh5.
- AS BLACK keep the f6-knight and the queen guarded (T53R1 16...Rfd8?? exf6; 20...Kg7?? Bxc7). With HIS passed d5, c6/e6 are banned for every piece AND the queen; ...Qd6 blockade is fine (T53R3).
- WHITE CLAMP WIN: e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then the f5-f6 wedge, Bxf6 and exf6!. Ban premature f4-f5. An in-between CHECK (T49R4 13.Nxe7+!) beats resolving a queen attack.

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies): his Ng4 is GUARDED by Bc8 through d7-e6-f5; answer 9.Nxc6! bxc6 10.Bg5, NEVER Qxg4 (T49R2).
- King safety first after ...Qa5/...Rb8; no f4 while his knight reaches h5/f4; no a7 grab with his knight in my camp (T52 Final 18.Bxa7?).
- T53R2 v SF19: O-O?! Be5! Bd4? Bxh2+! then ...Qh4/...Bg1+ mates - count ...Bxh2+ before castling.

## Opening: Taimanov as BLACK v Stockfish
- 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies; 7.e5 Nd5 8.Qf3 transposes). ...Nxc3 hands him c3+d4+e5 - only for a concrete reason.
- 7.Ndb5 Qb8! is the only good retreat. With queens on, do NOT open the centre and never take on e5; ...f6 only with his Bf4 off the c7 diagonal.
- T57 Final (L m11): 9.Qg4! is the sting. Do NOT answer ...O-O: 9...O-O?? 10.Bh6! Qc7?? 11.Qxg7#. g7 is PINNED to Kg8, so ...gxh6 is illegal. Meet Qg4 by removing her g-file aim and keep the king on e8; no short castle until g7 has a PIECE guard and her queen is off g4.
- T58 Final (DRAW v SF19 down a queen): 9...g6! 10...O-O-O is playable and better than ...O-O; g6 takes the g-file aim and ...Bg7/...Bf8 guards g7. But 12.Bh6! and 15.Bg5 hit d8: before O-O-O check Bg5/Bh6 to d8. I lost the d8-rook to 16.Bxd8 Qxd8 and later 22...Qxb2?? 23.Rb1 24.Rxb2 lost my queen. Survived by keeping king and bishop mutually defended and shuffling legal checks; SF accepted threefold at +8.4.
- T54S1G1 (L m20): 11...Bd6?? exd6 and 12...Qc7?? dxc7 handed bishop AND queen, 20.Qd8#. T54R3 (L m13): 11...h6?? 12.Bxh6! With his queen on g3 and a bishop reaching h6, ...h6 is a mating hook: ...f5, a PIECE on g7, or the queen trade.

## Opponents
- Stockfish 19 (depth 4): instant. Punishes loose pieces, hidden defenders, unguarded c6 (Bxc6!), a kicked Ng4, f6 on his e5-pawn's capture square, ...f6 met by exf6, ...h6 met by Bxh6. T55R2: 5...d4 / 8...d3 clamp, ...Bg4, the dxe2 pawn fork, ...Qxf2# m13. T56R2: early ...d4 clamp plus a knight tour (...Nc3/...Nb4/...Nc2/...Nxe3/...Nxg2). T57R2: 5...d4 again; 10.Ne1?!/11.dxe3?? lost my queen to ...Qxd1. T57 Final: 9.Qg4! punished 9...O-O?? with 10.Bh6! 11.Qxg7#. T58R2: 5...d4 clamp, ...Na6/...O-O/...Be6/...c5; 11.d4?! let ...c5; ...Nb4/...Nd3! outpost forked Re1+Bc1; ...Qxb3 took a knight on the b-file. T58 Final: in the Taimanov 9.Qg4! line its 12.Bh6/15.Bg5 won my d8-rook after O-O-O; down a queen at +8 it accepted a threefold when I kept king+bishop defended. T58 Arm: same ...d4 clamp and ...Na6/...Nb4/...Be6 plan; it took 15.Be4 with Nxe4 and then Nxd3/Ne1/Nxf3, and accepted 23.Qg6?? hxg6. Give it no loose unit, no pawn break, no piece on a knight square.
- GLM 5.3 Flash: as White the English/reversed QGD, as Black the Taimanov; sound build but careless with piece safety. T56R3/R5.2/T57R1/T58R1 (my four 1-0): it hands knight, bishop, queen and rook to plain captures and to pawn takes (Ne6?? fxe6, Bc5?? Bxc5, Rxa2?? Bxa2, 17.Qd2?? Nxd2, 18.Qd2?? Bxe4 free pawn). ITS CLOCK SELF-DESTRUCTS: forfeited T58R1 with 5:43 v my 55:51. Take every loose unit and queen; convert without waiting; never an empty or illegal reply.
- DeepSeek V4.1 Flash (mirror): solid Taimanov/English both colours, converts without gifts, up to 8 illegal tries/game (T58R3: 6). T54R1 up a bishop it walked Kf2-e3-d4-e5 and mated N+B m67; T55R3 beat me off my 24.Qd4?? cxd4; T56S2G1 ...c5/...d4! forked Qe3+Nc3. T56R1 (my 1-0 as Black): its 32.Qd7?? Bxd7 and 37.Ra6?? bxa6 gave the game back. T57R3 (my 0-1 as Black): my 15...Qc5?? queen for bishop, Q+2R mated. T57R4 (my 1-0 as Black on time): 28...Bb7 fell to 30.Qxb7; he flagged 2 min v my 47. T58R3 (my 0-1 as White): I won a piece clean 13.Bxe5!/19.dxe6, then 22.Qxb5?? lost my queen and was mated m57 while he had 3:32. T58S2G1 (my 1-0 as Black on time): 16...Qxe5?? left me down a bishop for a pawn; his 4 illegal tries and 12-min thinks flagged him with 2:48 v my 39. It grabs any unit left on his queen's line or a pawn's capture square; its clock can collapse but do not rely on it.
- Expect the ...c5/...d4 fork when my queen sits on d4/e3. NEVER a queen grab while HIS queen covers the landing square, and never a piece on an enemy knight's jump square (T58 Arm 15.Be4).

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record (condensed)
- v SF19: T58 Final 1/2 (B Taimanov, down a queen, threefold); T58 Arm 0-1 (W English clamp, m30: 15.Be4?? Nxe4, 23.Qg6?? hxg6); losses T53 Final, T54R1/R3/S1G1, T55R2/R3/S2G1, T57 Final, T58R2. Wins v GLM T55R5.3, T56R3, T57R1, T58R1.
- T57R4 1-0 v mirror (B Taimanov, he flagged): ...Bc5! won a piece, but 28...Bb7 fell to 30.Qxb7. T58R2 0-1 v SF19 m25 (W English clamp): 11.d4?!, 14.a3?! Nb4-d3!, 17.Nb3?? Qxb3. T58R3 0-1 v mirror m57 (W English): 22.Qxb5?? lost my queen; 35 moves never flagged his 25 min.
- T58S2G1 1-0 v mirror on time (B Taimanov): 16...Qxe5?? left me down B for P; his flag saved me. Keep the rook on the first rank pin, don't push h while his rook checks.
- T58 Arm 0-1 v SF19 (W English clamp): everything guarded except two destinations - the bishop on e4 and the queen on g6. Clock 4:01 left at m30.
