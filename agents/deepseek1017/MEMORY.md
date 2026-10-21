# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit, and 3 total ends the game the same way. T55R1: I spent ALL THREE allowed invalids in a won position while a rook up with 45 min left. When the position is won, write the path slowly: piece, CURRENT square, destination, both crossed squares for a pawn push. After ONE rejection pick a DIFFERENT move/idea. Re-read occupancy before EVERY rook grab.
- HIS PAWN TWO SQUARES FROM MY BACK RANK IS A FORK MACHINE: T55R2 8...d3 9.O-O? ...Bg4 10.Ne1?? dxe2! forked Qd1 and Rf1 - e2 was immune because his Bg4 covered the recapture - 11...exf1=R+ and mate m13. Every move name that pawn's two capture squares and test each of my recapturers against his guards and pins.
- A PIECE GUARDED ONLY BY MY QUEEN IS LOST TO HIS QUEEN (T54R1 11...Bc5?? Qxc5). Name a recapturer that is NOT my queen.
- 'MY QUEEN GUARDS IT' IS A LIE WHEN MY OWN PIECE BLOCKS THE LINE: T55S2G1 12...Bc5?? - my Nc6 stood on the c-file between Qc7 and c5, so the bishop had ZERO recapturers and 13.Bxc5 won it (a clean 4-pawn lead). Before any active bishop/knight sortie, name the recapturer by square and walk its line through my own blockers; zero = the piece is a gift.
- ANY OF MY PIECES ON HIS PAWN'S CAPTURE SQUARE IS LOST, CHECKS AND ROOKS INCLUDED (T50R3 44...Ra4+?? bxa4; T49R2 10.Qxg4?? Bxg4). Sweep every enemy pawn's two capture squares before landing. A PAWN I ATTACK TWICE STILL CAPTURES: T55R3 24.Qd4?? cxd4 - my Qd4 was hitting his c5 pawn, my Rc1 helped, and the pawn took my QUEEN on d4, its own capture square, three moves after I wrote 'his c-pawn hits b4/d4'. The moving pawn does not need a defender when the target lands on its square.
- A PAWN THAT JUST ADVANCED OR CAPTURED OWNS ITS NEW SQUARES: T54S1G1 11...Bd6?? exd6, then 12...Qc7?? dxc7 - bishop AND queen. After every enemy pawn move name BOTH its capture squares and ban them for every piece, queen included. His b7/c7/d7 pawns cover c6/d6/e6 for the whole game: T55R3 34.Bc6?? bxc6 (and the d7-pawn trick never worked for the same reason).
- AN OPEN FILE + HIS ROOK + EMPTY SQUARES = MY PIECE THERE IS FREE (T53R3 14...Bf5?? Rxf5). The mirror also wins for me: T55 27...Nxc4! took a rook that no pawn could reach, bxc4 recaptured a knight.
- HIS e5 PAWN OWNS f6 AND d6 (15.Nf6+?? exf6); a pawn-covered square is no fork square (16...Qe5?? Nxe5).
- THE MOVING PIECE ABANDONS ITS DUTY: name what it guarded and the line it opens (T52R3 20...Bb7?? Nd7 to Rxd7). Answer an attacked piece before any quiet move or castle.
- A CAPTURE THAT UNSCREENS A LINE RE-ARMS THE PIECE BEHIND IT: redraw after EACH capture and name HIS last capturer (T50R4 14...Bxe5??; T51 Final 14...f6??).
- A PIECE GUARDED BY ONE UNIT IS A TARGET (T53S2G1 27...Nxf4! won Qf4; T55R2 his Qf6+Bg4 took my once-guarded Nf3). MY OWN PIECE ON THE RECAPTURE LINE = NO RECAPTURE (T53R1 14.Nc5??).
- A PAWN LOST IS GONE - never 'balance' with a queen grab. MY OWN QUEEN GRAB ON b2 CAN BURY HER (T53 Final 11...Qxb2??): write her retreat squares first. (T55R2 13.Qxb7 was material-only while ...Qxf2# stood on the board.)
- A WARNING I WRITE IS AN ORDER; reread my last comment, and when I write 'guarded' name the guard's PIECE TYPE (T54R1; T54S1G1 ignored two warnings in a row; T55R2 wrote 'only Bg2 guards Nf3' then let ...Bg4 come; T55R3 had written his c-pawn's squares then played Q onto d4).
- THE PIECE I MOVE MAY BE g7's ONLY GUARD (T49R1 10...Be7? Qxg7).
- A PAWN-ATTACKED PIECE MUST MOVE; defending it does not save it. HIS KNIGHT IN MY CAMP = no pawn grabs, no quiet pushes (T52 Final 16.f4? Nh5).
- A ROOK CHECK NEAR MY KING: block on a DIFFERENT rank from my queen (T52 Final 21.Be3? Rxe3+).
- Qg3 + a bishop that reaches e5/f6/h6 = Qxg7#: never capture on e5 then (T48 Final 13...dxe5??); ...h6?? met 12.Bxh6! (T54R3 m13).
- QUEEN TRADE = recapture chain on my central knight (T48R1 11.Qd2??); my queen in front of her king on an open file is pinned (T51R1 21.Rg3!); a pawn on the far side of my centre pawn also unpins a central file (T55R3 his c5/d4 capture killed me).
- A ROOK PINNED ON A DIAGONAL TO MY KING IS FREED BY HITTING THE PINNER: T55S2G1 15...Ne7 and 18...Ne7 attacked his pinning Qd5 and forced her off, unpinning my Rf7; then ...b5/...Nc6 kept the queen busy. When his queen pins a piece to my king, list every knight/pawn jump onto her line before moving the pinned unit.
- DOWN A PIECE OR MORE v SF: guard every unit, 5-10 s, fortress and king shuttle, hunt ONE freeing trade early (T54R1's 60-move fortress still lost m67).

## Endings, king safety, conversion
- MY Kg8 WITH AN EMPTY f8/e8 = BACK-RANK MATE (T54S1G1 20.Qd8# after Rh8-h7). Before a rook leaves my 8th rank name every heavy piece of his reaching d8/e8/f8; keep the rook home or play h6. Mirror for him: T55R2 g1-king, f1-rook gone, f2 taken by his queen.
- HIS Qf6 + A BISHOP REACHING f2 (Bc5 or c1-h6) WITH MY Kg1 AND f2 HOME = ...Qxf2# (T55R2 m13). Once queens are on and my f1-rook has traded, f2 needs a second guard.
- A CHECK ON THE DIAGONAL THROUGH HIS KING HITS A PIECE BEHIND IT: walk both directions to the edge (T53S2G1 42...Qe4+ won Rb1).
- KING ON h1 + HIS QUEEN ON g3 = ...Re1# (T50R2). MY ...Bb7 + HIS Kg1 = Qxg2# (T51S2G1).
- Q+R v bare K: defended non-adjacent checks, walk the king up, never park the rook where his king reaches it; check stalemate every move (T53S2G1 46...Qbe1#).
- UP A ROOK WITH ONLY PAWNS LEFT (T55R1, 12 moves): rank-2/3 rook checks drive his king off his pawns, my king walks up, and a check my own king covers is free (Kg6 before ...h5+) - he had no flight or counter-check and flagged with 0:34. Alternate checks with king progress, never a pure 3-fold shuffle, and keep the rook out of his king's reach.
- UP A ROOK WITH QUEENS OFF: rook to the 7th/8th, collect pawns (T54R2 27.Rb8/30.Rxa6), bishop covers the promotion square, never take a pawn his king guards. R+B v B with a rook up (T55S2G1): rook checks on the 8th first (Ra8+), bishop to f7 to seal g8/g6 - I mated on h4 in 41 moves with no gifts.
- UP A QUEEN: harvest only squares no rook, pawn or knight hits; Qxf7 waits until the f8-rook leaves (T54 3rd m23-33).
- UP A ROOK / 2R v R: take the first clean rook trade, then eat loose pawns; drive a bare king off the passer's square with a rook check. R+B v R: stop the passer before racing. A rook needs a SAFE square, not a check (...Ra4+?? bxa4).
- LEVEL R+B v R+B: the repetition draw is fair; shuffles 15-30 s. TWO ROOKS v QUEEN: draw by blockade, not raids (T49R3).

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock. T55S2G1: 0 invalid, 39 min left at m41 while down a piece - grieving time was fine. Long thinks only for a concrete question (T54R2's 2-min 17.Nb5 found the fork). T55R2: 1:48 and 2:39 on the two blunders; T55R3 16:55 on 16.a3 with nothing to find.

## Opening: English (W v 1...e5; B v 1...Nf6 reversed QGD)
- W: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 (10 plies) - the squeeze setup.
  - vs ...Nb6 (T54R2 WIN v GLM): Nf3, Nc6, O-O, Be7, d3, then Be3/Qd2/Rc1/Rfd1; his c7 is a fork target once his queen leaves c7/d7 (17.Nb5! 18.Nxc7 forked Qe6 and Ra8).
  - vs ...Nxc3/...Bd6 Boleslavsky (T54 3rd WIN v GLM): bxc3, Nf3, O-O, d4 exd4 cxd4, Be3, Re1, d5! Ne7, Bf4 Ng6, Bxd6 cxd6, Nd4, a6, h3 Bh5, g4! - his bishop has no retreat (own Ng6, own f7-pawn): 18...Bxg4 19.hxg4 = piece up.
- v SF's ...d4 clamp, White (T55R2 LOSS m13): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Bg2?! d4 6.Ne4 Nc6 7.Nxf6+ Qxf6 8.Nf3 d3 (16 plies) - trading his Nf6 handed him ...Qf6 + ...Bg4 against a knight guarded once. Play 5.Nf3 or 5.d4 FIRST; if ...d4 comes, keep the knight home for defence (Nb1) instead of Ne4; and once his pawn sits on d3 answer ...Bg4 with b3/Bb2 (tempo on his Qf6), never a knight retreat to e1.
- B reversed QGD: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3 12...Qxd4). Keep ...c6 (or ...Ne4) before ...c5.
  - T52R2: 17...Qxb3; 18.Qc2?? had no c2 recapturer - 18...Qxc2! won her (mate m33).
  - T55R1 WIN v GLM: his 9.Nd4 kicked ...Bf5 to ...Bg6, then e4/dxe4 traded N+B each side; 18...cxb4 (extra pawn), 19...Rxe4 (rook trade while up a pawn), 27...Nxc4 R-for-N, clock win. Do not grab his d4-knight while his queen looks at it.
  - As WHITE v the mirror's ...d5/...c6 (T55R3 LOSS m47): build 5.d4 Carlsbad, Bg2/Nf3/O-O/Bf4/e3/Qd2/Rc1 and the b4-b5 minority - analysis gave only 21.Qd2?! and my queen placement on c5's capture square; the setup itself is sound and stays my plan.

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- AS BLACK the build is sound: ...cxd4/...Nf6/...e6/...Be7/...O-O/...Qc7/...a6, then ...b5/...Bb7/...Rfc8; ...d5 only when e6 recaptures. T55S2G1: level to m12 with f4/e5 clamp neutralized by 10...Nd5 11.Nxd5 exd5; then 12...Bc5?? (see above) - the ONE bad move cost a bishop. After his Nf5 lands, hit the e5 clamp with ...f6 only once the c5 bishop is defended or withdrawn.
- AS BLACK ...b5 needs a guard first (...a6/...Bb7), else Nxb5! (T51R3). His e5 hitting Nf6: never ...Ne8 with my a8-rook home (Nc7 forks) - ...Nd5 (count guards) or ...Nh5.
- AS BLACK keep the f6-knight and the queen guarded: T53R1 16...Rfd8?? exf6; 20...Kg7?? Bxc7; 22.Nxc6! (d8's last defender gone).
- T53R3 (L m24): with HIS d-pawn passed on d5, c6/e6 are banned for every piece AND the queen; ...Qd6 blockade is fine.
- WHITE CLAMP WIN (T50 3rd, T51R1, T53R1): e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then f5-f6 wedge, Bxf6 and exf6! Ban premature f4-f5.
- AS BLACK don't jump ...Nd5 into his Nc3 when e6 cannot recapture; ...Qc7 covers c6 and eyes e5; trade his f6-knight FIRST. An in-between CHECK (T49R4 13.Nxe7+!) beats resolving a queen attack; before my queen leaves the 2nd rank check ...Qxc2/...Qxb2.

## Opening: Open Sicilian Dragon (me White)
- 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies): his Ng4 is GUARDED by Bc8 through d7-e6-f5; answer 9.Nxc6! bxc6 10.Bg5, NEVER Qxg4 (T49R2).
- King safety first after ...Qa5/...Rb8; no f4 while his knight reaches h5/f4; no a7 grab with his knight in my camp (T52 Final 18.Bxa7?).
- T53R2 v SF19: 10.O-O?! Be5! 11.Bd4? Bxh2+! then ...Qh4/...Bg1+ mates - count ...Bxh2+ before castling.

## Opening: Taimanov as BLACK v Stockfish
- 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies; 7.e5 Nd5 8.Qf3 transposes). ...Nxc3 hands him c3+d4+e5 - only for a concrete reason.
- 7.Ndb5 Qb8! only good retreat. With queens on, do NOT open the centre and never take on e5 (14...Bxe5?? 15.Bxe5 Qxe5+ 16.Qxe5); ...f6 only with his Bf4 off the c7 diagonal.
- T54S1G1 (L m20): sound to 8...Nd5; 9.Qg4 forced ...Kf8; then 11...Bd6?? exd6 and 12...Qc7?? dxc7 handed bishop AND queen, 20.Qd8#. The Taimanov is good; pawn-capture-square discipline is what is missing.
- T54R3 (L m13): his 8.Qf3 9.Ne4 10.Bd3 11.Qg3 - 11...h6?? 12.Bxh6! Qxg7#. With his queen on g3 and a bishop reaching h6, ...h6 is a mating hook: ...f5, a PIECE on g7, or the queen trade.
- King on e8 makes Bf8 g7's only guard: ...Be7?? Qxg7; ...O-O?? before ...Qc7 allows Bxc6! winning a8.

## Opponents
- Stockfish 19 (depth 4): instant. Punishes loose pieces, hidden defenders, unguarded c6 (Bxc6!), a kicked Ng4 (...Nxe3!), f6 on his e5-pawn's capture square, ...f6 met by exf6, ...h6 met by Bxh6. T53R2 Dragon ...Be5/...Bxh2+/...Qh4 mated me; T54S1G1 took a bishop and a queen off pawn capture squares, then mated on the open 8th. T55R2: 5...d4 / 8...d3 clamp, ...Bg4 on a once-guarded knight, then the dxe2 pawn fork and ...Qxf2# in 13 moves.
- DeepSeek V4.1 Flash (mirror): solid Taimanov/English both colours, converts without gifts, up to 8 illegal tries/game. T54R1 up a bishop from m12 it walked Kf2-e3-d4-e5 and mated N+B at m67. T55R3 it played the reversed QGD as Black and beat me 0-1 m47: my sound setup was undone by 24.Qd4?? cxd4. T55S2G1: it played 12.Nf5! at my d7-blocked Be7, took the undefended 12...Bc5, then kept the pin with Qd5 until my ...Ne7/...b5/...Nc6 freed the rook, and converted R+B v B without a gift. Vs mirror: gift nothing, no 'active' undefended piece, expect no gift back when down.
- GLM 5.3 Flash: as White the English; as Black the Taimanov with a sound build but careless with the f6-knight and queen (T53R1 16...Rfd8?? exf6; T52R2 18.Qc2?? Qxc2!). T54 3rd: its ...Nxc3/...Bd6 Boleslavsky let 18.g4! trap a bishop and 22.Qxg4 win the queen; it thought 8:08/11:14/7:48 while a queen down and flagged. T55R1: flagged again (0:34) at m39 while I had 45 min, after a 10:08 think on 18.b4 that only lost a pawn; it plays pawn pushes into the fire (18.b4??/26.axb3?) and leaves a rook where a knight takes it (...Nxc4 won R for N). Vs GLM: 10-20 s sound moves, e5 clamp or plain central play, take every loose unit and queen, let its clock run, but NEVER risk an illegal reply while ahead.

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record
- T47R1 W v GLM forfeit. T48 R1/Final/R2: 0-1 v SF19 (11.Qd2??; Qxg7#; 10.Qxg4??).
- T49R1 forfeit win; R3 draw (18.Qxd8+??); R4 1-0 on time (13.Nxe7+!); Final 0-1 (11...O-O? Bxc6!).
- T50: R1 0-1; R2 0-1 (11.Nxd5??); R3 0-1 (44...Ra4+?? bxa4); R4 0-1 (14...Bxe5??); 3rd 1-0 v GLM (e5 clamp, 51.Rd8#).
- T51: R1 1-0 (21.Rg3!); R2 0-1 (9.h3?! Nxe3!); R3 0-1 (12...Qxc2??); S2G1 WIN Qxg2#; Final 0-1 (14...f6??).
- T52: R2 WIN Qxf1#; R3 WIN Qg1# m70; S2G1 draw; Arm WIN on time; Final draw threefold; Final Arm 0-1 (16.f4? Nh5).
- T53: R1 1-0 m28 (17.exf6!, 28.Bd5#); R2 0-1 Qh2#; R3 0-1 m24 (14...Bf5?? Rxf5; 17...Qe6?? dxe6); S2G1 WIN Qbe1# m46; Final 0-1 m47 (11...Qxb2??).
- T54: R1 0-1 m67 (11...Bc5?? Qxc5). R2 1-0 m39 (English vs ...d5; 18.Nxc7!; Qe8#). R3 0-1 m13 (11...h6?? Bxh6!). S1G1 0-1 m20 (11...Bd6?? exd6, 12...Qc7?? dxc7; 20.Qd8#). 3rd 1-0 v GLM (English Boleslavsky; 18.g4! trapped Bh5, 22.Qxg4 won her, GLM flagged m33; 2 illegal tries).
- T55R1 1-0 (B v GLM): English reversed QGD level to m17, extra pawn 18...cxb4, 19...Rxe4 rook trade, 27...Nxc4 R-for-N, rank-2 rook checks + king walk; GLM flagged m39. 3 invalid tries = the cap: legality, not chess, was the risk.
- T55R2 0-1 v SF19 m13 (W English reversed QGD): 9.O-O? ...Bg4 10.Ne1?? dxe2! fork, 13...Qxf2#. Zero illegal; the miss was the pawn's capture squares under his bishop's guard.
- T55R3 0-1 v mirror m47 (W English reversed QGD Carlsbad): sound to m24; 24.Qd4?? cxd4 lost my queen, 34.Bc6?? bxc6 the bishop. Zero illegal.
- T55S2G1 0-1 v mirror m41 (B Taimanov): level to m12, 12...Bc5?? lost a bishop to Bxc5 (my Nc6 blocked Qc7's recapture). Then defended R+B v B for 28 moves - ...Ne7 attacking his pinning Qd5 twice worked, ...b5/...Nc6 kept her busy - until 41.Rxh4#. Zero illegal, 39 min left.
