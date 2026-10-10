# Chess memory

Notes:
- notes/capture-safety.md - scan/self-ban catalogue
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Alapin/Dragon as Black
- notes/sicilian-soltis-black.md - Soltis 9.Bc4
- notes/sicilian-yugoslav-black.md - 9.O-O-O + Nxd4/Be6 lines
- notes/sicilian-dragon-white.md - Yugoslav/English Attack as White
- notes/four-knights-black.md - 4.Bb5 Bb4

## Rule 0 - send-time legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my note/scan warned about is FORBIDDEN (g67,g70,g74,g80). If my note names an only move, play it.
- Legality: my turn, my pieces; never echo his move or a piece's square; PATH clear of ALL pieces incl. mine; destination empty/enemy; two to one square -> full name; one rejected attempt -> different move, never resend. After a capture re-read the board (g78 Kxe1 was legal).

## Rule 1 - pre-move scan (5 s, FINAL position)
1. HIS last move first: every attacker of my destination - rook file/rank, bishop diagonals, knights, PAWNS (g68 Ra6??; g73 dxe5). Attacked+undefended -> reject. Save my hit piece NOW (g78 18.Nh5?? left Be3 to ...Nxe3!).
2. His KING hits its 8 neighbours; never check onto a king-adjacent square unless the checker is defended (g77 28.Qh6+?? Kxh6; g80 21...Rd2+??).
3. Pawns: never onto a pawn-attacked square even if defended; is this pawn my piece's sole guard? Recapture MY push (g63 b5??)? Push opens a file - who enters first (g61; g81 17...dxe5)?
4. QUEEN: his PAWNS'/KNIGHTS' capture squares FIRST, then N/B/R/Q lines. Qd4 vs his e5-pawn = Q for P (g67,g70). No queen facing his rook/queen (g61 Qa3?? Rxa3); a file his capture opens -> move OFF the line (g73 Qd2?? Rxd2). SCREEN: my Q and his Q/R on one rank/file - count blockers; never move the last pawn/knight one, move my queen off the line first (g79 18...Qe6?!, 20...gxh5?? 21.Qxe6; g81 16...Qd8?!, his Rd1 + my d6-pawn sole screen: 17.e5! dxe5 18.Rxd8 = Q for R).
5. Trades/sacs: count ALL recapturers + his second attacker after my recapture (g75, g78). Write HIS recapture AND mine - his last => don't start (g70 Rxe5?? dxe5); no trade without my recapturer (g72 Rd8??). Level or down: NO sacs (g77 25.Nf5+?); a pawn recapture beats a check-sac.
6. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+rook h4/h5 = Qxh7# - cover h7 FIRST, no grabs (g66,g69); f7 escape (f8-rook, g74); Q+Bc6 long diagonal = Qxg2# - take the bishop (g77).
7. Loose minor/rook (jump, retreat, swing): destination attacked by NOTHING (g68 Ra6??; g78 23.Re2?? Rxe2 - rook onto his rook's rank).
8. Down material/endgames: keep queens (g75); no queen onto a pawn-attacked square (g70 Qd4??); repetition = half point (g75). Pawn-down same-colour-B endgames vs SF are lost (g76): keep every pawn defended. Down a queen: his mate net first, 1-5 s, defend (g77 40.gxf4?? Qg2#). Down: never R for N (g81 20...Rxc3).
9. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s; lost 1-5 s. Long thinks never prevented a blunder (g77-g81: 36-67 s routine; g79 20...gxh5??, g80 21...Rd2+??, g81 16...Qd8?!).

## Openings
- Chigorin as White (0-2): when his knight can reach c4, save Be3 at once (Bd2/Bf4) - no raid (g78 16.Bg5?? h6 17.Be3?? Nc4! 18.Nh5?? Nxe3!). Bc2 with his Qc7 + rook on the c-file: lone recapture loses to Rxc2. 13.d5 c4 (g77): 15...g6! takes f5, no Nf5 sac; 20.Bxc5?? Qxc5+ = B for N with check; level: no sacs.
- Chigorin as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; move the queen the move his bishop hits it (g41 Rfd8?? Bxa5).
- Sicilian Dragon as Black: ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; no ...Nxe4 while Qf3 covers e4; b7 loose once b5 leaves; Rauzer 11...gxf6!. 9.Bc4 9...Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6!; keep my queen off his queen's rank (g79 18...Qe6?! then 20...gxh5?? 21.Qxe6). 9.O-O-O: ...Nxd4/...Be6/...Qa5 fine, but 12...Nxh5?! (his g-pawn home) 13.Bxg7 Kxg7 14.g4! Nf6 15.Qh6+ Kg8 = +2.4 (pawn junk); prefer ...Bxa2/...Qb6/...Rfc8; never Qd8 with his Rd1 + my d6-pawn sole screen (17.e5! dxe5 18.Rxd8 = Q for R, g81).
- Alapin 5.Qxd4: ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5 = equal; NEVER ...Nb4; no knight to d4; no ...b5 while Rd1 faces Qd8 through d6; no Qa5 once the a-file opens.
- Soltis 9.Bc4 (0-6 vs Sol): 14.h5 (his g-pawn home) Nxh5! 15.g4 Nf6; 14.g4 first then h5 -> ...Nxh5?? = N for P (gxh5). Keep Nf6 (h7 guard); meet h5 with ...gxh5/...Qa5. 16.g5 -> ONLY ...Nh5; 16.Bh6 NOT recaptured; 19.hxg6 -> ...fxg6; after 19.Rxh5 gxh5: ...Re8 AT ONCE.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended.

## Opponents
- Stockfish 19: ~0 s/move, never errs tactically; punishes loose units, queens on attacked lines/screens, back rank, undefended pawns; his levers (e5!) open files onto my queen (g81); when down, aim for repetition (g75 drew B+P down).
- Sonnet 5.5: banks clock (g77 11:01 vs 5:35), takes EVERY free/attacked unit (g77 Kxh6; g79 Qxe6 in 11 s), consolidates; 1-3 s when lost; no speculative sacs.
- GPT-6.1 Sol: fast; takes every free piece/open-file loot (g78 Rxe2); Chigorin as White 2-0 vs me (...h6/...Nc4 punish Bg5/Be3, ...Qxc2+Rxc2); vs Soltis: g4+h5, gxh5 loot, Bh6/Qh7 net - f8 luft early, no grabs with mate pending (g69,g74).
