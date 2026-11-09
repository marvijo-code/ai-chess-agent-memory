# MEMORY - GLM 5.3 Flash

Last change: T86Semi1G1 L 0-1 m19 FORFEIT v SF19 as Black (Morra accepted): +2 squandered by 11...O-O-O?? (his a4/b4 then opened HIS file AT my king) and 17...hxg5?? - my own tool's pawn-loss flag was REAL, blind resend burned 11 min + 3 gated tries.

## FIRST, EVERY GAME
- FLAG CLASSIFIER (T86Semi FIX, hxg5?? dead): before ANY resend of a flagged move name the capturer BY SQUARE + its protection + my whole recapture chain. A flag over HIS capture reaching MY queen/rook/piece is REAL - change the move or take safe-keepers.py top. '~1 pawn = noise, resend same' is DEAD: it cost 11 min of clock and the game. Pawn-only blind resend now requires: all three named AND I stay up; NEVER when up material or down.
- 50-MOVE COUNT LAW (T86R5): locked level + every break tool-closed + opponent with no forcing plan = the halfmove clock IS the plan. King-pair + rook/queen keeper loops ONLY; read the halfmove count from the FEN every send and write 'halfmove N, X his-quiet-moves to 100' in the comment. ZERO captures and ZERO pawn pushes from ~m40 on - each resets the count.
- LOCKED FORTRESS = HONEST DRAW (T86R4): every pawn break tool-closed + both kings boxed = fire ONE hook (a5/b5-class with the rook ready behind it), then keeper loops; never force progress. Duty packs: the ray-blinding bishop and its rook backup; a pawn never stands double-rook-uncovered (Rxd6-class is rook-for-pawn suicide); NEVER a king step while that king is the sole guard of a screen-backed rook.
- ROOK ATTACKS MY QUEEN = QUEEN MOVES FIRST: a counter-capture 'priced' by me into near-even (Q for R+N, 'only -1') is a story, not a check; the eval standing behind it (his +6) removes it. Name the retreat squares when the file opens, send one.
- STALE-SQUARE RATCHET (T85R5, T86R5 m55): every send re-derives the MOVER's square from the CURRENT FEN in one line: piece@sq -> UCI; the moving KING included. Send PLAIN UCI, never SAN (ambiguity = instant illegal try). Under double attack: plain keeper <=10 s, FIRST refusal = idea dead, never a third variant.
- SHELTER VS RACE (T85 3rd): v his h4-h5 hold f7/g7/h7 SHUT; gxh5 opened the h-file his Rf5 rebuilt on for a whole ending. In a queenless race every opened file near both kings is HIS tempo weapon.
- MEMO FIX = NAME ITS CURRENT TARGET: a stored answer fires only if its target EXISTS on this board; write who occupies each square it touches.
- TWO-DIAGONAL RECAPTURE (T85 SF2): before ANY piece trade list MY units on the recapturing PAWN's both forward diagonals; two of mine = the trade loses material (...Nxd5-class is dead unless both hit squares are free).
- FLAG-NET REPLY = ONE FEN CHAIN: a referee/material flag = a COUNT, not a puzzle; derive the reply chain from the CURRENT FEN, send ONCE at 10 s; no 1-min re-think, no variants, no third different move.
- WEDGE-CREEP LAW (T85R5): static +0.5..1 v SF compounds every 3-4 keepers; at the FIRST +1 play the named unblock inside 10 moves.
- CHECK THAT 'TAKES A PIECE': name ALL guards of the target AND its live tempo retreats; a defended minor near his king is NOT a win - only zero-retreat pieces are grabs.
- BvB FORTRESS (proven v Sonnet): king adjacent ON the flank kills the passer by occupancy; bishop tours one triangle; NEVER vacate the guard pawns; -1 = threefold is THREE: repeat the keeper, if he sidesteps repeat again next turn.
- PAWN-FILE CENSUS: after ANY pawn capture a remembered pawn is DEAD; piece-map.py before every pawn push. GHOST LEDGER: totals from the FEN only AFTER his capture's whole recapture chain; material-sweep.py before ANY '+'/'level' claim.
- QUEEN ON A HIS-ROOK FILE: name every his rook reaching her file in one move; a rook in FRONT hits her with tempo; her answer LEAVES the file.
- PAWN-BREAK DESTINATION LAW: before any push list EVERY unit reaching the landing and all my recapturers in order; two enemy takers, one of mine = dead BEFORE the push.
- PIN TRANSFERS TO THE CAPTURER: capturing ON a slider-to-my-king line re-pins with HIS tempo; name the king step or surviving recapturer first.
- FORCED RECAPTURE = MOVE CLOSED: 3-10 s; both my knights BY SQUARE before a knight UCI. Q+R HERDING in check: before a flight name the check that LANDS on the new square; all flights lose = least-cost flight in 5 s.
- ENGINE DRIFT = MOVE FIRST: level or worse = keepers 10-20 s with one verification sentence; DOWN / flag race = 5-10 s instant sends. GATE CASCADE = 11 min of clock per blunder-trap: run safe-keepers.py FIRST, play its top, never re-argue inside a race.
- RAY-THROUGH-QUEEN: after every his bishop/rook/queen move walk every line through my queen; a one-pawn screen is not a guard.
- FORK CHAIN, ONE HIS TEMPO PER CAPTURE: before a queen capture near his pieces name every knight/rook jump at her landing and each royal chain it opens; settle her FIRST. Up >=+3: quiet progress, zero grabs near his pieces.
- OPENING LINES (16 plies = stored): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 then d3 - PLAY AGAIN. 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3 - PLAY AGAIN vs Muse. All other lines in notes.
- CLOSING LINE: at every move point consult note files first; nothing new is added here except FLAG CLASSIFIER and 50-MOVE LAW.

## newer one liners
- WEDGE RULE: name the support first; a sealed block = a keeper.
- RAY-WALK AFTER EVERY CAPTURE: every vacated line must be re-walked; seal-push = target-builder (name who guards the attacked front square).

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, SIT; only a NAMED threat moves him. QUEENLESS LEVEL: both kings trapped = his bishop/rook tempo hits are the only decision; rooks leave squares NOT adjacent to his bishop's next diagonal.
- SEAL-PUSH = TARGET-BUILDER: an unguarded new front square that cannot be re-guarded = lose-1-and-play-on: ONE resend, never a 3-try hunt.
- ARTILLARY BANK: keep a bucket of unchecked safe keepers: at 50-move law, banks roll.
- DEAD LOCKED LEVEL: keeper loops AND the halfmove count AND threefold keys: count BOTH.
- KING SHUTTLES LOSE TO NOTHING: in still shells steer mini-orbits not new squares.
- LAST-ROOK TRADE = K+P RACE COUNT FIRST; K+P: king DIRECTLY at the contested pawn.
- FLAG WIN TEMPLATE (proven at -3): one job per unit, 5-10 s passes, king parked, every keep tool-clean, ZERO gestures while down a piece.
- SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice.

## OPENING as White: g3 build everywhere (incl. v SF); bans: 4.Nf3/Be2 reversed-FK
- Reversed-GP v ...e5 - LEVEL six times incl. T86R4 black mirror; then d3/Bg2/Be7/Nf3 build - NO bishop parked past pawn support = entombed.
- Reversed-QGD v SONNET - PLAY AGAIN (16 plies): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6, then NEIGHBOR build; the d4! break near m14. BANS: 4.Nf3/Be2; SF wedge 0-3; h4-h5 seal.

## OPENING as Black
- MORRA v 4.c3 (REPAIR, T86Semi 0-1 m19): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 4...dxc3! 5.Nxc3 Nc6 - +1 honest and unhurt to m12; the losses were 11...O-O-O?? (SKIP castling, play ...Be6 hitting Nd5; long castle put my king on his a4/b4 file-raids: 12.b4 = +8.7, queen netted at b4) and 17...hxg5?? (blind resend, Rxc5+ took the Q; the tool already said so). CASTLE SHORT v the Morra, piece-first build, Bxc6-class even trades only.
- SCHEVENINGEN 6.Be2 battery - PLAY AGAIN 3x: T86R5 1/2 m83 (16 plies): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 Re8; 9...e5! strike; d5-break region, h6!+g5 seal = TRUE SHELL; from m40 ZERO pushes/captures + king pair loops = fifty m83. see notes/scheveningen-black.md
- v 1.c4 ENGLISH MIRROR - PLAY AGAIN (16 plies, T86R4 1/2 m58): 1...Nf6 2.Nc3 e5 3.Nf3 Nc6 4.g3 d6 5.Bg2 Be7 6.O-O O-O 7.d3 Re8 8.e4. see notes/muse-level-white.md
- v 1.d4: QGD Carlsbad - PLAY AGAIN, wins T84R5 + T85R4: c5 wedge + Ne4!, knight trade = even. see notes/qgd-black.md
- 6.Be3 dialect: 7...e5! strike; O-O-O his means RACE: b4, Rb8, Bb7, Qc7, a5, a4!; NO ...g6 vs h4-h5.
- Four Knights v 3.Nc3: 3...Bb4; NEVER Ncd7/Nb3; shell until every recurrence counted.
- Sicilian d6 orders: NEVER ...a6 into his Bb5 pin - PIECE first, UNPIN FIRST; his break opening HIS ray = CAPTURE THAT BISHOP FIRST.

## OPPONENTS (one-liners)
- STOCKFISH 19: instant, zero illegal, clock never moves. Punishes static clamps by COMPOUNDING and punishes greed with the NEXT tempo. v the Morra he strips the pawntruck fast: a4/b4 dominoes, Nd5 tempo on my queen, evals +0.9 -> +8.7 in four moves once my king sat on the b-file. Level v SF = 15-25 s keepers, ONE named break by m25; keepers-only = slow death.
- SONNET 5.5: zero illegal, engine-clean keepers, trades evenly. At level otherwise he wins only the clock; kills only AFTER my shelter loses its SECOND guard.
- DEEPSEEK V4.1 Flash: loses by CLOCK only; board engine-clean. Beat plan: pre-verified keepers 10-20 s, bank 40+, ONE frozen move per flag.
- MUSE SPARK 1.3: SLOW, few board errors, does NOT attack - parks units; locks self-freeze. Beat plan: every unit two-exit, ONE verified send per move 10-20 s PLAIN UCI, SUPPORTED break every ~8 then loops.
- ALL: when I'm up BIG they bank; one pawn break or rook-attack per game.

## Notes
notes/english-rev-fourknights.md - v SF wedge line, memo-fix + creep + stale-square kills, herding net
notes/english-white.md - reversed builds incl. T86R3 v DeepSeek, T84R3 Sonnet +1-forfeit, endgame kills
notes/qgd-black.md - Carlsbad build, d4+c5 breaks, double-hit send economy
notes/scheveningen-black.md - fifty-move white-shell draw + Muse race + two-diagonal kill
notes/sicilian-black.md - Morra T86Semi verdict: O-O-O ban, flag-classifier kill, forfeit anatomy
notes/taimanov-sol.md - 6.Be2 battery: strike confirmed, block-with-tempo
notes/white-maroczy.md - Maroczy; 7.f3! pin fix; SHORT castle; b2 mate door
notes/muse-level-white.md - v Muse: locked-fortress duty net, a5/b5 hook

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
