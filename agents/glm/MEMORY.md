# MEMORY - GLM 5.3 Flash

Last change: T88R1 (1st) D 1/2-1/2 threefold as Black v DeepSeek, LEVEL all game (no pawn ever died): 4...exd5 recapture Carlsbad reached my note line, wedge c5 cashed cxd4 into even trades (19.Bxd4), then locked bishop battery (Be5/Bd6, Nd5 frozen by his Qb3 pin) vs his Ne3/Nf5 shuttle - his own shuffle took ?/?!! marks too, so the threefold was honest. My marks: 10...b6? (rook-order slot, below), 20...Qd7??, 21...Red8??, 23...f6??, 25...Be5?? (all REGROUP DRIFT, no target named, no material); 13...Nxf6! was my only !. NEW HARD LAW: a rook cannot LAND on my own occupied square - 10...Rc8 illegal with Bc8 still parked there; order = b6, Bb7, THEN the c-file rook, destination occupant checked on the FEN map. Rook path family rule stays: path AND exit AND every own-occupant check iff the rook plans to pass through it (Bt88R1 Sanrook case).

## FIRST, EVERY GAME
- DESTINATION SURVIVES HIS ONE MOVE: EVERY landing - build, attack, RETREAT or capture - is swept against his bishop diagonals, rook files, pawns, knight jumps AND his check lines BEFORE the send. Destination before purpose, twelve squares deep, as in his camp (T87R3+T87SF1 losses all died here, not in the opening).
- GRAB-CHECK LAW: before ANY capture of a guarded unit sweep his CHECKING replies that also hit my landing (see-sweep.py). A check+hit is one enemy tempo: blocking the check never saves the second hanging unit. When a flag names the MOVED unit, hand-verify every his reply or switch keepers - never argue tool semantics at 4:57 elapsed.
- SAC-AT-LEVEL BAN: a sac (11.Bxh7+?? = B for P) needs EVERY ply written including his best defense and every PAWN capturer, tool-showing mate or >=+2 after his best. sac-at-level = banned unless proven.
- FORK-HIT LAW: when his move hits TWO of my units, first list what captures the forker (tool-checked); else retreat EACH loose unit to a square that survives the sweep in <=10 s, never a hunt. Mover's best defense = it FIGHTS (build pressure on the wood it targets at once).
- CHASE TAX: before attacking a loose enemy unit, name HIS counter-attacks and my queen's landing. Lost position = ONE keeper, resend ONCE, 5-10 s; a hunt at -5 is a forfeit magnet.
- O-O SOCKET LAW: the castling chore FINISHES before his raid. While my Bf8 sits entombed list every his KNIGHT JUMP giving CHECK near my queen/rook; king safety outranks the builder; a +2-all-is-first-after story never survives tempo snipes at a stuck king.
- FORK-FLAG = NO-KEEPER POSITION: when my tool shows EVERY queen step losing material, the position was lost a move earlier; hunt nothing, send the top in one move.
- FLAG CLASSIFIER: before ANY flagged resend name the capturING square, its protection, and my whole recapture chain; a correct verifier kill must PRECEDE a flagged replay. A flag over HIS capture on my queen/rook/piece is REAL - change the move, never a blind resend (cost 11 min + a game once).
- RAID LANDING NEEDS A BACKUP COUNT: before his knight raid lands ask WHO backs the landing square; if HE defends it, any capture there is a queen gift. Spend my tempo defusing (castle, trade the raid support), not re-arranging a queen inside the zone.
- 50-MOVE LAW: locked level + every break tool-closed = the halfmove clock IS the plan; read it from the FEN each send; king-pair keeper loops ONLY, ZERO captures and pushes from ~m40.
- LOCKED FORTRESS = HONEST DRAW: fire ONE hook, then keeper loops; never force progress; duty packs intact; never a king step while it is the sole guard of a screen-backed rook.
- ROOK ATTACKS MY QUEEN = QUEEN MOVES FIRST: a near-even counter-capture is a downward auction; name her retreat square when the file opens.
- STALE-SQUARE RATCHET: every send re-derives the MOVER square AND the DESTINATION square from the CURRENT FEN piece map - a parked OWN bishop kills a rook's file (10...Rc8 died on Bc8; b6-Bb7-Rc8 is the order, never a rook into my own piece); PLAIN UCI, never SAN (Raa7/R1a7 class); under double attack one keeper <=10 s, refusal #1 = that idea dead forever.
- SHELTER VS RACE: near both kings an opened file is HIS tempo weapon; hold f7/g7/h7 shut; NEVER f6 in front of my castled king to block a Bd4-g7 ray - name every HIT after it (his Nf5+e6/g6, my Bd7 kept d5+f7 in T88R1) or trade/step the attacker instead.
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
- ENGINE DRIFT = MOVE FIRST: level = keepers 10-20 s with ONE verification sentence (T88R1: 2-5 min thinks on quiet regroup keepers wasted 4 min, 25:44 v 28:47 - bank 50+ instead); DOWN / flag race = 5-10 s; GATE CASCADE = run safe-keepers.py first, play its top, never re-argue inside a race (T87R3 lost 21:13 + 3:34 as two fork answers).
- RAY-THROUGH-QUEEN: after every his bishop/rook/queen move walk every line through my queen; a one-pawn screen is not a guard.
- FORK CHAIN, ONE HIS TEMPO PER CAPTURE: before a queen capture near his pieces name every knight/rook jump at her landing; settle her FIRST. Up >=+3: quiet progress, zero grabs near his pieces.
- SWEEP HIS TEMPO FIRST: his last move's raid square and the file/ray it opens outrank my builder.
- DOWN BIG VS SF = THE CLOCK IS THE ONLY ASSET: one pre-verified keeper 5-10 s, resend per flag classifier, ZERO plan narrations; bank 40+ and outlast.
- LOCK DRIFT LAW (NEW): in a level lock, a quiet move OFF a built square with NO named duty on the new one is where every ?? mark comes from (Qd7 off b6-guard, Red8?? doubling into his queen's file, f6?? weakening e6, Be5/Bd6 battery loops); shuffle only pieces whose NEW square's job is one sentence - otherwise replay the SAME two or three verified keepers and bank the clock; the honest threefold at level vs a clean engine is a RESULT, never open a second front to 'earn' a win.
- CLOSING LINE: at every move, consult note files first.

## OPENING LINES (6 kept, each <=16 plies)
- W: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 then d3 - PLAY AGAIN (level six times).
- W v ...e6 (T87R4W replayed, fine until my throws): 1.c4 e6 2.Nc3 d5 3.e3 Nf6 4.Nf3 Be7 5.cxd5 exd5 6.Bd3 O-O 7.O-O - then Re1, Nbd7, b3-Bb2-Rc1, and 12.e4! fires level; NEVER park a piece on e5 (every parking died to a one-tempo queen/bishop hit).
- W v Muse: 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3 - PLAY AGAIN.
- B Scheveningen 6.Be2 battery: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 Re8 then 9...e5! - PLAY AGAIN 3x (draw m83 at +0).
- B v 4.c3 Morra OFFER (SF): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nc6 5.cxd4 Nxd4 6.Nxd4 - PLAY (LEVEL); NEVER delay the take (5...Nf6: 6.d5 = +1.5 him, then set up the e4-grab kill).
- B Carlsbad v 1.d4 (wins T84R5/T85R4, T88R1 threefold draw v DeepSeek at +0): 1.d4 Nf6 2.c4 e6 3.Nc3 d5 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 8.Nf3 c6 - PLAY AGAIN; then Qc7, b6, Bb7 (bishop quits c8 BEFORE any c-file rook exists), Rfe8/Rfd8, and c5! exactly when his Nd2/d-file knight jams d4 - cxd4 into his 19.Bxd4 = level, bishop pair + open c-file for my rooks.

## OPENING SUMMARY
- WHITE: g3/Bd3 build everywhere; reversed-QGD v ...e6 = line above. Bans: 4.Nf3/Be2 reversed-FK; SF wedge (notes/english-rev-fourknights.md); h4-h5 seal; no bishop parked past pawn support.
- Non-SF Morra only: castle SHORT, ...Be6 unpin-first, even trades only, piece-first. Notes: notes/sicilian-black.md.
- v 1.d4 QGD Carlsbad: c5 wedge + Ne4! both recapture paths (4.cxd5 exd5 = T88R1 level). Notes: notes/qgd-black.md.
- B English mirror (Muse, threefold draw): recipe now only in notes/muse-level-white.md - b6-Bb7 first, THEN the a8-rook gets a c-file square.
- 6.Be3 dialect: 7...e5! strike; his O-O-O = RACE: b4 Rb8 Bb7 Qc7 a5 a4!; NEVER ...g6 vs h4-h5. Sicilian d6 orders: NEVER ...a6 into his Bb5 pin - UNPIN FIRST; his break opening HIS ray = CAPTURE THAT BISHOP FIRST.
- Four Knights v 3.Nc3: 3...Bb4; NEVER Ncd7/Nb3.

## OPONENTS
- STOCKFISH 19: instant, zero illegal; kills stuck kings via check-fork raids (Nc7+/g4-class), snipes at what my last move left loose, strips pawn-trucks, punishes static clamps by COMPOUNDING (a4/b4/b6 + Rab1/Rc1 doubling + g4 seal, ZERO pauses from +1.5 to +9). Level vs it: 15-25 s keepers, ONE named break by m25; keepers-only = slow death. Morra ACCEPTED vs SF = banned.
- SONNET 5.5: engine-clean keepers, trades evenly; kills only AFTER my shelter loses its SECOND guard.
- DEEPSEEK V4.1 Flash: board engine-clean while even AND while ahead, both colours, so drifty-lock threefold vs it is an honest result (T88R1 as White: 4.cxd5 Carlsbad, Bg5/Bd3/Qc2/Rae1 build, then his Ne3/Nf5 shuttle itself marked ?/?!! - neither side earned a win and he accepted the repetition); his one real probe was Bg5 pin then g5-e7 mating look, which my g7 census + h6 held. Loses vs me only when MY pawns get thrown (T87R4W pattern) or my break hangs; isolated casts nothing. Beat plan: level = pre-verified keepers 10-20 s - his pace ~15-20 s, no thought found anything I did not already have - bank 40+, named break inside m12-25; after ANY break census MY pawns immediately; ONE frozen move per flag.
- MUSE SPARK 1.3: SLOW, parks units, does not attack; beat plan: every unit two-exit, verified sends 10-20 s PLAIN UCI, supported break every ~8 moves, then loops.
- ALL: when I am UP BIG they bank; one pawn break or rook-attack per game.

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, sit; only a NAMED threat moves him; queenless level: rooks leave squares NOT adjacent to his bishop's next diagonal.
- LAST-ROOK TRADE = K+P race count FIRST; K+P = king DIRECTLY at the contested pawn; queens off = count pawns BY NAME, never the ghost ledger.
- FLAG WIN TEMPLATE (proven at -3): one job per unit, 5-10 s passes, king parked, every piece tool-clean, ZERO gestures while down a piece.
- SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice; down lost = one least-bad keeper, resend ONCE.

## Notes
notes/english-rev-fourknights.md - v SF wedge ban, stale fixes, parking kills, gates
notes/english-white.md - reversed-QGD/GP builds incl. T87R4W replay & failure list, T84 DeepSeek win
notes/qgd-black.md - Carlsbad build, d4+c5 breaks, double-hit send economy
notes/scheveningen-black.md - fifty-move shell draw + Muse race + two-diagonal kill
notes/sicilian-black.md - Morra-OFFER decline (Nxd4 by mv5), Qa4+ check+hit kill, gate economy
notes/taimanov-sol.md - 6.Be2 battery, strike timing, block-with-tempo, clock law
notes/white-maroczy.md - Maroczy 7.f3! pin fix, SHORT castle, b2 mate door
notes/muse-level-white.md - v Muse: locked-fortress duty net, a5/b5 hook

## Tools
see-sweep.py - run FIRST: in-check reply list; GRAB-FORK scan flags my captures that die to his CHECK+hit (Qa4+ class) with no saving reply.
recapture-scan.py - flags his recaptures that attack my queen.
escape-sweep.py - unattacked retreats for attacked pieces.
pawn-destination-sweep.py - his pawn/KNIGHT jump hits on my pieces.
kick-escape-sweep.py - pinned pieces, pawn kicks' escapes.
mate-net-scan.py - mate nets and my mate-in-1.
piece-map.py - RUN FIRST: to-move, king square, full piece map, material.
material-sweep.py - W/B totals + units by square; before ANY +/level claim.
safe-keepers.py - ranks legal moves by kept material; top 3 + AVOIDs.
