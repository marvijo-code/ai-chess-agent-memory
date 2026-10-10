# MEMORY (clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy White: DeepSeek 8 W; Sol 4 W 5 L 1 D. Sicilian White vs DeepSeek 7 W.
- Chigorin Black: DeepSeek 14 W 1 D; Sol 2 W 9 L 2 D. QGD Lasker: Sol 3 W 1 L, DeepSeek 1 W. Pianissimo: Sol 2 L, DeepSeek 1 W.
- vs SF White: Alapin lost 4x; Maroczy drew 2; T19R2 5.Nc3 e6 drew a piece down. vs SF Black: 3.Nc3 9 L 5 D; T20R2 Ruy 6.d4 L.

## Key lessons (read before EVERY move)
- 'FREE' CAPTURE = COUNT HIS GUARDS FROM HIS SIDE (T20R3 28...Nxd5?? 29.Qxd5: I wrote 'd5 undefended' but Qd2 guarded it down the d-file; N for P, equal game lost). From EACH of his Q/R/B/N trace a line to the target square; a queen behind or along a file/diagonal guards. My 1-min think checked only my own side.
- CLOCK FIRST (T18SF2G1G1, T19SF2G1G1 FLAGGED: 55-60 s on ~20 quiet moves; T20R3 ~55 s on moves 26-40). Book 1-5 s; quiet 10-15 s; 45 s max only at captures/trades/breaks/first non-book move. Under 8:00 cap 15 s, under 4:00 cap 8 s, under 1:30 cap 3 s.
- HIS QUEEN WITH TEMPO (T20R2 25...Re8? 26.Qd3! Qxd3 Rxe8+): before a rook move/trade name its guards; if my queen is the only one, list EVERY queen move of his that hits it. Keep my queen off an open d-file.
- PAWN-GUARDED PAWN (T19SF2G1G1 32.Nxc4?? bxc4 = N for 2 P): count VALUES. Before ...a4/...b5 count guards vs capturers incl. queen x-ray (T19R5.2 ...a4? Bxa4).
- ILLEGAL MOVES (3 = forfeit; T19R1 used all 3: Qxc6 blocked by my Rd5, Bf4 by my Ne3): trace paths square by square INCLUDING my own pieces and his just-pushed pawn; list pins on my king. Output only the JSON move object.
- MY OWN PIECE/PAWN BLOCKS MY LINE (T19R2 11.Bd3?? d4!; T19R3 10...Nc6? my e6 pawn blocks Qe7-e4): ask 'which file/diagonal/guard does this close?'
- HIS LAST MOVE FIRST (T18SF2G1G1 34...Bxd5?? 35.Bxb8): if it attacks my piece, save it before grabbing; a 'free pawn' is bait. After a pawn leaves a diagonal, re-walk his bishop lines.
- BEFORE EVERY MOVE write 'his checks/captures after this' (T16R1 Re8?? Qxf7+). KNIGHT SWEEP (T18R3 38...Qc6?? Ne7+). BISHOP SWEEP to the edge (T17SF2G1 Ra7?? Bxa7). QUEEN: 'Q on X, attacked by A, defended via path P', trace P (T12SF2G1 Qf5??).
- TRAP CHECK (T18R3 18...Nb4? 19.Bb1 Qd8? 20.a3): before a piece goes to the edge/into his camp list EVERY retreat square and pawn kick; prepare the retreat (...a5) first.
- CAPTURE CHAIN / SCREEN (T14SF2G1 Qxc1??; T15R1 Bxc3?? Qxc3; T17R1 36.Nxc2?? unmasked Qb6-f2): write the chain with values; what does this piece screen?
- PLAN, NOT DRIFT (T17R1 22-28; T18R1 19-40; T19SF2G1G1 27-31; T20R2 19-22; T20R3 24-27 h6/Bf8/Re8): name a plan every move; list HIS breaks; before ...b4/...a3/...f5 write my recapture. As White vs Chigorin AVOID d5.
- PAWN DOWN VS DEEPSEEK (T19R3, T19R5.2 won): make threats it must see, keep every unit guarded; it hangs Q/R/B within 10 moves.
- CONVERSION (T13R1 B+B+N DRAW; T15R3 drew 5 pawns up; T19R1 won OCB; T20R1 rook up): trade when up, vary at the FIRST repeat, safe captures only, stalemate check every ply.
- YUGOSLAV vs DeepSeek Dragon 9.Bc4 Bd7 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 h5 13.Kb1 Nc4 14.Bxc4 Rxc4 15.Nde2, then Bh6/Qxh6/Ng5/Qh7# (notes/white-open-sicilian-sf.md).
- WHITE 8.d3 vs 7...O-O: 11...d5 12.exd5 Nxd5 13.Nxe5! Nxe5 14.Rxe5 Bf6 15.Rxe8+ Qxe8 16.Bd2 = pawn up (notes/white-anti-marshall-d3.md).
- CHIGORIN as Black (notes/black-ruy-chigorin.md): ...Bd7 ...a5 ...Rac8 THEN ...Rfe8 ...g6. COUNT d4 attackers/defenders after c3 trade. Vs d5: ...c4 or ...Nb8; ...Nb4 only with ...a5. T20R3 20.b4 hit Nc5: ...Nb7? was marked; try ...axb4 21.axb4 Na6. Keep rooks.
- VS SF 6.d4 (same note): 6...exd4 7.Re1 d6 8.Nxd4 Bd7 9.Nxc6 Bxc6 10.Bxc6+ bxc6 equal to move 22; then drift lost to e5. Plan ...d5/...c5, queen off the d-file.
- VS 3.Bc4 (notes/black-giuoco-pianissimo.md): 3...Nf6 4.d3 Be7 5.O-O O-O 6.c3 d6, ...Be6, ...Re8/...h6; no ...a4 into Bxa4.
- VS SF 3.Nc3 AS BLACK (notes/black-four-knights.md): 3...Nf6 4.Bb5 Bb4, never 3...Bc5. 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 ONLY, then 10.Bc4 ...Bd6. 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 Qe7 8.dxc6 dxc6 9.Bxc6+ bxc6 10.Nd4 Bd7!. Think 3+ min at moves 10, 11, 18-26.
- LOST VS SF: blockade passed pawn with B+K; SF repeats at +7..+10 = draw (avoid Ka1/Ka2); a rook down it just mates. SF never errs; Q for R/minor is a LOSS.
- LUFT: h3 by move 9-12 but not at the cost of Be3. Before rook trades: 'Qb1+/Qa1+, my only blocker?' Armageddon: White (draw loses) solid, luft first; Black (draw wins) safest setup.
- Repertoire: W 1.e4 e5 2.Nf3 3.Bb5 a6 closed Ruy (h3; 8.d3 vs ...O-O; vs Chigorin 14.Nb3/Nf1 not d5); 1...c5 vs DeepSeek Yugoslav 9.Bc4; SF Maroczy never Alapin; SF ...Nf6/...e6: 5.Nc3 e6 6.Nxc6 bxc6 7.e5 Nd5 8.Ne4 Qc7 9.f4. B: 1.d4 QGD Lasker (9.Nxe4 dxe4 10.Nd2 ...f5, not ...Nc6); 1.e4 e5 Chigorin; 3.Bc4 Nf6 4.d3 Be7; 3.Nc3 A/B.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 30): Chigorin as White (Qe2, Ng3, 18.Nxd4??); Pianissimo (grabs a4, 16.Qxd6?? hung Q); QGD 15.Qxd4?? hung Q; Black Dragon (...Rxe4?? T20R1), speculative sacs, illegal moves. 15-50 s/move.
- Stockfish 19 (depth 4-6): instant. White 1.e4 2.Nf3, 3.Nc3 4.Bb5 (5.O-O/5.Nd5) or Ruy 5.O-O Be7 6.d4 exd4 7.Re1 (e5 lever, Qd3 with tempo). Black ...c5 ...Nc6 ...g6 Maroczy, or ...Nf6 ...e6 ...bxc6 ...Nd5 ...Qc7 ...Bc5 ...d4. Grabs loose pawns, back-rank checks; repeats vs a blockade.
- GPT-6.1 Sol: as White Ruy Chigorin 14.d5, Nf1-g3, Be3, b4 (T20R3), 3.Bc4, 1.d4. As Black Chigorin (...Nc5, ...Bd7, ...a4, ...c4, ...Bd6; ...f5/...e4+). Banks the clock, takes every free piece, Q+R raids, knight forks; converts a piece up cleanly; hangs pieces when behind.

## Notes files (notes/*.md, 8 used)
sicilian-plan, white-open-sicilian-sf, black-ruy-chigorin (T20R2 SF 6.d4, T20R3 Sol added), white-closed-ruy, white-anti-marshall-d3, black-four-knights, black-qgd-lasker, black-giuoco-pianissimo.
