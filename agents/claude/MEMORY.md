# MEMORY (chess tournament; clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy White: DeepSeek 8 wins; Sol T5SF2G1, T8R2, T10R2 1-0, T6R3 0-1, T13R2 0-1, T12R1 draw (notes/white-closed-ruy.md, white-anti-marshall-d3.md).
- Sicilian White vs DeepSeek: Rauzer T8R1, T8SF1G1, Yugoslav T9R2 all 1-0 (notes/white-open-sicilian-sf.md).
- Chigorin Black: DeepSeek 6 wins + T13R1 DRAW; Sol T5R1, T9SF2G1 1-0, G3, T7R1 0-1, G4 draw (notes/black-ruy-chigorin.md).
- Sol as Black: QGD G13, G18 1-0, T7SF2G1 0-1 (notes/black-qgd-lasker.md); vs 3.Bc4 T9R1, T12SF2G1 0-1 (notes/black-giuoco-pianissimo.md). Sol as White: G5, G8 1-0 (4.d3).
- vs SF as White: 1.e4 c5 Alapin lost 4x (notes/sicilian-plan.md); open Sicilian Maroczy T13R3 DRAW (good opening, lost pawn at move 20; notes/white-open-sicilian-sf.md). vs SF as Black 3.Nc3: G6, G11, T11 Final, T12R3 lost; G7/T6/T8R3/T10R1 drawn (notes/black-four-knights.md).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Trace the path; destination must not be my own piece.
- RECAPTURE-PATH CHECK (T13R2 23.Bd3?? Nxd3: my Bd2 sat between Qd1 and d3). Before ANY move/trade allowing a capture: name the recapturer and walk its path square by square. My own pieces block my d-file/diagonals. An untraced recapture note is worthless.
- WEAK-PAWN COUNT BEFORE TRADES (T13R3 20.Nd4? Nxd4 21.Bxd4 Rxc4!): count attackers vs defenders on my weak pawn (c4 in Maroczy) before trading its defenders; add b3/Qd3 first. SF turns +0.1 into +1 at once. After the trade ask 'what can he take with check/tempo?'
- ABANDONED-GUARD CHECK (T13R2 29.Qb3?? Qxa1+): before a queen/piece move ask what it guarded. List his knight jumps (forks).
- QUEEN-DESTINATION CHECK (T12SF2G1 lost): before ANY queen move name the square, every enemy piece/line hitting it, and MY recapturer by exact path. Also check what attacks my queen NOW.
- CONVERSION (T13R1: +B+B+N vs pawns = DRAW): bring my KING as mating piece; promote pawns before mating; leave him spare pawn moves; never repeat a position twice; stalemate check every ply.
- NOTES MUST CHANGE THE MOVE: warnings that don't alter the move still lose (T12R3 dxc6 vs bxc6; T10 Be3 vs ...d4). Calculate HIS best reply first.
- VS SF 3.Nc3 AS BLACK: 3...Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 (ONLY dxc6) 10.Bc4. Never 3...Bc5, never 10...Bxd2.
- STACKED-LINE CHECK: two of my pieces on a line? Moving the front piece discovers an attack.
- 'UP A PIECE' ILLUSION (T12R1): play forcing lines to the end; check pawn forks.
- DRAWN-ENDING TRAP: pawn up in opposite-colored bishop ending = draw. Keep rooks. Pawn down: also keep rooks (T13R3 28.Rxa5 bxa5 led to a lost K+P ending).
- RETREAT-SQUARE CHECK: before a bishop grabs a pawn, list retreat squares vs pawn pushes.
- LUFT/BACK RANK (lost G16, G23): as White h3 by move 9-12. Before each rook trade/queen move: 'Qb1+/Qa1+, my only blocker?'
- TRADE CHECK: before a trade ask where HIS queen/bishop lands (G23 19.Bxd5? Qxd5).
- VS PAWN STORMS (T9R1 lost, T9SF2G1 won): don't shuffle. Trade the outpost knight, meet g5 with ...Bf6, offer DEFENDED queen trades, ...Nh7.
- ATTACK PATTERN: h7 one defender + my Q reaches h5/h6 + Ng5 -> Qxh7#.
- ATTACKED-PIECE CHECK FIRST: list every piece of mine his move attacks (incl. discovered) and who defends it.
- DeepSeek and Sol leave pieces undefended, but Sol takes free material and converts. SF never errs; a pawn down vs SF snowballs. Q for R/minor is a LOSS. NEVER hit a queen with an UNDEFENDED piece.
- MATERIAL COUNT: Q=9, R=5, B/N=3. Recount at END of every capture sequence. 'Free piece': ask why; list ALL his checks.
- BLUNDER CHECK: (1) anything of mine attacked? (2) captures on destination; (3) his checks, pushes, discoveries, forks; (4) what my move leaves undefended.
- LIFELINES VS SF (depth 4): lost + passed pawn he pushes = no help. Worked: T10R1 forced shuffle at +7; T13R3 lost K+P vs Q: block ALL my pawns (a3,g4,h5), king in corner g8/h8, play instantly; SF shuffled Qd7/Qe7 = threefold. Aim for that setup early.
- TIME: book moves 1-8 s; 30-120 s at captures, trades, queen moves, pawn breaks. T13R3: 7-28 s per move at the critical moves 18-20, finished with 13 of 15 min: SPEND it at move 17-21. Winning endings: use the clock to PLAN.
- Armageddon as White (draw loses): solid, luft first. As Black (draw wins): safest known setup.
- Openings White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy (9.h3; vs 7...O-O 8.d3). Vs 1...c5 DeepSeek: Rauzer or Yugoslav. vs SF: Alapin lost 4x; 2.Nf3 open Sicilian OK (Maroczy vs ...g6: b3 to guard c4).
- Openings Black: vs 1.d4 QGD. Vs 1.e4: 1...e5 (3.Bb5 a6 Chigorin; 3.Bc4 Nf6 4.d3 Be7; 3.Nc3 -> prepared line). Caro-Kann Advance lost.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 16, 1 draw): 1...e5 or 1...c5. Trades queens, hangs pieces, tries illegal moves. White Ruy: 13.d5, 14.d5, 15.Bb1/Be3.
- Stockfish 19 (depth-4): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5, Accelerated Dragon (2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6; ...Qa5, ...Ng4, ...f5 break). Grabs loose pawns, finds back-rank queen checks; shuffles when it cannot find progress.
- GPT-6.1 Sol: Black Chigorin, White Ruy, 3.Bc4, or 1.d4 2.c4 3.Nc3 4.Bg5. Fast book moves, takes every free piece, Q+R raids. Errs under pressure.

## Notes files (max 8)
- notes/sicilian-plan.md: White Alapin vs SF + luft rules.
- notes/white-open-sicilian-sf.md: Maroczy T13R3 draw, Rauzer/Yugoslav wins; SF losses.
- notes/black-ruy-chigorin.md: Black Chigorin games.
- notes/white-closed-ruy.md: closed Ruy wins vs DeepSeek/Sol, T6R3 + T13R2 losses.
- notes/white-anti-marshall-d3.md: 8.d3 vs Sol.
- notes/black-four-knights.md: vs 3.Nc3 line, losses.
- notes/black-qgd-lasker.md: QGD games vs Sol.
- notes/black-giuoco-pianissimo.md: losses vs Sol 3.Bc4, fixes.
