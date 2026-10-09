# Chess memory

Notes (read at start):
- notes/capture-safety.md - pre-move scan + blunder catalogue g1-g54
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Dragon/Alapin/Rauzer as Black
- notes/sicilian-soltis-black.md - 9.Bc4 Soltis (g49,g53,g54; Nh5 timing)
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4 as Black

## Rule 0 - legality & sanity BEFORE sending (3 invalid = forfeit)
- My turn; my pieces only; never echo his move; path clear incl. own blockers (g52 f4 blocked by my own Nf3); destination empty or enemy-held.
- One rejected attempt: do NOT resend it - play a different, trivially legal move, traced twice (g50 Rxc7 illegal -> Nd8).
- Never send a move my own reasoning just rejected (g48 22.Qxd6??). Re-read the destination right before submitting.

## Rule 1 - pre-move scan (5 s, FINAL position)
1. HIS last move first: what does it attack now? (g46 16...Rad8 hit Qd1; 17.Be3?? lost her.) Then my destination: which enemy piece attacks it? Attacked+undefended -> reject; moving vacates guards (g30).
2. Save my attacked/loose piece NOW; with his rook on my 2nd rank, moving a blocker drops the piece behind it (g52 25...Ra2, 26.Bd3? Rxd2). A queen attacked by a rook must MOVE - 'defended' loses Q for R (g42,g46). A loose rook facing his rook is lost.
3. Queen: never on a file/rank/diagonal his rook/bishop/pawn/queen covers. Before any queen capture: my recapturer on the destination (trace the path, blockers kill it) and can his queen take mine there? Q for N/B loses (g48,g50,g51).
4. Captures/trades: count ALL recapturers - rooks on rank/file, PAWNS, QUEENS (g51 25.Rxe5?? dxe5; g36,g42,g47). Before ANY capture, list his mate/one-move threats first (g53 17...Rxd4?? 18.Qxh7#).
5. Knight: never undefended or pawn/bishop/queen-attacked, esp. down material (g44,g46,g51). Nd2?? Qxd2 (g46,g48).
6. Pawn pushes/captures: never onto a defended piece or pawn attack, where a queen gains tempo, or while it guards my piece (g48 21.d6?! Bxd6; g51 28.f3??).
7. Attacking his queen excuses nothing: list my loose pieces/queen first (g45,g50,g51). Never remove the sole guard of h7/h5 while his Q+Rh1 face the open h-file (g49 16...Nxe4?? 17.Rxh5! Qxh7#; g53 16...Ne8?? 17.Qh2! Qxh7#). The ...Nh5 block is safe only once his g-pawn has LEFT g4 (g54 16...Nh5?? 17.gxh5! Qxh7#): on g4 it attacks h5.
8. Lost: defend/trade, 1-15 s, no undefended pieces - KEEP PLAYING: repetition/stalemate can save half a point (g52 K+2P vs K+2B+N drawn by repetition). When winning: make progress, don't shuffle into a third repetition.
9. Time: routine <=15 s, book <=10 s, m1-12 <=20 s. Long thinks never prevented a blunder (g46 0:18, g47 0:36, g48 0:32, g53 46 s routine).

## Openings
- RL as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3. Resolve the centre before his d5; no knight where his d5-pawn kicks it (g44); Qc7 leaves when the c-file opens (g35,g38,g41).
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; keep e3 empty (g33). If my capture opens a file, fix my rook there FIRST (g43). g46: 14.dxe5 opened the d-file under Qd1 (17.Qe2!). Drop the pawn-losing d6?! / Qxd5?? grab (g48,g51). g52: keep Nd2 guarded - 26.Bd3? left it to Rxd2.
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O (g47,g49). Vs 4.c3/5.Qxd4: after ...Bg4 ...Bxf3 his Qxf3 covers e4 - never ...Nxe4; b7 loose once b5 leaves - defend (Qd7/Rb8) or retreat (Bc8); no rook swings (g45). Vs 4.c3 dxc3 (g50): setup fine; after 10.Qxd6 play ...Qb6/...Qc8, never ...Qc7??. Rauzer: 11...gxf6!; no ...f5/...f4 while it guards a knight (g30).
- Soltis 9.Bc4 (g49,g53,g54): 11...Ne5 12.h4 Nc4 13.Bxc4 Rxc4 (SF !) equal; 14.h5 Nxh5!; 15.g4 Nf6 - the f6-knight must never leave h7's guard while Q+Rh1 aim at h7. 16.g5 -> ONLY 16...Nh5! (g4-pawn left, g6 defends h5, knight blocks the h-file). g54: 16.Qh2 (g-pawn STILL on g4!) - 16...Nh5?? 17.gxh5! gxh5 18.Qxh5 Qxh7#; keep Nf6 (h7 recapture) and play ...e6/...Qe8, meet 17.g5 with 17...Nh5 (then safe). Ne8/Nd7 abandon h7 = Qxh7# (g53). After 15.Bh6 do NOT take; 16...Nxe4?? 17.Rxh5! Qxh7#.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; nothing on f5 while his Qf3; no ...Bg4 after h3.
- Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; keep Bc5 defended while Rfc8/Ra8 can come (g42); no queen on a1-net squares after O-O-O (g6); Rxh5 wins once his f6-knight leaves h5 (g49).

## Opponents
- Stockfish 19: ~0 s/move; punishes loose units, queens on attacked lines, loose bishops (g45 Bb7), back-rank. g47: won on my flag. g50: 10...Qc7?? = 11.Qxc7, mate m21.
- Sonnet 5.5: banks clock; takes EVERY free/attacked unit (g48,g51,g52 26...Rxd2). Keep everything defended; move an attacked queen at once. Book line vs my Chigorin. g52: won a knight with ...c4/...Qxb6/...b4/...Ra2, then could NOT mate K+2P in ~19 moves - draw by repetition. Never resign vs him; shuffle fast.
- GPT-6.1 Sol: fast; takes Q-for-R on open files and free knights (g46,g48). Soltis g49/g53/g54 h4-h5 storm: if my f6-knight leaves, Qh2+Rh1 = Qxh7#; 16...Nh5 is safe only once his g-pawn has left g4 (g54: 16.Qh2! then 17.gxh5! punished the premature ...Nh5). No greedy grabs under mate threat; match his speed.
