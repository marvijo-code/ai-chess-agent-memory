# MEMORY - GLM 5.3 Flash

Last change: T78R6.2 White v DeepSeek L = FORFEIT ON AN ILLEGAL SAN ('Rfc1' with NO rook on f1; my Rfd1 at m18 had just left rooks a1+d1). The game was LEVEL to m18 in a French-advance build; 2 gated refuses earlier (cxd5, Qd3) meant the next send had to be a plainly legal UCI - it was not. Loss was output discipline, not chess. Read this file + listed notes at game start.

## FIRST, EVERY GAME
- EVERY SEND = UCI TYPED FROM THE CURRENT FEN, never a remembered SAN prefix ('Rf'-does-not-exist forfeited a level game). After ANY of my rook/queen moves re-walk WHICH squares my heavies occupy before naming the move; tools/heavy-squares.py prints them plus their legal UCI. With 2 invalids already banked the NEXT send is a verified-legal UCI, one try, zero style.
- 3 invalid tries on ONE move = forfeit; tries reset between moves. A TOOL-AVOID REFUSAL OF MY CANDIDATE IS ONE OF THOSE TRIES. STALE refusal (names a move I did not send) = resending my intended UCI is allowed and worked 10+ times. Refusal naming my ACTUAL candidate = that idea is DEAD: change piece AND idea, redraw from the FEN. IN CHECK: write the reply list ONCE - flights, blocks, CAPTURE OF THE CHECKER BY SQUARE (T78R6 m37: Kxe5! took his checking bishop clean) - pick ONE, send in 5-10 s. Forfeits cluster on check replies and gated floods (T75R4, T78R6 twice).
- GATED REFUSALS ARE THE CLOCK DEATH (T78R6 ~25 min at -8; T78R6.2 TWO refuses in a LEVEL game still burned the forfeit margin): when a keeper exists, take it instead of re-arguing a refuted idea - a different unit's quiet move in ONE try. Down heavy my sweeps flag EVERY move: read once, send the least-bad in ONE try.
- ENTOMB-BOOKKEEPING IS NOT A MOVE: a long think re-checking a trapped/stuck enemy piece changes nothing. ONE named plan + 10-20 s keepers; the stuck piece is HIS problem.
- KNIGHT-RESULT FORK = BISTRO CHECK: before MY knight jumps toward HIS camp, list HIS OWN one-jump checks (Nb6+; Ne6+; Nd5+). Run tools/knight-noted first.
- QUEENS OFF, PAWN UP, NO CASTLING = SHELTER FIRST (T78R5+R6): after ...Kxd8 play ...Bd7/...Bf8/...Rd8 so a PIECE, never the king, carries every pawn guard. A king move that RETAINS a guard duty (Kd6 on e6) is a check-magnet: every N-check gains HIM a tempo, a4+b4 drive my knight off, then Nxa8. Never let EVERY black move be a king step.
- BLOCKER ABANDON: one blocking piece is NOT defense - blocks jump away once the screen drains; sweep every piece I plan a block with.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS (T78R3 opened Be3's ray; dxc5! only).
- RECAPTURER'S LINES FROM ITS NEW SQUARE (T77R3 Bxd4+ forked Qb6+Kg7): before ANY capture I initiate, name HIS recapturer and its attack lines from the LANDING square. tools/recapture-scan.py.
- ATTACKED PIECE = RETREAT LIST FIRST, NEVER COUNTER-GRAB INTO HIS COVER: unattacked retreats (tools/escape-sweep.py) + defend/trade BEFORE any capture. Unavoidable: enumerate EVERY retreat, even the ugly one (28...Bf8 T77R1).
- MUTUAL ATTACK = HIS MOVE WINS THE RACE: before attacking/chasing an enemy piece, list MY defenders of MY lander on the NEW board. Never walk my rook off the open file my queen then stands on (T77R2).
- LANDING GUARD BEFORE PURPOSE: name MY units defending the destination after it lands, enemy file supports included (T78R4 Qd5?? missed Rd8's d-file). Sweep BEFORE any long think.
- OWN-BLOCKADE KILLS MY BREAK (T77R2 5.Bd3?): play the stored build ORDER (d4 first, then Be2/Bd3).
- FRONTIER PUSH = RECAPTURER ON THE NEW BOARD (T77R2 22.b5 lost P). Space is not worth permanent king duties.
- TOOL SILENCE BEATS NARRATIVE: run tools/see-sweep.py + pawn-destination-sweep.py FIRST, then search only non-flagged candidates. A tool AVOID is dead unless I name a square-walked refutation - a re-send costs a TRY.
- THREEFOLD IS DIRECTION-SENSITIVE: down/fortress = MY best move; even/better = MY loss. tools/threefold-scan.py names 2nd/3rd occurrences (AVOID when up).
- UP BIG = QUIET-PROGRESS CONVERSION: king anchor first, rook net, ONE break, at most ONE check in a row. Cycling checks = HE drives repetition.
- STORED FIX = ORDER, NOT INFO: at EVERY early move of a noted opening re-read that note's BANS (T77R5 7.f3). Others' trap notes = ban list too.
- QUEEN FACING MY KING = PIN FIRST.
- PAWN CAPTURE SQUARES COME IN PAIRS: tools/pawn-destination-sweep.py.
- A GUARD LIST IS GUESSWORK UNTIL SQUARE-WALKED: tools/see-sweep.py.
- A PAWN IS A GUARD ON ITS FORWARD DIAGONALS: before any push beside my king list the mover's remaining guards and his rays into my king after the grab (T75R4 ...g5 -> Nxh6 -> mate).
- PAWN PUSH = ITS LEFTOVERS: tools/pawn-destination-sweep.py on every non-book move.
- UNCAPTURABLE UNBLOCKABLE CHECK IS ALREADY MATE: tools/mate-net-scan.py before central thrusts.
- PAWN KICK AT A MINOR: sweep its escapes first; any capture-with-check kills the push (tools/kick-escape-sweep.py). A g5-class kick at MY Nf4: retreat to e2/e3 BEFORE the kick lands, never to h5 (near-trapped behind Bg4; cost a two-move bishop dance to save, T78R6.2).
- BOOK = 5-10 s; slow budget only for a concrete named plan. DOUBT = SAFE MOVE; a self-rejected candidate is dead (T75R3).
- TWO of my rooks/queens on one line = UCI ONLY, never SAN (T77R5; T78R6.2 'Rfc1' forfeit).
- LEDGER = THE FEN: after every capture write 'W ... / B ...'; recount one line each turn.
- TRADE-OFFER LANDING = all his attackers of the square from the piece list, never the prompting piece alone.
- CLOCK: vs a banker my long thinks are a pure transfer. Book 5-10 s, routine 10-20 s, HARD CAP 30 s unless a named forced win. Frozen even games the same cap (T78R4). UNEQUAL + LONG THINK = T78R6 KILL: from -1 to -8 at 1-6 min a move. Down heavy: fastest quiet keeper.

## CAPTURE LEDGER (before every send)
- KING-ONLY GUARD = losing recapture. tools/king-only-guard.py.
- I am the cheaper attacker against a once-guarded piece = trade-down sac is MY weapon; name his last recapturer by square, THEN its attack lines from that square.
- A fresh PAWN recapture kills the piece even after my queen recaptures; pawn attacked twice v defended once is lost: push, trade or accept.
- v Stockfish: donate NO first pawn; Open-Sicilian order 4.Nxd4! then Nc3/Be2/O-O; v ...g6 5.c4 AND THEN 7.f3! at once vs ...Qa5 - Qd2/Qd3 do NOT fix the pin (Bg7 backs d4). Miss now 4 games old.

## OPENING as White (v Nimzo-English)
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3 Nc5 6.d4 Ne4 7.cxd5 exd5 = LEVEL big chain (c3/d4/e5). T78R6.2 then DRIFTED: g3?/Nh3?/Qd3?/Bg2/O-O? over four quiet tempi bought nothing, left the Ne4 squatting, and ...g5! kicked my Nf4 into a saving dance. Next time: 8.f3! kicks the Ne4 at once (Nxe4 fxe4 = a full pawn front) before ...Bb4 sets the pin, or trade Nxe4 dxe4 early - free the f3-break or resolve the knight, never slow-build around it.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (7.Nxc6! bxc6 8.Bxc6+ = Q-for-B). Answer Bb5 with a PIECE: ...Bd7/...Nf6/...Be7 first. Pinned-Nc6 recap: ...bxc6 after Nxc6 loads it for Bxc6+ = Q-for-B; UNPIN FIRST.
- v the 4.c3 dialect (T78R5 AND R6, both L from pawn-up): 4.c3?! dxc3! 5.Nxc3 Nf6 6.e5 dxe5 7.Qxd8+ Kxd8 = pawn up, queens off. 8.Ng5! 8...Be6? 9.Bb5 Kc7 10.Nxe6+ fxe6!; then ONE planned shelter build (...Bd7/...Nbd7 on e6-duty BEFORE any king move), answer Bc4 with a piece move, accept e6 as a drip rather than a duty-walking king anchor.
- v the English Attack (f3/Be3/Qd2/O-O-O/g4-h4): confirmed twice with the ...Nxd4/...e5 counterstrike (12...Nxd4! 13.Bxd4 e5!); see notes/scheveningen-black.md.
- 2...d6 6.Be2 build (v Sol, DeepSeek, Muse, Sonnet): ...Be7 ...O-O ...Qc7 ...a6 then ...b5 ...Bb7, ...Nb6 hits d4; LEVEL to m20 in ALL recorded games; every loss came AFTER m20. With material banked the wins were TRADES and holds.

## FROZEN ENDGAME (two verdicts)
- FLAG WIN v MUSE (T78R3, equal, queens off m43): freeze every unit on ONE named job, pass at 6-30 s while he burns 1-3 min. HIS CLOCK is the win condition - only while it visibly bleeds. Same shape v SONNET has NO flag (T78R4): zero-refusal keeper repeats instead.
- +2P -N MODEL v SF (T77R5, held ~45 moves): wall c3/c4/e4/f3/g3, Bf1/Be2 on d3, rooks c2+d2, K g1/g2; his rooks entombed behind his own Nc5.
- A FORTRESS MUST STOP FORCING CHECKS: run his rook-check chains before settling; every block survives the checker or has a 2nd heavy piece behind.
- Shell: every unit double-guarded or parked behind HIS blockers; ONE rook permanently owning my pawn pair; king anchors the wing; NOTHING else moves. ACCEPT THE DRIPS: a 1-pawn loss is the cheapest path, never loosen the shell to save a drip.
- DRIVE THE THREEFOLD when down; UP +5 the same loop is MY loss.

## OPPONENTS (one-liners)
- STOCKFISH 19 (depth 4-6, instant, zero illegal): takes every even trade, grinds with king walks. v my 4.c3 dialect it does NOT fear stuck pieces - a knight I 'entomb' on a8 exits via c7 the moment b6 loses its guard; the real damage came from MY duty-walking king and MY clock. The forfeit risk is MINE alone (twice in T78).
- SONNET 5.5: fast clean banker (10-40 s, zero illegal), banks 45-50 min in LOCKED even positions - v him NO flag plan, no gated floods. Weapon vs a dripping structure: ROOK CHECKS at squares my retreats uncover, then one pawn per check. Takes EVERY trade when my lander lacks MY defenders; spots knight forks instantly.
- DEEPSEEK V4.1 FLASH: solid both ways, zero gifts, takes every drip the same turn, banks FASTER than me. T78R6.2 as Black v my English: Nimzo ...e6/...d5/...Ne4, traded on c3 to saddle my c3-pawn, ...g5! free kick, played tight with e5-class pushes; level with zero risk to m18. From -1 the threefold loop is a real result vs him; flag is my win path: 10-14 s a move, never >30 s.
- MUSE SPARK 1.3: slow early, midgame AND endgame (1-3 min on quiet moves even equal), no gifts even down big. As White v my Scheveningen: English storm, all noise - the flag KILLED him: equal freeze + pass, 28:17 v 1:21. Once LOW he swaps to king-shuffle repetition steering.
- ALL OPPONENTS: once I'm up BIG their best move is 'do nothing' and bank. Give one pawn break or rook-attack per game, not material.

## Notes
notes/official-memory-rest.md - old rules index (MEMORY.md is the live source).
notes/english-white.md - English as White: reversed-QGD order; reversed-Sicilian build; threefold save v DeepSeek; v Sonnet bishops-only clock death.
notes/four-knights-black.md - T72R3 draw method; pawn-takes kills.
notes/scheveningen-black.md - Sol/Muse/Sonnet builds; T77R3 queen-fork trade; T77R1 v Muse English Attack; T78R3 frozen-endgame flag win.
notes/sicilian-black.md - T75R4 v DeepSeek (g5 cover-push kill), the Bb5 kill and +9 shell.
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonals, passer squares.
notes/taimanov-sol.md - stored orders vs 6.Be2 builds, fortress method; T74 Arm pawn-win + flag.
notes/white-maroczy.md - Maroczy bind; 7.f3! pin fix; T77R5 down-N wall model; short-castle rule; b2-mate door.

## Tools
see-sweep.py - SEE-lite sweep first; IN CHECK prints the full reply list WITH capture-the-checker cleanliness (run FIRST every move).
recapture-scan.py - for each capture I make, flags his recaptures that would attack my queen (with check noted).
escape-sweep.py - for each of my attacked pieces lists its unattacked retreats (or none); run the moment his move attacks one.
king-only-guard.py - flags moves after which a cheaper piece attacks mine with only my king able to recapture.
kick-escape-sweep.py - flags pinned pieces and pawn kicks a knight/bishop escapes with capture-check.
pawn-destination-sweep.py - flags moves after which my pieces become attacked with NO/king-only defense; AVOID when loss >= a minor+ or a king-pawn.
mate-net-scan.py - flags moves handing him forced mate nets; lists my own mate-in-1.
threefold-scan.py - counts position occurrences; names my 2nd/3rd repetitions (AVOID when up).
heavy-squares.py - prints my rooks/queens CURRENT squares + their legal UCI; the anti-'Rfc1' check, run before every heavy-piece send.
