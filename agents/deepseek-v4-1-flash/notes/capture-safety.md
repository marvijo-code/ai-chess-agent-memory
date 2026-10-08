# Pre-move scan & blunder catalogue (cause of the games 1-4 losses)

## Scan (EVERY move, not only captures)
1. Destination: list enemy pieces/pawns attacking it. If any and my piece is undefended -> don't play it (or prove a forcing follow-up).
2. Capture: list every recapturer (pawns always, queen behind), then count material after the exchange.
3. Post-move: checks, back-rank, opened files/diagonals to my king or queen; no piece left loose.
4. Never: piece for one pawn; queen for knight/bishop; rook or minor piece on a square the enemy queen attacks; capture a defended piece unless the trade is equal or better.

## Blunder catalogue (every loss ended here)
- g1 Black, RL: 12...Nxb2?? Bxb2 - knight for pawn (b2 defended by Bc1; the a8-rook does not cover b2).
- g2 White, RL Chigorin: 16.a3?? ...Nxc2 17.Qxc2 Qxc2 - c2 defended by Qc7; queen for knight.
- g3 Black, Four Knights: 14...Bxd4?? cxd4 (bishop for pawn); 15...Ne4?? Bxe4 (undefended square); 19...Qxe4?? Rxe4 (Re3 guarded e4).
- g4 Black, Four Knights vs Stockfish: 8...Bxd2?? Qxd2 (d2 defended by Qd1/Bc1; +0.5 -> +6.9); 10...Nf4?? Qxf4 (queen sees d2-e3-f4); 12...Qxe5?? Qxe5 (e5 knight defended by Qe3; queen for knight); 13...Re8?? Qxe8# (undefended rook to a queen-attacked square, back-rank mate).

## Habits that failed
- Long thinks (30-45s) on simple moves did not prevent the g4 blunders; the scan is the fix, not more time.
- In dead-lost positions (down 2+), still spent 30-45s/move; play 5s moves, king safety only.
