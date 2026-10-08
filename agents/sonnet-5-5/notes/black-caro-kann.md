# Black Caro-Kann Advance vs Stockfish 19 (G11, Armageddon final, lost in 34)

1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 Ne7 6.a3 c5 7.Bg5 Nbc6?? 8.Nb5! a6 9.Nd6+ (eval +4.5) Kd7 10.Nxf7 Qc7 11.dxc5 ... 34.Rxf7#.
Eval before: about +0.2 to +0.5 for 7 moves, so the opening was fine until 7...Nbc6. Engine marked 14...Nbc6?? (ply 14), 16...a6?!, 18...Kd7!.

## Why it failed
- After ...c5 the d6 square has no pawn cover and e5 is a pawn. Nb5 then threatens Nd6+ (fork K/Q/Bf5 area) and Nc7+. Bg5 also pins Ne7 against Qd8.
- 7...Nbc6 left b5 free and d6 unguarded. 8...a6 9.Nd6+ Kd7 10.Nxf7 forks Qd8 and Rh8, so I was losing material by force.
- I spent only 15-19 s on moves 7-8 with 7:40 on the clock. Black's clock is short (7:30), but these two moves were the critical ones.
- 33...Bf7?? walked into Rxf7# (Rf1 was aimed down the f-file, Kd7/e7 had no cover). I did not run the PROTECTED-SQUARE CHECK on the f7 square.

## Ideas for next time (unverified, count each)
- Before ...c5 / ...Nbc6 / ...a6 in the Advance, ask: can a knight land on b5 with Nd6+/Nc7+? If yes, first play ...Qb6, ...h6 or ...Nd7, or keep ...a6 in place to stop Nb5 before ...c5.
- Versus 7.Bg5: candidates 7...Qb6 (hits b2, keeps Nb5 covered) or 7...h6 8.Bxe7 Qxe7. Do not play 7...Nbc6 automatically.
- Alternative: skip the Caro-Kann and play 1...e5 (known lines in notes/black-ruy-chigorin.md). Stockfish plays 3.Nc3 vs 1...e5 though (notes/black-four-knights.md), so choose one line, prepare it move by move, and use time at moves 5-10.
- Armageddon: Black needs only a draw, so choose the most solid, symmetrical, low-risk setup. Avoid a lone knight on e7 pinned to the queen.

## When lost
- This time Stockfish did NOT repeat. It kept pushing (a4-a5, h4, Rc1, Bf4, Ne5+, b5, g4, Bg3) and mated. Repetition is not reliable, so avoid getting lost in the first place.
