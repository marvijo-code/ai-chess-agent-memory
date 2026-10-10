# Chess memory

Notes:
- notes/capture-safety.md - scan/self-ban catalogue (g1-g86)
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Ruy Chigorin as White (g84)
- notes/sicilian-black.md - Alapin/Dragon as Black
- notes/sicilian-soltis-black.md - Soltis 9.Bc4
- notes/sicilian-yugoslav-black.md - 9.O-O-O d5 (g75-g86)
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my note/scan called bad/illegal is FORBIDDEN (g67,g70,g74,g80); note names an only move -> play it.
- Trace EVERY path piece by piece: my pieces, his; never echo his move/square; two of my pieces reach one square -> full name (g84); one rejected attempt -> different move. Before a CAPTURE walk the capturer's line to the target: no bishop reaches e7 from f5/g7 (g86 illegal try, 1:51 lost). Queen lines: e2-d4 is no queen move (g82). After a capture re-read the board (g78 Kxe1 legal).

## Rule 1 - pre-move scan (5 s, FINAL position)
1. KNIGHT SWEEP (his knights' 8 squares) before every move: recaptures (g85 15.Qxd4?? Nxd4; g82 18.Nxd4??, 22.Rxe7??, 23.Qxd5??) and forks of my queen+piece (g84 19.Qc2?? Nb4!). Then his last move: rook lines, BISHOPS (g82 20.Nf5?? Bd7xf5; g86 17...Bd3?? Bf1xd3), PAWNS (g68 Ra6??). Attacked+undefended -> reject; save my hit piece NOW (g78).
2. His KING's 8 neighbours: no check onto one unless the checker is defended (g77 28.Qh6+??).
3. Pawns: never onto a pawn-attacked square; is this pawn a piece's sole guard? Recapture MY push? Push opens a file - who enters first (g81 17...dxe5)? After ANY queen trade re-list pawn guards: e7 was guarded only by Qc7, fell to Bxe7 the move I traded (g86).
4. QUEEN: his PAWNS'/KNIGHTS' capture squares FIRST, then N/B/R/Q lines (g67,g70); recapture with the PAWN, never the queen, on a square his knight sweeps (g85). No queen facing his rook/queen on an open line (g61); a capture that opens a file -> leave the line (g73). SCREEN: count blockers to his Q/R, never move the last; his capture of it IS an attack - step off or trade THAT move (g79,g81,g83). Queen attacked: move it, never grab (g84 20.Qxc8?? Rxc8).
5. Trades/sacs: count ALL recapturers + his second attacker after my recapture; write HIS recapture AND mine - his last => don't start (g70). Level/down: NO sacs (g77).
6. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+rook = Qxh7#; f7 escape; Q+Bc6 long diagonal = Qxg2# (g77).
7. Loose minor/rook (jump, retreat, swing): destination attacked by NOTHING - bishops/knights too (g82 20.Nf5; g68 Ra6??; g78 23.Re2??).
8. Down material: keep queens (g75); repetition = half point; no N-for-B/R-for-B 'trades'; a pawn lost to ...exd4/Nc6 with no second recapturer stays lost - no piece sac (g82 18.Nxd4??).
9. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (30-67 s routine; g86 43 s on 17...Bd3??).

## Openings
- Ruy Chigorin as White (0-4): 12...cxd4 13.cxd4 -> only Nf3 guards d4 (Qe2 does NOT): Nf1 first (g82). Keep Be3 when ...Nc4 looms (g78). g84: Bd3+Qc2 loses to ...Nb4! fork; sweep b4 first, then keep the queen (Qb1/Qc1).
- QGD Lasker as White (g85, 0-1): 13.Be2 e5 -> 14.dxe5 now; if ...exd4 comes, 15.exd4! (pawn) then ...Nxd4 is level (g3-knight cannot recapture).
- Chigorin as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; move the queen the move his bishop hits it (g41).
- Sicilian Dragon as Black: ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; Rauzer 11...gxf6!; 9.Bc4 9...Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6!; queen off his queen's rank (g79). 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ONLY ...Qc7! (13...e6?? lost a rook, g83); never Qd8 with Rd1 facing Qd8 through my d6-pawn (g81); g86 14.Qc5! do NOT trade - 14...Qxc5? 15.Bxc5 leaves e7 with no guard, 16.Bxe7 wins a 2nd pawn; keep the queen on the 7th rank (14...Qd7) or if traded defend e7 at once (...Be6/...Re8).
- Alapin 5.Qxd4: ...Nc6 ...g6 ...Bg7 ...O-O ...Nc5 = equal; NEVER ...Nb4, no knight to d4, no ...b5 while Rd1 faces Qd8.
- Soltis 9.Bc4 (0-6 vs Sol): g-pawn home: 14.h5 Nxh5! 15.g4; 14.g4 then h5: ...Nxh5?? = N for P. Keep Nf6 (h7 guard); meet h5 with ...gxh5/...Qa5. 16.g5 -> ONLY ...Nh5; 16.Bh6 NOT recaptured; 19.hxg6 -> ...fxg6.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended; no loose bishop on his rook's c-file (g42).

## Opponents
- Stockfish 19: ~0 s/move, never errs; punishes loose units, queens on attacked lines/screens (g81,g83), back rank; his levers (e5!) open files onto my queen (g81); when down aim for repetition (g75 drew B+P down); g86 traded queens to strip e7's only guard, then looted.
- Sonnet 5.5: banks clock (g82 14:53 vs 3:32; g85 15:33 vs 8:45), 0-27 s/move, takes EVERY free/attacked unit (g77 Kxh6; g82 Nxd4/Nxe7; g85 Rxd4/Rxe2), converts cleanly; keep every unit defended; never queen-recapture on his knight's square.
- GPT-6.1 Sol: fast, banks clock; takes every free piece/open-file loot, knight forks (g78 Rxe2; g84 ...Nb4); Chigorin as White 3-0 vs me (g78 ...h6/...Nc4; g84 ...a5-a4, ...Qb6, ...Nb4); vs Soltis: g4+h5, gxh5 loot, Bh6/Qh7 net - no grabs with mate pending.
