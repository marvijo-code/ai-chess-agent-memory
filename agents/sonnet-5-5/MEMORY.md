# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White: vs DeepSeek G1,G9,G14,G15,G19,G20,T5R3 all 1-0; vs Sol T5 SF2G1 1-0, T6R3 0-1 (notes/white-closed-ruy.md).
- Chigorin as Black: vs DeepSeek T6R2, T7R2 1-0; vs Sol T5R1 1-0, G3 0-1, G4 draw, T7R1 0-1 (Qc4?? Q for R) (notes/black-ruy-chigorin.md).
- vs Sol: G5, G8 W 1-0 (4.d3); G13, G18 B 1-0 (QGD).
- vs SF as White (1.e4 c5): Sicilian G2, G16, G21, T6R1, G22, T7R3 (Rossolimo 4.e5) losses; G10, G12, G17 draws. White vs SF is my weak spot.
- vs SF as Black: G6 0-1 (3.Nc3 Nf6 4.Bb5 Bb4), G7 draw, G11 0-1 (Caro Advance 7...Nbc6?? 8.Nb5!), T6 4...Nd4 draw.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Trace the path; destination must not be my own piece.
- ATTACKED-PIECE CHECK FIRST (T5R1, T7R3): after each enemy move list every piece of mine it attacks (incl. discovered) and who defends it. T7R3: ...Ng6 hit Bf4, I played Qd3 which did not guard f4 -> lost a piece, game over. If a piece is attacked, the move must save it.
- DEFENDER COUNT (T7R3): before moving a piece, name what it guards (Nf3 was e5's only guard). A pawn I'm 'regaining' may cost a pawn.
- PIN CHECK (T7R3): a pin is real only if the pinned piece is NOT pawn-protected; check enemy pawn pushes hitting my queen (...h4) and her flight squares.
- QUEEN-ESCAPE CHECK (T7R1, T7R3): before a queen capture/move, list squares she can flee to after his pawn/rook/minor attacks her. Q for R/minor is a LOSS. 60+ s.
- MATERIAL COUNT: Q=9, R=5, B/N=3. Recount after every exchange.
- SHIELD CHECK (T6R1): is the moving piece BLOCKING a line onto one of my pieces?
- LEAVING-POST CHECK (G21, T6R1, T7R1, T7R3): what does the moved/captured piece stop guarding?
- NEVER hit a queen with an UNDEFENDED piece (G21).
- X-RAY/DISCOVERY CHECK (G18): list discovered checks onto my queen before captures.
- 'Free piece' grabs (G12, G18, T5R1): ask why it is offered; list ALL his checks and captures.
- KNIGHT-CHECK FORKS (T5R1, T7R1): list enemy knight checks/forks; use them myself.
- PAWN-PUSH CHECK (G17, G11, T7R3): every enemy pawn push that attacks my pieces; count retreat squares.
- KING-STEP CHECK (G17): what does a king move stop defending?
- BACK-RANK/LUFT (G16, T7R1): h3/h6 by move 10-12. Before a trade: after ...Rc1+/Re8+ can I interpose or step out?
- RECAPTURE CHOICE (G16, G21): compare ALL recaptures.
- SELF-BLOCK CHECK (G9, G12, G15, G19): name the recapturer AND its path.
- PROTECTED-SQUARE CHECK (G10, G11, G21): who recaptures on the destination.
- KNIGHT-JUMP CHECK (G11): before ...c5/...Nbc6/...a6 ask where an enemy knight can land.
- BLUNDER CHECK: (1) anything of mine attacked now? (2) enemy captures on destination; (3) enemy checks, pushes, discoveries, forks; (4) what my move leaves undefended.
- WATCH-LIST: a watch item must CHANGE the move; do the check BEFORE the move. Writing 'watch X' then playing into X happened in G22, G18, T7R3.
- SF takes every free pawn; a pawn down vs SF snowballs, a piece down is lost. Prefer solid moves with no loose pawns.
- GREED CHECK: no wing-pawn raids, no h7 grabs; keep pieces connected.
- OPENING DISCIPLINE: play only lines I know; slow down at moves 5-13. 30+ s on captures/recaptures/queen moves. Book moves 1-8 s. Time is plentiful (T7R3 ended with 7:30 unused): spend it early, not after the damage.
- WINNING ENDINGS (T7R2): trade rooks when ahead, push passed pawn, stalemate check EVERY ply; mate with R+2B+N.
- WHEN LOST: keep pieces protected, make threats, trade rooks. Sol hangs pieces under pressure. SF does not reliably repeat.
- Armageddon as White (draw loses): solid d3/c3 setup. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy. Vs 1...c5 SF plays Accelerated Dragon vs 2.Nf3+3.d4; Rossolimo 3.Bb5 4.e5 lost T7R3 (do not play d4 with e5 hanging on Nf3); Alapin lost. See notes/white-open-sicilian-sf.md. Consider a different first move vs SF (1.d4 / 1.Nf3 with e4-free setups) if I have a known plan.
- Openings as Black: vs 1.d4 QGD (notes/black-qgd-lasker.md). Vs 1.e4: 1...e5 (Ruy: notes/black-ruy-chigorin.md; vs 3.Nc3 notes/black-four-knights.md). 1...c6 Advance: notes/black-caro-kann.md.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 9): Ruy 4.Ba4 main line, 14.d5, then drifts (Ng3?? allowing ...Nb3; hanging rook). 35-60 s/move, hangs pieces when worse, tries illegal moves.
- Stockfish 19 (depth-4): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5, 2...Nc6, Accelerated Dragon or ...Nf6/Nd5/Nc7 vs Rossolimo; grabs any loose pawn (Nxe5), punishes any hanging piece.
- GPT-6.1 Sol: White main-line Ruy or 1.d4 2.c4 with Bh7+ tricks. Black: Berlin/...Bc5/...Ba7 vs 4.d3, Chigorin vs closed Ruy. Passive, blunders to one-move tactics, but punishes queen/back-rank errors fast.

## Notes files
- notes/sicilian-plan.md: White vs 1...c5 Alapin (G2, G10, G12, G16, G21).
- notes/white-open-sicilian-sf.md: Open Sicilian/Maroczy G22, G17, T6R1 plus Rossolimo T7R3 vs SF.
- notes/black-ruy-chigorin.md: Black Chigorin G3/G4/T5R1/T6R2/T7R1/T7R2.
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 vs Sol.
- notes/white-closed-ruy.md: closed Ruy wins vs DeepSeek and Sol, T6R3 loss.
- notes/black-four-knights.md: G6/G7/T6 vs 3.Nc3.
- notes/black-caro-kann.md: G11 Advance Caro-Kann loss, Nb5/Nd6+.
- notes/black-qgd-lasker.md: G13 Lasker win, G18 Exchange QGD vs Sol.
