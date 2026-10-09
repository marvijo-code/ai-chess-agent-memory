# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White: vs DeepSeek G1, G9, G14, G15, G19, G20, T5R3 all 1-0; vs Sol T5 SF2G1 1-0 (notes/white-closed-ruy.md).
- Closed Ruy as Black (Chigorin): T6R2 vs DeepSeek 1-0 (19.Ng3?? Nb3! fork); vs Sol T5R1 1-0, G3 0-1, G4 draw (notes/black-ruy-chigorin.md).
- vs Sol: G5, G8 W 1-0 (4.d3); G13, G18 B 1-0 (QGD).
- vs SF as White: G2 0-1 (Sicilian 3.Bb5); G10, G12 draws; G16 0-1 (back rank); G17 draw (Maroczy); G21 0-1 (Alapin 7.Nxd4? Qxg2!); T6R1 0-1 (Maroczy, 16.Nd5? Bxb2).
- vs SF as Black: G6 0-1 (3.Nc3 Nf6 4.Bb5 Bb4), G7 draw (8...d6?? 9.f4!), G11 0-1 (Caro Advance 7...Nbc6?? 8.Nb5!).

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Trace the path; destination must not be my own piece.
- SHIELD CHECK (T6R1): before moving a piece ask 'is it BLOCKING a line onto one of my pieces?' Nc3 shielded b2 from Bg7. Same for Bf1 guarding g2, Bd3 blocking Rd1.
- ATTACKED-PIECE CHECK (T5R1): FIRST list every one of my pieces the enemy's last move attacks, incl. discovered attacks. If my queen is attacked, move/guard/trade it. Keep queen off the c-file facing Rc1.
- LEAVING-POST CHECK (G21, T6R1): what does the moved piece stop guarding or unblock?
- NEVER hit a queen with an UNDEFENDED piece (G21). Name the attacker's defender.
- X-RAY/DISCOVERY CHECK (G18): before ANY capture list enemy discovered checks and unmasked lines onto my queen.
- 'Free piece' grabs (G12, G18, T5R1): ask why it is offered; list ALL his checks and captures first.
- KNIGHT-CHECK FORKS (T5R1 51.Ne7+): list enemy knight checks and forks before a grab. Use them myself: a knight on b3/c2 forking R+B/Q+R when no piece covers the square (T6R2).
- PAWN-PUSH CHECK (G17, G11): list every enemy pawn push that attacks my pieces; count retreat squares.
- KING-STEP CHECK (G17): before a king move list what the king stops defending.
- BACK-RANK/LUFT (G16): by move 10-12 play h3. Before any trade ask: after ...Qb1+/...Rc1+, can I interpose or step out?
- RECAPTURE CHOICE (G16, G21): compare ALL recaptures; which pieces stop being defended?
- SELF-BLOCK CHECK (G9, G12, G15, G19): before any queen move/trade/mate try, name the recapturer AND its path; none of MY pieces may block.
- PROTECTED-SQUARE CHECK (G10, G11, G21): for every move name who recaptures on the destination and which enemy Q/R/B attacks it.
- KNIGHT-JUMP CHECK (G11): before ...c5/...Nbc6/...a6 ask where an enemy knight can land (b5, d6, c7, f7, e5, d5).
- BLUNDER CHECK: (1) is anything of mine attacked now? (2) enemy captures on the destination; (3) enemy checks, pushes, discoveries, forks; (4) what does my move leave undefended or unblock?
- WATCH-LIST: a watch item must CHANGE the move; do the check BEFORE the move.
- SF as Black: improves pieces, then a pawn push, check or queen raid wins material; takes every free pawn. A pawn down vs SF snowballs. In equal positions prefer solid, loose-pawn-free moves; no 'active' knight jumps with loose pawns behind.
- Equal positions vs SF: no pins on my knight; do not leave Bf3 where ...Ne5 hits it with tempo.
- GREED CHECK: no wing-pawn raids, no h7 bishop grabs; keep pieces connected.
- OPENING DISCIPLINE: play only lines I know move by move; slow down at moves 5-10, 13-18, 22-25. 30+ s on every capture/recapture and on any move that relocates a knight/bishop in a bind. Vs SF use real time; vs DeepSeek/Sol fast book moves are fine.
- TIME: 1-8 s on book moves, 30-60 s at every capture, trade, queen move.
- WINNING ENDINGS (SF2G1, T6R2): trade rooks when ahead, never capture a pawn defended by king/pawn, push the passed pawn, check stalemate EVERY move; cut ranks with the rook, bishops cover flight squares, mate with R+2B.
- WHEN LOST: keep pieces protected, make threats. Sol hangs pieces under pressure. SF does not reliably repeat. Avoid getting lost.
- Armageddon as White (draw loses): solid d3/c3 setup. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 play 4.d3; vs 3...a6 closed Ruy (5.O-O 6.Re1 7.Bb3 8.c3 9.h3). Vs 1...c5: SF plays the Accelerated Dragon vs 2.Nf3 (Maroczy lost/drew twice, notes/white-maroczy.md); Alapin 2.c3 lost too (notes/sicilian-plan.md). Untested vs SF: 3.d4 cxd4 4.Nxd4 g6 5.Nc3 (no c4). Add h3 early.
- Openings as Black: vs 1.d4 QGD (notes/black-qgd-lasker.md). Vs 1.e4: 1...e5 (Ruy: notes/black-ruy-chigorin.md; vs 3.Nc3 notes/black-four-knights.md). 1...c6 Advance: notes/black-caro-kann.md first.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 8): as White Ruy 4.Ba4 main line, 14.d5, then drifts (Qe2, Nf1, Ng3?? allowing ...Nb3 fork); as Black Chigorin or Breyer. 35-60 s/move, hangs pieces when worse, tries illegal moves, burns clock (1 min left at end).
- Stockfish 19 (depth-4): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5; vs 2.c3 plays 2...d5 3.exd5 Qxd5; vs 2.Nf3 3.d4 plays ...Nc6, ...g6, ...Nf6, ...Qa5, ...Qd8, ...d6, ...b6, ...Bg7, ...Ng4, ...O-O, ...Be6, ...Rc8, then Bxb2 / Ne5xc4 the moment a pawn is loose. Takes all free material.
- GPT-6.1 Sol: White main-line Ruy or 1.d4 2.c4 with Bh7+ tricks. Black: Berlin/...Bc5/...Ba7 vs 4.d3, Chigorin vs the closed Ruy. Passive, then blunders to one-move tactics.

## Notes files
- notes/sicilian-plan.md: White vs 1...c5 Alapin (G2, G10, G12, G16, G21).
- notes/white-maroczy.md: G17 + T6R1 Maroczy vs SF Dragon; b2 shield, ...f4, Kh2 errors.
- notes/black-ruy-chigorin.md: Black Chigorin G3/G4/T5R1/T6R2 (Qc7 vs Rc1 trap; ...Nb3 fork win).
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 vs Sol.
- notes/white-closed-ruy.md: closed Ruy wins vs DeepSeek and Sol.
- notes/black-four-knights.md: G6/G7 losses vs 3.Nc3.
- notes/black-caro-kann.md: G11 Advance Caro-Kann loss, Nb5/Nd6+.
- notes/black-qgd-lasker.md: G13 Lasker win, G18 Exchange QGD vs Sol.
