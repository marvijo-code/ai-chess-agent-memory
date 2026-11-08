# MEMORY - GLM 5.3 Flash

Last change: T85 SF2. L as Black v Sonnet 5.5, forfeit m17 from LEVEL: 16...Nxd5? let 17.exd5 hit BOTH diagonals of his new pawn (Nc6+Be6); then 1:41 inside the flag net + 3 cycled tries forfeited. Stale-square recidivist again: 15...Rfd8 (rooks stood c8+e8).

## FIRST, EVERY GAME
- STALE-SQUARE RATCHET, BOTH MOVES (T85R5, T85SF2): after ANY hop, mine or his, the piece's old square is DEAD for the next plan; every send re-derives the mover's square from the FEN in one line: piece@sq -> UCI. My forfeit record is stale squares, overrides and memo-fixes, nothing else.
- MEMO FIX = NAME ITS CURRENT TARGET (T85R5): a stored answer (e.g. ...Nb4 -> Nxf6+) fires only if that target EXISTS on this board; write who occupies each square the fix touches before sending it.
- TWO-DIAGONAL RECAPTURE (T85 SF2 KILL): before ANY piece trade, list MY units standing on the recapturing PAWN's BOTH forward diagonals; two of mine = the trade loses material. 16...Nxd5? 17.exd5 hit Nc6 AND Be6 in one tempo (~2 pawns). Fix vs his Nd5-first: ...Bxd5 leaves only one hit square occupied; ...Nxd5 is dead unless both are free.
- FLAG-NET REPLY = ONE FEN CHAIN (T85 SF2 forfeit): when a referee/material flag names a lost unit, the position is a COUNT, not a puzzle: derive the reply chain from the CURRENT FEN (his exd5 -> my ...Ne7 frees c6, a5 held by the Rc8), send ONCE at 10 s. No 1+ minute re-think inside a net, no variants, no third different move.
- WEDGE-CREEP LAW (T85R5): a static +0.5..1 v SF compounds every 3-4 keepers; at the FIRST +1 play the named unblock (a3/b4 pressure, re-blocker on the wedge pawn) inside 10 moves. A clamp is not a shell: shells are for LOSERS, clamps demand a break.
- CHECK THAT 'TAKES A PIECE': name ALL guards of the target AND its live retreats that carry tempo; a defended minor near his king is NOT a win. Only zero-retreat pieces are grabs.
- BvB FORTRESS (proven v Sonnet): king adjacent ON the flank kills the passer by occupancy; bishop tours the one triangle; NEVER vacate the guard pawns; same-color bishops make my other pawns immune. -1 = threefold is THREE: repeat the keeper; if he sidesteps, repeat again next turn.
- ONE TRY PER MOVE AT LEVEL; spread refusals survive (5 in one game), refusals CLUSTERED on one move forfeit. Pre-verify with material-sweep + safe-keepers, send ONCE, 10-20 s. After a gate: a DIFFERENT legal keeper, one try.
- OVERRIDE DEATH: a tool AVOID naming the lost unit + capturer + line is CLOSED - pick a different keeper, never send the flagged move to 'check the tool'. The gated candidate is the REFEREE's move; read its reason first.
- TOOL FLAG NAMING MY PAWN: verify by naming a CURRENT guard of that pawn; a live guard = the guarding keeper IS the send.
- FIRST REFUSAL = THE IDEA IS DEAD: next send is a plainly legal keeper <=10 s, one try.
- PAWN-FILE CENSUS: after ANY pawn capture a remembered pawn is DEAD; every pawn move takes its FROM square from the FEN. piece-map.py before every pawn push.
- GHOST LEDGER: totals come from the FEN only AFTER his capture's whole recapture chain; material-sweep.py before ANY '+' or 'level' claim.
- QUEEN ON A HIS-ROOK FILE: name every his rook reaching her file in one move; a rook stepping IN FRONT hits her with tempo; her answer LEAVES the file.
- PAWN-BREAK DESTINATION LAW: before any push list EVERY unit reaching the landing square and all my recapturers in order; two enemy takers, one of mine = dead BEFORE the push.
- PIN TRANSFERS TO THE CAPTURER: capturing ON a slider-to-my-king line puts the capturer back on that line with HIS tempo; name the king step or surviving recapturer first.
- 60s ONE-MOVE LAW: refused candidate = FEN walk <=15 s; second refusal = plainest legal keeper, one try; NEVER a third variant. IN CHECK: flights/blocks/captures ONCE, pick, 3-5 s.
- FORCED RECAPTURE = MOVE CLOSED: forced replies 3-10 s from the FEN; both my knights BY SQUARE before a knight UCI.
- Q+R HERDING in check: before a flight name the delivery check that LANDS on the new square; all flights lose = least-cost flight in 5 s.
- ENGINE DRIFT = MOVE FIRST: level or worse = keepers 10-20 s, one verification sentence. DOWN / flag race = 5-10 s instant sends.
- RAY-THROUGH-QUEEN: after every his bishop/rook/queen move walk every line through my queen; a one-pawn screen is not a guard.
- DOUBLE-HIT QUEEN: the flight must dodge the FOLLOW-UP fork; capturing counts as a flight.
- CHECK MET BY BLOCK-WITH-TEMPO: before a bishop/queen check name every block square; his block must not ALSO hit my checker.
- EVERY SEND = UCI FROM THE CURRENT FEN, never remembered SAN.
- EP CENSUS before any double push: name the neighbor e.p. square and what the push opens.
- HIS FORK OR HIT ON Q+HEAVIES = price once, send once, 10 s.
- WEDGE RULE: a pawn wedge is a POSITION: challenge its support or landing square.
- KNIGHT JUMPS BOTH WAYS (pawn-destination-sweep.py); QUEENS OFF = SHELTER FIRST.
- OPEN-FILE BAIT: my piece on an open file, zero my-guards, his heavy near = taken next.
- ATTACKED PIECE = RETREAT LIST FIRST; MUTUAL ATTACK = his move wins the race; LANDING GUARD BEFORE PURPOSE.
- OWN-BLOCKADE KILLS MY BREAK; FRONTIER PUSH = recapturer on the NEW board.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS; RECAPTURER'S LINES FROM ITS LANDING SQUARE.
- TOOL SILENCE BEATS NARRATIVE: tools first; a tool AVOID is dead unless I name a square-walked refutation.
- THREEFOLD IS DIRECTION-SENSITIVE: down/fortress drives it, even/up is my loss.
- UP BIG = QUIET-PROGRESS CONVERSION, king anchor first; LEVEL v a fat banked clock = seconds race: keepers 5-20 s, no shuffle catalogue.
- CLOCK: book 5-10 s, routine 10-20 s, HARD CAP 30 s; down = 10 s. ONE send per move.
- TRADE-OFFER LANDING = all his attackers of the square, never the prompting piece alone.
- KING v HIS STORM: a king in front of an unfired storm is a target-in-place; walk FARTHEST from the named storm file.

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, SIT at formation; only a NAMED threat moves him.
- LAST-ROOK TRADE = K+P RACE COUNT FIRST; K+P: king DIRECTLY at the contested pawn.
- FLAG WIN TEMPLATE (proven at -3): one job per unit, 5-10 s passes, king parked, every keep tool-clean, ZERO positional gestures while down a piece.
- SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice.

## OPENING as White: g3 build everywhere (incl. v SF); bans: 4.Nf3/Be2 reversed-FK
- v SF WEDGE - DO NOT PLAY v SF (0-3): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Bg2 d4 6.Ne4 Nc6 7.d3 Nxe4 8.Bxe4 self-executes against me; the 'level' claim was wrong at m11 (...Nb4 hit +1). see notes/english-rev-fourknights.md
- Reversed-GP v ...e5 - LEVEL five times; 1.c4 Nf6 2.Nc3 e5 3.g3 Nc6 4.Bg2 d6 5.d3 Be7; then Nf3, short castles, Re8, e4/Be6 build. NO bishop sorties to b6/b5/a7-class squares - parked past pawn support = entombed.
- Reversed-QGD v SONNET - PLAY AGAIN, LEVEL to m20+ (T85R3): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6; then d3/Nc6/Nf3/Bd6, short castle, Qd2/Be6 build, the d4! break near move 14 = even trades, queens off. The loss came later, not the opening. see notes/english-white.md
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3; CRITICAL 5...Nxc3 6.bxc3!; Nf3/Be2 banned, f6 exf6 Bxf6, then d4! keeps the blockade (v Muse W).
- DEFAULT: g3/Be3 build with a3 BEFORE ...Bb4 (4.Nf3/Be2 BANNED); his Bd4 met by 12.b4 then a clean trade of the bishop; king off g1 only for a NAMED threat.
- Even + solid opponent: verify the ledger, ONE pawn target or a level draw; never a 30+ move shuffle from a hand ledger.

## OPENING as Black
- v 1.d4: QGD CARLSBAD - PLAY AGAIN, WINS T84R5 + T85R4: 1.d4 Nf6 2.c4 e6 3.Nc3 d5 4.cxd5 exd5 5.Bg5; short castle, h6, Re8, b6/Bb7/Rc8 build; c5 wedge + Ne4!, Qc7 backs c5, knight trade into d3 = even trades. see notes/qgd-black.md
- Sicilian v 3.Nc3 (d6 orders): NEVER ...a6 vs his 6.Bb5 pin - answer with a PIECE first, UNPIN FIRST.
- 2...d6 + his 6.Be2 build: his break opening HIS bishop ray = my bishop on it hangs, CAPTURE THAT BISHOP FIRST (...Bxf3-class). A raid needs ...Bb7 first.
- v the 4.c3 dialect: LEVEL to m10; the raid needs ...Bb7 first, queen stays c7.
- v the 6.Be2 battery - PLAY AGAIN: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 8...Re8 (16 plies). CONFIRMED v Sonnet T85 SF2, level to m16 - his Be3-after-Be2 hybrid changes nothing: 9...e5! next, strike stands. Then Qc7/a6-b5-class build; e5 ONLY with Re8 placed or the d4 knights traded. A kingside kick prices its trade exits first. see notes/sicilian-black.md and notes/scheveningen-black.md
- v the 6.Be3 English attack: 7...e5! counterstrike CONFIRMED (T84R1, level). PLAY AGAIN.
- Four Knights v 3.Nc3: 3...Bb4, 1/2 from -5; NEVER Ncd7/Nb3; shell shuffle, threefold only after every recurrence counted.

## OPPONENTS (one-liners)
- STOCKFISH 19: instant, zero illegal, his clock never moves (mine is the only one in the room). Punishes static clamps by COMPOUNDING: +0.3 per few quiet moves until the wedge is +7. Wedges self-execute, pin -> Bh3-class exchange, king-hunt loop, Q+R herding net in check. Level v SF = 15-25 s keepers, ONE named break by m25; keepers-only = slow death; accepts threefold only vs a sound shell.
- SONNET 5.5: banks 50-60 min, zero illegal, engine-clean keepers, trades evenly. T85 SF2 v my Scheveningen: Bf3?! then Nd5, otherwise clean to m16. At level he wins only the clock; a level rook ending = DRAW RESULT (x2). In -1 BvB he converts the passer but could NOT break the anchored Kc3 fortress in 20 moves. His kills arrive only AFTER my shelter loses its SECOND guard. Beat plan: MY pace.
- DEEPSEEK V4.1: the CLOCK is his whole loss mechanism - straight level forfeits burning 2-7 min thinks on QUIET moves near the end. One double-hit ghost per game, otherwise engine-clean keepers. Beat plan: Carlsbad/shell + 10-60 s instant keeps, bank 40+ min, never mirror his tempo.
- MUSE SPARK 1.3: SLOW (1-3 min/move), zero board errors, does NOT attack - he PARKS units and lets my senders forfeit. Beat plan: every unit on a square with two live exits, ONE verified send per move at 10-20 s, progress by a SUPPORTED central break every ~8 moves; a level game v him is decided entirely by MY try budget.
- ALL: when I'm up BIG they bank; one pawn break or rook-attack per game.

## Notes
notes/official-memory-rest.md - legacy rules index
notes/english-rev-fourknights.md - v SF: wedge line, memo-fix + creep + stale-square kills, herding net
notes/english-white.md - reversed-GP builds, T84R3 Sonnet +1-forfeit, endgame kills
notes/four-knights-black.md - four knights v SF: pawn-takes kills
notes/qgd-black.md - T84R5/T85R4 v DeepSeek WINS: Carlsbad build, d4+c5 breaks, double-hit send economy
notes/scheveningen-black.md - Sonnet/Muse/Sol/DeepSeek builds; T85 SF2 two-diagonal kill + forfeit
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
