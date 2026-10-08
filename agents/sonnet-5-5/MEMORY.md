# MEMORY (chess tournament, 600+10 clock)

## Record
- G1 (W vs DeepSeek V4.1 Flash): 1-0, won on time. Closed Ruy.
- G2 (W vs Stockfish 19): 0-1. 1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.O-O Nc7 6.Bc4? b5 7.Bb3?? c4 trapped the bishop.
- G3 (B vs GPT-6.1 Sol): 0-1, mate move 67. Closed Ruy Chigorin gave me +B+2P by move 41, then 42...Qe6?? Rxe6 and 45...Bd4+?? Qxd4 threw it away. I ended with 9 min unused on the clock.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3).
- BLUNDER CHECK (both lost games came from skipping it): for my intended move, (1) list every enemy piece, ROOKS INCLUDED, that can capture on the destination square; (2) list all enemy checks, captures and threats after the move; (3) say what the move leaves undefended. Do not justify a move by a line that assumes the enemy recaptures with the queen. In G3 I offered a queen trade on e6 with the enemy rook on e4 and it simply took.
- Do not give a check just because it is a check. 45...Bd4+ lost the bishop because the pinned/blocked defender (d6 pawn blocked Rd8) could not recapture. Ask who recaptures.
- TIME: I use about 10 s a move and finish with 9+ minutes left. Spend 60-90 s whenever I am ahead, a queen/bishop moves to an attacked square, or I offer a trade. Time is a resource; the opponents often run low (GPT-6.1 Sol had 21 s at the end).
- When ahead: trade pieces only after the blunder check; keep a simple, safe move. When far behind, nothing worked; avoid getting there.
- BISHOP SAFETY: before bishop moves/retreats, list escape squares after ...b5, ...c4, ...a6, ...d5. Ba4/Bb3/Bc4 can be trapped. Prefer Bf1 or Bxc6 early.
- Before each trade, recheck what recaptures and what is pinned.
- Stockfish plays instantly and punishes any hung piece; no swindles.
- Keep the king covered vs a queen+Bd6 battery on b8-h2 (h3).
- Opening as White vs 1...e5: Ruy Lopez 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.d4 (Chigorin trap: 11.h3 Bh5 12.Be3 Na5 13.Bc2 Nc4 14.Bc1, Nxb2 loses to Bxb2).
- Opening as White vs 1...c5: see notes/sicilian-plan.md.
- Opening as Black vs 1.e4: 1...e5 and the Chigorin worked well: see notes/black-ruy-chigorin.md.

## Opponents
- DeepSeek V4.1 Flash: knows Ruy theory, slow (20-40 s a move), time trouble by move 20, blunders pieces and tries illegal moves. Keep solid.
- Stockfish 19: instant, tactically precise, answers 1.e4 with 1...c5, finds trapping pawn pushes.
- GPT-6.1 Sol: plays main-line Ruy (Bb3, c3, h3, Bc2, d4, Nbd2-f1-g3), thinks 20-60 s a move and ran down to ~20 s. It takes free material instantly (Rxe6) and converts Q vs pawns cleanly, but it also blundered a queen once (Qxg5+? Kxg5) and made loose moves (Qg3, Nh4, Nf3) while behind. Play solidly and wait.

## Notes files
- notes/sicilian-plan.md: safe White setups vs 1...c5 and the G2 loss.
- notes/black-ruy-chigorin.md: Black Chigorin line from G3, where it went right and the two blunders.
