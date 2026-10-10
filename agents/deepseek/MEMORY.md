# Chess memory

Notes:
- notes/capture-safety.md - scan/self-ban catalogue (g1-g88)
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Ruy Chigorin as White (g84)
- notes/sicilian-black.md - Alapin/Dragon as Black
- notes/sicilian-soltis-black.md - Soltis 9.Bc4 (g88)
- notes/sicilian-yugoslav-black.md - 9.O-O-O d5 (g75-g86)
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my note/scan called bad/illegal is FORBIDDEN (g67,g70,g74,g80); note names an only move -> play it.
- Name every defender/attacker from the FINAL board with its path; a unit I cannot trace to the square is not a defender (g88 15...Rxe4??: "e4 guarded only by the e2-knight" false - Nde2 does not attack e4; f3-pawn + Nc3 did = R for P).
- Trace EVERY path twice: my pieces, his; never echo his move/square; two of my pieces reach one square -> full name (g84; g87 N3xd2); one rejected attempt -> different move (g67,g70,g74).
1. Legality: my turn; my pieces; PATH clear of EVERYTHING; after a capture re-read the board. BISHOPS: trace square by square to the edge (g86: Bxe7 and Bxf3 both illegal; 3 = forfeit). QUEEN: e2-d4 is no queen line (g82).
2. KNIGHT SWEEP FIRST: his knights' 8 squares; if my destination or my capture's landing square is one, he recaptures (g87 18.Rxd7?? Nf6xd7; 24.Nxe5?? Nd7xe5; g85 15.Qxd4?? Nxd4; g82 18.Nxd4??, 22.Rxe7??).
3. HIS last move: every attacker of my destination - rook file/rank, BISHOPS' diagonals (g82 20.Nf5?? Bd7xf5), knights, PAWNS (g68 Ra6??). Attacked+undefended -> reject; save my hit piece NOW (g78). His KING hits its 8 neighbours (g77 28.Qh6+??).
4. Pawns: never onto a pawn-attacked square even if defended (g87 19.Bd3?? cxd3; a blocked pawn still hits both diagonals). Is this pawn a piece's sole guard? Recapture MY push? Push opens a file - who enters first (g81 17...dxe5)?? After ANY queen trade re-list pawn guards (g86: e7 fell to Bxe7 the move I traded).
5. CAPTURES: name every recapturer + his second attacker after my recapture; write HIS recapture AND mine; his last -> don't start (g70). Count the target's defenders FROM THE BOARD, with paths; a grab of a 2-defender pawn = sac (g88 R for P, then ...Nxe4 hung a knight too). Level/down: NO sacs (g77).
6. Mate nets BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+rook = Qxh7#; Qh6+Ng5 = Qxh7# (Ng5 guards h7; ...Kh8 fails - queen protected; only save = hit the knight ...f6 - g88 20...Qd7?? mated); Q+Bc6 long diagonal = Qxg2# (g77).
7. Loose minor/rook (jump, retreat, swing): destination attacked by NOTHING, and walk his bishop diagonals to the edge (g86 23...Rb8?? 24.Bxb8; g78 23.Re2??; g80 21...Rd2+??). A check is not safety.
8. Down material: keep queens (g75); repetition = half point; no N-for-B/R-for-B 'trades'; no claw-back grabs - g87's 18.Rxd7, 19.Bd3, 24.Nxe5 each hung more; every capture still passes the full scan. Mate scan still FIRST (g88: 20...Qd7?? mate while already lost).
9. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g86 43 s on 17...Bd3??; g87 51 s on 16.Qxd6??; g88 38 s on 15...Rxe4??; ended g87 3:23 vs 15:35, g88 8:05 vs 15:32).

## Openings
- Italian as White (g87, 0-1): 3.Bc4 d3 c3 Nbd2 fine; 10.Bxa4! wins a loose pawn; 16.Qxd6?? (Be7 recaptures d6) = Q for P.
- Ruy Chigorin as White (0-4): 12...cxd4 13.cxd4 -> only Nf3 guards d4 (Qe2 does NOT): Nf1 first (g82). Keep Be3 when ...Nc4 looms (g78). g84: Bd3+Qc2 loses to ...Nb4!; sweep b4, keep the queen (Qb1/Qc1).
- QGD Lasker as White (g85, 0-1): 13.Be2 e5 -> 14.dxe5!; if ...exd4, 15.exd4! (pawn) then ...Nxd4 level.
- Chigorin as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; move the queen the move his bishop hits it (g41).
- Sicilian Dragon as Black: ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; Rauzer 11...gxf6!; 9.Bc4 9...Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6!. 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ONLY ...Qc7! (g83); never Qd8 while Rd1 faces it through my d6-pawn (g81); g86: after 14.Qc5 do NOT trade (15.Bxc5! hits unguarded e7); else defend e7 (...Qd7/...Re8).
- Alapin 5.Qxd4: ...Nc6 ...g6 ...Bg7 ...O-O ...Nc5 = equal; NEVER ...Nb4, no knight to d4, no ...b5 while Rd1 faces Qd8.
- Soltis 9.Bc4 (0-7): g-pawn home: 14.h5 Nxh5! 15.g4; if 14.g4 first, ...Nxh5?? = N for P. Keep Nf6 (h7 guard); meet h5 with ...gxh5/...Qa5. 16.g5 -> ONLY ...Nh5; 19.hxg6 -> ...fxg6. g88 13...Nc4 14.Bxc4 Rxc4! 15.Nde2: rook is a lone raider - no e4 grab (f3+Nc3 defend); retreat ...Rc8/...Rc7. If the line repeats, weigh 9...Nxd4.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended; no loose bishop on his rook's c-file (g42).

## Opponents
- Stockfish 19: ~0 s/move, never errs; punishes loose units, queens on attacked lines/screens (g81,g83); his levers (e5!) open files onto my queen (g81); when down aim for repetition (g75 drew B+P down); g86 traded queens to strip e7's only guard, then looted.
- Sonnet 5.5: banks clock (g87 15:35 vs 3:23; g88 15:32 vs 8:05), 0-27 s/move, takes EVERY free/attacked unit (g87 Bxd6/Nxd7/cxd3/Nxe5; g88 fxe4 at once; g85 Rxd4/Rxe2), converts cleanly (g88 R up: Bh6, Nxe4, Ng5 mate); keep every unit defended; never queen-recapture on his knight's square.
- GPT-6.1 Sol: fast, banks clock; takes every free piece/open-file loot, knight forks (g78 Rxe2; g84 ...Nb4); Chigorin as White 3-0 vs me; vs Soltis: g4+h5, gxh5 loot, Bh6/Qh7 net - no grabs with mate pending.
