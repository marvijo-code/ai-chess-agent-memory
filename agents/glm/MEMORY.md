# MEMORY - GLM 5.3 Flash

Last change: T86R4 DRAW threefold m58 v Muse as Black (mirrored English) FROM LEVEL: every break tool-closed and both kings boxed - the draw WAS the result (one hook a5/b5, then keeper loops, 16 min banked v his 2). New laws: rebuild the piece map before ANY capture thesis (28...Qxb7?? ILLEGAL - no b7 bishop exists) and send PLAIN UCI, never SAN (ambiguous SAN = instant illegal try).

## FIRST, EVERY GAME
- LOCKED FORTRESS = THE HONEST DRAW (T86R4 v Muse): census says every pawn break tool-closed + both kings boxed = fire ONE hook (a5/b5-class with the rook ready behind it), then keeper loops reset the 50-move clock; never force progress. Duty packs never shift one member: the ray-blinding bishop (Bf6-v-Rg6, also d6's needed 2nd cover) and its rook backup R(move the same turn? NO) - d6 stays double-rook-guarded (Rd7/Rd8) so Rxd6 is always a rook-for-pawn suicide; NEVER a king step (g8-class) while that king is the sole guard of a screen-backed rook (Kf7 = e8's only guard).
- REFUSAL LIST EXPIRES PER-MOVE (T85 3rd, proven in T86): gated/AVOID calls never carry across QUIET moves. A refusal is a statement about ONE position; after ANY board change the list is blank. Before every send count sendable keepers >2; if not, the plain one-step retreat of the attacked unit IS the send (send once, resend SAME if flagged).
- ONE TRY PER MOVE AT LEVEL: pre-verify with material-sweep + safe-keepers, send ONCE, 10-20 s. A refusal naming ONLY a ~1-pawn loss in a level/borderline position is NOISE: RESEND THE SAME move once (it goes through). Cycling a third DIFFERENT flagged candidate forfeited T86R3 from a level board. After a MATERIAL gate (piece/rook/exchange/mate): a DIFFERENT legal keeper, one try.
- SHELTER VS RACE (T85 3rd): v his O-O-O h4-h5 build my ...g6?! was unneeded; holding f7/g7/h7 SHUT (no concession) plus queenside hooks outraced him, and gxh5 opened the h-file his Rf5 rebuilt on for the whole ending. In a queenless race every opened file near both kings is HIS tempo weapon.
- STALE-SQUARE RATCHET, BOTH MOVES (T85R5, T85SF2): after ANY hop, mine or his, the piece's old square is DEAD for the next plan; every send re-derives the mover's square from the FEN in one line: piece@sq -> UCI. My forfeit record is stale squares, overrides and memo-fixes, nothing else.
- MEMO FIX = NAME ITS CURRENT TARGET (T85R5): a stored answer (e.g. ...Nb4 -> Nxf6+) fires only if that target EXISTS on this board; write who occupies each square the fix touches before sending it.
- TWO-DIAGONAL RECAPTURE (T85 SF2): before ANY piece trade, list MY units standing on the recapturing PAWN's BOTH forward diagonals; two of mine = the trade loses material. ...Nxd5-class is dead unless both hit squares are free.
- FLAG-NET REPLY = ONE FEN CHAIN (T85 SF2 forfeit): when a referee/material flag names a lost unit, the position is a COUNT, not a puzzle: derive the reply chain from the CURRENT FEN, send ONCE at 10 s. No 1+ minute re-think inside a net, no variants, no third different move.
- WEDGE-CREEP LAW (T85R5): a static +0.5..1 v SF compounds every 3-4 keepers; at the FIRST +1 play the named unblock inside 10 moves.
- CHECK THAT 'TAKES A PIECE': name ALL guards of the target AND its live retreats that carry tempo; a defended minor near his king is NOT a win. Only zero-retreat pieces are grabs.
- BvB FORTRESS (proven v Sonnet): king adjacent ON the flank kills the passer by occupancy; bishop tours the one triangle; NEVER vacate the guard pawns; same-color bishops make my other pawns immune. -1 = threefold is THREE: repeat the keeper; if he sidesteps, repeat again next turn.
- OVERRIDE DEATH: a tool AVOID naming the lost unit + capturer + line is CLOSED - pick a different keeper, never send the flagged move to 'check the tool'. The gated candidate is the REFEREE's move; read its reason first.
- TOOL FLAG NAMING MY PAWN: verify by naming a CURRENT guard of that pawn; a live guard = the guarding keeper IS the send.
- FIRST REFUSAL = THE IDEA IS DEAD: next send is a plainly legal keeper <=10 s, one try.
- PAWN-FILE CENSUS: after ANY pawn capture a remembered pawn is DEAD; piece-map.py before every pawn push.
- GHOST LEDGER: totals come from the FEN only AFTER his capture's whole recapture chain; material-sweep.py/piece-map.py before ANY '+' or 'level' claim (T86R1 I wrote B+5 while truly ~B+4).
- QUEEN ON A HIS-ROOK FILE: name every his rook reaching her file in one move; a rook stepping IN FRONT hits her with tempo; her answer LEAVES the file.
- PAWN-BREAK DESTINATION LAW: before any push list EVERY unit reaching the landing square and all my recapturers in order; two enemy takers, one of mine = dead BEFORE the push.
- PIN TRANSFERS TO THE CAPTURER: capturing ON a slider-to-my-king line puts the capturer back on that line with HIS tempo; name the king step or surviving recapturer first.
- 60s ONE-MOVE LAW: refused candidate = FEN walk <=15 s; second refusal = plainest legal keeper, one try; NEVER a third variant. IN CHECK: flights/blocks/captures ONCE, pick, 3-5 s.
- FORCED RECAPTURE = MOVE CLOSED: forced replies 3-10 s from the FEN; both my knights BY SQUARE before a knight UCI.
- Q+R HERDING in check: before a flight name the delivery check that LANDS on the new square; all flights lose = least-cost flight in 5 s.
- ENGINE DRIFT = MOVE FIRST: level or worse = keepers 10-20 s, one verification sentence. DOWN / flag race = 5-10 s instant sends.
- RAY-THROUGH-QUEEN: after every his bishop/rook/queen move walk every line through my queen; a one-pawn screen is not a guard.
- FORK CHAIN, ONE HIS TEMPO PER CAPTURE (T86R1 kill, details notes/sicilian-black.md): before ANY capture with my queen near his pieces, name every one of his knight/rook jumps at her landing square AND each royal chain it opens; queen under NEW attack = settle her FIRST (Ra6/g6/Be7-class quiet), capture after. Up >=+3: quiet progress, zero more grabs.
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
- SEAL PUSH = TARGET BUILDER (T86R3): an unguarded new front square (h4-h5) that cannot be re-guarded = LOSE-1-BUT-PLAY-ON, worth ONE resend, never a three-try hunt. Before ANY push past move 20 name who guards the attacked front square.

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, SIT at formation; only a NAMED threat moves him.
- QUEENLESS LEVEL ENDING: both kings trapped -> his R+recurring Bc4/Bd3-class tempo hits on my rooks are the only decision; pre-write the rook-step. Rooks stay on squares NOT adjacent to his bishop's next diagonal.
- LAST-ROOK TRADE = K+P RACE COUNT FIRST; K+P: king DIRECTLY at the contested pawn.
- FLAG WIN TEMPLATE (proven at -3): one job per unit, 5-10 s passes, king parked, every keep tool-clean, ZERO positional gestures while down a piece.
- SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice.

## OPENING as White: g3 build everywhere (incl. v SF); bans: 4.Nf3/Be2 reversed-FK
- v ...e6+...d5 REVERSED-CARLSBAD - PLAY AGAIN (16 plies): 1.c4 e6 2.Nc3 Nf6 3.g3 d5 4.cxd5 exd5 5.d3 Be7 6.Bg2 O-O 7.Nf3 Re8 8.O-O Nbd7; level to m26. Then Re1 c6 d4 Bf4, Rb1, a4-class build; his ...Ne4 outpost makes the e4 break DEAD (no clean recapture ever) - play Nc5/Nd3 regroupings and even queen trades instead. BANS: h4-h5 seal (h5 hangs to ...Bf5-g4), Qd3??/Qc2?? (Ne4's d2/g3 jumps hit both), a5/b4 past his queen. Losses were sends, not chess.
- v SF WEDGE - DO NOT PLAY v SF (0-3): self-executing f5/g5 wedge, 'level' wrong at m11. see notes/english-rev-fourknights.md
- Reversed-GP v ...e5 - LEVEL six times now incl. T86R4's black mirror: 1.c4 Nf6 2.Nc3 e5 3.g3 Nc6 (6 plies), then d3/Bg2/Be7/Nf3 build, short castle; NO bishop sorties to b6/b5/a7-class squares - parked past pawn support = entombed.
- Reversed-QGD v SONNET - PLAY AGAIN, LEVEL to m20+: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6; then d3/Nc6/Nf3/Bd6, short castle, Qd2/Be6 build, the d4! break near move 14 = even trades, queens off. The loss came later, not the opening. see notes/english-white.md
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3; CRITICAL 5...Nxc3 6.bxc3!; Nf3/Be2 banned, f6 exf6 Bxf6, then d4! keeps the blockade (v Muse W).
- DEFAULT: g3/Be3 build with a3 BEFORE ...Bb4 (4.Nf3/Be2 BANNED); his Bd4 met by 12.b4 then a clean trade of the bishop; king off g1 only for a NAMED threat.
- Even + solid opponent: verify the ledger, ONE pawn target or a level draw; never a 30+ move shuffle from a hand ledger.

## OPENING as Black
- v 1.c4 ENGLISH MIRROR - PLAY AGAIN, T86R4 v Muse LEVEL m58 (16 plies): 1...Nf6 2.Nc3 e5 3.Nf3 Nc6 4.g3 d6 5.Bg2 Be7 6.O-O O-O 7.d3 Re8 8.e4 Kh8; his e4/f3/f5 wedge SELF-FROZE: answer 9...Bg4 10...Bxf3 even trade, ...h6, ...Nd8 (frees c6)->...c5!, ...Ne6, ...Nd4 traded for his bishop pair; then a5/Rd8 keeper loops to the threefold. see notes/muse-level-white.md
- v 1.d4: QGD CARLSBAD - PLAY AGAIN, WINS T84R5 + T85R4: 1.d4 Nf6 2.c4 e6 3.Nc3 d5 4.cxd5 exd5 5.Bg5; short castle, h6, Re8, b6/Bb7/Rc8 build; c5 wedge + Ne4!, Qc7 backs c5, knight trade into d3 = even trades. see notes/qgd-black.md
- Sicilian v 3.Nc3 (d6 orders): NEVER ...a6 vs his Bb5 pin - answer with a PIECE first, UNPIN FIRST.
- 2...d6 + his 6.Be2 build: his break opening HIS bishop ray = my bishop on it hangs, CAPTURE THAT BISHOP FIRST (...Bxf3-class). A raid needs ...Bb7 first.
- v the 4.c3 dialect (Smith-Morra accepted): PLAY AGAIN, opening NOT the problem (honest pawn up, his own eval ~level). ...dxc3! 5.Nxc3 Nc6; Bd7 v his Bb5 pin, Nf6, Qc7 (guards d6 v Bf4+...e6), Bxc6 Bxc6; then Bxf3 Qxf3, dxe5! (Qxe5 safe once his Nf3 is gone). I stood ~B+4 at m24 (T86R1) - the loss was the exf4?? conversion kill, not the opening; raid still needs ...Bb7 first, queen stays c7.
- v the 6.Be2 battery - PLAY AGAIN: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 8...Re8 (16 plies). CONFIRMED v Sonnet T85 SF2, level to m16; 9...e5! next, strike stands. A kingside kick prices its trade exits first. see notes/scheveningen-black.md
- v the 6.Be3 English attack + his O-O-O: 7...e5! strike CONFIRMED TWICE (T84R1, T85R7 both LEVEL). PLAY AGAIN. His O-O-O means RACE: ...b4, Rb8, Bb7, Qc7, a5, a4! hooking his Nb3. NO ...g6 vs his h4-h5 - keep the shelter SHUT. see notes/scheveningen-black.md
- Four Knights v 3.Nc3: 3...Bb4, 1/2 from -5; NEVER Ncd7/Nb3; shell shuffle, threefold only after every recurrence counted.

## OPPONENTS (one-liners)
- STOCKFISH 19: instant, zero illegal, his clock never moves (mine is the only one in the room). Punishes static clamps by COMPOUNDING: +0.3 per few quiet moves until the wedge is +7. Punishes capture greed with the NEXT tempo, not the recapture: my exf4?? at B+4 -> Nb5/Nc7+/Qd1+ royal chain, mate m18. Level v SF = 15-25 s keepers, ONE named break by m25; keepers-only = slow death; accepts threefold only vs a sound shell.
- SONNET 5.5: banks 50-60 min, zero illegal, engine-clean keepers, trades evenly. At level he wins only the clock; a level rook ending = DRAW RESULT. In -1 BvB he converts the passer but could NOT break the anchored Kc3 fortress. His kills arrive only AFTER my shelter loses its SECOND guard. Beat plan: MY pace.
- DEEPSEEK V4.1 Flash: loses by CLOCK only - 2-9 min thinks on QUIET moves (T86R3: 8:55 on Qb4) even as the flag race says otherwise; ended 27 min vs my 50 banked, so MY pace was winning on the clock. Board: engine-clean keepers (only f6?/Qc7?? all game), parks units inside his walls (Ne4 outpost, Qb4) with no entry. Beat plan: pre-verified keepers 10-20 s, bank 40+ min, ONE frozen move per flag - my forfeits vs him are mine.
- MUSE SPARK 1.3: SLOW (1-3 min/move), few board errors (1.c4?!, b3??), does NOT attack - parks units (his e4/f5 wedge self-froze in T86R4) and lets my senders forfeit. T86R4: 2 invalid tries, burned to 2:07 v my 16 banked, clean level threefold. Beat plan: every unit on a two-exit square, ONE verified send per move at 10-20 s in PLAIN UCI, progress by a SUPPORTED break every ~8 moves, then keeper loops; a level game v him is decided entirely by MY try budget.
- ALL: when I'm up BIG they bank; one pawn break or rook-attack per game.

## Notes
notes/english-rev-fourknights.md - v SF: wedge line, memo-fix + creep + stale-square kills, herding net
notes/english-white.md - reversed builds incl. T86R3 v DeepSeek, T84R3 Sonnet +1-forfeit, endgame kills
notes/qgd-black.md - T84R5/T85R4 v DeepSeek WINS: Carlsbad build, d4+c5 breaks, double-hit send economy
notes/scheveningen-black.md - T85R7 Muse race + refusal-starvation forfeit; T85 SF2 two-diagonal kill
notes/sicilian-black.md - 4.c3/Morra accepted T86 fork-chain kill, g5-kick kill, +9 shell
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
