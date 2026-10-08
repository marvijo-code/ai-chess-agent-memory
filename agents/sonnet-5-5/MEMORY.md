# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- Closed Ruy as White vs DeepSeek: G1, G9, G14, G15 all 1-0 (G14/G15 mate 34, notes/white-closed-ruy.md).
- G2 W vs SF 0-1 (Sicilian 3.Bb5, 6.Bc4? b5 7.Bb3?? c4).
- G3 B vs Sol 0-1 (Chigorin, was +B+2P, then 42...Qe6??). G4 B vs Sol draw (my Kh7?, exf4?, a5??, b4??).
- G5 W vs Sol 1-0 (Armageddon, 4.d3). G6 B vs SF 0-1 (3.Nc3 Nf6 4.Bb5 Bb4 ... 9...bxc6?). G7 B vs SF 1/2 (8...d6?? 9.f4!).
- G8 W vs Sol 1-0 (4.d3, mate 24). G10 W vs SF 1/2 (23.Rc2??).
- G11 B vs SF 0-1 (Caro-Kann Advance 7...Nbc6?? 8.Nb5!). G12 W vs SF 1/2 (Alapin; 18.Bxh7+??, 23.Bd2??).
- G13 (T3 R2) B vs Sol 1-0: QGD Lasker vs 1.d4, 17...Nd4! won a rook.
- G15 (T3 SF1 g1) W vs DeepSeek 1-0, mate 34: same Ruy plan, Bh6/Qd2/Qh6+, 26.Nxg5 won a piece.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Destination must not be my own piece; no own piece on the line.
- SELF-BLOCK CHECK (G9, G12, G15; cost a queen twice, an illegal try in G15): before any queen move/trade/capture/rook line, name the recapturing piece AND its exact path; none of MY pieces may block it (G15: Qh6 illegal because my Ng5 stood on the diagonal).
- NO 'FREE PAWN' CHECKS (G12): if my piece is attacked, just recapture. Never insert a capture-with-check first (Bxh7+ Nxh7 lost a bishop). After a capture ask: what recaptures MY capturing piece?
- PROTECTED-SQUARE CHECK (G10, G11): for every move name who recaptures on the destination and which enemy rook/queen/bishop attacks it.
- KNIGHT-JUMP CHECK (G11): before ...c5/...Nbc6/...a6 ask where an enemy knight can land (b5, d6, c7, f7, e5, d5) and what it forks. Compute 3 plies.
- BLUNDER CHECK: (1) enemy captures on the destination; (2) enemy checks, captures, pawn pushes (f4! e5! c5! b5! c4!), knight forks; (3) what does my move leave undefended or block?
- LOOSE-PIECE SCAN (G13 win): each move look for enemy undefended pieces on files/diagonals. Do it for my pieces too.
- WRITE-A-WATCH-LIST (G14, G15 worked): after each move note 'watch ...X' (checks, recaptures, which queen check is safe). Kept me error-free for 34 moves twice.
- Equal positions: no tricks. Stockfish at depth 4 punishes every mistake; simple solid moves are enough.
- GREED CHECK: no wing-pawn raids, no h7 bishop grabs; keep pieces connected. Take a pawn (Nxg5) only if the capturer is protected and the follow-up recapture is counted.
- RETREAT-SQUARE CHECK: which of my pieces can be hit by a pawn push and where would it go? Bishop escape squares after ...b5, ...c4, ...a6, ...d5, f4.
- PIN/FILE CHECK: no knight pinned to the queen; no pieces on open files vs rooks. KING SAFETY: keep luft.
- OPENING DISCIPLINE: play only lines I know move by move; slow down at moves 5-10 vs Stockfish.
- TIME: 1-8 s on book moves is fine, but 60-90 s at every capture, trade, queen move, or fork chance. G12 lost with 11 min unused.
- When ahead: trade pieces after the blunder check; take pawns safely; check stalemate EVERY move in won endings (leave a flight square until the mating move).
- WHEN LOST: Stockfish repeated in 3 of 4 lost games (not G11). Play safe king moves that give checks; keep rooks connected.
- Armageddon as White (draw loses): solid d3/c3 setup. As Black (draw wins): safest known setup.
- Openings as White: vs 1...e5 3...Nf6 play 4.d3; vs 3...a6 closed Ruy (5.O-O 6.Re1 7.Bb3 8.c3 9.h3 10.Bc2 11.d4 12.Nbd2, vs ...Nc6 13.d5). Vs 1...c5: 2.c3 (notes/sicilian-plan.md).
- Openings as Black: vs 1.d4 QGD Lasker (notes/black-qgd-lasker.md; worked). Vs 1.e4: 1...e5 (notes/black-ruy-chigorin.md; vs 3.Nc3 notes/black-four-knights.md). 1...c6 Advance: see notes/black-caro-kann.md first.

## Opponents
- DeepSeek V4.1 Flash (0 losses to me in 4): Chigorin Ruy as Black (...Na5, ...c5, ...Qc7, ...Nc6, 13.d5 Nb8, ...Nbd7, ...g6, ...Re8, ...Bf8, ...Kh8 = self-weakening dark squares); 40-50 s/move, ends with 2-4 min, hangs pieces/queen when worse, tries illegal moves (3 in G15). Stay solid.
- Stockfish 19 (depth-4 ladder): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5; vs Caro-Kann 2.d4 3.e5 ... Nb5 forks. Black: 1...c5; vs 2.c3 plays 2...d5 3.exd5 Qxd5 4.d4 Nf6 5.Nf3 e6 ...Bb7, ...Nc6-b4, ...Bxf3. Finds pins, forks, traps; takes free material; usually repeats when far ahead.
- GPT-6.1 Sol: White either main-line Ruy or 1.d4 2.c4 3.Nf3 4.Nc3 5.Bg5 6.e3 7.Bh4 8.Bxe7 9.Rc1. Black Berlin/...Bc5/...Ba7 vs 4.d3. Passive, then blunders to one-move tactics. Thinks 5-60 s.

## Notes files
- notes/sicilian-plan.md: White vs 1...c5: G2 loss, G10/G12 Alapin games.
- notes/black-ruy-chigorin.md: Black Chigorin lines G3/G4.
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 lines vs Sol.
- notes/white-closed-ruy.md: G9, G14, G15 closed Ruy wins vs DeepSeek, recapture/self-block lessons.
- notes/black-four-knights.md: G6/G7 losses vs 3.Nc3.
- notes/black-caro-kann.md: G11 Advance Caro-Kann loss, Nb5/Nd6+ fork.
- notes/black-qgd-lasker.md: G13 QGD Lasker win vs Sol, Nd4 trick, endgame.
