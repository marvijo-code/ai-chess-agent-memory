# MEMORY (chess tournament, 600+10 clock)

## Record
- G1 (W vs DeepSeek V4.1 Flash): 1-0, Black won on time. Closed Ruy Lopez.
- G2 (W vs Stockfish 19): 0-1, mate on move 45. 1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.O-O Nc7 6.Bc4? b5 7.Bb3?? c4 trapped the bishop. Lost a piece, then the rest.

## Key lessons
- Output: reply with only the JSON move object. Illegal moves count as attempts (max 3), so check legality first.
- BISHOP SAFETY: before every bishop move or retreat, list its escape squares after each enemy pawn push (...b5, ...c4, ...a6, ...d5). A bishop on b3/c4/a4 can be trapped by ...b5 and ...c4 (a pawn on c4 hits b3, and Ba4 hangs to ...bxa4). Prefer retreats to f1, or trade it off (Bxc6) before it is kicked.
- Before each trade (Bxc4 etc.), recheck what recaptures and what is pinned. After 7...c4 my 8.Bxc4 bxc4 gave only a pawn for the bishop.
- Stockfish plays instantly (depth ~4) but punishes any hung or trapped piece. Do not expect swindles. Aim for a solid, safe position, not traps.
- Before every move check: what is hanging, all checks, all captures, and each pawn push by the opponent.
- Opening as White vs 1...e5: 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.d4 (reliable; in the Ruy, ...c5/...c4 pawn pushes against Bb3 are not a problem because d6 was played, but still check).
- Opening as White vs 1...c5: see notes/sicilian-plan.md. Do NOT play the Bb5-c4-b3 retreat plan against ...Nc7/...b5.
- Chigorin trap (Ruy): after 11.h3 Bh5 12.Be3 Na5 13.Bc2 Nc4 14.Bc1, Nxb2 loses a piece (Bxb2).
- When ahead: trade pieces, keep e4 covered, convert with rooks on the 7th.
- Clock: about 10 s per move was fine vs slow opponents. In G2 I was never short of time; the loss was a calculation error on move 7-8, so spend extra time on any move that retreats or trades a minor piece in the opening.
- When far behind, repeated passive defence loses (Qg3/Bd6 battery mated on h2). Keep the king covered against a Bd6 + queen battery on the b8-h2 diagonal early (h3 or Nf3/Bd2 control of h2).

## Opponents
- DeepSeek V4.1 Flash: knows Ruy Lopez theory but spends 20-40 s per move and gets into time trouble by move 20. It blundered pieces and makes illegal-move attempts. Keep positions solid and let it err.
- Stockfish 19 (ladder): moves instantly, tactically precise, answered 1.e4 with 1...c5. It finds piece-trapping pawn pushes (...c4). Play sound theory, not tricks.

## Notes files
- notes/sicilian-plan.md: safe White setups against 1...c5 and the line that lost G2.
