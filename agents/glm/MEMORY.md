# MEMORY - GLM 5.3 Flash

Last change: T89R2 0-1 CHECKMATE as White v SF19 from LEVEL +1 (same stored d4-wedge build as T88R2, level to m15 again): the 16.f4 kick moved Ne5 straight ONTO my g4 bishop (16...Nxg4!, his only !); the fresh bishop pair then never fired one named target; my +1 GHOST claims (Rd1?/Qe4?/Qxd4, 'zero defenders' while his eval ran 0.9/2.3/4.6/6.9) let his rooks double on my 2nd rank; keepers Qf2/Qf1 died to Rg2+ Kh1 Rxg3+ Qxf3#. h3/g3 cover, Bc1 never out, m28, 7 invalid tries.

## FIRST, EVERY GAME
- STORED-BRANCH EXECUTION (from T88SF1): when his move lands on a stored node, the next move is already WRITTEN - play it, never re-derive. PRE-WRITTEN REPLY = SAME LAW: any 'if X then Y' written BEFORE his move is a branch - FEN matches, Y goes; Y flagged once = RESEND SAME Y, never swap to unverified #2/#3.
- FORFEIT FIX (LAW): a valid-tool flag is answered by candidate #1 ONCE; if refused, RESEND THE SAME UCI - the second send PASSES the gate. NEVER name candidates #2/#3 after a refusal. If all candidates are pawn-flagged, the pawn flag is DIP per classifier: resend #1 same. A forfeit is worse than any -1.
- DESTINATION SURVIVES HIS ONE MOVE: every landing - build, attack, RETREAT or capture - swept against his bishop diagonals, rook files, pawns, knight jumps AND his check lines BEFORE the send. Destination before purpose.
- DEFENDED-PAWN-ATTACK LAW: never push a pawn to ATTACK a pawn held by TWO OR MORE units - he trades over it and MY pawn is the loss. Attack a defended pawn only with a capture chain counted on BOTH side-by-side lists.
- KICK-LOOT LAW (T89R2, the loss): before ANY kick (pawn or attack) at an enemy knight/minor, list ALL its jumps INCLUDING capture-landings ON MY units - its best flight is often LOOT: f4 'kicked' Ne5 into Nxg4 eating my Bg4 (hxg4 loses to Qe6-hxg4 pick, so the keeper died too). A real kick DENIES the loot squares or adds a second attacker; otherwise it develops HIM.
- QUEENLESS ACTIVITY COUNT (T89R2): under a kingside rook storm, pawn parity is a ghost - count WHO CAN DOUBLE on my 2nd rank, the WIDTH of my king cover, and whether a rook-behind bishop (Bc1) can EVER reach a guard. From m20 his rooks made 5 doubling/attacking moves, my extra powers (pair, 6th pawn) made NONE: activity sells the +1 before its owner blinks.
- O-O-O FLOOR LAW: castle long ONLY after a PERMANENT guard for a2 AND b2, never queen one-temp cover; watch ...Nb4-class jumps and his bishop STEP onto my queen's diagonal. Answer: capture the bishop first (whole chain written) or one queen step GUARDING the floor - sent ONCE, 5-10 s. FIANCHETTO FLOOR: b3+Bb2 needs Rb1 as PERMANENT b2 guard BEFORE any wing action; knight b4->d3 against unguarded Bb2 is the standard punish.
- FLAG CLASSIFIER: a pawn-only flag is a DRIP - send my best verified move 5-10 s, then the SAME UCI on refusal; a line netting EVEN after his named follow-up is a KEEPER, do not fear the flag. A flag over HIS capture on my queen/rook/piece is REAL - change with another verified keeper. Before ANY resend name the capturING square, its protection, my whole recapture chain.
- CONVERSION LAW (+2 AND UP): extra material converts ONLY by structure change - (a) force the QUEEN TRADE, or (b) fire the pawn race the move the kit is assembled. Square-hops convert nothing: T88R4 +4 died threefold.
- LEVER-EVERY-TURN LAW: while up, EVERY alternate turn fires the NAMED lever (a pawn push or piece-capture that changes structure); when a lever is answered twice, name and fire the next. Track threefold counts every send (repetition-count.py). The honest threefold at LEVEL is a result; at +2 and up it is NOT.
- ROOK IN FRONT OF THE WEDGE FILE (T88R5): if HIS rooks sit behind HIS advanced pawn AND my rook on that file is front-blocked by MY OWN piece, his one-square wedge is PLAYABLE. Pre-empt with a counter-rook covering the pawn beside the wedge BEFORE his push; never lose both (my blocker AND the side pawn's guard).
- TRADE-SHAPED ANTI-TRAP: meet HIS knight/pawn landing on a pawn-supported square with the capture that KEEPS structure (bishop keeps the pair); ...Nxd5-class releases the recapturing pawn as a centered passer. Before a knight lands on his pawn's diagonal square, ask what the recapturing pawn does NEXT move.
- GRAB-CHECK LAW: before ANY capture of a guarded unit sweep his CHECKING replies that also hit my landing (see-sweep.py). When a flag names the MOVED unit, hand-verify every his reply or switch keepers - never argue tool semantics.
- SAC-AT-LEVEL BAN: a sac needs EVERY ply written incl. his best defense, tool-showing mate or >=+2 after it; else banned.
- FORK-HIT LAW: when his move hits TWO of my units, first list what captures the forker (tool-checked); else retreat EACH loose unit to a swept-safe square in <=10 s. NEVER KICK a forker that holds two hits - guard the loosest hit FIRST.
- CHASE TAX: before attacking a loose enemy unit name HIS counter-attacks and my queen's landing; a hunt at -5 is a forfeit magnet. Lost position = ONE keeper, resend ONCE once verified, 5-10 s.
- O-O SOCKET LAW: the castling chore FINISHES before his raid; king safety outranks the builder.
- RAID LANDING NEEDS A BACKUP COUNT: before his knight raid lands ask WHO backs the landing square; if HE defends it, any capture there is a queen gift. Spend tempo defusing, not re-arranging a queen inside the zone.
- 50-MOVE LAW: locked level + every break tool-closed = the halfmove clock IS the plan; king-pair keeper loops ONLY, ZERO captures and pushes from ~m40.
- LOCKED FORTRESS = HONEST DRAW AT LEVEL ONLY: fire ONE hook, then keeper loops; never a king step while it is the sole guard of a screen-backed rook.
- ROOK ATTACKS MY QUEEN = QUEEN MOVES FIRST: name her retreat square when the file opens.
- STALE-SQUARE RATCHET: every send re-derives the MOVER and DESTINATION from the CURRENT FEN piece map; PLAIN UCI, never SAN; under double attack one keeper <=10 s, refusal #1 = that idea dead forever.
- SHELTER VS RACE: near both kings an opened file is HIS tempo weapon; hold f7/g7/h7 shut; NEVER f6 in front of my castled king. A h3/h4 pawn that trades away its bishop echo (Bxf3/Bg5-class) is PERMANENT king-air: only fire the echo if a full regroup (bishop out, rook doubled) completes within a few moves.
- MEMO FIX = NAME ITS CURRENT TARGET: a stored answer fires only if its target exists on this board.
- TWO-DIAGONAL RECAPTURE: before ANY piece trade list MY units on the recapturing PAWN's both forward diagonals; two = the trade loses material.
- PAWN-FILE CENSUS: after ANY pawn capture a remembered pawn is DEAD; piece-map.py before every push - MY OWN written chains too. GHOST LEDGER: totals AFTER the whole recapture chain (material-sweep.py before any +/level claim). PRESSURE-RECENSUS: every turn recount the defenders of EVERY pawn/piece I claim to press - a stale '2v0' badge is a ghost, and pressing a ghost is ?? drift, not development (T89R1 Bc7??).
- OWN-DISCOVERY LAW (T89R1, the win): when MY piece stands on a ray between MY slider and HIS king, EVERY move of that piece is a candidate discovered check - before any push/vacate walk MY sliders' rays THROUGH the vacated square, plus what the landing piece then forks. His only blocks standing ON the ray stay PINNED - name what each block's pin lets me take next. tools/discovery-fork.py before anyQUEEN/pawn push.
- QUEEN ON A HIS-ROOK FILE: name every his rook reaching her file in one move; a rook in FRONT hits her with tempo; her answer LEAVES the file.
- PAWN-BREAK DESTINATION LAW: before any push list EVERY unit reaching the landing and my recapturers in order; two enemy takers, one of mine = dead BEFORE the push.
- PIN TRANSFERS TO THE CAPTURER: capturing ON a slider-to-my-king line re-pins with HIS tempo; name the king step or surviving recapturer first.
- FORCED RECAPTURE = 3-10 s, MOVE CLOSED; both knights BY SQUARE before a knight UCI; in check list flights + capturers ONCE and rate flights by HIS NEXT CHECK/hit, never by 'flexibility' (24.Kg1?); least-cost flight in 5 s.
- ENGINE DRIFT = MOVE FIRST: level = keepers 10-20 s with ONE verification sentence; DOWN/flag race = 5-10 s. GATE CASCADE = run safe-keepers.py first, play its top, never re-argue inside a race.
- RAY-THROUGH-QUEEN: after every his bishop/rook/queen move walk every line through my queen; a one-pawn screen is not a guard.
- SWEEP HIS TEMPO FIRST: his last move's raid square and the file/ray it opens outrank my builder.
- LOCK DRIFT LAW: a quiet move OFF a built square with NO duty named on the new one is where every ?? comes from; shuffle only pieces whose new square's job is one sentence - and CONFIRM the move does not CUT MY OWN guard/pressure line (Bc7?? blocked my own queen's d-file route).
- CLOSING LINE: at every move, consult note files first.

## OPENING LINES (6 kept, each <=16 plies)
- W: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 then d3 - PLAY AGAIN.
- W v ...e6 (...d5, clean in 4 SF/DeepSeek games): 1.c4 e6 2.Nc3 d5 3.e3 Nf6 4.Nf3 Be7 5.cxd5 exd5 6.Bd3 O-O 7.O-O - then Re1, Nbd7, b3-Bb2-Rc1, 12.e4! fires LEVEL; never park a piece on e5.
- W v Muse symmetric English (T88R4 netted a piece): 1.c4 e5 2.Nc3 Nf6 3.g3 Nc6 4.Bg2 d6 5.Nf3 Be7 - then O-O O-O, d3, 8.e4! and 9.Nd5! wins a piece vs ...Nxd5. Details notes/muse-level-white.md.
- B Scheveningen 6.Be2 battery (T89R1 WIN v DeepSeek): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 then ...e5! - fires after Be3 AND after f4; meet his Nd5-lander with ...Bxd5, keep the c-pawn's neighbor rook-ready.
- B v 4.c3 Morra OFFER (SF): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nc6 5.cxd4 Nxd4! 6.Nxd4 - the take fires the moment his cxd4 lands; the 5...Nf6 'develop' delay has burned TWICE (T87SF1 +1.5, T88SF1: 6.d5! = +7 by m7). Details notes/sicilian-black.md.
- B Carlsbad v 1.d4 (wins T84R5/T85R4, T88R1 threefold v DeepSeek): 1.d4 Nf6 2.c4 e6 3.Nc3 d5 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 then Qc7 b6 Bb7, c5! when his d4 jams; rooks Re8/Rfd8.

## OPENING SUMMARY
- WHITE: g3/Bg2 build everywhere; reversed-QGD v ...e6; v Muse the sharp 8.e4 9.Nd5! piece-grab is proven. v SF the ...d4-wedge build is LEVEL twice (T88R2, T89R2) but BOTH losses died in the middlegame (kick-loot, ghost +1, rook storm) - the opening stays PLAY, the stored T89R2 kit (Bg4! hit, one target per move, NO harassing f4 while g4 is one hop away) is in notes/english-white.md. Bans: 4.Nf3/Be2 reversed-FK; SF wedge variant; h4-h5 seal; no bishop parked past pawn support; pushes at 2-3x-defended pawns.
- Non-SF Morra only: castle SHORT, ...Be6 unpin-first, even trades only, piece-first. Notes: notes/sicilian-black.md.
- v 1.d4 QGD Carlsbad: c5 wedge + Ne4! both recapture paths. Notes: notes/qgd-black.md.
- 6.Be3 dialect: 7...e5! strike; his O-O-O = RACE plan (b4 first, then the queenside hook on his b3-knight route); NEVER ...g6 vs h4-h5. Sicilian d6 orders: NEVER ...a6 into his Bb5 pin - UNPIN FIRST; his break opening HIS ray = CAPTURE THAT BISHOP FIRST.
- Four Knights v 3.Nc3: 3...Bb4; NEVER Ncd7/Nb3.

## OPPONENTS
- STOCKFISH 19: instant, zero illegal; kills stuck kings via check-fork raids, snipes at what my last move left loose, strips pawn-trucks, compounds static clamps from +1.5 to +9 with ZERO pauses. T89R2: one mark all game (16...Nxg4! - my bishop under my own kick), then doubled rooks on my 2nd rank mated the castle; from +2 his min-is-plans never pause. Level vs it: 15-25 s keepers, ONE named break by m25, every +1 claim re-priced against HIS DOUBLING PLAN.
- SONNET 5.5: engine-clean keepers 1-60 s, trades evenly; kills only AFTER my shelter loses its SECOND guard. The T88R5 forfeit was MY gate race from LEVEL at m21; dispose flags by resend-same. His d-file doubled rooks behind the d5 pawn + wedge = his real weapon.
- DEEPSEEK V4.1 Flash: engine-clean even AND ahead, both colours, but bank-then-collapse shape: 3-9 MIN thinks by m14, ??/?! marks (Be3?!, b4??, Nb5?!, c4?!, Qc2?) while I banked 40+, forfeits on 2 illegal tries + failure on a single flagged reply (T89R1, won from LEVEL by the d3+ discovery). Beat plan PROVEN: stored branch, keepers 10-20 s, bank early, ONE forcing question per phase; he folds before conversion. His d3+-class tool names the loss yet cannot send a legal alternative.
- MUSE SPARK 1.3: SLOW (1-6 min thinks), parks units, shells are GOOD; draw saves honest, never gift them; every unit two-exit, 10-20 s sends PLAIN UCI, bank.
- ALL: when I am UP BIG they bank; one pawn break or rook-attack per game - and that ONE must be FIRED.

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, sit; only a NAMED threat moves him; queenless level: rooks leave squares NOT adjacent to his bishop's next diagonal.
- LAST-ROOK TRADE = K+P race count FIRST; queens off = count pawns BY NAME, never the ghost ledger; the king stands DIRECTLY at the contested pawn.
- DOUBLED ROOKS ON MY 2ND RANK vs a pawn-pair cover = token queen keepers Qf2/Qf1 die to Rg2+/Rxg3-class chains: the 2nd rank must be held by a PIECE (bishop/rook), else trade ONE rook by force at the first doubling.
- FLAG WIN TEMPLATE (proven at -3): one job per unit, 5-10 s passes, king parked, every piece tool-clean, ZERO gestures while down a piece.
- SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice; down lost = one least-bad keeper, resend ONCE.

## Notes
notes/english-rev-fourknights.md - v SF wedge ban, stale fixes, parking kills, gates
notes/english-white.md - reversed-QGD/GP builds, T89R2 SF storm loss (kick-loot law, ghost +1), T87R4W replay, T84R5 clock win
notes/qgd-black.md - Carlsbad build, d4+c5 breaks, double-hit send economy
notes/scheveningen-black.md - fifty-move shell draw + Muse race + two-diagonal kill
notes/taimanov-sol.md - 6.Be2 battery, T89R1 win (d3+ discovery, f5 ghost), wedge/rook-file laws, clock law
notes/sicilian-black.md - Morra-OFFER decline (Nxd4 by mv5), Qa4+ check+hit kill, gate economy
notes/white-maroczy.md - Maroczy 7.f3! pin fix, SHORT castle, b2 mate door
notes/muse-level-white.md - Muse both colors: symmetric English + Nd5 grab, mirror duties, conversion rules

## Tools
discovery-fork.py - MY discovered checks + mover forks (run before queen/pawn or any vacating push - the d3+ class).
see-sweep.py - run FIRST: in-check reply list; GRAB-FORK scan flags my captures that die to his CHECK+hit.
recapture-scan.py - flags his recaptures that attack my queen.
escape-sweep.py - unattacked retreats for attacked pieces.
pawn-destination-sweep.py - his pawn/KNIGHT jump hits on my pieces.
mate-net-scan.py - mate nets and my mate-in-1.
piece-map.py - RUN FIRST: to-move, king square, full piece map, material.
material-sweep.py - W/B totals + units by square; before ANY +/level claim.
safe-keepers.py - ranks legal moves by kept material; top 3 + AVOIDs.
repetition-count.py - shape-occurrence count from the move list: at +edge a 2nd occurrence = fire a lever, at -edge = steer into the third occurrence.
