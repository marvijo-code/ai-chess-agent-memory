# MEMORY (clocks 900+10)

## Record
- T34 R4 B v Sonnet, Taimanov: L m30. 17...Qxe5?? (I counted Nf6 as an e5-guard; a knight on f6 does NOT hit e5) = Q for P, then 18...Bd6?? Qxd6 (my Bd7 blocked Rd8's guard of d6). Finished Q+R+B vs K+P.
- T34 R3 W v DeepSeek, Rauzer: L m26. 13.g5?? after 12...Bxf6 hit d4 (Nd4's only guard Qd2): 13...Bxd4! 14.Qxd4 Nxd4. Later 25.Kb1? Qxd2 26...Qe1#. 5 illegal tries.
- T34 R1 B v Sol, Scheveningen: L m24. 14...b5? 15.axb5 15...Qb6?? (b5 AND c6 loose) 16.bxc6!; killer 21...Qd3?? 22.cxd3.

## Key lessons (check before EVERY move)
- CAPTURE DESTINATION: before ANY capture, name MY defenders of the LANDING square on the final board, derived from geometry, not habit. Knight on f6 hits e4/d5/d7/e8/g4/g8/h5/h7 - NEVER e5 (17...Qxe5?? = Q for P, T34 R4). Count his attackers of that square too; 0 guards = the move does not exist.
- BLOCKED DEFENDER: trace every guard line THROUGH my own pieces before counting it. 18...Bd6?? (T34 R4) trusted Rd8 to cover d6, but Bd7 stood in between -> Qxd6 for free. Same class: own pawn/piece on the 7th rank blocking back-rank guards (Claude's rule).
- RECAPTURE FIRST: after his capture, name MY recapturer and what that recapturer leaves unguarded (14.Qxd4 'restored balance' but met Nxd4, T34 R3). 15...Qb6?? (R1) left b5 AND c6 loose; 15...axb5 was there.
- ONLY-QUEEN GUARD: after EVERY trade and pawn push, re-count guards of each attacked piece. A piece whose only guard is my queen is lost when his second attacker lands (13...Bxd4; 24...Qxf4+/25...Qxd2). Pawn-takes-queen is the most common gift (21...Qd3?? cxd3).
- ATTACKED PIECE CAPTURES FIRST: 13.g5?? 'drove' Nf6, but the knight simply took d4. Before a pawn attack on a piece, check what it captures en route and what my push unguards.
- MATE FIRST: after every his move ask what mates and what a pawn push OPENS. 23.exf6 enabled Qxg7# (R1); 26...Qe1#: Kb1 behind f2/g2/h2 = back-rank mate once the last rank-1 guard falls. Count g7/h7/back-rank guards each move.
- DOWN MATERIAL: trade pieces, no grabs, hunt repetition. And when already lost or just blundered, do NOT compound with an 'activity gesture' (18...Bd6?? was a lost-position kick); play the safest solid move.
- SCAN each move: his last move's new attacks; checks and knight jumps; pawn breaks both ways; my loose pieces and their CURRENT guards. Re-run the guard count after every capture or king move.
- LEGALITY: illegal tries cost 17-40 s and tilt. Before sending: destination not MY piece, path empty, SAN fits (one rook: plain Rd1; two rooks both reaching: file+R). After ONE rejection, redraw the board and pick a DIFFERENT idea, never resend.
- CLOCK: every game ends 14+ min up; blunders, not pace, decide. The legality scan is free time.

## Openings
- B Taimanov/Scheveningen v Sonnet (notes/sicilian-black.md): 5.Nc3 a6 6.Be2 setup reached full development with no opening problem. Losses came at moves 17-18 (capture scans), not the opening. R1 lessons on ...b5 timing live in the note.
- W Rauzer v ...d6 Sicilian (notes/sicilian-white-rauzer.md): 8.O-O-O, 9.f4, 10.Be2, 11.g4 fine; verify d4's SECOND guard before ANY kingside pawn (candidates 13.Nxc6 / 13.Nde2 / 13.f5 - calculate first). Watch his ...b5/...b4 storm vs my long-castled king (guards of c3/b2).

## Opponents
- Sonnet 5.5: as White Taimanov: 8.Be3, 9.f4, 10.Kh1, 11.Qe1-g3, 14.Nxc6 bxc6, 16.e5! break. Takes every free piece instantly (free queen at 18.Qxe5), converts Q-up via Bxh6/Qg7#. Fast, banks clock, zero illegal moves. As White in the earlier Scheveningen: a4 to restrain ...b5, e5 break, Bxa8 rook grab, Qxg7# behind f6 support. Never hand him a loose unit.
- DeepSeek V4.1 Flash: very fast (1-5 s), calm, zero illegal moves. Pounces on only-queen-guarded pieces (13...Bxd4, 24...Qxf4+/25...Qxd2); converts Q-up with plain trades + back-rank mate. As Black v my Rauzer: ...e6/...Nc6/...Be7/...O-O, ...a6/...Bd7/...b5/...b4, ...f6 to blunt g5, ...d5.
- Sol: fast, never flagged; Open Sicilian with Kh1, Qe1-g3 battery, a4 vs ...b5, e5 break, Bxa8 grab; takes every loose unit; converts piece-up into Qxg7#.
