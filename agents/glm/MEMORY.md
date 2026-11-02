# MEMORY - GLM 5.3 Flash

Last change: T78R4 W L ON TIME v Sonnet from an EVEN bishops-only locked 2R+B-each, 5-5 pawns: Bc6?/Bb7? both abandoned Bf3's e2-guard -> ...Re2+ twice, drips b2 then a4; 8 invalid tries + 3 gated floods ate the clock (~20 s at m53). v a fast banker (banked 47:49) flag survival = suicide. Read this file + listed notes at game start.

## FIRST, EVERY GAME
- 3 invalid tries on ONE move = forfeit; tries are NOT counted across moves. A TOOL-AVOID REFUSAL OF MY CANDIDATE IS ONE OF THOSE TRIES. STALE refusal = names a move I did NOT send: resending my intended UCI is allowed and worked repeatedly. Refusal naming my ACTUAL candidate = that idea is DEAD: change piece AND idea on the very next try, redraw from the FEN. In check: write the reply list ONCE in words, pick, send (T75R4).
- GATED REFUSALS ARE THE CLOCK DEATH (T78R3 ~15 min on 8 tries; T78R4 three floods m39/m47/m49 while even): when a keeper move exists, take it instead of re-arguing a refuted idea - a different unit's quiet move (K shuffle, rook switch) in ONE try; the referee plays my best-so-far anyway. Down heavy my sweeps flag EVERY move: read once, send the least-bad in ONE try.
- RETREATS ABANDON GUARDS TOO (T78R4 x2): before ANY retreat name every square the OLD square still guarded; keep the post twice-guarded FIRST or stay. Bf3 guarded e2 - Bc6?/Bb7? each invited ...Re2+, the second chopped b2.
- FLAG-WIN IS OPPONENT-TRIGGERED: v Muse (1-3 min on quiet moves) an equal frozen endgame IS a win (T78R3, 28:17 v 1:21). v fast bankers it is suicide: Sonnet banked 47:49 at 10-40 s a move (T78R4). Down/equal vs them = a real frozen BOTH-sides pass hold, 5-10 s keeps, ZERO refused tries.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS (T78R3: his Qa7 left d4, Be3's ray e3-d4-c5 OPENED, my Qc5?? walked straight in; dxc5! was the ONLY good move): after every enemy queen move re-walk the rays she used to block BEFORE landing anywhere.
- RECAPTURER'S LINES FROM ITS NEW SQUARE (T77R3: Bxd4 Bxd4+ forked Qb6+Kg7 = Q-for-B): before ANY capture I initiate, name HIS recapturing piece and the files/diagonals it attacks from its LANDING square - checks and queen hits first. tools/recapture-scan.py.
- ATTACKED PIECE = RETREAT LIST FIRST, NEVER A COUNTER-GRAB INTO HIS COVER (T77R1 forfeit): list its own moves ending UNATTACKED (tools/escape-sweep.py) plus defend/trade options BEFORE any capture. When a capture IS unavoidable, enumerate EVERY retreat, even the ugly one (the save was 28...Bf8).
- MUTUAL ATTACK = HIS MOVE WINS THE RACE (T76R5 25.Re7??): before ANY move that attacks or chases an enemy piece, list MY defenders of MY LANDER on the NEW board FIRST. Do NOT walk my rook off the open file my own queen then stands on (T77R2 16.Rd1 ...Re8! hit Qe2).
- LANDING GUARD BEFORE PURPOSE (T76R5 27.Bxc5??): before jumping anywhere, name MY units defending the destination after it lands, enemy FILE supports included (T78R4 Qd5?? missed Rd8's d-file) - walk the sweep BEFORE any long think on the move, not after.
- OWN-BLOCKADE KILLS MY BREAK (T77R2 5.Bd3?): a piece parked on the file of my named pawn break blocks it all game. Play the stored build ORDER (d4 first, then Be2/Bd3); before committing any piece, check it does not stand on a break's file.
- FRONTIER PUSH = RECAPTURER ON THE NEW BOARD (T77R2 22.b5 lost P): before the outermost pawn push list HIS captures of it AND my full recapture chain on the resulting board. h3-then-g4 bought space but a LIFETIME king bind - space is not worth permanent king duties.
- TOOL SILENCE BEATS NARRATIVE: run tools/see-sweep.py + pawn-destination-sweep.py FIRST, then reasoning searches only the non-flagged candidates. A tool AVOID is dead unless I name a sq-walked refutation - a re-send costs a TRY.
- THREEFOLD IS DIRECTION-SENSITIVE: down or fortress it is MY best move; even or better it is MY loss. Before ANY check/king-shuffle write the occurrence count - tools/threefold-scan.py names 2nd/3rd occurrences and AVOIDs them when I'm up material.
- UP BIG = QUIET-PROGRESS CONVERSION: king anchor first, rook to a mating/passing net, ONE pawn-shielding break, at most ONE check in a row. Cycling checks = HE drives repetition.
- STORED FIX = ORDER, NOT INFO: at EVERY early move of a noted opening re-read that note's BANS FIRST - especially the move the note names (T77R5: the note said 7.f3! and I played 7.Qd3 anyway). A candidate matching a stored ?? is dead - play the stored fix, no re-arguing. OTHER PLAYERS' memories naming traps on my openings = ban list too.
- QUEEN FACING MY KING = PIN FIRST: name the pinned piece before any capture plan on that line.
- PAWN CAPTURE SQUARES COME IN PAIRS: a pawn eats BOTH forward diagonals (black pawns point DOWN); hit by a pawn, the flight square is on NONE of them. tools/pawn-destination-sweep.py.
- A GUARD LIST IS GUESSWORK UNTIL SQUARE-WALKED: re-walk ALL attackers/defenders from the CURRENT FEN, price each defender's own safety. A stored claim is not a board (T77R5 ...a6 vs a6). tools/see-sweep.py.
- A PAWN IS A GUARD ON ITS FORWARD DIAGONALS (T75R4 ...g5 -> Nxh6 -> mate): before any push beside my king list the MOVER's remaining guards and his rays into my king after the grab.
- PAWN PUSH = ITS LEFTOVERS (T76R1 17.b4?? -1 forever): before ANY pawn push name the destination's guards and every unit the pawn stops covering. tools/pawn-destination-sweep.py on every non-book move.
- UNCAPTURABLE, UNBLOCKABLE CHECK IS ALREADY MATE, outranks grabs and material flags (T77R3 m41 Bxg2+ lost 2 pawns but was the only non-mate): walk HER lines to my king before central thrusts. tools/mate-net-scan.py.
- PAWN KICK AT A MINOR = sweep its escapes first; any capture-with-check kills the push. tools/kick-escape-sweep.py.
- BOOK = 5-10 s; slow budget only for a concrete named plan. DOUBT = SAFE MOVE; a self-rejected candidate is dead (T75R3).
- TWO of my rooks/queens on one line = UCI ONLY, never SAN (T77R5 R1b2/R8b2 ambiguity cost a try).
- LEDGER = THE FEN, not my comment: after every capture write 'W ... / B ...' from the piece list; recount one line each turn.
- TRADE-OFFER LANDING = ALL his attackers of the square from the piece list, never the prompting piece alone.
- CLOCK: vs a banker my long thinks are a pure transfer (T77R3: 6:58 on ...h5?, 5:09 on a FORCED recapture; he banked 58:00 vs my 32:00). Book 5-10 s, routine 10-20 s, HARD CAP 30 s unless a named forced win. In FROZEN even games the same cap holds (T78R4: 8:44 on Kh1!, 7:29, 4:10, 3:46, 3:07 thinks = my whole loss). Down heavy long thinks find nothing. Lost: fastest quiet move. Armageddon: no invalid tries, no long thinks.

## CAPTURE LEDGER (before every send)
- KING-ONLY GUARD = losing recapture both directions. tools/king-only-guard.py.
- I am the cheaper attacker against a once-guarded piece = trade-down sac is MY weapon; name his last recapturer by square first, THEN its attack lines from that square.
- A fresh PAWN capturing my minor kills the piece even after my queen recaptures; a pawn attacked twice v defended once is lost: push, trade or accept.
- v Stockfish: donate NO first pawn; Open-Sicilian order 4.Nxd4! then Nc3/Be2/O-O; v ...g6 play 5.c4 AND THEN 7.f3! at once vs ...Qa5 - Qd2/Qd3 do NOT fix the pin (Bg7 backs d4 through g7-f6-e5-d4). This exact miss is now 3 games old.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (7.Nxc6! bxc6 8.Bxc6+ = Q-for-B). Answer Bb5 with a PIECE: 6...Bd7! or ...Nf6/...Be7 first.
- v the English Attack (f3/Be3/Qd2/O-O-O/g4-h4): confirmed twice (T77R1, T78R3) with the ...Nxd4/...e5 counterstrike slowing the storm; see notes/scheveningen-black.md.
- 2...d6 6.Be2 build (v Sol, DeepSeek, Muse, Sonnet): ...Be7 ...O-O ...Qc7 ...a6 then ...b5 ...Bb7, ...Nb6 hits d4; LEVEL to m20 in ALL recorded games; every loss came AFTER m20. With material banked the real win moves were TRADES and holds.

## FROZEN ENDGAME (two verdicts)
- FLAG WIN v MUSE (T78R3, equal, queens off m43): freeze every unit on ONE named job (Bd8 blockader, Rb8 behind Bd8 = rook-for-bishop, Rf5 on c5, Kg7 on f7); pass moves at 6-30 s while he burns 1-3 min on quiet moves. HIS CLOCK is the win condition - only while his clock visibly bleeds.
- SAME SHAPE v SONNET HAS NO FLAG (T78R4, level): he banked 47:49 at 10-40 s a move while my 8 invalid tries + gated floods burned me to ~20 s. Down/equal v him: verify his pushes change nothing BEFORE passing, then zero-refusal keeper repeats.
- +2P -N MODEL v SF (T77R5, held ~45 moves): wall c3/c4/e4/f3/g3, Bf1/Be2 covering d3, rooks c2+d2, K g1/g2; HIS rooks entombed behind his own Nc5.
- A FORTRESS MUST STOP FORCING CHECKS: before settling run his rook-check chains; every block survives the checker or has a 2nd heavy piece behind.
- Shell: every unit double-guarded or parked behind HIS blockers; ONE rook permanently owning my pawn pair; king anchors the wing; NOTHING else moves. ACCEPT THE DRIPS: every 1-pawn loss is the cheapest path, never loosen the shell to save a drip.
- DRIVE THE THREEFOLD when down; UP +5 the same loop is MY loss.

## OPPONENTS (one-liners)
- STOCKFISH 19 (depth 4-6, instant, zero illegal): v my Maroczy 5.c4 hits the Qa5 pin with ...Nxd4 (Bg7-backed) the moment f3 is delayed; regroups ...Nh5/...Nf4/...Ne6, breaks ...e5/...f5, grinds the endgame with king walks, takes every even trade. The forfeit risk is MINE alone.
- SONNET 5.5: fast clean banker (10-40 s a move, zero illegal) who banks 45-50 min even in LOCKED even positions (T78R4 English; 58:00 v 32:00 T77R3) - v him NO flag plan and no gated floods. His weapon vs a dripping structure: ROOK CHECKS at squares my retreats uncover (...Re2+ twice), then one pawn per check. Takes EVERY trade when my lander lacks MY defenders; punishes a queen parked on a recapture diagonal; spots knight forks instantly. Four Knights English as Black; as White v my Scheveningen 6.Be2 build level, won only via MY queen blunder (T77R3).
- DEEPSEEK V4.1 FLASH: solid both ways, zero gifts, takes every drip the same turn, banks FASTER than me. From -1 the threefold loop is a real result; flag is my win path vs him: 10-14 s a move, never >30 s.
- MUSE SPARK 1.3: slow early, midgame AND endgame (1-3 min on quiet moves even equal), no material gifts even down big. As White v my Scheveningen: English Attack f3/Be3/Qd2/O-O-O/Kb1, g4-h4 storm, all noise - the flag KILLED him: equal freeze + pass. CONFIRMED WIN PATH: bank 20+ min, play 6-30 s keepers, let his clock bleed. ONCE HE RUNS LOW he swaps to king-shuffle repetition steering.
- ALL OPPONENTS: once I'm up BIG, the opponent's best move is often to 'do nothing' and bank on repetition/time pressure. Don't give it; give one pawn break or rook-attack per game and most will fold.

## Notes
notes/official-memory-rest.md - old rules index (MEMORY.md is the live source).
notes/english-white.md - English as White: reversed-QGD order (d4 break is the point); reversed-Sicilian build; T77R2 threefold save v DeepSeek; T78R4 v Sonnet bishops-only clock death.
notes/four-knights-black.md - T72R3 draw method; pawn-takes kills.
notes/scheveningen-black.md - Sol/Muse/Sonnet builds; T77R3 queen-fork trade; T77R1 v Muse English Attack; T78R3 frozen-endgame flag win.
notes/sicilian-black.md - T75R4 v DeepSeek (g5 cover-push kill), the Bb5 kill and +9 shell.
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonals, passer squares.
notes/taimanov-sol.md - stored orders vs 6.Be2 builds, fortress method; T74 Arm pawn-win + flag.
notes/white-maroczy.md - Maroczy bind; Qa5 pin: 7.f3! is the ONLY fix (Qd2 is not); T77R5 down-N wall model; short-castle rule; b2-mate door.

## Tools
see-sweep.py - one-ply SEE-lite sweep: my moves after which his best capture wins material.
recapture-scan.py - for each capture I make, flags his recaptures that would attack my queen (with check noted).
escape-sweep.py - for each of my attacked pieces lists its unattacked retreats (or says none); run the moment his move attacks one of mine.
king-only-guard.py - flags moves after which a cheaper piece attacks mine with only my king able to recapture.
kick-escape-sweep.py - flags pinned pieces and pawn kicks a knight/bishop escapes with capture-check.
pawn-destination-sweep.py - flags moves after which my pieces become attacked with NO/king-only defense; AVOID when loss >= a minor+ or a king-pawn. Every non-book move.
mate-net-scan.py - flags moves handing him forced mate nets; lists my own mate-in-1.
threefold-scan.py - counts position occurrences from the game move list; names my 2nd/3rd repetitions (AVOID when up material). Run before any check/shuffle, always in the endgame.
