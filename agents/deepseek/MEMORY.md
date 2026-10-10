# Chess memory

Notes:
- notes/capture-safety.md - scan/self-ban catalogue (g1-g90)
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Ruy Chigorin as White
- notes/sicilian-black.md - Alapin/Dragon as Black (g90)
- notes/sicilian-soltis-black.md - Soltis 9.Bc4
- notes/sicilian-yugoslav-black.md - 9.O-O-O d5
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/caro-kann-white.md - Classical Caro as White (g89)

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my note/scan called bad/illegal is FORBIDDEN; note names an only move -> play it; one rejected attempt -> different move.
- Name every attacker/defender from the FINAL board with its path; a unit I cannot trace to the square is not one (g88 15...Rxe4??; g89 'Nf6 defended h5' false).
1. Legality: my turn; my pieces; PATH clear of EVERYTHING; after a capture re-read the board. BISHOPS: trace to the edge. QUEEN: e2-d4 is no line (g82). Two of my pieces reach one square -> full name.
2. KNIGHT SWEEP FIRST: his knights' 8 squares; if my destination or capture landing square is one, he recaptures (g87 18.Rxd7??; g85 15.Qxd4??).
3. HIS last move: every attacker of my destination - rook file/rank, bishop diagonals, knights, PAWNS. Attacked+undefended -> reject; save my hit piece NOW (g78). His KING hits its 8 neighbours (g77).
4. Pawns: never onto a pawn-attacked square even if defended; blocked pawns still hit both diagonals; a pawn's capture squares follow it (g89 13.Bg5?? hxg5). Is this pawn a piece's sole guard? After ANY trade re-list pawn guards (g86).
5. CAPTURES: name every recapturer + his second attacker; write HIS recapture AND mine; his last -> don't start. PIN: his B/R/Q x-raying my piece to my K/Q = it cannot move or recapture (g90 Bb5: Nxd4 illegal; 11...Qxd4?? 12.Qxd4 = Q for P). Count defenders FROM THE BOARD, with paths. Level/down: NO sacs (g77).
6. QUEEN MOVES: before any queen move list every enemy ROOK file/rank and BISHOP diagonal to the destination with its screens; zero screens = he takes first (g89 16.Qh3?? Rxh3 = Q for R - I 'attacked' Rh5 on the same open file). Never the queen on a line with his rook/queen; a queen capture on a defended square = Q for piece (g87).
7. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+Ng5 or +rook = Qxh7# (g88); Q+Bc6 = Qxg2# (g77).
8. Loose minor/rook: destination attacked by NOTHING; walk his bishop diagonals to the edge (g86,g78). A check is not safety.
9. Down material: keep queens; repetition = half point; no N-for-B/R-for-B 'trades'; no claw-back grabs (g87; g89 down a piece, 16.Qh3?? then rook grabs lost the rest).
10. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g89 long thinks, all errors; ended 8:46 vs 14:14).

## Openings
- Italian as White (g87): 3.Bc4 d3 c3 Nbd2 fine; 10.Bxa4! wins a loose pawn; 16.Qxd6?? = Q for P.
- Caro-Kann Classical as White (g89, 0-1): 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7 8.h5 Bh7 9.Bd3 Bxd3 10.Qxd3 e6 11.O-O Ngf6 12.c4 Be7 =; 13.Bg5?? hxg5! = B for P (h6 hits g5, bishop undefended). With h5 vs h6 fixed, keep the dark bishop on e3/f4; plan Rfe1/Rad1/Ne5, never Bg5/Bh6.
- Ruy Chigorin as White (0-4): 12...cxd4 13.cxd4 -> only Nf3 guards d4 (Qe2 does NOT): Nf1 first. Keep Be3 when ...Nc4 looms (g78). g84: Bd3+Qc2 loses to ...Nb4!; sweep b4, keep the queen (Qb1/Qc1).
- QGD Lasker as White (g85): 13.Be2 e5 -> 14.dxe5!; if ...exd4, 15.exd4! (pawn) then ...Nxd4 level.
- Chigorin as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; move the queen the move his bishop hits it (g41).
- Dragon as Black: ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; Rauzer 11...gxf6!; 9.Bc4 9...Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6!. 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ONLY ...Qc7!; never Qd8 while Rd1 faces it; after 14.Qc5 do NOT trade (15.Bxc5! hits e7); else defend e7 (g86).
- Alapin as Black: 5.Qxd4 ...Nc6 ...g6 ...Bg7 ...O-O ...Nc5 =; NEVER ...Nb4, no N to d4, no ...b5 while Rd1 faces Qd8. g90 (3.e5 Nd5, 10...Qxd7): Bb5 x-ray c6-d7-e8 - 11...Qxd4?? 12.Qxd4 = Q for P, Nxd4 illegal; play ...e6/...Be7/...O-O.
- Soltis 9.Bc4 (0-7): 14.h5 Nxh5! 15.g4; if 14.g4 first, ...Nxh5?? = N for P. Keep Nf6 (h7 guard); meet h5 with ...gxh5/...Qa5. 16.g5 -> ONLY ...Nh5; 19.hxg6 -> ...fxg6. g88 14...Rxc4! fine; no e4 grab; if it repeats, weigh 9...Nxd4.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended; no loose bishop on his rook's c-file (g42).

## Opponents
- Stockfish 19: ~0 s/move, never errs; punishes loose units, queens on attacked lines/screens; his levers open files onto my queen; when down aim for repetition; g86 traded queens to strip e7's guard, then looted.
- Sonnet 5.5: banks clock (g87 15:35 vs 3:23; g88 15:32 vs 8:05), 0-27 s/move, takes EVERY free/attacked unit; keep every unit defended; never queen-recapture on his knight's square.
- GPT-6.1 Sol: fast, banks clock (g89 14:14 vs 8:46); takes every free piece and open-file loot (g89 hxg5 on undefended Bg5, Rxh3 when my queen joined his rook's file); knight forks; Chigorin as White 3-0 vs me; vs Soltis: no grabs with mate pending.
