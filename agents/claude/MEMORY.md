# MEMORY (chess tournament; clocks 600+10, 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy White: DeepSeek 8 W; Sol 3 W, 2 L, 1 D (notes/white-closed-ruy.md, white-anti-marshall-d3.md).
- Sicilian White vs DeepSeek: 4 W (notes/white-open-sicilian-sf.md).
- Chigorin Black: DeepSeek 7 W 1 D; Sol 2 W, 2 L, 1 D (notes/black-ruy-chigorin.md).
- Sol as Black: QGD 3 W 1 L (black-qgd-lasker.md); vs 3.Bc4 2 L (black-giuoco-pianissimo.md).
- vs SF as White: Alapin lost 4x (sicilian-plan.md); Maroczy drew T13R3 and T14R2, both from lost positions (white-open-sicilian-sf.md). vs SF as Black 3.Nc3: 5 L, 4 D (black-four-knights.md).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Trace the path; destination must not be my own piece.
- MAROCZY VS SF (T14R2: +0.1 at move 12, lost by move 21): vs 11...Ng4 play 12.Bxg4 Bxg4 13.f3 (T13R3), NOT 12.h3?! Nxe3 (my queen lands on e3 facing Bg7-h6). With Qe3 no Nd5: ...e6 hits it, Nf4 is pinned by ...Bh6; Nc3 was the retreat. Before an outpost ask 'where does the piece go after ...e6?' and list his bishop pins on my queen's line.
- RECAPTURE-PATH CHECK (T13R2 23.Bd3?? Nxd3: my Bd2 sat between Qd1 and d3). Before ANY move/trade allowing a capture, name the recapturer, walk its path square by square, and ask where HIS queen/bishop lands.
- WEAK-PAWN COUNT (T13R3 20.Nd4? Rxc4!; T13SF1G1 21...Rd7?? f7): count attackers vs defenders on my weak pawn BEFORE each move or trade.
- PASSIVE-DRIFT vs SF (T13SF1G1): after a queen trade I shuffled and eval went +0.3 -> +3 in 6 moves. Before each rook/bishop trade: whose rook gets the open file / 7th rank?
- BOOK DEVIATION LOSES vs SF (10...Qf6 T13SF1G1, 9...bxc6 T12R3, 10...Bxd2 T11F, 12.h3 T14R2). Follow the notes line; at the first branch calculate HIS best reply.
- ABANDONED-GUARD CHECK (T13R2 29.Qb3?? Qxa1+): before a queen/piece move ask what it guarded. List his knight jumps.
- QUEEN-DESTINATION CHECK (T12SF2G1): before ANY queen move name the square, every enemy piece/line hitting it, and MY recapturer by exact path. Enemy pawns block my rook lines. Before a rook trade check his queen backs the file (T14R2 35.Re3?? Rxe3).
- SAC CHECK: before a knight sac, calculate his BEST reply. Equal + solid beats an unsound sac vs SF/Sol.
- CONVERSION (T13R1: +B+B+N vs pawns = DRAW; T14R1 up Q: trade pieces, rook to open file, mate in 33): bring my KING, win pawns with rook on 7th, never repeat, stalemate check every ply.
- NOTES MUST CHANGE THE MOVE: warnings that don't alter the move still lose. Calculate HIS best reply first; write pin/fork checks BEFORE the move, not after.
- VS SF 3.Nc3 AS BLACK: 3...Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 (ONLY dxc6) 10.Bc4. Never 3...Bc5, never 10...Bxd2, avoid 10...Qf6.
- STACKED-LINE CHECK: two of my pieces on a line? Moving the front piece discovers an attack.
- DRAWN-ENDING TRAP: pawn up in opposite-colored bishop ending = draw. Keep rooks. Pawn down: keep rooks too.
- RETREAT-SQUARE CHECK: before a bishop grabs a pawn, list retreat squares vs pawn pushes.
- LUFT/BACK RANK (G16, G23): h3 by move 9-12 BUT not at the cost of Be3 (T14R2). With K on b1 and no flight square play Kc1 first. Before each rook trade: 'Qb1+/Qa1+, my only blocker?'
- VS PAWN STORMS (T9R1 lost, T9SF2G1 won): trade the outpost knight, meet g5 with ...Bf6, offer DEFENDED queen trades, ...Nh7.
- ATTACK PATTERN: h7 one defender + my Q reaches h5/h6 + Ng5 -> Qxh7#.
- ATTACKED-PIECE CHECK FIRST: list every piece of mine his move attacks (incl. discovered) and who defends it.
- SF never errs; a pawn down vs SF snowballs. Q for R/minor is a LOSS. NEVER hit a queen with an UNDEFENDED piece. DeepSeek/Sol hang pieces; Sol converts free material.
- MATERIAL COUNT: Q=9, R=5, B/N=3. Recount at END of every capture sequence. 'Free piece': ask why; list ALL his checks.
- LIFELINES VS SF (depth 4): worked T10R1 (+7 shuffle), T13R3 (block pawns, king in corner), T14R2 (at +10: Qd4+Ne2, K e1/f2, defended blockers; SF repeated Qb1+/Qf5+). Play quickly, keep everything defended.
- TIME: book moves 1-8 s; 30-120 s at captures, trades, queen moves, pawn breaks. Vs SF SPEND the clock at moves 10-21 (T14R2 spent 5-25 s there, 40-65 s after the damage). DeepSeek burns 30-60 s a move and can flag.
- Armageddon as White (draw loses): solid, luft first. As Black (draw wins): safest known setup.
- Openings White: vs 1...e5 3...Nf6 4.d3; vs 3...a6 closed Ruy (9.h3; vs 7...O-O 8.d3). Vs 1...c5 DeepSeek: Rauzer or Yugoslav. vs SF: Alapin lost 4x; 2.Nf3 open Sicilian + Maroczy (12.Bxg4!).
- Openings Black: vs 1.d4 QGD. Vs 1.e4: 1...e5 (3.Bb5 a6 Chigorin; 3.Bc4 Nf6 4.d3 Be7; 3.Nc3 prepared line). Caro-Kann Advance lost.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 18, 1 draw): 1...e5 or 1...c5; as White plays Chigorin Ruy. Trades queens, hangs pieces, tries illegal moves, flags when lost.
- Stockfish 19 (depth-4): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5; Bc4, Bh6, Re1/Rad1, Re7, Bxf7+ in the Four Knights. Black vs 1.e4: 1...c5 2...Nc6 g6 (Maroczy: Qa5, Qd8, Ng4, Bh6 pin, ...e6-e5). Grabs loose pawns, finds back-rank queen checks; shuffles/repeats checks when it cannot progress.
- GPT-6.1 Sol: Black Chigorin, White Ruy, 3.Bc4, or 1.d4 2.c4 3.Nc3 4.Bg5. Fast book moves, takes every free piece, Q+R raids. Errs under pressure.

## Notes files (max 8, all used)
- notes/sicilian-plan.md: White Alapin vs SF + luft rules.
- notes/white-open-sicilian-sf.md: Maroczy vs SF (T13R3, T14R2), Yugoslav/Soltis win, Rauzer, SF losses.
- notes/black-ruy-chigorin.md: Black Chigorin games incl. T14R1 win.
- notes/white-closed-ruy.md: closed Ruy wins, T6R3 + T13R2 losses.
- notes/white-anti-marshall-d3.md: 8.d3 vs Sol.
- notes/black-four-knights.md: vs 3.Nc3 line, 5 losses incl. T13SF1G1.
- notes/black-qgd-lasker.md: QGD games vs Sol.
- notes/black-giuoco-pianissimo.md: losses vs Sol 3.Bc4, fixes.
