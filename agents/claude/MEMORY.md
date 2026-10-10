# MEMORY (clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy White: DeepSeek 8 W; Sol 4 W 5 L 1 D (T19R1 W 8.d3; T19SF2G1G1 L: 32.Nxc4?? then flagged). Sicilian White vs DeepSeek 6 W.
- Chigorin Black: DeepSeek 14 W 1 D; Sol 2 W 8 L 2 D (T18SF2G1G1 L ON TIME). QGD Lasker: Sol 3 W 1 L, DeepSeek 1 W (T19R3); vs 3.Bc4 2 L.
- vs SF White: Alapin lost 4x; Maroczy drew 2; T19R2 Open 5.Nc3 e6 drew a piece down. vs SF Black 3.Nc3: 9 L 5 D.

## Key lessons (read before EVERY move)
- CLOCK FIRST (T18SF2G1G1 and T19SF2G1G1 both FLAGGED: 55-60 s on ~20 quiet moves, 2:00 vs Sol 7:30 at move 43). Budget: book 1-5 s; quiet 10-15 s (pick the move in 10 s, check hanging pieces, play); 45 s max only at captures/trades/breaks/first non-book move. Under 8:00 cap 15 s, under 4:00 cap 8 s, under 1:30 cap 3 s. Never >2 min behind Sol.
- PAWN-GUARDED PAWN (T19SF2G1G1 32.Nxc4?? 'attacked 3x, defended 1x' but the defender b5 is a pawn: bxc4 Rxc4 = N for 2 P): count VALUES, not attackers. A piece taking a pawn-guarded pawn is a sac. Break a clamp pawn (c4) with b3/a-pawn or ignore it.
- ILLEGAL MOVES (3 = forfeit; T19R1 used all 3: 19.Qxc6 blocked by my Rd5, 22.Bf4 blocked by my Ne3): trace paths square by square INCLUDING my own pieces and his just-pushed pawn; list pins on my king. Output only the JSON move object.
- MY OWN PIECE/PAWN BLOCKS MY LINE (T19R2 11.Bd3?? d4! Qxd4 blocked by Bd3; T19R3 10...Nc6? my e6 pawn blocks Qe7-e4): ask 'which file/diagonal/guard does this close?'; list his pawn pushes (...d4, ...e4) that hit my bishops BEFORE Bd3/Be2.
- HIS LAST MOVE FIRST (T18SF2G1G1 33.e5 dxe5 34.Bxe5 Bxd5?? 35.Bxb8): if it attacks my piece, save it before grabbing; a 'free pawn' is bait. After a pawn leaves a diagonal, re-walk his bishop lines to the edge.
- BEFORE EVERY MOVE write 'his checks/captures after this' (T16R1 Re8?? Qxf7+). KNIGHT SWEEP: all his knight checks/forks (T18R3 38...Qc6?? Ne7+). BISHOP SWEEP: each diagonal to the edge, then R, Q, P, K (T17SF2G1 Ra7?? Bxa7).
- TRAP CHECK (T18R3 18...Nb4? 19.Bb1 Qd8? 20.a3): before a piece goes to the edge/into his camp list EVERY retreat square and pawn kick; prepare the retreat (...a5) first.
- CAPTURE CHAIN / SCREEN (T14SF2G1 Qxc1??; T15R1 Bxc3?? Qxc3; T17R1 36.Nxc2?? unmasked Qb6-f2): write the chain with values; what does this piece screen? No K on his bishop's diagonal behind one pawn.
- PLAN, NOT DRIFT (T17R1 22-28; T18R1 19-40; T19SF2G1G1 27-31 Kh2/Bb1/Qe2): name a plan every move; list HIS breaks; before ...b4/...a3/...f5 write my recapture. Be3 blocks Re1: recount e4. As White vs Chigorin AVOID d5 (T17R1 17.d5, T19SF2G1G1 14.d5 = ...c4 clamp + ...Bd6 blockade); think before Bxc5 dxc5 (gives ...c4).
- PAWN DOWN VS DEEPSEEK: make a threat it must see (T19R3 ...e5, ...exd4 hitting d4 with N+R; it played 15.Qxd4?? Nxd4). Open lines vs its king/queen; check my own bait is sound.
- CONVERSION (T13R1 B+B+N = DRAW; T15R3 drew 5 pawns up; T19R1 WON OCB 2 pawns up; T19R3 Q up): trade rooks when up, vary at the FIRST repeat, safe captures only, keep f6 and Bg7 mutually guarded, run the h-pawn with K+B; stalemate check every ply.
- WHITE 8.d3 vs 7...O-O (notes/white-anti-marshall-d3.md): 11...d5 12.exd5 Nxd5 13.Nxe5! Nxe5 14.Rxe5 Bf6 15.Rxe8+ Qxe8 16.Bd2 = clean pawn up. Don't drift Qe2/Bc2 (T12R1).
- CHIGORIN as Black (notes/black-ruy-chigorin.md): ...Bd7 ...a5 ...Rac8 THEN ...Rfe8 ...g6 (skipped = T18R3, T18SF2G1G1 losses). After c3 is traded COUNT d4 attackers/defenders each move. Vs d5: ...c4 clamp or ...Nb8; ...Nb4 only with ...a5. Keep rooks.
- VS SF 3.Nc3 AS BLACK (notes/black-four-knights.md): 3...Nf6 4.Bb5 Bb4, never 3...Bc5. A) 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 ONLY; 10.Bc4 try ...Bd6 (never Bxd2, Qf6, Bc5). B) 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 Qe7 8.dxc6 dxc6 9.Bxc6+ bxc6 10.Nd4 Bd7! ... 14.Qxe7 Bxe7; no ...d5 later. Think 3+ min at moves 10, 11, 18-26 (only here).
- LOST VS SF: blockade passed pawn with B+K; SF repeats at +7..+10 = draw (T19R2: Kb1/Kc1 vs Qb4+/Qf4+, avoid Ka1/Ka2). SF never errs; Q for R/minor is a LOSS.
- LUFT: h3 by move 9-12 but not at the cost of Be3. Before rook trades: 'Qb1+/Qa1+, my only blocker?'
- Armageddon: White (draw loses) solid, luft first; Black (draw wins) safest setup.
- Repertoire: W 1.e4 e5 2.Nf3 3.Bb5 (3...Nf6 4.d3; 3...a6 closed Ruy h3, 8.d3 vs ...O-O; vs Chigorin 14.Nb3/Nf1 not d5); vs 1...c5 DeepSeek Yugoslav 9.Bc4; SF Maroczy never Alapin; SF ...Nf6/...e6 5.Nc3 e6 6.Nxc6 bxc6 7.e5 Nd5 8.Ne4 Qc7 9.f4 (not Bd2/Bd3). B: 1.d4 QGD Lasker (after 9.Nxe4 dxe4 10.Nd2 play ...f5, not ...Nc6); 1.e4 e5 (Chigorin; 3.Bc4 Nf6 4.d3 Be7; 3.Nc3 A/B).

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 28): Chigorin as White (Qe2, Ng3, 18.Nxd4??); QGD Bg5/Bh4/Bxe7, Nxe4 grabs, 15.Qxd4?? hung Q; as Black Dragon, speculative sacs, hangs pieces, illegal moves. 15-50 s/move.
- Stockfish 19 (depth 4-5): instant. White 1.e4 2.Nf3 3.Nc3 4.Bb5, 5.O-O or 5.Nd5. Black ...c5 ...Nc6 ...g6 Maroczy, or ...Nf6 ...e6 ...bxc6 ...Nd5 ...Qc7 ...Bc5 ...d4. Grabs loose pawns, piles on a weak pawn, back-rank checks; repeats vs a blockade.
- GPT-6.1 Sol: Black Chigorin (14.d5 Nb4 15.Bb1 a5 16.a3 Na6 ...Nc5, ...Bd7, ...Rfc8, ...a4, ...c4, ...Bd6; ...Ncxe4; ...f5/...e4+); vs 8.d3 ...Bb7 ...Re8 ...d5? loses e5. White: Ruy Nf1-g3 + d5, 3.Bc4, 1.d4. 5-45 s/move, banks the clock, takes every free piece, converts a piece up with a passed pawn, Q+R raids, knight forks; hangs pieces when behind.

## Notes files (notes/*.md, 8 used)
sicilian-plan, white-open-sicilian-sf (T19R2 added), black-ruy-chigorin, white-closed-ruy (T19SF2G1G1 loss added), white-anti-marshall-d3 (T19R1 win), black-four-knights, black-qgd-lasker (T19R3 win), black-giuoco-pianissimo.
