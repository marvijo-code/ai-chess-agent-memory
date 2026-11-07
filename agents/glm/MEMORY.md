# MEMORY - GLM 5.3 Flash

Last change: T83R5. LOST BY FORFEIT v SF19 at m18 while LEVEL to m13 (my Qxe4! got the only good mark): all gates - 12.c3?? ILLEGAL (c-pawn traded on m4; a remembered pawn file is DEAD after ANY pawn capture), 14.Qf4 gated 3x and the REFEREE played it, dropping B-for-P in one move (+0.5 -> +2.3), then 3 provider failures after ...Re6! +5.7. Every send tool-clean with the recapturer named BEFORE sending; unsure = the plainest legal keeper, ONE try. White default unchanged: g3/Be3 build with a3 BEFORE ...Bb4 (4.Nf3/Be2 BANNED). 60s law stands; a forced recapture CLOSES the move.

## FIRST, EVERY GAME
- KING-KEEPER RATCHET (T83R4 forfeit): after MY OWN king (or rook) hop its old square is DEAD as a keeper; every king/rook/queen keeper re-derives its square from the FEN at send time; one piece-map read before every king keeper, then send <=15 s.
- FIRST REFUSAL = THE IDEA IS DEAD (T83R3): after ANY refusal the next send is ANY plainly legal keeper <=10 s, ONE try - never a variant, never the same square re-argued. HIS true flag naming MY piece = one try, keep the piece; a flag naming my TARGET = dead. Mark-ban: g4! in the g3/Be3 build.
- PAWN-FILE CENSUS (T83R5 c3??): after ANY pawn capture by either side a remembered pawn is DEAD - piece-map.py before every pawn push.
- GATED CANDIDATE = HIS MOVE (T83R5 14.Qf4): the referee played my gated attacker and ...fxe4 dropped B-for-P (+0.5 -> +2.3) while I burned 5 min. The gate is NOT protection: name the recapture chain on the CURRENT board before the FIRST send; no unverified attacker - the plainest tool-clean keeper goes.
- QUEEN ON A HIS-ROOK FILE (T83R5 ...Re6! +5.7): before centering a queen name every his rook that reaches its file in ONE move; a rook stepping IN FRONT hits her - and the pawn behind her screen - with tempo. Her answer LEAVES the file, never steps onto an attacked square.
- PAWN-BREAK DESTINATION LAW (T83R3 g4??): before ANY pawn push list EVERY unit reaching the landing square (sliders through EMPTY squares + every knight jump) and ALL my recapturers in order. Two enemy takers, one of mine = dead BEFORE the push. Name the carry: g3 builds carry breaks through c-pawns, Ne5/Nd2 steps or a Bh6-Qe2 e4 pair, never through an occupied square.
- FORTRESS CENSUS WRITTEN ONCE (T82R4): sealed-line list at formation; later keepers ONE sentence + send <=15 s; a note re-narrating the census is THE SEND SIGNAL.
- PIN TRANSFERS TO THE CAPTURER (T82R4 38...Nxh6): capturing ON a slider-to-my-king line puts the capturer back on that line with HIS tempo. Name the king step or surviving recapturer first.
- 60s ONE-MOVE LAW (T82R2: 20:21 lost the game): refused candidate = FEN walk <=15 s; SECOND refusal = plainest legal keeper, one try; NEVER a third variant. TOOL-AVOID answer = a different quiet king/rook/bishop-square move in one try.
- FORCED RECAPTURE = MOVE CLOSED (T82R3): forced replies 3-10 s from the FEN; BOTH my knights BY SQUARE before a knight UCI; a cut-off/unfinished plan note = the LAST VERIFIED KEEPER goes NOW.
- AN ATTACKED UNIT PLAIN ESCAPE IS HIS TEMPO (T82R3 13.Nf5!): price every candidate hit before pushing against a GUARDED pawn.
- BISHOP-ENTRY FILE: my g-pawn on g3 (g2 empty) or any unit on a rank his pawn passed = his bishop LANDS and my pieces cannot take it. Name h3/g4 entries and the eaten rook's flight in every retreat census.
- ENGINE DRIFT = MOVE FIRST (T82R2, T83R2): level OR worse = keepers 10-20 s, ONE sentence of verification; the 3-7 min think blocks against SF's 15-40 s keepers WERE the game. DOWN = 5-10 s instant sends, accept the drip.
- SF DRIFTS = PURE GENIUS: Qh6-f4-h4 checking loop, Rdf8/Rg8 doubling, c6+f5 flips. Lost = 5-10 s sends, his clock does the rest.
- PAWN CAPTURE OPENS MY K-FILE: before any g/h capture near my castled king walk the queen's newly-opened file (Qxh4+ net, T82R2).
- RAY-THROUGH-QUEEN: after every HIS bishop/rook/queen move walk every line through my queen's square; a one-pawn screen is not a guard.
- DOUBLE-HIT QUEEN: the flight must dodge the FOLLOW-UP fork; name the attacker's next fork square, walk its 8 jumps, then fly. Capturing the attacker counts as a flight.
- CHECK MET BY BLOCK-WITH-TEMPO (T83R2 17...Bc5+??): before a bishop/queen check name every block square and ask whether his block ALSO hits my checker along the same diagonal.
- GHOST LEDGER: after EVERY capture write BOTH totals from the FEN, pawns by file; recount once more after the trade loop closes ('+1' believed at true LEVEL twice).
- EVERY SEND = UCI FROM THE CURRENT FEN, never a remembered SAN - after MY OWN king/rook hop the remembered KEEPER square is stale too. Doubled rooks = UCI first. material-sweep.py before ANY material claim; after ANY his-capture rebuild from the FEN first.
- EP CENSUS: before ANY double push name the neighbor e.p. capture square and what the push opens.
- HIS FORK OR HIT ON Q+HEAVIES = PRICE ONCE, SEND ONCE: the flight keeps her, the CHEAPEST unit drops; count from the FEN, send in 10 s.
- IN CHECK: list once - flights, blocks, captures, partner captures; one pick, 3-5 s.
- WEDGE RULE: a pawn wedge (b4/c5/f5/g5/d4) is already a POSITION: challenge its support or its landing square; knight retreats that leave the wedge running = repeat loss. SF's ...d4 wedge (T83R5): the Ne4-trade dodge beats chasing it.
- KNIGHT JUMPS BOTH WAYS (pawn-destination-sweep.py); QUEENS OFF = SHELTER FIRST.
- OPEN-FILE BAIT: my piece on an open file, zero my-guards, his heavy near = taken next.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS; RECAPTURER'S LINES FROM ITS NEW SQUARE.
- ATTACKED PIECE = RETREAT LIST FIRST (escape-sweep.py); MUTUAL ATTACK = his move wins the race; LANDING GUARD BEFORE PURPOSE.
- OWN-BLOCKADE KILLS MY BREAK; FRONTIER PUSH = recapturer on the NEW board.
- TOOL SILENCE BEATS NARRATIVE: tools FIRST; a tool AVOID is dead unless I name a square-walked refutation.
- THREEFOLD IS DIRECTION-SENSITIVE: down/fortress drives it, even/up is MY loss.
- UP BIG = QUIET-PROGRESS CONVERSION, king anchor first; LEVEL v a fat banked clock = pure seconds-race: keepers 5-20 s, no shuffle catalogue (a level game vs a 1-4 min/move opponent is lost ONLY when my senders fail).
- CLOCK: book 5-10 s, routine 10-20 s, HARD CAP 30 s (endgame hold 30-60 s); down = 10 s, LOST = 5 s; the 60s ONE-MOVE LAW sits on top of all of it. ONE send per move, never a second remembered keeper.
- TRADE-OFFER LANDING = all his attackers of the square, never the prompting piece alone.

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, SIT (T82R4): choose h7 or h8 ONCE at formation; only a NAMED threat moves him; vary nothing else without a candidate.
- LAST-ROOK TRADE = K+P RACE COUNT FIRST (T81R1 50.Rd3?); K+P: king DIRECTLY at the contested pawn (52.Kc3??).
- FLAG WIN: level position, one job per unit, 5-30 s passes, king parked - v MUSE works twice; v SONNET a level rook ending is a DRAW result; v SF a level game needs ONE named pawn break by move 25, not shuffles.
- +2P -N WALL v SF (T77R5): entomb his rook behind his own Nc5; wall map c3/c4/e4/f3/g3, Bf1/Be2 on d3, rooks c2+d2, Kg1/g2.
- Fortress stops forcing checks; SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice.

## OPENING as White: g3/Be3 build everywhere (incl. v SF); bans: 4.Nf3/Be2 reversed-FK
- DEFAULT (T82R1.2 v Muse, LEVEL; the v SF choice): 1.c4 Nf6 2.Nc3 e6 3.g3 Nf6 4.Bg2 Bb4 5.Nf3 O-O 6.O-O d6 7.d3 Re8 (14), then e4 h6, 9.Be3 Be6, 10.Qd2 Rc8; a3+b4 dissolve the Bb4 pin into queenside space, a3 BEFORE his ...Bb4 exists; his Bd4 met by 11.a3 Bc5 12.b4 13.Bxd4! (banked trades); Nd5 holds d4/e4 with g2-bishop backing; queen stays d2 or trade-guarded; king off g1 only for a NAMED threat; g4! mark-banned.
- v SF ...d4 WEDGE (T83R5, LEVEL to m13 - PLAY AGAIN): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Bg2 d4 6.Ne4 Nc6 7.d3 Nxe4 8.Bxe4; then the pattern Nf3/a5, O-O O-O, Qd2 Nb4, a3! axb4 Bxb4 = about level; NEVER 14.Qf4 (gated-then-lost B-for-P). g4 banned.
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3; CRITICAL 5...Nxc3 forks Qd1, 6.bxc3!; Nf3/Be2, f6 exf6 Bxf6, 12.d4!, 13.Bxd4 keeps the blockade (v Muse W).
- Reversed-GP v ...e5: LEVEL FOUR times, the opening NEVER lost. T83R3 stored order (16 plies): 1.c4 Nf6 2.Nc3 e5 3.g3 Nc6 4.Bg2 d6 5.d3 Be7 6.Nf3 O-O 7.O-O Re8 8.e4 Be6; then the pattern h3 Nd7, Be3 Qc8, a3 h6, Nd5 Kh8, Qe2 Nf6, h4, Rad1/Rac8, Qd2 a6, a4 a5 - LEVEL to m21, PLAY AGAIN. Nge2 is ILLEGAL in this order; queen stays d2 or trade-guarded.
- BANNED v SF: 4.Nf3/Be2/7.O-O reversed-Four-Knights; the g2-shell works only with a3/anti-pin first and queen OFF d1 (d2-c2).
- Even + solid opponent: verify the ledger, ONE pawn target or a level draw; never a 30+ move shuffle from a hand ledger.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6?; answer with a PIECE first; pinned Nc6 UNPIN FIRST.
- 2...d6 6.Be2 build: his break opening HIS bishop ray = my bishop on it hangs, CAPTURE THAT BISHOP FIRST (16...Bxf3!). Raid needs ...Bb7 first; every ...b5/...b4 knight-jump sweep first.
- v the 4.c3 dialect: LEVEL to m10; the raid needs ...Bb7 first, queen stays c7.
- v the 6.Be2 battery: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O (14), then ...Re8 FIRST. STRIKE CONFIRMED TWICE: his 9.f4? -> ...e5! (f4 is the target), 10.fxe5 dxe5; his 11.Nf3? -> 11...Nc6! holds e5 (12.Nxe5 Nxe5 = no recapture); queens off by m12 = LEVEL minor ending. ...e5 ONLY with ...Re8 placed or ...Nxd4 traded. After: ...Be6/...Qc7/...a6/...b5; ...Qb7/...Bd7 + ...Bxc3! kills his LAST e5-attacker, e4 entombed - PLAY AGAIN. A kingside kick prices its trade exits first (16...g6?! gave 17.Nxe7+; 31...f5 at 3:30 = the flag).
- v the English Attack: ...Nxd4/...e5 counterstrike confirmed; see notes/scheveningen-black.md.
- Four Knights v 3.Nc3: 3...Bb4, 1/2 from -5; NEVER Ncd7??/Nb3??; shell SHUFFLE, threefold only after every recurrence counted.

## OPPONENTS (one-liners)
- STOCKFISH 19: instant, zero illegal; grinds: pin -> Bh3! exchange, king-hunt loop to flag, wedges SELF-EXECUTE. T83R5: met my g3 build with 3...d5/...d4 out of book and won on MY gates, not chess. Every move obeys the 60s law; every retreat includes a flight census; accepts threefold only vs a sound shell.
- SONNET 5.5: banks 50-54 min, ZERO illegal, engine-clean keepers, trades evenly, plays a4/b4/Rad1/Kf2 positionally. At LEVEL he wins nothing on the board, only the clock; a level rook ending = DRAW RESULT; takes the last-rook trade only when the K+P race is won. T83R4: he beat me ONLY through my three stale ...Kf8 tries (T83R4 ratchet). Beat plan: MY pace, nothing else.
- DEEPSEEK V4.1: solid, banks 40+ min while I decay, one ghost per game. T83R2 6.Be2 Scheveningen: my LEVEL game forfeited m32 on quiet keeps; his board errors went unexploited. Stored build + 20 s pace + material-sweep every capture beats him. T82R1.1 e.p. fork - see EP CENSUS.
- MUSE SPARK 1.3: SLOW, finds forks, forfeits on time when level. T83R3: 1-3.5 min EVERY move, zero material errors shown - my g4?? forfeit was his only win. Recipe: trade his ONE active aggressor, then fast LEGAL keepers <=30 s; the flag kills him only while my senders hold.
- ALL: when I'm up BIG their plan is 'do nothing' and bank; one pawn break or rook-attack per game.

## Notes
notes/official-memory-rest.md - legacy rules index
notes/english-rev-fourknights.md - v SF: T81R5 slot, T82R2 g3-door, T83R5 ...d4-wedge + gate-cascade law
notes/english-white.md - reversed-GP build (4x LEVEL), T81R1 endgame kills, T83R3 break census
notes/four-knights-black.md - four knights v SF: pawn-takes kills
notes/scheveningen-black.md - Sonnet/Muse/Sol builds, English-attack jobs
notes/sicilian-black.md - 4.c3 dialect, g5-kick kill, +9 shell
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonal rules
notes/taimanov-sol.md - 6.Be2 battery: strike confirmed v DeepSeek+Sonnet, ghost +1 law, block-with-tempo
notes/white-maroczy.md - Maroczy; 7.f3! pin fix; SHORT castle; b2 mate door

## Tools
see-sweep.py - SEE-lite first; IN CHECK prints the full reply list (run FIRST).
recapture-scan.py - flags his recaptures that would attack my queen.
escape-sweep.py - unattacked retreats for each attacked piece.
pawn-destination-sweep.py - flags his pawn/KNIGHT jump hits on my pieces.
kick-escape-sweep.py - pinned pieces, pawn kicks a knight/bishop escapes.
mate-net-scan.py - flags mate nets and lists my mate-in-1.
piece-map.py - RUN FIRST: prints TO MOVE, my king square, full piece map by square, material - no remembered keeper or pawn file without it.
material-sweep.py - W/B totals + every pawn/piece by square; run before writing ANY '+' claim or plan.
safe-keepers.py - ranks every legal move by the capture-race material it keeps; top 3 safe moves + AVOID for moves far worse than best; run when unsure, after any refusal, or before any attack.
