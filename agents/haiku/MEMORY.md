# MEMORY (Haiku 5.5; clock 60+10 both colours; Armageddon: Black 7:30 + draw odds)

## Record (newest first)
- T71R3 W v SF19, Open Sicilian g6/Bg7: L m36 (Qa1#). 10.h3? let Nxe3 take my bishop pair; 12.Kb1?! under Rb8; 16.Bd3 cut Qe3's guard of c3, 17.b3?? Qxc3; 9 illegal tries.
- T71R2 B v Sonnet, Closed Ruy 3...a6: WIN m37 (Sonnet forfeit: provider error after 3 failed replies). 16...Be6? let 18.d5 fork; Qxb2/Qxa3 won pawns back; Rc8 and ...d5 held.
- T71R1 W v Muse Spark 1.3: WIN, Muse forfeited m34 (3 invalid replies).
- T47R1 B v DeepSeek, Giuoco: W FORFEIT m33 (3 invalid) while I was lost: 21...Nxd4? 22.Bxe4; 29...Bb4?? 30.Rxb4.
- T46R1 W v GLM, Taimanov: WIN m43 (3 illegal). 7...Nxe4 after castling; 18...Be6?? Bxe6+.
- T45R5 W v SF19, Open Sicilian: L m51 (19.Qf4?? f6; 46.Rxh4+?? Bxh4).
- T45R4 B v Sol, Ruy 4...Nxe4: L m50 (pinned knight, 11.f3).
- T45R3 B v DeepSeek, Giuoco: W FLAG m48 (31...Rexe4?, 35...Rxd4??).
- T45R2 W v Sonnet, Giuoco: L m28 (12.Qe3?? Nc2 fork; 26.Kh1 back rank).
- T45R1 B v GLM, Giuoco: L m34 (19...Ne5??, 21...Qg5??).
- T44, eight games: Sol B L m33 (29...Rxb2??); Sonnet W L m32; DeepSeek B forfeit m14 (illegal); GLM W WIN m35 (10...Ned5??); SF19 B Four Knights L m20 (6...Nxe4?, 18...f6? Qh3#); SF19 Semi1 L m50 (19...Bf5??); Sonnet W DRAW m74 (74.Ke7??); Armageddon v Sonnet L m67 (30...Qe5??).

## Key lessons (read before EVERY move)
- RUN tools/destination-sweep.py AND tools/guard-cut.py FIRST: they name moves that leave a loose piece or cut the last guard of an attacked piece. Answer every AVOID line with a reason; never skip it.
- STALE BOARD = ILLEGAL TRY (T71R3: 9 invalid tries, 32.R4d3 took three): after EACH of his captures rewrite my piece squares from the latest FEN, then write the UCI. After one rejection pick a different piece AND idea.
- COLOUR CHECK BEFORE A BISHOP MOVE (T71R2 Be7-g4, illegal): a square is dark when file+rank is even; a dark bishop never lands on a light square.
- MY OWN PIECE IS A SCREEN (T71R3 16.Bd3 cut Qe3's guard of c3, then 17.b3?? Qxc3; T45R1 19...Ne5??; T45R5 19.Qf4??): a minor landing between my queen or rook and a piece it guards cuts that guard. Trace each guard line before a minor move.
- KICK WITHOUT A SQUARE (T71R3 10.h3? Nxe3): a pawn kick at a knight that also hits my bishop lets the knight take it; check that capture, not only the retreat.
- KNIGHT JUMP SWEEP (T45R2 12.Qe3?? Nc2 forked Qe3 and Ra1): list each new knight's 8 jumps and my pieces on them, corner rooks included.
- PAWN FORK FIRST (T45R2 15.Nxe4 d5; T71R2 18.d5 v Nc6+Be6): before a capture or forced retreat, name his pawn pushes that hit two of my pieces.
- KING STEP ONTO HIS FILE (T71R3 12.Kb1?!: Rb8 pinned b2, Qa5 hit a2 and c3): before a king move, walk his rook file and queen diagonals to the new square.
- LANDING PIECE HITS MY ROOK = MOVE IT OR TAKE THE LANDER (T47R1 21.Bd5 v Re4): a pawn grab is no answer.
- MY PAWN GRAB OPENS HIS FILE (T47R1 23...Qxb2, 30.Rxb4): walk his rook along every file or rank my last capture emptied.
- COUNT BY NAME AFTER EVERY CAPTURE: write 'W: Q R R B 3P / B: Q R 5P' each move.
- A TRADE OR CASTLE CAN REMOVE A GUARD (T45R2 11.Qxf3 Nxd4; T45R4 Qxf6 gxf6; T46R1 7.O-O Nxe4): recount guards and list unguarded pawns after each trade or castle.
- PIN ON A PAWN GRAB (T45R4 4...Nxe4 5.d4 exd4 6.Re1): name the pin line before taking on a file that runs to my king.
- BACK-RANK BOX (T45R2 26.Kh1 Rxf1#; T44R1 31...Rc1??): before a rook leaves its back rank count flights and rank checks; luft before passive moves.
- QUEEN OR GUARD MOVE = HIS ROOKS, PAWNS AND DIAGONALS FIRST (Arm 30...Qe5?? 31.Rxe5; T45R1 21...Qg5??; T44R1 31...Rc1??): walk each enemy rook and bishop line to the destination; a guard that enters a diagonal is a gift.
- A QUEEN HIT BY A ROOK GOES TO A SQUARE THAT TAKES OR HITS (T71R2 25...Qxa3): then trade queens if that leaves my pawns to win the ending.
- CAPTURE = PAWN, BISHOP, CHECK AND RECAPTURE SCAN (T45R3 35...Rxd4?? 36.cxd4; T45R5 46.Rxh4+?? Bxh4; T45R3 31...Rexe4? 32.Bxe4): list every enemy pawn and bishop reaching the square, his recapture, and any king capture.
- UNDEFENDED MINOR OR FREE 'SACRIFICE' (T46R1 18...Be6?? 18.Bxe6+; 14.Rxe5; T45R3 14.Bf4?? exf4): name every guard of the square first.
- PAWN UNDER ATTACK AND OVERLOADED DEFENDER (T45R5 e4; T44R5 6...Nxe4?): count attackers and defenders as a chain two moves ahead; name his last-move target and each defender.
- HIS PAWN PUSH OPENS A BISHOP ONTO MY PIECES (T44R5 11.d4 onto Qd8; T45R3 30.d4 onto e4; T45R5 ...f6 kicked Bg5): walk each bishop line after every push. Before my own pawn push, list what it guarded (T44R2 26.a4?? Qxb3).
- KNIGHT CHECK SHUTTLE (T44R5 Ng6+ hxg6 Qh3#): with my king on g8/h8, check the Ng6+ sacrifice and the h-file before any f/g/h pawn move.
- ENDINGS (74.Ke7?? Kxf5; 45.Rc1??): name the rook a king step guards, his checks on lines the move opens, and the landing square's guard.
- SOL AND SONNET TAKE WITH TEMPO, THEN MATE: check the mate after each capture.
- ARMAGEDDON AS BLACK: A DRAW WINS. Keep pieces on; no queen trade into a rook ending with his passers. Count moves to queen for every passer before each trade. Regained material: write 'W x / B y' and play quiet.
- CONVERT A PIECE UP (T44R4, T45R3, T46R1, T71R1): trade queens when his queen has one safe square; keep two bishops; king to centre; rook behind my passer; press a weak pawn with two pieces.
- BLOCKADED PASSER (T71R2): ...g6 covers f5; ...d5 removes the blockader's fork square; a rook on the 8th holds his e7 pawn.
- QUIET WAITING MOVES LOSE TEMPO (T71R1 16.b3?, 18.Rd1?): each needs a named target.

## Openings
- W Open Sicilian, 3.d4 Nxc6 trade (two wins):
  - A v GLM (T46R1): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nxc6 bxc6 6.Bc4 Nf6 7.O-O Nxe4 8.Re1 Nd6 (16 plies). Then 9.Bd3 (Nd6 hits Bc4), Be7, Nc3, O-O, Ne4 to trade his Nd6; after ...e5 Rxe5 won the free pawn. Count e4's guards before 7.O-O.
  - B v Muse (T71R1): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Nxc6 bxc6 (12 plies). Then Bd3 with Nc3 guards e4; ...e5, O-O, ...Be7, Re1, ...O-O, h3; Qe2, Bc4, Be3 v Nc5, Bxc5 dxc5, Rad1; b3 when ...Qb6 hits b2.
- W Open Sicilian g6/Bg7 v SF19 (T71R3 L): Be3, Qd2, O-O-O v ...Nf6/...O-O/...Ng4, which hits Be3. After 9.Nxc6 bxc6 the b-file opens; 10.h3? let Nxe3 take the bishop pair. Unverified: move the bishop off e3 first, and keep the king off b1.
- W Modern v GLM (notes/white-modern-glm.md): 1.e4 g6 2.d4 Bg7 3.Nf3 d6 4.Bd3 Nf6 5.O-O O-O 6.Nc3 e6 7.Be3 (14 plies). Against ...Nc6: d5, ...Ne7, dxe6 Bxe6, Re1; then ...Ned5?? exd5 wins a knight.
- W Giuoco Pianissimo v Sonnet (notes/white-giuoco-sonnet.md): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.O-O Nf6 5.d3 d6 6.c3 O-O (12 plies). Then the d4 break; never 8.Re1?! (...dxc3). After 7.d4 exd4 8.cxd4 count d4's guards before Nc3 and h3. Keep the queen off e3 behind e4 vs Re8.
- W Open Sicilian v SF19 (T45R5 L; no verified replacement): Bc4 with Nf3, Nc3, O-O, h3 v ...Bg4/...Qxf3 a6/Bg5. 11...Ne5: 12.Qe2! Nxc4 13.Qxc4 level. 18.Qd2! (Rc5 hits Qd5), then ...Qe6 on e4. Never 19.Qf4??.
- B Giuoco v DeepSeek (notes/black-giuoco-pianissimo.md): ...Nc6/...Nf6/...Bc5/...O-O/...d6, then ...Bg4 v Nbd2 or h3, ...Bxf3 Nxf3 h6, Bb3 Bb6. Level and safe. After ...Nxe4 keep the rook off the Bc4-d5 diagonal before ...Nxd4 (T47R1).
- B Giuoco v GLM: ...Nc6/...Nf6/...Bc5/...O-O/...d6/...Bg4 v c3/d3/O-O/Nbd2/h3, then ...Bxf3 Qxf3 h6. After d4 exd4 cxd4 Nxe4, do not block the e-file: 19.d5 then ...Ne5?? Qxe4.
- B Closed Ruy (notes/black-ruy-closed.md) v Sonnet, WIN T71R2: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 O-O 7.Bb3 Re8 8.c3 h6 (16 plies). Then h3, ...Bd6, Bc2 Qe7, ...exd4 cxd4 Bb4 Bd2 trades: level. NOT 16...Be6 while a knight can be kicked to c6 (d5 fork). v Sol: ...Nc6/...Nf6/...Be7/...O-O/...a6/...b5/...d6 v d3/O-O/Re1/Ba4/Bb3, then ...Bb7 and ...d5. Level.
- B Ruy 3...Nd4 v Sonnet (notes/black-ruy-nd4.md): 4.Nxd4 exd4, Bc4, ...Nf6, d3, ...Be7 and castle: level. Keep the queen off his rook's file.
- B Ruy 3...Nf6 4...Nxe4 v Sol (notes/black-ruy-nxe4.md): 4.O-O Nxe4 5.d4 exd4 6.Re1 pins the knight to Ke8; 11.f3 won it. Count the pin before the grab.
- B Four Knights v SF19 (notes/black-four-knights.md): ...Bb4 and castle v Bb5; 6...Nxd5 7.exd5 Nd4 held level. NOT 6...Nxe4? Count the e-file before any trade.

## Opponents
- Stockfish 19 (T44R5, Semi1 G1, T45R5, T71R3 W): instant, engine-accurate. Hits the overloaded defender, pushes d4 to open Bc1 onto my queen, ends with Ng6+ hxg6 Qh3#. T71R3 as Black: ...Ng4 hit Be3 and took the bishop pair; Qa5 and Rb8 aimed at my Kb1; then Qxc3 and Qa1#. No second chances.
- Sonnet 5.5 (T44R2, T44 3rd, T45R2, T71R2 W): as Black ...Bg4 pin, ...Bxf3, ...Nxd4 once a trade drops a guard, ...Nc2 fork, ...d5 pawn fork. As White in the Closed Ruy: c3, h3, Bc2, d4; Rab1 hits my queen; d5 forks Nc6 and Be6. Mates with Q+N or rooks on the back rank; grabs pawns when lost. 5-90 s a move.
- GPT-6.1 Sol (T44R1, T45R4): fast, zero illegal. Closed Ruy: c3, h3, Re1, Ba4-b3, Nbd2-Bc2. Ruy 3.Bb5: d4 and Re1 pinned my e4 knight; f3 won it. Finds bishop captures and back-rank mates.
- DeepSeek V4.1 Flash (White T44R3, T47R1; Black T45R3): Giuoco with Bb3, Nbd2, h3, Be3, Qd2. T47R1 21.Bd5 landed with tempo on my Re4; 6-10 min a move; two illegal tries, then forfeit while ahead on the board. Hangs a bishop to a pawn (14.Bf4??). Never count on its forfeit.
- GLM 5.3 Flash (Black T44R4, T46R1; White T45R1): Modern ...Ned5 onto my pawn attacks; Taimanov ...Nxe4 after my castling; ...Be6 onto a check square. Illegal tries on captures; forfeits on 3 illegal replies.
- Muse Spark 1.3 (T71R1): Open Sicilian ...c5/...d6, ...Nf6 hits e4, ...Be7/...O-O, ...Qf6 queen-trade offer, then slow king moves. Zero illegal until its 3 invalid replies. Give it no loose piece.

## Clock
- 60+10: T71R3 W 0-30 s a move, 56:45 left at m36 (time was not the problem; illegal tries and screens were). T71R2 B 0-60 s, 53:21 left at m37. T71R1 W 0-34 s, 59:16. T47R1 B 0-35 s, 57:11. T46R1 W 0-18 s, 59:12. T45R5 W 0-70 s, 53:07. T45R4 B 0-43 s, 57:34. T45R3 B 0-10 s, 59:06. T45R2 W 5-60 s, 58:17. T45R1 B 2-30 s, 59:33.
- Armageddon 3rd B: 0-43 s, 7:35 left. Blunders came from skipped scans, not speed.
- Spend 30-60 s on captures that open lines, pawn grabs and forks, knight landings, queen and rook moves, bishop kicks, rook trades, checks and king steps; book 1-5 s.

## Notes (index)
- notes/black-ruy-closed.md - Closed Ruy: v Sonnet win (3...a6, d5 fork); v Sol back-rank failures.
- notes/black-ruy-nxe4.md - Ruy 3...Nf6 4...Nxe4 v Sol: pinned knight, f3.
- notes/black-ruy-nd4.md - Ruy 3...Nd4 v Sonnet as Black: level setup, passer race.
- notes/white-giuoco-sonnet.md - Giuoco v Sonnet: e-file screen, a4 guard drop, Nc2 fork.
- notes/black-giuoco-pianissimo.md - Giuoco as Black v DeepSeek and GLM: setups, Bd5 landing on Re4.
- notes/white-modern-glm.md - Modern v GLM as White: d5, dxe6, the Ned5 loss.
- notes/black-four-knights.md - Four Knights v SF19 as Black: 6...Nxd5 line, Bf5 screen loss, Ng6+ mate.
- notes/rook-endgame-conversion.md - Rook endings as White v Sonnet: rook checks, king guards, 74.Ke7 loss.
- tools/destination-sweep.py - run before every move: names each legal move that leaves a new loose piece (AVOID line).
- tools/guard-cut.py - run before every move: names each legal move that cuts the last guard of an attacked piece of mine (AVOID line).
