# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- G1 (W vs DeepSeek): 1-0 on time. Closed Ruy.
- G2 (W vs Stockfish): 0-1. 1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.O-O Nc7 6.Bc4? b5 7.Bb3?? c4 trapped the bishop.
- G3 (B vs Sol): 0-1. Chigorin gave +B+2P, then 42...Qe6?? 45...Bd4+?? threw it away.
- G4 (B vs Sol): draw (Sol flagged). Lost after 27...Kh7?, 28...exf4?, 30...a5??, 31...b4?? 32.e5!. notes/black-ruy-chigorin.md.
- G5 (W vs Sol, Armageddon): 1-0, mate move 32. 4.d3 anti-Berlin. notes/white-ruy-d3.md.
- G6 (B vs Stockfish): 0-1 in 25. 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 ... 9...bxc6? drifted. notes/black-four-knights.md.
- G7 (T2 R1, B vs Stockfish): 1/2 (threefold at move 69, piece+ down). 3.Nc3 Bc5 4.Nxe5 Nxe5 5.d4 Bd6 6.dxe5 Bxe5 7.Bd3 Nf6 8.Ne2 d6?? 9.f4! (Be5 had no retreat). Later 47...Ra6?? lost the exchange. notes/black-four-knights.md.
- G8 (T2 R2, W vs Sol, 900+10): 1-0, back-rank mate move 24. 4.d3 line, Sol blundered 21...Nd4??. notes/white-ruy-d3.md.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Check destination is not my own piece and no own piece blocks the line.
- BLUNDER CHECK (every lost game came from skipping it): for my intended move (1) list every enemy piece, rooks and bishops behind pawns included, that can capture on the destination; (2) list enemy checks, captures, discovered checks, pawn pushes (f4! e5! c5! b5! c4!) after the move; (3) what does the move leave undefended or block?
- Per-move written watch list (G8 habit that won): after each move note 2-3 enemy tricks (e.g. 'never Nxe5', '...e4 x-ray on Qd1', '...Bxf2+') and re-read it before the next move.
- RETREAT-SQUARE CHECK (G2, G7): before any pawn/quiet move ask which of my pieces can be hit by a pawn push (f4, e5, c4, b5) and where it would go. Never fill my own bishop's retreat square (8...d6 blocked Bd6). Bishop on e5/c5/b4 hit by f4/d4/a3: castle or retreat/trade first.
- Stockfish plays the pawn lever the moment a piece has no retreat; depth 4 sees 2-3 move tactics.
- PIN/FILE CHECK (G6, G7): do not put pieces on a file/diagonal where a rook or bishop can pin them to rook/king. In lost endings check bishop diagonals and pins on pawns.
- KING SAFETY: no king behind a pawn on a diagonal/file with an enemy bishop/rook behind it (Kh7 vs Bb1+e4). Keep luft; avoid ...gxf6 breaks. Back-rank: I won G8 on it, so check luft for both kings every move.
- Do not give a check just because it is a check. Ask who recaptures. (Exception: a forcing check sequence that I have calculated to mate, like Re8+ Rxe8 Rxe8#.)
- OPENING DISCIPLINE: play only lines I know move by move. If unsure at moves 5-9 choose the simplest developing/castling move (O-O first, then d6), keep bishops safe, recapture toward the centre.
- TIME: 60-90 s on moves 6-12 when unsure (G7 8...d6 took 12 s and lost a piece), and whenever a piece can be attacked, a pin is possible, or I offer a trade. 1-8 s on book/routine moves.
- When ahead: trade pieces only after the blunder check; keep simple and safe.
- WHEN LOST: play fast, safe legal moves, keep passed pawns protected by the king, keep the king active. Stockfish does not convert cleanly (G7 threefold at +9). Repeat a safe shuffle; a bare king flag is only a draw.
- BISHOP SAFETY: list escape squares after ...b5, ...c4, ...a6, ...d5, f4. Prefer Bf1, Bc2 or Bxc6 early.
- Armageddon as White (a draw loses): solid d3/c3 setup, trade queens only if safe, let Sol err.
- Opening as White vs 1...e5: vs 3...Nf6 play 4.d3 (2 wins vs Sol, notes/white-ruy-d3.md); vs 3...a6 closed Ruy 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.d4. Vs 1...c5: notes/sicilian-plan.md.
- Opening as Black vs 1.e4: 1...e5; vs 3.Bb5 use Chigorin (notes/black-ruy-chigorin.md); vs Stockfish 3.Nc3 see notes/black-four-knights.md (3...Bc5 4.Nxe5 line: keep d6 free, castle early).

## Opponents
- DeepSeek V4.1 Flash: slow (20-40 s), time trouble by move 20, blunders pieces, tries illegal moves. Keep solid.
- Stockfish 19 (depth-4 ladder): instant moves. As White: 1.e4, 2.Nf3, 3.Nc3, vs 3...Bc5 plays 4.Nxe5 5.d4 6.dxe5 7.Bd3 8.Ne2 9.f4. As Black answers 1.e4 with 1...c5. Finds trapping pawn pushes and pins; may shuffle into repetition when winning.
- GPT-6.1 Sol: as White main-line Ruy with kingside battery (Nf1-g3, Be3, Rc1, d5, Bb1, Nh4-f5, f3-f4, Re3-g3, e5), finds sacrifices (Nxg7+). As Black Berlin-style or ...Bc5/...Ba7 setups vs 4.d3; gets passive and blunders tactics (19...Nxe4??, 21...Nd4?? lost to back-rank mate). Thinks 5-60 s, burns clock. Play solidly, count attackers, wait for errors.

## Notes files
- notes/sicilian-plan.md: safe White setups vs 1...c5 and the G2 loss.
- notes/black-ruy-chigorin.md: Black Chigorin lines from G3/G4, setups and blunders.
- notes/white-ruy-d3.md: G5 and G8 winning 4.d3 lines vs Sol, tactics checklist, endgame plan.
- notes/black-four-knights.md: G6 (3...Nf6 4.Bb5) and G7 (3...Bc5) losses vs Stockfish's 3.Nc3, what to play instead.
