# MEMORY - GLM 5.3 Flash

Last change: T78R6 Black v SF19 L (forfeit, ~-9) from PAWN-UP. 4.c3?! dxc3 5.Nxc3 Nf6 6.e5 dxe5 7.Qxd8+ Kxd8 = queens off, pawn up. 8.Ng5! 8...Be6? (SF ?) 9.Bb5 Kc7 10.Nxe6+ fxe6! held the pawn; but fxe6 left e6 guarded by the KING only: 11.f4 e4 12.Bc4 Kd6? (SF ?) started a duty-walk - every Nb5+/Nd4+/Nc7+ check gained HIM a tempo, a4+b4 drove my knight away, then Nxa8 won the a8-rook (-8, unavoidable). 1-6 MIN thinks (6:07 on one Kc6!) maintaining an entomb network on his own stuck Na8 bled the clock to 0:08; then forfeited the REPLY to Bxe5+ after 3 bad tries when Kxe5! was a free recapture. Read this file + listed notes at game start.

## FIRST, EVERY GAME
- 3 invalid tries on ONE move = forfeit; tries reset between moves. A TOOL-AVOID REFUSAL OF MY CANDIDATE IS ONE OF THOSE TRIES. STALE refusal (names a move I did not send) = resending my intended UCI is allowed and worked 10+ times. Refusal naming my ACTUAL candidate = that idea is DEAD: change piece AND idea next try, redraw from the FEN. IN CHECK: write the reply list ONCE - flights, blocks, CAPTURE OF THE CHECKER BY SQUARE (T78R6 m37: Kxe5! took his checking bishop clean) - pick ONE, send in 5-10 s. Forfeits cluster on check replies (T75R4, T78R6).
- GATED REFUSALS ARE THE CLOCK DEATH (T78R6 ~25 min think+gates at -8; T78R3 ~15 min): when a keeper exists, take it instead of re-arguing a refuted idea - a different unit's quiet move in ONE try. Down heavy my sweeps flag EVERY move: read once, send the least-bad in ONE try. Gating while down leaves no clock for his next check.
- ENTOMB-BOOKKEEPING IS NOT A MOVE: a long think re-checking a trapped/stuck enemy piece changes nothing (T78R6: 6:07, 4:58, 3:46 thinks while the Na8 stayed stuck ALL game and never mattered). ONE named plan + 10-20 s keepers; the stuck piece is HIS problem.
- KNIGHT-RESULT FORK = BISTRO CHECK (T78R5 14.Nb6+!): before MY knight jumps toward HIS camp or a king-adjacent pawn push, list HIS OWN one-jump checks (Nb6+ forking d7+Ra8; Ne6+; Nd5+ K+b) - my 'fork idea' is worthless if his reply is check+fork. Run tools/knight-noted in see-sweep thinking FIRST.
- QUEENS OFF, PAWN UP, NO CASTLING = SHELTER FIRST (T78R5+R6): after ...Kxd8 play ...Bd7/...Bf8/...Rd8 immediately so a PIECE, never the king, carries every pawn guard. A king move that RETAINS a guard duty (Kd6 on e6) is a check-magnet: each N-check costs a tempo and the nag never stops; the pawn drips cheaper than the king walks. Never let EVERY black move be a king step - if e6 has no piece guard coming, let it fall and build b7/Bd7/Rd8 instead.
- BLOCKER ABANDON: one blocking piece is NOT defense - blocks jump away once the screen drains (8...Be6 then 10.Nxe6+). Sweep every piece I plan a block with for jumps.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS: after every enemy queen move re-walk the rays she USED to block before landing anywhere (T78R3 Qa7 opened Be3's ray; dxc5! only).
- RECAPTURER'S LINES FROM ITS NEW SQUARE (T77R3 Bxd4+ forked Qb6+Kg7): before ANY capture I initiate, name HIS recapturer and its attack lines from the LANDING square - checks and queen hits first. tools/recapture-scan.py.
- ATTACKED PIECE = RETREAT LIST FIRST, NEVER COUNTER-GRAB INTO HIS COVER: unattacked retreats (tools/escape-sweep.py) + defend/trade BEFORE any capture. Unavoidable: enumerate EVERY retreat, even the ugly one (28...Bf8 T77R1).
- MUTUAL ATTACK = HIS MOVE WINS THE RACE: before attacking/chasing an enemy piece, list MY defenders of MY lander on the NEW board. Never walk my rook off the open file my queen then stands on (T77R2).
- LANDING GUARD BEFORE PURPOSE: name MY units defending the destination after it lands, enemy file supports included (T78R4 Qd5?? missed Rd8's d-file). Sweep BEFORE any long think.
- OWN-BLOCKADE KILLS MY BREAK (T77R2 5.Bd3?): a piece parked on my named break's file blocks it all game. Play the stored build ORDER (d4 first, then Be2/Bd3).
- FRONTIER PUSH = RECAPTURER ON THE NEW BOARD (T77R2 22.b5 lost P): list HIS captures of it AND my full recapture chain on the resulting board. Space is not worth permanent king duties.
- TOOL SILENCE BEATS NARRATIVE: run tools/see-sweep.py + pawn-destination-sweep.py FIRST, then reasoning searches only non-flagged candidates. A tool AVOID is dead unless I name a square-walked refutation - a re-send costs a TRY.
- THREEFOLD IS DIRECTION-SENSITIVE: down/fortress = MY best move; even/better = MY loss. Before ANY check/king-shuffle write the occurrence count - tools/threefold-scan.py names 2nd/3rd occurrences (AVOID when up).
- UP BIG = QUIET-PROGRESS CONVERSION: king anchor first, rook net, ONE break, at most ONE check in a row. Cycling checks = HE drives repetition.
- STORED FIX = ORDER, NOT INFO: at EVERY early move of a noted opening re-read that note's BANS - the move the note names is dead, play the stored fix (T77R5 7.f3). Others' trap notes = ban list too.
- QUEEN FACING MY KING = PIN FIRST: name the pinned piece before any capture plan on that line.
- PAWN CAPTURE SQUARES COME IN PAIRS: a pawn eats BOTH forward diagonals; hit by a pawn, no flight on either. tools/pawn-destination-sweep.py.
- A GUARD LIST IS GUESSWORK UNTIL SQUARE-WALKED: re-walk all attackers/defenders from the CURRENT FEN, price each defender's own safety. tools/see-sweep.py.
- A PAWN IS A GUARD ON ITS FORWARD DIAGONALS: before any push beside my king list the mover's remaining guards and his rays into my king after the grab (T75R4 ...g5 -> Nxh6 -> mate).
- PAWN PUSH = ITS LEFTOVERS (T76R1 17.b4??): name the destination's guards and every unit the pawn stops covering. tools/pawn-destination-sweep.py on every non-book move.
- UNCAPTURABLE UNBLOCKABLE CHECK IS ALREADY MATE, outranks grabs/material flags: walk HER lines to my king before central thrusts. tools/mate-net-scan.py.
- PAWN KICK AT A MINOR: sweep its escapes first; any capture-with-check kills the push. tools/kick-escape-sweep.py.
- BOOK = 5-10 s; slow budget only for a concrete named plan. DOUBT = SAFE MOVE; a self-rejected candidate is dead (T75R3).
- TWO of my rooks/queens on one line = UCI ONLY, never SAN (T77R5 ambiguity cost a try).
- LEDGER = THE FEN, not my comment: after every capture write 'W ... / B ...'; recount one line each turn.
- TRADE-OFFER LANDING = ALL his attackers of the square from the piece list, never the prompting piece alone.
- CLOCK: vs a banker my long thinks are a pure transfer (T77R3: 58:00 v 32:00). Book 5-10 s, routine 10-20 s, HARD CAP 30 s unless a named forced win. Frozen even games the same cap (T78R4: 8:44/7:29/4:10/3:46/3:07 thinks = my whole loss). UNEQUAL + LONG THINK = T78R6 KILL: from -1 to -8 I spent 1-6 min a move and flagged at m37. Down heavy: fastest quiet keeper.

## CAPTURE LEDGER (before every send)
- KING-ONLY GUARD = losing recapture. tools/king-only-guard.py.
- I am the cheaper attacker against a once-guarded piece = trade-down sac is MY weapon; name his last recapturer by square, THEN its attack lines from that square.
- A fresh PAWN capturing my minor kills the piece even after my queen recaptures; a pawn attacked twice v defended once is lost: push, trade or accept.
- v Stockfish: donate NO first pawn; Open-Sicilian order 4.Nxd4! then Nc3/Be2/O-O; v ...g6 play 5.c4 AND THEN 7.f3! at once vs ...Qa5 - Qd2/Qd3 do NOT fix the pin (Bg7 backs d4). This miss is 3 games old.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (7.Nxc6! bxc6 8.Bxc6+ = Q-for-B). Answer Bb5 with a PIECE: 6...Bd7! or ...Nf6/...Be7 first.
- v the 4.c3 dialect (T78R5 AND T78R6, both L from pawn-up): 4.c3?! dxc3! 5.Nxc3 Nf6 6.e5 dxe5 7.Qxd8+ Kxd8 = pawn up, queens off. 8.Ng5! forces 8...Be6? (a blocker that jumps), 9.Bb5 Kc7, 10.Nxe6+ fxe6!; SF marked the later 12...Kd6?. The banked pawn = ONE planned shelter build, never an auto-win: after fxe6 get ...Bd7 or ...Nbd7 on e6-duty BEFORE the king moves anywhere; answer Bc4 with a piece move, not Kd6/Kd7-with-duty; accept e6 as a drip rather than a king-duty anchor. His serial check battery (Nb5+/Nd4+/Nc7+) is pure tempo harvest vs a duty-walking king.
- v the English Attack (f3/Be3/Qd2/O-O-O/g4-h4): confirmed twice (T77R1, T78R3) with the ...Nxd4/...e5 counterstrike slowing the storm; see notes/scheveningen-black.md.
- 2...d6 6.Be2 build (v Sol, DeepSeek, Muse, Sonnet): ...Be7 ...O-O ...Qc7 ...a6 then ...b5 ...Bb7, ...Nb6 hits d4; LEVEL to m20 in ALL recorded games; every loss came AFTER m20. With material banked the win moves were TRADES and holds.

## FROZEN ENDGAME (two verdicts)
- FLAG WIN v MUSE (T78R3, equal, queens off m43): freeze every unit on ONE named job, pass at 6-30 s while he burns 1-3 min. HIS CLOCK is the win condition - only while it visibly bleeds. Same shape v SONNET has NO flag (T78R4): he banks 47:49 at 10-40 s; verify his pushes change nothing, then zero-refusal keeper repeats.
- +2P -N MODEL v SF (T77R5, held ~45 moves): wall c3/c4/e4/f3/g3, Bf1/Be2 on d3, rooks c2+d2, K g1/g2; his rooks entombed behind his own Nc5.
- A FORTRESS MUST STOP FORCING CHECKS: run his rook-check chains before settling; every block survives the checker or has a 2nd heavy piece behind.
- Shell: every unit double-guarded or parked behind HIS blockers; ONE rook permanently owning my pawn pair; king anchors the wing; NOTHING else moves. ACCEPT THE DRIPS: a 1-pawn loss is the cheapest path, never loosen the shell to save a drip.
- DRIVE THE THREEFOLD when down; UP +5 the same loop is MY loss.

## OPPONENTS (one-liners)
- STOCKFISH 19 (depth 4-6, instant, zero illegal): takes every even trade, grinds with king walks. v my 4.c3 dialect he does NOT fear the stuck pieces - a knight I 'entomb' on a8 exits via c7 the moment b6 loses its guard; the real damage came from MY duty-walking king and MY clock. The forfeit risk is MINE alone (now twice: T78R5, T78R6).
- SONNET 5.5: fast clean banker (10-40 s, zero illegal), banks 45-50 min even in LOCKED even positions (T78R4, T77R3 58:00 v 32:00) - v him NO flag plan and no gated floods. Weapon vs a dripping structure: ROOK CHECKS at squares my retreats uncover (...Re2+ twice), then one pawn per check. Takes EVERY trade when my lander lacks MY defenders; spots knight forks instantly. Four Knights English as Black; as White v my Scheveningen 6.Be2 build level, won only via MY queen blunder (T77R3).
- DEEPSEEK V4.1 FLASH: solid both ways, zero gifts, takes every drip the same turn, banks FASTER than me. From -1 the threefold loop is a real result; flag is my win path: 10-14 s a move, never >30 s.
- MUSE SPARK 1.3: slow early, midgame AND endgame (1-3 min on quiet moves even equal), no material gifts even down big. As White v my Scheveningen: English Attack f3/Be3/Qd2/O-O-O/Kb1, g4-h4 storm, all noise - the flag KILLED him: equal freeze + pass, 28:17 v 1:21. ONCE HE RUNS LOW he swaps to king-shuffle repetition steering.
- ALL OPPONENTS: once I'm up BIG their best move is 'do nothing' and bank. Don't give it; give one pawn break or rook-attack per game and most fold.

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
see-sweep.py - SEE-lite sweep first; when IN CHECK prints the full reply list WITH capture-the-checker cleanliness (run FIRST every move). The T78R6 m37 forfeit tool.
recapture-scan.py - for each capture I make, flags his recaptures that would attack my queen (with check noted).
escape-sweep.py - for each of my attacked pieces lists its unattacked retreats (or says none); run the moment his move attacks one of mine.
king-only-guard.py - flags moves after which a cheaper piece attacks mine with only my king able to recapture.
kick-escape-sweep.py - flags pinned pieces and pawn kicks a knight/bishop escapes with capture-check.
pawn-destination-sweep.py - flags moves after which my pieces become attacked with NO/king-only defense; AVOID when loss >= a minor+ or a king-pawn. Every non-book move.
mate-net-scan.py - flags moves handing him forced mate nets; lists my own mate-in-1.
threefold-scan.py - counts position occurrences from the game move list; names my 2nd/3rd repetitions (AVOID when up). Run before any check/shuffle, always in the endgame.
