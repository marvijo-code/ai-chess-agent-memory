# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes: notes/ruy-lopez-black.md (Ruy Lopez Closed as Black); notes/ruy-lopez-white.md (RL Closed as White, Chigorin); notes/four-knights-black.md (Four Knights 4.Bb5 Bb4; the b6-bishop trap).

## Rule 1 - capture safety (the cause of the game 1, 2 and 3 losses)
- Before EVERY capture: list enemy pieces/pawns that can recapture on the target square; count material after the exchange. I keep missing pawn recaptures.
- Blunders: g1 12...Nxb2?? Bxb2; g2 (as White) 16.a3?? ...Nxc2 17.Qxc2 Qxc2 (c2 defended by Qc7); g3 14...Bxd4?? cxd4 (bishop for pawn, game over) and 19...Qxe4?? Rxe4 (Re3 guarded e4; queen for bishop).
- Never give a piece for one pawn (Bxd4-cxd4, Bxf3-Rxf3, Nxb2): down 2 for nothing.
- After capturing, scan again: can my capturing piece be captured next move (open lines, undefended squares)?

## Rule 2 - piece safety
- Do not move a piece to a square enemy pieces attack unless it is defended or I have a forcing follow-up (g3 15...Ne4 -> 16.Bxe4, no recapture, knight gone).
- If my attacked piece has no safe square (g3 Bb6 hit by Nc4: a5/c5/d4/e3 covered, a7/c7 own pawns, c7-pawn blocks b6-d8): free it by attacking the attacker (...b5! vs Nc4) or allow an equal trade (Nxb6 cxb6); never a cash-in capture of a defended pawn.
- Before pawn moves and king-area moves, scan c2, b2, d3, e4, f2 for knight jumps/pins, and open files for enemy rooks/queens.

## Rule 3 - time (TC 600+10; g3: ~28s/move avg, ended with 69s vs opponent 14:40)
- Opening/theory <=10s; routine moves <=15s; only 2-3 decisions 30-45s. The 30-40s searches on simple moves 4-14 and the 54s on 17...Bxf3 were waste.
- Once clearly lost (down 2+ pieces / mate near): <=5s per move, king safety only; g3 moves 20-26 burned ~4 min for nothing.
- Check the clock every 5 moves; verify piece+square before submitting (illegal attempts cost 30-100s).

## Openings
- RL Closed as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then Chigorin or Breyer; keep f7 covered; ...Nxb2 only if a rook already covers b2. Details: notes/ruy-lopez-black.md.
- RL Closed as White: Chigorin 9.h3 Na5 10.Bc2 c5...; at 15...Nb4 play 16.Rac1 or 16.Bb1; 16.a3?? loses to ...Nxc2 (c2 undefended). Details: notes/ruy-lopez-white.md.
- Four Knights as Black after 4.Bb5 Bb4: fine through move 14; when Nc4 hits b6, fix it with ...b5 (Nxb6 cxb6 = equal). Details: notes/four-knights-black.md.

## Opponents
- Stockfish 19 (ladder): ~0s/move, banks clock, takes any loose piece instantly, never gives material back. Vs it: every piece defended, no unsafe captures, no hope of counter-blunders.
- Sonnet 5.5: fast, sound; stay ahead on clock. GPT-6.1 Sol: spots hanging pieces instantly; keep everything defended.

## Principles
- No pieces for pawns; no queen for bishop/knight; no rook takes without a pin or forcing reason.
- After a blunder: stabilize (defend loose pieces, block), do not panic-capture; when worse trade pieces; when dead-lost play fast and lose nothing more.
