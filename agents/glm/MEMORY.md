# MEMORY (clocks 900+10)

## Record
- T35 R1 W v Sol, English/reversed Sicilian: L m23. 12.Nd5 Nxd5 13.Rd1?? (named recapture Bxd5 never played) = piece down; 17.Qe3?? dxe3 (d4-pawn hits e3) = Q for P; 19.Rdb1 Bxa1 wasted a rook; Rb1+ Bf1 Bh3 Rxf1#. 2 illegal tries (Rac1: my own Bc1 on c1; Qxd4: Qe2 not on d4's line).
- T34 R5 W v SF, Maroczy: L m48. 7.Nb5?! a6 8.Nc7+?? Qxc7 (Qa5 covered c7) = N for P; 40 moves passive defense lost.
- T34 R4 B v Sonnet, Taimanov: L m30. 17...Qxe5?? (Nf6 never hits e5) = Q for P; 18...Bd6?? (Bd7 blocked Rd8) Qxd6.
- T34 R3 W v DeepSeek, Rauzer: L m26. 13.g5?? Bxd4! (d4's only guard Qd2) = Q for B.
- T34 R1 B v Sol, Scheveningen: L m24. 14...b5? 15...Qb6?? (b5+c6 loose); 21...Qd3?? cxd3.

## Key lessons (check before EVERY move)
- FINISH THE NAMED SEQUENCE: when the plan is 'capture, then recapture' (12.Nd5 Nxd5 13.Bxd5, T35 R1), the recapture is played IMMEDIATELY - a different move (13.Rd1??) forfeits the whole piece. After HIS capture the first question is always 'what recaptures and what does the recapturer leave unguarded', not 'what else do I want'.
- QUEEN vs ENEMY PAWN: before every queen move, list every enemy pawn hitting the destination square (pawns attack exactly 2 squares). 17.Qe3?? dxe3 = Q for P - I had even written 'd4 defended by Bf6', but d4's DEFENSE is irrelevant; what matters is what d4 ATTACKS. Sweep the 8 neighbor squares of every queen destination.
- FORK REALITY: a check or fork is only real if NOTHING captures my checking piece on its destination - scan EVERY slider's diagonal/rank to that square first. 8.Nc7+?? met Qxc7 (T34 R5 = N for P). Blocking a check: count every enemy piece hitting the block square and every king flight BEFORE committing the blocker.
- CAPTURE DESTINATION: before ANY capture, name MY defenders of the LANDING square from real geometry, not habit. Knight on f6 hits e4/d5/d7/e8/g4/g8/h5/h7 - NEVER e5 (17...Qxe5?? = Q for P, T34 R4). Count his attackers too; 0 guards = the move does not exist. Pawn diagonals: g6 defends h5, h6 defends g5.
- BLOCKED DEFENDER: trace every guard line THROUGH my own pieces before counting it. 18...Bd6?? (T34 R4) trusted Rd8 to cover d6 but Bd7 stood in between -> Qxd6. Own piece on the 7th/back rank can block guards and blockades.
- RECAPTURE FIRST (general form of the T35 rule): after his capture, name MY recapturer and what that recapturer leaves unguarded (14.Qxd4 met Nxd4, T34 R3). Recount material FROM THE BOARD after every capture before choosing a plan.
- ONLY-QUEEN GUARD: after EVERY trade and pawn push, re-count guards of each attacked piece. A piece whose only guard is my queen is lost when his second attacker lands (13...Bxd4; 24...Qxf4+/25...Qxd2). Pawn-takes-queen is the most common gift.
- ATTACKED PIECE CAPTURES FIRST: 13.g5?? 'drove' Nf6 but the knight took d4. Before a pawn attack on a piece, check what it captures en route and what my push unguards.
- MATE FIRST: after every his move ask what mates and what a pawn push OPENS. 23.exf6 enabled Qxg7# (T34 R1); 26...Qe1#: K behind f2/g2/h2 = back-rank mate once the last rank-1 guard falls.
- DOWN MATERIAL: trade pieces, no grabs, hunt repetition. Do NOT compound a blunder with 'activity gestures' (18...Bd6??, 19.Rdb1 Bxa1) or new pawn-hunts - when mating is on the board he never cooperates with repetition. Play the safest solid move.
- SCAN each move: his last move's new attacks; checks and knight jumps; pawn breaks both ways; my loose pieces and their CURRENT guards. Re-run the guard count after every capture or king move.
- LEGALITY: illegal tries cost 17-56 s and tilt (T35: Rac1 rejected - c1 held my OWN bishop; Qxd4 rejected - Qe2 not on d4's line; Nxe6+ with knight on c3, T34 R5). Before sending: destination not MY piece AND not occupied at all, path empty, SAN fits, the piece can actually move there. After ONE rejection redraw the board and pick a DIFFERENT idea, never resend.
- CLOCK: every game ends 14+ min up; blunders, not pace, decide. A 56 s think (13.Rd1) that skips the recapture is worse than a 5 s one that plays it.

## Openings
- W English/reversed Sicilian v ...e5 (notes/english-white.md): c4/Nc3/Nf3/g3/Bg2/O-O/d3/e4 clamp. Opening was fine to move 11; the loss was execution (missed recapture, queen into a pawn). Line reusable.
- W Maroczy v ...g6 Sicilian (notes/white-maroczy.md): c4/Nc3/Be3/Be2/O-O clamp. V ...Qa5 DROP the Nb5/Nc7+ trap; plain development instead.
- B Taimanov/Scheveningen v Sonnet (notes/sicilian-black.md): 5.Nc3 a6 6.Be2 setup reached full development with no opening problem. Losses came at moves 17-18 (capture scans), not the opening. ...b5 timing lessons live in the note.
- W Rauzer v ...d6 Sicilian (notes/sicilian-white-rauzer.md): 8.O-O-O, 9.f4, 10.Be2, 11.g4 fine; verify d4's SECOND guard before ANY kingside pawn (candidates 13.Nxc6 / 13.Nde2 / 13.f5 - calculate first).

## Opponents
- Sol: fast, never flagged, zero illegal. As Black v my English (T35): 1...e5, early ...d5 tension, ...Nb6 keeps the knight, then plain Qd7/Rad8 development; punished my missed recapture (Nxd5!) and pawn-takes-queen (dxe3) instantly, then Rb1+...Bh3/Rxf1# conversion. In the Scheveningen he plays Kh1, Qe1-g3 battery, a4 vs ...b5, e5 break, Bxa8 grab; takes every loose unit. No repetition offers once ahead.
- SF 19: instant, zero illegal. As Black: ...g6/...Nf6/...Qa5; took my fork fantasy (Qxc7), converted piece-up patiently to a back-rank Rxd1#. Down a piece vs SF expect ZERO gifts; trade and repeat, never complicate.
- Sonnet 5.5: as White Taimanov: 8.Be3, 9.f4, 10.Kh1, 11.Qe1-g3, 14.Nxc6 bxc6, 16.e5! break. Takes every free piece instantly, converts Q-up via Bxh6/Qg7#. Never hand him a loose unit.
- DeepSeek V4.1 Flash: very fast, calm, zero illegal. Pounces on only-queen-guarded pieces (13...Bxd4, 24...Qxf4+/25...Qxd2); converts Q-up with plain trades + back-rank mate. As Black v my Rauzer: ...e6/...Nc6/...Be7/...O-O, ...a6/...Bd7/...b5/...b4, ...f6 to blunt g5, ...d5.
