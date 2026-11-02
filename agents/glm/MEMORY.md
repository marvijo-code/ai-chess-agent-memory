# MEMORY - GLM 5.3 Flash

Last change: T79R2.2 Black v SF19, L ON TIME from a position my chess held at -2. The 4.c3 trap WORKED a 3rd time (+1, queens off, m13; fxe6!/axb6! engine-!); the kills: 13...Nd7?? parked my LAST minor on the open d-file with zero guards (Rad1! Rxd7+ Nxe4 = -2 by m19), then ~21 min of clock on THREE gated drip-fights (13:08 on 14...e4 alone). Down heavy, my tools flagged all 16 legal moves - and the referee played my intended e4 anyway: tries 2-3 of a gated candidate buy NOTHING but clock. Read this file + listed notes at game start.

## FIRST, EVERY GAME
- EVERY SEND = UCI TYPED FROM THE CURRENT FEN, never a remembered SAN prefix ('Rfc1' with no rook on f1 forfeited a level game). After ANY of my rook/queen moves re-walk WHICH squares my heavies occupy; tools/heavy-squares.py before every heavy send. With 2 invalids banked the NEXT send is a verified-legal UCI, one try, zero style.
- 3 failed tries on ONE move = referee plays my stale best-so-far (T79R2) or forfeit - either way a disaster. TOOL-AVOID refusals are tries too. STALE refusal (names a move I did not send) = resending my intended UCI is allowed and worked 10+ times. Refusal naming my ACTUAL candidate = that idea is DEAD: change piece AND idea, redraw from the FEN.
- IN CHECK: write the reply list ONCE - flights, blocks, CAPTURES OF THE CHECKER BY SQUARE (Kxe5! T78R6; at T79R2 m15 the Kxd7 question stayed open - walk the checker's attackers MYSELF, never trust a stored 'only flights' list). Pick ONE, send in 5-10 s. Forfeits cluster on check replies and gated floods.
- GATED FLOOD = CLOCK DEATH (T79R2: 13:08 on 14...e4, 3:25 Kc8, 4:09 Rh8; T78R6 ~25 min): when my sweeps flag EVERY legal move, the position has NO safe move and the flag is noise. Read once, send the least-bad ONCE per try, <=10 s think BETWEEN tries, never re-derive the same loss. The drip was unavoidable; let the resend/fallback land it.
- ENTOMB-BOOKKEEPING IS NOT A MOVE: ONE named plan + 10-20 s keepers; the stuck piece is HIS problem.
- KNIGHT-RESULT FORK = BISTRO CHECK: before MY knight jumps toward HIS camp, list HIS OWN one-jump checks (Nb6+; Ne6+; Nd5+) by hand.
- QUEENS OFF, PAWN UP = SHELTER FIRST (T78R5+R6): after ...Kxd8 play ...Bd7/...Bf8/...Rd8 so a PIECE, never the king, carries every pawn guard; a king move RETAINING a guard duty is a check-magnet. T79R2: the king walks were FORCED (Rd8+ nets) - the real fix is never losing the anchoring piece (open-file bait below).
- OPEN-FILE BAIT (T79R2 13...Nd7??): my piece on an open file with ZERO my-guards + his heavy one move from that file = Rxd7 next. When his rook takes the open file at my uncastled king, my move list = OFFER THE MINOR TRADE in the centre (Ne4!/Nd5!), block, or luft - never a slow re-route THROUGH the file. Up a pawn, queens off: trades ARE the conversion.
- BLOCKER ABANDON: one blocking piece is NOT defense - blocks jump away once the screen drains; sweep every piece I plan a block with.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS (T78R3: opened Be3's ray; dxc5! only).
- RECAPTURER'S LINES FROM ITS NEW SQUARE (T77R3 Bxd4+ forked Qb6+Kg7): before ANY capture I initiate, name HIS recapturer and its attack lines from the LANDING square. tools/recapture-scan.py.
- ATTACKED PIECE = RETREAT LIST FIRST, NEVER COUNTER-GRAB INTO HIS COVER: unattacked retreats (tools/escape-sweep.py) + defend/trade BEFORE any capture. Unavoidable: enumerate EVERY retreat, even the ugly one (28...Bf8 T77R1).
- MUTUAL ATTACK = HIS MOVE WINS THE RACE: before attacking/chasing an enemy piece, list MY defenders of MY lander on the NEW board. Never walk my rook off the open file my queen then stands on (T77R2).
- LANDING GUARD BEFORE PURPOSE: name MY units defending the destination after it lands (T78R4 Qd5?? missed Rd8's d-file). Sweep BEFORE any long think.
- OWN-BLOCKADE KILLS MY BREAK (T77R2 5.Bd3?): play the stored build ORDER (d4 first, then Be2/Bd3).
- FRONTIER PUSH = RECAPTURER ON THE NEW BOARD (T77R2 22.b5 lost P). Space is not worth permanent king duties.
- TOOL SILENCE BEATS NARRATIVE: run tools/see-sweep.py + pawn-destination-sweep.py FIRST, then search only non-flagged candidates. But DOWN HEAVY the flags are noise (see gated flood). A tool AVOID is dead unless I name a square-walked refutation - a re-send costs a TRY.
- THREEFOLD IS DIRECTION-SENSITIVE: down/fortress = MY best move; even/better = MY loss. tools/threefold-scan.py names 2nd/3rd occurrences (AVOID when up).
- UP BIG = QUIET-PROGRESS CONVERSION: king anchor first, rook net, ONE break, at most ONE check in a row.
- STORED FIX = ORDER, NOT INFO: at EVERY early move of a noted opening re-read that note's BANS (T77R5 7.f3). Others' trap notes = ban list too.
- QUEEN FACING MY KING = PIN FIRST.
- PAWN CAPTURE SQUARES COME IN PAIRS: tools/pawn-destination-sweep.py.
- A GUARD LIST IS GUESSWORK UNTIL SQUARE-WALKED: tools/see-sweep.py.
- A PAWN IS A GUARD ON ITS FORWARD DIAGONALS: before any push beside my king list the mover's remaining guards and his rays into my king after the grab (T75R4 ...g5 -> Nxh6 -> mate).
- UNCAPTURABLE UNBLOCKABLE CHECK IS ALREADY MATE: tools/mate-net-scan.py before central thrusts.
- PAWN KICK AT A MINOR: sweep its escapes first; any capture-with-check kills the push (tools/kick-escape-sweep.py). A g5-class kick at MY Nf4: retreat to e2/e3 BEFORE the kick lands, never to h5 (T78R6.2).
- BOOK = 5-10 s; slow budget only for a concrete named plan. DOUBT = SAFE MOVE (T75R3). T79R2 fat thinks: 2:39 Nb6, 4:06 Nd7?? in a +1 queens-off game - the clock was donated before the fight began.
- TWO of my rooks/queens on one line = UCI ONLY, never SAN (T78R6.2 'Rfc1' forfeit).
- LEDGER = THE FEN: after every capture write 'W ... / B ...' and RECOUNT MY OWN LEDGERS TOO (T79R2 mine carried a dead Bb5 for 10 moves). One line each turn.
- TRADE-OFFER LANDING = all his attackers of the square from the piece list, never the prompting piece alone.
- CLOCK: book 5-10 s, routine 10-20 s, HARD CAP 30 s unless a named forced win. Frozen even games the same cap (T78R4). UNEQUAL + LONG THINK = T78R6 KILL. Down heavy: fastest quiet keeper ~10 s - T79R2 held -2 for 10 moves on keeper chess (Ba3! Bxb2, h6, hxg5, Re8, Rxh4 forecasting Nxe6->h4 bare); the flag was lost in moves 11-20, not the shell.

## CAPTURE LEDGER (before every send)
- KING-ONLY GUARD = losing recapture. tools/king-only-guard.py.
- I am the cheaper attacker against a once-guarded piece = trade-down sac is MY weapon; name his last recapturer by square, THEN its attack lines from that square.
- A fresh PAWN recapture kills the piece even after my queen recaptures; pawn attacked twice v defended once is lost: push, trade or accept.
- v Stockfish: donate NO first pawn; Open-Sicilian order 4.Nxd4! then Nc3/Be2/O-O; v ...g6 5.c4 AND THEN 7.f3! at once vs ...Qa5 - Qd2/Qd3 do NOT fix the pin (Bg7 backs d4).

## OPENING as White (v Nimzo-English)
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3 Nc5 6.d4 Ne4 7.cxd5 exd5 = LEVEL big chain (c3/d4/e5). T78R6.2 then DRIFTED: g3?/Nh3?/Qd3?/Bg2/O-O? left the Ne4 squatting, and ...g5! kicked my Nf4. Next time: 8.f3! kicks the Ne4 at once before ...Bb4 sets the pin, or trade Nxe4 dxe4 early.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (7.Nxc6! bxc6 8.Bxc6+ = Q-for-B). Answer Bb5 with a PIECE: ...Bd7/...Nf6/...Be7 first. Pinned-Nc6 recap: ...bxc6 after Nxc6 loads it for Bxc6+ = Q-for-B; UNPIN FIRST.
- v the 4.c3 dialect (T78R5, R6, T79R2 - the trap WORKS, all 3 losses came later): 4.c3?! dxc3! 5.Nxc3 Nf6 6.e5 dxe5 7.Qxd8+ Kxd8 = pawn up, queens off. 8.Ng5 8...Be6 (8...h6?? 9.Nxf7+ forks Kd8+Rh8 - BANNED, square-checked). 9.Bb5 answer with PIECE moves (...Nbd7), 10.Nxe6+ fxe6! accept the drip. T79R2 KILL: after 13.O-O I played 13...Nd7?? - my LAST minor onto the open d-file, zero guards: 14.Rad1 15.Rxd7+ 16.Nxe4 = -2, no minors left to hold. FIX: at 13.O-O OFFER THE KNIGHT TRADE AT ONCE (13...Ne4! or 13...Nd5! - N-for-N even, still +1, shell comes fast). Then ONE planned shelter build (...Bd7 on e6-duty BEFORE any king move); accept e6 as a drip rather than a duty-walking king anchor.
- v the English Attack (f3/Be3/Qd2/O-O-O/g4-h4): confirmed twice with the ...Nxd4/...e5 counterstrike (12...Nxd4! 13.Bxd4 e5!); see notes/scheveningen-black.md.
- 2...d6 6.Be2 build (v Sol, DeepSeek, Muse, Sonnet): ...Be7 ...O-O ...Qc7 ...a6 then ...b5 ...Bb7, ...Nb6 hits d4; LEVEL to m20 in ALL recorded games; every loss came AFTER m20. With material banked the wins were TRADES and holds.

## FROZEN ENDGAME (two verdicts)
- FLAG WIN v MUSE (T78R3, equal, queens off m43): freeze every unit on ONE named job, pass at 6-30 s while he burns 1-3 min. HIS CLOCK is the win condition - only while it visibly bleeds. Same shape v SONNET has NO flag (T78R4): zero-refusal keeper repeats instead.
- +2P -N MODEL v SF (T77R5, held ~45 moves): wall c3/c4/e4/f3/g3, Bf1/Be2 on d3, rooks c2+d2, K g1/g2; his rooks entombed behind his own Nc5.
- A FORTRESS MUST STOP FORCING CHECKS: run his rook-check chains before settling; every block survives the checker or has a 2nd heavy piece behind.
- Shell: every unit double-guarded or parked behind HIS blockers; ONE rook permanently owning my pawn pair; king anchors the wing; NOTHING else moves. ACCEPT THE DRIPS: a 1-pawn loss is the cheapest path, never loosen the shell to save a drip.
- DRIVE THE THREEFOLD when down; UP +5 the same loop is MY loss.

## OPPONENTS (one-liners)
- STOCKFISH 19 (depth 4-6, instant, zero illegal): takes every even trade, grinds with king walks. Its kill vs my uncastled Kd8 (T79R2): rook DOUBLING on the open d-file (Rad1/Rfd1, Rxd7+, Rd8+-Rxa8), h4/g4/g5 to open my king, Rf7 eating f7. 8.Ng5? shows depth-4 slips in the opening, but +6 converts instantly and it ended 65:00 v my flag - vs SF the clock is the only lose-condition I control. The forfeit risk is MINE alone.
- SONNET 5.5: fast clean banker (10-40 s, zero illegal), banks 45-50 min in LOCKED even positions - v him NO flag plan, no gated floods. Weapon vs a dripping structure: ROOK CHECKS at squares my retreats uncover, then one pawn per check. Takes EVERY trade when my lander lacks MY defenders; spots knight forks instantly.
- DEEPSEEK V4.1 FLASH: solid both ways, zero gifts, takes every drip the same turn, banks FASTER than me. T78R6.2 as Black v my English: Nimzo ...e6/...d5/...Ne4, ...g5! free kick, level with zero risk to m18. From -1 the threefold loop is a real result vs him; flag is my win path: 10-14 s a move, never >30 s.
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
