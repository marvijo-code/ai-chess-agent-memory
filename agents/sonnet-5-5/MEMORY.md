# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White: vs DeepSeek G1, G9, G14, G15, G19, G20, T5R3 all 1-0; vs Sol T5 SF2G1 1-0 in 56 (Chigorin; notes/white-closed-ruy.md).
- vs Sol: G5, G8 W 1-0 (4.d3); G13, G18 B 1-0 (QGD; G18 luck after I lost my queen); G3 B 0-1 (42...Qe6??); G4 B draw (Kh7?, exf4?); T5R1 B 1-0 (Chigorin; I hung Qc7 with 24...Nxb4??; notes/black-ruy-chigorin.md).
- vs SF as White: G2 0-1 (Sicilian 3.Bb5, 7.Bb3?? c4); G10, G12 draws; G16 0-1 (24.Qxf3?? back rank); G17 draw (Maroczy, 18.Qe2? f4!, 22.Kh2??); G21 0-1 (Alapin 7.Nxd4? Qxg2!, 9.Bg2?? Qxg2; notes/sicilian-plan.md).
- vs SF as Black: G6 0-1 (3.Nc3 Nf6 4.Bb5 Bb4), G7 draw (8...d6?? 9.f4!), G11 0-1 (Caro Advance 7...Nbc6?? 8.Nb5!).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Destination must not be my own piece; no piece on the line (SF2G1 Rb6 blocked by b5 pawn). Trace the path.
- ATTACKED-PIECE CHECK (T5R1, cost my queen): FIRST list every one of my pieces the enemy's last move attacks, INCLUDING discovered attacks. If my queen is attacked, move/guard/trade it. Keep queen off the c-file facing Rc1.
- LEAVING-POST CHECK (G21): what does the moved piece stop guarding (Bf1 guards g2)? A queen raid is not trapped: Qh3 escapes.
- NEVER hit a queen with an UNDEFENDED piece (G21). Name the attacker's defender.
- X-RAY/DISCOVERY CHECK (G18): before ANY capture list enemy discovered checks and unmasked lines onto my queen.
- 'Free piece' grabs (G12, G18, T5R1): if the enemy offers something, ask why; list ALL his checks and captures first.
- KNIGHT-CHECK FORKS (T5R1 51.Ne7+): before a pawn/rook grab list enemy knight checks and forks.
- PAWN-PUSH CHECK (G17, G11, SF2G1 17...d5): list every enemy pawn push (...d5, ...f4, ...e4, ...b5, ...c5) that attacks my pieces; count retreat squares. Before a quiet queen move (Qd2) check the central break.
- KING-STEP CHECK (G17): before a king move list what the king stops defending.
- BACK-RANK/LUFT (G16): by move 10-12 play h3. Before any trade ask: after ...Qb1+/...Rc1+, can I interpose or step out?
- RECAPTURE CHOICE (G16, G21): compare ALL recaptures; which pieces stop being defended?
- LOOSE-BISHOP: after rooks are traded a lone Bc1/Be3 is a target. Keep minors defended.
- SELF-BLOCK CHECK (G9, G12, G15, G19): before any queen move/trade/mate try, name the recapturer AND its path; none of MY pieces may block.
- PROTECTED-SQUARE CHECK (G10, G11, G21): for every move name who recaptures on the destination and which enemy Q/R/B attacks it.
- KNIGHT-JUMP CHECK (G11): before ...c5/...Nbc6/...a6 ask where an enemy knight can land (b5, d6, c7, f7, e5, d5).
- BLUNDER CHECK: (1) is anything of mine attacked now? (2) enemy captures on the destination; (3) enemy checks, pushes, discoveries, forks; (4) what does my move leave undefended or block?
- WATCH-LIST: a watch item must CHANGE the move, not just be written. Good habit (T5R3, SF2G1): a short note each ply naming the specific trick, then actually avoiding it.
- SF as Black: improves pieces, then a pawn push, check or queen raid wins material; takes every free pawn/piece.
- Equal positions vs SF: no pins on my knight; do not leave Bf3 where ...Ne5 hits it with tempo.
- GREED CHECK: no wing-pawn raids, no h7 bishop grabs; keep pieces connected.
- OPENING DISCIPLINE: play only lines I know move by move; slow down at moves 5-10, 13-18, 22-25. 30+ s on every capture/recapture.
- TIME: 1-8 s on book moves, 30-60 s at every capture, trade, queen move.
- WINNING ENDINGS (SF2G1): trade rooks when up a piece, never capture a pawn defended by the king or a pawn (Rxg5+, Rxb5), push the passed pawn, check stalemate EVERY move.
- WHEN LOST (G7, G17 drew; G18, T5R1 won): keep pieces protected, make threats, play solid. Sol hangs pieces under pressure. SF does not always repeat.
- Armageddon as White (draw loses): solid d3/c3 setup. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 play 4.d3; vs 3...a6 closed Ruy (5.O-O 6.Re1 7.Bb3 8.c3 9.h3). Vs 1...c5: Alapin 2.c3 (notes/sicilian-plan.md) or 2.Nf3 Nc6 3.d4 with 5.c4 Maroczy (notes/white-maroczy.md). Add h3 early.
- Openings as Black: vs 1.d4 QGD (notes/black-qgd-lasker.md). Vs 1.e4: 1...e5 (notes/black-ruy-chigorin.md; vs 3.Nc3 notes/black-four-knights.md). 1...c6 Advance: notes/black-caro-kann.md first.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 7): Chigorin or Breyer Ruy as Black; 35-60 s/move, hangs pieces when worse, tries illegal moves. Stay solid.
- Stockfish 19 (depth-4): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5; vs 2.c3 plays 2...d5 3.exd5 Qxd5 and queen raids on g2; vs 2.Nf3 3.d4 plays ...Nc6, ...g6, ...Nf6, ...Qa5, ...b6, ...Bb7, ...Ne5, ...f5-f4. Takes all free material.
- GPT-6.1 Sol: White main-line Ruy (14.d5, Rc1 vs my Qc7, b4, Bd3 discovery) or 1.d4 2.c4 with Bh7+ tricks. Black: Berlin/...Bc5/...Ba7 vs 4.d3, Chigorin vs the closed Ruy (...d5 at move 17). Passive, then blunders to one-move tactics (19...Nxe3, 20...Nxe5, 33...Rc1+). Sees my blunders too.

## Notes files
- notes/sicilian-plan.md: White vs 1...c5 Alapin (G2, G10, G12, G16, G21).
- notes/white-maroczy.md: G17 Maroczy vs SF, ...f4 and Kh2 errors, fortress.
- notes/black-ruy-chigorin.md: Black Chigorin G3/G4/T5R1 (Qc7 vs Rc1 trap).
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 vs Sol.
- notes/white-closed-ruy.md: closed Ruy wins vs DeepSeek and Sol (17.Qd2?? note, conversion).
- notes/black-four-knights.md: G6/G7 losses vs 3.Nc3.
- notes/black-caro-kann.md: G11 Advance Caro-Kann loss, Nb5/Nd6+.
- notes/black-qgd-lasker.md: G13 Lasker win, G18 Exchange QGD vs Sol.
