# MEMORY (chess tournament; clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy White: DeepSeek 8 W; Sol 3 W, 2 L, 1 D (white-closed-ruy.md, white-anti-marshall-d3.md).
- Sicilian White vs DeepSeek: 4 W (white-open-sicilian-sf.md).
- Chigorin Black: DeepSeek 8 W 1 D (T14R5.2 mate 30); Sol 2 W, 4 L, 1 D (black-ruy-chigorin.md).
- Sol as Black: QGD 3 W 1 L; vs 3.Bc4 2 L.
- vs SF as White: Alapin lost 4x; Maroczy drew T13R3, T14R2 from lost positions. vs SF as Black 3.Nc3: 5 L, 4 D.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Trace the path (own pawn on d6 blocks Be7-c5); destination must not be my own piece.
- CAPTURE-CHAIN COUNT (T14SF2G1 25...Qxc1?? Q+R for R+B = -6): on a square he guards twice, write the chain with values BEFORE capturing; the FIRST capturer is lost. My Q in front of my R on a file takes first. If his minor/queen guards the square, move the queen off the line (...Qb6/Qd8). Play the note.
- STACKED-LINE (T14SF2G1 24...Nxb3 uncovered Rc1 on Qc7): my knight/bishop in FRONT of my queen against his rook: moving or trading it discovers the attack. Name the piece behind it and his piece at the other end. Spend the clock on c-file battery at moves 21-24.
- TRADE-GUARD CHECK (T14R3 loss): 20...Bxf5 removed the only guard of b5. Before ANY trade or piece move list what it guards; if a pawn goes loose fix it THAT move.
- MAROCZY VS SF (T14R2): vs 11...Ng4 play 12.Bxg4 Bxg4 13.f3, NOT 12.h3?! Nxe3. Before an outpost ask where it goes after ...e6; list his bishop pins on my queen's line.
- RECAPTURE-PATH CHECK (T13R2 23.Bd3?? Nxd3: my Bd2 blocked Qd1). Name the recapturer, walk its path, ask where HIS queen/bishop lands.
- WEAK-PAWN COUNT (T13R3 20.Nd4? Rxc4; T13SF1G1 21...Rd7?? f7): count attackers vs defenders on my weak pawn before each move/trade.
- PASSIVE-DRIFT (T13SF1G1, T14R3): every move needs a named plan or defensive task. Before each rook/bishop trade: whose rook gets the open file/7th?
- BOOK DEVIATION LOSES vs SF (10...Qf6, 9...bxc6, 10...Bxd2, 12.h3). Follow the notes; at the first branch calculate HIS best reply.
- ABANDONED-GUARD CHECK (T13R2 29.Qb3?? Qxa1+): what did the moved piece guard; list his knight jumps.
- QUEEN-DESTINATION CHECK (T12SF2G1): name the square, every enemy line hitting it, MY recapturer by exact path (enemy pawns block rook lines). Before a rook trade check his queen backs the file.
- SAC CHECK: calculate his BEST reply first. Equal + solid beats an unsound sac.
- CONVERSION (T13R1 +B+B+N vs pawns = DRAW; T14R1 up Q: mate 33; T14R5.2 up Q+N: mate 30): take only captures after listing his checks/forks, each capture removes an attacker or forks (Nc2, Nxe2+ then Qxa1+); trade pieces, rook to open file, bring KING, rook on 7th, never repeat, stalemate check every ply.
- VS SF 3.Nc3 AS BLACK: 3...Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 (ONLY dxc6) 10.Bc4. Never 3...Bc5, never 10...Bxd2, avoid 10...Qf6.
- DRAWN ENDING: pawn up in opposite-colored bishops = draw; keep rooks. Pawn down: keep rooks too.
- RETREAT-SQUARE: before a bishop grabs a pawn, list retreats vs pawn pushes.
- LUFT/BACK RANK: h3 by move 9-12 but not at the cost of Be3. Before rook trades: 'Qb1+/Qa1+, my only blocker?'
- VS PAWN STORMS (T9R1 lost, T9SF2G1 won): trade outpost knight, ...Bf6 vs g5, DEFENDED queen trades, ...Nh7.
- H7 PATTERN: his Bd3 + Qf5/Qg6 vs h7 (T14SF2G1 mate); mine: h7 one defender + Q reaches h5/h6 + Ng5 -> Qxh7#.
- ATTACKED-PIECE CHECK FIRST: list every piece his move attacks (incl. discovered) and who defends it.
- SF never errs; a pawn down vs SF snowballs. Q for R/minor is a LOSS. NEVER hit a queen with an UNDEFENDED piece. DeepSeek/Sol hang pieces (T14SF2G1 25.Bxb3??; T14R5.2 18.Nxe5??, 21.Qxa4??): list all my options after EVERY enemy trade/odd move; 'free piece': ask why, list ALL his checks.
- MATERIAL COUNT: Q=9, R=5, B/N=3; recount at END of every capture sequence.
- LIFELINES VS SF (depth 4): defended blockers, king in corner; SF repeats checks. Play quickly, keep everything defended.
- TIME: book 1-8 s; 30-120 s at captures, trades, queen moves, pawn breaks. Time without a checklist is wasted.
- Armageddon as White (draw loses): solid, luft first. As Black (draw wins): safest setup.
- Openings White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy (9.h3; vs 7...O-O 8.d3). Vs 1...c5 DeepSeek: Rauzer or Yugoslav. vs SF: 2.Nf3 open Sicilian + Maroczy (12.Bxg4!), never Alapin.
- Openings Black: vs 1.d4 QGD. Vs 1.e4: 1...e5 (3.Bb5 a6 Chigorin: ...Nb4, ...a5, ...a4, ...Bd7, ...Rac8; 3.Bc4 Nf6 4.d3 Be7; 3.Nc3 prepared line).

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 19, 1 draw): trades queens, hangs pieces (even Q when lost), tries illegal moves, 40-50 s/move, flags when lost.
- Stockfish 19 (depth-4): instant moves. White 1.e4 2.Nf3 3.Nc3 (Bc4, Bh6, Re7, Bxf7+). Black vs 1.e4: ...c5, ...Nc6, ...g6 Maroczy. Grabs loose pawns, finds back-rank queen checks; repeats when stuck.
- GPT-6.1 Sol: Black Chigorin; White Ruy (d5 Nb4 Bb1 a5 a3 Na6, Nf1-g3, Ba2, Be3, Rc1 c-file battery vs Nc5+Qc7, b4), 3.Bc4, or 1.d4 2.c4 3.Nc3 4.Bg5. Fast book moves, takes every free piece/pawn, Q+R raids, knight forks. Errs under pressure.

## Notes files (max 8, all used)
- notes/sicilian-plan.md: White Alapin vs SF + luft rules.
- notes/white-open-sicilian-sf.md: Maroczy vs SF, Yugoslav, Rauzer, SF losses.
- notes/black-ruy-chigorin.md: Black Chigorin games incl. T14R5.2 win, T14R1 win, T14R3 + T14SF2G1 losses.
- notes/white-closed-ruy.md: closed Ruy wins, T6R3 + T13R2 losses.
- notes/white-anti-marshall-d3.md: 8.d3 vs Sol.
- notes/black-four-knights.md: vs 3.Nc3 line, 5 losses.
- notes/black-qgd-lasker.md: QGD games vs Sol.
- notes/black-giuoco-pianissimo.md: losses vs Sol 3.Bc4, fixes.
