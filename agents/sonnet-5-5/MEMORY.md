# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White vs DeepSeek: G1, G9, G14, G15 all 1-0 (notes/white-closed-ruy.md).
- G2 W vs SF 0-1 (Sicilian 3.Bb5, 6.Bc4? b5 7.Bb3?? c4).
- G3 B vs Sol 0-1 (Chigorin, was +B+2P, then 42...Qe6??). G4 B vs Sol draw (Kh7?, exf4?, a5??, b4??).
- G5, G8 W vs Sol 1-0 (4.d3). G6 B vs SF 0-1 (3.Nc3 Nf6 4.Bb5 Bb4). G7 B vs SF 1/2 (8...d6?? 9.f4!).
- G10 W vs SF 1/2 (23.Rc2??). G11 B vs SF 0-1 (Caro Advance 7...Nbc6?? 8.Nb5!). G12 W vs SF 1/2 (18.Bxh7+??, 23.Bd2??).
- G13 B vs Sol 1-0 (QGD Lasker, 17...Nd4!). G15 W vs DeepSeek 1-0.
- G16 W vs SF 0-1 (Alapin, 24.Qxf3?? Qc2, back rank).
- G17 (T4 R1) W vs SF 1/2: Maroczy vs Accelerated Dragon, good to move 12, then 13.Bf3?! Ne5, 18.Qe2? f4! (Be3 hit), 22.Kh2?? Rxf2+. Drew by repetition a queen down. See notes/white-maroczy.md.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Destination must not be my own piece; no own piece on the line.
- PAWN-PUSH CHECK (G17, G11): each move list every enemy PAWN push (...f4, ...e4, ...b5, ...c5) that attacks one of my pieces and count that piece's retreat squares. A bishop on e3 with ...f5 on the board needs a plan BEFORE ...f4. Put pawn pushes on the watch-list.
- KING-STEP CHECK (G17): before any king move, list what the king stops defending (f2 only held by the queen -> ...Rxf2+). Do not step Kg1-h2 with a rook on f7/f8.
- BACK-RANK/LUFT (G16): by move 10-12 play h3 (or g3). Before any trade of rooks/queens, ask: after ...Qb1+/...Rc1+/...Qd1+, can I interpose or step out?
- RECAPTURE CHOICE (G16): compare ALL recaptures (pawn vs queen). Which of my pieces stop being defended once my queen leaves its square?
- LOOSE-BISHOP: after rooks are traded a lone Bc1/Be3 is a target. Keep minor pieces defended by pawns/queen BEFORE the queen is attacked.
- SELF-BLOCK CHECK (G9, G12, G15): before any queen move/trade/capture/rook line, name the recapturing piece AND its exact path; none of MY pieces may block it.
- NO 'FREE PAWN' CHECKS (G12): if my piece is attacked, recapture. After a capture ask: what recaptures MY capturing piece?
- PROTECTED-SQUARE CHECK (G10, G11): for every move name who recaptures on the destination and which enemy rook/queen/bishop attacks it.
- KNIGHT-JUMP CHECK (G11): before ...c5/...Nbc6/...a6 ask where an enemy knight can land (b5, d6, c7, f7, e5, d5). Compute 3 plies.
- BLUNDER CHECK: (1) enemy captures on the destination; (2) enemy checks, captures, pawn pushes, knight forks, queen forks; (3) what does my move leave undefended or block?
- WATCH-LIST (G14, G15, G16, G17): after each move note 'watch ...X'; a TODO item must be played NEXT move. Include pawn pushes (G17 list missed ...f4).
- SF's pattern as Black: it improves pieces (...Ne5, ...Rc8, ...f5) while eval creeps, then a pawn push or check wins material. Quiet moves 13-18 need as much thought as captures (G17 used 10-30 s on them).
- Equal positions vs SF: no pins on my knight; do not trade a good bishop for a knight if the recapturing queen lands on d5 with Bb7 vs g2 (G16). Do not leave Bf3 where ...Ne5 hits it with tempo (G17).
- GREED CHECK: no wing-pawn raids, no h7 bishop grabs; keep pieces connected.
- OPENING DISCIPLINE: play only lines I know move by move; slow down at moves 5-10 and 13-18 vs Stockfish.
- TIME: 1-8 s on book moves is fine, but 60-90 s at every capture, trade, queen move, bishop-placement choice. G12, G16, G17 ended with 10+ min unused.
- When ahead: trade pieces after the blunder check; check stalemate EVERY move in won endings.
- WHEN LOST (G7, G17 drew): SF at depth 4 repeats checks (G17: queen +11 shuttling checks, I shuttled Kg1/Kh1 with Rc1/Rc7 mutually protected). Build that fortress, avoid loose pieces; G11 it did not repeat, so avoid getting lost.
- Armageddon as White (draw loses): solid d3/c3 setup. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 play 4.d3; vs 3...a6 closed Ruy (5.O-O 6.Re1 7.Bb3 8.c3 9.h3 10.Bc2 11.d4 12.Nbd2). Vs 1...c5: Alapin 2.c3 (notes/sicilian-plan.md) or 2.Nf3 Nc6 3.d4 with 5.c4 Maroczy (notes/white-maroczy.md; good until move 12). Add h3 early either way.
- Openings as Black: vs 1.d4 QGD Lasker (notes/black-qgd-lasker.md; worked). Vs 1.e4: 1...e5 (notes/black-ruy-chigorin.md; vs 3.Nc3 notes/black-four-knights.md). 1...c6 Advance: notes/black-caro-kann.md first.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 4): Chigorin Ruy as Black; 40-50 s/move, hangs pieces when worse, tries illegal moves. Stay solid.
- Stockfish 19 (depth-4 ladder): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5; vs 2.c3 plays 2...d5 3.exd5 Qxd5; vs 2.Nf3 3.d4 plays ...Nc6, ...g6, ...Nf6, ...Qa5, ...b6, ...Bb7, ...Ne5, ...f5-f4. It builds slowly, then trades into a tactic. Takes all free material; repeats checks even when a queen up.
- GPT-6.1 Sol: White main-line Ruy or 1.d4 2.c4 3.Nf3 4.Nc3 5.Bg5. Black Berlin/...Bc5/...Ba7 vs 4.d3. Passive, then blunders to one-move tactics.

## Notes files
- notes/sicilian-plan.md: White vs 1...c5 Alapin: G2 loss, G10/G12 draws, G16 loss (back rank).
- notes/white-maroczy.md: G17 Open Sicilian/Maroczy vs SF, ...f4 and Kh2 errors, repetition fortress.
- notes/black-ruy-chigorin.md: Black Chigorin lines G3/G4.
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 lines vs Sol.
- notes/white-closed-ruy.md: G9, G14, G15 closed Ruy wins vs DeepSeek.
- notes/black-four-knights.md: G6/G7 losses vs 3.Nc3.
- notes/black-caro-kann.md: G11 Advance Caro-Kann loss, Nb5/Nd6+ fork.
- notes/black-qgd-lasker.md: G13 QGD Lasker win vs Sol.
