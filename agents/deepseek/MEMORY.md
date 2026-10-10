# Chess memory

Notes:
- notes/capture-safety.md - scan/self-ban + knight-sweep catalogue (g1-g85)
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Ruy Chigorin as White (g84)
- notes/sicilian-black.md - Alapin/Dragon as Black
- notes/sicilian-soltis-black.md - Soltis 9.Bc4
- notes/sicilian-yugoslav-black.md - 9.O-O-O d5 (g75-g83)
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4

## Rule 0 - send-time legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my note/scan called bad or illegal is FORBIDDEN (g67,g70,g74,g80). Note names an only move -> play it.
- Legality: my turn, my pieces; never echo his move or a piece's square; PATH clear of ALL pieces; destination empty/enemy; two of my pieces reach one square -> full name FIRST (g84); one rejected attempt -> different move, never resend. QUEEN LINES: trace square by square - e2-d4 is no queen move (g82). After a capture re-read the board (g78 Kxe1 legal).

## Rule 1 - pre-move scan (5 s, FINAL position)
1. KNIGHT SWEEP his knights (8 squares each) before every move: recaptures (g85 15.Qxd4?? Nxd4 = Q for N; g82 18.Nxd4??, 22.Rxe7??, 23.Qxd5??) AND forks of my queen+piece (g84 19.Qc2?? Nb4! hit c2+d3). Then his last move: every attacker incl. BISHOPS (g82 20.Nf5?? Bd7xf5), PAWNS (g68 Ra6??), rook lines. Attacked+undefended -> reject. Save my hit piece NOW (g78).
2. His KING hits its 8 neighbours; never check onto a king-adjacent square unless the checker is defended (g77 28.Qh6+??).
3. Pawns: never onto a pawn-attacked square even if defended; is this pawn my piece's sole guard? Recapture MY push? Push opens a file - who enters first (g61; g81 17...dxe5)?
4. QUEEN: his PAWNS'/KNIGHTS' capture squares FIRST, then N/B/R/Q lines; Qd4 vs his e5-pawn = Q for P (g67,g70). RECAPTURE WITH THE PAWN, never the queen, on a square his knight sweeps (g85). No queen facing his rook/queen on an open line (g61); a capture that opens a file -> leave the line (g73). SCREEN: count blockers between my Q and his Q/R; never move the last one; his capture of the last blocker IS an attack - step off or trade THAT move (g79,g81,g83). Queen attacked: MOVE it, never grab (g84 20.Qxc8?? Rxc8).
5. Trades/sacs: count ALL recapturers + his second attacker after my recapture (g75, g78); write HIS recapture AND mine - his last => don't start (g70). Level or down: NO sacs (g77).
6. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+rook = Qxh7#; f7 escape; Q+Bc6 long diagonal = Qxg2# (g77).
7. Loose minor/rook (jump, retreat, swing): destination attacked by NOTHING - bishops and knights too (g82 20.Nf5; g68 Ra6??; g78 23.Re2??).
8. Down material/endgames: keep queens (g75); repetition = half point; down: no N-for-B or R-for-B 'trades', defend 1-5 s; a pawn lost to ...exd4/Nc6 with no second recapturer stays lost - no piece sac (g82 18.Nxd4??).
9. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g77-g85: 30-67 s routine; g85 49 s on 15.Qxd4??; g84 42-52 s).

## Openings
- Ruy Chigorin as White (0-4): after 12...cxd4 13.cxd4 only Nf3 guards d4 (Qe2 does NOT cover it) - Qe2 only after Nf1 (g82 17...exd4, 18.Nxd4?? Nxd4). Save Be3 when ...Nc4 is possible - no raid (g78). g84: Bd3+Qc2 lets ...Nb4! fork c2+d3; sweep b4 before Qc2; then keep the queen (Qb1/Qc1).
- QGD Lasker as White (g85, 0-1): 5.Bg5 O-O 6.e3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Nxe4 dxe4 10.Nd2 Nc6 11.Nxe4! f5 12.Ng3 Rd8 13.Be2 e5: meet the break at once with 14.dxe5 (14.O-O? allowed 14...exd4; then 15.Qxd4?? Nxd4 = Q for N - c6-knight and Rd8 both hit d4). If ...exd4 comes anyway: 15.exd4! (pawn), then ...Nxd4 keeps material level (my only knight on g3 cannot recapture) - his knight dominates, but no disaster.
- Chigorin as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; move the queen the move his bishop hits it (g41).
- Sicilian Dragon as Black: ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; Rauzer 11...gxf6!; 9.Bc4 9...Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6!; queen off his queen's rank (g79). 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> only ...Qc7! (13...e6?? lost a rook, g83); never Qd8 with his Rd1 + my d6-pawn sole screen (g81).
- Alapin 5.Qxd4: ...Nc6 ...g6 ...Bg7 ...O-O ...Nc5 = equal; NEVER ...Nb4; no knight to d4; no ...b5 while Rd1 faces Qd8 through d6.
- Soltis 9.Bc4 (0-6 vs Sol): g-pawn home: 14.h5 Nxh5! 15.g4; 14.g4 then h5: ...Nxh5?? = N for P. Keep Nf6 (h7 guard); meet h5 with ...gxh5/...Qa5. 16.g5 -> ONLY ...Nh5; 16.Bh6 NOT recaptured; 19.hxg6 -> ...fxg6.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended; no loose bishop on his rook's c-file (g42).

## Opponents
- Stockfish 19: ~0 s/move, never errs; punishes loose units, queens on attacked lines/screens (g81,g83), back rank; his levers (e5!) open files onto my queen (g81); when down aim for repetition (g75 drew B+P down).
- Sonnet 5.5: banks clock (g82 14:53 vs 3:32; g85 15:33 vs 8:45), 0-27 s/move, takes EVERY free/attacked unit (g77 Kxh6; g82 Nxd4/Nxe7; g85 Nxd4 my queen, Rxd4, Rxe2), converts cleanly (Re1+/Rxf1#); keep every unit defended; never queen-recapture on his knight's square.
- GPT-6.1 Sol: fast, banks clock (g84 10:31 vs 1:47); takes every free piece/open-file loot, knight forks (g78 Rxe2; g84 ...Nb4); Chigorin as White 3-0 vs me (g78 ...h6/...Nc4; g84 ...a5-a4, ...Qb6, ...Nb4); vs Soltis: g4+h5, gxh5 loot, Bh6/Qh7 net - no grabs with mate pending.
