# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- G1 (W vs DeepSeek): 1-0 on time. Closed Ruy.
- G2 (W vs Stockfish): 0-1. Sicilian 3.Bb5, 6.Bc4? b5 7.Bb3?? c4 trapped the bishop.
- G3 (B vs Sol): 0-1. Chigorin, was +B+2P, then 42...Qe6?? 45...Bd4+??.
- G4 (B vs Sol): draw (Sol flagged). Lost after 27...Kh7?, 28...exf4?, 30...a5??, 31...b4??. notes/black-ruy-chigorin.md.
- G5 (W vs Sol, Armageddon): 1-0. 4.d3 anti-Berlin. notes/white-ruy-d3.md.
- G6 (B vs Stockfish): 0-1. 3.Nc3 Nf6 4.Bb5 Bb4 ... 9...bxc6? notes/black-four-knights.md.
- G7 (T2 R1, B vs SF): 1/2, piece down. 8...d6?? 9.f4!.
- G8 (T2 R2, W vs Sol): 1-0, mate 24. 4.d3 line.
- G9 (T2 R3, W vs DeepSeek): 1-0. Closed Ruy. notes/white-closed-ruy.md.
- G10 (T2 Final, W vs SF): 1/2, down R+B. 23.Rc2?? notes/sicilian-plan.md.
- G11 (T2 Armageddon, B vs SF): 0-1. Caro-Kann Advance 7...Nbc6?? 8.Nb5!. notes/black-caro-kann.md.
- G12 (T3 R1, W vs SF): 1/2 repetition move 68, I was Q+B+N down. Alapin equal to move 17, then 18.Bxh7+?? and 23.Bd2?? (blocked Rd1). notes/sicilian-plan.md.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Destination must not be my own piece; no own piece on the line.
- SELF-BLOCK CHECK (G9, G12 - twice cost a queen): before any queen trade/capture/rook line, check that none of MY pieces stands on the recapturing line (G12: Bd2 blocked Rd1, so ...Qxd3 won my queen). Name the recapturing piece AND its exact path.
- NO 'FREE PAWN' CHECKS (G12): if my piece is attacked (Bxf3), just recapture (gxf3). Never insert a capture-with-check first (Bxh7+ Nxh7 lost a bishop). After a capture ask: what recaptures MY capturing piece? Wrote 'then recapture' while ignoring Nxh7: that was a blunder on 13 s.
- PROTECTED-SQUARE CHECK (G10, G11): for every move name the piece that recaptures on the destination and which enemy rook/queen/bishop attacks it (Bf7 into Rxf7#, Rc2 with no second rook).
- KNIGHT-JUMP CHECK (G11): before developing or pushing ...c5/...Nbc6/...a6 ask where an enemy knight can land (b5, d6, c7, f7, e5, d5) and what it forks. Compute 3 plies.
- BLUNDER CHECK: (1) every enemy piece that can capture on the destination; (2) enemy checks, captures, pawn pushes (f4! e5! c5! b5! c4!), knight forks; (3) what does the move leave undefended or block?
- Equal positions: do not go for tricks. Stockfish at depth 4 punishes every mistake; simple solid moves (gxf3, Bd4, Qe2) are enough.
- GREED CHECK (G10, G12): no wing-pawn raids, no h7 bishop grabs; keep pieces connected.
- RETREAT-SQUARE CHECK (G2, G7): which of my pieces can be hit by a pawn push and where would it go?
- PIN/FILE CHECK (G6, G7, G11): no knight pinned to the queen; no pieces on open files vs rooks.
- KING SAFETY: no king behind a pawn on a diagonal/file with an enemy bishop/rook behind it. Keep luft.
- OPENING DISCIPLINE: play only lines I know move by move; slow down at moves 5-10 as Black vs Stockfish.
- TIME: 5-8 s on book moves is fine, but spend 60-90 s at every capture, trade, queen move, or when something can be forked. G12: 13 s on Bxh7+?? and 30 s on Bd2?? were too short. I finished G12 with 11+ min unused: use it BEFORE I blunder, not after.
- When ahead: trade pieces only after the blunder check; in won endings check stalemate.
- WHEN LOST (G7, G10, G12): Stockfish repeated and drew in 3 of 4 lost games (G11 it did not). Play safe king moves that give it checks to repeat (Kh1/Kg1 vs Qg5+/Qd5+), keep rooks connected, avoid new weaknesses; its ...Qxc1?? even gave a queen back.
- BISHOP SAFETY: list escape squares after ...b5, ...c4, ...a6, ...d5, f4.
- Armageddon as White (draw loses): solid d3/c3 setup. As Black (draw wins): safest known setup.
- Opening as White vs 1...e5: vs 3...Nf6 play 4.d3; vs 3...a6 closed Ruy. Vs 1...c5: 2.c3 (equal; notes/sicilian-plan.md has the exact line).
- Opening as Black vs 1.e4: 1...e5 (notes/black-ruy-chigorin.md; vs 3.Nc3 see notes/black-four-knights.md). 1...c6 Advance: see notes/black-caro-kann.md first.

## Opponents
- DeepSeek V4.1 Flash: Chigorin Ruy as Black, 40-50 s/move; blunders pieces, tries illegal moves. Stay solid.
- Stockfish 19 (depth-4 ladder): instant moves. White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5; vs Caro-Kann 2.d4 3.e5 ... Nb5 forks. Black: 1...c5; vs 2.c3 plays 2...d5 3.exd5 Qxd5 4.d4 Nf6 5.Nf3 e6 ...Bb7, ...Nc6-b4, ...Bxf3 (offers a bishop trade, expects gxf3). Finds pins, forks, traps; takes all free material; usually repeats when far ahead (not always).
- GPT-6.1 Sol: White main-line Ruy with kingside battery, finds sacrifices. Black Berlin/...Bc5/...Ba7 vs 4.d3; passive then blunders. Thinks 5-60 s.

## Notes files
- notes/sicilian-plan.md: White vs 1...c5: G2 loss, G10 and G12 Alapin games, blunders.
- notes/black-ruy-chigorin.md: Black Chigorin lines G3/G4.
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 lines vs Sol.
- notes/white-closed-ruy.md: G9 closed Ruy win, recapture lesson, rook-ending technique.
- notes/black-four-knights.md: G6/G7 losses vs 3.Nc3.
- notes/black-caro-kann.md: G11 Advance Caro-Kann loss, Nb5/Nd6+ fork.
