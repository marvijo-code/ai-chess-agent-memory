# MEMORY (clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy White: DeepSeek 8 W; Sol 4 W 5 L 1 D. Sicilian White vs DeepSeek 6 W.
- Chigorin Black: DeepSeek 14 W 1 D; Sol 2 W 8 L 2 D. QGD Lasker: Sol 3 W 1 L, DeepSeek 1 W. Pianissimo 3.Bc4: Sol 2 L, DeepSeek 1 W (T19R5.2).
- vs SF White: Alapin lost 4x; Maroczy drew 2; T19R2 Open 5.Nc3 e6 drew a piece down. vs SF Black 3.Nc3: 9 L 5 D.

## Key lessons (read before EVERY move)
- CLOCK FIRST (T18SF2G1G1, T19SF2G1G1 FLAGGED: 55-60 s on ~20 quiet moves). Budget: book 1-5 s; quiet 10-15 s (pick the move, check hanging pieces, play); 45 s max only at captures/trades/breaks/first non-book move. Under 8:00 cap 15 s, under 4:00 cap 8 s, under 1:30 cap 3 s. Never >2 min behind Sol.
- PAWN-GUARDED PAWN (T19SF2G1G1 32.Nxc4?? bxc4 Rxc4 = N for 2 P): count VALUES, not attackers. A piece taking a pawn-guarded pawn is a sac.
- PAWN PUSH AT HIS BISHOP (T19R5.2 9...a4?! 10.Bxa4: Ra8 sole guard, Qd1 backs Bxa4): count the pawn's guards vs his capturers incl. queen x-ray BEFORE ...a4/...b5; else Bxb3 or a quiet move.
- ILLEGAL MOVES (3 = forfeit; T19R1 used all 3: 19.Qxc6 blocked by my Rd5, 22.Bf4 by my Ne3): trace paths square by square INCLUDING my own pieces and his just-pushed pawn; list pins on my king. Output only the JSON move object.
- MY OWN PIECE/PAWN BLOCKS MY LINE (T19R2 11.Bd3?? d4! Qxd4 blocked; T19R3 10...Nc6? my e6 pawn blocks Qe7-e4): ask 'which file/diagonal/guard does this close?'; list his pawn pushes (...d4, ...e4) hitting my bishops BEFORE Bd3/Be2.
- HIS LAST MOVE FIRST (T18SF2G1G1 33.e5 dxe5 34.Bxe5 Bxd5?? 35.Bxb8): if it attacks my piece, save it before grabbing; a 'free pawn' is bait. After a pawn leaves a diagonal, re-walk his bishop lines.
- BEFORE EVERY MOVE write 'his checks/captures after this' (T16R1 Re8?? Qxf7+). KNIGHT SWEEP (T18R3 38...Qc6?? Ne7+). BISHOP SWEEP to the edge (T17SF2G1 Ra7?? Bxa7). QUEEN: write 'Q on X, attacked by A, defended via path P' and trace P (T12SF2G1 Qf5??).
- TRAP CHECK (T18R3 18...Nb4? 19.Bb1 Qd8? 20.a3): before a piece goes to the edge/into his camp list EVERY retreat square and pawn kick; prepare the retreat (...a5) first.
- CAPTURE CHAIN / SCREEN (T14SF2G1 Qxc1??; T15R1 Bxc3?? Qxc3; T17R1 36.Nxc2?? unmasked Qb6-f2): write the chain with values; what does this piece screen?
- PLAN, NOT DRIFT (T17R1 22-28; T18R1 19-40; T19SF2G1G1 27-31): name a plan every move; list HIS breaks; before ...b4/...a3/...f5 write my recapture. As White vs Chigorin AVOID d5 (T17R1, T19SF2G1G1 = ...c4 clamp + ...Bd6); think before Bxc5 dxc5.
- PAWN DOWN VS DEEPSEEK (T19R3, T19R5.2 both won): make threats it must see (...e5/...exd4; ...Na5/...b5/...c5/...c4), keep every unit guarded, recheck each capture; it hangs Q/R/B within 10 moves.
- CONVERSION (T13R1 B+B+N = DRAW; T15R3 drew 5 pawns up; T19R1 WON OCB 2 pawns up): trade rooks when up, vary at the FIRST repeat, safe captures only, stalemate check every ply.
- WHITE 8.d3 vs 7...O-O (notes/white-anti-marshall-d3.md): 11...d5 12.exd5 Nxd5 13.Nxe5! Nxe5 14.Rxe5 Bf6 15.Rxe8+ Qxe8 16.Bd2 = clean pawn up. Don't drift Qe2/Bc2.
- CHIGORIN as Black (notes/black-ruy-chigorin.md): ...Bd7 ...a5 ...Rac8 THEN ...Rfe8 ...g6 (skipped = T18R3, T18SF2G1G1 losses). COUNT d4 attackers/defenders each move after c3 trade. Vs d5: ...c4 clamp or ...Nb8; ...Nb4 only with ...a5. Keep rooks.
- VS 3.Bc4 (notes/black-giuoco-pianissimo.md): 3...Nf6 4.d3 Be7 5.O-O O-O 6.c3 d6, ...Be6, ...Re8/...h6; don't push ...a4 into Bxa4. Keep a bishop.
- VS SF 3.Nc3 AS BLACK (notes/black-four-knights.md): 3...Nf6 4.Bb5 Bb4, never 3...Bc5. A) 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 ONLY; 10.Bc4 try ...Bd6 (never Bxd2, Qf6, Bc5). B) 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 Qe7 8.dxc6 dxc6 9.Bxc6+ bxc6 10.Nd4 Bd7! ... 14.Qxe7 Bxe7; no ...d5 later. Think 3+ min at moves 10, 11, 18-26 (only here).
- LOST VS SF: blockade passed pawn with B+K; SF repeats at +7..+10 = draw (avoid Ka1/Ka2). SF never errs; Q for R/minor is a LOSS.
- LUFT: h3 by move 9-12 but not at the cost of Be3. Before rook trades: 'Qb1+/Qa1+, my only blocker?'
- Armageddon: White (draw loses) solid, luft first; Black (draw wins) safest setup.
- Repertoire: W 1.e4 e5 2.Nf3 3.Bb5 (3...Nf6 4.d3; 3...a6 closed Ruy h3, 8.d3 vs ...O-O; vs Chigorin 14.Nb3/Nf1 not d5); vs 1...c5 DeepSeek Yugoslav 9.Bc4; SF Maroczy never Alapin; SF ...Nf6/...e6 5.Nc3 e6 6.Nxc6 bxc6 7.e5 Nd5 8.Ne4 Qc7 9.f4 (not Bd2/Bd3). B: 1.d4 QGD Lasker (after 9.Nxe4 dxe4 10.Nd2 play ...f5, not ...Nc6); 1.e4 e5 (Chigorin; 3.Bc4 Nf6 4.d3 Be7; 3.Nc3 A/B).

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 29): Chigorin as White (Qe2, Ng3, 18.Nxd4??); Pianissimo (4.d3, Nbd2, Bb3, grabs a4, 16.Qxd6?? hung Q); QGD Bg5/Bh4, 15.Qxd4?? hung Q; as Black Dragon, speculative sacs, illegal moves. 15-50 s/move.
- Stockfish 19 (depth 4-5): instant. White 1.e4 2.Nf3 3.Nc3 4.Bb5, 5.O-O or 5.Nd5. Black ...c5 ...Nc6 ...g6 Maroczy, or ...Nf6 ...e6 ...bxc6 ...Nd5 ...Qc7 ...Bc5 ...d4. Grabs loose pawns, piles on a weak pawn, back-rank checks; repeats vs a blockade.
- GPT-6.1 Sol: Black Chigorin (14.d5 Nb4 15.Bb1 a5 16.a3 Na6 ...Nc5, ...Bd7, ...Rfc8, ...a4, ...c4, ...Bd6; ...Ncxe4; ...f5/...e4+). White: Ruy Nf1-g3 + d5, 3.Bc4, 1.d4. 5-45 s/move, banks the clock, takes every free piece, converts a piece up with a passed pawn, Q+R raids, knight forks; hangs pieces when behind.

## Notes files (notes/*.md, 8 used)
sicilian-plan, white-open-sicilian-sf, black-ruy-chigorin, white-closed-ruy, white-anti-marshall-d3, black-four-knights, black-qgd-lasker, black-giuoco-pianissimo (T19R5.2 win added).
