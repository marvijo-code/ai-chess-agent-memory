# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- G1 (W vs DeepSeek): 1-0 on time. Closed Ruy.
- G2 (W vs Stockfish): 0-1. 1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.O-O Nc7 6.Bc4? b5 7.Bb3?? c4 trapped the bishop.
- G3 (B vs Sol): 0-1. Chigorin gave +B+2P, then 42...Qe6?? 45...Bd4+?? threw it away.
- G4 (B vs Sol): draw (Sol flagged). Lost after 27...Kh7?, 28...exf4?, 30...a5??, 31...b4?? 32.e5!. notes/black-ruy-chigorin.md.
- G5 (W vs Sol, Armageddon): 1-0, mate move 32. 4.d3 anti-Berlin. notes/white-ruy-d3.md.
- G6 (B vs Stockfish): 0-1 in 25. 3.Nc3 Nf6 4.Bb5 Bb4 ... 9...bxc6? drifted. notes/black-four-knights.md.
- G7 (T2 R1, B vs Stockfish): 1/2 (threefold move 69, piece down). 8...d6?? 9.f4!. notes/black-four-knights.md.
- G8 (T2 R2, W vs Sol): 1-0, back-rank mate move 24. 4.d3 line.
- G9 (T2 R3, W vs DeepSeek): 1-0, mate move 53. Closed Ruy. Nearly blundered 31.Qxd4?? (own Bd3 blocked Rd1). notes/white-closed-ruy.md.
- G10 (T2 Final, W vs Stockfish, 900+10): 1/2 threefold at move 81, down R+B vs pawn. 1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.d4 equal; 20.Nb5?! 21.Nxa7 Rxb2 22.Nc6?! Ba3 23.Rc2?? Rxc2 (no recapture) lost a rook. notes/sicilian-plan.md.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Check destination is not my own piece and no own piece blocks the line.
- PROTECTED-SQUARE CHECK (G10, cost a rook): for every move, name the piece that recaptures on the destination square. Includes trade offers like Rc2 / Rd1 / Qg3: write 'if ...Rxc2 then X takes' with X's exact path. If I cannot name X, do not play it. Never assume a rook behind/beside covers the square without tracing the line.
- BLUNDER CHECK (every lost game came from skipping it): for the intended move (1) list every enemy piece, rooks and bishops behind pawns included, that can capture on the destination; (2) list enemy checks, captures, discovered checks, pawn pushes (f4! e5! c5! b5! c4!); (3) what does the move leave undefended or block?
- GREED CHECK (G10): knight raids for a wing pawn (Nb5xa7) let Black's rook take b2 and the knight ended offside. When equal/better, develop and keep pieces connected rather than grab a7/b7 pawns.
- RECAPTURE CHECK (G9): before any capture or trade, who recaptures, and does one of MY pieces block my recapture line? When ahead, choose the trade that needs no luck.
- Per-move written watch list (G8/G9 habit) is good but must include 'which piece recaptures'. Keep a concrete plan, not shuffles.
- RETREAT-SQUARE CHECK (G2, G7): before any pawn/quiet move ask which of my pieces can be hit by a pawn push (f4, e5, c4, b5) and where it would go. Never fill my own bishop's retreat square. Bishop on e5/c5/b4 hit by f4/d4/a3: castle or retreat/trade first.
- Stockfish plays the pawn lever the moment a piece has no retreat; depth 4 sees 2-3 move tactics and punishes any hanging piece instantly.
- PIN/FILE CHECK (G6, G7): do not put pieces on a file/diagonal where a rook or bishop can pin them to rook/king.
- KING SAFETY: no king behind a pawn on a diagonal/file with an enemy bishop/rook behind it. Keep luft; avoid ...gxf6 breaks. Check luft for both kings (back-rank mate won G8).
- Do not give a check just because it is a check. Ask who recaptures.
- OPENING DISCIPLINE: play only lines I know move by move. If unsure at moves 5-9, simplest developing/castling move, keep bishops safe, recapture toward the centre.
- TIME: 60-90 s on moves 6-12 when unsure, and whenever a piece can be attacked, a pin is possible, or I offer a trade. 1-8 s on book/routine moves. G10: I had 15 min left and still blundered in 25 s: slow down on any move that moves a rook/queen to a new square.
- When ahead: trade pieces only after the blunder check; keep simple and safe. In won endings check stalemate each move.
- WHEN LOST: play fast, safe legal moves, keep the king guarding pawns/shield squares. Stockfish does not convert (G7 and G10 both threefold at +7..+9): shuffle the king between two safe squares (Kf2/Kf3) and avoid h-file mates; it repeats within ~30 moves.
- BISHOP SAFETY: list escape squares after ...b5, ...c4, ...a6, ...d5, f4. Prefer Bf1, Bc2 or Bxc6 early.
- Armageddon as White (a draw loses): solid d3/c3 setup, trade queens only if safe, let Sol err.
- Opening as White vs 1...e5: vs 3...Nf6 play 4.d3 (notes/white-ruy-d3.md); vs 3...a6 closed Ruy 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 (notes/white-closed-ruy.md). Vs 1...c5: 2.c3 is fine vs Stockfish (G10), see notes/sicilian-plan.md.
- Opening as Black vs 1.e4: 1...e5; vs 3.Bb5 Chigorin (notes/black-ruy-chigorin.md); vs Stockfish 3.Nc3 see notes/black-four-knights.md.

## Opponents
- DeepSeek V4.1 Flash: Chigorin Ruy as Black quickly, then 40-50 s/move; time trouble by move 25; blunders pieces, tries illegal moves. Stay solid, convert safely.
- Stockfish 19 (depth-4 ladder): instant moves. As White: 1.e4, 2.Nf3, 3.Nc3, vs 3...Bc5 4.Nxe5 5.d4 6.dxe5 7.Bd3 8.Ne2 9.f4. As Black: 1...c5; vs 2.c3 it plays 2...d5 3.exd5 Qxd5 4.d4 Nf6 5.Nf3 e6 6.Be2 cxd4 (equal). Finds trapping pawn pushes and pins; takes any free material; shuffles into repetition when winning.
- GPT-6.1 Sol: as White main-line Ruy with kingside battery (Nf1-g3, Be3, Rc1, d5, Bb1, Nh4-f5, f4, Re3-g3, e5), finds sacrifices (Nxg7+). As Black Berlin-style or ...Bc5/...Ba7 setups vs 4.d3; gets passive and blunders. Thinks 5-60 s.

## Notes files
- notes/sicilian-plan.md: White vs 1...c5: G2 loss, G10 Alapin game and the Rc2?? blunder.
- notes/black-ruy-chigorin.md: Black Chigorin lines from G3/G4.
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 lines vs Sol.
- notes/white-closed-ruy.md: G9 closed Ruy win, Qxd4?? recapture lesson, rook-ending mate technique.
- notes/black-four-knights.md: G6/G7 losses vs Stockfish's 3.Nc3.
