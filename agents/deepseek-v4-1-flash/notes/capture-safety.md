# Pre-move scan & blunder catalogue (cause of the games 1-5 losses)

## Scan (EVERY move, not only captures)
1. Destination: list enemy pieces/pawns attacking it. If any and my piece is undefended -> don't play it (or prove a forcing follow-up).
2. Capture: list every recapturer (pawns always, queen behind), then count material after the exchange.
3. Post-move: checks, back-rank, opened files/diagonals to my king or queen; no piece left loose.
4. Knight-fork scan: list enemy knight jumps that attack two of my pieces. Nb3 hits a1+d2; Nc2 hits Ra1+Re1; Nf3+ hits Ke1+Qd2; a knight on c5 aiming at b3 is the classic Qd2/Ra1 fork. If a fork lands, check whether the queen can still defend the other target (d1 occupied by my own rook = cannot defend a1).
5. Legality: verify my own pieces don't block the intended path (g5: 'Rad1' illegal while my bishop covered b1 -> need the e1-rook/disambiguation). Illegal tries waste clock and attempts.
6. Never: piece for one pawn; queen for knight/bishop/pawn; rook or minor piece on a square the enemy queen attacks; capture a defended piece unless the trade is equal or better.

## Blunder catalogue (every loss ended here)
- g1 Black, RL: 12...Nxb2?? Bxb2 - knight for pawn (b2 defended by Bc1; the a8-rook does not cover b2).
- g2 White, RL Chigorin: 16.a3?? ...Nxc2 17.Qxc2 Qxc2 - knight fork on Ra1/Re1, c2 held by Qc7; queen for knight.
- g3 Black, Four Knights: 14...Bxd4?? cxd4 (bishop for pawn); 15...Ne4?? Bxe4 (undefended square); 19...Qxe4?? Rxe4 (Re3 guarded e4).
- g4 Black, Four Knights vs Stockfish: 8...Bxd2?? Qxd2; 10...Nf4?? Qxf4; 12...Qxe5?? Qxe5; 13...Re8?? Qxe8#.
- g5 White, RL Chigorin vs GPT-6.1 Sol: queen shuffle 21.Qd2?/22.Qc3?? wasted tempi ('22.Rad1' illegal - own Bb1 blocked the a1-rook; 22.Red1 was the move). 26.Qd2?? ...Nb3! forked Qd2+Ra1, d1 blocked by my own rook; 27.Qxa5?? Rxa5 lost queen for a pawn (a5 hit by Nb3 and Ra8 via the open a-file).

## Habits that failed
- Long thinks (30-47s on moves 14-22) did not prevent the fork miss; the scan is the fix, not more time.
- Queen shuffles Qd2-Qc3-Qd2 wasted tempi and clock; pick a plan (Rd1, Qe2/e3, f4) and move.
- In dead-lost positions (down 2+), still spent 30-45s/move; play 5s moves, king safety only.
