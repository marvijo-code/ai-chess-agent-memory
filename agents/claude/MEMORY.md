# MEMORY (chess tournament; clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy White: DeepSeek 8 W; Sol 3 W, 3 L, 1 D (T16R3 L mate 40).
- Sicilian White vs DeepSeek: 5 W (Yugoslav 3/3).
- Chigorin Black: DeepSeek 10 W 1 D; Sol 2 W, 5 L, 2 D.
- Sol as Black: QGD 3 W 1 L; vs 3.Bc4 2 L.
- vs SF as White: Alapin lost 4x; Maroczy drew T13R3, T14R2 from lost spots. vs SF as Black 3.Nc3: 8 L, 4 D (T16SF2G1 L mate 35).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count (max 3; T16R3 two tries cost 2:50). Trace the path square by square INCLUDING MY OWN pieces (Be3 blocked Re1-e4); destination not my own piece; list pins on my king.
- QUEEN-SCREEN (T16SF2G1 Qe5 v Qa5 through ONE Bd5; 22.c4 Be6?? 23.Qxe5+): never leave my queen on a rank/file/diagonal with his queen/rook behind a lone screen of mine; a pawn push hits the screen, and the screen's own move can block my guard (Be6 blocked Re8). Before moving any screen/guard: 'who guards my queen AFTER this, path square by square?' Trade queens or sidestep first.
- E4 DEFENDER COUNT (T16R3 21.b4? axb3 22.Bxb3 Ncxe4!): with Be3 on the e-file Re1 does NOT guard e4. Recount e4's guards BY PIECE after every exchange; vs ...Nc5 play Bxc5 or keep Bc2/Bb1 home; never b4. (My own Black plan: ...Na6-c5, ...Ncxe4.)
- LONG DIAGONAL (T16R3 29.Nd2 Bxa1): once b2/d4 left and ...e4 clears e5, Bf6 hits Ra1. Move the rook BEFORE ...e4/...Bf6; ...e4 also forked Qd3+Nf3.
- GUARD-OF-F7 CHECK (T16R1 11...Re8?? 12.Qxf7+ mate): before ANY move write 'his checks/captures after this move'; name guards of f7/h7 BY PIECE. Never move Rf8 while f7 is hit twice.
- DESTINATION CHECK (T15SF2G1G1 23...Nxd5?? 24.Qxd5): before ANY capture write 'square X: attacked by [all, incl. queen/rook down open lines], defended by [mine]'. A 'free' pawn is bait.
- NO REPEAT WHEN AHEAD (T15R3: 5 pawns v 2, drew by Nb4+/Nd5+ x3): at the FIRST repeat play another move.
- ATTACKED-PIECE (T15R1 11...Bxc3?? 12.Qxc3): pawn hits my bishop -> RETREAT; list every piece his move attacks (incl. discovered) and who defends it.
- CAPTURE-CHAIN (T14SF2G1 25...Qxc1?? Q+R for R+B): write the chain with values BEFORE capturing; the FIRST capturer is lost.
- GUARD/PATH CHECK (T14R3 20...Bxf5 removed b5's only guard; T13R2 23.Bd3?? Nxd3): before ANY trade/move list what it guards and trace every line; enemy pawns block my rook lines.
- MAROCZY VS SF (T14R2): vs 11...Ng4 play 12.Bxg4 Bxg4 13.f3, NOT 12.h3?!. Count attackers vs defenders on c4 (T13R3 20.Nd4? Rxc4).
- PASSIVE-DRIFT vs SF: every move needs a named plan. BOOK DEVIATION LOSES: at the first branch calculate HIS best reply incl. Qxf7+/Bxf7+ and pawn pushes/forks hitting my minors. SAC CHECK: his BEST reply first.
- CONVERSION (mates T14R1/T15R2/T15R5.2/T16R2; T13R1 B+B+N vs pawns = DRAW): list his checks, safe captures only, trade rooks when up, rook to 7th, passed pawn, KING up, never repeat, stalemate check each ply. Pawn up in opposite-colored bishops = draw; keep rooks.
- CHIGORIN VS DEEPSEEK (T16R2 W): 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7, ...Rfe8, ...h6, ...Rac8; vs 19.d5 Nb4 20.Bb1; 21.Nf5 Bxf5 22.exf5 Nbxd5 wins d5. It hangs queens: after each odd move list my captures.
- VS SF 3.Nc3 AS BLACK (see note): 3...Nf6 4.Bb5 Bb4. A) 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 (ONLY) 10.Bc4: try 10...Bd6; never Bxd2, Qf6, Bc5, 3...Bc5. B) 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 (pins e4) Qe7 8.dxc6 dxc6 9.Bxc6+ bxc6 10.Nd4: NOT 10...c5? (11.Nc6 wins the b4 pawn); try 10...Bd7 (guards c6). Think 3+ min at moves 10 AND 11, and again at 17-22.
- LUFT: h3 by move 9-12 but not at the cost of Be3. Before rook trades: 'Qb1+/Qa1+, my only blocker?' VS PAWN STORMS: trade outpost knight, ...Bf6 vs g5, defended queen trades.
- SF never errs; Q for R/minor is a LOSS. DeepSeek/Sol hang pieces: after EVERY odd enemy move list my options. Sol takes every real free pawn (Rxa3, Bxa1, Rxc2): none of mine may hang. Q=9 R=5 B/N=3.
- TIME: book 1-8 s; 30-120 s at captures, trades, queen moves, breaks, first non-book move; spend it listing HIS checks/captures and my blocked lines, not justifying. Recapturing a hanging piece <=60 s. When lost vs SF play 3-8 s.
- Armageddon: White (draw loses) solid, luft first; Black (draw wins) safest setup.
- Openings White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy (9.h3; vs 7...O-O 8.d3). Vs 1...c5 DeepSeek: Yugoslav/Rauzer; vs SF: 2.Nf3 open Sicilian + Maroczy (12.Bxg4!), never Alapin.
- Openings Black: vs 1.d4 QGD. Vs 1.e4: 1...e5 (3.Bb5 a6 Chigorin; 3.Bc4 Nf6 4.d3 Be7; 3.Nc3 prepared lines A/B).

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 22, 1 draw): trades queens, hangs pieces/queen, illegal moves, flags when lost.
- Stockfish 19 (depth 4-5): instant moves. White 1.e4 2.Nf3 3.Nc3 4.Bb5, then 5.O-O or 5.Nd5 (7.Qe2 pin). Black vs 1.e4: ...c5, ...Nc6, ...g6 Maroczy. Grabs loose pawns, finds queen skewers, back-rank checks and mating sacs; repeats only when stuck.
- GPT-6.1 Sol: Black Chigorin (plays ...Na6-c5, ...Ncxe4 vs Be3, ...Bf6xa1); White Ruy, 3.Bc4, or 1.d4 2.c4 3.Nc3 4.Bg5. Fast book moves, banks clock, takes every free piece, Q+R raids, forks. Errs under pressure; repeats when worse.

## Notes files (max 8, all used)
- notes/sicilian-plan.md: Alapin/Closed Sicilian vs SF + luft rules.
- notes/white-open-sicilian-sf.md: Yugoslav, Maroczy vs SF, Rauzer, SF losses.
- notes/black-ruy-chigorin.md: Black Chigorin games (T16R2 win line).
- notes/white-closed-ruy.md: closed Ruy wins, 3 losses vs Sol (T16R3 e4/Be3 line).
- notes/white-anti-marshall-d3.md: 8.d3 vs Sol.
- notes/black-four-knights.md: vs 3.Nc3 lines A/B, 8 losses.
- notes/black-qgd-lasker.md: QGD vs Sol.
- notes/black-giuoco-pianissimo.md: losses vs Sol 3.Bc4.
