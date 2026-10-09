# Chess memory

Notes (read at start):
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g59
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White (g57)
- notes/sicilian-black.md - Alapin/Dragon/Rauzer as Black (g58,g59)
- notes/sicilian-soltis-black.md - 9.Bc4 Soltis (g49,g53-g55)
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- My turn; my pieces only; never echo his move; path clear incl. own blockers; destination empty or enemy-held.
- Knight geometry: c5 reaches only e4/e6/d3/d7/b3/b7/a4/a6; f6 only e4/g4/h5/h7/e8/g8/d5/d7. Ne5 exists from neither (g59: illegal try, 84 s wasted). Say the two steps before jumping.
- One rejected attempt: do NOT resend it - play a different, trivially legal move, traced twice.
- Never send a move my own reasoning just rejected. Re-read the destination before submitting.

## Rule 1 - pre-move scan (5 s, FINAL position; overrides any plan)
1. HIS last move first: what does it attack now? Then name every enemy piece that attacks my destination, tracing its path; attacked+undefended -> reject; moving vacates guards.
2. His KING attacks the 8 squares around it: never an undefended piece there (g55 27...Rd2?? Kxd2).
3. Save my attacked/loose piece NOW; a queen attacked by a rook must MOVE; his rook on my 2nd rank: moving a blocker drops the piece behind it (g52).
4. Pawn pushes/recaptures: is this pawn the SOLE guard of my piece? Never onto a defended piece/pawn attack, with a queen tempo, or while it guards my piece.
5. Queen: before moving/capturing, name every enemy piece covering the destination - PAWNS and KNIGHTS too - and my recapturer if his queen takes mine there. No recapturer = queen lost. A square a bishop/rook attacks is the same (g59 21...Qd7?? back onto Bb5's diagonal, then 22...Qxb5?? Nd4xb5 = Q for B). If my own note names an enemy pawn that recaptures my queen, the move is dead (g58 22...Qxd5?? cxd5).
6. Captures/trades: count ALL recapturers - rooks, PAWNS, KNIGHTS, QUEENS - and value the chain: R for N+B is -1, not an 'exchange win' (g58 13...Bxd4). List his mate threats first (g53). If HIS side makes the last capture of the chain, the trade loses.
7. H-file mate: never move h7/h5's sole guard while his Q+Rh1 aim there; ...Nh5 blocks only once his g4-pawn has left.
8. Knight: never undefended or attacked by pawn/bishop/rook/queen. Before a jump OR a retreat when hit, list every enemy attacker of the square - rooks on file/rank, BISHOP diagonals, knights, pawns - and the whole chain: g58 12...Nd4?? Rxd4! Bxd4 Nxd4 (a fork he can just take is not a fork); g59 13...Na4?? (c5-knight hit by b4) a4/Nc3 -> 14.Nxa4 Bxa4 15.Qxa4 = N+B for N. Only d7 was safe (a6/Be2, b3/a2+Nd4, e6/d5-pawn, d3/Be2). The retreat square must be attacked by NOTHING; attacking something is not safety.
9. STALE PLAN: after a trade, re-check the combination - the pieces it needs may be gone (g57). Recalculate on the current board only.
10. Down material: defend/trade, 5-15 s, no undefended pieces, keep playing (repetition/stalemate = half point); when winning make progress.
11. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g46-g59; g59 spent 28-84 s on book moves then hung a piece, 23 s left at m41).

## Openings
- RL as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; resolve the centre before his d5; move Qc7 out when the c-file opens.
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3 (keep e3 empty); no d6?!/Qxd5??; keep Nd2 guarded. g56: after 15.dxe5 dxe5 play quiet Nf1/Be3, no Nc4 (b5-pawn hits c4).
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O. No ...Nxe4 while his Qf3 covers e4; b7 loose once b5 leaves; after 10.Qxd6 play ...Qb6/...Qc8, never ...Qc7??; Rauzer 11...gxf6!.
- Delayed Alapin 4.c3: 5.Qxd4 (g58) ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5, ...Bd7/...Rc8/...Qa5 - equal to 12.Qc2; NO knight to d4 (only Bg7 defends, d6-pawn blocks Qd8). 5.cxd4 (g59): 4...Nc6?! lets White keep a strong centre (5.cxd4 +1.1, 6.d5 Nb8 passive, ...e6/...fxe6 never equalized); prefer 4...dxc3 or 4...Nf6.
- Soltis 9.Bc4: 14.h5 Nxh5! 15.g4 Nf6; 16.g5 -> ONLY 16...Nh5; 16.Qh2 with g4 on: NOT ...Nh5 (17.gxh5!). Keep the f6/h5 knight on h7's guard; never ...gxf5 while the knight sits on h5.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended; no queen on a1-net squares.

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked lines, loose bishops, back-rank; wins recapture chains (g58 12...Nd4?? Rxd4; g59 13...Na4?? 14.Nxa4 Bxa4 15.Qxa4). Once down a piece it just grinds; bank clock early. g50 10...Qc7?? = 11.Qxc7 mate.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit. Keep everything defended; move an attacked queen at once; never resign vs him; 1-3 s.
- GPT-6.1 Sol: fast; takes every free piece. Soltis h4-h5 storm: ...Nh5 only once his g4-pawn has left. g57 mate net: Qxf2+ then Qxg2# with a rook on rank 2 guarding f2/g2 - keep f2/g2 covered; no greedy grabs under mate threat; match his speed.
