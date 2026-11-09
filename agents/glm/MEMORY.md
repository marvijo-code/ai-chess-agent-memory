# MEMORY - GLM 5.3 Flash

Last change: T86R5 DRAW fifty-move m83 v Sonnet as Black (Scheveningen battery 6.Be2): sealed level from ~m30, halfmove 40-99 chased, honest result.

## FIRST, EVERY GAME
- 50-MOVE COUNT LAW (T86R5): locked level + every break tool-closed + opponent with no forcing plan = the halfmove clock IS the plan. King-pair + rook/queen keeper loops ONLY; read the halfmove count from the FEN every send and write 'halfmove N, X his-quiet-moves to 100' in the comment. ZERO captures and ZERO pawn pushes from ~m40 on - each resets the count. His tour squares (9th rook square, 5th queen square) guard nothing; at level a fifty-move finish is a full result.
- LOCKED FORTRESS = HONEST DRAW (T86R4): every pawn break tool-closed + both kings boxed = fire ONE hook (a5/b5-class with the rook ready behind it), then keeper loops; never force progress. Duty packs: the ray-blinding bishop (Bf6-v-Rg6) and its rook backup; d6 stays double-rook-covered (Rd7/Rd8 never leave together, Rxd6 always a rook-for-pawn suicide); NEVER a king step while that king is the sole guard of a screen-backed rook.
- STALE-SQUARE RATCHET (T85R5, T86R5 m55 g8g7 flagged - the king stood g7): every send re-derives the MOVER's square from the CURRENT FEN in one line: piece@sq -> UCI; the moving KING included. Stale squares are my top forfeit cause. Send PLAIN UCI, never SAN (ambiguity = instant illegal try).
- REFUSAL LIST EXPIRES PER-MOVE (T85 3rd): gated/AVOID calls never survive a QUIET move; a refusal is about ONE position. Before every send count sendable keepers >2; if not, the plain one-step retreat of the attacked unit IS the send - send once, resend SAME if flagged.
- ONE TRY PER MOVE AT LEVEL: pre-verify (material-sweep + safe-keepers), send ONCE, 10-20 s. A refusal naming ONLY ~1 pawn in a level/borderline position = NOISE: RESEND SAME once. A MATERIAL gate (piece/rook/exchange/mate) = a DIFFERENT legal keeper, one try. Cycling a third different candidate forfeited T86R3.
- SHELTER VS RACE (T85 3rd): v his h4-h5 hold f7/g7/h7 SHUT; gxh5 opened the h-file his Rf5 rebuilt on for a whole ending. In a queenless race every opened file near both kings is HIS tempo weapon.
- MEMO FIX = NAME ITS CURRENT TARGET: a stored answer fires only if its target EXISTS on this board; write who occupies each square it touches.
- TWO-DIAGONAL RECAPTURE (T85 SF2): before ANY piece trade list MY units on the recapturing PAWN's both forward diagonals; two of mine = the trade loses material (...Nxd5-class is dead unless both hit squares are free).
- FLAG-NET REPLY = ONE FEN CHAIN: a referee/material flag = a COUNT, not a puzzle; derive the reply chain from the CURRENT FEN, send ONCE at 10 s; no 1-min re-think, no variants, no third different move.
- WEDGE-CREEP LAW (T85R5): static +0.5..1 v SF compounds every 3-4 keepers; at the FIRST +1 play the named unblock inside 10 moves.
- CHECK THAT 'TAKES A PIECE': name ALL guards of the target AND its live tempo retreats; a defended minor near his king is NOT a win - only zero-retreat pieces are grabs.
- BvB FORTRESS (proven v Sonnet): king adjacent ON the flank kills the passer by occupancy; bishop tours one triangle; NEVER vacate the guard pawns; -1 = threefold is THREE: repeat the keeper, if he sidesteps repeat again next turn.
- OVERRIDE DEATH: a tool AVOID naming the lost unit + capturer + line is CLOSED - pick a different keeper, never send the flagged move to 'test' it. TOOL FLAG NAMING MY PAWN: verify by naming a CURRENT guard; the live guard IS the send. FIRST REFUSAL = idea dead; next send a plainly legal keeper <=10 s, one try. IN CHECK: flights/blocks/captures once, pick, 3-5 s. Refusal 2 = plainest keeper; never a third variant.
- PAWN-FILE CENSUS: after ANY pawn capture a remembered pawn is DEAD; piece-map.py before every pawn push. GHOST LEDGER: totals from the FEN only AFTER his capture's whole recapture chain; material-sweep.py before ANY '+'/'level' claim.
- QUEEN ON A HIS-ROOK FILE: name every his rook reaching her file in one move; a rook in FRONT hits her with tempo; her answer LEAVES the file.
- PAWN-BREAK DESTINATION LAW: before any push list EVERY unit reaching the landing and all my recapturers in order; two enemy takers, one of mine = dead BEFORE the push (own blockade kills my break).
- PIN TRANSFERS TO THE CAPTURER: capturing ON a slider-to-my-king line re-pins with HIS tempo; name the king step or surviving recapturer first.
- FORCED RECAPTURE = MOVE CLOSED: 3-10 s; both my knights BY SQUARE before a knight UCI. Q+R HERDING in check: before a flight name the check that LANDS on the new square; all flights lose = least-cost flight in 5 s.
- ENGINE DRIFT = MOVE FIRST: level or worse = keepers 10-20 s with one verification sentence; DOWN / flag race = 5-10 s instant sends.
- RAY-THROUGH-QUEEN: after every his bishop/rook/queen move walk every line through my queen; a one-pawn screen is not a guard.
- FORK CHAIN, ONE HIS TEMPO PER CAPTURE (notes/sicilian-black.md): before a queen capture near his pieces name every knight/rook jump at her landing and each royal chain it opens; settle her FIRST (Ra6/g6/Be7-class. Up >=+3: quiet progress, zero grabs.
- OPENING LINES (16 plies = stored): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 then d3 - PLAY AGAIN. 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3 - PLAY AGAIN vs Muse. All other lines in notes.
- CLOSING LINE: at every move point consult note files first; nothing new is added here except 50-MOVE LAW.

- A ATTACKED PIECE: every dial lists ALL its lines by square; a triple-walk; LANDING GUARD BEFORE PURPOSE.

## newer one liners
- WEDGE RULE: name the support first; a sealed block = a keeper.
- RAY-WALK AFTER EVERY CAPTURE: every vacated line must be re-walked; seal-push = target-builder (name who guards the attacked front square; a level lost-a-pawn line sees ONE resend, not retries).

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, SIT; only a NAMED threat moves him. QUEENLESS LEVEL: both kings trapped = his bishop/rook tempo hits are the only decision; rooks leave squares NOT adjacent to his bishop's next diagonal.
- SEAL-PUSH = TARGET-BUILDER: an unguarded new front square that cannot be re-guarded = lose-1-and-play-on: ONE resend, never a 3-try hunt.
- ARTILLARY BANK: keep a bucket of unchecked safe keepers: at 50-move law, banks roll.
- DEAD LOCKED LEVEL: keeper loops AND the halfmove count AND threefold keys: count BOTH (thumb: halfmove N, his-x-quiet to 100; same-position repeats by mover).
- KING SHUTTLES LOSE TO NOTHING: in still shells steer mini-orbits not new squares; tour-set-blocking means bright states.
- LAST-ROOK TRADE = K+P RACE COUNT FIRST; K+P: king DIRECTLY at the contested pawn.
- FLAG WIN TEMPLATE (proven at -3): one job per unit, 5-10 s passes, king parked, every keep tool-clean, ZERO gestures while down a piece.
- SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice.

## OPENING as White: g3 build everywhere (incl. v SF); bans: 4.Nf3/Be2 reversed-FK
- Reversed-GP v ...e5 - LEVEL six times incl. T86R4 black mirror; then d3/Bg2/Be7/Nf3 build - NO bishop parked past pawn support = entombed.
- Reversed-QGD v SONNET - PLAY AGAIN (16 plies): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6, then NEIGHBOR build; the d4! break near m14. The loss came later, never the opening. BANS: 4.Nf3/Be2; SF wedge 0-3; h4-h5 seal.

## OPENING as Black
- SCHEVENIN GEN v 6.Be2 battery - PLAY AGAIN 3x: T86R5 1/2 m83 (16 plies): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 8...Re8; 9...e5! strike; then d5-break region, h6!+g5 seal structure = TRUE SHELL; KEPT: from m40 ZERO pushes/captures + king pair loops = fifty m83. see notes/scheveningen-black.md
- v 1.c4 ENGLISH MIRROR - PLAY AGAIN (16 plies, T86R4 1/2 m58): 1...Nf6 2.Nc3 e5 3.Nf3 Nc6 4.g3 d6 5.Bg2 Be7 6.O-O O-O 7.d3 Re8 8.e4; .see notes/muse-level-white.md
- v 1.d4: QGD Carlsbad - PLAY AGAIN, wins T84R5 + T85R4: c5 wedge + Ne4!, knight trade = even. see notes/qgd-black.md
- Sicilian v 4.c3 Morra (PLAY): ...dxc3! 5.Nxc3 Nc6 - honest pawn up; piece-first build; Bxc6-class even trades; losses were CONVERSION (exf4??), never the opening.
- Sicilian d6 orders: NEVER ...a6 into his Bb5 pin - PIECE first, UNPIN FIRST; his break opening HIS ray = CAPTURE THAT BISHOP FIRST.
- 6.Be3 dialect: 7...e5! strike; O-O-O his means RACE: b4, Rb8, Bb7, Qc7, a5, a4!; NO ...g6 vs h4-h5.
- Four Knights v 3.Nc3: 3...Bb4; NEVER Ncd7/Nb3; shell until every recurrence counted.

## OPPONENTS (one-liners)
- SONNET 5.5: banks 50-60 min, zero illegal, engine-clean keepers, trades evenly. T86R5: 58 banked bought ZERO entries in a sealed shell; at level otherwise he wins only the clock; kills only AFTER my shelter loses its SECOND guard; beats = MY pace or in shelf shells the HALFMOVE count.
- STOCKFISH 19: instant, zero illegal, clock never moves. Punishes static clamps by COMPOUNDING. Punishes greed with the NEXT tempo, not recapture: exf4?? at B+4 was a royal chain, mate m18. Level v SF = 15-25 s keepers, ONE named break by m25; keepers-only = slow death.
- DEEPSEEK V4.1 Flash: loses by CLOCK only: 8:55 on Qb4-class quiet moves v flag race; ended 27 min v my 50 banked. Board: engine-clean. Beat plan: pre-verified keepers 10-20 s, bank 40+, ONE frozen move per flag.
- MUSE SPARK 1.3: SLOW, few board errors, does NOT attack - parks units; locked shells self-freeze (e4/f5 wedge). Beat plan: every unit two-exit, ONE verified send per move 10-20 s PLAIN UCI, progress by a SUPPORTED break every ~8, then loops; a level game is decided by MY try budget.
- ALL: when I'm up BIG they bank; one pawn break or rook-attack per game.

## Notes
notes/english-rev-fourknights.md - v SF wedge line, memo-fix + creep + stale-square kills, herding net
notes/english-white.md - reversed builds incl. T86R3 v DeepSeek, T84R3 Sonnet +1-forfeit, endgame kills
notes/qgd-black.md - T84R5/T85R4 v DeepSeek WINS: Carlsbad build, d4+c5 breaks, double-hit send economy
notes/scheveningen-black.md - T86R5 fifty-move white-shell draw + T85R7 Muse race + T85 SF2 two-diagonal kill
notes/sicilian-black.md - 4.c3/Morra accepted T86 fork-chain kill, +9 shell
notes/taimanov-sol.md - 6.Be2 battery: strike confirmed, block-with-tempo
notes/white-maroczy.md - Maroczy; 7.f3! pin fix; SHORT castle; b2 mate door
notes/muse-level-white.md - v Muse: T86R4 black-mirror English, locked-fortress duty net, a5/b5 hook

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
