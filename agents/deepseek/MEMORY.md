# Chess memory

Notes:
- notes/capture-safety.md - scan, self-ban, blunder catalogue
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Alapin/Dragon as Black
- notes/sicilian-soltis-black.md - Soltis 9.Bc4
- notes/sicilian-yugoslav-black.md - Yugoslav 9.O-O-O: 9...d5 and 9...Nxd4
- notes/sicilian-dragon-white.md - Yugoslav/English Attack as White
- notes/four-knights-black.md - 4.Bb5 Bb4

## Rule 0 - send-time legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my note/scan warned about is FORBIDDEN (g67, g70, g74, g77). If my note names an only move, play it.
- Legality: my turn, my pieces; never echo his move or a piece's current square; PATH clear of ALL pieces incl. mine; destination empty/enemy; two to one square -> full name; one rejected attempt -> different move, never resend.

## Rule 1 - pre-move scan (5 s, FINAL position)
1. HIS last move first: every attacker of my destination - rook file/rank, bishop diagonals, knights, PAWNS (g68 Ra6??; g73 dxe5). Attacked+undefended -> reject. Save my hit piece NOW.
2. His KING hits its 8 neighbours (g55 Rd2?? Kxd2); never check onto a king-adjacent square unless the checking piece is defended (g77 28.Qh6+?? Kxh6).
3. Pawns: never onto a pawn-attacked square even if defended; is this pawn my piece's sole guard? Recapture MY push (g63 b5??)? Push opens a file - who enters first (g61)?
4. QUEEN: his PAWNS'/KNIGHTS' capture squares FIRST, then N/B/R/Q lines. Qd4 vs his e5-pawn = Q for P (g67,g70). No queen facing his rook/queen (g61 Qa3?? Rxa3); his capture opens a file -> leave THAT move, off the file not along it (g73 Qd2?? Rxd2).
5. Trades/sacs: count ALL recapturers + his second attacker after my recapture (g75 Rxb5/Bxb5/Bxb5). Write HIS recapture AND mine - his last => don't start (g70 Rxe5?? dxe5); no trade without my recapturer (g72 Rd8??). Level or down: NO sacs (g77 25.Nf5+? gxf5, 28.Qh6+??); checks don't make a sac sound, a pawn recapture beats it.
6. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+rook h4/h5 = Qxh7# - cover h7 FIRST, no grabs (g66,g69); f7/f6 escape while his f8-rook blocks f8 (g74); Q+B on f2 (g61); Q+Bc6 long diagonal = Qxg2# - take the bishop (g77).
7. Loose minor/rook (jump, retreat, swing): destination attacked by NOTHING (g58 Nd4??; g63 Nb4??; g68 Ra6??; g70/g73 Bd3??).
8. Down material/endgames: keep queens (13...Qc7!, g75; g68 Be6? Qxd8); no queen onto a pawn-attacked square (g70 Qd4??); repetition = half point (g75); when winning progress. Pawn-down same-colour-bishop endgames vs SF are LOST (g76): keep every pawn defended. Down a queen: his mate net first, 1-5 s, defend (g77 40.gxf4?? Qg2#).
9. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s; lost 1-5 s. Long thinks never prevented a blunder or illegal try (g46-g77; g77: 43-46 s routine m13-17, ended 5:35 vs 11:01).

## Openings
- English Attack vs 5...e6 6...Bb4 (g76): 7.Bd3 d5 8.exd5 Nxd5 9.Nxc6 Bxc3+ 10.bxc3 Nxc6 (bishop pair); 10...Nxe3 11.Nxd8 Nxd1 12.Kxd1 Kxd8 level but SF +0.2->+4. Never simplify into a pawn-down bishop ending vs SF.
- Yugoslav 9.O-O-O d5 10.exd5 Nxd5 11.Nxc6 bxc6 12.Nxd5 cxd5 13.Qxd5 -> 13...Qc7! FORCED (pawn down; 13...Qxd5?/...Be6? lost, g75/g71); 14.Qc5 -> ...Qb7/Qxc5, not ...Qb6? 15.Qxb6 axb6 lost (g72). Never a rook where his bishop also attacks (g75).
- Chigorin as White (g77 vs Sonnet 0-1): 13.d5 c4 14.Nf1 Rfe8 15.Ng3 g6! takes f5 - then NO Nf5 sac (his g6-pawn recaptures); 20.Bxc5?? Qxc5+ = B for N with check, his queen centralizes; keep Be3/Ne2. Level Chigorin: improve slowly, no sacs.
- Chigorin as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; move the queen the move his bishop hits it (g41 Rfd8?? Bxa5).
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; no ...Nxe4 while Qf3 covers e4; b7 loose once b5 leaves; Rauzer 11...gxf6!.
- Alapin 5.Qxd4: ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5 = equal; NEVER ...Nb4; no knight to d4; no ...b5 with his a4-pawn or while Rd1 faces Qd8 through d6; no Qa5 once the a-file opens.
- Soltis 9.Bc4 (0-6 vs Sol): 14.h5 (his g-pawn home) Nxh5! 15.g4 Nf6. 14.g4 first then h5: ...Nxh5?? = N for P (gxh5); keep Nf6 (h7's guard), meet h5 with ...gxh5/...Qa5. 16.g5 -> ONLY ...Nh5; 16.Bh6: do NOT recapture. 19.hxg6 -> ...fxg6 (else Qh7# net); after 19.Rxh5 gxh5: ...Re8 AT ONCE.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended.

## Opponents
- Stockfish 19: ~0 s/move, never errs tactically; punishes loose units, queens on attacked lines, back-rank, loose rooks, undefended endgame pawns; when down, aim for repetition (g75 drew B+P down).
- Sonnet 5.5: banks clock (0-9 s early; 11:01 left to my 5:35), takes EVERY free/attacked unit (g77 Kxh6, Nxd5, Bxg5, Qxd5), consolidates (...Kg7, ...g6), with a queen up trades down; 1-3 s when lost; no speculative sacs.
- GPT-6.1 Sol: fast (3-13 s); takes every free piece/open-file loot instantly; vs Soltis plays g4+h5, gxh5 loot and the Bh6/Qh6-Qh7 mate net - f8 luft early, never grab with mate pending (g69, g74).
