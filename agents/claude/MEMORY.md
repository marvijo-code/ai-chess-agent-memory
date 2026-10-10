# MEMORY (clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy White: DeepSeek 8 W; Sol 3 W 4 L 1 D. Sicilian White vs DeepSeek 6 W (T18R2 Yugoslav, mate 29).
- Chigorin Black: DeepSeek 13 W 1 D; Sol 2 W 6 L 2 D. QGD vs Sol 3 W 1 L; vs 3.Bc4 2 L.
- vs SF White: Alapin lost 4x; Maroczy drew T13R3, T14R2. vs SF Black 3.Nc3: 9 L 5 D (T18R1 L).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count (max 3). Trace paths square by square INCLUDING MY OWN pieces and HIS just-pushed pawn (T17SF2G1 ...Bxb4: own d6; T17 5.2 ...Qf2: own Ne3; T18R2 14.Bxf6 illegal: his e5 pawn blocked d4-f6); list pins on my king.
- BISHOP SWEEP (T17SF2G1 31...Ra7?? Bxa7; T17R3 26...Rd2?? Bxd2; T12 Qf5??): before any rook/queen/capture move to X, walk EACH of his bishops' diagonals to the edge, then R, N, Q, P, K lines; write 'X hit by / defended by [path]'. Free pawn = bait.
- WEAK PAWN COUNT (T18R1 25.Nxc6: N+R+R vs B+R): every move count attackers vs defenders of my weak pawn (c6/c7/a6); never fix it with ...d5?!. Waiting moves (h6 a6 Rb8 Rb6 Kf8 Be8) let him add attackers: name a plan (trade his N/B, ...a5 vs b4, ...Re5, K active) or trade rooks while equal.
- BREAK CHECK (T17SF2G1 22...b4 23.axb4 a3?!): before ...b4/...a3/...f5 write my legal recapture and his best reply.
- SCREEN RULE (T17R1 36.Nxc2?? unblocked Qb6-f2; 27.Kh2 on Bd6's diagonal, 29.exf5?? e4+): ask 'what does this piece screen vs his B/Q/R?' and 'which push opens it with check?'. No K on his bishop's diagonal behind one pawn. A free rook may be bait: capture with the piece that screens nothing.
- E4 COUNT (T16R3 21.b4? axb3 22.Bxb3 Ncxe4!): Be3 blocks Re1. Recount e4 after each exchange; vs ...Nc5 play Bxc5 or keep Bb1; never b4. Move Ra1 BEFORE ...e4/...Bf6.
- F7 CHECK (T16R1 11...Re8?? 12.Qxf7+; T17R3 19...f6?! no threat existed): before ANY move write 'his checks/captures after this'; count his 'threat' first.
- CAPTURE CHAIN (T14SF2G1 Qxc1??; T14R3 Bxf5 removed b5's guard; T15R1 Bxc3?? Qxc3): write the chain with values and what a trade stops guarding; pawn hits my bishop -> retreat.
- PASSIVE DRIFT (T17R1 22-28; T18R1 19-40): every move needs a named plan; list HIS pawn breaks. Avoid 17.d5 vs ...c4 clamp. At the first book deviation calculate his best reply.
- CONVERSION (T13R1 B+B+N = DRAW; T15R3 drew 5 pawns up): vary at the FIRST repeat; list his checks, safe captures only, trade when up, stalemate check each ply. OCB = draw; keep rooks. Up a queen (T18R2): grab only guarded pawns, then Q+R mate net.
- CHIGORIN (notes/black-ruy-chigorin.md): ...Bd7 ...Rac8 ...Rfe8 ...g6 ...a5; vs 13.d5 ...c4 clamp. No ...Nxd5 unless counted. Vs Sol 17.d5 Nb4 18.Bb1: ...Na6/...Nc5, keep rooks.
- VS SF 3.Nc3 AS BLACK (notes/black-four-knights.md): 3...Nf6 4.Bb5 Bb4. A) 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 (ONLY) 10.Bc4: try 10...Bd6; never Bxd2, Qf6, Bc5, 3...Bc5. B) 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 Qe7 8.dxc6 dxc6 9.Bxc6+ bxc6 10.Nd4 Bd7! 11.O-O O-O 12.d3 exd3 13.cxd3 Rfe8 14.Qxe7: T17R3 Bxe7 held; T18R1 Rxe7 ... 18.b4 d5?! lost c6. Try 14...Bxe7, ...Bf6 vs Nd4; vs b4 ...a5. Think 3+ min at moves 10, 11, 18-26. 9 L 5 D: try 4...Nd4 once.
- LOST VS SF: blockade the passed pawn with B+K (T17R3); SF repeats at +7 = draw. Keep every piece guarded.
- LUFT: h3 by move 9-12 but not at the cost of Be3. Before rook trades: 'Qb1+/Qa1+, my only blocker?' Vs pawn storms: trade outpost knight.
- SF never errs; Q for R/minor is a LOSS. DeepSeek/Sol hang pieces; Sol takes every free pawn/piece.
- TIME: book 1-8 s; 30-120 s at captures, trades, queen moves, breaks, first non-book move; spend it on HIS checks/breaks and my screens.
- Armageddon: White (draw loses) solid, luft first; Black (draw wins) safest setup.
- White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy (9.h3; vs 7...O-O 8.d3). Vs 1...c5 DeepSeek: Yugoslav 9.Bc4, Bh6 trade, Qxh6, h4-g4-g5-h5 (T18R2; SF liked Bxd4/Qxh6, marked 19.g5??: count ...Nxe4/...Nh5 first); Rauzer; vs SF: 2.Nf3 open Sicilian + Maroczy (vs 11...Ng4 12.Bxg4 Bxg4 13.f3; count c4), never Alapin.
- Black: vs 1.d4 QGD. Vs 1.e4: 1...e5 (3.Bb5 a6 Chigorin; 3.Bc4 Nf6 4.d3 Be7; 3.Nc3 lines A/B).

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 26): book Chigorin as White; as Black Dragon (...Nxd4 ...Be6 ...fxe6 ...e5 ...Rf7), then speculative sacs (Nf5+, Qh6+??), hangs queen/pieces, illegal moves. 30-60 s a move yet ignores my threats.
- Stockfish 19 (depth 4-5): instant. White 1.e4 2.Nf3 3.Nc3 4.Bb5, then 5.O-O or 5.Nd5. Black: ...c5 ...Nc6 ...g6 Maroczy. Grabs loose pawns, piles every piece on a weak pawn, queen skewers, back-rank checks; repeats when it cannot break a blockade.
- GPT-6.1 Sol: Black Chigorin (...Na5-c5, ...Ncxe4, ...c4 clamp, ...f5/...e4+); White Ruy 14.Nb3/17.d5, 3.Bc4, or 1.d4 Nc3 Bg5. Banks clock, takes every free piece, Q+R raids, forks; errs under pressure.

## Notes files (notes/*.md, 8 used)
sicilian-plan (Alapin/Closed vs SF), white-open-sicilian-sf (Yugoslav vs DeepSeek 4 W, Maroczy vs SF), black-ruy-chigorin, white-closed-ruy, white-anti-marshall-d3, black-four-knights (lines A/B, 9 L 5 D), black-qgd-lasker, black-giuoco-pianissimo (vs 3.Bc4).
