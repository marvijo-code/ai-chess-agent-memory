# Chess memory

Notes:
- notes/capture-safety.md - scan/self-ban + knight-sweep catalogue
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Alapin/Dragon as Black
- notes/sicilian-soltis-black.md - Soltis 9.Bc4
- notes/sicilian-yugoslav-black.md - 9.O-O-O + Nxd4/Be6 lines
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4

## Rule 0 - send-time legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my note/scan warned about is FORBIDDEN (g67,g70,g74,g80). If my note names an only move, play it.
- Legality: my turn, my pieces; never echo his move or a piece's square; PATH clear of ALL pieces; destination empty/enemy; two to one square -> full name; one rejected attempt -> different move, never resend. QUEEN LINES: trace square by square - e2-d4 is no queen move (g82 illegal try). After a capture re-read the board (g78 Kxe1 legal).

## Rule 1 - pre-move scan (5 s, FINAL position)
1. KNIGHT SWEEP his knights (8 squares each) before every capture/placement; if my destination or my capture's landing square is one, assume he recaptures (g82: 18.Nxd4??, 22.Rxe7??, 23.Qxd5?? all lost to unseen knight takes - c6-e7, e7-d5, f6-d5). Then his last move: every attacker incl. BISHOPS (g82 20.Nf5?? Bd7xf5), PAWNS (g68 Ra6??), rook lines. Attacked+undefended -> reject. Save my hit piece NOW (g78).
2. His KING hits its 8 neighbours; never check onto a king-adjacent square unless the checker is defended (g77 28.Qh6+??).
3. Pawns: never onto a pawn-attacked square even if defended; is this pawn my piece's sole guard? Recapture MY push? Push opens a file - who enters first (g61; g81 17...dxe5)?
4. QUEEN: his PAWNS'/KNIGHTS' capture squares FIRST, then N/B/R/Q lines; Qd4 vs his e5-pawn = Q for P (g67,g70). No queen facing his rook/queen on an open line (g61); a file his capture opens -> leave the line (g73). SCREEN: my Q and his Q/R on one rank/file - count blockers; never move the last pawn/knight one, move my queen off first (g79, g81).
5. Trades/sacs: count ALL recapturers + his second attacker after my recapture (g75, g78); write HIS recapture AND mine - his last => don't start (g70). Level or down: NO sacs (g77).
6. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+rook = Qxh7#; f7 escape; Q+Bc6 long diagonal = Qxg2# (g77).
7. Loose minor/rook (jump, retreat, swing): destination attacked by NOTHING - bishops and knights too (g82 20.Nf5; g68 Ra6??; g78 23.Re2??).
8. Down material/endgames: keep queens (g75); repetition = half point; down: no N-for-B or R-for-B 'trades' (g82), defend 1-5 s; a pawn lost to ...exd4/Nc6 with no second recapturer stays lost - no piece sac to regain it (g82 18.Nxd4??).
9. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g77-g82: 36-67 s routine; g82 moves 14-25 all 40-61 s, then 3 blunders).

## Openings
- Chigorin as White (0-3): after 12...cxd4 13.cxd4 d4's only defender is Nf3 (Qe2 does NOT cover d4; Qd1/Qd2 do via the file). Never play Qe2 while his Nc6 + ...exd4 threaten d4 - 17...exd4 wins a pawn and 18.Nxd4?? Nxd4 loses a piece (g82). When his knight can reach c4, save Be3 at once (Bd2/Bf4) - no raid (g78). Bc2 with his Qc7 + rook on the c-file: lone recapture loses to Rxc2. 13.d5 c4 (g77): 15...g6! takes f5; 20.Bxc5?? Qxc5+.
- Chigorin as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; move the queen the move his bishop hits it (g41).
- Sicilian Dragon as Black: ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; no ...Nxe4 while Qf3 covers e4; Rauzer 11...gxf6!. 9.Bc4 9...Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6!; keep my queen off his queen's rank (g79). 9.O-O-O: ...Nxd4/...Be6/...Qa5; prefer ...Bxa2/...Qb6/...Rfc8; never Qd8 with his Rd1 + my d6-pawn sole screen (g81).
- Alapin 5.Qxd4: ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5 = equal; NEVER ...Nb4; no knight to d4; no ...b5 while Rd1 faces Qd8 through d6.
- Soltis 9.Bc4 (0-6 vs Sol): 14.h5 (his g-pawn home) Nxh5! 15.g4 Nf6; 14.g4 first then h5 -> ...Nxh5?? = N for P (gxh5). Keep Nf6 (h7 guard); meet h5 with ...gxh5/...Qa5. 16.g5 -> ONLY ...Nh5; 16.Bh6 NOT recaptured; 19.hxg6 -> ...fxg6.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended; never a loose bishop on his rook's c-file (g42).

## Opponents
- Stockfish 19: ~0 s/move, never errs; punishes loose units, queens on attacked lines/screens, back rank, undefended pawns; his levers (e5!) open files onto my queen (g81); when down, aim for repetition (g75 drew B+P down).
- Sonnet 5.5: banks clock (g82 14:53 vs 3:32), takes EVERY free/attacked unit in ~10 s (g77 Kxh6; g82 Nxd4/Nxe7/Nexd5), consolidates, never misjudges knight lines; 1-3 s when lost.
- GPT-6.1 Sol: fast; takes every free piece/open-file loot (g78 Rxe2); Chigorin as White 2-0 vs me (...h6/...Nc4 punish Bg5/Be3); vs Soltis: g4+h5, gxh5 loot, Bh6/Qh7 net - no grabs with mate pending.
