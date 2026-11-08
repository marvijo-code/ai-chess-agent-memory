# MEMORY - GLM 5.3 Flash

Last change: T84R5. WON 0-1 v DeepSeek on TIME as Black from ~-3: QGD Carlsbad shell level to m22, his Qb3/e6 double-hits plus 5 gated slots (~4 min each) cost R+B (Qxf7!, Bxc7) - but his pieces stayed WALLED BEHIND HIS OWN PAWNS, I sent 5-10 s instant keeps, and his five 5-7 min expresses flagged him. Flags are won by shell + send speed, never by material.

## FIRST, EVERY GAME
- DOUBLE-HIT = ONE COMPUTED SEND (T84R5 NEW): when two units hang at once (m23 Qb3 hit b6+f7; m25 e6 hit Qd7 AND opened g3-c7), compute the least-loss ONCE from the FEN and that read IS the send. My Rb8/Qd8 = R-for-B reads were right; the 4-min re-verifications inside the gated slots were the real price - Qxf7! and Bxc7 landed through slot TIME. Recompute costs 10 s, never 4 min.
- OVERRIDE DEATH (T84R3): a tool AVOID naming the lost unit + capturer + line is CLOSED - pick a different keeper, never send the flagged move to 'check the tool'. My whole forfeit record is this one override repeated.
- KING-KEEPER RATCHET: after MY king/rook hop its old square is DEAD as a keeper; every king/rook/queen keeper re-derives its square from the FEN at send time; piece-map.py, send <=15 s.
- FIRST REFUSAL = THE IDEA IS DEAD: after ANY refusal the next send is a plainly legal keeper <=10 s, ONE try - never a variant. HIS true flag naming MY piece = one try, keep the piece; a flag naming my TARGET = dead.
- PAWN-FILE CENSUS: after ANY pawn capture a remembered pawn is DEAD; every pawn move takes its FROM square from the FEN - write only the pushes that FROM allows. piece-map.py before every pawn push.
- GATED CANDIDATE = HIS MOVE: the gate is NOT protection - the referee plays it. Name the recapture chain on the CURRENT board before the first send; the plainest tool-clean keeper goes.
- GHOST LEDGER: totals come from the FEN only AFTER his capture's whole recapture chain; material-sweep.py before ANY '+' or 'level' claim.
- QUEEN ON A HIS-ROOK FILE: before centering her name every his rook reaching her file in one move; a rook stepping IN FRONT hits her with tempo; her answer LEAVES the file.
- PAWN-BREAK DESTINATION LAW: before any push list EVERY unit reaching the landing square and all my recapturers in order; two enemy takers, one of mine = dead BEFORE the push.
- FORTRESS CENSUS WRITTEN ONCE: sealed-line list at formation; later keepers one sentence + send <=15 s; a note re-narrating the census is THE SEND SIGNAL.
- PIN TRANSFERS TO THE CAPTURER: capturing ON a slider-to-my-king line puts the capturer back on that line with HIS tempo; name the king step or surviving recapturer first.
- 60s ONE-MOVE LAW: refused candidate = FEN walk <=15 s; second refusal = plainest legal keeper, one try; NEVER a third variant. IN CHECK: list flights/blocks/captures ONCE, pick, 3-5 s (T84R3 forfeit = census inside the check).
- FORCED RECAPTURE = MOVE CLOSED: forced replies 3-10 s from the FEN; both my knights BY SQUARE before a knight UCI; unfinished plan = the last verified keeper goes NOW.
- Q+R HERDING (v SF in check): before choosing a king flight name the check that LANDS on the new square; all flights lose = least-cost flight in 5 s, never census in the net.
- ATTACKED UNIT PLAIN ESCAPE = HIS TEMPO: price every candidate hit before pushing against a guarded pawn.
- BISHOP-ENTRY FILE: my g-pawn on g3 or a unit on a rank his pawn passed = his bishop LANDS; name h3/g4 entries in every retreat census.
- ENGINE DRIFT = MOVE FIRST: level or worse = keepers 10-20 s, one sentence of verification. DOWN / flag race = 5-10 s instant sends, accept the drip; no 2-7 min expresses on quiet moves (that was HIS whole loss in T84R5).
- SF DRIFTS = PURE GENIUS: checking loops, doubled rooks, c6+f5 flips. Lost = his clock does the rest.
- RAY-THROUGH-QUEEN: after every his bishop/rook/queen move walk every line through my queen; a one-pawn screen is not a guard.
- DOUBLE-HIT QUEEN: the flight must dodge the FOLLOW-UP fork; name the fork square, walk the 8 jumps, then fly. Capturing counts as a flight.
- CHECK MET BY BLOCK-WITH-TEMPO: before a bishop/queen check name every block square; his block must not ALSO hit my checker.
- EVERY SEND = UCI FROM THE CURRENT FEN, never remembered SAN; SAN ambiguity costs tries.
- EP CENSUS: before any double push name the neighbor e.p. square and what the push opens.
- HIS FORK OR HIT ON Q+HEAVIES = PRICE ONCE, SEND ONCE: the flight keeps her, cheapest unit drops; 10 s.
- WEDGE RULE: a pawn wedge (b4/c5/f5/g5/d4) is a POSITION: challenge its support or landing square. My ...d4+...c5 pair beat his f4/f5/h4/h5 storm - wedges were the only live coordinates.
- KNIGHT JUMPS BOTH WAYS (pawn-destination-sweep.py); QUEENS OFF = SHELTER FIRST.
- OPEN-FILE BAIT: my piece on an open file, zero my-guards, his heavy near = taken next.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS; RECAPTURER'S LINES FROM ITS NEW SQUARE.
- ATTACKED PIECE = RETREAT LIST FIRST (escape-sweep.py); MUTUAL ATTACK = his move wins the race; LANDING GUARD BEFORE PURPOSE.
- OWN-BLOCKADE KILLS MY BREAK; FRONTIER PUSH = recapturer on the NEW board.
- TOOL SILENCE BEATS NARRATIVE: tools first; a tool AVOID is dead unless I name a square-walked refutation.
- THREEFOLD IS DIRECTION-SENSITIVE: down/fortress drives it, even/up is my loss.
- UP BIG = QUIET-PROGRESS CONVERSION, king anchor first; LEVEL v a fat banked clock = seconds-race: keepers 5-20 s, no shuffle catalogue.
- CLOCK: book 5-10 s, routine 10-20 s, HARD CAP 30 s; down = 10 s; a gated slot takes the FIRST computed read, never a rebuild. ONE send per move.
- TRADE-OFFER LANDING = all his attackers of the square, never the prompting piece alone.
- KING v HIS STORM (T84R5 19...Kh7??): a king in front of an unfired h4/h5/f5 storm is a target-in-place; the keeper class is walk FARTHEST from the named storm file (h8-class once the g-file unpins).

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, SIT at formation; only a NAMED threat moves him.
- LAST-ROOK TRADE = K+P RACE COUNT FIRST (T81R1 50.Rd3?); K+P: king DIRECTLY at the contested pawn.
- FLAG WIN TEMPLATE (T84R5, now proven at -3 = Muse recipe): one job per unit, 5-10 s passes, king parked, every keep tool-clean, ZERO positional gestures while down a piece. v SONNET a level rook ending = DRAW result; v SF level needs ONE named pawn break by m25.
- Fortress stops forcing checks; SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice.

## OPENING as White: g3/Be3 build everywhere (incl. v SF); bans: 4.Nf3/Be2 reversed-FK
- v SF ...d4 WEDGE (PLAY AGAIN): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Bg2 d4 6.Ne4 Nc6 7.d3 Nxe4 8.Bxe4; then Nf3 a5, O-O O-O, Qd2 = level both times. FIX: 11...Nb4 met by 12.Nxf6+ or 12.Nd2, never a3 while Be4 strapped; NEVER 14.Qf4 (gated -> ...fxe4 = +2, twice). After 13...Bxb4 keepers Rd1/Rfc1/Qe2-type; g4 banned. see notes/english-rev-fourknights.md
- v SONNET reversed-QGD (PLAY AGAIN; f4 BANNED at m28): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 6.d3 Nc6 7.Nf3 Bd6 8.O-O; then Qd2 Be6 e4 Qd7 Rd1 Rad8 Qe2 h6 Be3 a5 = level to m20; the d4 break = +1 PAWN queens on. THE KILL was own-tool-flagged 28.f4?? (Qd4+ fork). Ban f/h pushes with queens on while his queen re-enters the vacated f2/d4-e3 diagonal without a second guard; +1 = TRADE QUEENS at 5-10 s pace. see notes/english-white.md
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3; CRITICAL 5...Nxc3 6.bxc3!; Nf3/Be2, f6 exf6 Bxf6, 12.d4! keeps the blockade (v Muse W).
- DEFAULT: g3/Be3 build with a3 BEFORE ...Bb4 (4.Nf3/Be2 BANNED); his Bd4 met by 12.b4 13.Bxd4!; king off g1 only for a NAMED threat.
- Reversed-GP v ...e5: LEVEL four times. 1.c4 Nf6 2.Nc3 e5 3.g3 Nc6 4.Bg2 d6 5.d3 Be7 (then Nf3 O-O O-O Re8 e4 Be6); Nge2 ILLEGAL here; queen stays d2 or trade-guarded.
- Even + solid opponent: verify the ledger, ONE pawn target or a level draw; never a 30+ move shuffle from a hand ledger.

## OPENING as Black
- v DeepSeek 1.d4: QGD CARLSBAD - PLAY AGAIN (T84R5 WIN). Level to m22; the ...d4 wedge + ...c5 break with Rc8 behind won queenside space against his whole f/h-storm. Hanging: Qc7 while his Bg3 diagonal lives; bare c5/d5 pushes without knight/Rc8 support die to his e4-class hits. see notes/qgd-black.md
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6?; answer with a PIECE first; UNPIN FIRST.
- 2...d6 6.Be2 build: his break opening HIS bishop ray = my bishop on it hangs, CAPTURE THAT BISHOP FIRST (16...Bxf3!). Raid needs ...Bb7 first.
- v the 4.c3 dialect: LEVEL to m10; the raid needs ...Bb7 first, queen stays c7.
- v the 6.Be2 battery: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O (14), then ...Re8 FIRST. His 9.f4? -> ...e5!, 11.Nf3? -> ...Nc6 holds e5; queens off m12 = LEVEL minor ending. ...e5 ONLY with ...Re8 placed or ...Nxd4 traded. A kingside kick prices its trade exits first (31...f5 at 3:30 = the flag).
- v the 6.Be3 English attack: 7...e5! counterstrike CONFIRMED (T84R1, level). PLAY AGAIN. see notes/scheveningen-black.md
- Four Knights v 3.Nc3: 3...Bb4, 1/2 from -5; NEVER Ncd7??/Nb3??; shell SHUFFLE, threefold only after every recurrence counted.

## OPPONENTS (one-liners)
- STOCKFISH 19: instant, zero illegal; wedges SELF-EXECUTE; pin -> Bh3! exchange, king-hunt loop, Q+R herding net in check. Met my g3 build out of book and WON on my gates/ledgers, not chess. Every move obeys the 60 s law; accepts threefold only vs a sound shell.
- SONNET 5.5: banks 50-54 min, ZERO illegal, engine-clean keepers, trades evenly. At LEVEL he wins only the clock; a level rook ending = DRAW RESULT. His kills (Qd4+) arrive only AFTER my shelter loses its SECOND guard. T83R4: beat me ONLY through my stale ...Kf8 tries. Beat plan: MY pace.
- DEEPSEEK V4.1: solid but ONE double-hit ghost per game (T84R5 m23 Qb3, m25 e6). At level/slightly better he burns 5-7 min thinks on QUIET moves and can FLAG with 5 min left (T84R5: seven of my seconds per his minutes). Rule: shell + 5-10 s instant keeps in ANY level or down-but-solid spot; never mirror his tempo; T83R2 forfeit was my quiet-keeps pace, the cure is the same law - pace, not the book.
- MUSE SPARK 1.3: SLOW (1-3 min/move every phase), forks named, zero board errors. T84R1: lost to my 8 invalid tries, not him. Trade his ONE aggressor, else fast LEGAL keepers <=30 s; his flag kills him only while MY senders hold.
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
