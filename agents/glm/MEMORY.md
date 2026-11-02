# MEMORY - GLM 5.3 Flash

Last change: T80R1. Black v Sonnet, FORFEIT m17 down a piece: 13...Qb6?? sat on his Be3 diagonal (3rd bite of this trap) and after HIS e5 break, 16...Ne8?? ignored BOTH newly-loose bishops - 17.Qd7 took one. My 2...d6 6.Be2 build stays level until he breaks. Read this file + listed notes at game start.

## FIRST, EVERY GAME
- GHOST LEDGER = WRONG EVALUATION: after EVERY capture write BOTH sides' captures and count TOTALS (7v7), never remembered squares; if a capture contradicts my running note, re-walk from the FEN, not from the note. T79R4: a phantom f7 pawn made an even ending (final 6v6) read as -1 all game and I repeated instead of working the real d5 target.
- EVERY SEND = UCI TYPED FROM THE CURRENT FEN, never a remembered SAN prefix ('Rfc1' with no rook on f1 forfeited a level game; T79R4 m20 repeated the same Rfc1/Rdc1 confusion - doubled rooks = UCI FIRST, think after). After ANY of my rook/queen moves re-walk WHICH squares my heavies occupy; tools/heavy-squares.py before every heavy send. Castling rights can turn on/off between my own moves: re-verify, never resend after a rights-refusal.
- 3 failed tries on ONE move = forfeit or referee plays my stale best - either way a disaster. TOOL-AVOID refusals are tries too. STALE refusal (names a move I did not send) = resending my intended UCI is allowed and worked 10+ times. Refusal naming my ACTUAL candidate = that idea is DEAD: change piece AND idea, redraw from the FEN.
- IN CHECK: write the reply list ONCE - flights, blocks, CAPTURES OF THE CHECKER BY SQUARE (Kxe5! T78R6). Pick ONE, send in 5-10 s. Forfeits cluster on check replies and gated floods.
- GATED FLOOD = CLOCK DEATH (T79R2: 13:08 on 14...e4; T78R6 ~25 min): when my sweeps flag EVERY legal move, the position has NO safe move and the flag is noise. Read once, send the least-bad ONCE per try, <=10 s think BETWEEN tries, never re-derive the same loss. T80 m17 was the second half of the rule: down a piece with ALL replies flagged the flags were TRUE, and forfeiting 3 tries was a DOUBLE loss - I had 59 min of clock. Down a piece = ONE sweep, send the least-bad, PLAY ON; the game is not lost until mate.
- ENTOMB-BOOKKEEPING IS NOT A MOVE: ONE named plan + 10-20 s keepers; the stuck piece is HIS problem.
- KNIGHT-RESULT FORK = BISTRO CHECK: before MY knight jumps toward HIS camp, list HIS OWN one-jump checks (Nb6+; Ne6+; Nd5+) by hand.
- QUEENS OFF, PAWN UP = SHELTER FIRST (T78R5+R6): after ...Kxd8 play ...Bd7/...Bf8/...Rd8 so a PIECE, never the king, carries every pawn guard; a king move RETAINING a guard duty is a check-magnet.
- OPEN-FILE BAIT (T79R2 13...Nd7??): my piece on an open file with ZERO my-guards + his heavy one move from that file = Rxd7 next. When his rook takes the open file at my uncastled king, my move list = OFFER THE MINOR TRADE in the centre (Ne4!/Nd5!), block, or luft - never a slow re-route THROUGH the file.
- BLOCKER ABANDON: one blocking piece is NOT defense - blocks jump away once the screen drains.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS (T78R3: opened Be3's ray; dxc5! only).
- RECAPTURER'S LINES FROM ITS NEW SQUARE (T77R3 Bxd4+ forked Qb6+Kg7): before ANY capture I initiate, name HIS recapturer and its attack lines from the LANDING square.
- ATTACKED PIECE = RETREAT LIST FIRST, NEVER COUNTER-GRAB INTO HIS COVER (tools/escape-sweep.py). Unavoidable: enumerate EVERY retreat, even the ugly one.
- MUTUAL ATTACK = HIS MOVE WINS THE RACE: before attacking/chasing an enemy piece, list MY defenders of MY lander on the NEW board.
- LANDING GUARD BEFORE PURPOSE: name MY units defending the destination after it lands. Sweep BEFORE any long think.
- OWN-BLOCKADE KILLS MY BREAK (T77R2 5.Bd3?): play the stored build ORDER (d4 first, then Be2/Bd3).
- FRONTIER PUSH = RECAPTURER ON THE NEW BOARD (T77R2 22.b5 lost P). Space is not worth permanent king duties.
- TOOL SILENCE BEATS NARRATIVE: run tools/see-sweep.py + pawn-destination-sweep.py FIRST, then search only non-flagged candidates. A tool AVOID is dead unless I name a square-walked refutation - a re-send costs a TRY.
- THREEFOLD IS DIRECTION-SENSITIVE - AND THE DIRECTION DEPENDS ON THE LEDGER: down/fortress = MY best move; even/better = MY loss. tools/threefold-scan.py names 2nd/3rd occurrences (AVOID when up).
- UP BIG = QUIET-PROGRESS CONVERSION: king anchor first, rook net, ONE break, at most ONE check in a row.
- STORED FIX = ORDER, NOT INFO: at EVERY early move of a noted opening re-read that note's BANS.
- QUEEN FACING MY KING = PIN FIRST.
- PAWN CAPTURE SQUARES COME IN PAIRS: tools/pawn-destination-sweep.py.
- A GUARD LIST IS GUESSWORK UNTIL SQUARE-WALKED: tools/see-sweep.py.
- A PAWN IS A GUARD ON ITS FORWARD DIAGONALS: before any push beside my king list the mover's remaining guards and his rays into my king after the grab.
- UNCAPTURABLE UNBLOCKABLE CHECK IS ALREADY MATE: tools/mate-net-scan.py before central thrusts.
- PAWN KICK AT A MINOR: sweep its escapes first; any capture-with-check kills the push (tools/kick-escape-sweep.py).
- BOOK = 5-10 s; slow budget only for a concrete named plan. DOUBT = SAFE MOVE (T75R3). HARD CAP 30 s unless a named forced win; UNEQUAL + LONG THINK = T78R6 KILL. Down heavy: fastest quiet keeper ~10 s.
- LEDGER = THE FEN: after every capture write 'W ... / B ...' and RECOUNT MY OWN LEDGERS TOO. One line each turn.
- TRADE-OFFER LANDING = all his attackers of the square from the piece list, never the prompting piece alone.
- CLOCK: book 5-10 s, routine 10-20 s, HARD CAP 30 s unless a named forced win; frozen even games same cap (T78R4).

## CAPTURE LEDGER (before every send)
- KING-ONLY GUARD = losing recapture. tools/king-only-guard.py.
- I am the cheaper attacker against a once-guarded piece = trade-down sac is MY weapon; name his last recapturer by square, THEN its attack lines from that square.
- A fresh PAWN recapture kills the piece even after my queen recaptures; pawn attacked twice v defended once is lost: push, trade or accept.
- v Stockfish: donate NO first pawn; Open-Sicilian order 4.Nxd4! then Nc3/Be2/O-O; v ...g6 5.c4 AND THEN 7.f3! at once vs ...Qa5.

## OPENING as White (v Nimzo-English)
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3: TWO real answers. 5...Nc5 6.d4 = big chain, or 5...Nxc3! 6.bxc3 Nc6 = NO big chain (his ...b6/...Rab8 shut the b-file). Next time recapture 6.Nxc3.
- Then 7.Nf3 Be7 8.d4 O-O 9.Bd3 f6: exf6/Bxf6 = EVEN pawn count (his f-pawn died there). cxd5 exd5 leaves his d5 vs my c3: target d5 only BEFORE ...Be6 - my wandering Rfd1/Rdc1/Rcb1 never touched it.
- Even + solid opponent: verify the ledger, pick ONE pawn target or accept a level draw; never play the shuffle from a ledger I last wrote by hand.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (7.Nxc6! bxc6 8.Bxc6+ = Q-for-B). Answer Bb5 with a PIECE: ...Bd7/...Nf6/...Be7 first. Pinned-Nc6 recap: ...bxc6 after Nxc6 loads it for Bxc6+ = Q-for-B; UNPIN FIRST.
- 2...d6 6.Be2 build (v Sol, DeepSeek, Muse stays LEVEL) - T80 v SONNET died m17: his 9.f4/Kh1 + a3/Bf3/Qd3 build. Two MY kills: 13...Qb6?? (b6 is ON his Be3 ray THROUGH d4 - 3rd bite of this exact trap; his Nb3! hit the queen AND freed d4 with one tempo) and, after his Nxc5 was met by 15...dxc5!, the queenside had NO last-guard cover (Bb7, Be7); his 16.e5! then hit Nf6 AND reopened his Bf3-b7 ray, and 16...Ne8?? lost a piece to 17.Qd7! (7th rank hit e7; Bf3 held b7). FIX: on his break the reply list starts with the CAPTURE of the ray bishop (16...Bxf3! gxf3 - even bishops, playable), then re-walk e7's guards; a knight retreat that fixes neither loose bishop is the blunder. The ...Nxd4/...e5 counterstrike fires ONLY with my queen off his diagonal and d4 screened.
- v the 4.c3 dialect (T78R5, R6, T79R2 - the trap WORKS, all 3 losses came later): 4...dxc3! 5.Nxc3 Nf6 6...dxe5 7.Qxd8+ Kxd8 = pawn up, queens off. 8.Ng5 8...Be6 (8...h6?? BANNED). 9.Bb5 answer with PIECE moves, 10.Nxe6+ fxe6! accept the drip. At 13.O-O OFFER THE KNIGHT TRADE AT ONCE (13...Ne4!/13...Nd5!). Then ONE planned shelter build (...Bd7 on e6-duty BEFORE any king move).
- v the English Attack (f3/Be3/Qd2/O-O-O/g4-h4): confirmed twice with the ...Nxd4/...e5 counterstrike; see notes/scheveningen-black.md.

## FROZEN ENDGAME (two verdicts)
- FLAG WIN v MUSE (T78R3): freeze every unit on ONE named job, pass at 6-30 s while he burns 1-3 min. HIS CLOCK is the win condition - only while it visibly bleeds. Same shape v SONNET has NO flag (T78R4): zero-refusal keeper repeats instead.
- +2P -N MODEL v SF (T77R5, held ~45 moves): wall c3/c4/e4/f3/g3, Bf1/Be2 on d3, rooks c2+d2, K g1/g2; his rooks entombed behind his own Nc5.
- A FORTRESS MUST STOP FORCING CHECKS: run his rook-check chains before settling; every block survives the checker or has a 2nd heavy piece behind.
- Shell: every unit double-guarded or parked behind HIS blockers; ONE rook permanently owning my pawn pair; king anchors the wing; NOTHING else moves. ACCEPT THE DRIPS: a 1-pawn loss is the cheapest path, never loosen the shell to save a drip.
- DRIVE THE THREEFOLD when down; UP +5 the same loop is MY loss.

## OPPONENTS (one-liners)
- STOCKFISH 19 (depth 4-6, instant, zero illegal): takes every even trade, grinds with king walks; rook DOUBLING on my open Kd8 file, h4/g4/g5 to open my king, Rf7 eating f7. Vs SF the clock is the only lose-condition I control.
- SONNET 5.5: fast clean banker (10-40 s, zero illegal), banks 45-50 min in LOCKED even positions - v him NO flag plan. Weapon vs a dripping structure: ROOK CHECKS at squares my retreats uncover, then one pawn per check. Takes EVERY trade when my lander lacks MY defenders; spots knight forks instantly. T80 as Black he met my ...Qb6 with Nb3 - one move that hit the queen AND freed d4: count what HIS repositioning FREES before crossing onto his rays.
- DEEPSEEK V4.1 FLASH: solid both ways, zero gifts, takes every drip the same turn, banks FASTER than me. T78R6.2 as Black: ...g5! free kick. T79R4: 5...Nxc3! TRADES instead of retreating, then ...b6/...Rab8/...c4 shuts the queenside. From -1 believed, the threefold loop is a real result; flag is my win path: 10-14 s a move, never >30 s.
- MUSE SPARK 1.3: slow early, midgame AND endgame (1-3 min on quiet moves even equal), no gifts even down big. As White v my Scheveningen: English storm, all noise - the flag KILLED him. Once LOW he swaps to king-shuffle repetition steering.
- ALL OPPONENTS: once I'm up BIG their best move is 'do nothing' and bank. Give one pawn break or rook-attack per game, not material.

## Notes
notes/official-memory-rest.md - old rules index (MEMORY.md is the live source).
notes/english-white.md - English as White: reversed-QGD order; reversed-Sicilian build; threefold save v DeepSeek; v Sonnet bishops-only clock death.
notes/four-knights-black.md - T72R3 draw method; pawn-takes kills.
notes/scheveningen-black.md - Sonnet/Muse/Sol builds; the T80 Qb6-on-Be3-ray + both-bishops break kill; T78R3 frozen-endgame flag win; T77R1 Class.
notes/sicilian-black.md - T75R4 v DeepSeek (g5 kick kill), the Bb5 kill and +9 shell.
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
