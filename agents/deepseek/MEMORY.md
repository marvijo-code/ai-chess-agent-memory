# Chess memory

Notes (read at start):
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g56
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Dragon/Alapin/Rauzer as Black
- notes/sicilian-soltis-black.md - 9.Bc4 Soltis (g49,g53,g54,g55)
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- My turn; my pieces only; never echo his move; path clear incl. own blockers; destination empty or enemy-held.
- One rejected attempt: do NOT resend it - play a different, trivially legal move, traced twice (g50 Rxc7 illegal -> Nd8; g56 2 illegal tries: m20 71 s, m25 65 s).
- Never send a move my own reasoning just rejected (g48 22.Qxd6??). Re-read the destination before submitting.

## Rule 1 - pre-move scan (5 s, FINAL position; overrides any plan)
1. HIS last move first: what does it attack now? (g46 16...Rad8 hit Qd1; 17.Be3?? lost her.) Then name every enemy piece that attacks my destination, tracing its path; attacked+undefended -> reject; moving vacates guards (g30). A note asking 'is X safe?' = REJECT until the attacker's path is written (g56: wrote 'check Be7' then 19.Qd6?? Bxd6).
2. His KING attacks the 8 squares around it: never an undefended piece there (g55 27...Rd2?? Kxd2).
3. Save my attacked/loose piece NOW; a queen attacked by a rook must MOVE - 'defended' still loses Q for R (g42,g46); his rook on my 2nd rank: moving a blocker drops the piece behind it (g52 26.Bd3? Rxd2).
4. Pawn pushes/recaptures: is this pawn the SOLE guard of my piece? (g55 19...gxf5?? moved g6, Nh5's only defender; 20.Rxh5.) Never onto a defended piece/pawn attack, with a queen tempo, or while it guards my piece (g48,g51).
5. Queen: before moving/capturing, name every enemy piece covering the destination (g56 19.Qd6?? - Be7 one step + Qc7; undefended; Bxd6) and my recapturer if his queen can take mine there. Q for N/B loses (g48,g50,g51).
6. Captures/trades: count ALL recapturers - rooks, PAWNS, QUEENS (g51 25.Rxe5?? dxe5); list his mate threats first (g53 17...Rxd4?? 18.Qxh7#); attacking his queen excuses nothing (g45,g50,g51).
7. H-file mate: never move h7/h5's sole guard while his Q+Rh1 aim there (g49,g53); ...Nh5 blocks only once his g4-pawn has left (g54,g55).
8. Knight: never undefended or attacked by pawn/bishop/queen (g44,g46,g51). g56 16.Nc4??: his b5-PAWN attacked c4 - bxc4 won N for P; 'defended' does not save a piece from a pawn.
9. Down material: defend/trade, 5-15 s, no undefended pieces, keep playing (repetition/stalemate = half point, g52); when winning make progress, never a third repetition.
10. Time: routine <=15 s, book <=10 s, m1-12 <=20 s, m13+ <=25 s; <3 min -> <=5 s; <1 min -> 1-2 s. Long thinks never prevented a blunder (g46,g47,g48,g53,g55; g56 1:34 on 14.Bb3, then 19.Qd6??, ended 2:14 vs 16:12).

## Openings
- RL as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; resolve the centre before his d5; move Qc7 out when the c-file opens (g35,g38,g41).
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3 (keep e3 empty, g33); rook to the file my capture opens (g43); no d6?!/Qxd5?? (g48,g51); keep Nd2 guarded (g52). g56: after 15.dxe5 dxe5 play a quiet move (Nf1 then Be3) - no Nc4: his b5-pawn attacks c4.
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O. No ...Nxe4 while his Qf3 covers e4 (g47); b7 loose once b5 leaves - defend/retreat (g45); after 10.Qxd6 play ...Qb6/...Qc8, never ...Qc7?? (g50); Rauzer 11...gxf6! (g32).
- Soltis 9.Bc4: 14.h5 Nxh5! 15.g4 Nf6; 16.g5 -> ONLY 16...Nh5; 16.Qh2 with g4 on: NOT ...Nh5 (17.gxh5!); keep the f6/h5 knight on h7's guard; g55: 19...gxf5?? dropped h5's sole guard (20.Rxh5). Detail: notes/sicilian-soltis-black.md.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended (g42); no queen on a1-net squares (g6).

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked lines, loose bishops, back-rank; g50 10...Qc7?? = 11.Qxc7 mate m21; g47 won on my flag.
- Sonnet 5.5: banks clock (16:19 left at m33); takes EVERY free/attacked unit (g56 19...Bxd6 in 8 s; g48,g51,g52 26...Rxd2; g55 20.Rxh5). Keep everything defended; move an attacked queen at once; vs my Chigorin he plays book and waits for my blunder. g52: 2B+N up, failed to mate K+2P ~19 moves = 1/2 threefold. Never resign vs him; 1-3 s.
- GPT-6.1 Sol: fast; takes Q-for-R on open files, free knights (g46,g48). Soltis h4-h5 storm: Qh2+Rh1 = Qxh7# once my f6-knight leaves; ...Nh5 only once his g4-pawn has left (g54). No greedy grabs under mate threat; match his speed.
