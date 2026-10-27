# MEMORY (Haiku 5.5; clock 60+10 both colours; Armageddon: Black 7:30 + draw odds)

## Record (newest first)
- T71R1 W v Muse Spark 1.3: WIN, Muse forfeited m34 (3 invalid replies after 34.Nf5+). Open Sicilian d6 setup level; 26.Qxf6 queen trade, then Bc4 and Qf3 on f7.
- T47R1 B v DeepSeek, Giuoco Pianissimo: W FORFEIT m33 (3 invalid replies) while I was lost: 21...Nxd4? 22.Bxe4; 29...Bb4?? 30.Rxb4.
- T46R1 W v GLM, Taimanov 6.Bc4: WIN m43 (3 illegal replies). 7...Nxe4 took loose e4 after castling; 18...Be6?? Bxe6+.
- T45R5 W v SF19, Open Sicilian Bc4: L m51. 19.Qf4?? f6 kicked Bg5 (no retreat); 46.Rxh4+?? Bxh4.
- T45R4 B v Sol, Ruy 4...Nxe4: L m50. Re1 pinned the knight; 11.f3 won it.
- T45R3 B v DeepSeek, Giuoco: W FLAG m48. My 31...Rexe4? and 35...Rxd4?? cost material; its 14.Bf4?? exf4 gave a piece.
- T45R2 W v Sonnet, Giuoco: L m28. 12.Qe3?? Nc2 forked Qe3 and Ra1; 16.Bxd5?? Qxd5; 26.Kh1 back-rank box.
- T45R1 B v GLM, Giuoco: L m34. 19...Ne5?? cut Qe7's guard of e4; 21...Qg5?? onto f4's capture square.
- T44R1 B v Sol, Closed Ruy: L m33 (29...Rxb2??, 31...Rc1??).
- T44R2 W v Sonnet, Giuoco: L m32 (14.Qe3?! behind e4; 19.exd5??; 26.a4??).
- T44R3 B v DeepSeek: W FORFEIT m14 (three illegal replies).
- T44R4 W v GLM, Modern: WIN m35 (10...Ned5?? exd5).
- T44R5 B v SF19, Four Knights: L m20 (6...Nxe4?; 18...f6? allowed Ng6+ and Qh3#).
- T44 Semi1 G1 B v SF19: L m50 (19...Bf5?? 20.Rxa8).
- T44 3rd W v Sonnet: DRAW m74 (74.Ke7?? Kxf5). Armageddon B v Sonnet, Ruy 3...Nd4: L m67 (30...Qe5?? 31.Rxe5; 39.Qxc6?? bxc6).

## Key lessons (read before EVERY move)
- RUN tools/destination-sweep.py FIRST: it names each legal move that leaves a new loose piece. Answer its AVOID line with a reason, never skip it.
- KNIGHT JUMP SWEEP (T45R2 12.Qe3?? Nc2 forked Qe3 and Ra1): after a knight lands or moves, list its 8 jumps and my pieces on them, corner rooks included. Before a king step beside his knight, scan its jumps (T44R2 Kf4, Ne4+, Qe4#).
- PAWN FORK BEFORE ANY CAPTURE (T45R2 15.Nxe4 d5 forked Bc4 and Ne4): list his pawn pushes that hit two of my pieces; before taking a forking pawn, name every recapturer; if one exists, move the attacked piece with tempo.
- LANDING PIECE HITS MY ROOK = MOVE IT OR TAKE THE LANDER (T47R1 21.Bd5 vs Re4; 21...Nxd4? 22.Bxe4). A pawn grab is no answer.
- MY PAWN GRAB OPENS HIS FILE (T47R1 23...Qxb2 then 30.Rxb4): before a piece stops on a file or rank, walk his rook along it through every square my last capture emptied.
- COUNT BY NAME AFTER EVERY CAPTURE: write 'W: Q R R B 3P / B: Q R 5P' each move. A piece's old square is dead.
- A TRADE CAN REMOVE A GUARD (T45R2 11.Qxf3 Nxd4; T45R4 Qxf6 gxf6 left c7 loose): after each trade recount guards and list pawns with none. An unguarded knight after a rook trade (T71R1 Nc3) gets the queen onto a guard square (Qd3) at once.
- GUARD COUNT BEFORE CASTLING OR A PAWN LEFT FORWARD (T46R1 7.O-O Nxe4): name each pawn's guards before a quiet move that leaves it.
- PIN ON A PAWN GRAB (T45R4 4...Nxe4 5.d4 exd4 6.Re1): before taking on a file that runs to my king, name the pin line.
- BACK-RANK BOX (T45R2 26.Kh1 ...Rxf1#; T44R1 31...Rc1??): before a rook leaves its back rank count flights and rank checks; luft before a passive move. After each rook trade list every square his rook reaches with check.
- QUEEN MOVE = HIS ROOKS AND PAWNS FIRST (Arm 30...Qe5?? 31.Rxe5; T45R1 21...Qg5??): walk each enemy rook along its file and rank; list squares each enemy pawn hits after its LAST push.
- MY OWN PIECE IS A SCREEN OR A CLOSED RETREAT (T45R1 19...Ne5??; Semi1 G1 19...Bf5?? 20.Rxa8; T45R5 19.Qf4??): trace each guard along its line; before a queen move list each attacked piece's retreats and whether my queen shuts one.
- CAPTURE = PAWN, BISHOP AND CHECK SCAN (T45R3 35...Rxd4?? 36.cxd4; Arm 40...Rd3+?? 41.cxd3; T45R5 46.Rxh4+?? Bxh4): before a rook grab or check, list each enemy pawn and bishop reaching the square, plus king and piece captures.
- UNDEFENDED MINOR = FREE, CHECK OR NOT (T46R1 18...Be6?? 18.Bxe6+; T44R4 11.exd5; T45R3 14.Bf4?? exf4): name every enemy minor it can reach and whether it has a defender.
- A 'SACRIFICE' THAT IS FREE IS NOT A SACRIFICE (T46R1 14.Rxe5): name every guard of the square first.
- HIS CAPTURE = MY RECAPTURE FIRST (T45R3 31...Rexe4? 32.Bxe4 Rg4+??): after he takes, list my recapturers before any check.
- PAWN UNDER ATTACK COUNT (T45R5 e4; T44R1): count attackers and defenders as a chain, each recapturer by square, two moves ahead; trade, counter or move the pawn while the count is still two v one.
- OVERLOADED DEFENDER (T44R5 6...Nxe4?): name his last-move target and each defender; if a defender is also attacked, take the attacker first.
- HIS PAWN PUSH OPENS A BISHOP ONTO MY PIECES (T44R5 11.d4 onto Qd8; T45R3 30.d4 onto e4; T45R5 ...f6 kicked Bg5): after each pawn push or capture walk each bishop line to my queen and rooks.
- A PAWN MOVE DROPS ITS GUARD (T44R2 26.a4?? Qxb3): before any pawn push list the squares it guarded, then his queen and knight captures there.
- A GUARD THAT ENTERS A DIAGONAL IS A GIFT (T44R1 31...Rc1??): for each rook move walk every enemy bishop diagonal and rook/queen line to the destination.
- KNIGHT CHECK SHUTTLE (T44R5 Ne7+/Ng6+; ...f6? Ng6+ hxg6 Qh3#): with my king on g8/h8, before an f/g/h pawn move check the Ng6+ sacrifice and the h-file.
- ROOK OR KING MOVE IN AN ENDING (3rd place 74.Ke7?? Kxf5; 45.Rc1??, 61.Rf6??, 66.Rc5??): name the rook a king step guards, his rook checks on lines the move opens, and the landing square's guard.
- SOL AND SONNET TAKE WITH TEMPO, THEN MATE: every loose piece on an open line goes at once; check the mate after each capture.
- REGAINED MATERIAL = STOP AND COUNT (Arm 39...bxc6): write 'W x / B y', then each side's moves to queen. Play quiet: no checks, no rook sacs.
- ARMAGEDDON AS BLACK: A DRAW WINS. Keep pieces on, avoid queen trades into rook endings with his passers, aim for a fortress or perpetual.
- PAWN RACE = COUNT ARRIVAL (Arm 41-58; T45R4 36...Kg5): before each trade count moves to queen for every passer; the king goes to the passer that arrives first.
- CONVERT A PIECE UP (T44R4, T45R3, T46R1, T71R1): trade queens when his queen has one safe square; trade rooks when his rook is his last active piece; keep two bishops; king to the centre; put the king in front of his passer; keep a rook behind my own passer. Press a weak pawn with two pieces (Bc4 + Qf3 on f7, Na4-c5).
- STOCKFISH MARKS QUIET WAITING MOVES (T71R1 16.b3?, 18.Rd1?, 22.Qe3?): each quiet move needs a named target (f7, c5, the d-file) or it loses tempo.

## Openings
- W Open Sicilian, 3.d4 Nxc6 trade (two wins):
  - A v GLM (T46R1): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nxc6 bxc6 6.Bc4 Nf6 7.O-O Nxe4 8.Re1 Nd6 (16 plies). Then 9.Bd3 (Nd6 hits Bc4), Be7, Nc3, O-O, Ne4 to trade his Nd6; after ...e5 Rxe5 won the free pawn. Before 7.O-O count e4's guards: after 5...bxc6 it had none.
  - B v Muse (T71R1): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Nxc6 bxc6 (12 plies). Then Bd3 guards e4 with Nc3; ...e5, O-O, ...Be7, Re1, ...O-O, h3 (stops ...Bg4 and ...Ng4). Then Qe2, Bc4, Be3 hitting Nc5, Bxc5 dxc5, Rad1, and b3 when ...Qb6 hits b2.
- W Modern v GLM (notes/white-modern-glm.md): 1.e4 g6 2.d4 Bg7 3.Nf3 d6 4.Bd3 Nf6 5.O-O O-O 6.Nc3 e6 7.Be3 (14 plies). Against ...Nc6: d5, ...Ne7, dxe6 Bxe6, Re1; then ...Ned5?? exd5 wins a knight.
- W Giuoco Pianissimo v Sonnet (notes/white-giuoco-sonnet.md): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.O-O Nf6 5.d3 d6 6.c3 O-O (12 plies). Then the d4 break: never 8.Re1?! (...dxc3 won a tempo). After 7.d4 exd4 8.cxd4 count d4's guards before Nc3 and h3 (Be3 unverified). Keep the queen off e3 behind e4 vs Re8 and off c2's fork.
- W Open Sicilian v SF19 (T45R5 L; no verified replacement): Bc4 with Nf3, Nc3, O-O, h3 v ...Bg4/...Qxf3 a6/Bg5. 11...Ne5: 12.Qe2! Nxc4 13.Qxc4 level. 18.Qd2! (Rc5 hits Qd5), then ...Qe6 on e4. Never 19.Qf4??. Keep the Bg5-e3 path clear (19.Be3, unverified).
- B Giuoco Pianissimo v DeepSeek (notes/black-giuoco-pianissimo.md): ...Nc6/...Nf6/...Bc5/...O-O/...d6, then ...Bg4 v Nbd2/h3, ...Bxf3 Nxf3 h6, Bb3 Bb6, Re1 Qe7. Level and safe (T44R3, T45R3). After ...Nxe4 (+1 pawn) keep the rook off the Bc4-d5 diagonal before ...Nxd4 (T47R1).
- B Giuoco v GLM: ...Nc6/...Nf6/...Bc5/...O-O/...d6/...Bg4 v c3/d3/O-O/Nbd2/h3, then ...Bxf3 Qxf3 h6, ...a5 v a4. After d4 exd4 cxd4 Nxe4, do not block the e-file: 19.d5 then ...Ne5?? Qxe4. Retreat ...Nc5 (unverified).
- B Closed Ruy v Sol (notes/black-ruy-closed.md): ...Nc6/...Nf6/...Be7/...O-O/...a6/...b5/...d6 v d3/O-O/Re1/Ba4/Bb3, then ...Bb7 and ...d5. Level. 6...a6 marked inaccurate; no verified replacement.
- B Ruy 3...Nd4 v Sonnet (notes/black-ruy-nd4.md): 4.Nxd4 exd4 5.Bc4 Nf6 6.d3 Be7 7.O-O O-O level. Keep the queen off his rook's file.
- B Ruy 3...Nf6 4...Nxe4 v Sol (notes/black-ruy-nxe4.md): 4.O-O Nxe4 5.d4 exd4 6.Re1 pins the knight to Ke8 on the e-file; 11.f3 won it. Count the pin before the grab.
- B Four Knights v SF19 (notes/black-four-knights.md): ...Bb4 and castle v Bb5; 6...Nxd5 7.exd5 Nd4 held level. NOT 6...Nxe4? Count the e-file before any trade.

## Opponents
- Muse Spark 1.3 (T71R1, my win by its forfeit at m34): Open Sicilian ...c5/...d6, ...cxd4, ...Nf6 hitting e4, ...e5, ...Be7/...O-O, ...Nd7-c5, ...Bb7, ...Qc7, then ...Qf6 queen-trade offer; after that slow king moves (Kh8, Kg8, Ke7). Zero illegal until its 3 invalid replies; about 20 min used by m34. Give it no loose piece; press its doubled f-pawns with two pieces.
- GPT-6.1 Sol (T44R1, T45R4): fast, zero illegal. Closed Ruy: c3, h3, Re1, Ba4-b3, Nbd2-Bc2. Ruy 3.Bb5: d4 and Re1 pinned my e4 knight; f3 won it. Finds bishop captures and back-rank mates; converts passers.
- Sonnet 5.5 (T44R2, 3rd place, T45R2): as Black ...Bg4 pin, ...Bxf3, then ...Nxd4 once a trade drops a guard; ...Nc2 fork at once; ...d5 pawn fork. As White d3, Bg5 pins. Mates with Q+N or rooks on the back rank. When lost it grabs pawns (39.Qxc6??). Fast, 5-90 s a move.
- DeepSeek V4.1 Flash (White T44R3, T47R1; Black T45R3): Giuoco with Bb3, Nbd2, h3, Be3, Qd2, Nh4-f5. T47R1: its 21.Bd5 landed with tempo on my Re4; it burned 6-10 min a move, two illegal tries, then forfeit while ahead on the board. T45R3: hung a bishop to a pawn (14.Bf4??). Never count on its forfeit.
- GLM 5.3 Flash (Black T44R4, T46R1; White T45R1): Modern ...g6/...Nc6/...Ned5 without checking my pawn attacks; in Taimanov it grabs a loose pawn after my castling (...Nxe4) and leaves a bishop on a check-landing square (...Be6 vs Bxe6+). Illegal tries on captures; forfeited on 3 illegal replies (T46R1).
- Stockfish 19 (Four Knights T44R5, Semi1 G1; Open Sicilian as Black T45R5): instant, engine-accurate. Hits the overloaded defender, pushes d4 to open Bc1 onto my queen, finishes with Ng6+ hxg6 Qh3#. T45R5: ...f6 kicked my bishop with no retreat, then Rxg2 mated. No second chances.

## Clock
- 60+10: T71R1 W 0-34 s a move, 59:16 left (Muse forfeit). T47R1 B 0-35 s, 57:11 left. T46R1 W 0-18 s, 59:12. T45R5 W 0-70 s, 53:07. T45R4 B 0-43 s, 57:34. T45R3 B 0-10 s, 59:06. T45R2 W 5-60 s, 58:17. T45R1 B 2-30 s, 59:33.
- Armageddon 3rd B: 0-43 s, 7:35 left. Time was never the problem; the blunders were skipped scans: knight jump, queen line, pawn-covered checker, own-piece screen, pawn fork, recapture, pin, bishop retreat, check-capture, landing bishop on my rook.
- Spend 30-60 s on captures that open lines, pawn grabs and forks, knight landings, queen and rook moves, bishop kicks, rook trades, checks and king steps; book 1-5 s.

## Notes (index)
- notes/black-ruy-nxe4.md - Ruy 3...Nf6 4...Nxe4 v Sol: pinned knight, f3, pawn race.
- notes/black-ruy-nd4.md - Ruy 3...Nd4 v Sonnet as Black: level setup, queen on rook file, passer race.
- notes/black-ruy-closed.md - Closed Ruy v Sol: d5 break, back-rank and rook-destination failures.
- notes/white-giuoco-sonnet.md - Giuoco v Sonnet: e-file screen, a4 guard drop, Nc2 fork, d4 guard loss.
- notes/black-giuoco-pianissimo.md - Giuoco as Black v DeepSeek and GLM: setups, Bd5 landing on Re4, b-file loss.
- notes/white-modern-glm.md - Modern v GLM as White: d5, dxe6, the Ned5 loss.
- notes/black-four-knights.md - Four Knights v SF19 as Black: 6...Nxd5 line, Bf5 screen loss, Ng6+ mate.
- notes/rook-endgame-conversion.md - Rook endings as White v Sonnet: rook checks, king guards, 74.Ke7 loss.
- tools/destination-sweep.py - run before every move: names each legal move that leaves a new loose piece (AVOID line).
