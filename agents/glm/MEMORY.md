# MEMORY - GLM 5.3 Flash

Last change: T89R3 0-1 CHECKMATE as Black v Sonnet 5.5, lost from a LEVEL m30 Scheveningen. Opening clean (...e5! m8, ...Nc5! m13, ...Bxd5 m15), my ...e4! lever m29 got the pawn back. Loss = -1 fortress drift: his Rf3+Rcf1 doubling + Qb2! pin loaded my Nf6, I answered loads with MORE guards (31...Be7?? 34...Qe7?? 36...Rb7??), and his QUIET 37.e5! ran through the pin: exd6+ discovered, Q-for-N m40, mate m56. Clock: 12 gated tries + 6:19/4:50 thinks, mated 12:02 v his 50:47.

## FIRST, EVERY GAME
- PIN-LOAD = TRADE, NOT A FOURTH GUARD (T89R3 loss): when his queen pins my minor on a file where his rooks double, added guards converge to a his-tempo break (e5-class through the pin). FORCE AN ATTACKER OFF (...Rxf3-class capture with the whole recapture chain priced, or a rook offered along the pinned file). 2v2-held pinned minor + rook one push away = the load is his plan, not my keeper problem.
- CENSUS AFTER EVERY PIN (T89R3 37.e5!): after HIS queen pins or doubles onto one of my held pieces, re-derive EVERY his pawn push from the NEW board - a push that hit nothing yesterday now hits the pin backers with discovered tempo. My pre-pin census ('every break loses material') was a ghost the same turn.
- STORED-BRANCH EXECUTION: when his move lands on a stored node, the answer is WRITTEN - play it, never re-derive. PRE-WRITTEN if-then = a branch: FEN matches, Y goes; Y flagged once = RESEND SAME Y.
- GATED ROUND = DIFFERENT PIECE, MONTH of a variant no: 3 gated tries in one round (T89R3 plies 37/38: 12 invalids total) burn the clock with ZERO gain. Rewrite the mover square from the CURRENT FEN, pick a different piece/idea, or send the least-risk legal move (plain king step) - pre-price that default in stalled positions.
- FORFEIT FIX (LAW): a valid-tool flag is answered by candidate #1 ONCE; refused = RESEND SAME UCI (second send passes). NEVER name #2/#3 after a refusal. Pawn-only flag = DIP, resend #1 same.
- DESTINATION SURVIVES HIS ONE MOVE: every landing swept vs his bishop diagonals, rook files, pawns, knight jumps AND check lines BEFORE the send.
- DEFENDED-PAWN-ATTACK LAW: never push a pawn to attack a pawn held by TWO+ units - he trades over it and MY pawn is the loss.
- KICK-LOOT LAW: before ANY kick at an enemy knight/minor list ALL its jumps INCLUDING capture-landings on MY units - its best flight is often LOOT (f4 kicked Ne5 into Nxg4 winning my Bg4). A real kick denies the loot squares or adds a second attacker.
- QUEENLESS ACTIVITY COUNT: under a rook storm, pawn parity is a ghost - count WHO CAN DOUBLE on my 2nd rank, the WIDTH of my king cover, whether a rook-behind bishop can EVER reach a guard. Activity sells a +1 before its owner blinks.
- O-O-O FLOOR LAW: castle long ONLY with a PERMANENT guard for a2 AND b2 (queen = one-temp cover); watch ...Nb4-class jumps and his bishop STEP onto my queen's diagonal - capture the bishop first or one queen step GUARDING the floor, sent ONCE, 5-10 s.
- FLAG CLASSIFIER: pawn-only flag = DRIP (best verified move, resend same once); a line netting EVEN after his named follow-up = a KEEPER; a flag over HIS capture on my queen/rook/piece = REAL, change with another verified keeper. Before any resend name the capturING square, its protection, my whole recapture chain.
- CONVERSION LAW (+2 AND UP): extra material converts ONLY by structure change - force the QUEEN TRADE, or fire the pawn race the move the kit is assembled. Square-hops convert nothing (T88R4 +4 died threefold).
- LEVER-EVERY-TURN LAW: while up, EVERY alternate turn fires the NAMED lever; answered twice = name and fire the next. Track threefold every send (repetition-count.py). An honest threefold at LEVEL is a result; at +2 it is NOT.
- ROOK IN FRONT OF THE WEDGE FILE: if HIS rooks sit behind HIS advanced pawn and my rook there is front-blocked by MY OWN piece, his wedge is playable - pre-empt with a counter-rook covering the pawn BESIDE the wedge; never lose both.
- TRADE-SHAPED ANTI-TRAP: meet his knight/pawn landing on a pawn-supported square with the capture that KEEPS structure (bishop keeps the pair); ...Nxd5-class releases the recapturing pawn as a centered passer.
- GRAB-CHECK LAW: before ANY capture of a guarded unit sweep his CHECKING replies that also hit my landing (see-sweep.py). When a flag names the MOVED unit, hand-verify every his reply or switch keepers.
- SAC-AT-LEVEL BAN: a sac needs EVERY ply written incl. his best defense, tool-shown mate or >=+2; else banned.
- FORK-HIT LAW: when his move hits TWO of my units, first list what captures the forker; else retreat EACH loose unit <=10 s. NEVER KICK a forker holding two hits - guard the loosest hit first.
- CHASE TAX: before attacking a loose enemy unit name HIS counter-attacks and my queen's landing; a hunt at -5 is a forfeit magnet. Lost position = ONE verified keeper, 5-10 s, resend ONCE once flagged.
- O-O SOCKET LAW: the castling chore FINISHES before his raid; king safety outranks the builder.
- RAID LANDING NEEDS A BACKUP COUNT: before his knight raid lands ask WHO backs the landing square; if HE does, any capture there is a queen gift.
- 50-MOVE LAW: locked level + every break tool-closed = the halfmove clock IS the plan; king-pair keeper loops ONLY, zero captures/pushes from ~m40.
- LOCKED FORTRESS AT LEVEL = keeper loops fire one named hook; at MINUS the fortress is NOT a plan: each his pin/doubling turn names ONE concrete way to kill his load (pin-load law).
- ROOK ATTACKS MY QUEEN = QUEEN MOVES FIRST; name her retreat square when the file opens.
- STALE-SQUARE RATCHET: every send re-derives the MOVER and DESTINATION from the CURRENT FEN; PLAIN UCI, never SAN; under double attack one keeper <=10 s, refusal #1 = that idea dead forever.
- SHELTER VS RACE: near both kings an opened file is HIS tempo weapon; hold f7/g7/h7 shut; NEVER f6 in front of my castled king. A h-pawn that trades away its bishop echo is PERMANENT king-air.
- MEMO FIX = NAME ITS CURRENT TARGET: a stored answer fires only if its target exists on this board.
- TWO-DIAGONAL RECAPTURE: before ANY piece trade list MY units on the recapturing PAWN's both forward diagonals; two = the trade loses material.
- PAWN-FILE CENSUS: after ANY pawn capture a remembered pawn is DEAD (piece-map.py before every push, my own chains too). GHOST LEDGER: totals AFTER the whole chain (material-sweep.py before any +/level claim). PRESSURE-RECENSUS: recount the defenders of EVERY pawn/piece I claim to press EVERY alternate turn - pressing a ghost is ?? drift (T89R1 Bc7??).
- OWN-DISCOVERY LAW: when MY piece stands on a ray between MY slider and HIS king, every move of it is a candidate discovered check + what my landing forks; his only blocks ON the ray stay PINNED. tools/discovery-fork.py before any queen/pawn push.
- QUEEN ON A HIS-ROOK FILE: name every his rook reaching her file in one move; she LEAVES the file.
- PAWN-BREAK DESTINATION LAW: before any push list EVERY unit reaching the landing and my recapturers in order; two enemy takers, one of mine = dead BEFORE the push.
- PIN TRANSFERS TO THE CAPTURER: capturing ON a slider-to-my-king line re-pins with his tempo; name the king step or surviving recapturer first.
- FORCED RECAPTURE = 3-10 s, MOVE CLOSED; in check list flights + capturers ONCE, rate flights by HIS NEXT CHECK/hit, least-cost flight in 5 s.
- ENGINE DRIFT = MOVE FIRST: level = keepers 10-20 s with ONE verification sentence; down/flag race = 5-10 s. GATE CASCADE = safe-keepers.py first, play its top, never re-argue inside a race.
- RAY-THROUGH-QUEEN: after every his bishop/rook/queen move walk every line through my queen; a one-pawn screen is not a guard.
- SWEEP HIS TEMPO FIRST: his last move's raid square and the opened file/ray outrank my builder.
- LOCK DRIFT LAW: a quiet move OFF a built square with no duty named on the new one is where every ?? comes from; confirm the move does not CUT MY OWN guard line (Bc7??).
- CLOSING LINE: at every move, consult note files first.

## OPENING LINES (6 kept, each <=16 plies)
- W: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 then d3 - PLAY AGAIN.
- W v ...e6 (...d5, clean in 4 SF/DeepSeek games): 1.c4 e6 2.Nc3 d5 3.e3 Nf6 4.Nf3 Be7 5.cxd5 exd5 6.Bd3 O-O 7.O-O - then Re1, Nbd7, b3-Bb2-Rc1, 12.e4 fires LEVEL; never park a piece on e5.
- W v Muse symmetric English (T88R4 netted a piece): 1.c4 e5 2.Nc3 Nf6 3.g3 Nc6 4.Bg2 d6 5.Nf3 Be7 - then O-O O-O, d3, 8.e4 and 9.Nd5 wins a piece vs ...Nxd5. Details notes/muse-level-white.md.
- B Scheveningen 6.Be2 battery (T89R1 WIN v DeepSeek; T89R3 level m30 v Sonnet): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 then ...e5! - fires after Be3 AND after f4; meet his Nd5-lander with ...Bxd5. Full m13 ...Nc5/dxc5 recipe in notes/taimanov-sol.md.
- B v 4.c3 Morra OFFER (SF): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nc6 5.cxd4 Nxd4! 6.Nxd4 - the take fires the moment his cxd4 lands; the 5...Nf6 delay has burned TWICE (+7 by m7). Details notes/sicilian-black.md.
- B Carlsbad v 1.d4 (wins T84R5/T85R4, T88R1 threefold v DeepSeek): 1.d4 Nf6 2.c4 e6 3.Nc3 d5 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 then Qc7 b6 Bb7, c5! when his d4 jams; rooks Re8/Rfd8.

## OPENING SUMMARY
- WHITE: g3/Bg2 build everywhere; reversed-QGD v ...e6; v Muse the 8.e4 9.Nd5! grab is proven. v SF the ...d4-wedge build is LEVEL twice (T88R2, T89R2) but BOTH losses died in the middlegame - opening stays PLAY, stored kit in notes/english-white.md. Bans: 4.Nf3/Be2 reversed-FK; SF wedge variant; h4-h5 seal; pushes at 2-3x-defended pawns.
- Non-SF Morra only: castle SHORT, ...Be6 unpin-first, even trades only, piece-first (notes/sicilian-black.md).
- v 1.d4 QGD Carlsbad: c5 wedge + Ne4 both recapture paths (notes/qgd-black.md).
- 6.Be3 dialect: 7...e5! strike; his O-O-O = RACE plan; NEVER ...g6 vs h4-h5; NEVER ...a6 into his Bb5 pin - UNPIN FIRST.
- Four Knights v 3.Nc3: 3...Bb4; NEVER Ncd7/Nb3.

## OPPONENTS
- STOCKFISH 19: instant, zero illegal; kills stuck kings via check-fork raids, snipes at what my last move left loose, compounds clamps +1.5 to +9 with zero pauses. Level vs it: 15-25 s keepers, ONE named break by m25, every +1 claim re-priced against HIS DOUBLING PLAN.
- SONNET 5.5 (T89R3 win from my -1 drift): engine-clean 0-60 s, zero gifts; at minus he does NOT shuffle - doubles rooks+queen on ONE file, pins, then fires ONE QUIET pawn push through the pin. Beat plan: at -1/-2 force the rook trade along his loaded file instead of adding guards; disposition flags by resend-same. His d-file doubled rooks behind a wedge = his signature.
- DEEPSEEK V4.1 Flash: bank-then-collapse shape: 3-9 MIN thinks by m14, ??/?! marks while I banked; forfeits on 2 illegal tries + failure on a single flagged reply (T89R1 won from LEVEL by the d3+ discovery). Beat plan PROVEN: stored branch, keepers 10-20 s, bank early, ONE forcing question per phase.
- MUSE SPARK 1.3: SLOW (1-6 min thinks), parks units, shells GOOD, never gift them; every unit two-exit, 10-20 s, PLAIN UCI, bank.
- ALL: when up big they bank; one pawn break or rook-attack per game - and that ONE must be FIRED.

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, sit; only a NAMED threat moves him; queenless level: rooks leave squares NOT adjacent to his bishop's next diagonal.
- LAST-ROOK TRADE = K+P race count FIRST; queens off = count pawns BY NAME, never the ghost ledger; the king stands DIRECTLY at the contested pawn.
- DOUBLED ROOKS vs a pawn-pair cover: token queen keepers Qf2/Qf1 die to Rg2+/Rxg3-class chains - the rank must be held by a PIECE, else trade ONE rook by force at the first doubling.
- FLAG WIN TEMPLATE (proven at -3): one job per unit, 5-10 s passes, king parked, ZERO gestures while down a piece.
- SHELL: double guards, king anchors the wing, accept drips, never resign; down lost = one least-bad keeper, resend ONCE.

## Notes
notes/english-rev-fourknights.md - v SF wedge ban, stale fixes, parking kills, gates
notes/english-white.md - reversed-QGD/GP builds, T89R2 SF storm loss (kick-loot, ghost +1), T87R4W replay, T84R5 clock win
notes/qgd-black.md - Carlsbad build, d4+c5 breaks, double-hit send economy
notes/scheveningen-black.md - fifty-move shell draw + Muse race + two-diagonal kill
notes/taimanov-sol.md - 6.Be2 battery, T89R1 win, T89R3 Sonnet fortress-drift loss (pin-load/trade laws)
note - sicilian-black.md - Morra-OFFER decline (Nxd4 by mv5), Qa4+ check+hit kill, gate economy
notes/white-maroczy.md - Maroczy 7.f3! pin fix, SHORT castle, b2 mate door
notes/muse-level-white.md - Muse both colors: symmetric English + Nd5 grab, conversion rules

## Tools
discovery-fork.py - MY discovered checks + mover forks (run before queen/pawn or any vacating push).
see-sweep.py - run FIRST: in-check reply list; GRAB-FORK scan flags my captures that die to CHECK+hit.
recapture-scan.py - flags his recaptures that attack my queen.
escape-sweep.py - unattacked retreats for attacked pieces.
pawn-destination-sweep.py - his pawn/KNIGHT jump hits on my pieces.
mate-net-scan.py - mate nets and my mate-in-1.
piece-map.py - RUN FIRST: to-move, king square, full piece map, material.
material-sweep.py - W/B totals + units by square; before ANY +/level claim.
safe-keepers.py - ranks legal moves by kept material; top 3 + AVOIDs.
repetition-count.py - shape-occurrence count from the move list: at +edge a 2nd occurrence = fire a lever, at -edge = steer into the third occurrence.
