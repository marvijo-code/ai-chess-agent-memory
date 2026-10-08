# MEMORY (chess tournament, 600+10 clock; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- G1 (W vs DeepSeek V4.1 Flash): 1-0, won on time. Closed Ruy.
- G2 (W vs Stockfish 19): 0-1. 1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.O-O Nc7 6.Bc4? b5 7.Bb3?? c4 trapped the bishop.
- G3 (B vs GPT-6.1 Sol): 0-1, mate move 67. Chigorin gave me +B+2P, then 42...Qe6?? and 45...Bd4+?? threw it away.
- G4 (B vs Sol, semifinal 2 g1): draw (Sol flagged vs my bare king, which cannot win on time). I was lost after 27...Kh7?, 28...exf4?, 30...a5??, 31...b4?? 32.e5!. See notes/black-ruy-chigorin.md.
- G5 (W vs Sol, semifinal 2 Armageddon): 1-0, mate on move 32. 4.d3 anti-Berlin Ruy, queens off, Sol blundered a piece (19...Nxe4??), then K+N march and Ne5#. See notes/white-ruy-d3.md.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Check the square is not occupied by my own piece.
- BLUNDER CHECK (all lost games came from skipping it): for my intended move, (1) list every enemy piece, ROOKS AND BISHOPS BEHIND PAWNS INCLUDED, that can capture on the destination square; (2) list all enemy checks, captures, discovered checks and pawn pushes (e4-e5!) after the move; (3) say what the move leaves undefended. Count attackers vs defenders on every contested square (this won G5).
- KING SAFETY: do not park the king on a diagonal/file behind a pawn when an enemy bishop or rook sits behind it (Kh7 vs Bb1+e4, G4). Count attackers on g7/h7/h6/f7 once the enemy has a Rg3 + Nf5 + Bb1 battery. Fix the king before quiet pawn moves.
- Do not give a check just because it is a check (45...Bd4+ lost a bishop). Ask who recaptures.
- TIME: 5-20 s a move is fine. Spend 60-90 s when the enemy has a battery at my king, when I am ahead, when a piece moves to an attacked square, or when I offer a trade.
- When ahead: trade pieces only after the blunder check; keep a simple, safe move. In pawn/knight endings: king to the centre, keep the knight defended, avoid knight squares that allow pawn forks/attacks, look for mating nets near the enemy king.
- BISHOP SAFETY: before bishop moves, list escape squares after ...b5, ...c4, ...a6, ...d5. Prefer Bf1, Bc2 or Bxc6 early.
- Stockfish plays instantly and punishes any hung piece; no swindles.
- NEVER resign mentally: Sol burns clock when converting. When lost, play fast, safe, legal moves and keep a pawn alive (a flag vs a bare king is only a draw). Better: avoid lost positions.
- Armageddon as White (a draw loses): do not force things. Solid d3/c3 setup, trade queens only if safe, and let Sol err in simplified positions.
- Opening as White vs 1...e5: vs 3...Nf6 play 4.d3 (notes/white-ruy-d3.md); vs 3...a6 closed Ruy 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.d4.
- Opening as White vs 1...c5: see notes/sicilian-plan.md.
- Opening as Black vs 1.e4: 1...e5 and the Chigorin: see notes/black-ruy-chigorin.md.

## Opponents
- DeepSeek V4.1 Flash: knows Ruy theory, slow (20-40 s a move), time trouble by move 20, blunders pieces and tries illegal moves. Keep solid.
- Stockfish 19: instant, tactically precise, answers 1.e4 with 1...c5, finds trapping pawn pushes.
- GPT-6.1 Sol: as White plays main-line Ruy and builds a kingside battery (Nf1-g3, Be3, Rc1, d5, Bb1, Nh4-f5, f3-f4, Re3-g3, e5) and finds sacrifices (Nxg7+ discovered check). As Black (G5) it plays Berlin-style ...Nf6/...Bc5, ...d5 and trades queens. It thinks 5-60 s a move, burns clock, and can blunder: Qxg5+? once, Rg3?? in G4, 19...Nxe4?? (piece lost) in G5. Play solidly, count attackers on every capture, wait for its errors.

## Notes files
- notes/sicilian-plan.md: safe White setups vs 1...c5 and the G2 loss.
- notes/black-ruy-chigorin.md: Black Chigorin lines from G3 and G4, where they went right and the blunders.
- notes/white-ruy-d3.md: G5 winning line with 4.d3 vs Sol and the endgame plan.
