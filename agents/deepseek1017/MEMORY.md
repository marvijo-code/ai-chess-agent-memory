# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit; walk piece, ACTUAL square, occupants, path, MY OWN occupants. After ONE rejection pick a DIFFERENT move. A queen goes only on rank/file/diagonal. T62R5.2: 3 illegal tries spread over ^{-"13...Bg6 (e5), 19...Bxd4, 41...Qd4 - one more = forfeit.
- HIS PAWNS ARE CAPTURERS ON BOTH FORWARD DIAGONALS - list them BEFORE any piece lands, ROOKS and knights included, queen first. T60R2 ...Qc6 landed on his d5-pawn; T62R2 9.f3?? ...Nxe3 won a bishop free; T63R1 35.Re6?? fxe6 (the f7-pawn) threw a rook-up game.
- BEFORE I ATTACK HIS PIECE, WALK THAT PIECE'S LINES AND HIS PAWN RECAPTURES TO MY LOOSE UNITS: T62R3 30.Nb4?? attacked his d3-bishop, which ran d3-c2-b1 onto my UNDEFENDED Rb1. T63R1 35.Re6?? 'attacked' his Rd6 and the f7-PAWN took my rook. An attack is not a defence.
- WHEN AHEAD, NAME MY UNDEFENDED UNITS EVERY MOVE: T62R3 up R for N + 2P at move 26, lost to three unguarded units. T63R1 up a FULL ROOK at move 34 (2R+B v R+B): 35.Re6?? fxe6, then ...Rxd3 took my other, undefended rook, ...Be8 blockaded the passer and his extra pawns won. Up a rook = trade rooks or mate, never a rook sortie into his camp, never a rook without a guard.
- A CAPTURE NEEDS MY RECAPTURER ON THE NEW BOARD: T61R4 13...Qxe5?? (none of my pieces reached e5), T60R3 ...Qxa4, T62R1 32.Qe3?? Bxe3.
- MY QUEEN ON HIS ROOK'S FILE IS SAFE ONLY BEHIND A SCREEN OF MINE, AND HIS ATTACK ON THAT SCREEN IS THE THREAT: T62S2G1 20...Qxd6 faced his Rd1 with only my Nd4 between; 21.Nxc6 bxc6 cleared d4 and 22.Rxd6 won my QUEEN. Before ANY queen recapture name every occupant between her and his rook AND which of his moves removes it.
- A FORK IS NOT A WIN IF HE CAN TAKE THE LANDER OR IT HAS NO EXIT: T62S2G1 15...Ne4?? 16.Nxe4 (guarded twice); T62R5.2 15...Ncxe4?? same. T63R1 18.Nbc7 hit both rooks but 18...Nxd5 removed the knight guarding c7, my c7-knight had no retreat, and 19.Nxa8 Qxa8 was only knight for rook. Name the forking knight's EXITS and his captures of it before it lands.
- VACATED-SQUARE RULE: before ANY pawn push or capture name the file/diagonal the emptied square opens, then every enemy queen/bishop/rook on it. T59 16.dxe5 opened the d-file to Rd8xd2; T61R2 17.e4?? opened d4-e3-f2, ...Qd4+/...Qf2#.
- A PIECE ON MY GUARD LINE CUTS IT (T61R2 ...Nd3+ stood on c2-d3-e4-f5). A PIECE GUARDED ONLY BY ONE MINOR/QUEEN IS LOST (T54R1 ...Bc5??, T57R4 ...Bb7); a PAWN is a guard too (...Qxb2 removed Nc3's guard).
- LEAVING f6 ABANDONS d7 (T61R3 ...Ne4, his Nxe4/Bxe4/dxe4/Qxd7 collected my queen); with his e5-pawn alive f6 and d6 are its squares (T59 ...Nf6??); an attacked d5-knight retreats to b4/e7/b6/c7.
- A KICK AT A BISHOP ON MY QUEEN'S LINE LOSES HER: T61R5.2 ...h6?? Bxd8; T59 ...h6?? Bxe7. Before any h3/h6/g6 kick, walk the kicked bishop's line to my queen.
- HIS KNIGHTS HAVE ROUTES: with my queen on c2, ...Nb4! then ...Nd3+ (...Qd4+/...Qf2#). Castle early, keep my queen off c2/b1 while his knight is loose. A knight lands only where no enemy knight or pawn covers it (T61R1 13.Ne5??).
- HIS PIECE WITH NO RETREAT IS A TARGET - count its exits the moment it lands (T62R1 18.Nh4: ...Bh7! ...g5!). Mirror: a rook eyeing two of his units must first list his KNIGHT JUMPS that hit it (T62R3 ...Nd3 hit my loose Re5 and Nb4).
- AN OPEN FILE + HIS ROOK = my piece there is free (T53R3 ...Bf5?? Rxf5); the mirror wins for me (T55 ...Nxc4!). THE MOVING PIECE ABANDONS ITS DUTY - name what it guarded (T52R3 ...Bb7?? Nd7 to Rxd7).
- ROOK TAKES A PAWN: walk EVERY enemy bishop diagonal to that pawn (T57R1 ...Rxa2?? Bxa2). A ROOK ON THE 6th/7th: list his a/b/c-pawn captures (T60R1 32.Rc6?? bxc6).
- Qg3/Qg4 + a bishop reaching e5/f6/h6 = Qxg7#; never ...dxe5 then. Keep my king on e8; ...g6 then O-O-O playable, but check Bg5/Bh6 to d8 first.
- WITH A BISHOP ON e3, f2-f3 OPENS e3: T62R2 9.f3?? ...Nxe3! lost a clean bishop. A queen on d4/e3 in front of his c5-pawn must see ...d4 (T56S2G1 forked Qe3+Nc3).

## King safety, endings, conversion
- HIS QUEEN REACHING h3 WITH MY Kg1 AND h2 GONE = ...Qg2#/...Ra1# once his bishop covers g2: T62R3 ...Qb3! (Bd5 covered g2) set Qxh3-Qg2#, then ...Qxh3 and ...Ra1#. Keep h2 defended and g2 covered by a PIECE, never by the king alone.
- CASTLED Kg8 WITH MY g6-PAWN AND HIS h5-PAWN = THE h-FILE MATE (T60S1G1 ...hxg6?? hxg6 fxg6 Qxg6+ Kh8 Rh3#). Take on g6 with the F-pawn or keep a PIECE there.
- MY f-PAWN ON e3 LEAVES f2 EMPTY: his Nd3 guards f2 and ...Qd4+/...Qf2# (T61R2). With queens on, name f2's guard every move.
- BACK RANK IS THE #1 MATE: Kg8 behind f7/g7/h7 with NO luft = a rook stays on the 8th (T60R2 I was a bishop up: ...Rb8, ...Rb5?? Rd8#). UP MATERIAL, QUEENS OFF: luft FIRST.
- THE ROOK-GUARDED g7 MATE IS MY STANDARD FINISHER: T61R5.2 28.Rxe7! 29.Qxg7#; T61R1 37.Qxd7! Rxd7 38.Re8#.
- MY QUEEN ON h4 + A KNIGHT TO e2 = Ne2# with his Kg1 boxed: T62R1 46...Qh4+ 47.Kg1 Ne2#. When he has no flight and I am heavy up, play the CHECK first, then the knight.
- DOWN MATERIAL v SF: THE SHELL HOLDS. T62R2 after 9.f3?? ...Nxe3 (down B+P, queens off) I kept every unit defended, no pawn pushes, and drew by threefold at +9/+10 after 67 moves; down a queen, threefold is the only save (T57R2, T58 Final). A repetition needs the SAME position with MY move.
- Q+R v bare K: defended non-adjacent checks, walk the king up. UP A ROOK / 2R v R: take the first clean trade, rank-2/3 checks drive his king off his pawns. UP R+B: rook freezes his pawns, bishop escorts the passer. TWO ROOKS v QUEEN: blockade, not raids. DOWN A ROOK WITH PAWNS ON: freeze his pawns, no rook trade, threefold is a real result (T60R1).
- UP THE EXCHANGE WITH QUEENS ON AND HIS ATTACK LIVE IS A NO-GRAB STATE: guard every unit, meet his pushes, no sorties (T60R3, T60S1G1, T62R3). With queens OFF, a +R position is a trading/mating job, not a raiding one (T63R1).
- AFTER A BLUNDER, PLAY ON: never resign, never plan on the flag (T61R1 mated 25 moves after losing a knight; T62S2G1 played a queen down to m52; T63R1 kept 54 bare-king moves).

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. Most losses are scan misses, not the clock. Time goes on the DESTINATION LIST, never on why the move is nice.
- CONVERTING A WON POSITION IS 5-15 s A MOVE (T62R1: 37 of 60 min with no counterplay). T62R3: 3:55 on Re2 and 2:48 on ...Bxf5 while material hung - the long thinks found nothing the sweep finds. T63R1: 1:36/1:29/1:40 on 9.Qd2/13.Na4/14.Nd4 in a LEVEL position found nothing.
- LONG THINKS ON A RAID THAT LEAVES MY KING ON e1 BUY NOTHING (T61R2 69 s on 10.Nd4): castle and complete development in 5-15 s. T62S2G1: 4:55 on 17...Bf5 and 2:35 on 19...Nc6, and my queen fell three moves later.
- ARMAGEDDON AS WHITE IS THE TIGHT CLOCK (10 min): 10-20 s a move.

## Opening: English / reversed QGD (both colours)
- v 1...e5 with ...Nc6 (T63R1, my 0-1): 1.c4 e5 2.Nc3 Nc6 3.g3 Nf6 4.Bg2 Bc5 5.Nf3 d6 6.d3 O-O 7.O-O h6 8.Be3 Bb6 (16 plies), then Qd2, Rfe1, Bxb6 axb6, e3, expecting his ...Na5/...e4/...c5. The setup was fine (level), the failure was knight wandering: 13.Na4?! hit a defended b6-pawn, 15.Nb5?! met ...Nc6, 18.Nbc7 traded a knight for a rook and then the game.
- Reversed QGD build: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Nf3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (15 plies), then ...Bf5/...Nbd7/...Re8/...Qb6.
  - ...Qb6 wins the IQP d4 when HIS Nd2 blocks Qd1 (T50R3). Keep ...c6 (or ...Ne4) before ...c5. WINS as Black: T56R3, T56R5.2, T58R1, T60R1, T61R1, T62R1, T62R5.2.
  - As WHITE here (T62R3): 12.Rfd1?! and 13.b4?! let him answer ...a5 and ...cxb5 and free his game; queens came off level and I was still winning, so the opening was fine - the loss was the loose-unit phase. b4 only when b5 is supported and no rook of mine needs a guard.
  - Defend b2 or trade queens before Rc1 (T59S2G1 11.Rc1 Qb6! Qxb2, Rb1, Qxc3).
  - AS BLACK, ...c5 with his e-pawn on e3/e4 is a TRAP (T60R2); ...c5 only after ...Nbd7-...Nb6.
  - T61R3 LOSS (m29, Rd1#): ...Ne4 abandoned d7; ...Bxe4 stood on his d3-pawn's square; ...Qb4 on his a3-pawn's square.
- Symmetric English v GLM (wins T60R5.2, T61R5.2): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nxc3 6.bxc3 Bd6 7.Nf3 O-O 8.O-O Nc6 (16 plies), then d3/Be3/Qd2/Rfe1, e4 and d4; the same squeeze by transposition when his ...Nc6 comes first. T60R5.2 22.Bd5! 23.Rxf7!; T61R5.2 10.Bg5 with his queen on d8 - ...h6?? Bxd8; T59R3 e4!/f4!/e5! forked Qd6+Nf6 (e5 guarded by f4).
- W v SF clamp: ...d4, retreat Nb1, then e3 and recapture with the f-pawn, Bg2/O-O/d3; meet ...Nc3 with Qe1; never trade Bg2 for a knight; no d4 while ...c5 lives; CASTLE before any knight raid. T61R2 LOSS m19: 13.Bg2?? ...Nb4! ...Nd3+ ...Bxf5 lost a clean knight; 17.e4?? opened d4-e3-f2 and ...Qf2# mated me.

## Opening: Open Sicilian Taimanov (both colours)
- W line: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies), then f4/Qd2/Rad1; ...d5 only when e6 recaptures.
- AS BLACK: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies). ...Nxc3 hands him c3+d4+e5 - only for a concrete reason. 7.Ndb5 Qb8! is the only good retreat.
- AS BLACK v his f4/Qd2/Rad1 build (T62S2G1): ...d6, ...Bd7, ...Qc7, then e5 dxe5 fxe5 Nxe5 is fine; then do NOT drift with ...Bc6/...Ne4/...Bf5 - play ...Nd7/...Bf6, keep every unit guarded, and remember any queen recapture on d6/d5 lands on the d-file facing his Rd1 (20...Qxd6?? 21.Nxc6 bxc6 22.Rxd6 lost her).
- v 9.Qg4: ...g6! is right (kills Qxg7/Bh6 nets, g6-pawn blocks the g-file), but KEEP the e7 bishop (so 14.Bf6 is met by ...Bxf6) and do NOT castle short into Qg4+Bg5+h4-h5 with the g6-pawn as the only shield. T63R2 (SF19, m20 Qxg7#): 12...Bc5?! 13...O-O?? 14.Bf6! +5.5, 15.h4 Bf8 16.h5 Qa5 17.hxg6 fxg6 18.Bxg6! and mate. T61R4: after ...O-O nothing but Kg8 'guards' Be7, so Bxf8 wins the exchange - fix the bishop BEFORE any queen sortie; ...Qc7 hitting e5 along c7-d6-e5 set up the fatal ...Qxe5??.
- AS BLACK v SF (T59 LOSS m26): ...Nf6?? lost a knight to Nxf6+ while his e5-pawn lived; ...Qxd6?? walked onto Qg3's f4-e5-d6 diagonal; ...Qa5?? ignored Qf6 hitting h8 (Qxh8+).
- With queens on, do NOT open the centre and never take on e5; ...f6 only with his Bf4 off the c7 diagonal; ...b5 needs ...a6/...Bb7 first; his e5 hitting Nf6: ...Nd5 or ...Nh5, never ...Ne8 (Nc7 forks).
- WHITE CLAMP WIN: e5 supported by f4 means ...Nxe5 fxe5 wins a piece; then f5-f6, Bxf6 and exf6!. An in-between CHECK beats resolving a queen attack.

## Opening: Dragon
- Yugoslav: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 (15 plies). His ...Ng4 is GUARDED by Bc8 through d7-e6-f5: answer Nxc6! bxc6 Bg5, NEVER Qxg4. NO f3 while my Be3 sits on e3: ...Nxe3 wins a piece free (T62R2). King safety after ...Qa5/...Rb8; count ...Bxh2+ before castling; no a7 grab with his knight loose.

## Opponents
- Muse Spark 1.3 Contributor (T63R1, my 0-1 as White): meets the English with ...e5/...Nc6/...Bc5/...Bb6, ...Na5 hitting c4, ...e4 and ...c5; patient (5:11 on one quiet ...Qb8), ZERO illegal, took every loose unit (fxe6, Rxd3, Bxh5, cxb4, bxa4) and converted a rook-down position without a slip. Give it no loose rook, no piece on its pawns' capture squares; expect it to sit tight, then win the endgame.
- Stockfish 19 (depth 4): instant, zero errors. Punishes loose pieces, hidden defenders, an unguarded c6, any piece on his e5-pawn's f6/d6 square, ...h6 met by Bxh6, a rook behind a moved pawn, and a shield pawn recaptured by a pawn that opens a file to my king. Builds Qg4 + h4-h5 + Re3/Rae1, plays ...d4 then ...Nb4/...Nd3+ (...Qf2#) in the English, and takes any 'offer' I cannot recapture. T62R2 it punished 9.f3?? with ...Nxe3 then could not break my compact shell (threefold). T63R2: after 9.Qg4 g6 it beat my Taimanov with Qg4/Bg5/h4-h5 - 14.Bf6! once my bishop left e7.
- GLM 5.3 Flash: English/reversed QGD as White, Taimanov/Modern as Black; checks pawn lines hard (T61R3 it took my bishop on e4 with its d3-pawn and my queen on b4 with its a3-pawn) and CONVERTS (Bc4+ then Rd1#). Leaks: plain captures win its undefended pieces, its QUEEN falls to a bishop kick on the d8 line (T61R5.2 ...h6?? Bxd8), its rim Nh4 to ...Bh7! ...g5! (T62R1). 6 illegal tries in T62R1, clock collapses (T58R1, T59R2 forfeits) yet it once thought 6:19 - never count on its flag. My 1-0s: T56R3, T56R5.2, T57R1, T58R1, T59R2, T60R5.2, T61R5.2, T62R1, T62R5.2; lost T60R2, T61R3.
- DeepSeek V4.1 Flash (mirror): solid Taimanov/English both colours, converts without gifts, 1-3 illegal tries. T61R1 (my 1-0): parked its queen on my c6-pawn and its knight on my e-pawn, then down a queen allowed 37.Qxd7! 38.Re8#. T60R1 draw: shuffled to threefold. T62R3 (my 0-1): same reversed QGD, answered my b4 with ...a5 and ...cxb5 and took my e2-pawn, d3-pawn and loose Rb1. T62S2G1 (my 0-1 as Black): punished 20...Qxd6 with 21.Nxc6 bxc6 22.Rxd6. It parks pieces on MY pawns' capture squares and takes any queen on an open file with its rook.

## Notes
- notes/black-english-reversed-qgd-t50r3.md; notes/black-taimanov-guards.md; notes/stockfish-dragon-queen-trade.md; notes/taimanov-black-g7-battery.md; notes/white-dragon-yugoslav.md; notes/white-taimanov-glm-t49r4.md; notes/white-taimanov-qd2-f4.md; notes/white-english-reversed-sicilian.md

## Record (condensed)
- v SF19: T62R2 1/2 (Dragon; 9.f3?? ...Nxe3 won B, 67-move shell, threefold at +10); losses T61R4 (13...Qxe5??, m39 Rf7#), T61R2 (m19 Qf2#), T60S1G1 (h-file Rh3#), T60R3 ...Qxa4??, T59 ...Nf6??/...Qxd6??, T59 Final ...Qa5??, T63R2 (Taimanov 12...Bc5?! 13...O-O?? 14.Bf6!, m20 Qxg7#), plus T53-T58.
- v GLM 1-0: T55R5.3, T56R3, T57R1, T58R1, T59R2, T60R5.2, T61R5.2, T62R1, T62R5.2 (her Qxc5?? Qxc5, Qe4#). 0-1: T60R2, T61R3.
- v mirror: 1-0 T56R1, T57R4, T58S2G1, T59R3, T59S2G1, T61R1; 1/2 T60R1; 0-1 T57R3, T58R3, T62R3 (up R+2P at m26, lost to my own loose units), T62S2G1.
- v Muse Spark: 0-1 T63R1 (up a FULL rook at m34: 35.Re6?? fxe6, ...Rxd3, ...Be8, lost).
