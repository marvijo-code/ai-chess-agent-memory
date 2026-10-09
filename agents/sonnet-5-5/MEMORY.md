# MEMORY (chess tournament; clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White: vs DeepSeek G1,G9,G14,G15,G19,G20,T5R3 1-0; vs Sol T5 SF2G1, T8R2 1-0, T6R3 0-1 (notes/white-closed-ruy.md).
- Sicilian White vs DeepSeek: Rauzer T8R1, T8SF1G1 1-0; Dragon Yugoslav T9R2 1-0 (notes/white-open-sicilian-sf.md).
- Chigorin as Black: DeepSeek T6R2, T7R2, T7R5.2 1-0; Sol T5R1 1-0, G3 0-1, G4 draw, T7R1 0-1, T9SF2G1 1-0 (notes/black-ruy-chigorin.md).
- vs Sol as Black: QGD G13, G18 1-0; T7SF2G1 0-1 (notes/black-qgd-lasker.md). T9R1 0-1 vs 3.Bc4 (notes/black-giuoco-pianissimo.md).
- vs Sol as White: G5, G8 1-0 (4.d3).
- vs SF as White 1.e4 c5: only losses/draws, latest T9 Final G23 Alapin, back-rank mate in 30 (notes/sicilian-plan.md). vs SF as Black: G6, G11 losses, G7/T6/T8R3 draws (notes/black-four-knights.md).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Trace the path; destination must not be my own piece.
- LUFT/BACK RANK (lost G16 and G23 to Qb1+ ... Qxd1#): as White play h3 by move 10-12 in EVERY game, before Rc1/Qd2. Before each rook trade, queen move, or recapture ask: 'Qb1+/Qa1+, what is my only blocker?' Black Qg6 pinning g2 + ...Bxf3 means h3 was needed BEFORE it.
- OBEY MY OWN NOTES: seven times I wrote 'never X / consider h3 / watch Y' and ignored it. If a note says consider a move, play it that move. If it bans one, calculate the forced line. First check HIS best reply.
- TRADE CHECK (G23 19.Bxd5? Qxd5 put his Q+Bb7 battery on e5/g2): before a trade ask where HIS queen/bishop lands and what it hits. Do not give him a centralized queen.
- VS PAWN STORMS (T9R1 lost, T9SF2G1 won): don't shuffle. Trade the outpost knight (...Bxf5), meet g5 with ...Bf6/...hxg5 tricks, offer queen trades, block the h-pawn with ...Nh7, keep Q off the c-file. Count his pawn pushes 3 moves ahead.
- BACK-RANK/Rf8# with Kh8 under g6/h7: keep a piece guarding f8 and a rook home; before ...b4/...e3 ask what leaves f8 or the d-file.
- ATTACK PATTERN THAT WORKS (T9R2): sole defender of h7 (Nf6) + my Q on h6 + Rh1 -> g5 kick = Qxh7#. Look for 'sole defender' kicks.
- OUTPOST CHECK: a white knight on e6/d6/f5 beside my king must be traded. Don't open e6 with ...fxe6 when Nxe6 lands.
- QUEEN-LINE CHECK: queen on a file/diagonal with an enemy rook/bishop and ONE blocker? Moving the blocker allows Rxq+/discovery. Queen off e-file/c-file/d-file.
- ATTACKED-PIECE CHECK FIRST: list every piece of mine his move attacks (incl. discovered) and who defends it.
- 'Is his piece defended?': DeepSeek and Sol leave pieces undefended. Before each capture list his defenders AND my recapture path. SF never does.
- PAWN-OPENING CAPTURES: before ...hxg5 / ...fxe6 ask what the recapturing piece gets.
- DEFENDER COUNT, LEAVING-POST CHECK, SHIELD CHECK, PIN CHECK (pawn-protected pieces aren't pinned), KING-STEP, RECAPTURE CHOICE, SELF-BLOCK.
- QUEEN-ESCAPE CHECK before a queen capture/move. Q for R/minor is a LOSS.
- MATERIAL COUNT: Q=9, R=5, B/N=3. Recount at the END of every capture sequence.
- NEVER hit a queen with an UNDEFENDED piece. 'Free piece' grabs: ask why it is offered; list ALL his checks.
- KNIGHT-CHECK FORKS / PAWN-PUSH CHECK: count retreat squares for e5, d4, g5, e6 pushes.
- BLUNDER CHECK: (1) anything of mine attacked? (2) captures on destination; (3) his checks (esp. queen checks to my back rank), pushes, discoveries, forks; (4) what my move leaves undefended.
- SF takes every free pawn; a pawn down vs SF snowballs. Solid moves, no loose pawns, no wing raids. SF eval jumps fast once I'm passive (+1 -> +3 in 5 moves).
- TIME: book moves 1-8 s; 30-120 s at captures, queen moves, pawn breaks, luft decisions. G23: spent 4:20 on a plain trade (15.Nxd5) and 2-10 s at the critical moves 19, 24, 27. Spend time where the position changes.
- WINNING ENDINGS: trade rooks when ahead, stalemate check EVERY ply, ladder mate with two rooks.
- WHEN LOST: keep pieces protected, make threats, trade rooks. Sol hangs pieces under pressure. SF does not reliably repeat.
- Armageddon as White (draw loses): solid, but luft first. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy. Vs 1...c5 DeepSeek: Rauzer or Yugoslav. vs SF: Alapin lost 4 times (see notes), include h3 early or try other lines (notes/white-open-sicilian-sf.md).
- Openings as Black: vs 1.d4 QGD. Vs 1.e4: 1...e5 (3.Bb5 a6 Chigorin; 3.Bc4 Bc5 -> notes/black-giuoco-pianissimo.md; 3.Nc3 -> notes/black-four-knights.md, play 3...Bc5). Caro-Kann Advance lost.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 12): 1...e5 (Ruy 4.Ba4) or 1...c5. 25-60 s/move, trades queens into worse endings, hangs pieces, ignores sole-defender mate threats, tries illegal moves.
- Stockfish 19 (depth-4): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5, Accelerated Dragon, vs Alapin 2...d5 3...Qxd5 Nf6 e6 Be7 b6 Bb7 Nc6-b4-d5. Grabs loose pawns, finds back-rank queen checks.
- GPT-6.1 Sol: White Ruy (c3, h3, d4, Nbd2-f1-g3, Nf5, g4-g5, h4-h6 storm) or 3.Bc4 Pianissimo, or 1.d4 2.c4 3.Nc3 4.Bg5. Strong at kingside storms/outposts, but errs (38.Bg5??) so stay alive, trade queens/outposts, keep counterplay.

## Notes files (max 8)
- notes/sicilian-plan.md: White Alapin vs SF (G2, G10, G12, G16, G21, G23) + luft rules.
- notes/white-open-sicilian-sf.md: Rauzer + Dragon Yugoslav wins vs DeepSeek; Open Sicilian/Maroczy/Rossolimo losses vs SF.
- notes/black-ruy-chigorin.md: Black Chigorin games.
- notes/white-closed-ruy.md: closed Ruy wins vs DeepSeek and Sol, T6R3 loss.
- notes/black-four-knights.md: vs 3.Nc3 plus Caro-Kann Advance loss.
- notes/black-qgd-lasker.md: QGD games vs Sol.
- notes/black-giuoco-pianissimo.md: T9R1 loss vs Sol, fixes.
