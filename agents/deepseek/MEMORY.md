# Chess memory

Notes:
- notes/capture-safety.md - scan/self-ban catalogue (g1-g93)
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Ruy Chigorin as White
- notes/sicilian-black.md - Alapin/Dragon as Black (g90,g91)
- notes/sicilian-soltis-black.md - Soltis 9.Bc4
- notes/sicilian-yugoslav-black.md - 9.O-O-O d5
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/caro-kann-white.md - Classical Caro as White (g89)

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my note/scan called bad/illegal is FORBIDDEN; note names an only move -> play it; one rejected attempt -> different move.
- Name every attacker/defender from the FINAL board with its path; a unit I cannot trace is not one (g88 15...Rxe4??; g89 Nf6-defends-h5 false).
1. Legality: my turn; my pieces; PATH clear of EVERYTHING; after a capture re-read the board. BISHOPS: trace to the edge. QUEEN e2-d4 is no line (g82). Two of my pieces reach one square -> full name.
2. KNIGHT SWEEP FIRST: his knights' 8 squares; if my destination or capture landing square is one, he recaptures (g87, g85).
3. HIS last move: every attacker of my destination - rook file/rank, bishop diagonals, knights, PAWNS; attacked+undefended -> reject; save my hit piece NOW (g78). His KING hits its 8 neighbours.
4. Pawns: never a minor/rook onto a pawn-guarded square - walk his pawns' capture squares first, INCLUDING a pawn that just moved (g92/g89 13.Bg5?? hxg5, the SAME blunder twice). Blocked pawns still hit both diagonals; a pawn's capture squares follow it; after ANY trade re-list pawn guards (g86).
5. CAPTURES: name every recapturer + his second attacker; write HIS recapture AND mine; his last -> don't start; count defenders FROM THE BOARD with paths. Level/down: NO sacs. PIN: his B/R/Q x-raying my piece to my K/Q = it cannot move or recapture (g90 Nxd4 illegal).
6. QUEEN: never a queen capture on a defended square (g87); his QUEEN defends along open files/diagonals (g91). A 'trade' needs MY recapturer that SURVIVES: if his piece takes my queen and no legal unit of mine hits that square, it was Q for a pawn/minor (g91 19...Qxd6?? 20.Qxd6+; g93 13.Bd4?? Bxd4 14.Qxd4?? Qxd4 - Nc3/Nd2 never reach d4). Before any queen move walk every enemy rook file/rank and bishop diagonal to the destination, screens counted (g89 16.Qh3?? Rxh3).
7. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+Ng5 = Qxh7#; Q+Bc6 = Qxg2#.
8. Loose minor/rook: destination attacked by NOTHING; walk his bishop diagonals to the edge. A check is not safety.
9. Down material: keep queens; repetition = half point; no N-for-B/R-for-B 'trades'; no claw-back grabs. K+P race: get the king IN FRONT of the passer, count tempos to the square in front; beside/behind loses (g92).
10. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g89-g93: 30-40 s routine, every error).

## Openings
- Italian 4.d3 d5 as White (g87,g92,g93 0-3): 5.exd5 Nxd5 6.O-O Bc5 7.Bxd5 Qxd5 8.Nc3 Qd8 9.Be3 Bd6 10.d4 O-O 11.dxe5 Nxe5 12.Nxe5 Bxe5 = equal; then 13.Bd4?? is a TRAP (Bxd4 Qxd4 = Q for B, no recapturer). Play Rfe1/Rc1, Nf1-g3/Be3-f2, h3/c3, keep every unit defended; NEVER Bg5 once h3/h6 is in.
- Caro-Kann Classical as White (g89 0-1): 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7 8.h5 Bh7 9.Bd3 Bxd3 10.Qxd3 e6 11.O-O Ngf6 12.c4 Be7 =; 13.Bg5?? hxg5! With h5/h6 fixed keep the dark bishop on e3/f4.
- Ruy Chigorin as White (0-4): 12...cxd4 13.cxd4 -> only Nf3 guards d4 (Qe2 does NOT): Nf1 first; keep Be3 when ...Nc4 looms (g78); g84: Bd3+Qc2 loses to ...Nb4! (keep Qb1/Qc1).
- QGD Lasker as White (g85): 13.Be2 e5 -> 14.dxe5!; if ...exd4, 15.exd4! (pawn) then ...Nxd4 level.
- Chigorin as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; move the queen the move his bishop hits it (g41).
- Dragon as Black: ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; Rauzer 11...gxf6!; 9.Bc4 Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6. 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ONLY ...Qc7!; never Qd8 while Rd1 faces it; else defend e7 (g86).
- Alapin as Black (g58-g64,g90,g91): 5.Qxd4 ...Nc6 ...g6 ...Bg7 ...O-O ...Nc5 =; NEVER ...Nb4, no N to d4, no ...b5 while Rd1 faces Qd8; 3.e5 Nd5 7.Bc4 Nb6 8.Bb5 Bd7 9.Nc3 a6 10.Bxc6 -> recapture 10...bxc6! (10...Bxc6?! 11.d5! +2); g90: Bb5 x-rays c6-d7-e8, 11...Qxd4?? 12.Qxd4 = Q for P.
- Soltis 9.Bc4 (0-7): 14.h5 Nxh5! 15.g4; if 14.g4 first, ...Nxh5?? = N for P; keep Nf6 (h7 guard), meet h5 with ...gxh5/...Qa5; 16.g5 -> ONLY ...Nh5; 19.hxg6 -> ...fxg6; no e4/Rxe4 grabs.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended (g42).

## Opponents
- Stockfish 19: ~0 s/move, never errs; punishes loose units and queens on attacked lines/screens; his levers open files onto my queen; down: aim for repetition; g86 traded queens to strip e7's guard then looted; g91 ...Bxc6?! let 11.d5! (+2); g93 accepted the offered Bd4 trade and recaptured with the queen on the d-file.
- Sonnet 5.5: banks clock (g92 4:34 vs 2:15), 0-60 s/move, takes EVERY free/attacked unit; keep every unit defended; never queen-recapture on his knight's square; converts a piece up cleanly.
- GPT-6.1 Sol: fast, banks clock (g89 14:14 vs 8:46); takes every free piece and open-file loot (g89 hxg5 on undefended Bg5, Rxh3 when my queen joined his rook's file); knight forks; Chigorin as White 3-0 vs me; vs Soltis: no grabs with mate pending.
