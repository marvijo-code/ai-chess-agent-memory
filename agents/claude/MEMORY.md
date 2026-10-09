# MEMORY (chess tournament; clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White: vs DeepSeek G1,G9,G14,G15,G19,G20,T5R3,T10R3 1-0; vs Sol T5 SF2G1, T8R2, T10R2 1-0, T6R3 0-1, T12R1 draw (notes/white-closed-ruy.md, notes/white-anti-marshall-d3.md).
- Sicilian White vs DeepSeek: Rauzer T8R1, T8SF1G1 1-0; Dragon Yugoslav T9R2 1-0 (notes/white-open-sicilian-sf.md).
- Chigorin as Black: DeepSeek T6R2, T7R2, T7R5.2, T11R2, T12R2 1-0; Sol T5R1 1-0, G3 0-1, G4 draw, T7R1 0-1, T9SF2G1 1-0 (notes/black-ruy-chigorin.md).
- T12R2 (mate 30, used 2 of 15 min): 14.Nf1 Bb7 15.Ng3 Rfe8 16.d5 Nb4 17.Bb1 a5 18.a3 Na6! 19.Be3 Nc5 20.Bxc5 dxc5 21.d6? Bxd6 22.Qxd6?? Qxd6 23.Nd2 Qxd2, then Qxe1, Qxf1+, Rd1+, Qf2#. Bb1 blocked Ra1, so Re1/Nf1 were loose.
- vs Sol as Black: QGD G13, G18 1-0; T7SF2G1 0-1 (notes/black-qgd-lasker.md). T9R1 0-1 vs 3.Bc4 (notes/black-giuoco-pianissimo.md).
- vs Sol as White: G5, G8 1-0 (4.d3).
- vs SF as White 1.e4 c5: only losses/draws, latest T9 Final G23 Alapin, back-rank mate (notes/sicilian-plan.md). vs SF as Black 1.e4 e5 2.Nf3 Nc6 3.Nc3: G6, G11, T11 Final losses, G7/T6/T8R3/T10R1 draws (notes/black-four-knights.md).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Trace the path; destination must not be my own piece.
- VS SF 3.Nc3 AS BLACK: never 3...Bc5. Play 3...Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! and at move 10 do NOT take Bxd2 (notes/black-four-knights.md).
- 'UP A PIECE' ILLUSION (T12R1): 'Bxh6 wins a piece' but ...Nxe4 dxe4 d3 forked Q+B. Play the whole forcing line to the end. Check every enemy pawn push that forks (d3, d4, e4).
- DRAWN-ENDING TRAP (T12R1): a pawn up in an opposite-colored bishop ending is a draw. Don't trade rooks into it; keep rooks, make a plan (b5/g4 break, king to c5), don't shuffle into threefold. Use the clock when ahead.
- CHECK MY OWN WRITTEN FIXES: a note said '8...O-O 9.f4 Bd6' and it lost to 10.e5. Calculate his best reply before copying a note move.
- RETREAT-SQUARE CHECK: before a bishop grabs a pawn on e5/d4, list its retreat squares vs f4/c3/e5 pushes.
- LUFT/BACK RANK (lost G16, G23): as White play h3 by move 9-12 in EVERY game, before Rc1/Qd2. Before each rook trade or queen move ask: 'Qb1+/Qa1+, what is my only blocker?'
- OBEY MY OWN NOTES: if a note says consider a move, play it. If it bans one, calculate the forced line. First check HIS best reply.
- TRADE CHECK (G23 19.Bxd5? Qxd5): before a trade ask where HIS queen/bishop lands and what it hits.
- VS PAWN STORMS (T9R1 lost, T9SF2G1 won): don't shuffle. Trade the outpost knight (e6/d6/f5), meet g5 with ...Bf6, offer queen trades, ...Nh7, keep Q off the c-file.
- BACK-RANK/Rf8# with Kh8 under g6/h7: keep a piece guarding f8 and a rook home.
- ATTACK PATTERN (T9R2, T10R3): h7 has one defender + my Q reaches h5/h6 + Ng5 (Nf5 covering g7) -> Qxh7#.
- QUEEN-LINE CHECK: queen on a file/diagonal with enemy rook/bishop and ONE blocker? Moving the blocker allows discovery. Queen off e/c/d-file.
- ATTACKED-PIECE CHECK FIRST: list every piece of mine his move attacks (incl. discovered) and who defends it.
- 'Is his piece defended?': DeepSeek and Sol leave pieces undefended (T12R2: Qxd6??, Nd2??, Re1, Nf1). Before each capture list his defenders AND my recapture path. SF never does.
- DEFENDER COUNT, LEAVING-POST, SHIELD, PIN (pawn-protected pieces aren't pinned), KING-STEP, RECAPTURE CHOICE, SELF-BLOCK.
- QUEEN-ESCAPE CHECK before a queen capture/move. Q for R/minor is a LOSS. NEVER hit a queen with an UNDEFENDED piece.
- MATERIAL COUNT: Q=9, R=5, B/N=3. Recount at the END of every capture sequence. 'Free piece': ask why it is offered; list ALL his checks.
- BLUNDER CHECK: (1) anything of mine attacked? (2) captures on destination; (3) his checks, pushes, discoveries, forks; (4) what my move leaves undefended.
- SF takes every free pawn; a pawn down vs SF snowballs. Solid moves, no loose pawns.
- REPETITION LIFELINE vs SF: when lost, find a forced queen/piece shuffle (T10R1 drew at +7). Keep pieces protected.
- TIME: book moves 1-8 s; 30-120 s at captures, queen moves, pawn breaks, luft decisions, moves 6-10 of a risky opening. Right questions beat more minutes.
- WINNING ENDINGS (up material): trade down, stalemate check EVERY ply, ladder mate with two rooks, keep back rank safe.
- Armageddon as White (draw loses): solid, but luft first. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy (9.h3; vs 7...O-O 8.d3). Vs 1...c5 DeepSeek: Rauzer or Yugoslav. vs SF: Alapin lost 4 times, include h3 early or try other lines.
- Openings as Black: vs 1.d4 QGD. Vs 1.e4: 1...e5 (3.Bb5 a6 Chigorin; 3.Bc4 Bc5 -> notes/black-giuoco-pianissimo.md; 3.Nc3 -> prepared 3...Nf6 line). Caro-Kann Advance lost.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 14): 1...e5 (Ruy, Chigorin 9...Na5) or 1...c5. 25-60 s/move, trades queens into worse endings, hangs pieces, ignores sole-defender mate threats, tries illegal moves.
- Stockfish 19 (depth-4): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5, Accelerated Dragon, vs Alapin 2...d5 3...Qxd5. Grabs loose pawns, finds back-rank queen checks, repeats positions when ahead.
- GPT-6.1 Sol: White Ruy (c3, h3, d4, Nf1-g3, Nf5, g4-g5 storm) or 3.Bc4, or 1.d4 2.c4 3.Nc3 4.Bg5. As Black vs 8.d3: ...d6, ...Bb7, ...Re8, ...Bf8, ...d5; defends opposite-bishop endings by blockade. Strong at storms/outposts, errs under pressure: stay alive, trade queens/outposts.

## Notes files (max 8)
- notes/sicilian-plan.md: White Alapin vs SF + luft rules.
- notes/white-open-sicilian-sf.md: Rauzer/Yugoslav wins vs DeepSeek; losses vs SF.
- notes/black-ruy-chigorin.md: Black Chigorin games.
- notes/white-closed-ruy.md: closed Ruy wins vs DeepSeek/Sol, T6R3 loss.
- notes/white-anti-marshall-d3.md: 8.d3 vs Sol (T10R2 win, T12R1 draw).
- notes/black-four-knights.md: vs 3.Nc3 prepared line, losses.
- notes/black-qgd-lasker.md: QGD games vs Sol.
- notes/black-giuoco-pianissimo.md: T9R1 loss vs Sol, fixes.
