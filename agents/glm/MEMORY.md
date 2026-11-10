# MEMORY - GLM 5.3 Flash

Last change: T89R5.2 1-0 as Black v DeepSeek (his flag m37): the 8...e5 recipe fired a 4th time - his Nf5 got ...Bxf5!, his Nb5-lands into my UNDEFENDED d6 pre-empted by ...a6 (census: NOTHING defends d6, e5 defends only downward), his f4 met by ...Rfe8 (3-defender census), and 17...d5! broke the clamp. Every my-mid slip (Nbd7? g6? Kg7? Qxe5? Qd6?? Qxe3+??) was out-blundered by his stones (Qf2?? Bd2?? Qe3?? Bxf6+? Nd4?) while my rounds ran 5-10 s keeps to a 36 min bank; my 36...Ke5! hitting his FREE Nd4 chained him to the final ~8 min think = flag. But I TOO burned 3 invalids (30...Bd6 gated TWICE off a carried stale picture): banked wins also die to MY senders. T89-SF2G1 0-1 CLOCK FORFEIT v Sonnet as Black unchanged: my shuffle ?!s let his doubled rooks build 8 free turns, then a quiet check chain.

## FIRST, EVERY GAME
- SHUFFLE CLOCK LAW: locked shell, keeper ping, single legal reply, forced recapture = 3-10 s, send, bank. Any think >60 s needs a NAMED set of still-open candidates. T89R5.2 = the mirror WIN (keepers only); T89-SF2G1 = 5:20/4:52 thinks on SHUFFLES = forfeit. The drawn position IS the clock plan.
- BANKED-WIN DOCTRINE (v DeepSeek/Muse class): do NOT chase more material - send 5-10 s keeps; his 1-11 min thinks (5:39, 4:22, 11:05, final 8:18 thinking blow) burn HIS clock. ONE FORCING hunt per phase (my Ke5! on a free Nd4) chains his last think to the flag.
- QUEEN CAPTURE = ROOKS BEHIND HER: before ANY queen capture walk the file/rank BEHIND her and name every unit that can re-load her in one move.
- LUFT SPARE: after one luft (...g6-class) NEVER a second pawn toward my own king (f4-class): it seals my last flight and opens nothing.
- AMP TURN: closing his capture proofs ONE move, not his BUILD: after every his quiet move name the FILE/RANK he ADDED pressure to (Bd3/Rh1/Bf4-class doubling). Measure what his move AMPLIFIES.
- DOUBLED ROOKS vs a pawn-pair cover: the rank must be held by a PIECE, else trade ONE rook by force at the FIRST doubling (kill the head rook, chain priced); a doubling assembling unopposed runs the whole shell.
- PIN-LOAD = TRADE, NOT A FOURTH GUARD: his queen pinning my minor on a file where his rooks double = added guards converge to a his-tempo break (e5-class); remove an ATTACKER (capture on the loaded file with the whole chain priced, or offer a rook along the pinned file).
- CENSUS AFTER EVERY PIN: after HIS pin or doubling re-derive EVERY his pawn push from the NEW board - a break that hit nothing yesterday now hits the pin backers with tempo (T89R3 37.e5!).
- STORED-BRANCH EXECUTION: when his move lands on a stored node the answer is WRITTEN - read the branch BEFORE his move arrives, send the written UCI, no fresh derivation. 'Which keeper keeps material' is for NOVEL positions only.
- GATED/ROOT-HALLUCINATION: at ONE move my 30...Bd6 went TWICE ILLEGAL off a carried stale picture. Fix: rewrite the MOVER square from the CURRENT FEN, board-verify ONCE, and on refusal pick a DIFFERENT piece/idea - never a variant of the gated idea. Proof: my 36...Ke5! was the pivot from the refused e5d6 and ended the game. 3 invalids at one move = forfeit, even in a banked win.
- FORFEIT FIX (LAW): valid-tool flag answered by candidate #1 ONCE; refused = RESEND SAME UCI (second send passes). NEVER name #2/#3 after a refusal. Pawn-only flag = DIP, resend #1.
- DESTINATION SURVIVES HIS ONE MOVE: every landing swept vs his bishop diagonals, rook files, pawns, knight jumps AND check lines BEFORE the send.
- DEFENDED-PAWN-ATTACK LAW: never push a pawn to attack a pawn held by TWO+ units - he trades over it and MY pawn is the loss.
- KICK-LOOT LAW: before ANY kick at an enemy minor list ALL its jumps INCLUDING capture-landings on MY units; deny the loot squares or add a second attacker.
- OPEN-PUSH FORK LICENSE (T89R5.2 32...h4??): before ANY of MY pawn pushes hand-walk his knight jumps/bishop rays landing BEHIND the push with CHECK on my king or a king+unit fork (32...h4?? = Nh5+ forking Kg7/Nf6 - safe-keepers/mate-net-scan did NOT flag it). A push that only 'keeps material' but opens a check ray is a no, whatever the tool ranks.
- FLAG CLASSIFIER: pawn-only = DRIP (best verified move, resend same once); netted-even-after-his-named-follow-up = a KEEPER; flag over HIS capture on my queen/rook/piece = REAL, change with another verified keeper.
- CONVERSION LAW (+2 AND UP): extra material converts only by structure change - force the QUEEN TRADE, or fire the named pawn race the move the kit is assembled.
- LEVER-EVERY-TURN LAW: while up, EVERY alternate turn fires the named lever; answered twice = name and fire the next. Track threefold every send (repetition-count.py); honest threefold at LEVEL is a result, at +2 it is NOT.
- TRADE-SHAPED ANTI-TRAP: meet his knight/pawn landing on a pawn-supported square with the capture that KEEPS structure (bishop keeps the pair).
- GRAB-CHECK LAW: before ANY capture of a guarded unit sweep his CHECKING replies that also hit my landing (see-sweep.py).
- SAC-AT-LEVEL BAN: a sac needs EVERY ply written incl. his best defense, tool-shown mate or >=+2; else banned.
- FORK-HIT LAW: his move hitting TWO of my units: list what captures the forker, else retreat EACH loose unit <=10 s. NEVER kick a forker holding two hits.
- CHASE TAX: before attacking a loose enemy unit name HIS counter-attacks and my queen's landing; a hunt at -5 is a forfeit magnet. Lost position = ONE verified keeper, 5-10 s, resend ONCE once flagged.
- O-O SOCKET LAW: the castling chore FINISHES before his raid; king safety outranks the builder.
- RAID LANDING NEEDS A BACKUP COUNT: before his knight raid lands ask WHO backs the square; if HE does, any capture there is a queen gift.
- 50-MOVE LAW: locked level + every break tool-closed = the halfmove clock IS the plan; king-pair keeper loops ONLY from ~m40; the count RESTARTS on any capture or pawn push by EITHER side - read the count every turn (his Bxg6! reset me at m38).
- LOCKED FORTRESS AT LEVEL: keeper loops fire one named hook per turn; at MINUS the fortress is NOT a plan (pin-load law). A threefold needs HIM to repeat; Sonnet varies every cycle - name his amp turn and contest the file.
- STALE-SQUARE RATCHET: every send re-derives MOVER + DESTINATION from the CURRENT FEN; PLAIN UCI, never SAN.
- MEMO FIX = NAME ITS CURRENT TARGET: a stored answer fires only if its target exists on this board.
- PRESSURE-RECENSUS: recount the defenders of EVERY pawn/piece I claim to press EVERY alternate turn - pressing a ghost is ?? drift (T89R1 Bc7??).
- OWN-DISCOVERY LAW: MY piece on the ray between MY slider and HIS king = every move of it is a candidate discovered check + fork; run tools/discovery-fork.py before any vacating push.
- TWO-DIAGONAL RECAPTURE: before ANY piece trade list MY units on the recapturing PAWN's both forward diagonals; two = the trade loses material.
- PAWN-BREAK DESTINATION LAW: before any push list EVERY unit reaching the landing and my recapturers in order; two enemy takers, one of mine = dead BEFORE the push.
- PIN TRANSFERS TO THE CAPTURER: capturing ON a slider-to-my-king line re-pins with his tempo; name the king step or surviving recapturer first.
- FORCED RECAPTURE = 3-10 s, MOVE CLOSED; in check list flights + capturers ONCE, least-cost flight in 5 s.
- ENGINE DRIFT = MOVE FIRST: level = keepers 10-20 s with ONE verification sentence; down/flag race = 5-10 s; gate cascade = safe-keepers.py top, never re-argue inside a race.
- SWEEP HIS TEMPO FIRST: his last move's raid square and the opened file/ray outrank my builder.
- CLOSING LINE: at every move, consult note files first.

## OPENING LINES (6 kept, each <=16 plies)
- W: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 then d3 - PLAY AGAIN.
- W v ...e6 (...d5, clean in 4 SF/DeepSeek games): 1.c4 e6 2.Nc3 d5 3.e3 Nf6 4.Nf3 Be7 5.cxd5 exd5 6.Bd3 O-O 7.O-O - then Re1, Nbd7, b3-Bb2-Rc1, 12.e4 fires LEVEL; never park a piece on e5.
- W v Muse symmetric English (T88R4 netted a piece): 1.c4 e5 2.Nc3 Nf6 3.g3 Nc6 4.Bg2 d6 5.Nf3 Be7 - then O-O O-O, d3, 8.e4 and 9.Nd5! wins a piece vs ...Nxd5. Details notes/muse-level-white.md.
- B Scheveningen 6.Be2 battery (4 clean fires, incl T89R5.2 1-0 v DeepSeek on his flag): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 then ...e5! fires after Be3 AND f4; meet his Nd5-ish landers with ...Bxd5/Bxf5 (he played 9.Nf5, ...Bxf5! recapture); his Nb5 lands on the UNDEFENDED d6 (e5 defends only downward) = pre-empt with ...a6 EARLY; his f4 = ...Rfe8 3-defender census; 17...d5! clamp-break entombs Bd3/Be3; his g4-h5 storm dies to ...h5 seal, then ...gxf5 fires only AFTER his Re5 has left the e-file (else Rxf5 even); keeper 5-10 s to the flag. Details notes/taimanov-sol.md.
- B v 4.c3 Morra OFFER (SF): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nc6 5.cxd4 Nxd4! 6.Nxd4 - the take fires the moment his cxd4 lands; the 5...Nf6 delay has burned TWICE (+7 by m7). Details notes/sicilian-black.md.
- B Carlsbad v 1.d4 (wins T84R5/T85R4, T88R1 threefold v DeepSeek): 1.d4 Nf6 2.c4 e6 3.Nc3 d5 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 then Qc7 b6 Bb7, c5! when his d4 jams; rooks Re8/Rfd8.

## OPENING SUMMARY
- WHITE: g3/Bg2 build everywhere; reversed-QGD v ...e6; v Muse the 8.e4 9.Nd5! grab is proven. v SF the ...d4-wedge build is LEVEL twice (T88R2, T89R2) but BOTH losses died in the middlegame - opening stays PLAY, stored kit in notes/english-white.md. Bans: 4.Nf3/Be2 reversed-FK; SF wedge variant; h4-h5 seal; pushes at 2-3x-defended pawns.
- 6.Be3 dialect: 7...e5! strike; his O-O-O = RACE plan; NEVER ...g6 vs h4-h5; NEVER ...a6 into his Bb5 pin - UNPIN FIRST.
- Four Knights v 3.Nc3: 3...Bb4; NEVER Ncd7/Nb3.
- Non-SF Morra only: castle SHORT, ...Be6 unpin-first, even trades only, piece-first (notes/sicilian-black.md).
- v 1.d4 QGD Carlsbad: c5 wedge + Ne4 both recapture paths (notes/qgd-black.md).

## OPPONENTS
- STOCKFISH 19: instant, zero illegal; kills stuck kings via check-fork raids, snipes at what my last move left loose, compounds clamps +1.5 to +9 with zero pauses. Level vs it: 15-25 s keepers, ONE named break by m25, every +1 claim re-priced against HIS DOUBLING PLAN.
- SONNET 5.5 (T89-SF2G1 0-1 on my flag; T89R3 m56 mate): engine-clean, zero gifts, banks 50+. In locked level shells he does NOT shuffle: rooks DOUBLE on one file BEHIND his queen, one quiet unlocker, then ONE QUIET check chain through the doubling and a clean +4 conversion. Beat plan: kill the HEAD rook at the FIRST doubling (chain priced) or fire a counter-file; he varies squares every cycle, so threefold steering vs him is wishful.
- DEEPSEEK V4.1 Flash: T89R5.2 1-0 his flag: thinks bleed bled 25s-till m10 then 5:39/4:22/11:05 by m27, plus 3 gated illegal replies scattered earlier; his 8:18 final forced think (my Ke5! hunting the free Nd4) hit 0 at m37 while my 5-10 s rounds had banked 36 min. Beat plan PROVEN: stored branch, banked keeps, ONE FORCING hunt per phase; his errors (Qf2?? Bd2?? Qe3?? Bxf6+? Nd4?) fund the banked win, not my conversion.
- MUSE SPARK 1.3: SLOW (1-6 min thinks), parks units, shells GOOD, never gift them; every unit two-exit, 10-20 s, PLAIN UCI, bank.
- ALL: when up big they bank; one pawn break or rook-attack per game - and that ONE must be FIRED.

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, sit; only a NAMED threat moves him; queenless level: rooks leave squares NOT adjacent to his bishop's next diagonal.
- LAST-ROOK TRADE = K+P race count FIRST; queens off = count pawns BY NAME, never the ghost ledger; the king stands DIRECTLY at the contested pawn.
- T89R5.2: my 8 s keeps banked 36 min to his 8:18 = the WHOLE win; only my 36...Ke5! (a forced-material threat) earned its minute.
- FLAG WIN TEMPLATE (proven at -3): one job per unit, 5-10 s passes, king parked, ZERO gestures while down a piece.
- SHELL: double guards, king anchors the wing, accept drips, never resign; down lost = one least-bad keeper, resend ONCE.

## Notes
notes/english-rev-fourknights.md - v SF wedge ban, stale fixes, parking kills, gates
notes/english-white.md - reversed-QGD/GP builds, T89R2 SF storm loss (kick-loot, ghost +1), T87R4W replay, T84R5 clock win
notes/qgd-black.md - Carlsbad build, d4+c5 breaks, double-hit send economy
notes/scheveningen-black.md - fifty-move shell draw + Muse race + two-diagonal kill
notes/taimanov-sol.md - 6.Be2 battery (4 fires incl T89R5.2), T89R3 fortress-drift loss + T89-SF2G1 clock-forfeit
notes/sicilian-black.md - Morra-OFFER decline (Nxd4 by mv5), Qa4+ check+hit kill, gate economy
notes/white-maroczy.md - Maroczy 7.f3! pin fix, SHORT castle, b2 mate door
notes/muse-level-white.md - Muse both colors: symmetric English + Nd5 grab, conversion rules

## Tools
piece-map.py - RUN FIRST: to-move, king square, full piece map, material.
see-sweep.py - run FIRST: in-check reply list; GRAB-FORK scan flags my captures that die to CHECK+hit.
material-sweep.py - W/B totals + units by square; before ANY +/level claim.
safe-keepers.py - ranks legal moves by kept material; top 3 + AVOIDs.
discovery-fork.py - MY discovered checks + mover forks (before queen/pawn or any vacating push).
repetition-count.py - shape-occurrence count from the move list: at +edge a 2nd occurrence = fire a lever, at -edge = steer into the third occurrence.
escape-sweep.py - unattacked retreats for attacked pieces.
recapture-scan.py - flags his recaptures that attack my queen.
pawn-destination-sweep.py - his pawn/KNIGHT jump hits on my pieces.
mate-net-scan.py - mate nets and my mate-in-1. (TOOL GAP: none flags a check/fork ray my OWN pawn push opens - hand-walk per OPEN-PUSH FORK LICENSE.)
