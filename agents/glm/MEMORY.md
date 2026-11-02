# MEMORY - GLM 5.3 Flash

Last change: T80R2. White v DeepSeek, L 0-1 forfeit ON CLOCK from an EVEN queenless 4-rook endgame (even since cxd5 exd5, 4v4 through the blockade). My moves were drafted well (bxc3!, Rxc2!); loss = 6 moves >3:15 (5:25, 7:01, 5:18, 3:55, 3:04, 2:47) + 3 gated tries + timeout at m45. Even endgames = 30-60 s a move, not 5-min labs. Read this file + listed notes at game start.

## FIRST, EVERY GAME
- GHOST LEDGER = WRONG EVALUATION: after EVERY capture write BOTH sides' captures and count TOTALS, never remembered squares; if a capture contradicts my running note, re-walk from the FEN, not the note. T79R4: a phantom f7 pawn made an even ending read -1 all game.
- EVERY SEND = UCI FROM THE CURRENT FEN, never a remembered SAN ('Rfc1' no rook f1 forfeited a level game; doubled rooks = UCI FIRST, think after). tools/heavy-squares.py before every heavy send. NEVER invalidated by韧性: his last move[type] may leave a prior 'safe' square NOT safe: after an a2 push/capture rebuild the piece list from the FEN BEFORE writing the UCI (T72R3 NC 10 invalid hits at captures).
- 3 failed tries on ONE move = forfeit, and the game is LOST either way. TOOL-AVOID refusals are tries. STALE refusal (names a move I did not send) = resend that UCI ONCE (worked 10+ times). Refusal naming my TARGET = idea DEAD: change piece AND idea in ONE try, never resend. T80R2 m45: the 3 gated tries came AFTER reading the flood once - re-read = 2nd try.
- IN CHECK: list ONCE - flights, blocks, captures, and PARTNER captures of the forced block; pick ONE and send in 3-5 s. T80R2 m38/75 were model; T78R6 ~25 min was not.
- EVEN ENDGAME = SHUFFLE, NOT LAB (T80R2): every 4-rook endgame move = 30-60 s hard cap, candidate list written BEFORE the clock starts; never relaunch the same sweep on his response (improve ONE candidate from the list). T80R2 the whole game's loss was clock; 6 threats >3:15 = death. Even queenless endgauames are the ONLY shape where a 10 s/move KEEP-THING is not enough: broços, cadenas, truck-détente need the same discipline.
- SIX-MOVE DRAFT: a hold works ONLY when every unit keeps a duty; draft then hold. NEVER a king-shuffle that 'shouldn't matter' - T80R2 the whole loss came from trying to SWAP duties rather than SEND the pass.
- ENTOMB-BOOKKEEPING IS NOT A MOVE: ONE named plan + 10-20 s keepers; the stuck piece is HIS problem - but the label must name the WHOLE plan, not one square.
- KNIGHT-RESULT FORK = BISTRO CHECK: before ANY my-knight jump to HIS camp, list HIS OWN one-jump checks first ('Nb6+; Ne6+; Nd5+').
- QUEENS OFF, PAWN UP = SHELTER FIRST: after ...Kxd8 play ...Bd7/...Bf8/...Rd8 so a PIECE (never the king) carries every pawn guard; a king move RETAINING a guard is a check magnet.
- OPEN-FILE BAIT (T79R2 13...Nd7??): my piece on an open file with ZERO my-guards + his heavy one move from that file = Rxd7 next. Answer = offer the minor trade in the centre, block, or luft - never a slow re-route THROUGH the file.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS (T78R3: opened Be3's ray; dxc5! only).
- RECAPTURER'S LINES FROM ITS NEW SQUARE (T77R3): before ANY capture I initiate, name HIS recapturer and its attack lines from the LANDING square.
- ATTACKED PIECE = RETREAT LIST FIRST, NEVER COUNTER-GRAB INTO HIS COVER (tools/escape-sweep.py). Unavoidable: enumerate EVERY retreat, even the ugly one.
- MUTUAL ATTACK = HIS MOVE WINS THE RACE: before chasing an enemy piece, list MY defenders on the NEW board.
- LANDING GUARD BEFORE PURPOSE: name MY units defending the destination after it lands. Sweep FIRST.
- OWN-BLOCKADE KILLS MY BREAK (T77R2 5.Bd3?): play the stored build ORDER (d4 first, then Be2/Bd3).
- FRONTIER PUSH = RECAPTURER ON THE NEW BOARD (T77R2 22.b5 -P). Space is not worth a permanent king duty.
- TOOL SILENCE BEATS NARRATIVE: run tools/see-sweep.py + pawn-destination-sweep.py FIRST, then search only non-flagged candidates. A tool AVOID is dead unless I name a square-walked refutation - a re-send costs a TRY.
- THREEFOLD IS DIRECTION-SENSITIVE depends on the LEDGER: down/fortress = MY best move; even/better = MY loss. tools/threefold-scan.py names 2nd/3rd occurrences (AVOID when up).
- UP BIG = QUIET-PROGRESS CONVERSION: king anchor first, rook net, ONE break, ONE check per chain max. Like T80R2 down -Q the whole game - the draw is a REAL result.
- STORED FIX = ORDER, NOT INFO: at EVERY early move of a noted opening re-read the note's BANS.
- QUEEN FACING MY KING = PIN FIRST.
- PAWN CAPTURE SQUARES COME IN PAIRS (tools/pawn-destination-sweep.py).
- A GUARD LIST IS GUESSWORK UNTIL SQUARE-WALKED: tools/see-sweep.py.
- UNCAPTURABLE UNBLOCKABLE CHECK = MATE: tools/mate-net-scan.py before central thrusts.
- PAWN KICK AT A MINOR: sweep its escapes first (tools/kick-escape-sweep.py).
- BOOK = 5-10 s; slow budget ONLY for a concrete named plan. DOUBT = SAFE MOVE. HARD CAP 30 s unless a named forced win; UNEQUAL + LONG THINK = KILL. Down heavy: fastest quiet keeper ~10 s.
- LEDGER = THE FEN: after every capture write 'W .../B ...' and recount MY OWN.
- TRADE-OFFER LANDING = all his attackers of the square, never the prompting piece alone.
- CLOCK: book 5-10 s, routine 10-20 s, HARD CAP 30 s unless a named forced win; frozen even games same cap (T78R4); endgame speculative hold = 30-60 s (T80R2).

## OPENING as White: Nimzo-English chain
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3 (9 plies; twice level, playable).
- CRITICAL 6 (T80R2 killed my stored note): 5...Nxc3 FORKS my Qd1, so 6.bxc3! is FORCED - the old 'recapture with KNIGHT' note was fantasy (no knight). Doubled c2/c3 = fine; go Nf3/Be2, then after his ...f6 exf6 Bxf6 reply 12.d4! (block the Bf6-c3 ray at the source) and after ...cxd4 13.Bxd4 keeps the blockade; cxd5 exd5 attacks the entombed Bd7 only BEFORE ...Be6 (Rfd1/Rdc1/Rcb1 wandering never touched d5 late).
- Even + solid opponent: verify the ledger, pick ONE pawn target or accept a level draw; NEVER the 30+ move shuffle from a hand-written ledger.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (7.Nxc6! bxc6 8.Bxc6+ = Q-for-B). Answer with a PIECE: ...Bd7/...Nf6/...Be7 first. Pinned-Nc6 UNPIN FIRST (recap ...bxc6 loads Bxc6+ = Q-for-B).
- 2...d6 6.Be2 build (v Sol, DeepSeek, Muse stays LEVEL) - died m17 v SONNET T80R1: his 9.f4/Kh1 + a3/Bf3/Qd3 build. TWO my kills: 13...Qb6?? (b6 sits ON his Be3 ray! 14.Nb3! hits Q and FREES d4) and 16...Ne8?? after his 16.e5! took Nf6; the reply-list starts with 16...Bxf3! gxf3 (even bishops, playable). His break opening HIS bishop ray = my bishop on it hangs; capture THAT bishop FIRST, then named counters only. ...Nxd4/...e5 counterstrike fires ONLY with my queen off his diagonal and d4 screened.
- v the 4.c3 dialect (T78R5, R6, T79R2 all lost later in-game, trap WORKS): 4...dxc3! 5.Nxc3 Nf6 6...dxe5 7.Qxd8+ Kxd8 = pawn up, queens off. 8.Ng5 8...Be6 (8...h6?? BANNED). 9.Bb5 answer with PIECE moves, 10.Nxe6+ fxe6! accept the drip. At 13.O-O OFFER THE KNIGHT TRADE AT ONCE (13...Ne4!/...Nd5!). Then ONE planned shelter build (...Bd7 on e6-duty BEFORE any king move).
- v the English Attack (f3/Be3/Qd2/O-O-O/g4-h4): confirmed with the ...Nxd4/...e5 counterstrike; see notes/scheveningen-black.md.

## FROZEN ENDGAME (two verdicts)
- FLAG WIN v MUSE (T78R3): freeze every unit on ONE named job, pass at 6-30 s while he burns 1-3 min. Same shape v SONNET has NO flag (T78R4).
- +2P -N WALL v SF (T77R5, held ~45): c3/c4/e4/f3/g3, Bf1/Be2 on d3, rooks c2+d2, K g1/g2; his rooks entombed behind his own Nc5.
- A FORTRESS MUST STOP FORCING CHECKS: run his rook-check chains before settling; every block survives the checker or has a 2nd heavy piece behind.
- Shell: every unit double-guarded or parked behind HIS blockers; ONE rook permanently owning my pawn pair; king anchors the wing; NOTHING else moves. ACCEPT THE DRIPS: a 1-pawn loss is the cheapest path.
- DRIVE THE THREEFOLD when down; UP +5 the same loop is MY loss.

## OPPONENTS (one-liners)
- STOCKFISH 19 (depth 4-6, instant, zero illegal): takes every even trade, grinds with king walks; rook DOUBLING on my open Kd8 file, h4/g4/g5 opening my king, Rf7 eating f7. Clock is the only lose-condition I control.
- SONNET 5.5: fast clean banker (10-40 s, zero illegal), banks 45-50 min in locked even positions - v him NO flag plan. Weapon vs a dripping structure: ROOK CHECKS at squares my retreats uncover. Takes EVERY trade when my lander lacks MY defenders; spots knight forks instantly. T80 as Black hit Qb6 AND freed d4 with ONE tempo (Nb3): count what HIS repositioning FREES before crossing onto his rays.
- DEEPSEEK V4.1 FLASH: solid both ways, zero gifts, takes every drip the same turn, BANKS FASTER. T80R2 (W, my loss): clean opener, then solid ...f6 break and a c-passer; even the whole way, tried to trap me with Nxc6-to-bxc6 recruiting against Bd4 - I answered 22.Nxc6! bxc6 (level). His conversion from equal: wait for my time; his flag is NOT the danger, mine is: 10-20 s/move even in shaping, never 'a fine try' >60 s.
- MUSE SPARK 1.3: slow early/mid/endgame (1-3 min on quiet moves even equal), no gifts even down big. English storm v him: flag KILLED him. Once LOW he king-shuffles steering repetition.
- ALL OPPONENTS: once I'm up BIG their best move is 'do nothing' and bank. Give one pawn break or rook-attack per game, not material.

## Notes
notes/official-memory-rest.md - old rules index (live source = MEMORY.md).
notes/english-white.md - English as White: reversed-QGD order; reversed-Sicilian build; threefold save v DeepSeek; bishops-only clock death v Sonnet.
notes/four-knights-black.md - T72R3 draw method; pawn-takes kills.
notes/scheveningen-black.md - Sonnet/Muse/Sol builds; the T80 Qb6-on-Be3-ray + bishops break kill; T78R3 frozen-endgame flag win.
notes/sicilian-black.md - T75R4 v DeepSeek (g5 kick kill), Bb5 kill, +9 shell.
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonals, passer squares.
notes/taimanov-sol.md - stored orders vs 6.Be2 builds, fortress method; T74 Arm pawn-win + flag.
notes/white-maroczy.md - Maroczy bind; 7.f3! pin fix; T77R5 down-N wall; SHORT-castle rule; b2-mate door.

## Tools
see-sweep.py - SEE-lite sweep first; IN CHECK prints the full reply list WITH capture-the-checker cleanliness (run FIRST every move).
recapture-scan.py - for each capture I make, flags his recaptures that would attack my queen (check noted).
escape-sweep.py - for each attacked piece lists unattacked retreats (or none); run the moment his move attacks one.
king-only-guard.py - flags moves after which a cheaper piece attacks mine with only my king able to recapture.
kick-escape-sweep.py - flags pinned pieces and pawn kicks a knight/bishop escapes with capture-check.
pawn-destination-sweep.py - flags moves after which my pieces become attacked with NO/king-only defense; AVOID when loss >= minor+ or king-pawn.
mate-net-scan.py - flags moves handing him forced mate nets; lists my own mate-in-1.
heavy-squares.py - prints my rooks/queens CURRENT squares + their legal UCI; the anti-'Rfc1' check.
