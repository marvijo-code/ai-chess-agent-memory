# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White vs DeepSeek: G1, G9, G14, G15 all 1-0 (notes/white-closed-ruy.md).
- G2 W vs SF 0-1 (Sicilian 3.Bb5, 6.Bc4? b5 7.Bb3?? c4).
- G3 B vs Sol 0-1 (Chigorin, was +B+2P, then 42...Qe6??). G4 B vs Sol draw (Kh7?, exf4?, a5??, b4??).
- G5, G8 W vs Sol 1-0 (4.d3). G6 B vs SF 0-1 (3.Nc3 Nf6 4.Bb5 Bb4). G7 B vs SF 1/2 (8...d6?? 9.f4!).
- G10 W vs SF 1/2 (23.Rc2??). G11 B vs SF 0-1 (Caro Advance 7...Nbc6?? 8.Nb5!). G12 W vs SF 1/2 (18.Bxh7+??, 23.Bd2??).
- G13 B vs Sol 1-0 (QGD Lasker, 17...Nd4!). G15 W vs DeepSeek 1-0.
- G16 W vs SF 0-1 (Alapin, 24.Qxf3?? Qc2, back rank).
- G17 W vs SF 1/2: Maroczy, 13.Bf3?! Ne5, 18.Qe2? f4!, 22.Kh2?? Rxf2+ (notes/white-maroczy.md).
- G18 (T4 R2) B vs Sol 1-0 in 66: QGD Exchange, Bg5. I lost my queen 21...Nxf4?? (Bh7+ discovered Rd1 on Qd7); Sol dropped its queen 39.Qxa7?? Rxa7 and I won R+B vs N. Luck, not play (notes/black-qgd-lasker.md).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Destination must not be my own piece; no own piece on the line (G18: ...Rad8 illegal, Bc8 blocked; check the path).
- X-RAY/DISCOVERY CHECK (G18, worst blunder): before ANY capture or move, list enemy discovered checks/attacks: which enemy piece can move WITH CHECK/tempo and unmask a rook/bishop/queen onto my queen? Queen on the d-file in front of Rd1 with Bd3 between = Bh7+ wins it. Keep my queen off files/diagonals with an enemy battery (no Qd7 vs Bd3+Rd1+Qc2).
- 'Free piece' grabs (G12, G18): if the enemy offers a piece, ask why; list ALL his checks first. A knight 'undefended because the bishop blocks the rook' was bait.
- PAWN-PUSH CHECK (G17, G11): list every enemy PAWN push (...f4, ...e4, ...b5, ...c5) that attacks one of my pieces and count that piece's retreat squares.
- KING-STEP CHECK (G17): before any king move, list what the king stops defending (f2 only held by the queen -> ...Rxf2+).
- BACK-RANK/LUFT (G16): by move 10-12 play h3 (or g3). Before any trade, ask: after ...Qb1+/...Rc1+/...Qd1+, can I interpose or step out?
- RECAPTURE CHOICE (G16): compare ALL recaptures. Which of my pieces stop being defended once my queen leaves?
- LOOSE-BISHOP: after rooks are traded a lone Bc1/Be3 is a target. Keep minors defended.
- SELF-BLOCK CHECK (G9, G12, G15): before any queen move/trade/capture, name the recapturing piece AND its exact path; none of MY pieces may block it.
- PROTECTED-SQUARE CHECK (G10, G11): for every move name who recaptures on the destination and which enemy rook/queen/bishop attacks it.
- KNIGHT-JUMP CHECK (G11): before ...c5/...Nbc6/...a6 ask where an enemy knight can land (b5, d6, c7, f7, e5, d5). Compute 3 plies.
- BLUNDER CHECK: (1) enemy captures on the destination; (2) enemy checks, captures, pawn pushes, discovered attacks, forks; (3) what does my move leave undefended or block?
- WATCH-LIST (G14-G18): after each move note 'watch ...X'; a TODO item must be played NEXT move. In G18 my watch-lists named Bh7+ every move and I still walked into it: LIST IT, THEN TEST THE CAPTURE AGAINST IT.
- SF as Black: improves pieces (...Ne5, ...Rc8, ...f5) while eval creeps, then a pawn push or check wins material. Quiet moves 13-18 need real thought.
- Equal positions vs SF: no pins on my knight; do not leave Bf3 where ...Ne5 hits it with tempo.
- GREED CHECK: no wing-pawn raids, no h7 bishop grabs; keep pieces connected.
- OPENING DISCIPLINE: play only lines I know move by move; slow down at moves 5-10 and 13-18.
- TIME: 1-8 s on book moves is fine, but 60-90 s at every capture, trade, queen move. G18's queen blunder took 59 s, the key check was missed anyway: spend the time on enemy checks, not on my own idea.
- When ahead: trade pieces after the blunder check; check stalemate EVERY move in won endings (G13, G18: worked).
- WHEN LOST (G7, G17 drew; G18 won): keep pieces protected, make threats, play fast and sound; Sol greedily grabs pawns with the queen and can walk into pins. SF repeats checks sometimes (G17), not always (G11).
- Armageddon as White (draw loses): solid d3/c3 setup. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 play 4.d3; vs 3...a6 closed Ruy (5.O-O 6.Re1 7.Bb3 8.c3 9.h3 10.Bc2 11.d4 12.Nbd2). Vs 1...c5: Alapin 2.c3 (notes/sicilian-plan.md) or 2.Nf3 Nc6 3.d4 with 5.c4 Maroczy (notes/white-maroczy.md). Add h3 early.
- Openings as Black: vs 1.d4 QGD (notes/black-qgd-lasker.md; G13 Lasker and G18 Exchange both worked). Vs 1.e4: 1...e5 (notes/black-ruy-chigorin.md; vs 3.Nc3 notes/black-four-knights.md). 1...c6 Advance: notes/black-caro-kann.md first.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 4): Chigorin Ruy as Black; 40-50 s/move, hangs pieces when worse, tries illegal moves. Stay solid.
- Stockfish 19 (depth-4 ladder): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5; vs 2.c3 plays 2...d5 3.exd5 Qxd5; vs 2.Nf3 3.d4 plays ...Nc6, ...g6, ...Nf6, ...Qa5, ...b6, ...Bb7, ...Ne5, ...f5-f4. Builds slowly, then trades into a tactic. Takes all free material.
- GPT-6.1 Sol: White main-line Ruy or 1.d4 2.c4 3.Nf3/Nc3 4.cxd5/Nc3 5.Bg5, Bd3, Qc2, f3-e4 plan with Bh7+ tricks. Black Berlin/...Bc5/...Ba7 vs 4.d3. Passive, then blunders to one-move tactics (G18 Qxa7?? into a rook pin). Sees my blunders too: it found Bh7+ at once.

## Notes files
- notes/sicilian-plan.md: White vs 1...c5 Alapin: G2 loss, G10/G12 draws, G16 loss (back rank).
- notes/white-maroczy.md: G17 Open Sicilian/Maroczy vs SF, ...f4 and Kh2 errors, repetition fortress.
- notes/black-ruy-chigorin.md: Black Chigorin lines G3/G4.
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 lines vs Sol.
- notes/white-closed-ruy.md: G9, G14, G15 closed Ruy wins vs DeepSeek.
- notes/black-four-knights.md: G6/G7 losses vs 3.Nc3.
- notes/black-caro-kann.md: G11 Advance Caro-Kann loss, Nb5/Nd6+ fork.
- notes/black-qgd-lasker.md: G13 Lasker win, G18 Exchange QGD (Bg5/Bd3/Qc2) queen blunder + win vs Sol.
