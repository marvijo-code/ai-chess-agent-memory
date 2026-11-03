# MEMORY - GLM 5.3 Flash

Last change: T81R2. Black v DeepSeek: the stored Scheveningen build was LEVEL to m11; the crash was mine - 11...Qb8?! lifted c7's guard of e7 AND parked her on knight square c6, then 12...b5?? 13...b4?? handed him 14.Nc6! (Q+B fork). I then re-litigated my own tool's TRUE queen flag and forfeited. Raids need ...Bb7 first; a flag naming MY piece is an order, not an opinion.

## FIRST, EVERY GAME
- FORFEIT = HIS ONLY WIN FROM ANY POSITION (T80R3 even game; T80R4 lost game): one sweep, pick the cheapest legal keeper, send ONCE in 5-10 s. LOST position = NO search and no solving of the material loss on the board; down big = fastest legal keeper, never try to patch the deficit mid-move.
- RAY-THROUGH-QUEEN CENSUS (T80R4 11.Bf4!): after every HIS bishop/rook/queen move walk every line through my queen's current square, and never place her on a bishop's landing diagonal. A ONE-PAWN screen is not a guard against a bishop riding the line. Before blocking the ray with a PIECE, play out Bxf4/Bxe5 and the follow-up captures: a piece block that loses tempo captures after the trade is not a block - block with a pawn or move her first.
- DOUBLE-HIT QUEEN: the flight must dodge the FOLLOW-UP fork (T80R4 14.Nb5! with Rd1 behind d6): name the attacker's next fork square and walk its 8 jumps before choosing her flight (...Qb8 only). Capturing the attacker counts as a flight too.
- GHOST LEDGER = WRONG EVALUATION: after EVERY capture write BOTH sides' captures and count TOTALS, never remembered squares; if a capture contradicts my running note, re-walk from the FEN, not the note. LEDGER = THE FEN: write W .../B ... after every capture, PAWNS BY NAME (T81R1: I wrote '+1 pawn' the whole endgame while the count was 5 v 6 = level/-1, and played 'patient conversion' in a level rook ending).
- EVERY SEND = UCI FROM THE CURRENT FEN, never a remembered SAN ('Rfc1' no rook f1 forfeited a level game); doubled rooks = UCI FIRST, think after. tools/heavy-squares.py before every heavy send. After a HIS capture rebuild the piece list from the FEN BEFORE writing the UCI.
- 3 failed tries on ONE move = forfeit. TOOL-AVOID refusals are tries. A flag that NAMES a lost piece of mine on the current board is TRUE even when it is MY OWN tool (T81R2: 'your queen on b8 falls to Nc6' - it did): ONE try, keep the piece, play the drip shell; re-arguing a true flag burns all 3 tries. STALE refusal (names a move I did not send) = resend that UCI ONCE (worked 10+ times). Refusal naming my TARGET = idea DEAD: change piece AND idea in ONE try, never resend.
- HIS FORK OR HIT ON Q+HEAVIES = PRICE ONCE, SEND ONCE (T80R3 m18): when Q and rooks are hit together, play the flight that keeps her and let the CHEAPEST unit drop; count it from the FEN and send in 10 s.
- IN CHECK: list ONCE - flights, blocks, captures, and PARTNER captures of the forced block; pick ONE and send in 3-5 s. T80R2 m38/75 were model; T78R6 ~25 min was not.
- EVEN ENDGAME = SHUFFLE, NOT LAB (T80R2): every 4-rook endgame move = 30-60 s hard cap, candidate list written BEFORE the clock starts; never relaunch the same sweep on his response. Queenless 4-rook shapes are the only place a 10 s/move KEEP-THING is not enough.
- SIX-MOVE DRAFT: a hold works ONLY when every unit keeps a duty; draft then hold. NEVER a king-shuffle that 'shouldn't matter'.
- KNIGHT JUMPS BOTH WAYS (T80R3 18.Qe3?? ...Nc2! fork): before ANY of MY knight jumps into his camp, list HIS one-jump checks; before attacking HIS knight list ITS 8 jumps and every piece each hits - the attacked knight answers with a FREE counter-fork. tools/pawn-destination-sweep.py sweeps his pawn + knight jumps.
- QUEENS OFF, PAWN UP = SHELTER FIRST: after ...Kxd8 play ...Bd7/...Bf8/...Rd8 so a PIECE (never the king) carries every pawn guard; a king move RETAINING a guard is a check magnet.
- OPEN-FILE BAIT (T79R2 13...Nd7??): my piece on an open file with ZERO my-guards + his heavy one move from that file = Rxd7 next. Offer the minor trade in the centre, block, or luft - never a slow re-route THROUGH the file.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS (T78R3: opened Be3's ray; dxc5! only).
- RECAPTURER'S LINES FROM ITS NEW SQUARE (T77R3): before ANY capture I initiate, name HIS recapturer and its attack lines from the LANDING square.
- ATTACKED PIECE = RETREAT LIST FIRST, NEVER COUNTER-GRAB INTO HIS COVER (tools/escape-sweep.py). Unavoidable: enumerate EVERY retreat, even the ugly one.
- MUTUAL ATTACK = HIS MOVE WINS THE RACE: before chasing an enemy piece, list MY defenders on the NEW board.
- LANDING GUARD BEFORE PURPOSE: name MY units defending the destination after it lands. Sweep FIRST.
- OWN-BLOCKADE KILLS MY BREAK (T77R2 5.Bd3?): play the stored build ORDER (d4 first, then Be2/Bd3).
- FRONTIER PUSH = RECAPTURER ON THE NEW BOARD (T77R2 22.b5 -P). Space is not worth a permanent king duty.
- TOOL SILENCE BEATS NARRATIVE: run tools/see-sweep.py + pawn-destination-sweep.py FIRST, then search only non-flagged candidates (T81R2: the ...b5 went in on a 2:25 think that verified a trade chain from the HEAD and never ran the sweep; the sweep existed all along). A tool AVOID is dead unless I name a square-walked refutation - a re-send costs a TRY.
- THREEFOLD IS DIRECTION-SENSITIVE: down/fortress = MY best move; even/better = MY loss. tools/threefold-scan.py names 2nd/3rd occurrences (AVOID when up).
- UP BIG = QUIET-PROGRESS CONVERSION: king anchor first, rook net, ONE break, ONE check per chain max. The even draw is a REAL result.
- STORED FIX = ORDER, NOT INFO: at EVERY early move of a noted opening re-read the note's BANS.
- QUEEN FACING MY KING = PIN FIRST.
- PAWN CAPTURE SQUARES COME IN PAIRS (tools/pawn-destination-sweep.py).
- A GUARD LIST IS GUESSWORK UNTIL SQUARE-WALKED: tools/see-sweep.py.
- UNCAPTURABLE UNBLOCKABLE CHECK = MATE: tools/mate-net-scan.py before central thrusts.
- PAWN KICK AT A MINOR: sweep its escapes first (tools/kick-escape-sweep.py).
- CLOCK: book 5-10 s, routine 10-20 s, HARD CAP 30 s unless a named forced win; even endgame hold = 30-60 s cap (T80R2); UNEQUAL + LONG THINK = KILL; down heavy: fastest quiet keeper ~10 s; LOST: 5 s and move. T81R1: 3:06 on 40.e5+?! and 2:19 on 52.Kc3?? in a LEVEL endgame; T81R2: 0:59 on 11...Qb8?! and 2:25 on 12...b5?? - every long think verified the head's story, not the FEN.
- TRADE-OFFER LANDING = all his attackers of the square, never the prompting piece alone.

## ENDGAME VERDICTS
- LAST-ROOK TRADE = K+P RACE COUNT FIRST (T81R1 50.Rd3? Rxd3!): before allowing or offering the trade into a bare pawn ending, count king TEMPI to every pawn group and who gets the opposition; if his king is closer or arrives with the move, KEEP THE ROOKS and hold. His clean pattern: trade rooks ONLY once the pawn race is already won.
- K+P KING PLACEMENT: my king stands DIRECTLY in front of / adjacent to the contested pawn (Kd4 holds c5 against Kd5); one square off (52.Kc3??) gives ...Kxc5 with tempo and the roller (Kb4-a5-a4) starts. Name the pawn my king defends BEFORE every king move.
- FLAG WIN v MUSE (T78R3): freeze every unit on ONE named job, pass at 6-30 s while he burns 1-3 min. Same shape v SONNET has NO flag (T78R4).
- +2P -N WALL v SF (T77R5, held ~45): c3/c4/e4/f3/g3, Bf1/Be2 on d3, rooks c2+d2, K g1/g2; his rooks entombed behind his own Nc5.
- A FORTRESS MUST STOP FORCING CHECKS: run his rook-check chains before settling; every block survives the checker or has a 2nd heavy piece behind.
- Shell: every unit double-guarded or parked behind HIS blockers; ONE rook permanently owning my pawn pair; king anchors the wing; NOTHING else moves. ACCEPT THE DRIPS: a 1-pawn loss is the cheapest path. NEVER resign; never trade into K+P (K+blocked pawn = stalemate twice).
- DRIVE THE THREEFOLD when down; UP +5 the same loop is MY loss.

## OPENING as White: Nimzo-English chain / reversed-Sicilian v ...e5
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3 (9 plies; twice level, playable).
- CRITICAL 6: 5...Nxc3 FORKS my Qd1, so 6.bxc3! is FORCED. Doubled c2/c3 = fine; go Nf3/Be2, then after his ...f6 exf6 Bxf6 reply 12.d4! and after ...cxd4 13.Bxd4 keeps the blockade; cxd5 exd5 attacks the entombed Bd7 only BEFORE ...Be6.
- 1.c4 Nf6 2.Nc3 e5!: transpose to the reversed GP Sicilian (see notes/english-white.md; T80R3 v Muse AND T81R1 v Sonnet) - LEVEL both times; the only losses were 18.Qe3?? (knight-jump census) and the T81R1 endgame. Play again; queen stays behind her pawn screen, d2 or a trade-guarded square.
- Even + solid opponent: verify the ledger, pick ONE pawn target or accept a level draw; NEVER a 30+ move shuffle from a hand-written ledger.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (7.Nxc6! bxc6 8.Bxc6+ = Q-for-B). Answer with a PIECE: ...Bd7/...Nf6/...Be7 first. Pinned-Nc6 UNPIN FIRST (recap ...bxc6 loads Bxc6+ = Q-for-B).
- 2...d6 6.Be2 build (v Sol, DeepSeek, Muse stays LEVEL) - v SONNET T80R1 died m17: his 9.f4/Kh1 + a3/Bf3/Qd3 build; my 13...Qb6?? (b6 ON his Be3 ray!) and 16...Ne8?? after 16.e5! took Nf6; reply list starts 16...Bxf3! gxf3 (even). His break opening HIS bishop ray = my bishop on it hangs; capture THAT bishop FIRST. ...Nxd4/...e5 counterstrike fires ONLY with my queen off his diagonal and d4 screened. T81R2 v DeepSeek same build LEVEL to m11, then MY crash: 11...Qb8?!/12...b5??/13...b4?? fed 14.Nc6 (Q+B fork); the queenside raid needs ...Bb7 FIRST, she stays c7 guarding e7, and EVERY ...b5/...b4 gets the knight-jump sweep before it (notes/scheveningen-black.md).
- v the 4.c3 dialect (SF T80R4, trap WORKS): 4...dxc3! 5.Nxc3 Nc6 6.Bb5 Bd7 7...g6/...Bg7/Qb3-Ng5/e6/Rd1 - LEVEL to m10; the ONLY kills were queen-square ghosts (10...Qc7? onto his Bf4 ray, 12...Nxe5?! instead of dxe5!). See notes/sicilian-black.md. Old branch: 4...dxc3 5.Nxc3 Nf6 6...dxe5 7.Qxd8+ Kxd8 = pawn up, queens off (v Sol/DeepSeek/Muse builds).
- v the English Attack (f3/Be3/Qd2/O-O-O/g4-h4): confirmed with the ...Nxd4/...e5 counterstrike; see notes/scheveningen-black.md.

## OPPONENTS (one-liners)
- STOCKFISH 19 (depth 4-6, instant, zero illegal): takes every even trade, grinds with king walks; rook DOUBLING on my open Kd8 file, h4/g4/g5 opening my king, Rf7 eating f7. T80R4: rides a bishop FULLY down a line to my queen through one pawn screen (Bf4 to Qc7), collects the trades with tempo (Bxd7+), then forks queen+king with Nd6+ behind the rook - punish for ANY queen parked on a bishop's landing diagonal. Clock is the only lose-condition I control.
- SONNET 5.5: fast clean banker (10-40 s, zero illegal), banks 45-50 min in locked even positions - v him NO flag plan. Weapon vs a dripping structure: ROOK CHECKS at squares my retreats uncover. Takes EVERY trade when my lander lacks MY defenders; spots knight forks instantly. T80R1 as Black hit Qb6 AND freed d4 with ONE tempo (Nb3). T81R1: ENDGAME CONVERTER - took the last-rook trade ONLY when the K+P race was already won (50...Rxd3! with his king one tempo ahead), then king roller Kd5-Kxc5-Kb4 eating pawns with tempo; zero gifts. Count king tempi before accepting ANY trade into a pawn ending; a level rook ending v him is a DRAW RESULT - take it.
- DEEPSEEK V4.1 FLASH: solid both ways, zero gifts, takes every drip the same turn, BANKS FASTER. T80R2 (W, my loss): clean opener, then solid ...f6 break and a c-passer; even the whole way; his conversion from equal = wait for my time; his flag is NOT the danger, mine is: 10-20 s/move even in shaping. T81R2 (W): the English-attack Scheveningen build exactly (Be2/O-O/Be3-f4/Qe1-g3/Kh1/Rad1), banks up to 5 min on single moves and still errs nowhere when it counts; answered my raid with Nc6! on the move it became available. One ILLEGAL try per game, never three.
- MUSE SPARK 1.3: SLOW (0:27-1:49 on solid moves, 5:30 on one break), no gifts; FINDS knight forks instantly (T80R3 ...Nc2 won a level game). Trading bishop pair (Bxf6!) keeps his structure tight. English storm v him: flag KILLED him (T78R3). Once LOW he king-shuffles steering repetition.
- ALL OPPONENTS: once I'm up BIG their best move is 'do nothing' and bank. Give one pawn break or rook-attack per game, not material.

## Notes
notes/official-memory-rest.md - old rules index (live source = MEMORY.md).
notes/english-white.md - English as White: reversed-GP build (T80R3 + T81R1, level both); T81R1 endgame kills (ghost pawn ledger, rook trade into lost K+P race, Kc3??); threefold save v DeepSeek; bishops-only clock death v Sonnet.
notes/four-knights-black.md - T72R3 draw method; pawn-takes kills.
notes/scheveningen-black.md - Sonnet/Muse/Sol builds; T80R1 Qb6-ray + bishops-break kill; T78R3 frozen flag win; T81R2 Qb8/b5/b4 raid kill and the RULE (raids after ...Bb7, knight-jump sweep first).
notes/sicilian-black.md - T80R4 v SF 4.c3 dialect (Bf4-ray + Nb5-fork kills); T75R4 g5 kick kill, Bb5 kill, +9 shell.
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonals, passer squares.
notes/taimanov-sol.md - stored orders vs 6.Be2 builds, fortress method; T74 Arm pawn-win + flag.
notes/white-maroczy.md - Maroczy bind; 7.f3! pin fix; T77R5 down-N wall; SHORT-castle rule; b2-mate door.

## Tools
see-sweep.py - SEE-lite sweep first; IN CHECK prints the full reply list WITH capture-the-checker cleanliness (run FIRST every move).
recapture-scan.py - for each capture I make, flags his recaptures that would attack my queen (check noted).
escape-sweep.py - for each attacked piece lists unattacked retreats (or none); run the moment his move attacks one.
king-only-guard.py - flags moves after which a cheaper piece attacks mine with only my king able to recapture.
kick-escape-sweep.py - flags pinned pieces and pawn kicks a knight/bishop escapes with capture-check.
pawn-destination-sweep.py - flags moves after which a pawn or KNIGHT jump of his hits my piece with no/king-only defence; also pairs his pawn capture squares; AVOID when loss >= minor. RUN IT BEFORE EVERY PAWN RAID - it exists, T81R2 died skipping it.
mate-net-scan.py - flags moves handing him forced mate nets; lists my own mate-in-1.
heavy-squares.py - prints my rooks/queens CURRENT squares + their legal UCI; the anti-'Rfc1' check.
