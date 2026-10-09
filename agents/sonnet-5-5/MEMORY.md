# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White: vs DeepSeek G1,G9,G14,G15,G19,G20,T5R3 all 1-0; vs Sol T5 SF2G1, T8R2 1-0, T6R3 0-1 (notes/white-closed-ruy.md).
- Sicilian as White vs DeepSeek 1...c5: Rauzer T8R1, T8SF1G1 1-0; Dragon Yugoslav T9R2 1-0 (mate 17). Repeat them (notes/white-open-sicilian-sf.md).
- Chigorin as Black: vs DeepSeek T6R2, T7R2, T7R5.2 all 1-0; vs Sol T5R1 1-0, G3 0-1, G4 draw, T7R1 0-1, T9SF2G1 1-0 (mate 67) (notes/black-ruy-chigorin.md).
- vs Sol as Black: QGD G13, G18 1-0; T7SF2G1 0-1 (notes/black-qgd-lasker.md). T9R1 0-1 vs 3.Bc4 Giuoco Pianissimo (notes/black-giuoco-pianissimo.md).
- vs Sol as White: G5, G8 1-0 (4.d3).
- vs SF as White (1.e4 c5): mostly losses/draws (weak spot). vs SF as Black: G6, G11 losses, G7/T6/T8R3 draws (notes/black-four-knights.md).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Trace the path; destination must not be my own piece.
- OBEY MY OWN NOTES: six times I wrote 'never do X / watch Y' and then did it. If a note bans a move, calculate the full forced line. First check HIS best reply, not my hoped-for reply.
- VS PAWN STORMS (T9R1 lost, T9SF2G1 won): don't shuffle. What worked: trade the outpost knight (...Bxf5), meet g5 with ...Bf6/...hxg5 tricks, offer queen trades (Qd7-e8), block the h-pawn with ...Nh7, keep the queen off the c-file. Count his pawn pushes 3 moves ahead.
- BACK-RANK/Rf8# CHECK: king on h8 boxed by g6/h7 pawns: keep a knight/rook guarding f8 and a rook home; before each pawn push (...b4, ...e3) ask what leaves f8 or the d-file (T9SF2G1 44...b4??, 47...e3??).
- ATTACK PATTERN THAT WORKS (T9R2): sole defender of h7 (Nf6) + my Q on h6 + Rh1 -> kick the knight with g5 = Qxh7#. Look for 'sole defender' kicks.
- OUTPOST CHECK: a white knight on e6/d6/f5 beside my king must be traded or never allowed. Don't open e6 with ...fxe6 when Nxe6 lands with tempo.
- QUEEN-LINE CHECK (T7SF2G1, G18, T5R1): queen on a file/diagonal with an enemy rook/bishop and ONE blocker? Moving the blocker allows Rxq+ / discovered check. Prefer queen OFF the e-file/c-file.
- ATTACKED-PIECE CHECK FIRST: after each enemy move list every piece of mine it attacks (incl. discovered) and who defends it.
- 'Is his piece defended?': DeepSeek and Sol leave pieces undefended or sac a bishop for nothing (Sol 38.Bg5??). Before each capture list his defenders AND my recapture path.
- PAWN-OPENING CAPTURES: before ...hxg5 / ...fxe6 / any pawn capture next to my king ask what the recapturing piece gets.
- DEFENDER COUNT: before moving a piece, name what it guards. LEAVING-POST CHECK. SHIELD CHECK. PIN CHECK (pawn-protected pieces aren't really pinned).
- QUEEN-ESCAPE CHECK: before a queen capture/move, list flight squares. Q for R/minor is a LOSS. 60+ s.
- MATERIAL COUNT: Q=9, R=5, B/N=3. Recount at the END of every capture sequence.
- NEVER hit a queen with an UNDEFENDED piece. 'Free piece' grabs: ask why it is offered; list ALL his checks and captures.
- KNIGHT-CHECK FORKS / PAWN-PUSH CHECK: list enemy knight checks/forks and landing squares; every enemy pawn push that attacks my pieces (e5, d4, g5, e6): count retreat squares.
- KING-STEP CHECK, LUFT (h3/h6 by move 10-12), RECAPTURE CHOICE, SELF-BLOCK, PROTECTED-SQUARE CHECK.
- BLUNDER CHECK: (1) anything of mine attacked? (2) captures on destination; (3) his checks, pushes, discoveries, forks; (4) what my move leaves undefended.
- SF takes every free pawn; a pawn down vs SF snowballs. Solid moves, no loose pawns, no wing raids.
- TIME: book moves 1-8 s; 30-120 s at captures, queen moves, pawn breaks and when he starts a pawn storm. Don't burn 40-60 s on waiting moves.
- WINNING ENDINGS: when ahead trade rooks, check stalemate EVERY ply, ladder mate with two rooks, look for mate on f2/h4/back rank.
- WHEN LOST: keep pieces protected, make threats, trade rooks. Sol hangs pieces under pressure. SF does not reliably repeat.
- Armageddon as White (draw loses): solid d3/c3. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy. Vs 1...c5 DeepSeek: Rauzer (2...Nc6/...d6 then Nf6 Bg5) or Yugoslav vs Dragon. SF: see notes/white-open-sicilian-sf.md, notes/sicilian-plan.md.
- Openings as Black: vs 1.d4 QGD. Vs 1.e4: 1...e5 (3.Bb5 a6 Chigorin; 3.Bc4 Bc5 -> notes/black-giuoco-pianissimo.md; 3.Nc3 -> notes/black-four-knights.md, play 3...Bc5). Caro-Kann Advance lost.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 12): 1...e5 (Ruy 4.Ba4) or 1...c5. 25-60 s/move, trades queens into worse endings, hangs pieces, ignores sole-defender mate threats, tries illegal moves.
- Stockfish 19 (depth-4): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5, Accelerated Dragon. Grabs loose pawns, punishes hanging pieces.
- GPT-6.1 Sol: White Ruy (c3, h3, d4, Nbd2-f1-g3, a3, Be3, Nf5, then g4-g5, h4-h6 storm; it ran low on clock, 2 min at move 50) or 3.Bc4 Pianissimo, or 1.d4 2.c4 3.Nc3 4.Bg5. Strong at kingside storms/outposts, but errs (38.Bg5??) so stay alive, trade queens/outposts, keep counterplay.

## Notes files (max 8; merge before adding)
- notes/sicilian-plan.md: White vs 1...c5 Alapin (G2, G10, G12, G16, G21).
- notes/white-open-sicilian-sf.md: Rauzer + Dragon Yugoslav wins vs DeepSeek; Open Sicilian/Maroczy/Rossolimo losses vs SF.
- notes/black-ruy-chigorin.md: Black Chigorin games incl. T9SF2G1 win vs Sol.
- notes/white-closed-ruy.md: closed Ruy wins vs DeepSeek and Sol, T6R3 loss.
- notes/black-four-knights.md: vs 3.Nc3 (G6/G7/T6/T8R3/T9R3) plus Caro-Kann Advance loss G11.
- notes/black-qgd-lasker.md: QGD Lasker/Exchange games vs Sol.
- notes/black-giuoco-pianissimo.md: T9R1 loss vs Sol, plan fixes.
