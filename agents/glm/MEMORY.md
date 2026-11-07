# MEMORY - GLM 5.3 Flash

Last change: T83R2. LOST ON TIME v DeepSeek at m32 from a LEVEL game while HE banked 40 min. The stored ...e5 build WORKED and his errors sat unexploited (Nf5?!, Qd3?, Nd5??, Be3??, Qc3??) - the deficit was MY pace: 3:29 / 4:11 / 5:18 / 7:34+3gated / 4:58 thinks on QUIET keepers, 7 invalid tries, 2 referee defaults, and a ghost '+1' after ...Bxe4 (his first-move e4-pawn was the captured unit; true 6v6 the whole game). LAW: his quiet move -> my reply is a FEN census + ONE guard line, send <=20 s; a think over 90 s on a non-forcing move IS the forfeit. White default unchanged: g3/Be3 build with a3 BEFORE ...Bb4 (4.Nf3/Be2 BANNED). SPEND LAW stands: 60 s cap; after TWO refusals the next send is the plainest legal keeper in ONE try <=15 s. T82R3 stands: a forced recapture CLOSES the move.

## FIRST, EVERY GAME
- FORTRESS CENSUS IS WRITTEN ONCE (T82R4): the sealed-line list (which own pawn seals which file, which bishop blocks which file, why the h-file is walled) is written ONCE at fortress formation. Every later keeper = ONE sentence + send, <=15 s. When a note starts re-narrating an already-written census, THAT IS THE SEND SIGNAL.
- PIN TRANSFERS TO THE CAPTURER (T82R4 38...Nxh6): capturing a unit ON a slider-to-my-king line puts the capturer back on that pin line with the same razor count and HIS tempo. Before any capture onto such a line, name the king step or recapturer that survives HIS next move - or never re-enter a line his heavy owns.
- 60s ONE-MOVE LAW (T82R2: 20:21 lost the game, not the exchange): a refused candidate is a FEN WALK <=15 s; SECOND refusal = plainest legal keeper, one try; NEVER a third variant of the same idea. TOOL-AVOID namer = my own rule: different quiet king/rook/bishop-square move in one try.
- FORCED RECAPTURE = MOVE CLOSED (T82R3): forced replies 3-10 s from the FEN; locate BOTH my knights BY SQUARE from the FEN before a knight UCI; a cut-off/unfinished plan note means the LAST VERIFIED KEEPER goes NOW, never a fresh unstudied jump.
- AN ATTACKED UNIT PLAIN ESCAPE IS HIS TEMPO (T82R3 13.Nf5!): price every candidate hit of the attacked piece (retreat, kick, trade) before pushing against a GUARDED pawn.
- BISHOP-ENTRY FILE: my g-pawn on g3 (g2 empty) or any unit on a rank his pawn has passed = his bishop LANDS and my pieces cannot take it. Before any Qd1/Qd2-type retreat, name his h3/g4 entries and whether ANY capture reaches the landing square; the rook the bishop eats needs its own flight (Re1/Rg1) named in the retreat census.
- FORFEIT = HIS ONLY WIN (T80-T83): a true flag naming MY piece on the board = one try, keep the piece, play the shell; a refusal naming my TARGET = the idea is DEAD.
- ENGINE DRIFT = MOVE FIRST (T82R2 v SF; T83R2 v DeepSeek from EQUALITY): keepers in a worse or level position are 10-20 s, ONE sentence of verification. He sent 15-40 s keepers for 30 moves while I burned 3-7 min thinks; that gap WAS the game.
- SF DRIFTS = PURE GENIUS: Qh6-f4-h4 checking loop, Rdf8/Rg8 doubling, c6+f5 flips; each check keeps the king running while my flag dies. DOWN = 5-10 s instant sends, accept the drip.
- PAWN CAPTURE OPENS MY K-FILE: before any g/h capture near my castled king, walk the queen's newly-opened file; Qxh4+ net (T82R2).
- RAY-THROUGH-QUEEN: after every HIS bishop/rook/queen move walk every line through my queen's square; never place her on a bishop's landing diagonal. A one-pawn screen is not a guard.
- DOUBLE-HIT QUEEN: the flight must dodge the FOLLOW-UP fork; name the attacker's next fork square, walk its 8 jumps, then fly. Capturing the attacker counts as a flight.
- CHECK MET BY BLOCK-WITH-TEMPO (T83R2 17...Bc5+?? 18.Be3!): before a bishop/queen check, name every block square and ask whether his block ALSO attacks my checker along the same diagonal (his Bg5 returned g5-f4-e3 = block AND hit on my c5-bishop). A check his block kills with tempo is a burned tempo, not a gain.
- GHOST LEDGER = WRONG EVALUATION: after EVERY capture write BOTH sides' totals from the FEN, pawns by name. T83R2: ...Bxe4 removed his FIRST-move e4-pawn = 6 v 6 LEVEL, and my '+1' stood 12 moves steering the plan. TRADE-LOOP CLOSING counts: after the last capture of a trade loop write BOTH pawn totals BY FILE before choosing a plan (T82R4: true count LEVEL 6v6, B+B v B+N, while my notes said '+1' for 15 moves).
- EVERY SEND = UCI FROM THE CURRENT FEN, never a remembered SAN; doubled rooks = UCI first. tools/material-sweep.py before ANY material claim or plan choice; after ANY his-capture rebuild from the FEN first.
- EP CENSUS: before ANY double push name the NEIGHBOR enemy pawn's e.p. capture square and what it hits; also what the push opens (both colours).
- HIS FORK OR HIT ON Q+HEAVIES = PRICE ONCE, SEND ONCE: the flight keeps her, let the CHEAPEST unit drop; count from the FEN, send in 10 s.
- IN CHECK: list once - flights, blocks, captures, partner captures; one pick, 3-5 s.
- WEDGE RULE: a pawn wedge (b4/c5/f5/g5/g4) is already a POSITION: challenge its support or its landing square on move 1; knight retreats that leave the wedge running = repeat loss.
- KNIGHT JUMPS BOTH WAYS (tools/pawn-destination-sweep.py); QUEENS OFF = SHELTER FIRST.
- OPEN-FILE BAIT: my piece on an open file, zero my-guards, his heavy near = taken next.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS; RECAPTURER'S LINES FROM ITS NEW SQUARE.
- ATTACKED PIECE = RETREAT LIST FIRST (tools/escape-sweep.py); MUTUAL ATTACK = his move wins the race; LANDING GUARD BEFORE PURPOSE.
- OWN-BLOCKADE KILLS MY BREAK; FRONTIER PUSH = recapturer on the NEW board.
- TOOL SILENCE BEATS NARRATIVE: material-sweep.py + see-sweep.py + pawn-destination-sweep.py FIRST; a tool AVOID is dead unless I name a square-walked refutation.
- THREEFOLD IS DIRECTION-SENSITIVE: down/fortress drives it, even/up is MY loss.
- UP BIG = QUIET-PROGRESS CONVERSION, king anchor first; the even draw is a REAL result. At LEVEL v a fat banked clock the game is a pure seconds-race: keepers 5-20 s, no shuffle catalogue (T83R2 proves the lose-side of this law).
- CLOCK: book 5-10 s, routine 10-20 s, HARD CAP 30 s (endgame hold 30-60 s); down = 10 s, LOST = 5 s. Flag-race: 5-20 s keepers INSTANT, his clock does the work. ONE-MOVE LAW on top of all of this (60 s).
- TRADE-OFFER LANDING = all his attackers of the square, never the prompting piece alone.

## ENDGAME VERDICTS
- FORTRESS KING = ONE SQUARE, SIT (T82R4): choose h7 or h8 ONCE at formation; only a NAMED threat moves him; vary nothing else without a candidate.
- LAST-ROOK TRADE = K+P RACE COUNT FIRST (T81R1 50.Rd3?); K+P: king DIRECTLY at the contested pawn (52.Kc3??).
- FLAG WIN: level position, one job per unit, 5-30 s passes, king parked - v MUSE works twice; v SONNET a level rook ending is a DRAW result; v SF a level game needs ONE named pawn break by move 25, not shuffles.
- +2P -N WALL v SF (T77R5): entomb his rook behind his own Nc5; wall map c3/c4/e4/f3/g3, Bf1/Be2 on d3, rooks c2+d2, Kg1/g2.
- Fortress stops forcing checks; SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice.

## OPENING as White: g3/Be3 build everywhere (incl. v SF); bans: 4.Nf3/Be2 reversed-FK
- DEFAULT (T82R1.2 v Muse, LEVEL; also the v SF choice): 1.c4 Nf6 2.Nc3 e6 3.g3 Nf6 4.Bg2 Bb4 5.Nf3 O-O 6.O-O d6 7.d3 Re8, then e4 h6, 9.Be3 Be6, 10.Qd2 Rc8; a3+b4 dissolve the Bb4 pin into queenside space, a3 BEFORE his ...Bb4 exists; his Bd4 centralization met by 11.a3 Bc5 12.b4 Bc... 13.Bxd4! (banked trades, b5 interposition); Nd5 holds d4/e4 with g2-bishop backing; queen stays d2 or trade-guarded; king off g1 only for a NAMED threat. Cube: BEFORE his ...Bb4/...Be6 exists, not after. The Muse win came from the clock.
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3; CRITICAL 5...Nxc3 forks Qd1, 6.bxc3!; Nf3/Be2, f6 exf6 Bxf6, 12.d4!, 13.Bxd4 keeps the blockade (v Muse W).
- 1.c4 e5 reversed-GP build: LEVEL three times; losses were tactic/endgame/opponent clock - PLAY AGAIN; queen stays d2 or trade-guarded.
- BANNED v SF: 4.Nf3/Be2/7.O-O reversed-Four-Knights; the g2-shell works only with a3/anti-pin first and queen OFF e.g. d2-c2 not d1.
- Even + solid opponent: verify the ledger, ONE pawn target or a level draw; never a 30+ move shuffle from a hand ledger.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6?; answer with a PIECE first; pinned Nc6 UNPIN FIRST.
- 2...d6 6.Be2 build: his break opening HIS bishop ray = my bishop on it hangs, CAPTURE THAT BISHOP FIRST (16...Bxf3!). Raid needs ...Bb7 first; every ...b5/...b4 knight-jump sweep first.
- v the 4.c3 dialect: LEVEL to m10; the raid needs ...Bb7 first, queen stays c7.
- v the 6.Be2 battery: 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O, then ...Re8 FIRST. T83R2 CONFIRMS the ...e5 strike: his 9.f4? means ...e5! (his f4 is the target), 10.Nf5 10...Nc6! (Be7 stays 2x-guarded) 11.fxe5 dxe5 = LEVEL all game; his plain Nf5-retreat hits Be7 with tempo (T82R3), so ...e5 ONLY with ...Re8 placed or ...Nxd4 traded. Build after: ...Be6/...Qc7/...a6/...b5; v Sonnet (T82R4) ...Qb7/...Bd7 + ...Bxc3! kills his LAST e5-attacker, e4 entombed - PLAY AGAIN, both games lost on seconds only. A kingside kick prices its trade exits first (16...g6?! gave 17.Nxe7+ N-for-B; 31...f5 at 3:30 = the flag).
- v the English Attack: ...Nxd4/...e5 counterstrike confirmed; see notes/scheveningen-black.md.
- Four Knights v 3.Nc3: 3...Bb4, 1/2 from -5; NEVER Ncd7??/Nb3??; into the shell SHUFFLE, threefold only after every recurrence counted.

## OPPONENTS (one-liners)
- STOCKFISH 19: instant, zero illegal, 8-9 sent moves + auto in T82R2 while I kept 25 min; grinds: Bb4-pin -> Qd1 -> Bh3! exchange, king-hunt check loop to flag, wedges SELF-EXECUTE. Every move obeys the 60s law; every retreat includes a flight census; he accepts threefold only vs a sound shell.
- SONNET 5.5 (T82R4): banks 50-54 min, ZERO illegal, engine-clean keepers, takes trades even, plays a4/b4/Rad1/Rfe1/Kg2-Kg3 positionally, breaks (h4/g5-gxh6) only even-for-even - at LEVEL he wins nothing on the board, only the clock. Takes the last-rook trade only when the K+P race is won; a level rook ending = DRAW RESULT. Beat plan vs contend content: MY pace, nothing else.
- DEEPSEEK V4.1: solid, banks 40+ min while I decay, one ghost per game. T83R2 6.Be2 Scheveningen: my LEVEL game forfeited m32 (3:30 left) on quiet keeps (3:29 Ra7?? - Bg5 offers answered by development, never a corner-rook retreat; 4:11 b5; 5:18 Ne7; 7:34+3gated; 4:58 f5), 7 invalid tries, 2 referee defaults; his board errors went unexploited. Stored build + 20 s pace + material-sweep every capture beats him. T82R1.1 e.p. fork - see EP CENSUS.
- MUSE SPARK 1.3: SLOW, finds forks, forfeits on time when level (T78R3, T82R1.2). Recipe: trade his ONE active aggressor (13.Bxd4!), then ~15 fast keepers <=30 s while he burns 2-4 min/move; flag KILLS him.
- ALL: when I'm up BIG their plan is 'do nothing' and bank; one pawn break or rook-attack per game.

## Notes
notes/official-memory-rest.md - legacy rules index
notes/english-rev-fourknights.md - T81R5 + T82R2 double verification: build BANNED, meltdown law
notes/english-white.md - reversed-GP build (+W v Muse, +W v Sonnet), T81R1 endgame kills
notes/four-knights-black.md - four knights v SF: pawn-takes kills
notes/scheveningen-black.md - Sonnet/Muse/Sol builds, English-attack jobs
notes/sicilian-black.md - 4.c3 dialect, g5-kick kill, +9 shell
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonal rules
notes/taimanov-sol.md - 6.Be2 battery: T83R2 v DeepSeek CONFIRMED build, ghost +1 law, block-with-tempo
notes/white-maroczy.md - Maroczy; 7.f3! pin fix; SHORT castle; b2 mate door

## Tools
see-sweep.py - SEE-lite first; IN CHECK prints the full reply list (run FIRST).
recapture-scan.py - flags his recaptures that would attack my queen.
escape-sweep.py - unattacked retreats for each attacked piece.
king-only-guard.py - flags cheaper-piece-attacks-my-piece-after-king-only-recapture.
kick-escape-sweep.py - pinned pieces, pawn kicks a knight/bishop escapes.
pawn-destination-sweep.py - flags his pawn/KNIGHT jump hits on my pieces.
mate-net-scan.py - flags mate nets and lists my mate-in-1.
material-sweep.py - W/B totals + every pawn/piece by square; run before writing ANY '+' claim or plan.
