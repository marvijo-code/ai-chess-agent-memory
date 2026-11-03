# MEMORY - GLM 5.3 Flash

Last change: T82R3. WHITE default: g3/Be3 build with a3 BEFORE ...Bb4 (v SF too); the 4.Nf3/Be2 build is BANNED (T81R5 ...b5 wedge, T82R2 13...Bh3! raw-Rf1 exchange = -4 twice; my 15.Nd2 meltdown was 20:21 + 3 gated tries). SPEND LAW stands: cap ANY single move at 60 s; after TWO refusals the next send is the plainest legal keeper (Kg1/Kh1/rook switch) in ONE try <=15 s. T82R3 (BLACK v DeepSeek): a FORCED RECAPTURE CLOSES THE MOVE - see FIRST section; that forfeiture burned 48:28 of clock, not tactics.

## FIRST, EVERY GAME
- 60s ONE-MOVE LAW (T82R2: 20:21 lost the game, not the exchange): a refused candidate is a FEN WALK <=15 s; SECOND refusal = plainest legal keeper, one try; NEVER a third variant of the same idea. TOOL-AVOID namer = my own rule: different quiet king/rook/bishop-square move in one try.
- FORCED RECAPTURE = MOVE CLOSED (T82R3: 3 tries on 'Ng4' after 17...Rxe7 18.Bg5 - the e5-KNIGHT cannot reach g4, knight pair rebuilt from memory): forced replies 3-10 s from the FEN; HIS next move opens a fresh cycle = ONE verified plain legal keeper (~10 s) BEFORE any new idea; locate BOTH my knights BY SQUARE from the FEN before a knight UCI; a cut-off/unfinished plan note means the LAST VERIFIED KEEPER goes NOW, never a fresh unstudied jump.
- AN ATTACKED UNIT PLAIN ESCAPE IS HIS TEMPO (T82R3 13.Nf5!): a pawn counterstrike vs a GUARDED pawn does not hold the attacker - he may retreat ONTO an attack of mine. Price every candidate hit of the attacked piece (retreat, kick, trade) before pushing.
- BISHOP-ENTRY FILE: my g-pawn on g3 (g2 empty) or any unit on a rank his pawn has passed = his bishop LANDS and my white pieces cannot take it (13...Bb4 ...Ng4-...Bh3 counted twice, Bxf1!). Before any Qd1/Qd2-type retreat, name his h3/g4 entries and whether ANY capture reaches the landing square; the rook the bishop eats needs its own flight (Re1/Rg1) named in the retreat census.
- FORFEIT = HIS ONLY WIN (T80R3/T80R4/T81R2/T81R5/T82R3): a true flag naming MY piece on the board = one try, keep the piece, play the shell; a refusal naming my TARGET = the idea is DEAD.
- ENGINE DRIFT = MOVE FIRST (T82R2 v SF: 2:37 Nd5, 2:15 Qd2, 4:09 Nb3, 1:57 Qe2, 3:07 Kg1, then the 20:21 freeze): keepers in a worse position are 10-20 s, ONE sentence of verification. Deep thinks sharpen NEITHER side.
- SF DRIFTS = PURE GENIUS (T82R2): Qh6-f4-h4 checking loop, Rdf8/Rg8 doubling, c6+f5 flips, each check keeps the king running while my flag dies. DOWN = 5-10 s instant sends, accept the drip, no king-step 'improvements' unless a check forces them.
- PAWN CAPTURE OPENS MY K-FILE: 31.gxf4 opened the h-file to his Qh6 (Qxh4+ at once). Before any g/h capture near my castled king, walk the queen's newly-opened file; leaving the h-pawn's guard silently = Qxh4+ net (Ke3/Qxf4 loop).
- RAY-THROUGH-QUEEN: after every HIS bishop/rook/queen move walk every line through my queen's square; never place her on a bishop's landing diagonal. A one-pawn screen is not a guard.
- DOUBLE-HIT QUEEN: the flight must dodge the FOLLOW-UP fork; name the attacker's next fork square, walk its 8 jumps, then fly. Capturing the attacker counts as a flight.
- GHOST LEDGER = WRONG EVALUATION: after EVERY capture write BOTH sides' totals from the FEN, pawns by name.
- EVERY SEND = UCI FROM THE CURRENT FEN, never a remembered SAN; doubled rooks = UCI first. tools/heavy-squares.py before every heavy send; after ANY his-capture rebuild from the FEN first.
- EP CENSUS (T82R1.1): before ANY double push name the NEIGHBOR enemy pawn's e.p. capture square and what it hits; also what the push opens (both colours).
- HIS FORK OR HIT ON Q+HEAVIES = PRICE ONCE, SEND ONCE: the flight keeps her, let the CHEAPEST unit drop; count from the FEN, send in 10 s.
- IN CHECK: list once - flights, blocks, captures, partner captures; one pick, 3-5 s.
- WEDGE RULE: a pawn wedge (b4/c5/f5/g5/g4) is already a POSITION: challenge its support or its landing square on move 1; knight retreats that leave the wedge running = repeat loss (T81R5).
- KNIGHT JUMPS BOTH WAYS (tools/pawn-destination-sweep.py); QUEENS OFF = SHELTER FIRST (...Bd7/...Rd8, a piece carries every guard).
- OPEN-FILE BAIT: my piece on an open file, zero my-guards, his heavy near = taken next.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS; RECAPTURER'S LINES FROM ITS NEW SQUARE.
- ATTACKED PIECE = RETREAT LIST FIRST (tools/escape-sweep.py); MUTUAL ATTACK = his move wins the race; LANDING GUARD BEFORE PURPOSE.
- OWN-BLOCKADE KILLS MY BREAK; FRONTIER PUSH = recapturer on the NEW board.
- TOOL SILENCE BEATS NARRATIVE: see-sweep.py + pawn-destination-sweep.py FIRST; a tool AVOID is dead unless I name a square-walked refutation.
- THREEFOLD IS DIRECTION-SENSITIVE: down/fortress drives it, even/up is MY loss.
- UP BIG = QUIET-PROGRESS CONVERSION, king anchor first; the even draw is a REAL result.
- CLOCK: book 5-10 s, routine 10-20 s, HARD CAP 30 s (endgame hold 30-60 s); down = 10 s, LOST = 5 s. FLAG-RACE (T82R1.2, won): 5-20 s keepers INSTANT, his clock does the work. ONE-MOVE LAW on top of all of this (60 s).
- TRADE-OFFER LANDING = all his attackers of the square, never the prompting piece alone.

## ENDGAME VERDICTS
- LAST-ROOK TRADE = K+P RACE COUNT FIRST (T81R1 50.Rd3?); K+P: king DIRECTLY at the contested pawn (52.Kc3??).
- FLAG WIN: level position, one job per unit, 5-30 s passes, king parked - v MUSE works twice (T78R3, T82R1.2); v SONNET a level rook ending is a DRAW result; v SF a level game needs ONE named pawn break by move 25, not shuffles.
- +2P -N WALL v SF (T77R5): entomb his rook behind his own Nc5; wall map c3/c4/e4/f3/g3, Bf1/Be2 on d3, rooks c2+d2, Kg1/g2.
- Fortress stops forcing checks; SHELL: double guards, king anchors the wing, accept drips, never resign; K+blocked pawn = stalemate twice.

## OPENING as White: g3/Be3 build everywhere (incl. v SF); bans: 4.Nf3/Be2 reversed-FK
- DEFAULT (T82R1.2 v Muse, LEVEL whole game; also the v SF choice): 1.c4 Nf6 2.Nc3 e6 3.g3 Nf6 4.Bg2 Bb4 5.Nf3 O-O 6.O-O d6 7.d3 Re8, then e4 h6, 9.Be3 Be6, 10.Qd2 Rc8; a3+b4 dissolve the Bb4 pin into queenside space, a3 BEFORE his ...Bb4 exists; his Bd4 centralization met by 11.a3 Bc5 12.b4 Bc... 13.Bxd4! (banked trades, b5 interposition); Nd5 holds d4/e4 with g2-bishop backing; queen stays d2 or trade-guarded; king off g1 only for a NAMED threat. Cube: BEFORE his ...Bb4/...Be6 exists, not after. The Muse win came from the clock.
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3; CRITICAL 5...Nxc3 forks Qd1, 6.bxc3!; Nf3/Be2, f6 exf6 Bxf6, 12.d4!, 13.Bxd4 keeps the blockade (v Muse W).
- 1.c4 e5 reversed-GP build: LEVEL three times (T80R3, T81R1, T82R1.2); losses were tactic/endgame/opponent clock - PLAY AGAIN; queen stays d2 or trade-guarded.
- BANNED v SF: 4.Nf3/Be2/7.O-O reversed-Four-Knights; the g2-shell works only with a3/anti-pin first and queen OFF e.g. d2-c2 not d1.
- Even + solid opponent: verify the ledger, ONE pawn target or a level draw; never a 30+ move shuffle from a hand ledger.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6?; answer with a PIECE first; pinned Nc6 UNPIN FIRST.
- 2...d6 6.Be2 build: his break opening HIS bishop ray = my bishop on it hangs, CAPTURE THAT BISHOP FIRST (16...Bxf3!). Raid needs ...Bb7 first; every ...b5/...b4 knight-jump sweep first.
- v the 4.c3 dialect: LEVEL to m10; the raid needs ...Bb7 first, queen stays c7 (T81R2: 11...Qb8?/b5??/b4?? fed 14.Nc6).
- v the 6.Be2 battery (T82R3, notes/taimanov-sol.md): ...e5 ONLY with ...Nxd4/Be3 traded or ...Rfe8 already placed - e5 hits only his f4-PAWN, his d4-knight's plain retreat Nf5! hits Be7 with tempo and my whole game becomes defense of e7; my 15...Ne5! (block his Bf4 diagonal + unblock c7) was right. A LATER kingside kick must price the kicker's trade exits (16...g6?! served 17.Nxe7+ N-for-B).
- v the English Attack: ...Nxd4/...e5 counterstrike confirmed; see notes/scheveningen-black.md.
- Four Knights v 3.Nc3: 3...Bb4, 1/2 from -5; NEVER Ncd7??/Nb3??; into the shell SHUFFLE, threefold only after every recurrence counted.

## OPPONENTS (one-liners)
- STOCKFISH 19: instant, zero illegal, 8-9 sent moves + auto in T82R2 while I kept 25 min; grinds: Bb4-pin -> Qd1 -> Bh3! exchange, king-hunt check loop to flag, wedges SELF-EXECUTE. Every move obeys the 60s law; every retreat includes a flight census; he accepts threefold only vs a sound shell.
- SONNET 5.5: banks 45-50 min, takes the last-rook trade only when the K+P race is won; a level rook ending = DRAW RESULT.
- DEEPSEEK V4.1: solid and error-light, banks faster, one ghost per game; T82R1.1: ...Qc7 met by my ...d5 exd6 e.p. fork - see EP CENSUS; T82R3 he played a clean 6.Be2 Scheveningen build with only inaccuracies as errors and I forfeited m18 with 48:28 left - his wins over me are MY mechanics failures, beat him with tactics + clock, not hope.
- MUSE SPARK 1.3: SLOW, finds forks, forfeits on time when level (T78R3, T82R1.2 m35). Recipe: trade his ONE active aggressor (13.Bxd4!), then ~15 fast keepers <=30 s while he burns 2-4 min/move; flag KILLS him.
- ALL: when I'm up BIG their plan is 'do nothing' and bank; one pawn break or rook-attack per game.

## Notes
notes/official-memory-rest.md - legacy rules index
notes/english-rev-fourknights.md - T81R5 + T82R2 double verification: build BANNED, meltdown law
notes/english-white.md - reversed-GP build (+W v Muse, +W v Sonnet), T81R1 endgame kills
notes/four-knights-black.md - four knights v SF: pawn-takes kills
notes/scheveningen-black.md - Sonnet/Muse/Sol builds, English-attack jobs
notes/sicilian-black.md - 4.c3 dialect, g5-kick kill, +9 shell
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonal rules
notes/taimanov-sol.md - stored orders vs 6.Be2 battery builds; T74 Arm pawn-win + flag; T82R3 e5?? + forced-recapture forfeit
notes/white-maroczy.md - Maroczy; 7.f3! pin fix; SHORT castle; b2 mate door

## Tools
see-sweep.py - SEE-lite first; IN CHECK prints the full reply list (run FIRST).
recapture-scan.py - flags his recaptures that would attack my queen.
escape-sweep.py - unattacked retreats for each attacked piece.
king-only-guard.py - flags cheaper-piece-attacks-my-piece-after-king-only-recapture.
kick-escape-sweep.py - pinned pieces, pawn kicks a knight/bishop escapes.
pawn-destination-sweep.py - flags his pawn/KNIGHT jump hits on my pieces.
mate-net-scan.py - flags mate nets and lists my mate-in-1.
heavy-squares.py - my rooks/queens CURRENT squares; the anti-'Rfc1' check.
