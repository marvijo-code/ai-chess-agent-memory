# Chess memory

Notes:
- notes/capture-safety.md - scan, self-ban, blunder catalogue
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Alapin/Dragon as Black
- notes/sicilian-soltis-black.md - Soltis 9.Bc4
- notes/sicilian-yugoslav-black.md - Yugoslav 9.O-O-O: 9...d5 and 9...Nxd4
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4

## Rule 0 - send-time legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my note/scan warned about is FORBIDDEN (g67, g70, g74, g75 13...Qxd5?? while my note said '13...Qc7! only'). If my note names an only move, play it. Verify the SENT move contains no danger.
- Legality: my turn, my pieces; never echo his move or repeat a piece's square; PATH clear of ALL pieces incl. mine (g70 Be3 blocked by Nd2); destination empty/enemy; two to one square -> full name; one rejected attempt -> different move, never resend.

## Rule 1 - pre-move scan (5 s, FINAL position)
1. HIS last move first: every enemy attacker of my destination - rook file/rank, bishop diagonals, knights, PAWNS (g68 Ra6??; g73 dxe5). Attacked+undefended -> reject.
2. His KING attacks its 8 neighbours (g55 Rd2?? Kxd2); his rook on my 2nd rank: moving a blocker drops the piece behind. Save my hit piece NOW.
3. Pawns: never onto a pawn-attacked square even if defended; is this pawn my piece's sole guard? Recapture MY push (g63 b5??)? Push opens a file - who enters first (g61)?
4. QUEEN: his PAWNS'/KNIGHTS' capture squares FIRST, then N/B/R/Q lines. Qd4 next to his e5-pawn = Q for P (g67,g70). No queen facing his rook/queen (g61 Qa3?? Rxa3), no forced trade (g72 ...Qb6?). His capture opens a file -> my queen leaves THAT move, off the file not along it (g73 Qd2?? Rxd2).
5. Trades: count ALL recapturers (PAWNS, bishops, knights) AND his second attacker after my recapture: g75 18...Rb5?! 19.Rxb5 Bxb5 20.Bxb5 - his e2-bishop's second bite won a piece. Write HIS recapture AND mine - his last => don't start (g70 Rxe5?? dxe5); no 'trade' without my recapturer (g72 Rd8??); value chains (g58)/sacs (g65).
6. Mate nets BEFORE any move: Qh2+Rh1 open h-file (Nf6 = h7's only guard); Qh6+rook h4/h5 = Qxh7# - luft/cover h7 FIRST, no grabs (g66,g69); keep f7/f6 escape when Rh1 protects and my f8-rook blocks f8 (g74); Q+B on f2 (g61).
7. Loose minor/rook (jump, retreat, rook swing): destination attacked by NOTHING (g58 Nd4??; g63 Nb4?? cxb4; g68 Ra6??; g70/g73 Bd3??).
8. Down material: keep queens (13...Qc7! not Qxd5, g75; g68 Be6? Qxd8); no queen onto a pawn-attacked square (g70 Qd4??); no pawn grab that opens his attack (g74); repetition = half point (g75 threefold while down B+P); when winning progress.
9. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s; lost 1-5 s. Long thinks never prevented a blunder or illegal try (g46-g75; g75: 39-50 s/move, the 44 s move was the only '?').

## Openings
- Yugoslav 9.O-O-O d5 10.exd5 Nxd5 11.Nxc6 bxc6 12.Nxd5 cxd5 13.Qxd5 -> 13...Qc7! FORCED (I am a pawn down; 13...Qxd5? 14.Rxd5 lost endgame vs SF, g75); 12.Bd4 same: 13...Qc7! (...Be6? 14.Qxd8). 14.Qc5 -> ...Qb7 (rank 7 guards e7); 14...Qb6? 15.Qxb6 axb6 lost (g72). Never a rook where his bishop also attacks: 18...Rb5?! 19.Rxb5 Bxb5 20.Bxb5 (g75).
- Chigorin as White: 14...Nb4 -> 15.Bb1!; a5-a4: a3-kick once Nb4's retreats are covered; reroute d2-knight f1-e3-f5 (g70); 19.Nf5 Bxf5 20.exf5 good, then Be3/Qd2/Rc1, not 21.Bg5?!. After 22.Bxd4: bishop stays home (23.Be5?? dxe5, g73); no Nxe5/Bxh6/Qd4 grabs (g65-g70).
- Chigorin as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; move the queen the move his bishop hits it (g41 Rfd8?? Bxa5); resolve the centre before his d5.
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; no ...Nxe4 while Qf3 covers e4; b7 loose once b5 leaves; Rauzer 11...gxf6!.
- Alapin 5.Qxd4: ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5 = equal; NEVER ...Nb4; no knight to d4; no ...b5 with his a4-pawn or while Rd1 faces Qd8 through d6; no Qa5 once the a-file opens.
- Soltis 9.Bc4 (0-6 vs Sol, all guard/loot errors): 14.h5 (his g-pawn home) Nxh5! 15.g4 Nf6. 14.g4 first then h5: ...Nxh5?? = N for P (gxh5, g74) - keep Nf6 (h7's guard), meet h5 with ...gxh5 or ...Qa5. 16.g5 -> ONLY ...Nh5; 16.Qh2 (g4 gone): keep Nf6; 16.Bh6: do NOT recapture (...Qe8/...Qa5 + luft). After 19.Rxh5 gxh5: ...Re8 AT ONCE; g6 = h5's sole guard (g55). 19.hxg6 -> ...fxg6 (else Qh7# net).
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended.

## Opponents
- Stockfish 19: ~0 s/move, never errs tactically; punishes loose units, queens on attacked lines, back-rank, loose rooks; grabs favourable queen trades; when down, aim for repetition (g75 threefold king-dance drew while I was down B+P).
- Sonnet 5.5: banks clock, takes EVERY free/attacked unit (g73 dxe5, exd4, Nxd3, Rxd2); keep all defended, no speculative sacs; 1-3 s when lost.
- GPT-6.1 Sol: fast (3-13 s); takes every free piece/open-file loot instantly; vs Soltis plays g4+h5, gxh5 loot and the Bh6/Qh6-Qh7 mate net - f8 luft early, never grab with mate pending (g69, g74).
