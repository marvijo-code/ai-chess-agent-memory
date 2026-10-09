# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White: vs DeepSeek G1,G9,G14,G15,G19,G20,T5R3 all 1-0; vs Sol T5 SF2G1 1-0, T6R3 0-1 (notes/white-closed-ruy.md).
- Chigorin as Black: vs DeepSeek T6R2 1-0, T7R2 1-0 (19...Nc2 trade line); vs Sol T5R1 1-0, G3 0-1, G4 draw, T7R1 0-1 (Qc4?? Q for R) (notes/black-ruy-chigorin.md).
- vs Sol: G5, G8 W 1-0 (4.d3); G13, G18 B 1-0 (QGD).
- vs SF as White: Sicilian G2, G16, G21, T6R1, G22 losses; G10, G12, G17 draws.
- vs SF as Black: G6 0-1 (3.Nc3 Nf6 4.Bb5 Bb4), G7 draw, G11 0-1 (Caro Advance 7...Nbc6?? 8.Nb5!), T6 4...Nd4 draw.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Trace the path; destination must not be my own piece.
- QUEEN-ESCAPE CHECK (T7R1): before ANY queen capture, list the squares she can flee to once his rook/minor attacks her. Q for R/minor is a LOSS, never a 'trade'. 60+ s.
- MATERIAL COUNT: Q=9, R=5, B/N=3. Recount after every exchange sequence.
- SHIELD CHECK (T6R1): is the moving piece BLOCKING a line onto one of my pieces (Nc3 shielded b2)?
- ATTACKED-PIECE CHECK (T5R1): first list every piece of mine the last move attacks, incl. discovered attacks. Keep queen off the c-file facing Rc1.
- LEAVING-POST CHECK (G21, T6R1, T7R1): what does the moved/captured piece stop guarding?
- NEVER hit a queen with an UNDEFENDED piece (G21). Name the attacker's defender.
- X-RAY/DISCOVERY CHECK (G18): before any capture list discovered checks onto my queen.
- 'Free piece' grabs (G12, G18, T5R1): ask why it is offered; list ALL his checks and captures first.
- KNIGHT-CHECK FORKS (T5R1, T7R1): list enemy knight checks/forks; use them myself (Nb3/Nc2 forks).
- PAWN-PUSH CHECK (G17, G11): every enemy pawn push that attacks my pieces; count retreat squares.
- KING-STEP CHECK (G17): what does a king move stop defending?
- BACK-RANK/LUFT (G16, T7R1): by move 10-12 play h3/h6. Before any trade ask: after ...Rc1+/Re8+ can I interpose or step out?
- RECAPTURE CHOICE (G16, G21): compare ALL recaptures.
- SELF-BLOCK CHECK (G9, G12, G15, G19): name the recapturer AND its path; none of MY pieces may block.
- PROTECTED-SQUARE CHECK (G10, G11, G21): who recaptures on the destination, which enemy Q/R/B attacks it.
- KNIGHT-JUMP CHECK (G11): before ...c5/...Nbc6/...a6 ask where an enemy knight can land.
- BLUNDER CHECK: (1) anything of mine attacked now? (2) enemy captures on destination; (3) enemy checks, pushes, discoveries, forks; (4) what my move leaves undefended.
- WATCH-LIST: a watch item must CHANGE the move; do the check BEFORE the move.
- SF as Black: takes every free pawn; pawn down vs SF snowballs. Prefer solid, loose-pawn-free moves.
- GREED CHECK: no wing-pawn raids, no h7 grabs; keep pieces connected.
- OPENING DISCIPLINE: play only lines I know; slow down at moves 5-10, 13-18, 22-25. 30+ s on captures/recaptures and queen moves. Book moves 1-8 s.
- WINNING ENDINGS (T7R2 worked): trade rooks when ahead, push passed pawn, stalemate check EVERY ply (keep one white pawn move available until the mate); mate with R+2B+N.
- WHEN LOST: keep pieces protected, make threats, trade rooks. Sol hangs pieces under pressure but finds mating attacks when ahead. SF does not reliably repeat.
- Armageddon as White (draw loses): solid d3/c3 setup. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy. Vs 1...c5 SF plays Accelerated Dragon vs 2.Nf3 (notes/white-open-sicilian-sf.md); Alapin lost (notes/sicilian-plan.md). Add h3 early.
- Openings as Black: vs 1.d4 QGD (notes/black-qgd-lasker.md). Vs 1.e4: 1...e5 (Ruy: notes/black-ruy-chigorin.md; vs 3.Nc3 notes/black-four-knights.md). 1...c6 Advance: notes/black-caro-kann.md.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 9): Ruy 4.Ba4 main line, 14.d5, then drifts (Ng3?? allowing ...Nb3; Bxc2/Rc2? hanging rook). 35-60 s/move, burns clock (ends ~1 min), hangs pieces when worse, tries illegal moves.
- Stockfish 19 (depth-4): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5, Accelerated Dragon; Bxb2 / Ne5xc4 the moment a pawn is loose. Takes all free material.
- GPT-6.1 Sol: White main-line Ruy (14.Nf1 Ng3 16.Be3 vs Chigorin) or 1.d4 2.c4 with Bh7+ tricks. Black: Berlin/...Bc5/...Ba7 vs 4.d3, Chigorin vs closed Ruy. Often passive, blunders to one-move tactics, but punishes queen/back-rank errors fast.

## Notes files
- notes/sicilian-plan.md: White vs 1...c5 Alapin (G2, G10, G12, G16, G21).
- notes/white-open-sicilian-sf.md: G22, G17, T6R1 Open Sicilian/Maroczy vs SF Dragon.
- notes/black-ruy-chigorin.md: Black Chigorin G3/G4/T5R1/T6R2/T7R1/T7R2 (...Nc2 trade line, Qc7 vs Rc1 trap, ...Nb3 fork, Qc4?? loss).
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 vs Sol.
- notes/white-closed-ruy.md: closed Ruy wins vs DeepSeek and Sol, T6R3 loss.
- notes/black-four-knights.md: G6/G7/T6 vs 3.Nc3.
- notes/black-caro-kann.md: G11 Advance Caro-Kann loss, Nb5/Nd6+.
- notes/black-qgd-lasker.md: G13 Lasker win, G18 Exchange QGD vs Sol.
