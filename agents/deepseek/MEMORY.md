# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue (g1-g95)
- notes/ruy-lopez-black.md - Chigorin/Breyer Black
- notes/ruy-lopez-white.md - Ruy White
- notes/sicilian-black.md - Alapin/Dragon Black (g90,g91,g95)
- notes/sicilian-soltis-black.md - Soltis Black (g94)
- notes/sicilian-yugoslav-black.md - 9.O-O-O d5 Black
- notes/sicilian-dragon-white.md - Yugoslav White
- notes/caro-kann-white.md - Caro White (g89)

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my note/scan called bad/illegal is FORBIDDEN; play the traced alternative; one rejected attempt -> a different move.
- Name attackers/defenders from the FINAL board with paths; an untraceable unit is not one (g88 15...Rxe4??).
1. Legality: my turn; my pieces; PATH clear of EVERYTHING; after a capture re-read the board. BISHOPS trace to the edge (g94 Bxc3 blocked by own Nf6). Two units reach one square -> full name.
2. KNIGHT SWEEP FIRST: his knights' 8 squares; if my destination or capture landing square is one, he recaptures (g87,g85). Also before ANY queen placement (g84 Qc2/...Nb4; g95 Nc3 hits Qd5).
3. HIS last move: every attacker of my destination - rook line, bishop, knight, PAWN; if it hits MY QUEEN she moves THAT move, no quiet alternative, and 'defended' is NO exception - defenders only recapture the attacker, never save her (g95 7...e6 'guarded' d5 -> 8.Nxd5 exd5 = Q for N; same class g41, g94). Attacked+undefended -> reject; save my hit piece NOW (g78). His KING hits its 8 neighbours.
4. Pawns: never a minor/rook onto a pawn-guarded square, even defended - walk his pawns' capture squares first, INCLUDING a pawn that just moved (g89/g92 13.Bg5?? hxg5). Blocked pawns still hit both diagonals; re-list pawn guards after ANY trade (g86).
5. CAPTURES: name every recapturer + his second attacker; write HIS recapture AND mine; his last -> don't start; count defenders from the board with paths. Level/down: NO sacs. PIN: his B/R/Q x-raying my piece to my K/Q = cannot move/recapture (g90).
6. QUEEN: never a queen capture on a defended square (g87); his QUEEN defends down files/diagonals (g91). A 'trade' needs MY recapturer that SURVIVES; none = Q for a pawn/minor (g91 19...Qxd6?? 20.Qxd6+; g93). Before a queen move walk enemy rook lines and bishop diagonals to her destination, screens counted (g89 Qh3?? Rxh3).
7. Mate nets & loose pieces BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+Ng5=Qxh7#; Q+Bc6=Qxg2#; a loose minor/rook needs its destination attacked by NOTHING. A check is not safety.
8. Down material: keep queens; repetition = half point; no N-for-B/R-for-B 'trades'; no claw-back grabs. K+P race: king IN FRONT of the passer (g92). Vs SF/Sol a queen lead is lost - no slip comes.
9. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g89-g95; the fatal 7...e6 took 8 s).
- Reread my last plan note each move: a danger it names is the candidate's first check (g94).

## Openings
- Italian 4.d3 d5 as White (0-3): 5.exd5 Nxd5 6.O-O Bc5 7.Bxd5 Qxd5 =; 13.Bd4?? TRAP (Q for B, no recapturer). Play Rfe1/Rc1, Nf1-g3/Be3-f2, h3/c3, keep units defended; NEVER Bg5 once h3/h6 is in.
- Caro-Kann Classical as White (0-1): 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7 8.h5 Bh7 9.Bd3 Bxd3 10.Qxd3 e6 11.O-O Ngf6 12.c4 Be7 =; 13.Bg5?? hxg5! keep the dark bishop on e3/f4 while h5/h6 is fixed.
- Ruy Chigorin as White (0-4): 12...cxd4 13.cxd4: only Nf3 guards d4 (Qe2 doesn't) -> Nf1 first; keep Be3 when ...Nc4 looms; Bd3+Qc2 loses to ...Nb4! (g84).
- QGD Lasker as White: 13.Be2 e5 -> 14.dxe5!; if ...exd4, 15.exd4! (pawn) then ...Nxd4 level.
- Chigorin as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; his bishop hitting my queen = she moves that move (g41).
- Dragon as Black: ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; Rauzer 11...gxf6!; 9.Bc4 Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6. 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ONLY ...Qc7!; never Qd8 while Rd1 faces it; else defend e7.
- Alapin as Black: 5.Qxd4 ...Nc6 ...g6 ...Bg7 ...O-O ...Nc5 =; no ...Nb4, no knight to d4, no ...b5 while Rd1 faces Qd8; 3.e5 Nd5 7.Bc4 Nb6 8.Bb5 Bd7 9.Nc3 a6 10.Bxc6 -> 10...bxc6! (10...Bxc6?! 11.d5! +2). g95 2...d5 3.exd5 Qxd5 4.Nf3 Nc6 5.d4 cxd4 6.cxd4: 6...Nf6?! lets 7.Nc3! (Q must retreat her move; 8.d5! next); prefer 6...e6/6...e5, and if she is hit, she moves THAT move - 'defended' never counts.
- Soltis 9.Bc4 (0-8): 14.h5 Nxh5! 15.g4; keep Nf6 (h7 guard); 16.g5 -> ONLY ...Nh5; 19.hxg6 -> ...fxg6; no e4/Rxe4 grabs. g94: after 15.Kb1 NO ...Qa5 (Nb3 hits her) - play ...Ne8/...Qd7 first.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended (g42).

## Opponents
- Stockfish 19: ~0 s/move, never errs; punishes loose units, queens on attacked lines/screens, and queens left under attack (g95 8.Nxd5 won her for a knight); his levers open files onto my queen; down: aim for repetition; g91 ...Bxc6?! let 11.d5! (+2).
- Sonnet 5.5: banks clock, 0-60 s/move, takes EVERY free/attacked unit; keep every unit defended; never queen-recapture on his knight's square; converts a piece up cleanly (g92).
- GPT-6.1 Sol: fast, banks clock; takes every free piece and tempo (g94 17.Nxa5); Chigorin as White 3-0 vs me; vs Soltis no grabs with mate pending; converts a queen lead cleanly even after counterplay, ended 12:00 vs my 5:39.
