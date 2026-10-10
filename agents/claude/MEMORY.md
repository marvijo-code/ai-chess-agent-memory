# MEMORY (chess tournament; clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy White: DeepSeek 8 W; Sol 3 W, 2 L, 1 D.
- Sicilian White vs DeepSeek: 5 W (Yugoslav 3/3).
- Chigorin Black: DeepSeek 10 W 1 D (T16R2 W mate 34); Sol 2 W, 5 L, 2 D (T15R3 drew 3 pawns up; T15SF2G1G1 lost after winning a pawn).
- Sol as Black: QGD 3 W 1 L; vs 3.Bc4 2 L.
- vs SF as White: Alapin lost 4x; Maroczy drew T13R3, T14R2 from lost spots. vs SF as Black 3.Nc3: 7 L, 4 D (T16R1 mated in 14).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count (max 3). Trace the path (own pawn d6 blocks Be7-c5); destination not my own piece; list pins on my king before moving a piece.
- GUARD-OF-F7 CHECK (T16R1 11...Re8?? 12.Qxf7+ mate in 4): before ANY move write 'his checks/captures after this move' and name each guard of f7/h7/king-side pawns BY PIECE. Qf3+Bc4 hit f7; Rf8+Kg8 were the only guards; Re8 removed one; Bc8+Ra8 undeveloped = back-rank mate. Never move Rf8 while f7 is hit twice.
- DESTINATION CHECK (T15SF2G1G1 23...Nxd5?? 24.Qxd5): before ANY capture/move write 'square X: attacked by [all pieces incl. queen/rook down open lines], defended by [mine]'. A 'free' pawn is bait. When ahead keep it simple.
- NO REPEAT WHEN AHEAD (T15R3: 5 pawns v 2, drew by ...Nb4+/...Nd5+ x3): recount pawns every 10 moves; at the FIRST repeat play another move even if a pawn falls.
- ATTACKED-BISHOP (T15R1 11...Bxc3?? 12.Qxc3): pawn hits my bishop -> RETREAT (list squares). Name each recapturer from the CURRENT board.
- CAPTURE-CHAIN (T14SF2G1 25...Qxc1?? Q+R for R+B): write the chain with values BEFORE capturing; the FIRST capturer is lost.
- GUARD CHECK (T14R3 20...Bxf5 removed b5's only guard; T13R2 29.Qb3?? Qxa1+): before ANY trade or piece move list what it guards.
- QUEEN PATH (T13R2 23.Bd3?? Nxd3; T12SF2G1 Qf5??: his e5 pawn blocked my Rd5): trace every line square by square.
- MAROCZY VS SF (T14R2): vs 11...Ng4 play 12.Bxg4 Bxg4 13.f3, NOT 12.h3?! Nxe3.
- WEAK-PAWN COUNT (T13R3 20.Nd4? Rxc4; T13SF1G1 21...Rd7?? f7): count attackers vs defenders on my weak pawn before each move/trade.
- PASSIVE-DRIFT vs SF: every move needs a named plan; before each rook/bishop trade ask whose rook gets the open file/7th. (Vs DeepSeek quiet moves are fine.)
- BOOK DEVIATION LOSES vs SF (10...Qf6, 9...bxc6, 10...Bxd2, 10...Bc5?, 12.h3, 11...Bxc3): at the first branch calculate HIS best reply incl. Qxf7+/Bxf7+ and pawn pushes hitting my minors.
- SAC CHECK: his BEST reply first; equal + solid beats an unsound sac.
- CONVERSION (mates T14R1/T14R5.2/T15R2/T15R5.2/T16R2; T13R1 B+B+N vs pawns = DRAW): list his checks, safe captures only, trade rooks when up, rook to 7th/2nd, passed pawn, KING up, never repeat, stalemate check each ply. Rook on 2nd + Qxf2+ with rook support; his Ra1 blocked by own Bb1 = Rxe1+ wins.
- CHIGORIN VS DEEPSEEK (T16R2 W): 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7, ...Rfe8, ...h6, ...Rac8; vs 19.d5 Nb4 20.Bb1; 21.Nf5 Bxf5 22.exf5 Nbxd5 wins d5 (checked Bxh6 gxh6 first). It hangs queens (23.Qd4?? exd4): after each odd move list my captures.
- VS SF 3.Nc3 AS BLACK: 3...Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 (ONLY dxc6) 10.Bc4. Move 10 untested candidate: 10...Bd6 (then ...Qd7/...Be6/...Re8 only after f7 count). Never Bxd2, Qf6, Bc5 (11.Re1 Re8?? mate), 3...Bc5. Think 3+ min at move 10 AND 11.
- DRAWN ENDINGS: pawn up in opposite-colored bishops = draw; keep rooks.
- LUFT: h3 by move 9-12 but not at the cost of Be3. Before rook trades: 'Qb1+/Qa1+, my only blocker?'
- VS PAWN STORMS: trade outpost knight, ...Bf6 vs g5, defended queen trades. H7: his Bd3 + Qf5/Qg6; mine: Q to h5/h6 + Ng5 -> Qxh7#.
- ATTACKED-PIECE CHECK FIRST: list every piece his move attacks (incl. discovered) and who defends it.
- SF never errs and does NOT repeat at +6; Q for R/minor is a LOSS. DeepSeek/Sol hang pieces: list my options after EVERY odd enemy move; 'free piece': ask why, list ALL his checks, then take it fast. Q=9 R=5 B/N=3.
- TIME: book 1-8 s; 30-120 s at captures, trades, queen moves, breaks, first non-book move (T16R1 used 48 s on the losing 11...Re8 with a false justification: spend it listing HIS checks). Recapturing a hanging piece <=60 s. When lost vs SF play 3-8 s moves.
- Armageddon: White (draw loses) solid, luft first; Black (draw wins) safest setup.
- Openings White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy (9.h3; vs 7...O-O 8.d3). Vs 1...c5 DeepSeek: Yugoslav vs Dragon or Rauzer; vs SF: 2.Nf3 open Sicilian + Maroczy (12.Bxg4!), never Alapin.
- Openings Black: vs 1.d4 QGD. Vs 1.e4: 1...e5 (3.Bb5 a6 Chigorin: ...Nb4, ...a5, ...Bd7, ...Rac8, ...Rfe8, a3 Na6-c5, then ...Ncxe4 vs Be3; 3.Bc4 Nf6 4.d3 Be7; 3.Nc3 prepared line).

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 22, 1 draw): trades queens, hangs pieces/queen, illegal moves, 30-50 s/move, flags when lost.
- Stockfish 19 (depth 4): instant moves. White 1.e4 2.Nf3 3.Nc3 (Bc4, Bh6, Re7, Bxf7+, Qxf7+). Black vs 1.e4: ...c5, ...Nc6, ...g6 Maroczy. Grabs loose pawns, finds back-rank queen checks and mating sacs; repeats only when stuck.
- GPT-6.1 Sol: Black Chigorin; White Ruy, 3.Bc4, or 1.d4 2.c4 3.Nc3 4.Bg5. Fast book moves, takes every free piece, Q+R raids, forks. Errs under pressure; repeats when worse.

## Notes files (max 8, all used)
- notes/sicilian-plan.md: Alapin/Closed Sicilian vs SF + luft rules.
- notes/white-open-sicilian-sf.md: Yugoslav, Maroczy vs SF, Rauzer, SF losses.
- notes/black-ruy-chigorin.md: Black Chigorin games (T16R2 win line).
- notes/white-closed-ruy.md: closed Ruy wins, losses.
- notes/white-anti-marshall-d3.md: 8.d3 vs Sol.
- notes/black-four-knights.md: vs 3.Nc3 line, 7 losses (T16R1 f7 mate).
- notes/black-qgd-lasker.md: QGD vs Sol.
- notes/black-giuoco-pianissimo.md: losses vs Sol 3.Bc4.
