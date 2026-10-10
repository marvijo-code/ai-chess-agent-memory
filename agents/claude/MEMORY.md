# MEMORY (chess tournament; clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy White: DeepSeek 8 W; Sol 3 W, 4 L, 1 D (T17R1 L).
- Sicilian White vs DeepSeek: 5 W (Yugoslav 3/3).
- Chigorin Black: DeepSeek 13 W 1 D (T17 5.2 W); Sol 2 W, 6 L, 2 D (T17SF2G1 L).
- Sol as Black: QGD 3 W 1 L; vs 3.Bc4 2 L.
- vs SF White: Alapin lost 4x; Maroczy drew T13R3, T14R2. vs SF Black 3.Nc3: 8 L, 5 D (T17R3 D, a rook down).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count (max 3). Trace the path square by square INCLUDING MY OWN pieces (T17SF2G1 ...Bxb4: own d6; T17R2 Rxe1+: own Be7; T17R3 ...Bg6, ...Rec8; T17 5.2 ...Qf2: own Ne3); list pins on my king.
- BISHOP SWEEP (T17SF2G1 31...Ra7?? Bxa7; T17R3 26...Rd2?? Bb4xd2; T15 Nxd5?? Qxd5; T12 Qf5??): before any rook/queen/capture move to X, walk EACH of HIS bishops' diagonals to the edge, then R, N, Q, P, K lines; write 'X hit by ... / defended by [path]'. Free pawn = bait. Being worse is no reason to skip it.
- BREAK CHECK (T17SF2G1 22...b4 23.axb4 a3?! = 2 pawns down): before ...b4/...a3/...f5 write my legal recapture and his best reply; if it only trades my pawn for his passed pawn, don't.
- SCREEN RULE (T17R1 36.Nxc2?? unblocked Qb6-f2; 27.Kh2 on Bd6's diagonal, 29.exf5?? e4+; T16SF2G1 Qe5 v Qa5): before ANY move/capture ask 'what does this piece screen (K/Q/f2/g2) vs his B/Q/R?' and 'which pawn push opens it with check?'. Never K on his bishop's diagonal behind one pawn. A free rook may be bait: capture with the piece that screens nothing.
- E4 COUNT (T16R3 21.b4? axb3 22.Bxb3 Ncxe4!): Be3 blocks Re1. Recount e4 guards after every exchange; vs ...Nc5 play Bxc5 or keep Bb1; never b4. Move Ra1 BEFORE ...e4/...Bf6.
- F7 CHECK (T16R1 11...Re8?? 12.Qxf7+): before ANY move write 'his checks/captures after this'; name f7/h7 guards by piece.
- PIN / NO-THREAT (T17R3 19...f6?! 20.Bxf6): count his 'threat' first; don't spend a pawn move on it.
- NO REPEAT WHEN AHEAD (T15R3 drew 5 pawns up): vary at the FIRST repeat.
- ATTACKED PIECE (T15R1 Bxc3?? Qxc3): pawn hits my bishop -> retreat; list everything his move attacks incl. discovered.
- CAPTURE CHAIN (T14SF2G1 Qxc1?? Q+R for R+B): write the chain with values; before a trade list what it guards (T14R3 Bxf5 removed b5's guard; T13R2 Bd3?? Nxd3).
- MAROCZY VS SF: vs 11...Ng4 play 12.Bxg4 Bxg4 13.f3, not 12.h3?!. Count c4.
- PASSIVE DRIFT (T17R1 moves 22-28): every move needs a named plan; list HIS pawn breaks. Avoid 17.d5 vs the ...c4 clamp. At the first book deviation calculate his best reply.
- CONVERSION (mates T14R1/T15R2/T15R5.2/T16R2/T16R5.2/T17R2/T17 5.2; T13R1 B+B+N = DRAW): list his checks, safe captures only, trade when up, stalemate check each ply. OCB = draw; keep rooks. Q up: trade rooks/pieces, keep all guarded.
- CHIGORIN (W vs DeepSeek x13; lines in notes/black-ruy-chigorin.md): ...Bd7 ...Rac8 ...Rfe8 ...g6/...h6 ...a5; vs 13.d5 ...c4 clamp, ...Nb7-c5. No ...Nxd5 (Qxd5) unless counted (T17 5.2 ok). It hangs R/Q/B: after each odd move list my captures. Vs Sol 17.d5 Nb4 18.Bb1: ...Na6/...Nc5, keep rooks, no ...b4 unless ...Bxb4 is legal and wins something.
- VS SF 3.Nc3 AS BLACK (see note): 3...Nf6 4.Bb5 Bb4. A) 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 (ONLY) 10.Bc4: try 10...Bd6; never Bxd2, Qf6, Bc5, 3...Bc5. B) 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 Qe7 8.dxc6 dxc6 9.Bxc6+ bxc6 10.Nd4 Bd7! (NOT c5?) ... 18.Rc5: improve here (19.Rg5 no threat, keep f-pawn). Think 3+ min at moves 10, 11, 18-26.
- LOST VS SF: blockade the passed pawn with B+K (T17R3); SF repeated at +7 = draw. Keep every piece guarded.
- LUFT: h3 by move 9-12 but not at the cost of Be3. Before rook trades: 'Qb1+/Qa1+, my only blocker?' Vs pawn storms: trade outpost knight, ...Bf6 vs g5.
- SF never errs; Q for R/minor is a LOSS. DeepSeek/Sol hang pieces; Sol takes every real free pawn/piece. Q=9 R=5 B/N=3.
- TIME: book 1-8 s; 30-120 s at captures, trades, queen moves, breaks, first non-book move; spend it on HIS checks/breaks and my screens. Long thinks did not stop T17SF2G1 Ra7. Lost vs SF: 3-8 s.
- Armageddon: White (draw loses) solid, luft first; Black (draw wins) safest setup.
- Openings White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy (9.h3; vs 7...O-O 8.d3). Vs 1...c5 DeepSeek: Yugoslav/Rauzer; vs SF: 2.Nf3 open Sicilian + Maroczy, never Alapin.
- Openings Black: vs 1.d4 QGD. Vs 1.e4: 1...e5 (3.Bb5 a6 Chigorin; 3.Bc4 Nf6 4.d3 Be7; 3.Nc3 lines A/B).

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 25, 1 draw): book Chigorin as White (13.d5, Nf1-g3-h2, f4), then speculative sacs (Nf5+, f6+, Qh6+??), hangs rook/queen/pieces, illegal moves, flags when lost.
- Stockfish 19 (depth 4-5): instant. White 1.e4 2.Nf3 3.Nc3 4.Bb5, then 5.O-O or 5.Nd5 (7.Qe2 pin). Black vs 1.e4: ...c5 ...Nc6 ...g6 Maroczy. Grabs loose pawns, queen skewers, back-rank checks, mating sacs; repeats when it cannot break a blockade (even at +7).
- GPT-6.1 Sol: Black Chigorin (...Na5-c5, ...Ncxe4 vs Be3, ...Bf6xa1, ...c4 clamp, ...f5/...e4+); White Ruy 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.d5 Nb4 18.Bb1, 3.Bc4, or 1.d4 2.c4 3.Nc3 4.Bg5. Fast book, banks clock, trades queens at equality, takes every free piece, pushes passed pawns with rook support, Q+R raids, forks. Errs under pressure; repeats when worse.

## Notes files (max 8, all used)
- notes/sicilian-plan.md: Alapin/Closed Sicilian vs SF + luft rules.
- notes/white-open-sicilian-sf.md: Yugoslav, Maroczy vs SF, Rauzer, SF losses.
- notes/black-ruy-chigorin.md: Black Chigorin games (T17 5.2 win, T17SF2G1 loss) and lines.
- notes/white-closed-ruy.md: closed Ruy wins, 4 losses vs Sol.
- notes/white-anti-marshall-d3.md: 8.d3 vs Sol.
- notes/black-four-knights.md: vs 3.Nc3 lines A/B, 8 L 5 D, T17R3 line.
- notes/black-qgd-lasker.md: QGD vs Sol.
- notes/black-giuoco-pianissimo.md: losses vs Sol 3.Bc4.
