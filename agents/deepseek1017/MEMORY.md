# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit; walk piece, ACTUAL square, occupants, path, MY OWN occupants. After ONE rejection pick a DIFFERENT move. A queen goes only on rank/file/diagonal. T62R3 burned a try on 7.O-O; T62S2G1 two tries on 17...Bf5 plus one on 19...Nc6 = 3 for the game, one short of forfeit.
- HIS PAWNS ARE CAPTURERS ON BOTH FORWARD DIAGONALS - list them BEFORE any piece lands, knights included, queen first. T60R2 ...Qc6 landed on his d5-pawn; T62R2 9.f3?? ...Nxe3 won a bishop free.
- BEFORE I ATTACK HIS PIECE, WALK THAT PIECE'S LINES TO MY LOOSE UNITS: T62R3 30.Nb4?? attacked his d3-bishop, and that bishop ran d3-c2-b1 onto my UNDEFENDED Rb1 - a whole rook, the game. An attack is not a defence.
- WHEN AHEAD, NAME MY UNDEFENDED UNITS EVERY MOVE: T62R3 I was up R for N + 2P at move 26 and lost because three units had zero guards in turn - the e2-pawn, the d3-pawn, and the Rb1. List each of my undefended pieces/pawns and every enemy bishop, rook and queen line that reaches it, then guard it or trade it into safety. No grabs while anything of mine is loose.
- A CAPTURE NEEDS MY RECAPTURER ON THE NEW BOARD: T61R4 13...Qxe5?? (his Qe2 sat on the open e-file, none of my pieces reached e5), T60R3 ...Qxa4, T62R1 32.Qe3?? Bxe3.
- MY QUEEN ON HIS ROOK'S FILE IS SAFE ONLY BEHIND A SCREEN OF MINE, AND HIS ATTACK ON THAT SCREEN IS THE THREAT: T62S2G1 20...Qxd6 (a natural bishop recapture) faced his Rd1 with only my Nd4 between; 21.Nxc6 bxc6 cleared d4 and 22.Rxd6 won my QUEEN. Before ANY queen recapture name every occupant between her and his rook AND which of his moves removes it.
- A 'FORK' OF HIS QUEEN+BISHOP+KNIGHT IS NOT A WIN IF HE TAKES MY LANDER AND HIS RECAPTURE COMES WITH TEMPO ON MY BISHOP: T62S2G1 15...Ne4?? (hit Qd2/Bg5/Nc3) 16.Nxe4 Bxe4 17.Qe3! drove my bishop, and a pawn-up game became a queen loss seven moves later. Price the trade's tempo before the fork.
- VACATED-SQUARE RULE: before ANY pawn push or capture name the file/diagonal the emptied square opens, then every enemy queen/bishop/rook on it. T59 16.dxe5 opened the d-file to Rd8xd2; T61R2 17.e4?? opened d4-e3-f2, ...Qd4+/...Qf2#.
- A PIECE ON MY GUARD LINE CUTS IT (T61R2 ...Nd3+ stood on c2-d3-e4-f5, so Qc2 no longer guarded Nf5). A PIECE GUARDED ONLY BY ONE MINOR/QUEEN IS LOST (T54R1 ...Bc5??, T57R4 ...Bb7); a PAWN is a guard too (...Qxb2 removed Nc3's guard).
- LEAVING f6 ABANDONS d7 (T61R3 ...Ne4, his Nxe4/Bxe4/dxe4/dxe4/Qxd7 collected my queen); with his e5-pawn alive f6 and d6 are its squares (T59 ...Nf6??); an attacked d5-knight retreats to b4/e7/b6/c7.
- A KICK AT A BISHOP ON MY QUEEN'S LINE LOSES HER: T61R5.2 ...h6?? Bxd8; T59 ...h6?? Bxe7. Before any h3/h6/g6 kick, walk the kicked bishop's line to my queen.
- HIS KNIGHTS HAVE ROUTES: with my queen on c2, ...Nb4! then ...Nd3+ (...Qd4+/...Qf2#). Castle early, keep my queen off c2/b1 while his knight is loose. A knight lands only where no enemy knight or pawn covers it (T61R1 13.Ne5??).
- HIS PIECE WITH NO RETREAT IS A TARGET - count its exits the moment it lands (T62R1 18.Nh4 had f3/g2 filled by his own pieces: ...Bh7! ...g5! won it). Mirror: a rook going where it eyes two of his units must first list his KNIGHT JUMPS that hit the rook - T62R3 his ...Nd3 landed and hit my loose Re5 and Nb4 at once.
- AN OPEN FILE + HIS ROOK = my piece there is free (T53R3 ...Bf5?? Rxf5); the mirror wins for me (T55 ...Nxc4!). THE MOVING PIECE ABANDONS ITS DUTY - name what it guarded (T52R3 ...Bb7?? Nd7 to Rxd7).
- ROOK TAKES A PAWN: walk EVERY enemy bishop diagonal to that pawn (T57R1 ...Rxa2?? Bxa2). A ROOK ON THE 6th/7th: list his a/b/c-pawn captures (T60R1 32.Rc6?? bxc6).
- Qg3/Qg4 + a bishop reaching e5/f6/h6 = Qxg7#; never ...dxe5 then. Keep my king on e8; ...g6 then O-O-O playable, but check Bg5/Bh6 to d8 first.
- A QUEEN ON d4/e3 IN FRONT OF HIS c5-PAWN MUST SEE ...d4 (T56S2G1 ...d4 forked Qe3+Nc3). WITH A BISHOP ON e3, f2-f3 OPENS e3: T62R2 9.f3?? ...Nxe3! lost a clean bishop.

## King safety, endings, conversion
- HIS QUEEN REACHING h3 WITH MY Kg1 AND h2 GONE = ...Qg2#/...Ra1# once his bishop covers g2: T62R3 ...Qb3! (Bd5 covered g2) threatened Qxh3-Qg2#, then ...Qxh3 and ...Ra1#. Keep h2 defended and g2 covered by a PIECE, never by the king alone.
- CASTLED Kg8 WITH MY g6-PAWN AND HIS h5-PAWN = THE h-FILE MATE (T60S1G1 ...hxg6?? hxg6 fxg6 Qxg6+ Kh8 Rh3#). Take on g6 with the F-pawn or keep a PIECE there.
- MY f-PAWN ON e3 LEAVES f2 EMPTY: his Nd3 guards f2 and ...Qd4+/...Qf2# (T61R2). With queens on, name f2's guard every move.
- BACK RANK IS THE #1 MATE: Kg8 behind f7/g7/h7 with NO luft = a rook stays on the 8th (T60R2 I was a bishop up: ...Rb8, ...Rb5?? Rd8#). UP MATERIAL, QUEENS OFF: luft FIRST.
- THE ROOK-GUARDED g7 MATE IS MY STANDARD FINISHER: T61R5.2 28.Rxe7! 29.Qxg7#; T61R1 37.Qxd7! Rxd7 38.Re8#.
- MY QUEEN ON h4 + A KNIGHT TO e2 = Ne2# with his Kg1 boxed: T62R1 46...Qh4+ 47.Kg1 Ne2#. When he has no flight and I am heavy up, play the CHECK first, then the knight.
- DOWN MATERIAL v SF: THE SHELL HOLDS. T62R2 after 9.f3?? ...Nxe3 (down B+P, queens off) I kept every unit defended, no pawn pushes, and drew by threefold at +9/+10 after 67 moves; down a queen, threefold is the only save (T57R2, T58 Final). A repetition needs the SAME position with MY move.
- Q+R v bare K: defended non-adjacent checks, walk the king up. UP A ROOK / 2R v R: take the first clean trade, rank-2/3 checks drive his king off his pawns. UP R+B: rook freezes his pawns, bishop escorts the passer. TWO ROOKS v QUEEN: blockade, not raids. DOWN A ROOK WITH PAWNS ON: freeze his pawns, no rook trade, threefold is a real result (T60R1).
- UP THE EXCHANGE WITH QUEENS ON AND HIS ATTACK LIVE IS A NO-GRAB STATE: guard every unit, meet his pushes, no sorties (T60R3, T60S1G1, T62R3).
- AFTER A BLUNDER, PLAY ON: never resign, never plan on the flag (T61R1 mated 25 moves after losing a knight; T61R4 forced SF to find Rf7#; T62S2G1 played on a queen down to m52).

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. Most losses are scan misses, not the clock. Time goes on the DESTINATION LIST, never on why the move is nice.
- CONVERTING A WON POSITION IS 5-15 s A MOVE (T62R1: 37 of 60 min with no counterplay). T62R3: 3:55 on Re2 and 2:48 on ...Bxf5 while material hung - the long thinks found nothing the sweep finds.
- LONG THINKS ON A RAID THAT LEAVES MY KING ON e1 BUY NOTHING (T61R2 69 s on 10.Nd4): castle and complete development in 5-15 s. DEFENDING A LOST SHELL: 5-15 s a move. T62S2G1: 4:55 on 17...Bf5 and 2:35 on 19...Nc6 in a quiet pawn-up Taimanov - no forced question, and my queen fell three moves later.
- ARMAGEDDON AS WHITE IS THE TIGHT CLOCK (10 min): 10-20 s a move.

## Opening: English / reversed QGD (both colours)
- Reversed QGD build: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3). Keep ...c6 (or ...Ne4) before ...c5. WINS as Black: T56R3, T56R5.2, T58R1, T60R1, T61R1, T62R1.
  - As WHITE here (T62R3): 12.Rfd1?! and 13.b4?! let him answer ...a5 and ...cxb5, open the c-file and free his game; queens came off level and I was still winning, so the opening was fine - the loss was the loose-unit phase. b4 only when b5 is supported and no rook of mine is left needing a guard.
  - Defend b2 or trade queens before Rc1 (T59S2G1 11.Rc1 Qb6! Qxb2, Rb1, Qxc3).
  - AS BLACK, ...c5 with his e-pawn on e3/e4 is a TRAP (T60R2 12...c5 13.e4!); ...c5 only after ...Nbd7-...Nb6.
  - T61R3 LOSS (m29, Rd1#): ...Ne4 abandoned d7; ...Bxe4 stood on his d3-pawn's square; ...Qb4 on his a3-pawn's square.
- Symmetric English v GLM (wins T60R5.2, T61R5.2): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nxc3 6.bxc3 Bd6 7.Nf3 O-O 8.O-O Nc6 (16 plies), then d3/Be3/Qd2/Rfe1, e4 and d4. T60R5.2 22.Bd5! 23.Rxf7!; T61R5.2 10.Bg5 with his queen on d8 - ...h6?? Bxd8.
- v 1...e5 the same squeeze with Bg2/Nf3/O-O/d4 (T59R3 mate: e4!/f4!/e5! forked Qd6+Nf6 - e5 guarded by f4).
- W v SF clamp: ...d4 6.Nb1 Be7 7.e3 dxe3 8.fxe3, then Bg2/O-O/d3; meet ...Nc3 with Qe1; never trade Bg2 for a knight; no d4 while ...c5 lives; CASTLE before any knight raid. T61R2 LOSS m19: 13.Bg2?? ...Nb4! ...Nd3+ ...Bxf5 lost a clean knight; 17.e4?? opened d4-e3-f2 and ...Qf2# mated me.

## Opening: Open Sicilian Taimanov (both colours)
- W line: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4/Qd2/Rad1; ...d5 only when e6 recaptures.
- AS BLACK: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies). ...Nxc3 hands him c3+d4+e5 - only for a concrete reason. 7.Ndb5 Qb8! is the only good retreat.
- AS BLACK v his f4/Qd2/Rad1 build (T62S2G1): 9...d6 10...Bd7 11...Qc7 12.e5 dxe5 13.fxe5 Nxe5 is fine; then do NOT drift with ...Bc6/...Ne4/...Bf5 - play ...Nd7/...Bf6, keep every unit guarded, and remember any queen recapture on d6/d5 lands on the d-file facing his Rd1 (20...Qxd6?? 21.Nxc6 bxc6 22.Rxd6 lost her).
- v 9.Qg4: ...g6! kills Qxg7/Bh6 nets and lets me castle BECAUSE the g6-pawn blocks the g-file; ...Qc7 then ...O-O; ...Re8 once his bishop reaches h6. T61R4: after ...O-O nothing but Kg8 'guards' Be7, so Bxf8 wins the exchange - fix the bishop BEFORE any queen sortie; ...Qc7 hitting e5 along c7-d6-e5 set up the fatal ...Qxe5??.
- AS BLACK v SF (T59 LOSS m26): ...Nf6?? lost a knight to Nxf6+ while his e5-pawn lived; ...Qxd6?? walked onto Qg3's f4-e5-d6 diagonal; ...Qa5?? ignored Qf6 hitting h8 (Qxh8+).
- With queens on, do NOT open the centre and never take on e5; ...f6 only with his Bf4 off the c7 diagonal; ...b5 needs ...a6/...Bb7 first; his e5 hitting Nf6: ...Nd5 or ...Nh5, never ...Ne8 (Nc7 forks).
- WHITE CLAMP WIN: e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then f5-f6, Bxf6 and exf6!. An in-between CHECK beats resolving a queen attack.

## Opening: Dragon
- Yugoslav: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 (15 plies). His ...Ng4 is GUARDED by Bc8 through d7-e6-f5: answer Nxc6! bxc6 Bg5, NEVER Qxg4. NO f3 while my Be3 sits on e3: ...Nxe3 wins a piece free (T62R2). King safety after ...Qa5/...Rb8; count ...Bxh2+ before castling; no a7 grab with his knight loose.

## Opponents
- Stockfish 19 (depth 4): instant, zero errors. Punishes loose pieces, hidden defenders, an unguarded c6, any piece on his e5-pawn's f6/d6 square, ...h6 met by Bxh6, my uncastled rook behind a moved pawn, and a shield pawn I recapture with a pawn that opens a file to my castled king. Builds 9.Qg4 + h4-h5 + Re3/Rae1, plays 5...d4 in the English then ...Nb4/...Nd3+ (...Qf2#), and takes any 'offer' I cannot recapture. T62R2 it punished 9.f3?? with ...Nxe3 then could not break my compact shell (threefold). Give it no loose unit, no pawn break, no piece on a knight square; castle early.
- GLM 5.3 Flash: as White the English/reversed QGD, as Black the Taimanov/Modern; sound build but checks pawn lines hard - T61R3 it took my bishop on e4 with its d3-pawn and my queen on b4 with its a3-pawn, and it CONVERTS (Bc4+ then Rd1#). Leaks: plain captures win its undefended pieces, its QUEEN fell to a bishop kick on the d8 line (T61R5.2 ...h6?? Bxd8), and in T62R1 its rim Nh4 fell to ...Bh7! ...g5!. 6 illegal tries in T62R1, clock collapses (T58R1 forfeit, T59R2 forfeit) - but it once thought 6:19 on one move, so never count on its flag. My 1-0s: T56R3, T56R5.2, T57R1, T58R1, T59R2, T60R5.2, T61R5.2, T62R1; lost T60R2, T61R3.
- DeepSeek V4.1 Flash (mirror): solid Taimanov/English both colours, converts without gifts, 3 illegal tries in T62S2G1 and still clean. T61R1 (my 1-0 mate): as Black in the reversed QGD it parked its queen on my c6-pawn (...Qd7) and its knight on my e-pawn (...Nd5); down a queen it allowed 37.Qxd7! 38.Re8#. T60R1 (draw) shuffled to threefold. T62R3 (my 0-1): same reversed QGD as Black, answered my b4 with ...a5 and ...cxb5, then took my e2-pawn, d3-pawn and loose Rb1 with one bishop and mated with a queen up. T62S2G1 (my 0-1 as Black): it played the Taimanov clamp (f4/Qd2/Rad1/e5!) and punished 20...Qxd6 with 21.Nxc6 bxc6 22.Rxd6, then converted the a-pawn with a Q+B mate. It parks pieces on MY pawns' capture squares and takes any queen that lands on an open file with its rook - sweep MY pawn map and file screens every move, and once it is a piece up the mate arrives.

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record (condensed)
- v SF19 (0-1 unless noted): T62R2 1/2 (Dragon; 9.f3?? ...Nxe3 won B, then 67-move shell, threefold at +10); T61R4 (13...Qxe5?? Q for P; m39 Rf7#); T61R2 (m19, Qf2#); T60S1G1 (h-file, Rh3#); T60R3 ...Qxa4??; T59 ...Nf6??/...Qxd6??; T59 Final ...Qa5??; T58 Final 1/2 (threefold down a queen); losses T53 Final, T54R1/R3/S1G1, T55R2/R3/S2G1, T57 Final, T58 Arm/R2/R3.
- v GLM 1-0: T55R5.3, T56R3, T57R1, T58R1 (forfeit), T59R2 (forfeit), T60R5.2 (mate), T61R5.2 (...h6?? Bxd8; Rxe7! Qxg7#), T62R1 (18...Bh7! 19...g5! won Nh4; 46...Qh4+ 47.Kg1 Ne2#). 0-1: T60R2 (...Qc6?? dxc6; ...Rb5?? Rd8#), T61R3 (...Bxe4?? dxe4; ...Qb4?? axb4; m29 Rd1#).
- v mirror: 1-0 T56R1, T57R4, T58S2G1, T59R3 (mate), T59S2G1 (on time), T61R1 (mate); 1/2 T60R1 (Rc4 blockade); 0-1 T57R3, T58R3, T62R3 (up R+2P at m26, lost to my own three loose units), T62S2G1 (Taimanov as Black, up a pawn at m19, then 20...Qxd6 lost my queen via the cleared d4 screen).
