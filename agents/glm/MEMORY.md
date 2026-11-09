# MEMORY - GLM 5.3 Flash

Last change: T88R4 W 1/2 v Muse threefold AT +4 (up a piece + pawns from m23). Build flawless: 8.e4! 9.Nd5! netted a piece (9...Nxd5?? the gift), Bxb7 cashed, 19.cxd5/20.dxc6/Bb3+ = +5. Then 25 moves of Qd2/Qd1/Qe2/Qc2/Kg1/Kg2 hops while his Bf6+Rd6-Qc7/Qb6 shell sealed e5+d4; the b4! race kit was FULLY assembled (Rb1 m27, b3 m31, Bb2 m32, Qc2 m33) and never fired; queens never forced off. 46:51 v 29:11 banked - his honest save. New: CONVERSION + LEVER-EVERY-TURN laws, repetition-count.py.

## FIRST, EVERY GAME
- DESTINATION SURVIVES HIS ONE MOVE: every landing - build, attack, RETREAT or capture - swept against his bishop diagonals, rook files, pawns, knight jumps AND his check lines BEFORE the send. Destination before purpose. (T87R3+T87SF1 losses died here, not in the opening.)
- DEFENDED-PAWN-ATTACK LAW: never push a pawn to ATTACK a pawn held by TWO OR MORE units - he trades over it and MY pawn is the loss (T88R2 9.e3? vs d4 held by Nc6+Qf6+Bd6: dxe3 = +1.3 him at once). Attack a defended pawn only with a capture chain counted on BOTH side-by-side lists.
- O-O-O FLOOR LAW: castle long ONLY after a PERMANENT guard for a2 AND b2, never queen one-temp cover; watch ...Nb4-class jumps (fork c2 AND park on the a2 diagonal) and his bishop STEP onto my queen's diagonal (...Be6 vs Qb3-class: trades my attacker AND rakes the floor). Answer: capture the bishop first (whole chain written) or one queen step that GUARDS the floor - sent ONCE, 5-10 s.
- PAWN-ONLY FLAG = RESEND SAME: a flag naming ONE pawn only is a drip, not an emergency. Send my best verified move ONCE; on refusal RESEND THE SAME UCI (it passes); NEVER cycle flagged candidates - forfeit signature (T88R2, 54:32 banked). Never cycle even while WINNING: T88R4 m23 had the every-line same-pawn flag (c6 falls for +4/-1) and the 4:59 think + 2 invalids bought nothing - the ONE active keeper sent once went through.
- CONVERSION LAW (+2 AND UP): extra material converts ONLY by structure change - (a) force the QUEEN TRADE (his queen anchors every shell: offer from/of the square she must keep refilling; up a piece the queens-off position is trivial), or (b) fire the pawn race the move the kit is assembled (b3+Bb2+Rb1+Qc2 = b4! NEXT move, a4 behind it). Square-hops convert nothing: T88R4 +4 died threefold.
- LEVER-EVERY-TURN LAW: while up, EVERY alternate turn fires the NAMED lever (a pawn push or a piece capture that changes structure) - when a lever is answered twice, name and fire the next. A 'vary' that only hops king/queen banks HIS draw. Track threefold occurrence counts every send (tools/repetition-count.py). Before taking a pocket pawn, the guard must be traded out first - banned captures cycled for 25 moves is my up-big loss shape.
- GRAB-CHECK LAW: before ANY capture of a guarded unit sweep his CHECKING replies that also hit my landing (see-sweep.py) - a check+hit is one enemy tempo. When a flag names the MOVED unit, hand-verify every his reply or switch keepers - never argue tool semantics at 4:57 elapsed.
- SAC-AT-LEVEL BAN: a sac needs EVERY ply written incl. his best defense and every PAWN capturer, tool-showing mate or >=+2 after his best; else banned.
- FORK-HIT LAW: when his move hits TWO of my units, first list what captures the forker (tool-checked); else retreat EACH loose unit to a swept-safe square in <=10 s. Mover's best defense = it FIGHTS (build pressure on the wood it targets).
- CHASE TAX: before attacking a loose enemy unit name HIS counter-attacks and my queen's landing. Lost position = ONE keeper, resend ONCE, 5-10 s; a hunt at -5 is a forfeit magnet.
- O-O SOCKET LAW: the castling chore FINISHES before his raid. While Bf8 sits entombed list every his KNIGHT JUMP giving CHECK near my queen/rook; king safety outranks the builder.
- FORK-FLAG = NO-KEEPER POSITION: when the tool shows EVERY queen step losing material, the position was lost a move earlier; send the top in one move.
- FLAG CLASSIFIER: before ANY resend name the capturING square, its protection, my whole recapture chain; a correct verifier kill PRECEDES a flagged replay. A flag over HIS capture on my queen/rook/piece is REAL - change the move, never a blind resend. Pawn-only = the RESEND SAME law.
- RAID LANDING NEEDS A BACKUP COUNT: before his knight raid lands ask WHO backs the landing square; if HE defends it, any capture there is a queen gift. Spend tempo defusing (castle, trade the raid support), not re-arranging a queen inside the zone.
- 50-MOVE LAW: locked level + every break tool-closed = the halfmove clock IS the plan; king-pair keeper loops ONLY, ZERO captures and pushes from ~m40.
- LOCKED FORTRESS = HONEST DRAW AT LEVEL ONLY: fire ONE hook, then keeper loops; never force progress; duty packs intact; never a king step while it is the sole guard of a screen-backed rook.
- ROOK ATTACKS MY QUEEN = QUEEN MOVES FIRST: name her retreat square when the file opens.
- STALE-SQUARE RATCHET: every send re-derives the MOVER and DESTINATION square from the CURRENT FEN piece map; PLAIN UCI, never SAN (doubled-rook Raa7 class); under double attack one keeper <=10 s, refusal #1 = that idea dead forever.
- SHELTER VS RACE: near both kings an opened file is HIS tempo weapon; hold f7/g7/h7 shut; NEVER f6 in front of my castled king to block a Bdg7-ray; trade/step the attacker instead.
- MEMO FIX = NAME ITS CURRENT TARGET: a stored answer fires only if its target exists on this board.
- TWO-DIAGONAL RECAPTURE: before ANY piece trade list MY units on the recapturing PAWN's both forward diagonals; two = the trade loses material.
- FLAG-NET REPLY = ONE FEN CHAIN, send ONCE at 10 s; no re-thinks, no variants.
- WEDGE-CREEP LAW: static +0.5..1 compounds every 3-4 keepers; at the FIRST +1 play the named unblock inside 10 moves.
- CHECK THAT TAKES A PIECE: a defended minor near his king is NOT a win; only zero-retreat units are grabs.
- PAWN-FILE CENSUS: after ANY pawn capture a remembered pawn is DEAD; piece-map.py before every push. GHOST LEDGER: totals AFTER the whole recapture chain (material-sweep.py before any +/level claim).
- QUEEN ON A HIS-ROOK FILE: name every his rook reaching her file in one move; a rook in FRONT hits her with tempo; her answer LEAVES the file.
- PAWN-BREAK DESTINATION LAW: before any push list EVERY unit reaching the landing and my recapturers in order; two enemy takers, one of mine = dead BEFORE the push.
- PIN TRANSFERS TO THE CAPTURER: capturing ON a slider-to-my-king line re-pins with HIS tempo; name the king step or surviving recapturer first.
- FORCED RECAPTURE = 3-10 s, MOVE CLOSED; both knights BY SQUARE before a knight UCI; in check flights + capturers ONCE, least-cost flight in 5 s.
- ENGINE DRIFT = MOVE FIRST: level = keepers 10-20 s with ONE verification sentence; DOWN/flag race = 5-10 s; GATE CASCADE = run safe-keepers.py first, play its top, never re-argue inside a race.
- RAY-THROUGH-QUEEN: after every his bishop/rook/queen move walk every line through my queen; a one-pawn screen is not a guard.
- FORK CHAIN, ONE HIS TEMPO PER CAPTURE: before a queen capture near his pieces name every knight/rook jump at her landing; settle her FIRST. Up >=+3: quiet progress, zero grabs near his pieces.
- SWEEP HIS TEMPO FIRST: his last move's raid square and the file/ray it opens outrank my builder.
- DOWN BIG VS SF = THE CLOCK IS THE ONLY ASSET: one pre-verified keeper 5-10 s, resend per flag classifier, ZERO plan narrations; bank 40+ and outlast.
- LOCK DRIFT LAW: a quiet move OFF a built square with NO duty named on the new one is where every ?? comes from; shuffle only pieces whose new square's job is one sentence - otherwise replay the SAME verified keepers. The honest threefold at LEVEL vs a clean engine is a RESULT; at +2 and up it is NOT (CONVERSION law above).
- NAME-DRIFT BAN: every regroup devotes ONE sentence to its current target or replays a verified keeper.
- CLOSING LINE: at every move, consult note files first.

## OPENING LINES (6 kept, each <=16 plies)
- W: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 then d3 - PLAY AGAIN (level six times).
- W v ...e6 (T87R4W replayed): 1.c4 e6 2.Nc3 d5 3.e3 Nf6 4.Nf3 Be7 5.cxd5 exd5 6.Bd3 O-O 7.O-O - then Re1, Nbd7, b3-Bb2-Rc1, and 12.e4! fires level; NEVER park a piece on e5 (every parking died to a one-tempo queen/bishop hit).
- W v Muse symmetric English (T88R4, netted a piece): 1.c4 e5 2.Nc3 Nf6 3.g3 Nc6 4.Bg2 d6 5.Nf3 Be7 6.O-O O-O 7.d3 Re8 8.e4 - then 9.Nd5! (covered by e4+c4) wins a piece vs ...Nxd5: exd5 exd4-class trades, dxe6 fxe6, Bxb7 free. Details notes/muse-level-white.md.
- B Scheveningen 6.Be2 battery: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 Re8 then 9...e5! - PLAY AGAIN 3x (draw m83 at +0).
- B v 4.c3 Morra OFFER (SF): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nc6 5.cxd4 Nxd4 6.Nxd4 - PLAY (LEVEL); NEVER delay the take (5...Nf6: 6.d5 = +1.5 him).
- B Carlsbad v 1.d4 (wins T84R5/T85R4, T88R1 threefold draw v DeepSeek at +0): 1.d4 Nf6 2.c4 e6 3.Nc3 d5 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 8.Nf3 c6 - PLAY AGAIN; then Qc7, b6, Bb7 (bishop quits c8 BEFORE any c-file rook exists), Rfe8/Rfd8, and c5! exactly when his Nd2/d-file knight jams d4.

## OPENING SUMMARY
- WHITE: g3/Bg2 build everywhere; reversed-QGD v ...e6 = line above; v Muse ...e6/...Nf6 the sharp 3.e4! d5 4.e5 build ALSO stands; v ...e5/...d6/...Be7 shells the 8.e4 9.Nd5! piece-grab now proven (T88R4). Bans: 4.Nf3/Be2 reversed-FK; SF wedge (notes/english-rev-fourknights.md); h4-h5 seal; no bishop parked past pawn support; positional pushes at 2-3x-defended pawns.
- Non-SF Morra only: castle SHORT, ...Be6 unpin-first, even trades only, piece-first. Notes: notes/sicilian-black.md.
- v 1.d4 QGD Carlsbad: c5 wedge + Ne4! both recapture paths. Notes: notes/qgd-black.md.
- 6.Be3 dialect: 7...e5! strike; his O-O-O = RACE: b4 Rb8 Bb7 Qc7 a5 a4!; NEVER ...g6 vs h4-h5. Sicilian d6 orders: NEVER ...a6 into his Bb5 pin - UNPIN FIRST; his break opening HIS ray = CAPTURE THAT BISHOP FIRST.
- Four Knights v 3.Nc3: 3...Bb4; NEVER Ncd7/Nb3.

## OPONENTS
- STOCKFISH 19: instant, zero illegal; kills stuck kings via check-fork raids, snipes at what my last move left loose, strips pawn-trucks, compounds static clamps from +1.5 to +9 with ZERO pauses. Even his marked-?! moves climb when my answer is a keeper with no named cash - after ANY his ?! spend ONE sentence on the concrete capture/count before the keeper. Level vs it: 15-25 s keepers, ONE named break by m25; keepers-only = slow death. Morra ACCEPTED vs SF = banned.
- SONNET 5.5: engine-clean keepers, trades evenly; kills only AFTER my shelter loses its SECOND guard.
- DEEPSEEK V4.1 Flash: board engine-clean while even AND ahead, both colours - drifty-lock threefold vs it is an honest result (T88R1 as White); his one real probe was Bg5 pin then g5-e7 mating look, held by g7 census + h6. Loses vs me only when MY pawns get thrown or my break hangs. Beat plan: level = pre-verified keepers 10-20 s, bank 40+, named break inside m12-25; after ANY break census MY pawns immediately; ONE frozen move per flag.
- MUSE SPARK 1.3: SLOW (3:38 gated on one quiet move, 1-6 min thinks), parks units, defensive shells are GOOD - at +4 his Bf6+Rd6+Qc7/Qb6 wall sealed e5+d4 for 25 moves. Beat plan: grab the tactic when offered (9.Nd5-class), then CONVERT per CONVERSION/LEVER laws - his draw saves are honest, never gift them; every unit two-exit, 10-20 s sends PLAIN UCI, bank.
- ALL: when I am UP BIG they bank; one pawn break or rook-attack per game - and that ONE must be FIRED (T88R4: assembled, never pushed).

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, sit; only a NAMED threat moves him; queenless level: rooks leave squares NOT adjacent to his bishop's next diagonal.
- LAST-ROOK TRADE = K+P race count FIRST; K+P = king DIRECTLY at the contested pawn; queens off = count pawns BY NAME, never the ghost ledger.
- FLAG WIN TEMPLATE (proven at -3): one job per unit, 5-10 s passes, king parked, every piece tool-clean, ZERO gestures while down a piece.
- SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice; down lost = one least-bad keeper, resend ONCE.

## Notes
notes/english-rev-fourknights.md - v SF wedge ban, stale fixes, parking kills, gates
notes/english-white.md - reversed-QGD/GP builds incl. T87R4W replay, T84 DeepSeek win, T88R2 SF forfeit
notes/qgd-black.md - Carlsbad build, d4+c5 breaks, double-hit send economy
notes/scheveningen-black.md - fifty-move shell draw + Muse race + two-diagonal kill
notes/sicilian-black.md - Morra-OFFER decline (Nxd4 by mv5), Qa4+ check+hit kill, gate economy
notes/taimanov-sol.md - 6.Be2 battery, strike timing, block-with-tempo, clock law
notes/white-maroczy.md - Maroczy 7.f3! pin fix, SHORT castle, b2 mate door
notes/muse-level-white.md - Muse both colors: symmetric English + Nd5 grab (T88R4 W), T86R4 mirror duties, conversion rules

## Tools
see-sweep.py - run FIRST: in-check reply list; GRAB-FORK scan flags my captures that die to his CHECK+hit.
recapture-scan.py - flags his recaptures that attack my queen.
escape-sweep.py - unattacked retreats for attacked pieces.
pawn-destination-sweep.py - his pawn/KNIGHT jump hits on my pieces.
kick-escape-sweep.py - pinned pieces, pawn kicks' escapes.
mate-net-scan.py - mate nets and my mate-in-1.
piece-map.py - RUN FIRST: to-move, king square, full piece map, material.
material-sweep.py - W/B totals + units by square; before ANY +/level claim.
safe-keepers.py - ranks legal moves by kept material; top 3 + AVOIDs.
repetition-count.py - shape-occurrence count from the move list: at +edge a 2nd occurrence = fire a lever, at -edge = steer into the third occurrence.
