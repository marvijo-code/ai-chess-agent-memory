# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue (g1-g96)
- notes/ruy-lopez-black.md - Chigorin/Breyer Black
- notes/ruy-lopez-white.md - Ruy White
- notes/sicilian-black.md - Alapin/Dragon Black (g90,g91,g95)
- notes/sicilian-soltis-black.md - Soltis Black (g94)
- notes/sicilian-yugoslav-black.md - 9.O-O-O d5 Black
- notes/sicilian-dragon-white.md - Yugoslav White
- notes/caro-kann-white.md - Caro White (g89)

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- SELF-BAN: a move my note/scan called bad/illegal is FORBIDDEN; play the traced alternative; one rejected attempt -> a different move.
- Attackers/defenders only from the FINAL board with paths; an untraceable unit is not one (g88 15...Rxe4??).
1. Legality: my turn; my pieces; PATH clear of EVERYTHING; re-read the board after a capture. BISHOPS trace to the edge (g94 Bxc3 blocked by own Nf6). Two units to one square -> full name.
2. KNIGHT SWEEP FIRST: his knights' 8 squares; my destination or capture landing square hit -> he recaptures (g87,g85). Before ANY queen placement (g84 Qc2/...Nb4; g95 Nc3 hits Qd5).
3. HIS last move: every attacker of my destination - rook, bishop, knight, PAWN; if it hits MY QUEEN she moves THAT move: 'defended' never counts, defenders only recapture the attacker (g95 7...e6 -> 8.Nxd5 = Q for N; g41,g94). Attacked+undefended -> reject; save my hit piece NOW (g78). His KING hits its 8 neighbours.
4. PAWN SWEEP before ANY piece move: never a minor/rook onto a pawn-guarded square, even defended; list his pawns' capture squares first - a just-moved or BLOCKED pawn still hits both diagonals. g96 18.Bg6?? fxg6 = B for nothing (same class g89/g92 Bg5?? hxg5). Re-list pawn guards after ANY trade (g86).
5. CAPTURES: name every recapturer + his second attacker; write HIS recapture AND mine; his last -> don't start. Level/down: NO sacs. PIN: his B/R/Q x-raying my piece to my K/Q = cannot move or recapture (g90).
6. QUEEN destination scan: no queen capture on a defended square (g87); his QUEEN's own lines count, her landing square too - g96 21.Qd5+?? beside Qd6 with no defender -> Qxd5; A CHECK IS NOT SAFETY. A 'trade' needs MY recapturer that SURVIVES; none = Q for P/minor/nothing (g91 19...Qxd6??; g96). Walk his rook lines + bishop diagonals too (g89 Qh3?? Rxh3).
7. Mate nets & loose pieces BEFORE any move: Qh2/Rh1 h-file (Nf6 = h7's only guard); Qh6+Ng5=Qxh7#; Bb7+Qd5 = Qxg2# once e4 clears (g96 22...e3 23...Qxg2#, my f2/g2 box the king); a loose minor/rook needs its destination attacked by NOTHING.
8. Down material: keep queens; repetition = half point; no N-for-B/R-for-B 'trades'; no claw-back grabs. K+P race: king IN FRONT of the passer (g92). Vs SF/Sol a piece lead = lost (g96: mate 5 moves after my bishop hung).
9. Time: routine <=15 s, book <=10 s; <3 min <=5 s; <1 min 1-2 s. Long thinks never prevented a blunder (g89-g96; g96 18.Bg6 took 41 s).
- Reread my last plan note each move: a danger it names is the candidate's first check (g94).

## Openings
- QGD Tartakower W (0-1 Sol, g96): 5.Bg5 h6 7.Bh4 b6 8.Bd3 Bb7 9.O-O Nbd7 10.Rc1 c5 11.cxd5 exd5 12.Bg3 Rc8 13.Ne5 Nxe5 14.Bxe5 Bd6 15.Bxd6 Qxd6 16.dxc5 bxc5 =; after 17.Bf5 Rcd8 play Be4/Bc2 or b4/Ne2 - NEVER Bg6?? (f7/h7 pawns), never Qd5+ into Qd6.
- Italian 4.d3 d5 (0-3): 5.exd5 Nxd5 6.O-O Bc5 7.Bxd5 Qxd5 =; 13.Bd4?? TRAP (Q for B, no recapturer). Play Rfe1/Rc1, Nf1-g3/Be3-f2, h3/c3; NEVER Bg5 once h3/h6 is in.
- Caro-Kann Classical W (0-1): 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7 8.h5 Bh7 9.Bd3 Bxd3 10.Qxd3 e6 =; 13.Bg5?? hxg5! keep the dark bishop on e3/f4 while h5/h6 is fixed.
- Ruy Chigorin W (0-4): 13.cxd4: only Nf3 guards d4 (Qe2 doesn't) -> Nf1 first; keep Be3 when ...Nc4 looms; Bd3+Qc2 loses to ...Nb4! (g84).
- QGD Lasker W: 13.Be2 e5 -> 14.dxe5!; if ...exd4, 15.exd4! (pawn) then ...Nxd4 level.
- Chigorin B: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; his bishop hitting my queen = she moves THAT move (g41).
- Dragon B: ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; Rauzer 11...gxf6!; 9.O-O-O d5: 12.Nxd5 cxd5! 13.Qxd5 -> ONLY ...Qc7!; never Qd8 while Rd1 faces it.
- Alapin B: 5.Qxd4 ...Nc6 ...g6 ...Bg7 ...O-O ...Nc5 =; no ...Nb4, no knight to d4, no ...b5 while Rd1 faces Qd8; 3.e5 Nd5 7.Bc4 Nb6 8.Bb5 Bd7 9.Nc3 a6 10.Bxc6 -> 10...bxc6! (10...Bxc6?! 11.d5! +2); g95 6.cxd4 6...Nf6?! 7.Nc3!; prefer 6...e6/e5.
- Soltis 9.Bc4 (0-8): 14.h5 Nxh5! 15.g4; keep Nf6 (h7 guard); 16.g5 -> ONLY ...Nh5; 19.hxg6 -> ...fxg6; no e4/Rxe4 grabs. g94: after 15.Kb1 NO ...Qa5 (Nb3 hits her) - play ...Ne8/...Qd7 first.
- 4N B: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon W: keep Bc5 defended (g42).

## Opponents
- Stockfish 19: ~0 s/move, never errs; punishes loose units, queens on attacked lines/screens, queens left under attack (g95 8.Nxd5 won her for a knight); his levers open files onto my queen; down: aim for repetition; g91 ...Bxc6?! let 11.d5! (+2).
- Sonnet 5.5: banks clock, 0-60 s/move, takes EVERY free/attacked unit; keep every unit defended; never queen-recapture on his knight's square; converts a piece up cleanly (g92).
- GPT-6.1 Sol: fast, banks clock; takes every free piece and tempo (g94 17.Nxa5; g96 18...fxg6 took the 'sac'); Chigorin 3-0 as White vs me; converts a piece lead to mate in ~5 moves, out-clocked me 15:51 to 8:34.
