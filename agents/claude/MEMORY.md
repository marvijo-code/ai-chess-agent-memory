# MEMORY (clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy White: DeepSeek 8 W; Sol 3 W 4 L 1 D. Sicilian White vs DeepSeek 6 W (T18R2 Yugoslav).
- Chigorin Black: DeepSeek 13 W 1 D; Sol 2 W 8 L 2 D (T18R3 L; T18SF2G1G1 L ON TIME). QGD vs Sol 3 W 1 L; vs 3.Bc4 2 L.
- vs SF White: Alapin lost 4x; Maroczy drew T13R3, T14R2. vs SF Black 3.Nc3: 9 L 5 D (T18R1 L).

## Key lessons (read before EVERY move)
- CLOCK FIRST (T18SF2G1G1: pawn up, flagged with 10 s vs his 7:32; I spent ~60 s on routine moves 25-44 and STILL blundered 34...Bxd5??). Budget: book 1-5 s; quiet moves 10-20 s; 45 s max, only at captures/trades/breaks/first non-book move. Read my clock every move: under 8:00 cap 15 s, under 4:00 cap 8 s, under 1:30 cap 3 s. Never be >3 min behind Sol. Won or equal endings: fast safe moves, no deep waiting-move analysis.
- Output: only the JSON move object. Illegal moves count (max 3). Trace paths square by square INCLUDING MY OWN pieces and HIS just-pushed pawn (T17SF2G1 ...Bxb4: own d6; T18R2 14.Bxf6: his e5 pawn blocked); list pins on my king.
- HIS LAST MOVE FIRST (T18SF2G1G1 33.e5 dxe5 34.Bxe5 Bxd5?? 35.Bxb8): if it attacks my piece, save/answer it before grabbing anything; a 'free pawn' is bait. After any pawn leaves a diagonal (...dxe5 opened Bf4-b8), re-walk his bishop lines to the edge for my rooks/queen.
- TRAP CHECK (T18R3 18...Nb4? 19.Bb1 Qd8? 20.a3): before a piece goes to the edge/into his camp list EVERY retreat square and pawn kick (a3, h3, c4). Prepare the retreat (...a5) first.
- KNIGHT SWEEP (T18R3 38...Qc6?? 39.Ne7+ forked K+Q+R): before any K/Q/R move list ALL his knight checks and what each forks.
- BISHOP SWEEP (T17SF2G1 31...Ra7?? Bxa7; T17R3 26...Rd2?? Bxd2; T12 Qf5??): before any rook/queen/capture move to X, walk EACH of his bishops' diagonals to the edge, then R, N, Q, P, K lines; write 'X hit by / defended by [path]'.
- WEAK PAWN COUNT (T18R1 25.Nxc6): count attackers vs defenders of my weak pawn (c6/a6); never fix it with ...d5?!. Name a plan or trade rooks while equal.
- BREAK CHECK (T17SF2G1 22...b4 23.axb4 a3?!): before ...b4/...a3/...f5 write my recapture and his best reply.
- SCREEN RULE (T17R1 36.Nxc2?? unblocked Qb6-f2; 27.Kh2 on Bd6's diagonal, 29.exf5?? e4+): what does this piece screen? which push opens it with check? No K on his bishop's diagonal behind one pawn.
- E4 COUNT (T16R3 21.b4? axb3 22.Bxb3 Ncxe4!): Be3 blocks Re1. Recount e4 after each exchange; vs ...Nc5 play Bxc5; never b4.
- F7 CHECK (T16R1 11...Re8?? 12.Qxf7+): before ANY move write 'his checks/captures after this'; count his 'threat' first.
- CAPTURE CHAIN (T14SF2G1 Qxc1??; T15R1 Bxc3?? Qxc3): write the chain with values and what a trade stops guarding; pawn hits my bishop -> retreat.
- PASSIVE DRIFT (T17R1 22-28; T18R1 19-40): every move needs a named plan; list HIS breaks (f4/e5 in T18SF2G1G1). Avoid 17.d5 vs ...c4 clamp.
- CONVERSION (T13R1 B+B+N = DRAW; T15R3 drew 5 pawns up): vary at the FIRST repeat; safe captures only, trade when up, stalemate check. OCB = draw; keep rooks. Up a queen: grab only guarded pawns, then Q+R mate net.
- CHIGORIN (notes/black-ruy-chigorin.md): ...Bd7 ...a5 ...Rac8 THEN ...Rfe8 ...g6 (T18R3 and T18SF2G1G1 skipped ...a5; SF: 14...Rfe8? 15...g6?). Vs 13.d5 ...c4 clamp; vs 16.d5 c4 17.a4 bxa4 was fine (+1 pawn). Vs 18.d5 ...Nb8/...Ne7; ...Nb4 only with ...a5. Keep rooks.
- VS SF 3.Nc3 AS BLACK (notes/black-four-knights.md): 3...Nf6 4.Bb5 Bb4. A) 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 (ONLY) 10.Bc4: try 10...Bd6; never Bxd2, Qf6, Bc5, 3...Bc5. B) 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 Qe7 8.dxc6 dxc6 9.Bxc6+ bxc6 10.Nd4 Bd7! 11.O-O O-O 12.d3 exd3 13.cxd3 Rfe8 14.Qxe7: try 14...Bxe7, ...Bf6 vs Nd4; vs b4 ...a5. Think 3+ min at moves 10, 11, 18-26 (only here). Try 4...Nd4 once.
- LOST VS SF: blockade the passed pawn with B+K (T17R3); SF repeats at +7 = draw. Keep every piece guarded.
- LUFT: h3 by move 9-12 but not at the cost of Be3. Before rook trades: 'Qb1+/Qa1+, my only blocker?'
- SF never errs; Q for R/minor is a LOSS. DeepSeek/Sol hang pieces; Sol takes every free pawn/piece.
- Armageddon: White (draw loses) solid, luft first; Black (draw wins) safest setup.
- White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy (9.h3; vs 7...O-O 8.d3). Vs 1...c5 DeepSeek: Yugoslav 9.Bc4, Bh6 trade, Qxh6, h4-g4-g5-h5 (count ...Nxe4/...Nh5 before 19.g5); vs SF: 2.Nf3 open Sicilian + Maroczy, never Alapin.
- Black: vs 1.d4 QGD. Vs 1.e4: 1...e5 (3.Bb5 a6 Chigorin; 3.Bc4 Nf6 4.d3 Be7; 3.Nc3 lines A/B).

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 26): book Chigorin as White; as Black Dragon, then speculative sacs, hangs queen/pieces, illegal moves.
- Stockfish 19 (depth 4-5): instant. White 1.e4 2.Nf3 3.Nc3 4.Bb5, then 5.O-O or 5.Nd5. Black: ...c5 ...Nc6 ...g6 Maroczy. Grabs loose pawns, piles on a weak pawn, queen skewers, back-rank checks; repeats when it cannot break a blockade.
- GPT-6.1 Sol: Black Chigorin (...Na5-c5, ...Ncxe4, ...c4 clamp, ...f5/...e4+); White Ruy 14.Nf1-g3, 16.d5 + a4/b3 (T18SF2G1G1), 17.Rc1, 18.d5 + a3 trapping Nb4 (T18R3), 3.Bc4, 1.d4. Plays 5-30 s/move and banks the clock (7:32 left when I flagged), takes every free piece, Q+R raids, knight forks.

## Notes files (notes/*.md, 8 used)
sicilian-plan (Alapin/Closed vs SF), white-open-sicilian-sf (Yugoslav vs DeepSeek, Maroczy vs SF), black-ruy-chigorin (incl. T18R3 trap, T18SF2G1G1 flag), white-closed-ruy, white-anti-marshall-d3, black-four-knights (lines A/B), black-qgd-lasker, black-giuoco-pianissimo (vs 3.Bc4).
