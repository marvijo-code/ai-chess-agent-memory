# MEMORY (clocks 900+10)

## Record
- T36 R5 B v Sol, Taimanov 6.Be2: L m30. GOOD: 13...Kh8 vs his Qe1-g3+Be3 battery, 15...Qxe5! 16...Qxg3! queens off, 21...Bxf4 -> R+R vs R+R, +1 pawn. FATAL 26...Rxc2+??: his Be4 guarded c2 ALL GAME via e4-d3-c2 (d3 empty) - I verified 'c2 undefended' but never swept HIS attackers of my rook's landing square -> R for P. Then Kg8/Kf8 shuffles with f7/g7/h7, no luft, his Rd7 -> 30.Rd8#. 1 illegal try: bxc6 - my b5-pawn hits a4/c4, never backward.
- T36 R4 W v Sonnet, English 4K: L m42. 7.d3?? vs 6...e4: Nf3 unguarded since 3.g3 (g2 left f3, Qd1 blocked by my e2) -> 7...exf3 = N for P; correct 7.Nd2/Ne1. Held 20+ moves N+P down, then 33.Bd6?? 'defends d4 via e5' = two chained diagonals -> Rxd4; 38.Bd4?? fed Ra4 -> free B, ...d1=Q, m42. 1 illegal try: Nxe5 with NO knights on the board.
- T36 R3 W v DeepSeek, English/QGD: L m60. 17.Bxe4?? = B for P (sweep skipped enemy KNIGHTS: Nc5 hit e4); 31.Rc1? shuffled my rook OFF the d-file, boxed Bd2 lost only guard -> Rxd2; 44.Rc8+?? Bxc8 (empty e6-d7-c8) = R for B. GOOD: 36.exd4! won B+R for 2 pawns. 3 illegal tries.
- T36 R1 B v SF, Scheveningen 5.Qxd4: L m29. 11...Qb6?? Qxb6 - his Qe3 owned the empty a2-g8 diagonal (sweep checked pawns only); same move left Nc6 'defending' d5 (c6 never hits d5) -> 12.cxd5. 23...g6?? vs Qe3+Bg2 battery removed g7's guard of h6 -> Qxh6+/Qxg6+ net. 1 illegal try.
- T35 R5 B v SF, Spanish 4K: L m33. 7...Qe3+?? fxe3 = Q for P. From move 8 pure discipline: 0 illegal, still lost - one untraced move ends any defense.
- T35 R4 W v Sonnet, English 4K: L m43. 6...e4 7.Nxe4?? (Bg2's guard of e4 blocked by MY Nf3) Nxe4 = N for P. 21.Rxa7?? forgot his OTHER rook Ra8. 24.Rb1?? onto Rb2's b-file. Good: 31.gxh4!.
- T35 R3 B v DeepSeek, Taimanov: L m50. Good: 12...Nxd5!, Kxh5!. Bad: 13...exd5? counted Bb7's guard THROUGH my Nc6; 20...Bd7?? 0 guards vs Rc7. 4 illegal tries.
- T35 R1 W v Sol, English/reversed Sicilian: L m23. 13.Rd1?? (named recapture Bxd5 never played); 17.Qe3?? dxe3 = Q for P; 19.Rdb1 Bxa1. 2 illegal tries.
- T34 R5 W v SF, Maroczy: L m48. 8.Nc7+?? Qxc7 (Qa5 covered c7) = N for P; 40 passive moves lost.
- T34 R4 B v Sonnet, Taimanov: L m30. 17...Qxe5?? (Nf6 never hits e5) = Q for P; 18...Bd6?? (Bd7 blocked Rd8).
- T34 R3 W v DeepSeek, Rauzer: L m26. 13.g5?? Bxd4! (d4's only guard Qd2) = Q for B.
- T34 R1 B v Sol, Scheveningen: L m24. 14...b5? 15...Qb6?? (b5+c6 loose); 21...Qd3?? cxd3.

## Key lessons (check before EVERY move)
- CAPTURE = FULL DESTINATION SWEEP (fatal 26...Rxc2+??, T36R5): a capture is a move TO a square. Before taking, trace EVERY enemy slider's line to the destination square by square (his Be4-d3-c2, d3 empty, ate my rook), plus pawns and knights. 'Is the target undefended' describes HIS guards of HIS piece - it does NOT say my piece survives there. That bishop diagonal sat on the board for six moves while I wrote 'c2 guards: none'.
- BISHOP GUARD = ONE CONTINUOUS DIAGONAL (fatal 33.Bd6??): from d6 the e5-line runs to f4/g5/h6, never d4. Name the full unbroken line; a bend = no guard. HIS bishop guards obey the same walk - never call a square loose without walking every enemy bishop diagonal (T36R5: e4-d3-c2).
- UNGUARDED PIECES OUTLIVE THE PUSH (fatal 7.d3??): a pawn push that removes a guard (g3 unguarded f3) leaves the hole until something REPLACES it. Every move: which of my pieces have NO current guard?
- ROOK LINES: (a) never park a piece alone on an enemy rook's open rank/file - a rook attacks its FIRST blocker (38.Bd4?? Rxd4); (b) never walk my rook onto an enemy rook's file (24.Rb1??); (c) with two enemy rooks name EACH one's lines before moving (21.Rxa7?? forgot Ra8).
- KNIGHTS GO ON THE SWEEP LIST (fatal 17.Bxe4??): attackers = PAWNS + SLIDERS + EVERY ENEMY KNIGHT (c5-knight: a4/a6/b3/b7/d3/d7/e4/e6).
- SHUFFLE = GUARD DUTY LOSS (31.Rc1?): before ANY move, shuffles included, name what the moved piece WAS guarding on the old board.
- QUEEN DESTINATION SWEEP (fatal 5x): before ANY queen move - quiet, capture or CHECK - list every enemy PAWN attacking the destination AND every enemy SLIDER's line traced square by square. A check answered by a pawn capture = Q for P.
- KNIGHT GEOMETRY: recite the 8 squares before trusting a knight guard. c6: a5/a7/b4/b8/d4/d8/e5/e7 - NEVER d5. f6: d5/e4/d7/e8/g4/g8/h5/h7 - never e5.
- CHECKS PASS THE SAME SWEEP (44.Rc8+?? Bxc8): before delivering ANY check run the full destination sweep (pawns, sliders, knights, king flights).
- SELF-GUARD ILLUSION: the piece being MOVED never defends its own destination; exclude the mover from guard counts.
- BLOCKED DEFENDER: before any capture or move onto a 'defended' square, walk the line SQUARE BY SQUARE and name each occupant. A guard through any piece DOES NOT EXIST.
- ROOK-7TH = MATE NEXT (T36R5): my Kg8 + f7/g7/h7 + his rook reaching d7 hitting f7 = 30.Rd8#. When down material make luft (...h6 - first verify his battery does not punish it) BEFORE shuffling; MATE FIRST applies to rook endings too.
- KINGSHIELD PUSHES vs Q+B BATTERY: g7 guards h6 AND f6. Never push ...g6 while his queen + dark bishop aim at my castled king (T36R1). GOOD model: 13...Kh8 (T36R5) - then trade queens at first contact.
- FINISH THE NAMED SEQUENCE: the named recapture must BE the move played. After HIS capture the first question is 'what recaptures'. GOOD: Rxd8/Rxe7, Kxf1!.
- DESTINATION ATTACKERS: list every enemy piece attacking the destination (pawns one push away included) and all my guards from real geometry, excluding the mover.
- FORK REALITY: my check/fork is real only if nothing captures my piece on its destination - scan every slider's line first (8.Nc7+?? Qxc7). Verify HIS checks too: an undefended check loses to Kx.
- RECAPTURE FIRST / ONLY-QUEEN GUARD: after every trade re-count guards; a piece whose only guard is my queen is lost when his second attacker lands (13.g5?? Bxd4).
- MATE FIRST: after every his move ask what mates and what a pawn push OPENS (23...g6; exf6 -> Qxg7#; Rd7 -> Rd8#).
- DOWN MATERIAL: trade pieces, no grabs, blockade - vs SF expect NO repetition rescue. Discipline holds at the blunder moment but cannot rescue a hole. R-vs-B endings: bishop OFF the rook's open lines; KING blockades passers.
- MATERIAL FROM THE BOARD: recount after every capture; know my remaining pieces (Nxe5 with NO knights = instant rejection).
- SCAN each move: his last move's new attacks; checks and knight jumps; pawn breaks both ways; my loose pieces and their CURRENT guards; what each pawn push abandoned. Re-run guard counts after every capture or king move.
- LEGALITY: destination empty and not mine, path empty, SAN fits; disambiguation Rad8/Red8; castling needs both squares empty; PAWNS ATTACK DIAGONALLY FORWARD ONLY - a pawn that has advanced never guards or captures backward (b5 hits a4/c4, never c6: illegal bxc6 T36R5). BOXED PIECE RULE: after ONE rejection redraw and pick a DIFFERENT piece/idea.
- CLOCK: blunders, not pace, decide. The LIST is the check, not the duration (30 s on Qb6 still skipped sliders; 57 s still missed the guard hole).

## Openings
- W English 4 Knights v Sonnet (notes/english-white.md): ...e5/...Nf6/...Nc6/...Bb4/...O-O/...e4 every time. 6...e4: ONLY 7.Nd2/7.Ne1 (Nxe4 fails - Bg2 blocked by Nf3; d3 leaves Nf3 unguarded since g3). Otherwise equal; all losses were execution.
- W English v ...Nf6/...e6/...d5 QGD-style: cxd5/Bg2/Nf3/O-O/d4/e3/Bd2/Re1, trade c5 - comfortably equal.
- B Taimanov v 6.Be2 quiet line (notes/sicilian-black.md): e6/Nc6/a6/Be7/O-O/Qc7/b5/Bb7 solid to move 12, WORKED v Sol (T36R5). After any Nd5/exd5 exchange, ...Nxd4 first - never ...exd5 while my knight blocks Bb7's d5-diagonal.
- B Scheveningen/Taimanov order v SF 5.Qxd4 (notes/scheveningen-black.md): while his Qe3 stands NOTHING of mine on b6/c5/a7 (a2-g8 diagonal is hers); ...O-O does not solve d5 after 10.c4 - need ...Qd7 or ...b5 first.
- B Spanish Four Knights v SF (notes/spanish-four-knights-black.md): after 6.Nxe5 Qd4 7.Nf3 the ONLY plan is 7...Qxe4+ - never the e3 sortie.
- W Maroczy v ...g6 Sicilian (notes/white-maroczy.md): c4/Nc3/Be3/Be2/O-O clamp. V ...Qa5 DROP the Nb5/Nc7+ trap.
- W Rauzer v ...d6 Sicilian (notes/sicilian-white-rauzer.md): verify d4's SECOND guard before any kingside pawn push.
- B Scheveningen v Sol (notes/sicilian-black.md): ...b5 only after ...Nxd4 or ...Be6; answer e5/f6 breaks with ...Bxf6/...Nd7, keep g7 guarded twice.

## Opponents
- Sol: fast, zero illegal, banks clock (~25 s thinks, 12:47 left at m30 mate). As White Taimanov: Be2/O-O/f4/Kh1/Bf3/Qe1-g3 battery + e5 break; hxg3 opens the h-file when queens trade. When I win a pawn he simplifies (bishop-trade offer, Rad1/Rxd8), defends loose pawns with bishop+king, punishes capture-destination errors instantly, mates the un-lufted back rank. As Black v my English: 1...e5, early ...d5 tension, punishes missed recaptures. Scheveningen: Kh1, Qe1-g3, a4 vs ...b5. No repetition offers once ahead.
- Sonnet 5.5: 3 games, 0 wins. As Black v my English: ...e5 ...Bb4 ...O-O ...e4! - he KNOWS 3.g3 permanently unguards f3; takes every loose unit the move it loosens, converts piece-up with doubled rooks and king invasion. As White Taimanov: Be3, f4, Kh1, Qe1-g3, e5! break.
- DeepSeek V4.1 Flash: fast, calm, 3 invalid tries in T36R3. As Black v my English: QGD-style, grabs loose queenside pawns, converts piece-up patiently. As White v my Taimanov: quiet 6.Be2/O-O/Be3/f4, likes Nd5 trade-offers - verify HIS piece's attackers.
- SF 19: instant, zero illegal. As White v my ...e6 Sicilian order: 5.Qxd4!, Qe3, e5/Nd5 trade, Bd2, c4-cxd5 break, then g4/h4 storm - Qe3+Bg2 battery nets Qxh6+/Qxg6+ the moment I push ...g6; while his Qe3 stands b6/c5/a7 are forbidden ground. Spanish 4K Bb5 5.Bxc6 6.Nxe5! punishes queen sorties. No repetition rescue when far ahead.

## Notes
notes/english-white.md; notes/sicilian-black.md; notes/sicilian-white-rauzer.md; notes/spanish-four-knights-black.md; notes/white-maroczy.md; notes/scheveningen-black.md
