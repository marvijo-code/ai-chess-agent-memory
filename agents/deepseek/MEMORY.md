# Chess memory

Notes (read at start):
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g57
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White (g57)
- notes/sicilian-black.md - Dragon/Alapin/Rauzer as Black
- notes/sicilian-soltis-black.md - 9.Bc4 Soltis (g49,g53,g54,g55)
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- My turn; my pieces only; never echo his move; path clear incl. own blockers (g57 Be3 illegal: Nd2 still on d2); destination empty or enemy-held.
- One rejected attempt: do NOT resend it - play a different, trivially legal move, traced twice (g50, g56; g57 m16 = 1:44 incl. 1 illegal try).
- Never send a move my own reasoning just rejected (g48 22.Qxd6??). Re-read the destination before submitting.

## Rule 1 - pre-move scan (5 s, FINAL position; overrides any plan)
1. HIS last move first: what does it attack now? (g46 16...Rad8 hit Qd1.) Then name every enemy piece that attacks my destination, tracing its path; attacked+undefended -> reject; moving vacates guards (g30). 'Is X safe?' = REJECT until the attacker's path is written (g56).
2. His KING attacks the 8 squares around it: never an undefended piece there (g55 27...Rd2?? Kxd2).
3. Save my attacked/loose piece NOW; a queen attacked by a rook must MOVE - 'defended' still loses Q for R (g42,g46); his rook on my 2nd rank: moving a blocker drops the piece behind it (g52).
4. Pawn pushes/recaptures: is this pawn the SOLE guard of my piece? (g55 19...gxf5?? 20.Rxh5.) Never onto a defended piece/pawn attack, with a queen tempo, or while it guards my piece (g48,g51).
5. Queen: before moving/capturing, name every enemy piece covering the destination (g56 Qd6?? - Be7+Qc7) AND my recapturer if his queen can take mine there. No recapturer = queen lost (g48,g50,g51; g57 24.Qxd4?? Qxd4).
6. Captures/trades: count ALL recapturers - rooks, PAWNS, QUEENS (g51 25.Rxe5?? dxe5); list his mate threats first (g53).
7. H-file mate: never move h7/h5's sole guard while his Q+Rh1 aim there (g49,g53); ...Nh5 blocks only once his g4-pawn has left (g54,g55).
8. Knight: never undefended or attacked by pawn/bishop/queen (g44,g46,g51). g56 16.Nc4?? bxc4; g57 23.Nd4?? exd4 took my last knight; 'defended' does not save it from a pawn.
9. STALE PLAN: after a trade, re-check the combination - the pieces it needs may be gone. g57: traded B on c5 (22.Bxc5), then 23.Nd4?? still assumed 24.Bxd4 (no bishop) = lost N, then Q. Recalculate on the current board only.
10. Down material: defend/trade, 5-15 s, no undefended pieces, keep playing (repetition/stalemate = half point, g52); when winning make progress, never a third repetition.
11. Time: routine <=15 s, book <=10 s, m1-12 <=20 s, m13+ <=25 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g46-g56; g57 1:44+60 s routine m16-20, ended 5:06 vs 16:02).

## Openings
- RL as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; resolve the centre before his d5; move Qc7 out when the c-file opens (g35,g38,g41).
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3 (keep e3 empty, g33); no d6?!/Qxd5?? (g48,g51); keep Nd2 guarded (g52). g56: after 15.dxe5 dxe5 play quiet Nf1/Be3, no Nc4 (b5-pawn hits c4). g57: 14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Be3?! was fine to 21.exf5! - lost only via Rule 1.8/9 (m23-25).
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O. No ...Nxe4 while his Qf3 covers e4 (g47); b7 loose once b5 leaves (g45); after 10.Qxd6 play ...Qb6/...Qc8, never ...Qc7?? (g50); Rauzer 11...gxf6! (g32).
- Soltis 9.Bc4: 14.h5 Nxh5! 15.g4 Nf6; 16.g5 -> ONLY 16...Nh5; 16.Qh2 with g4 on: NOT ...Nh5 (17.gxh5!); keep the f6/h5 knight on h7's guard; g55 19...gxf5?? dropped h5's sole guard (20.Rxh5).
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended (g42); no queen on a1-net squares (g6).

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked lines, loose bishops, back-rank; g50 10...Qc7?? = 11.Qxc7 mate m21; g47 won on my flag.
- Sonnet 5.5: banks clock (16:19 at m33); takes EVERY free/attacked unit (g56,g48,g51,g52,g55). Keep everything defended; move an attacked queen at once; g52: 2B+N up failed to mate K+2P ~19 moves = 1/2. Never resign vs him; 1-3 s.
- GPT-6.1 Sol: fast (~15:56 left at m28); takes every free piece (g57 24...Qxd4 in 5 s, 25...Rxc2 in 13 s). Soltis h4-h5 storm: ...Nh5 only once his g4-pawn has left (g54). g57 mate net: Qxf2+ then Qxg2# with a rook on rank 2 guarding f2/g2 (Kxf2/Kxg2 illegal) - keep f2/g2 covered, no queen entry near my king. No greedy grabs under mate threat; match his speed.
