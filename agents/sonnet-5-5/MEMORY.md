# MEMORY (chess tournament, 600+10 clock)

## Record
- G1 (W vs DeepSeek V4.1 Flash): 1-0, won on time. Closed Ruy.
- G2 (W vs Stockfish 19): 0-1. 1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.O-O Nc7 6.Bc4? b5 7.Bb3?? c4 trapped the bishop.
- G3 (B vs GPT-6.1 Sol): 0-1, mate move 67. Closed Ruy Chigorin gave me +B+2P, then 42...Qe6?? Rxe6 and 45...Bd4+?? threw it away.
- G4 (B vs GPT-6.1 Sol, semifinal 2 g1): draw (corrected from a flag win): White flagged at move 67 while I had only a king, and a bare king cannot win on time (FIDE 6.9). I was dead lost (Q vs K). Chigorin was equal until 27...Kh7?, 28...exf4?, 30...a5??, 31...b4?? 32.e5! dxe5 33.Nxg7+ (discovered check from Bb1) and 35.Nxc7 won my queen. Details: notes/black-ruy-chigorin.md.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Check that the square is not occupied by my own piece (Nb7 with Qb7 was illegal).
- BLUNDER CHECK (all lost games came from skipping it): for my intended move, (1) list every enemy piece, ROOKS AND BISHOPS BEHIND PAWNS INCLUDED, that can capture on the destination square; (2) list all enemy checks, captures, discovered checks and pawn pushes (e4-e5!) after the move; (3) say what the move leaves undefended. Do not justify a move by a line that assumes the enemy recaptures with the queen.
- KING SAFETY: do not park the king on a diagonal/file behind my own or enemy pawn when an enemy bishop or rook sits behind that pawn (Kh7 vs Bb1+e4, G4). Count attackers on g7/h7/h6/f7 (R, N, B, Q) every move once the enemy has a Rg3 + Nf5 + Bb1 battery. A quiet pawn move (a5, b4) is wrong when the king is under battery; fix the king first (Kg8/Kh8, ...g6, ...Ng4 ideas).
- Do not give a check just because it is a check (45...Bd4+ lost a bishop). Ask who recaptures.
- TIME: I use about 10-20 s a move. Spend 60-90 s when the enemy has a battery aimed at my king, when I am ahead, when a piece moves to an attacked square, or when I offer a trade. Don't spend minutes on quiet pawn moves while ignoring the threat.
- When ahead: trade pieces only after the blunder check; keep a simple, safe move.
- BISHOP SAFETY: before bishop moves, list escape squares after ...b5, ...c4, ...a6, ...d5. Prefer Bf1 or Bxc6 early.
- Stockfish plays instantly and punishes any hung piece; no swindles.
- NEVER resign mentally: GPT-6.1 Sol burns clock when converting (30 s on a won Q vs pawn ending, flagged at 0:28). When lost against Sol, play fast, safe, legal moves, keep a pawn alive and stay near it (stalemate or flag chances). With a bare king a flag only gives a draw, so keeping a pawn matters. That half point was luck, not a plan: avoid lost positions.
- Opening as White vs 1...e5: Ruy Lopez 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.d4 (Chigorin trap: 11.h3 Bh5 12.Be3 Na5 13.Bc2 Nc4 14.Bc1, Nxb2 loses to Bxb2).
- Opening as White vs 1...c5: see notes/sicilian-plan.md.
- Opening as Black vs 1.e4: 1...e5 and the Chigorin: see notes/black-ruy-chigorin.md.

## Opponents
- DeepSeek V4.1 Flash: knows Ruy theory, slow (20-40 s a move), time trouble by move 20, blunders pieces and tries illegal moves. Keep solid.
- Stockfish 19: instant, tactically precise, answers 1.e4 with 1...c5, finds trapping pawn pushes.
- GPT-6.1 Sol: plays main-line Ruy as White (Bb3, c3, h3, Bc2, d4, Nbd2-f1-g3, then Be3, Rc1, d5, Bb1, Nh4-f5, f3-f4, Re3-g3, e5). It builds a kingside battery and finds sacrifices (Nxg7+ discovered check), takes free material instantly, converts cleanly. It thinks 20-60 s a move and reaches ~20-60 s by move 60. It can blunder (Qxg5+? once; Rg3?? marked in G4) and flagged in G4. Play solidly, watch its sacrifices, and wait.

## Notes files
- notes/sicilian-plan.md: safe White setups vs 1...c5 and the G2 loss.
- notes/black-ruy-chigorin.md: Black Chigorin lines from G3 and G4, where they went right and the blunders.
