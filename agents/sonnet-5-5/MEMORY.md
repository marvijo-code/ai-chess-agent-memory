# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White vs DeepSeek: G1, G9, G14, G15 all 1-0 (notes/white-closed-ruy.md).
- G2 W vs SF 0-1 (Sicilian 3.Bb5, 6.Bc4? b5 7.Bb3?? c4).
- G3 B vs Sol 0-1 (Chigorin, was +B+2P, then 42...Qe6??). G4 B vs Sol draw (Kh7?, exf4?, a5??, b4??).
- G5, G8 W vs Sol 1-0 (4.d3). G6 B vs SF 0-1 (3.Nc3 Nf6 4.Bb5 Bb4). G7 B vs SF 1/2 (8...d6?? 9.f4!).
- G10 W vs SF 1/2 (23.Rc2??). G11 B vs SF 0-1 (Caro Advance 7...Nbc6?? 8.Nb5!). G12 W vs SF 1/2 (18.Bxh7+??, 23.Bd2??).
- G13 B vs Sol 1-0 (QGD Lasker, 17...Nd4!). G15 W vs DeepSeek 1-0.
- G16 (T3 Final) W vs SF 0-1 in 27: Alapin, 18.Bxd5 Qxd5 pinned Nf3, 24.Qxf3?? Qc2, 25.Be3?? Qb1+ back-rank mate. See notes/sicilian-plan.md.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Destination must not be my own piece; no own piece on the line.
- BACK-RANK/LUFT (G16): by move 10-12 play h3 (or g3) in every game where I castled. Before any trade of rooks/queens, ask: after ...Qb1+/...Rc1+/...Qd1+, can I interpose or step out? Without luft, my queen is tied to d1/e1 and loses.
- RECAPTURE CHOICE (G16): when a piece is taken, compare ALL recaptures (pawn vs queen). Qxf3 left Bc1 and b2 loose to ...Qc2; gxf3 kept Qe3 guarding c1. Ask: which of my pieces stop being defended once my queen leaves its square?
- LOOSE-BISHOP: after rooks are traded a lone Bc1/Be3 is a target. Keep minor pieces defended by pawns/queen BEFORE the queen is attacked.
- SELF-BLOCK CHECK (G9, G12, G15): before any queen move/trade/capture/rook line, name the recapturing piece AND its exact path; none of MY pieces may block it.
- NO 'FREE PAWN' CHECKS (G12): if my piece is attacked, recapture. After a capture ask: what recaptures MY capturing piece?
- PROTECTED-SQUARE CHECK (G10, G11): for every move name who recaptures on the destination and which enemy rook/queen/bishop attacks it.
- KNIGHT-JUMP CHECK (G11): before ...c5/...Nbc6/...a6 ask where an enemy knight can land (b5, d6, c7, f7, e5, d5). Compute 3 plies.
- BLUNDER CHECK: (1) enemy captures on the destination; (2) enemy checks, captures, pawn pushes, knight forks, queen forks (...Qc2 hitting two pieces); (3) what does my move leave undefended or block?
- LOOSE-PIECE SCAN (G13 win): each move look for undefended pieces on files/diagonals, mine too.
- WRITE-A-WATCH-LIST (G14, G15): after each move note 'watch ...X'. In G16 the list said 'play h3 soon' and I never did: a watch-list item that is a TODO must be played NEXT move.
- Equal positions vs Stockfish: no pins on my knight. Do not trade a good bishop for a knight if the recapturing queen then lands on d5 with Bb7 vs g2 (G16 18.Bxd5). Eval turned bad right after that.
- GREED CHECK: no wing-pawn raids, no h7 bishop grabs; keep pieces connected.
- RETREAT-SQUARE CHECK: which of my pieces can be hit by a pawn push and where would it go?
- PIN/FILE CHECK: no knight pinned to the queen/g2; no pieces on open files vs rooks. KING SAFETY: keep luft.
- OPENING DISCIPLINE: play only lines I know move by move; slow down at moves 5-10 vs Stockfish.
- TIME: 1-8 s on book moves is fine, but 60-90 s at every capture, trade, queen move. G12 and G16 lost with 15 min unused (G16: 26 min of total game used under 1 min per move).
- When ahead: trade pieces after the blunder check; check stalemate EVERY move in won endings.
- WHEN LOST: Stockfish repeated in 3 of 5 lost games only. Play safe king moves; keep rooks connected.
- Armageddon as White (draw loses): solid d3/c3 setup. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 play 4.d3; vs 3...a6 closed Ruy (5.O-O 6.Re1 7.Bb3 8.c3 9.h3 10.Bc2 11.d4 12.Nbd2). Vs 1...c5: 2.c3 is equal until move ~17 but SF punishes passivity; add h3 early (notes/sicilian-plan.md).
- Openings as Black: vs 1.d4 QGD Lasker (notes/black-qgd-lasker.md; worked). Vs 1.e4: 1...e5 (notes/black-ruy-chigorin.md; vs 3.Nc3 notes/black-four-knights.md). 1...c6 Advance: notes/black-caro-kann.md first.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 4): Chigorin Ruy as Black; 40-50 s/move, hangs pieces when worse, tries illegal moves. Stay solid.
- Stockfish 19 (depth-4 ladder): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5. Black: 1...c5; vs 2.c3 plays 2...d5 3.exd5 Qxd5 4.d4 Nf6 5.Nf3 e6 ...Bb7, ...Nc6-b4, ...Bxf3. It builds slowly (eval creeps to +1 over 5 moves), then trades into a back-rank/queen-fork tactic. Takes all free material; does not always repeat when ahead.
- GPT-6.1 Sol: White main-line Ruy or 1.d4 2.c4 3.Nf3 4.Nc3 5.Bg5. Black Berlin/...Bc5/...Ba7 vs 4.d3. Passive, then blunders to one-move tactics.

## Notes files
- notes/sicilian-plan.md: White vs 1...c5: G2 loss, G10/G12 draws, G16 loss (Alapin, back rank).
- notes/black-ruy-chigorin.md: Black Chigorin lines G3/G4.
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 lines vs Sol.
- notes/white-closed-ruy.md: G9, G14, G15 closed Ruy wins vs DeepSeek.
- notes/black-four-knights.md: G6/G7 losses vs 3.Nc3.
- notes/black-caro-kann.md: G11 Advance Caro-Kann loss, Nb5/Nd6+ fork.
- notes/black-qgd-lasker.md: G13 QGD Lasker win vs Sol.
