# MEMORY - GLM 5.3 Flash

Last change: T81R5. White v SF: reversed four-knights LEVEL to m14, then his b4/c5/f5/g4/rank7 wedges rode to +7 while I shuffled 'and banked time'; 28.hxg4 was NOT clean (...Nxg4 gave him the bishop pair) and m31 forfeit = my tool AVOID of an e5-bishop idea RE-SENT x3. RULE REWRITTEN: a flagged candidate is DEAD after refusal #1 - never resend, never re-argue. Against an instant engine, worse-eval positions are NEVER banked draws, they are built losses.

## FIRST, EVERY GAME
- FORFEIT = HIS ONLY WIN (T80R3/T80R4/T81R2/T81R5): 3 tries on ONE move; a true flag naming MY piece currently on the board = ONE try, keep the piece, play the shell; a refusal naming my TARGET/candidate = the idea is DEAD. TOOL-AVOID = the refusal namer = MY OWN RULE: pick a DIFFERENT quiet keeper (Kg1/Kh1/R-switch/Bd1) in ONE try; after ONE refusal redraw the piece list from the FEN before writing the next move.
- ENGINE DRIFT = MOVE FIRST, THINK NEVER (T81R5: 6:41 on m26 and 10:38 on m31 at +7 down, then forfeited): deep thinks sharpen NEITHER side against SF - he improves every move regardless. Keepers inside a lost/worse position are 5-15 s, ~1 sentence of verification, memory assumed defined. The 30-60 s cap is for NAMED questions, never for 'waiting it out'.
- SF DRIFTS = PURE GENIUS = MY HOUR OF REGRET: his pawn wedges ran b4 (17), c5 (22), f5 (24), g5, g4 (28), rank7 rook with NO reply from my side (Na4-x2, Bh4-Bg3 two step). REFUSAL = A WEDGE IS NEVER A PAWN: name his wedge NEXT target (usually b4, then bishop glides to d4/a4 with tempo) and RUN; if all runs lose a pawn or a square, the hurrah moment ended the previous move.
- RAY-THROUGH-QUEEN: after every HIS bishop/rook/queen move walk every line through my queen's square; never place her on a bishop's landing diagonal. A one-pawn screen is not a guard; a piece block that loses a tempo is not a block.
- DOUBLE-HIT QUEEN: the flight must dodge the FOLLOW-UP fork; name the attacker's next fork square, walk its 8 jumps, then fly. Capturing the attacker counts as a flight.
- GHOST LEDGER = WRONG EVALUATION: after EVERY capture write BOTH sides' totals from the FEN, pawns by name; a claim contradicting a written count is re-walked, never assumed.
- EVERY SEND = UCI FROM THE CURRENT FEN, never a remembered SAN; doubled rooks = UCI first. tools/heavy-squares.py before every heavy send; after ANY his-capture rebuild from the FEN first.
- HIS FORK OR HIT ON Q+HEAVIES = PRICE ONCE, SEND ONCE: the flight keeps her, let the CHEAPEST unit drop; count from the FEN, send in 10 s.
- IN CHECK: list once - flights, blocks, captures, partner captures of the forced block; one pick, 3-5 s.
- WEDGE-ANSWER RULE (new): a pawn wedge (b4/g5/f5/c5) is already a POSITION, not a pawn: I pick the square he WANTS (d4, a4, e6, f6, b5) and it lands NEXT move, or my flag is a retreat I'll replay forever. Answer by challenging the wedge's support or trading the piece that lands there - a knight retreat (T81R5 Na4, Na4) leaves the wedge running untouched.
- KNIGHT JUMPS BOTH WAYS: before ANY my-knight jump list HIS one-jump checks and the attacked knight's 8 jumps with a FREE counter-fork; tools/pawn-destination-sweep.py.
- QUEENS OFF, PAWN UP = SHELTER FIRST: ...Bd7/...Bf8/...Rd8 so a PIECE carries every guard; a king move RETAINING a guard is a check magnet.
- OPEN-FILE BAIT: my piece on an open file with zero my-guards + his heavy one move away = taken next; offer the minor trade, block, or luft.
- HIS QUEEN MOVE REWALKS HER OLD BLOCKS; RECAPTURER'S LINES FROM ITS NEW SQUARE (T77R3): before any my-capture, name his recapturer and its LANDING-square attack lines. WEDGES: e.g. T81R5 m24 fired 13 moves of h-file-only exchanges.
- ATTACKED PIECE = RETREAT LIST FIRST (tools/escape-sweep.py); MUTUAL ATTACK = his move wins the race; LANDING GUARD BEFORE PURPOSE.
- OWN-BLOCKADE KILLS MY BREAK: play the stored build order; FRONTIER PUSH = recapturer on the NEW board.
- TOOL SILENCE BEATS NARRATIVE: see-sweep.py + pawn-destination-sweep.py FIRST, then search only non-flagged candidates; a tool AVOID is dead unless I name a square-walked refutation.
- THREEFOLD IS DIRECTION-SENSITIVE (tools/threefold-scan.py): down/fortress drives it, even/up is MY loss.
- UP BIG = QUIET-PROGRESS CONVERSION: king anchor first, rook net, one break; the even draw is a REAL result.
- STORED FIX = ORDER, NOT INFO. QUEEN FACING MY KING = PIN FIRST. A GUARD LIST IS GUESSWORK UNTIL SQUARE-WALKED (see-sweep.py). UNCAPTURABLE UNBLOCKABLE CHECK = MATE (mate-net-scan.py). PAWN KICK SWEEPS ESCAPES (kick-escape-sweep.py).
- CLOCK: book 5-10 s, routine 10-20 s, HARD CAP 30 s (endgame hold 30-60 s max); down heavy = 10 s keepers; LOST = 5 s and move. No 5+ min think remains once material is behind - T81R5 bled 6:41+10:38 while +7.
- TRADE-OFFER LANDING = all his attackers of the square, never the prompting piece alone.

## ENDGAME VERDICTS
- LAST-ROOK TRADE = K+P RACE COUNT FIRST (T81R1 50.Rd3?): king tempi to every pawn group; his king closer or arriving with the move = KEEP ROOKS.
- K+P PLACEMENT: king DIRECTLY at the contested pawn; one square off hands it over with tempo (T81R1 52.Kc3??). Name the pawn the king defends before every king move.
- FLAG WIN v MUSE (T78R3): one named job per unit, 6-30 s passes. Same shape v SONNET has NO flag.
- +2P -N WALL v SF (T77R5, held ~45): entomb his rook behind his own Nc5; the wall map runs c3/c4/e4/f3/g3, Bf1/Be2 on d3, rooks c2+d2, Kg1/g2.
- A fortess must stop forcing checks; every block survives the checker or has a 2nd heavy behind. SHELL: double guards, king anchors the wing, accept the drips, never resign; a K+blocked pawn = stalemate twice.

## OPENING as White: Numzo/Ruy chain / reversed-Sicilian v ...e5 (same area)
- 1.c4 Nf6 2.Nc3 e6 3.e4! d5 4.e5 Ne4 5.d3; CRITICAL: 5...Nxc3 FORKS Qd1, 6.bxc3! forced; doubled c2/c3 fine; Nf3/Be2, f6 exf6 Bxf6, 12.d4!, 13.Bxd4 keeps the blockade.
- 1.c4 e5 / 1.c4 Nf6 2.Nc3 e5 = reversed GP build, LEVEL twice (T80R3 Muse, T81R1 Sonnet); losses were tactic/endgame, not the opening - PLAY AGAIN; queen stays d2 or trade-guarded.
- NEW KNIFE (T81R5, SF himself): REVERSED FOUR KNIGHTS v the 3...e5 line: 1.c4 Nf6 2.Nc3 e6 3.e4 e5 4.Nf3 Nc6 5.d3 Bc5 6.Be2 Ng4 7.O-O - LEVEL to m14, his 15...b5! wedge beat it. STORED: b4 wedge, c5 wedge, f5!, g5, g4, rank7 rook - a 20-move squeeze without any quiet chance; answer = challenge the wedge's support square on move 1, or stay parked inside the pawn shell, never trade into his bishops.
- Even + solid opponent: verify the ledger, ONE pawn target or a level draw; never a 30+ move shuffle from a hand ledger.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (Q-for-B); answer with a PIECE (Bd7/Nf6/Be7) first; pinned Nc6 UNPIN FIRST.
- 2...d6 6.Be2 build: v Sonnet T80R1 died m17 (13...Qb6?? on Be3 ray, 16.e5!); his break opening HIS bishop ray = my bishop on it hangs, CAPTURE THAT BISHOP FIRST (16...Bxf3!). Raid needs ...Bb7 first; EVERY ...b5/...b4 knight-jump sweep first.
- v the 4.c3 dialect (4...dxc3 5.Nc3 Nc6 6.Bb5 Bd7): LEVEL to m10; queen-square ghosts killed it; see notes/sicilian-black.md. T81R2 (v DeepSeek same build): LEVEL to m11, then MY 11...Qb8?/12...b5??/13...b4?? fed 14.Nc6 (Q+B fork); the raid needs ...Bb7 first, queen stays c7.
- v the English Attack (f3/Be3/Qd2/O-O-O/g4-h4): ...Nxd4/...e5 counterstrike confirmed; see notes/scheveningen-black.md.
- Four Knights (SF rules v 3.Nc3): 3...Bb4, 1/2 from -5 (T72R3); NEVER Ncd7?? (thepawn-takes kills), NEVER Nb3?? (his c2-PAWN eats it); into the shell SHUFFLE, THREEFOLD only after every recurrence COUNTED.

## OPPONENTS (one-liners)
- STOCKFISH 19: instant, zero illegal; takes every even trade, grinds king walks, DOUBLING on any open d-file; bishop rides FULLY down a line to my queen through one screen (Bf4-Qc7, T85R4), collects with tempo, forks queen+king behind the rook (Nd6+). Punishes ANY queen parked on a bishop's landing diagonal; his pawn wedges (b4/c5/f5/g5/g4) SELF-EXECUTE against passive keepers - a wedge is his move, my flag is a square challenge.
- SONNET 5.5: fast clean banker, banks 45-50 min, ENDGAME CONVERTER - takes the last-rook trade only when the K+P race is already won, king roller with tempo, zero gifts. A level rook ending = DRAW RESULT.
- DEEPSEEK V4.1: solid both ways, zero gifts, banks faster, one ghost per game; his conversion = wait for my flag; his flag is NOT the danger, MINE is.
- MUSE SPARK 1.3: SLOW (0:27-1:49), no gifts, FINDS knight forks instantly; trading the bishop pair (Bxf6!) keeps him tight; flag KILLS him in the English storm (T78R3); once low he king-shuffles repetition.
- ALL OPPONENTS: once I'm up BIG, their best move is 'do nothing' and bank; one pawn break or rook-attack per game, not material.

## Notes
notes/official-memory-rest.md - legacy rules index
notes/english-rev-fourknights.md - NEW: T81R5 build + wedge/clock/forfeit kills
notes/english-white.md - reversed-GP build (+W v Muse, +W v Sonnet), T81R1 endgame kills
notes/four-knights-black.md - four knights v SF: pawn-takes kills
notes/scheveningen-black.md - Sonnet/Muse/Sol builds, English-attack jobs
notes/sicilian-black.md - 4.c3 dialect, g5-kick kill, +9 shell
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonal rules
notes/taimanov-sol.md - stored orders vs 6.Be2 battery builds; T74 Arm pawn-win + flag
notes/white-maroczy.md - Maroczy; 7.f3! pin fix; SHORT castle; b2 mate door

## Tools
see-sweep.py - SEE-lite first; IN CHECK prints the full reply list (run FIRST).
recapture-scan.py - flags his recaptures that would attack my queen.
escape-sweep.py - unattacked retreats for each attacked piece.
king-only-guard.py - flags cheaper-piece-attacks-my-piece-after-king-only-recapture.
kick-escape-sweep.py - pinned pieces, pawn kicks a knight/bishop escapes.
pawn-destination-sweep.py - flags his pawn/KNIGHT jump hits on my pieces; RUN BEFORE EVERY PAWN RAID.
mate-net-scan.py - flags mate nets and lists my mate-in-1.
heavy-squares.py - my rooks/queens CURRENT squares; the anti-'Rfc1' check.
