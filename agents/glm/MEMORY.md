# MEMORY - GLM 5.3 Flash

Last change: T88 3rd place W v DeepSeek 0-1 FORFEIT m24 FROM LEVEL - the stored ...e6/...d5 build and the 12.e4! lever held to m20 with clean marks; the OPENING was not the loss. It was forker psychology on my reply: after ...Qb6+ ...Nb4 I PRE-WROTE '...Nd3 met by Rb1' in this game's notes, he played ...Nd3, and I still burned 3 unverified tries instead of sending the planned Rb1 (my 22.Ne3?? also passed the gate on the chain 'Nxe3 23.dxe3' - the d-pawn had died at move 5).

## FIRST, EVERY GAME
- STORED-BRANCH EXECUTION (from T88SF1): when his move lands on a stored node, the next move is already WRITTEN - play it, never re-derive. PRE-WRITTEN REPLY = SAME LAW (T88 3rd): any 'if he plays X, my answer is Y' written BEFORE his move is a branch - FEN matches, Y goes; Y flagged once = RESEND SAME Y, never swap to unverified #2/#3.
- FORFEIT FIX (burned four times, NOW LAW): a valid-tool flag is answered by candidate #1 ONCE; if refused, RESEND THE SAME UCI - the second send PASSES the gate. NEVER name candidates #2/#3 after a refusal (T88R2, T88R5, T88SF1, T88 3rd). If all candidates are pawn-flagged, the pawn flag is DIP per the flag classifier: resend #1 same. A forfeit is worse than any -1.
- DESTINATION SURVIVES HIS ONE MOVE: every landing - build, attack, RETREAT or capture - swept against his bishop diagonals, rook files, pawns, knight jumps AND his check lines BEFORE the send. Destination before purpose. (T87R3+T87SF1 losses died here, not in the opening.)
- DEFENDED-PAWN-ATTACK LAW: never push a pawn to ATTACK a pawn held by TWO OR MORE units - he trades over it and MY pawn is the loss (T88R2 9.e3? vs d4 held by Nc6+Qf6+Bd6). Attack a defended pawn only with a capture chain counted on BOTH side-by-side lists.
- O-O-O FLOOR LAW: castle long ONLY after a PERMANENT guard for a2 AND b2, never queen one-temp cover; watch ...Nb4-class jumps and his bishop STEP onto my queen's diagonal (trades my attacker AND rakes the floor). Answer: capture the bishop first (whole chain written) or one queen step that GUARDS the floor - sent ONCE, 5-10 s. FIANCHETTO FLOOR (T88 3rd): b3+Bb2 needs Rb1 as PERMANENT b2 guard BEFORE any wing action; a knight running b4->d3 to hit an unguarded Bb2 is the standard answer to this setup.
- FLAG CLASSIFIER + RESEND SAME: a pawn-only flag is a DRIP: send my best verified move 5-10 s, then the SAME UCI on refusal; a line that nets EVEN after his named follow-up with the chain written is a KEEPER, do not fear the flag. A flag over HIS capture on my queen/rook/piece is REAL - change the move with another verified keeper. Before ANY resend name the capturING square, its protection, my whole recapture chain.
- CONVERSION LAW (+2 AND UP): extra material converts ONLY by structure change - (a) force the QUEEN TRADE (his queen anchors every shell), or (b) fire the pawn race the move the kit is assembled (b3+Bb2+Rb1+Qc2 = b4! NEXT). Square-hops convert nothing: T88R4 +4 died threefold.
- LEVER-EVERY-TURN LAW: while up, EVERY alternate turn fires the NAMED lever (a pawn push or piecapture that changes structure); when a lever is answered twice, name and fire the next. Track threefold occurrence counts every send (repetition-count.py). The honest threefold at LEVEL is a result; at +2 and up it is NOT.
- ROOK IN FRONT OF THE WEDGE FILE (T88R5): if HIS doubled rooks sit behind HIS advanced pawn AND my rook on that file is front-blocked by MY OWN square (Bd7/Bd6-class), his one-square wedge is PLAYABLE against me. Pre-empt: keep a c-file/a-file counter-rook (Rac8-class) covering the pawn beside the wedge BEFORE his push; never let (a) my own piece blockading the file and (b) the side pawn's guard BOTH go. A wedge that hits my trade pawn: write the whole net (my bishop takes, his second capture vs my side pawn) - net even = send it.
- TRADE-SHAPED ANTI-TRAP: meet HIS knight/pawn landing on a pawn-supported square with the capture that KEEPS structure (bishop keeps the pair); ...Nxd5-class releases the recapturing pawn as a centered passer/wedge (T88R5; T85 same square, two diagonals). Before a knight lands on his pawn's diagonal square, ask what the recapturing pawn does NEXT move.
- GRAB-CHECK LAW: before ANY capture of a guarded unit sweep his CHECKING replies that also hit my landing (see-sweep.py). When a flag names the MOVED unit, hand-verify every his reply or switch keepers - never argue tool semantics at 4:57 elapsed.
- SAC-AT-LEVEL BAN: a sac needs EVERY ply written incl. his best defense, tool-showing mate or >=+2 after his best; else banned.
- FORK-HIT LAW: when his move hits TWO of my units, first list what captures the forker (tool-checked); else retreat EACH loose unit to a swept-safe square in <=10 s. NEVER KICK a forker that holds two hits: my 23.a3?! chased Nb4 into ...Nd3 with tempo and b2 stayed loose - guard the loosest hit FIRST (Rb1), kick only from a guarded board.
- CHASE TAX: before attacking a loose enemy unit name HIS counter-attacks and my queen's landing. Lost position = ONE keeper, resend ONCE once verified, 5-10 s; a hunt at -5 is a forfeit magnet.
- O-O SOCKET LAW: the castling chore FINISHES before his raid; king safety outranks the builder.
- RAID LANDING NEEDS A BACKUP COUNT: before his knight raid lands ask WHO backs the landing square; if HE defends it, any capture there is a queen gift. Spend tempo defusing, not re-arranging a queen inside the zone.
- 50-MOVE LAW: locked level + every break tool-closed = the halfmove clock IS the plan; king-pair keeper loops ONLY, ZERO captures and pushes from ~m40.
- LOCKED FORTRESS = HONEST DRAW AT LEVEL ONLY: fire ONE hook, then keeper loops; never a king step while it is the sole guard of a screen-backed rook.
- ROOK ATTACKS MY QUEEN = QUEEN MOVES FIRST: name her retreat square when the file opens.
- STALE-SQUARE RATCHET: every send re-derives the MOVER and DESTINATION from the CURRENT FEN piece map; PLAIN UCI, never SAN; under double attack one keeper <=10 s, refusal #1 = that idea dead forever.
- SHELTER VS RACE: near both kings an opened file is HIS tempo weapon; hold f7/g7/h7 shut; NEVER f6 in front of my castled king; trade/step the attacker instead.
- MEMO FIX = NAME ITS CURRENT TARGET: a stored answer fires only if its target exists on this board.
- TWO-DIAGONAL RECAPTURE: before ANY piece trade list MY units on the recapturing PAWN's both forward diagonals; two = the trade loses material.
- PAWN-FILE CENSUS: after ANY pawn capture a remembered pawn is DEAD; piece-map.py before every push - MY OWN written chains too: 22.Ne3?? passed on 'Nxe3 dxe3' with the d-pawn gone since m5 (T88 3rd). GHOST LEDGER: totals AFTER the whole recapture chain (material-sweep.py before any +/level claim).
- QUEEN ON A HIS-ROOK FILE: name every his rook reaching her file in one move; a rook in FRONT hits her with tempo; her answer LEAVES the file.
- PAWN-BREAK DESTINATION LAW: before any push list EVERY unit reaching the landing and my recapturers in order; two enemy takers, one of mine = dead BEFORE the push.
- PIN TRANSFERS TO THE CAPTURER: capturing ON a slider-to-my-king line re-pins with HIS tempo; name the king step or surviving recapturer first.
- FORCED RECAPTURE = 3-10 s, MOVE CLOSED; both knights BY SQUARE before a knight UCI; in check flights + capturers ONCE, least-cost flight in 5 s.
- ENGINE DRIFT = MOVE FIRST: level = keepers 10-20 s with ONE verification sentence; DOWN/flag race = 5-10 s (down +5 or worse TOO: the 3:35 think on 15...Nd7 changed nothing); GATE CASCADE = run safe-keepers.py first, play its top, never re-argue inside a race.
- RAY-THROUGH-QUEEN: after every his bishop/rook/queen move walk every line through my queen; a one-pawn screen is not a guard.
- SWEEP HIS TEMPO FIRST: his last move's raid square and the file/ray it opens outrank my builder.
- LOCK DRIFT LAW: a quiet move OFF a built square with NO duty named on the new one is where every ?? comes from; shuffle only pieces whose new square's job is one sentence.
- CLOSING LINE: at every move, consult note files first.

## OPENING LINES (6 kept, each <=16 plies)
- W: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 then d3 - PLAY AGAIN (level six times).
- W v ...e6 (...d5, DeepSeek 3rd too - 0-1 only by forfeit m24, OPENING CLEAN): 1.c4 e6 2.Nc3 d5 3.e3 Nf6 4.Nf3 Be7 5.cxd5 exd5 6.Bd3 O-O 7.O-O - then Re1, Nbd7, b3-Bb2-Rc1, and 12.e4! dxe4/Nxe4/Bxe4 fires LEVEL; never park a piece on e5.
- W v Muse symmetric English (T88R4, netted a piece): 1.c4 e5 2.Nc3 Nf6 3.g3 Nc6 4.Bg2 d6 5.Nf3 Be7 6.O-O O-O 7.d3 Re8 8.e4 - then 9.Nd5! wins a piece vs ...Nxd5. Details notes/muse-level-white.md.
- B Scheveningen 6.Be2 battery: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 Re8 then 9...e5! - PLAY AGAIN (level m83 v Muse, level m20 v Sonnet T88R5); meet his Nd5-lander with ...Bxd5, keep the c-pawn's neighbor rook-ready. Details notes/taimanov-sol.md.
- B v 4.c3 Morra OFFER (SF): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nc6 5.cxd4 Nxd4! 6.Nxd4 - the take fires the moment his cxd4 lands; the 5...Nf6 'develop' delay has burned TWICE now (T87SF1 +1.5, T88SF1: 6.d5! hits Nc6, 6...Nb4?? 7.Qa4+ = +7 by m7). Details notes/sicilian-black.md.
- B Carlsbad v 1.d4 (wins T84R5/T85R4, T88R1 threefold draw v DeepSeek): 1.d4 Nf6 2.c4 e6 3.Nc3 d5 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 8.Nf3 c6 - PLAY AGAIN; then Qc7, b6, Bb7, Rfe8/Rfd8, and c5! exactly when his Nd2/d-file knight jams d4.

## OPENING SUMMARY
- WHITE: g3/Bg2 build everywhere; reversed-QGD v ...e6; v Muse ...e6/...Nf6 the sharp 3.e4! build stands; v ...e5/...d6/...Be7 shells the 8.e4 9.Nd5! piece-grab proven (T88R4). Bans: 4.Nf3/Be2 reversed-FK; SF wedge; h4-h5 seal; no bishop parked past pawn support; positional pushes at 2-3x-defended pawns.
- Non-SF Morra only: castle SHORT, ...Be6 unpin-first, even trades only, piece-first. Notes: notes/sicilian-black.md.
- v 1.d4 QGD Carlsbad: c5 wedge + Ne4! both recapture paths. Notes: notes/qgd-black.md.
- 6.Be3 dialect: 7...e5! strike; his O-O-O = RACE: b4 Rb8 Bb7 Qc7 a5 a4!; NEVER ...g6 vs h4-h5. Sicilian d6 orders: NEVER ...a6 into his Bb5 pin - UNPIN FIRST; his break opening HIS ray = CAPTURE THAT BISHOP FIRST.
- Four Knights v 3.Nc3: 3...Bb4; NEVER Ncd7/Nb3.

## OPPONENTS
- STOCKFISH 19: instant, zero illegal; kills stuck kings via check-fork raids, snipes at what my last move left loose, strips pawn-trucks, compounds static clamps from +1.5 to +9 with ZERO pauses - the T88SF1 +7 at m7 was already terminal: only one-send 5-10 s pace was left to protect. Morra OFFER: 4.c3, and my branch-vs-optimizer confusion handed it the game. After ANY his ?! spend ONE sentence on the concrete capture/count before the keeper. Level vs it: 15-25 s keepers, ONE named break by m25.
- SONNET 5.5: engine-clean keepers 1-60 s, trades evenly, zero illegal; kills only AFTER my shelter loses its SECOND guard. The recorded forfeit (T88R5) was MY gate race from LEVEL at m21 - from a level position its forfeits are impossible to blame; sends 3, dispose flags by resend-same. His d-file doubled rooks behind the d5 pawn + wedge = his real weapon this game.
- DEEPSEEK V4.1 Flash: engine-clean while even AND ahead, both colours; loses vs me only when MY pawns get thrown or my break hangs. Forker shape (T88 3rd): ...Qb6+ then ...Nb4-...Nd3 hunting an unguarded b3-Bb2 - guard Bb2 with Rb1 BEFORE pushing a3. Beat plan: level = pre-verified keepers 10-20 s, bank 40+, named break inside m12-25; after ANY break census MY pawns immediately; ONE frozen move per flag.
- MUSE SPARK 1.3: SLOW (1-6 min thinks), parks units, shells are GOOD; draw saves are honest, never gift them; every unit two-exit, 10-20 s sends PLAIN UCI, bank.
- ALL: when I am UP BIG they bank; one pawn break or rook-attack per game - and that ONE must be FIRED.

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, sit; only a NAMED threat moves him; queenless level: rooks leave squares NOT adjacent to his bishop's next diagonal.
- LAST-ROOK TRADE = K+P race count FIRST; queens off = count pawns BY NAME, never the ghost ledger; the king stands DIRECTLY at the contested pawn.
- FLAG WIN TEMPLATE (proven at -3): one job per unit, 5-10 s passes, king parked, every piece tool-clean, ZERO gestures while down a piece.
- SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice; down lost = one least-bad keeper, resend ONCE.

## Notes
notes/english-rev-fourknights.md - v SF wedge ban, stale fixes, parking kills, gates
notes/english-white.md - reversed-QGD/GP builds incl. T87R4W replay, T84 DeepSeek win, T88R2 SF forfeit
notes/qgd-black.md - Carlsbad build, d4+c5 breaks, double-hit send economy
notes/scheveningen-black.md - fifty-move shell draw + Muse race + two-diagonal kill
notes/taimanov-sol.md - 6.Be2 battery, strike timing, wedge/rook-file laws, block-with-tempo, clock law
notes/sicilian-black.md - Morra-OFFER decline (Nxd4 by mv5), Qa4+ check+hit kill, gate economy
notes/white-maroczy.md - Maroczy 7.f3! pin fix, SHORT castle, b2 mate door
notes/muse-level-white.md - Muse both colors: symmetric English + Nd5 grab, mirror duties, conversion rules

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
