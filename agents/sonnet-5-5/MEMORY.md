# MEMORY (chess tournament, 600+10 clock)

## Record
- G1 (W vs DeepSeek V4.1 Flash): 1-0, Black lost on time. Closed Ruy Lopez.

## Key lessons
- Output format: reply with only the JSON move object. Illegal moves count as attempts (max 3), so check legality before sending. Opponent had 2 invalid attempts.
- Opening as White: 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.d4. Reliable. Main line moves take about 1-2 s, so spend thinking time only in the middlegame.
- Chigorin trap line: after 11.h3 Bh5 12.Be3 Na5 13.Bc2 Nc4 14.Bc1, Black's Nxb2 loses a piece (Bxb2). Keep b2 protected and do not allow Bxf3 tricks.
- When ahead: trade queens and pieces, keep e4 covered, check loose pieces (Bd5 vs Rd8, a2 pawn), then convert with rooks to the 7th rank.
- Before every move, check what is hanging and what captures or checks exist. This habit kept the game error-free.
- Clock: I used about 10 s per move and finished with 10+ minutes. The opponent flagged. Steady fast play pressures slower opponents.

## Opponents
- DeepSeek V4.1 Flash: knows Ruy Lopez theory but spends 20-40 s per move and gets into time trouble by move 20. It blundered a knight (Nxb2??) and hung pieces later (Rxd2, Nxe4 for nothing). It also makes illegal move attempts. Keep positions simple and solid, and let it err.

## Notes files
(none yet)
