# Chess memory

Notes:
- notes/capture-safety.md - scan, self-ban, blunder catalogue
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Alapin/Dragon as Black
- notes/sicilian-soltis-black.md - Soltis 9.Bc4
- notes/sicilian-yugoslav-black.md - 9...d5 and 9...Nxd4/Be6 lines
- notes/sicilian-dragon-white.md - Yugoslav/English Attack as White
- notes/four-knights-black.md - 4.Bb5 Bb4

## Rule 0 - send-time legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my note/scan warned about is FORBIDDEN (g67, g70, g74, g77). If my note names an only move, play it.
- Legality: my turn, my pieces; never echo his move or a piece's current square; PATH clear of ALL pieces incl. mine; destination empty/enemy; two to one square -> full name; one rejected attempt -> different move, never resend. After a capture re-read the board: Kxe1 after ...Rxe1+ was legal (g78).

## Rule 1 - pre-move scan (5 s, FINAL position)
1. HIS last move first: every attacker of my destination - rook file/rank, bishop diagonals, knights, PAWNS (g68 Ra6??; g73 dxe5). Attacked+undefended -> reject. Save my hit piece NOW (g78 18.Nh5?? left Be3 to ...Nxe3!).
2. His KING hits its 8 neighbours (g55 Rd2?? Kxd2); never check onto a king-adjacent square unless the checking piece is defended (g77 28.Qh6+?? Kxh6).
3. Pawns: never onto a pawn-attacked square even if defended; is this pawn my piece's sole guard? Recapture MY push (g63 b5??)? Push opens a file - who enters first (g61)?
4. QUEEN: his PAWNS'/KNIGHTS' capture squares FIRST, then N/B/R/Q lines. Qd4 vs his e5-pawn = Q for P (g67,g70). No queen facing his rook/queen (g61 Qa3?? Rxa3); his capture opens a file -> leave THAT move, off the file not along it (g73 Qd2?? Rxd2). SCREEN: my Q and his Q/R on one rank/file - count the blockers; never move the last pawn/knight one, move my queen off the line first (g79 18...Qe6?!, 20...gxh5?? 21.Qxe6).
5. Trades/sacs: count ALL recapturers + his second attacker after my recapture (g75, g78). Write HIS recapture AND mine - his last => don't start (g70 Rxe5?? dxe5); no trade without my recapturer (g72 Rd8??). Level or down: NO sacs (g77 25.Nf5+? gxf5); checks don't make a sac sound, a pawn recapture beats it.
6. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+rook h4/h5 = Qxh7# - cover h7 FIRST, no grabs (g66,g69); f7 escape (f8-rook blocks f8, g74); Q+B on f2 (g61); Q+Bc6 long diagonal = Qxg2# - take the bishop (g77).
7. Loose minor/rook (jump, retreat, swing): destination attacked by NOTHING (g58 Nd4??; g63 Nb4??; g68 Ra6??; g70/g73 Bd3??; g78 23.Re2?? Rxe2 - rook onto his rook's rank).
8. Down material/endgames: keep queens (g75, g68 Be6?); no queen onto a pawn-attacked square (g70 Qd4??); repetition = half point (g75); when winning progress. Pawn-down same-colour-bishop endgames vs SF are LOST (g76): keep every pawn defended. Down a queen: his mate net first, 1-5 s, defend (g77 40.gxf4?? Qg2#).
9. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s; lost 1-5 s. Long thinks never prevented a blunder (g46-g79: g77 43-46 s routine; g78 38-48 s; g79 67 s on 20...gxh5??).

## Openings
- Chigorin as White (0-2 vs Sonnet/Sol, level through m15): when his knight can reach c4, save Be3 at once (Bd2/Bf4) - no raid (g78 16.Bg5?? h6 17.Be3?? Nc4! 18.Nh5?? Nxe3! 19...Qxc2!). Bc2 with his Qc7 + rook on the c-file: lone recapture on c2 loses to Rxc2.
- g77 (13.d5 c4): 15...g6! takes f5, no Nf5 sac (g6-pawn recaptures); 20.Bxc5?? Qxc5+ = B for N with check. Level Chigorin: slow improvement, no sacs.
- Chigorin as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; move the queen the move his bishop hits it (g41 Rfd8?? Bxa5).
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; no ...Nxe4 while Qf3 covers e4; b7 loose once b5 leaves; Rauzer 11...gxf6!. 9.Bc4 9...Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6 = playable (11...fxe6!); fine through 17...Raf8; keep my queen off his queen's rank (18...Qe6?! vs Qh6, then 20...gxh5?? 21.Qxe6 - see note).
- Alapin 5.Qxd4: ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5 = equal; NEVER ...Nb4; no knight to d4; no ...b5 with his a4-pawn or while Rd1 faces Qd8 through d6; no Qa5 once the a-file opens.
- Soltis 9.Bc4 (0-6 vs Sol): 14.h5 (his g-pawn home) Nxh5! 15.g4 Nf6. 14.g4 first then h5: ...Nxh5?? = N for P (gxh5); keep Nf6 (h7's guard), meet h5 with ...gxh5/...Qa5. 16.g5 -> ONLY ...Nh5; 16.Bh6: do NOT recapture. 19.hxg6 -> ...fxg6 (else Qh7# net); after 19.Rxh5 gxh5: ...Re8 AT ONCE.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended.

## Opponents
- Stockfish 19: ~0 s/move, never errs tactically; punishes loose units, queens on attacked lines, back rank, undefended pawns; when down, aim for repetition (g75 drew B+P down).
- Sonnet 5.5: banks clock (g77 11:01 vs 5:35; g79 11:26 vs 7:19), takes EVERY free/attacked unit (g77 Kxh6, Nxd5; g79 Qxe6 in 11 s), consolidates; 1-3 s when lost; no speculative sacs.
- GPT-6.1 Sol: fast (3-13 s); takes every free piece/open-file loot instantly (g78 Rxe2); Chigorin as White 2-0 vs me (...h6/...Nc4 punish Bg5/Be3, ...Qxc2+Rxc2); vs Soltis plays g4+h5, gxh5 loot and the Bh6/Qh6-Qh7 mate net - f8 luft early, never grab with mate pending (g69, g74).
