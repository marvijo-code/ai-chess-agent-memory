# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White vs DeepSeek: G1, G9, G14, G15, G19, G20 all 1-0 (notes/white-closed-ruy.md).
- vs Sol: G5, G8 W 1-0 (4.d3); G13, G18 B 1-0 (QGD; G18 was luck after I lost my queen); G3 B 0-1 (42...Qe6??); G4 B draw (Kh7?, exf4?).
- vs SF as White: G2 0-1 (Sicilian 3.Bb5, 7.Bb3?? c4); G10, G12 draws; G16 0-1 (24.Qxf3?? back rank); G17 draw (Maroczy, 18.Qe2? f4!, 22.Kh2??); G21 0-1 in 26 (Alapin 7.Nxd4? Qxg2!, 9.Bg2?? Qxg2; notes/sicilian-plan.md).
- vs SF as Black: G6 0-1 (3.Nc3 Nf6 4.Bb5 Bb4), G7 draw (8...d6?? 9.f4!), G11 0-1 (Caro Advance 7...Nbc6?? 8.Nb5!).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Destination must not be my own piece; no own piece on the line (G18, G19). Check the path.
- LEAVING-POST CHECK (G21, newest): before moving a piece ask what it stops guarding. Bf1 guards g2, so after Be2 an enemy Qd5 attacks g2 (and Rh1). A queen raid is NOT trapped by Rg1/Bf3: it escapes via h3. Recapture so that nothing hangs (7.cxd4, not 7.Nxd4).
- NEVER hit a queen with an UNDEFENDED piece (G21 9.Bg2?? Qxg2). Before 'attacking with tempo' name who defends the attacker.
- X-RAY/DISCOVERY CHECK (G18, worst blunder): before ANY capture list enemy discovered checks: which enemy piece can move WITH CHECK and unmask a rook/bishop/queen onto my queen? Keep my queen off files/diagonals with an enemy battery.
- 'Free piece' grabs (G12, G18): if the enemy offers a piece, ask why; list ALL his checks first.
- PAWN-PUSH CHECK (G17, G11): list every enemy PAWN push (...f4, ...e4, ...b5, ...c5) that attacks one of my pieces and count that piece's retreat squares.
- KING-STEP CHECK (G17): before any king move, list what the king stops defending (f2 only held by the queen -> ...Rxf2+).
- BACK-RANK/LUFT (G16): by move 10-12 play h3 (or g3). Before any trade ask: after ...Qb1+/...Rc1+, can I interpose or step out?
- RECAPTURE CHOICE (G16, G21): compare ALL recaptures. Which of my pieces/pawns stop being defended?
- LOOSE-BISHOP: after rooks are traded a lone Bc1/Be3 is a target. Keep minors defended.
- SELF-BLOCK CHECK (G9, G12, G15, G19): before any queen move/trade/capture/mate try, name the recapturing/attacking piece AND its exact path; none of MY pieces may block it.
- PROTECTED-SQUARE CHECK (G10, G11, G21): for every move name who recaptures on the destination and which enemy queen/rook/bishop attacks it.
- KNIGHT-JUMP CHECK (G11): before ...c5/...Nbc6/...a6 ask where an enemy knight can land (b5, d6, c7, f7, e5, d5).
- BLUNDER CHECK: (1) enemy captures on the destination; (2) enemy checks, captures, pawn pushes, discovered attacks, forks; (3) what does my move leave undefended or block?
- WATCH-LIST: after each move note 'watch ...X' and TEST the planned capture against it. In G21 my watch-list said '...Qxg2 only if Bf1 moves' and I still moved Bf1: a watch item must change the move, not just be written.
- SF as Black: improves pieces while eval creeps, then a pawn push, check or queen raid wins material. It takes every free pawn/piece, even with its queen (depth 4 sees 2-3 plies). Quiet moves 6-18 need real thought.
- Equal positions vs SF: no pins on my knight; do not leave Bf3 where ...Ne5 hits it with tempo.
- GREED CHECK: no wing-pawn raids, no h7 bishop grabs; keep pieces connected.
- OPENING DISCIPLINE: play only lines I know move by move; slow down at moves 5-10 and 13-18. Spend 30+ s on every early recapture (G21 7.Nxd4 took 26 s but I only looked at ...Qxg2 8.Bf3 and missed 8...Qh3).
- TIME: 1-8 s on book moves, 30-60 s at every capture, trade, queen move.
- When ahead: trade pieces after the blunder check; check stalemate EVERY move in won endings.
- WHEN LOST (G7, G17 drew; G18 won; G21 lost): keep pieces protected, make threats. SF does not always repeat. Down B+P passively (G21) it just built f5-f4/Rg8/Bb7 and mated: count mate threats on Kh1 (Bb7 + Rg8 pin Nf3) and seek counterplay.
- Armageddon as White (draw loses): solid d3/c3 setup. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 play 4.d3; vs 3...a6 closed Ruy (5.O-O 6.Re1 7.Bb3 8.c3 9.h3). Vs 1...c5: Alapin 2.c3 (SF plays 2...d5 3.exd5 Qxd5 4.d4 Nf6 5.Nf3 e6, then 6.Be2? allows ...Qxg2 ideas; see notes/sicilian-plan.md for fixes) or 2.Nf3 Nc6 3.d4 with 5.c4 Maroczy (notes/white-maroczy.md). Add h3 early.
- Openings as Black: vs 1.d4 QGD (notes/black-qgd-lasker.md). Vs 1.e4: 1...e5 (notes/black-ruy-chigorin.md; vs 3.Nc3 notes/black-four-knights.md). 1...c6 Advance: notes/black-caro-kann.md first.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 6): Chigorin or Breyer Ruy as Black; 35-50 s/move, hangs pieces when worse, tries illegal moves. Stay solid.
- Stockfish 19 (depth-4 ladder): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5; vs 2.c3 plays 2...d5 3.exd5 Qxd5 and queen raids on g2; vs 2.Nf3 3.d4 plays ...Nc6, ...g6, ...Nf6, ...Qa5, ...b6, ...Bb7, ...Ne5, ...f5-f4. Takes all free material.
- GPT-6.1 Sol: White main-line Ruy or 1.d4 2.c4 with Bh7+ tricks. Black Berlin/...Bc5/...Ba7 vs 4.d3. Passive, then blunders to one-move tactics. Sees my blunders too.

## Notes files
- notes/sicilian-plan.md: White vs 1...c5 Alapin: G2, G10, G12, G16, G21 (g2 hanging, Qxg2).
- notes/white-maroczy.md: G17 Open Sicilian/Maroczy vs SF, ...f4 and Kh2 errors, repetition fortress.
- notes/black-ruy-chigorin.md: Black Chigorin lines G3/G4.
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 lines vs Sol.
- notes/white-closed-ruy.md: G9, G14, G15, G19, G20 closed Ruy wins vs DeepSeek.
- notes/black-four-knights.md: G6/G7 losses vs 3.Nc3.
- notes/black-caro-kann.md: G11 Advance Caro-Kann loss, Nb5/Nd6+ fork.
- notes/black-qgd-lasker.md: G13 Lasker win, G18 Exchange QGD queen blunder + win vs Sol.
