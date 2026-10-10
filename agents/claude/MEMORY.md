# MEMORY (clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy White: DeepSeek 8 W; Sol 4 W 4 L 1 D (T19R1 W, 8.d3). Sicilian White vs DeepSeek 6 W.
- Chigorin Black: DeepSeek 14 W 1 D; Sol 2 W 8 L 2 D (T18SF2G1G1 L ON TIME). QGD vs Sol 3 W 1 L; vs 3.Bc4 2 L.
- vs SF White: Alapin lost 4x; Maroczy drew 2. vs SF Black 3.Nc3: 9 L 5 D.

## Key lessons (read before EVERY move)
- CLOCK FIRST (T18SF2G1G1: pawn up, flagged after ~60 s on routine moves, still blundered). Budget: book 1-5 s; quiet 10-20 s; 45 s max, only at captures/trades/breaks/first non-book move. Under 8:00 cap 15 s, under 4:00 cap 8 s, under 1:30 cap 3 s. Never >3 min behind Sol. Won/equal endings: fast safe moves.
- ILLEGAL MOVES (3 = forfeit; T19R1 used all 3: 19.Qxc6 blocked by my Rd5, 22.Bf4 blocked by my Ne3): trace paths square by square INCLUDING my own pieces and his just-pushed pawn; list pins on my king. Output only the JSON move object.
- HIS LAST MOVE FIRST (T18SF2G1G1 33.e5 dxe5 34.Bxe5 Bxd5?? 35.Bxb8): if it attacks my piece, save it before grabbing; a 'free pawn' is bait. After a pawn leaves a diagonal, re-walk his bishop lines to the edge.
- BEFORE EVERY MOVE write 'his checks/captures after this' (T16R1 Re8?? Qxf7+). KNIGHT SWEEP: all his knight checks/forks (T18R3 38...Qc6?? Ne7+). BISHOP SWEEP: each diagonal to the edge, then R, Q, P, K (T17SF2G1 Ra7?? Bxa7; T17R3 Rd2?? Bxd2; T12 Qf5??); write 'X hit by / defended by [path]'.
- TRAP CHECK (T18R3 18...Nb4? 19.Bb1 Qd8? 20.a3): before a piece goes to the edge/into his camp list EVERY retreat square and pawn kick; prepare the retreat (...a5) first.
- CAPTURE CHAIN / SCREEN (T14SF2G1 Qxc1??; T15R1 Bxc3?? Qxc3; T17R1 36.Nxc2?? unmasked Qb6-f2): write the chain with values; what does this piece screen? No K on his bishop's diagonal behind one pawn.
- PLAN, NOT DRIFT (T17R1 22-28; T18R1 19-40): name a plan every move; list HIS breaks; count attackers vs defenders of my weak pawn (T18R1 25.Nxc6); before ...b4/...a3/...f5 write my recapture. Be3 blocks Re1: recount e4 (T16R3 21.b4? Ncxe4!). Avoid 17.d5 vs ...c4 clamp.
- CONVERSION (T13R1 B+B+N = DRAW; T15R3 drew 5 pawns up; T19R1 WON OCB 2 pawns up): trade rooks when up, vary at the FIRST repeat, safe captures only, keep f6 and Bg7 mutually guarded, run the h-pawn with K+B; stalemate check every ply. Up a queen: guarded pawns only, then Q+K net.
- WHITE 8.d3 vs 7...O-O (notes/white-anti-marshall-d3.md): 11...d5 12.exd5 Nxd5 13.Nxe5! (Nf3+Re1 vs Nc6) Nxe5 14.Rxe5 Bf6 15.Rxe8+ Qxe8 16.Bd2 = clean pawn up. Don't drift Qe2/Bc2 (T12R1).
- CHIGORIN (notes/black-ruy-chigorin.md): ...Bd7 ...a5 ...Rac8 THEN ...Rfe8 ...g6 (skipped = T18R3, T18SF2G1G1 losses). After c3 is traded COUNT d4 attackers/defenders each move (17...exd4! 18.Nxd4 Nxd4 won a piece). Vs d5: ...c4 clamp or ...Nb8; ...Nb4 only with ...a5. Keep rooks.
- VS SF 3.Nc3 AS BLACK (notes/black-four-knights.md): 3...Nf6 4.Bb5 Bb4, never 3...Bc5. A) 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 ONLY; 10.Bc4 try ...Bd6 (never Bxd2, Qf6, Bc5). B) 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 Qe7 8.dxc6 dxc6 9.Bxc6+ bxc6 10.Nd4 Bd7! ... 14.Qxe7 Bxe7; no ...d5 later. Think 3+ min at moves 10, 11, 18-26 (only here).
- LOST VS SF: blockade passed pawn with B+K; SF repeats at +7 = draw. SF never errs; Q for R/minor is a LOSS.
- LUFT: h3 by move 9-12 but not at the cost of Be3. Before rook trades: 'Qb1+/Qa1+, my only blocker?'
- Armageddon: White (draw loses) solid, luft first; Black (draw wins) safest setup.
- Repertoire: W 1.e4 e5 2.Nf3 3.Bb5 (3...Nf6 4.d3; 3...a6 closed Ruy h3, 8.d3 vs ...O-O); vs 1...c5 DeepSeek Yugoslav 9.Bc4, SF Maroczy never Alapin (notes). B: 1.d4 QGD; 1.e4 e5 (Chigorin; 3.Bc4 Nf6 4.d3 Be7; 3.Nc3 A/B).

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 27): Chigorin as White (Qe2, Ng3, then 18.Nxd4??); as Black Dragon, speculative sacs, hangs pieces, illegal moves.
- Stockfish 19 (depth 4-5): instant. White 1.e4 2.Nf3 3.Nc3 4.Bb5, 5.O-O or 5.Nd5. Black ...c5 ...Nc6 ...g6 Maroczy. Grabs loose pawns, piles on a weak pawn, back-rank checks; repeats vs a blockade.
- GPT-6.1 Sol: Black Chigorin (...Na5-c5, ...Ncxe4, ...c4 clamp, ...f5/...e4+); vs 8.d3 ...Bb7 ...Re8 ...d5? loses e5, then rook raids and OCB defence. White: Ruy Nf1-g3 + d5, 3.Bc4, 1.d4. 5-30 s/move, banks the clock, takes every free piece, Q+R raids, knight forks; hangs pieces when behind.

## Notes files (notes/*.md, 8 used)
sicilian-plan, white-open-sicilian-sf, black-ruy-chigorin, white-closed-ruy, white-anti-marshall-d3 (T19R1 win), black-four-knights, black-qgd-lasker, black-giuoco-pianissimo.
