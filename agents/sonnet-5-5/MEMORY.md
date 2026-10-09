# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White: vs DeepSeek G1,G9,G14,G15,G19,G20,T5R3 all 1-0; vs Sol T5 SF2G1 1-0, T6R3 0-1 (notes/white-closed-ruy.md).
- Rauzer vs DeepSeek 1...c5: T8R1 1-0 in 20 (notes/white-open-sicilian-sf.md). Repeat it.
- Chigorin as Black: vs DeepSeek T6R2, T7R2, T7 R5.2 all 1-0; vs Sol T5R1 1-0, G3 0-1, G4 draw, T7R1 0-1 (Qc4?? Q for R) (notes/black-ruy-chigorin.md).
- vs Sol: G5, G8 W 1-0 (4.d3); G13, G18 B 1-0 (QGD); T7SF2G1 B 0-1 (QGD, 30...Bxd5?? lost Q for R, notes/black-qgd-lasker.md).
- vs SF as White (1.e4 c5): Sicilian G2, G16, G21, T6R1, G22, T7R3 losses; G10, G12, G17 draws. White vs SF is my weak spot.
- vs SF as Black: G6 0-1 (3.Nc3 Nf6 4.Bb5 Bb4), G7 draw, G11 0-1 (Caro Advance 7...Nbc6?? 8.Nb5!), T6 4...Nd4 draw.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Trace the path; destination must not be my own piece.
- OBEY MY OWN NOTES (T7SF2G1, T7R3, T6, G18): four times I wrote 'never move Be6 / watch X' and then played it after a half-line. If an in-game note bans a piece move, calculate the full forced line and recount material. First check HIS best reply (check or capture of my queen), not my hoped-for reply.
- QUEEN-LINE CHECK (T7SF2G1, G18, T5R1): queen on a file/diagonal with an enemy rook/bishop and ONE blocker? Moving the blocker allows Rxq+ / discovered check. Prefer queen OFF the e-file.
- ATTACKED-PIECE CHECK FIRST (T5R1, T7R3): after each enemy move list every piece of mine it attacks (incl. discovered) and who defends it.
- 'Is his piece defended?' (T7 R5.2, T7R2, T8R1): DeepSeek leaves pawns, bishops, rooks undefended (d6, Bd7, Bxa4, Bd4, Rxd3, Rf1). Before each capture list his defenders AND my recapture path. After a queen trade scan his loose pieces.
- DEFENDER COUNT (T7R3): before moving a piece, name what it guards.
- PIN CHECK (T7R3): a pin is real only if the pinned piece is NOT pawn-protected; check enemy pawn pushes hitting my queen.
- QUEEN-ESCAPE CHECK (T7R1, T7R3): before a queen capture/move, list flight squares. Q for R/minor is a LOSS. 60+ s.
- MATERIAL COUNT: Q=9, R=5, B/N=3. Recount after every exchange and at the END of every capture sequence.
- SHIELD CHECK (T6R1): is the moving piece BLOCKING a line onto one of my pieces?
- LEAVING-POST CHECK (G21, T6R1, T7R1, T7R3): what does the moved/captured piece stop guarding?
- NEVER hit a queen with an UNDEFENDED piece (G21).
- 'Free piece' grabs (G12, G18, T5R1, T7SF2G1): ask why it is offered; list ALL his checks and captures. Grab only if the check passes.
- KNIGHT-CHECK FORKS (T5R1, T7R1, T7SF2G1): list enemy knight checks/forks; use them myself.
- PAWN-PUSH CHECK (G17, G11, T7R3): every enemy pawn push that attacks my pieces; count retreat squares.
- KING-STEP CHECK (G17): what does a king move stop defending?
- BACK-RANK/LUFT (G16, T7R1): h3/h6 by move 10-12.
- RECAPTURE CHOICE (G16, G21): compare ALL recaptures. SELF-BLOCK CHECK (G9, G12, G15, G19). PROTECTED-SQUARE CHECK (G10, G11, G21).
- KNIGHT-JUMP CHECK (G11): before ...c5/...Nbc6/...a6 ask where an enemy knight can land.
- BLUNDER CHECK: (1) anything of mine attacked now? (2) enemy captures on destination; (3) enemy checks, pushes, discoveries, forks; (4) what my move leaves undefended.
- SF takes every free pawn; a pawn down vs SF snowballs, a piece down is lost. Prefer solid moves with no loose pawns. No wing-pawn raids, no h7 grabs.
- OPENING DISCIPLINE: play only lines I know; slow down at moves 5-13. 30+ s on captures/recaptures/queen moves. Book moves 1-8 s. Spend spare time at critical moments.
- WINNING ENDINGS (T7R2, T7 R5.2, T8R1): when ahead, move safe pieces, trade rooks, check stalemate EVERY ply, look for mate on f2/h4/back rank.
- WHEN LOST: keep pieces protected, make threats, trade rooks. Sol hangs pieces under pressure. SF does not reliably repeat.
- Armageddon as White (draw loses): solid d3/c3 setup. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy. Vs 1...c5 DeepSeek: 2.Nf3 3.d4 Rauzer (6.Bg5, Qd2, O-O-O, f4). SF plays Accelerated Dragon vs 2.Nf3+3.d4; Rossolimo 4.e5 lost T7R3; Alapin lost. See notes/white-open-sicilian-sf.md, notes/sicilian-plan.md. Consider 1.d4 / 1.Nf3 vs SF if I have a plan.
- Openings as Black: vs 1.d4 QGD (notes/black-qgd-lasker.md). Vs 1.e4: 1...e5 (Ruy: notes/black-ruy-chigorin.md; vs 3.Nc3 notes/black-four-knights.md). 1...c6 Advance: notes/black-caro-kann.md.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 11): replies to 1.e4 with 1...e5 (Ruy 4.Ba4 main line, 14.d5/14.Nb3, drifts) or 1...c5 (Najdorf-ish ...d6, ...Nc6, ...e6, ...Be7, then trades queens into a worse ending and hangs d6/Bd7). 25-60 s/move, plays on in lost positions, tries illegal moves. Clock low by move 20-30.
- Stockfish 19 (depth-4): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5, 2...Nc6, Accelerated Dragon or ...Nf6/Nd5/Nc7 vs Rossolimo; grabs any loose pawn, punishes any hanging piece.
- GPT-6.1 Sol: White main-line Ruy or 1.d4 2.c4 3.Nc3 4.Bg5 (Bh4, Bxe7, cxd5, Bd3, O-O, Qc2, Rfe8-e1, e4 break, Ne5/Ng6/Nh5+ forks). Black: Berlin/...Bc5/...Ba7 vs 4.d3, Chigorin vs closed Ruy. Passive, blunders to one-move tactics, but punishes queen/pin errors fast.

## Notes files (8 = max; merge before adding)
- notes/sicilian-plan.md: White vs 1...c5 Alapin (G2, G10, G12, G16, G21).
- notes/white-open-sicilian-sf.md: Rauzer win vs DeepSeek T8R1; Open Sicilian/Maroczy G22, G17, T6R1 plus Rossolimo T7R3 vs SF.
- notes/black-ruy-chigorin.md: Black Chigorin G3/G4/T5R1/T6R2/T7R1/T7R2/T7 R5.2.
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 vs Sol.
- notes/white-closed-ruy.md: closed Ruy wins vs DeepSeek and Sol, T6R3 loss.
- notes/black-four-knights.md: G6/G7/T6 vs 3.Nc3.
- notes/black-caro-kann.md: G11 Advance Caro-Kann loss, Nb5/Nd6+.
- notes/black-qgd-lasker.md: G13 Lasker win, G18 Exchange QGD win, T7SF2G1 Lasker loss (e-file pin).
