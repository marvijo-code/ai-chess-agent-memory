# MEMORY (clocks 900+10)

## Record
- T35 R3 B v DeepSeek, Taimanov: L m50. Good: 12...Nxd5! punished his 12.Nd5??; instant recaptures (Rxd8, Rxe7); Kxh5! took his undefended Qh5+ after verifying all diagonals/pawns. Bad: 13...exd5? counted Bb7's guard of d5 THROUGH my own Nc6 = blocked guard; 14...Bd6 defended nothing, 15.Bxd5 15...Nb4?? chased nothing (16.Bb3) = pawn down with dead Bb7; 20...Bd7?? landed where Rc7 attacks with 0 guards = bishop lost. Longest defense from Q+2B down, mated m50. 4 illegal tries: O-O (Ng8 home), Rd8 (needed Red8 disambiguation), Rxe1+, Kf8 (his e7-pawn attacks f8).
- T35 R1 W v Sol, English/reversed Sicilian: L m23. 12.Nd5 Nxd5 13.Rd1?? (named recapture Bxd5 never played) = piece down; 17.Qe3?? dxe3 (d4-pawn hits e3) = Q for P; 19.Rdb1 Bxa1 wasted a rook. 2 illegal tries.
- T34 R5 W v SF, Maroczy: L m48. 8.Nc7+?? Qxc7 (Qa5 covered c7) = N for P; 40 moves passive defense lost.
- T34 R4 B v Sonnet, Taimanov: L m30. 17...Qxe5?? (Nf6 never hits e5) = Q for P; 18...Bd6?? (Bd7 blocked Rd8) Qxd6.
- T34 R3 W v DeepSeek, Rauzer: L m26. 13.g5?? Bxd4! (d4's only guard Qd2) = Q for B.
- T34 R1 B v Sol, Scheveningen: L m24. 14...b5? 15...Qb6?? (b5+c6 loose); 21...Qd3?? cxd3.

## Key lessons (check before EVERY move)
- BLOCKED DEFENDER - my #1 recurring fatal error (T34R4 twice, T35R3): before counting ANY bishop/rook guard, walk the line SQUARE BY SQUARE and name the occupant of each. A guard through my own piece DOES NOT EXIST. Doubly urgent after exchanges: the piece standing on that line may just have been captured or moved. If a plan needs a blocked bishop to see a square, resolve the blocker FIRST (...Nxd4 / move the knight), or change the plan.
- DESTINATION ATTACKERS: before placing ANY piece on a square, list every enemy piece attacking that square and all my defenders from real geometry. 20...Bd7?? had zero guards vs Rc7 (a whole bishop for free). Model move: 24...Re8 (guarded the attacked Be7).
- FINISH THE NAMED SEQUENCE: 'capture, then recapture' means the recapture is played IMMEDIATELY (T35R3 Rxd8/Rxe7 - worked; T35R1 13.Rd1?? = piece lost). After HIS capture the first question is 'what recaptures and what does it leave unguarded', not 'what else do I want'.
- QUEEN vs ENEMY PAWN: before every queen move, list every enemy pawn hitting the destination (pawns attack exactly 2 squares). 17.Qe3?? dxe3 = Q for P - d4's defense was irrelevant; what matters is what d4 ATTACKS.
- FORK REALITY, BOTH WAYS: my check/fork is only real if NOTHING captures my piece on its destination - scan every slider's line first (8.Nc7+?? Qxc7, T34R5). But verify HIS checks too: 37.Qh5+?? was undefended and Kxh5 won his queen.
- CAPTURE DESTINATION: before ANY capture, name MY defenders of the LANDING square from real geometry. Knight on f6 NEVER hits e5 (17...Qxe5??, T34R4). 0 guards = the move does not exist.
- RECAPTURE FIRST / ONLY-QUEEN GUARD: after every trade re-count guards of attacked pieces; a piece whose only guard is my queen is lost when his second attacker lands (13...Bxd4, T34R3).
- ATTACKED PIECE CAPTURES FIRST: 13.g5?? 'drove' Nf6 but the knight took d4. Before a pawn attack on a piece, check what it captures en route.
- MATE FIRST: after every his move ask what mates and what a pawn push OPENS (23.exf6 -> Qxg7#, T34R1; 26...Qe1# back rank).
- DOWN MATERIAL: trade pieces, no grabs, hunt repetition, longest defense is a valid plan (T35R3: 30+ correct defensive moves). Never compound with activity gestures (18...Bd6??, 19.Rdb1). Keep the LAST rook; blockade passers with the rook, not the king alone.
- SCAN each move: his last move's new attacks; checks and knight jumps; pawn breaks both ways; my loose pieces and their CURRENT guards. Re-run the guard count after every capture or king move.
- LEGALITY (4 tries T35R3): before sending - destination empty and not mine, path empty, SAN fits, piece can move there; DOUBLED ROOKS need file/rank disambiguation (Rad8/Red8); castling needs both squares empty and both home pieces moved; pawns attack DIAGONALLY (his e7-pawn made Kf8 illegal). After ONE rejection redraw the board and pick a DIFFERENT idea, never resend.
- CLOCK: every game ends 14+ min up; blunders, not pace, decide. A long think that skips the trace/recapture is worse than a fast one that plays it.

## Openings
- B Taimanov v 6.Be2 quiet line (notes/sicilian-black.md): e6/Nc6/a6/Be7/O-O/Nf6/Qc7/b5/Bb7 was solid to move 12. After any Nd5/exd5 exchange, the d5-pawn + Bb7 need the c6-knight OFF the b7-d5 diagonal (...Nxd4 first) - never commit ...exd5 while my own knight blocks the bishop's duty-diagonal.
- W English/reversed Sicilian v ...e5 (notes/english-white.md): clamp fine; T35R1 loss was execution (missed recapture, Q into a pawn). Line reusable.
- W Maroczy v ...g6 Sicilian (notes/white-maroczy.md): c4/Nc3/Be3/Be2/O-O clamp. V ...Qa5 DROP the Nb5/Nc7+ trap; plain development instead.
- W Rauzer v ...d6 Sicilian (notes/sicilian-white-rauzer.md): verify d4's SECOND guard before any kingside pawn.
- B Scheveningen v Sol (notes/sicilian-black.md): ...b5 only after ...Nxd4 or ...Be6; vs his a4 keep the c6-knight safe; answer his e5/f6 breaks with ...Bxf6/...Nd7, keep g7 guarded twice.

## Opponents
- DeepSeek V4.1 Flash: fast, calm, 1 illegal try (T35R3). As White v my Taimanov: quiet 6.Be2/O-O/Be3/f4/Qd2/Rad1; likes Nd5 trade-offers - verify HIS piece's attackers before 'trading' (12.Nd5?? hung to Nf6/e6/Bb7). His blunders happen (Rad1?!, Nd5??, Bb3??, Rc7??, Qh5+??) but he converts pawn-up endings methodically with the bishop pair, promotes and mates. Punishes undefended and only-queen-guarded units. As Black v my Rauzer: ...e6/...Nc6/...O-O, ...a6/...Bd7/...b5/...b4, ...f6 to blunt g5.
- Sol: fast, zero illegal. As Black v my English: 1...e5, early ...d5 tension, ...Nb6, then Qd7/Rad8; punishes missed recaptures and pawn-takes-queen instantly. In the Scheveningen: Kh1, Qe1-g3, a4 vs ...b5, e5 break, Bxa8. No repetition offers once ahead.
- SF 19: instant, zero illegal. As Black: ...g6/...Nf6/...Qa5; took my fork fantasy, converted piece-up patiently. Down a piece vs SF: trade and repeat, never complicate.
- Sonnet 5.5: as White Taimanov: 8.Be3, 9.f4, 10.Kh1, 11.Qe1-g3, 14.Nxc6 bxc6, 16.e5! break. Takes every free piece instantly. Never hand him a loose unit.
