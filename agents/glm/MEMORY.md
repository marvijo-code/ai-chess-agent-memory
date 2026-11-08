# MEMORY - GLM 5.3 Flash

Last change: T85R3. Drew 1/2 v Sonnet as White (threefold m46). Reversed-QGD was level to m20, queens off m24, then my 26.Nf5+ burned 1:37 on a FALSE 'Nxf5 wins a clean bishop' read (the bishop merely retreated with tempo) and tempo-drift handed the initiative over: I ended -1 in a BvB ending - but the down-side FORTRESS (Kc3 anchor + bishop tour d3/c4/b5) held to threefold exactly as the direction rule says. T85R1's forfeit budget laws held here: 1 gated try total, no forfeit.

## FIRST, EVERY GAME
- CHECK THAT 'TAKES A PIECE' (T85R3): before sending a check I say wins material, name ALL guards of the target AND its live retreats that carry tempo; 26.Nf5+ 'won the Bf5' that just stepped to Bd7/c8 - a defended minor near his king is NOT a win, and a 1:37 think bought nothing. Only zero-retreat pieces are grabs.
- BvB -1 FORTRESS TEMPLATE, PROVEN v SONNET (T85R3): king adjacent ON the flank kills the passer by occupancy (Kc3 made c3/c4/b4 impossible AND double-guards b3 with a2), bishop tours the one triangle (d3/c4/b5), NEVER vacate the guard pawns (b3/a2), same-color bishops alone make my other pawns immune. -1 = threefold is THREE: repeat the keeper; if he sidesteps (45...Be4), repeat again next turn.
- ONE TRY PER MOVE AT LEVEL (T85R1): gated sends x2 a move ALONE can forfeit. Pre-verify with material-sweep + safe-keepers, send ONCE, 10-20 s. After a gate: a DIFFERENT legal keeper, one try, done - and never let every candidate be a gated variant of one idea.
- SORTIE PRICE = LANDING SQUARE EXITS (T85R1): before a bishop/rook/queen sortie onto a forward/remote square, list how I get it BACK (which of my exits are still legal next move, what his rooks/knights cover) - a square with both exits covered by one of his rook/knight pairs is a PARKING SPOT, play it only when I mean to trade it. Bb6/Ba7-class queen-hits fired for one tempo each and cost a WHOLE BISHOP of play.
- DOUBLE-HIT = ONE COMPUTED SEND (T84R5): when two units hang at once, compute the least-loss ONCE from the FEN and that read IS the send. Recompute inside a gated slot costs the slot's time - 10 s, never 4 min.
- OVERRIDE DEATH (T84R3): a tool AVOID naming the lost unit + capturer + line is CLOSED - pick a different keeper, never send the flagged move to 'check the tool'. My whole forfeit record is this one override repeated.
- TOOL FLAG NAMING MY PAWN: verify the flag by naming a guard of that pawn on the CURRENT board; when a guard exists, the guarding keeper IS the send (T85R1 d3-v-Qd6).
- KING-KEEPER RATCHET: after MY king/rook/queen hop its old square is DEAD as a keeper; every heavy keeper re-derives its square from the FEN at send time; piece-map.py, send <=15 s.
- FIRST REFUSAL = THE IDEA IS DEAD: after ANY refusal the next send is a plainly legal keeper <=10 s, ONE try - never a variant.
- PAWN-FILE CENSUS: after ANY pawn capture a remembered pawn is DEAD; every pawn move takes its FROM square from the FEN - write only the pushes that FROM allows. piece-map.py before every pawn push.
- GATED CANDIDATE = HIS MOVE: the gate is NOT protection - the referee plays it. Name the recapture chain on the CURRENT board before the first send; the plainest tool-clean keeper goes.
- GHOST LEDGER: totals come from the FEN only AFTER his capture's whole recapture chain; material-sweep.py before ANY '+' or 'level' claim.
- QUEEN ON A HIS-ROOK FILE: before centering her name every his rook reaching her file in one move; a rook stepping IN FRONT hits her with tempo; her answer LEAVES the file.
- PAWN-BREAK DESTINATION LAW: before any push list EVERY unit reaching the landing square and all my recapturers in order; two enemy takers, one of mine = dead BEFORE the push.
- PIN TRANSFERS TO THE CAPTURER: capturing ON a slider-to-my-king line puts the capturer back on that line with HIS tempo; name the king step or surviving recapturer first.
- 60s ONE-MOVE LAW: refused candidate = FEN walk <=15 s; second refusal = plainest legal keeper, one try; NEVER a third variant. IN CHECK: list flights/blocks/captures ONCE, pick, 3-5 s.
- FORCED RECAPTURE = MOVE CLOSED: forced replies 3-10 s from the FEN; both my knights BY SQUARE before a knight UCI; unfinished plan = the last verified keeper goes NOW.
- Q+R HERDING (v SF in check): before choosing a king flight name the check that LANDS on the new square; all flights lose = least-cost flight in 5 s, never census in the net.
- ATTACKED UNIT PLAIN ESCAPE = HIS TEMPO: price every candidate hit before pushing against a guarded pawn.
- BISHOP-ENTRY FILE: my g-pawn on g3 or a unit on a rank his pawn passed = his bishop LANDS; name h3/g4 entries in every retreat census.
- ENGINE DRIFT = MOVE FIRST: level or worse = keepers 10-20 s, one sentence of verification. DOWN / flag race = 5-10 s instant sends, accept the drip; no 2-7 min expresses on quiet moves.
- SF DRIFTS = PURE GENIUS: checking loops, doubled rooks, c6+f5 flips. Lost = his clock does the rest.
- RAY-THROUGH-QUEEN: after every his bishop/rook/queen move walk every line through my queen; a one-pawn screen is not a guard.
- DOUBLE-HIT QUEEN: the flight must dodge the FOLLOW-UP fork; name the fork square, walk the 8 jumps, then fly. Capturing counts as a flight.
- CHECK MET BY BLOCK-WITH-TEMPO: before a bishop/queen check name every block square; his block must not ALSO hit my checker.
- EVERY SEND = UCI FROM THE CURRENT FEN, never remembered SAN; SAN ambiguity costs tries.
- EP CENSUS: before any double push name the neighbor e.p. square and what the push opens.
- HIS FORK OR HIT ON Q+HEAVIES = PRICE ONCE, SEND ONCE: the flight keeps her, cheapest unit drops; 10 s.
- WEDGE RULE: a pawn wedge (b4/c5/f5/g5/d4) is a POSITION: challenge its support or landing square.
- KNIGHT JUMPS BOTH WAYS (pawn-destination-sweep.py); QUEENS OFF = SHELTER FIRST.
- OPEN-FILE BAIT: my piece on an open file, zero my-guards, his heavy near = taken next.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS; RECAPTURER'S LINES FROM ITS NEW SQUARE.
- ATTACKED PIECE = RETREAT LIST FIRST (escape-sweep.py); MUTUAL ATTACK = his move wins the race; LANDING GUARD BEFORE PURPOSE.
- OWN-BLOCKADE KILLS MY BREAK; FRONTIER PUSH = recapturer on the NEW board.
- TOOL SILENCE BEATS NARRATIVE: tools first; a tool AVOID is dead unless I name a square-walked refutation.
- THREEFOLD IS DIRECTION-SENSITIVE (CONFIRMED T85R3): down/fortress drives it, even/up is my loss.
- UP BIG = QUIET-PROGRESS CONVERSION, king anchor first; LEVEL v a fat banked clock = seconds-race: keepers 5-20 s, no shuffle catalogue.
- CLOCK: book 5-10 s, routine 10-20 s, HARD CAP 30 s; down = 10 s. ONE send per move.
- TRADE-OFFER LANDING = all his attackers of the square, never the prompting piece alone.
- KING v HIS STORM: a king in front of an unfired h4/h5/f5 storm is a target-in-place; the keeper class is walk FARTHEST from the named storm file.

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, SIT at formation; only a NAMED threat moves him.
- LAST-ROOK TRADE = K+P RACE COUNT FIRST; K+P: king DIRECTLY at the contested pawn.
- FLAG WIN TEMPLATE (T84R5, proven at -3): one job per unit, 5-10 s passes, king parked, every keep tool-clean, ZERO positional gestures while down a piece. v SONNET a level rook ending = DRAW result; v SF level needs ONE named pawn break by m25.
- Fortress stops forcing checks; SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice.

## OPENING as White: g3/Be3 build everywhere (incl. v SF); bans: 4.Nf3/Be2 reversed-FK
- Reversed-GP v ...e5: LEVEL five times (T85R1 v Muse to m22 = same store). 1.c4 Nf6 2.Nc3 e5 3.g3 Nc6 4.Bg2 d6 5.d3 Be7 (then Nf3 O-O O-O Re8 e4 Be6); Nge2 ILLEGAL here; queen stays d2 or trade-guarded; NO bishop sorties to b6/b5/a7-class squares - parked past pawn support = entombed (T85R1's whole loss).
- reversed-QGD v SONNET (PLAY AGAIN, T85R3 again LEVEL to m20): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 6.d3 Nc6 7.Nf3 Bd6 8.O-O; then Qd2 Be6 e4 Qd7 Rd1 Rad8 Qe2 h6 Be3, 14.d4! break = even trades through Nxd4/Bxd4/exd4/Nxd4 and Rxd4/Qxd4; queens off m24 = LEVEL minor ending. Minor inaccuracies fine (Qe3/b3 -1 ply each, b3 was pro-vs-Nc4); the loss of +0.3 came AFTER, in the minor ending, not the opening. see notes/english-white.md
- v SF ...d4 WEDGE (PLAY AGAIN): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Bg2 d4 6.Ne4 Nc6 7.d3 Nxe4 8.Bxe4; then Nf3 a5, O-O O-O, Qd2 = level. FIX: 11...Nb4 met by 12.Nxf6+ or 12.Nd2, never a3 while Be4 strapped; NEVER 14.Qf4 (gated -> ...fxe4 = +2, twice). After 13...Bxb4 keepers Rd1/Rfc1/Qe2-type; g4 banned. see notes/english-rev-fourknights.md
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3; CRITICAL 5...Nxc3 6.bxc3!; Nf3/Be2, f6 exf6 Bxf6, 12.d4! keeps the blockade (v Muse W).
- DEFAULT: g3/Be3 build with a3 BEFORE ...Bb4 (4.Nf3/Be2 BANNED); his Bd4 met by 12.b4 13.Bxd4!; king off g1 only for a NAMED threat.
- Even + solid opponent: verify the ledger, ONE pawn target or a level draw; never a 30+ move shuffle from a hand ledger.

## OPENING as Black
- v DeepSeek 1.d4: QGD CARLSBAD - PLAY AGAIN (T84R5 WIN). Level to m22; the ...d4 wedge + ...c5 break with Rc8 behind won queenside space. Hanging: Qc7 while his Bg3 diagonal lives; bare c5/d5 pushes without knight/Rc8 support die to his e4-class hits. see notes/qgd-black.md
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6?; answer with a PIECE first; UNPIN FIRST.
- 2...d6 6.Be2 build: his break opening HIS bishop ray = my bishop on it hangs, CAPTURE THAT BISHOP FIRST (16...Bxf3!). Raid needs ...Bb7 first.
- v the 4.c3 dialect: LEVEL to m10; the raid needs ...Bb7 first, queen stays c7.
- v the 6.Be2 battery: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O (14), then ...Re8 FIRST. His 9.f4? -> ...e5!, 11.Nf3? -> ...Nc6 holds e5; queens off m12 = LEVEL minor ending. ...e5 ONLY with ...Re8 placed or ...Nxd4 traded. A kingside kick prices its trade exits first.
- v the 6.Be3 English attack: 7...e5! counterstrike CONFIRMED (T84R1, level). PLAY AGAIN. see notes/scheveningen-black.md
- Four Knights v 3.Nc3: 3...Bb4, 1/2 from -5; NEVER Ncd7??/Nb3??; shell SHUFFLE, threefold only after every recurrence counted.

## OPPONENTS (one-liners)
- STOCKFISH 19: instant, zero illegal; wedges SELF-EXECUTE; pin -> Bh3! exchange, king-hunt loop, Q+R herding net in check. Every move obeys the 60 s law; accepts threefold only vs a sound shell.
- SONNET 5.5: banks 50-57 min, ZERO illegal, engine-clean keepers, trades evenly. At LEVEL he wins only the clock; a level rook ending = DRAW RESULT, CONFIRMED AGAIN T85R3. In a -1 BvB he converts the passer properly (Kd5 infiltration, b6+/c5+ tempo moves, one deviation 45...Be4 to dodge my repeat) but could NOT break the anchored Kc3 fortress in 20 moves. His kills (Qd4+) arrive only AFTER my shelter loses its SECOND guard. Beat plan: MY pace.
- DEEPSEEK V4.1: solid but ONE double-hit ghost per game. At level/slightly better he burns 5-7 min thinks on QUIET moves and can FLAG with 5 min left. Rule: shell + 5-10 s instant keeps in ANY level or down-but-solid spot; never mirror his tempo.
- MUSE SPARK 1.3 (T85R1): SLOW (1-3 min/move all phases), ZERO board/invalid errors, and he does NOT attack - he PARKS units (Rc7/Rc6/Rec8/Qd6 waited 12 moves on my entombed Ba7) and lets my senders forfeit. Beat plan: every unit on a square with two live exits, ONE verified send per move at 10-20 s, show progress by a SUPPORTED central break (e4/d4) every ~8 moves, never edge/king-shelf shuffles; a level game v him is decided entirely by MY try budget.
- ALL: when I'm up BIG they bank; one pawn break or rook-attack per game.

## Notes
notes/official-memory-rest.md - legacy rules index
notes/english-rev-fourknights.md - v SF: g3-door, wedge slot, herding net
notes/english-white.md - reversed-GP builds, T84R3 Sonnet +1-forfeit, endgame kills
notes/four-knights-black.md - four knights v SF: pawn-takes kills
notes/qgd-black.md - T84R5 v DeepSeek WIN: Carlsbad build, d4+c5 breaks, double-hit send economy
notes/scheveningen-black.md - Sonnet/Muse/Sol/DeepSeek builds, English-attack jobs
notes/sicilian-black.md - 4.c3 dialect, g5-kick kill, +9 shell
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonal rules
notes/taimanov-sol.md - 6.Be2 battery: strike confirmed, block-with-tempo
notes/white-maroczy.md - Maroczy; 7.f3! pin fix; SHORT castle; b2 mate door
notes/muse-level-white.md - T85R1: parking-square law, forfeit-budget law

## Tools
see-sweep.py - SEE-lite first; IN CHECK prints the reply list (run FIRST).
recapture-scan.py - flags his recaptures that attack my queen.
escape-sweep.py - unattacked retreats for attacked pieces.
pawn-destination-sweep.py - his pawn/KNIGHT jump hits on my pieces.
kick-escape-sweep.py - pinned pieces, pawn kicks' escapes.
mate-net-scan.py - mate nets and my mate-in-1.
piece-map.py - RUN FIRST: to-move, king square, full piece map, material.
material-sweep.py - W/B totals + units by square; before ANY '+'/'level' claim.
safe-keepers.py - ranks legal moves by kept material; top 3 + AVOIDs.
