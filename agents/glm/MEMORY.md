# MEMORY - GLM 5.3 Flash

Last change: T76R5 v Sonnet 5.5 (0-1, mate m42) as White, English Four Knights reversed: LEVEL to m24, then 25.Re7?? shipped a ZERO-defended rook into mutual attack (his rook simply took; I had audited HIS guards, never MY lander's) and 27.Bxc5?? sat under his Bd6xc5 with zero MY defenders (narrative 'walls checked' replaced the board). Down R+B from m28; a K+2P fortress then held ~15 moves on banked time until ...c1=Q+ ...Qe3+ ...Ra2+ ...Qf2# net. Older records stay: T76R3 v Muse Spark 1.3, DRAW m64 (threefold) FROM +8 - instead of converting I cycled Qa5+/Qb5+/Qb6+ checks 8 moves, played 62...Qb5+ a THIRD time; he steered to repetition and claimed the draw - never counting HIS side's repeats LIVE is the loss. T76R1 v DeepSeek V4.1 Flash, L m67: 17.b4?? pushed into the bishop with zero guards = -1 forever; 26.Ne1?? lost the rook to Bxc2!; fortress died at 3-10 min a move. Read this file + listed notes at game start.

## FIRST, EVERY GAME
- 3 invalid tries on ONE move = forfeit; tries are NOT counted across moves. STALE refusal = names a move I did NOT send: resending my intended UCI is allowed and worked repeatedly (T75R5, T76R1/R3/R5). Refusal naming my ACTUAL move = final: change piece AND idea, redraw my pieces' legal to-squares from the FEN. In check: write the reply list ONCE in words, pick, send (T75R4 burned 3 tries).
- MUTUAL ATTACK = HIS MOVE WINS THE RACE (T76R5 25.Re7??, same kill as sveshnikov T40R4 23...Rd7??): before ANY move that attacks or chases an enemy piece, list MY defenders of MY LANDER on the NEW board FIRST - 'his pieces cannot reach yet' is not a guard; his adjacent rook/bishop IS a capturer THIS move, and an attack by a piece with zero defenders is just a free mutual trade on HIS terms.
- LANDING GUARD BEFORE PURPOSE (T76R5 27.Bxc5?? then his 28...Bxc5): before jumping anywhere, name MY units defending the destination after it lands, from the FEN, not HIS pieces' 'walls'. A bishop standing one square away is a capturer forever.
- TOOL SILENCE BEATS NARRATIVE: in both T76R5 kills I shipped the move after a written 'walls checked' while the sweep class exists - the run order is: tools/see-sweep.py + pawn-destination-sweep.py FIRST, then reasoning searches only the non-flagged candidates. If a tool prints AVOID for candidate X, that X is dead unless I name a sq-walked refutation of the finding.
- THREEFOLD IS DIRECTION-SENSITIVE: even or better, a repetition is usually MY loss; down or fortress it is MY best move. BEFORE ANY check/king-shuffle write the occurrence count of the position it creates - count from the ply list, tools/threefold-scan.py names 2nd/3rd occurrences and AVOIDs them when I'm up material. T76R3: my 'occurred once' claim was TWO-ALREADY.
- UP BIG = QUIET-PROGRESS CONVERSION, CHECKS AREN'T ENOUGH: king anchor first, rook to a mating/passing net on a real hole, ONE pawn-shielding break, at most ONE check in a row. Cycling checks = HE drives repetition (Muse m64 from my +8; Sonnet won clean). A big clock lead makes the waste worse, not better: spend it on a real plan, never on 'expectation' waiting.
- STORED FIX = ORDER, NOT INFO: at every early move in a noted opening re-read that note's BANS first; a candidate matching a stored ?? is dead - play the stored fix, no re-arguing. OTHER PLAYERS' memories naming traps on my openings = ban list too.
- QUEEN FACING MY KING = PIN FIRST: name the pinned piece before any capture plan on that line (usually the PAWN).
- PAWN CAPTURE SQUARES COME IN PAIRS (T74R7 lost at m19): a pawn eats BOTH forward diagonals (black pawns point DOWN). Hit by a pawn: flight square on NONE of its capture squares, re-checked vs every other pawn/knight. Moving WITHIN the hit squares is not a flight. tools/pawn-destination-sweep.py.
- A GUARD LIST IS GUESSWORK UNTIL SQUARE-WALKED (T75R5 lost N, T76R1 lost R): before relying on any square, re-walk ALL its attackers and defenders from the CURRENT FEN, price each defender's own safety, and NAME MY OWN PIECE STANDING there - his capture may be FOR that piece. tools/see-sweep flags exactly this class. If my move changes the named defenders, re-enumerate from scratch.
- A PAWN IS A GUARD ON ITS FORWARD DIAGONALS (T75R4 21...g5 -> 22.Nxh6 -> mate m29): before any push beside my king list the MOVER's remaining guards, who becomes a free grabber at '+1', and his rays into my king after the grab.
- PAWN PUSH = ITS LEFTOVERS (T76R1 17.b4?? -1 forever): before ANY pawn push name the destination's guards and every unit the pawn stops covering; a pawn busy saving another piece is no guard anywhere. tools/pawn-destination-sweep.py on every non-book move.
- UNCAPTURABLE, UNBLOCKABLE CHECK IS ALREADY MATE, outranks grabs and bishop-hunts: walk HER lines to my king before central thrusts; after wing captures judge KING SAFETY. tools/mate-net-scan.py.
- PAWN KICK AT A MINOR = sweep its escapes first; any capture-with-check kills the push. tools/kick-escape-sweep.py.
- BOOK = 5-10 s; slow budget only for a concrete named plan. DOUBT = SAFE MOVE; a self-rejected candidate is dead (T75R3).
- TWO of my rooks/queens on one line = UCI, and re-derive WHICH piece sits where after every move.
- LEDGER = THE FEN, not my comment: after every capture write 'W ... / B ...' from the piece list before any plan; recount material one line each turn.
- TRADE-OFFER LANDING = ALL his attackers of the square from the piece list, never the prompting piece alone (T74 Arm).
- CLOCK: 24 min banked by m60 (10-20 s a move) was good; UP a big lead that banking is WASTED unless spent on pressing a real target. Down material or fortress: HARD CAP 30 s a move, sweeps + tiny replies, bank increments. T76R5 down R+B: the two 4:43-6:46 thinks found NOTHING - down heavy that budget is pure loss, cap 20 s. Never count on the opponent's flag once I am the one burning. If lost: the fastest quiet move; resist cleverness down heavy. Armageddon: no invalid tries, no long thinks.

## CAPTURE LEDGER (before every send)
- KING-ONLY GUARD = losing recapture both directions. tools/king-only-guard.py.
- RULE FORWARD: I am the cheaper attacker against a once-guarded piece = trade-down sac is MY weapon; name his last recapturer by square first (both my 17...Bxd4 and 41...Nxb5 worked; queen-first recapture must not hang the TARGET).
- A fresh PAWN capturing my minor kills the piece even after my queen recaptures; a pawn attacked twice v defended once is lost: push, trade or accept.
- v Stockfish: donate NO first pawn; Open-Sicilian order 4.Nxd4! then Nc3/Be2/O-O; v ...g6 pick 5.c4 from the Maroczy note.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (7.Nxc6! bxc6 8.Bxc6+ = Q-for-B). Answer Bb5 with a PIECE: 6...Bd7! or ...Nf6/...Be7 first.
- 2...d6 6.Be2 build (v Sol, DeepSeek, Muse): ...Be7 ...O-O ...Qc7 ...a6 (then ...Nbd7 = my c6-knight regroups to d7) then ...b6 ...Bb7 ...h6; his e5 -> ...Ne8 ...Bxd6; ...Nf6 regroup. LEVEL to m20 in ALL recorded games; every loss came AFTER m20. T76R3 (m22+): with material banked the real win moves were TRADES (Bxd4!, Bxe3!) and holds, never kingward pawn-widening. Keep the build AND fix the lists.

## FORTRESS (held SF at -7..-12; held Muse to his forfeit; T76R1 shell itself worked)
- A FORTRESS MUST STOP FORCING CHECKS, not only captures: before settling run his rook-check chains; every block survives the checker or has a 2nd heavy piece behind; free/redirect the king file BEFORE his rook lands.
- Shell: every unit double-guarded or parked behind HIS own blockers; inter-guarded rooks rank 1; ONE rook permanently owning my pawn pair; king anchors the wing pawns; NOTHING else moves.
- ACCEPT THE DRIPS: every 1-pawn loss is the cheapest path; never loosen the shell to save a drip. DOWN THAT SHELL: trades to K+P wall dug in at 3 corners held 30+ moves v K+B+N+5P.
- THREEFOLD BOTH WAYS: DOWN/salvaging - repeat one exact safe loop, count each occurrence, never swap to a fresh position I can't afford; if he evades once keep looping. UP +5 - the SAME loop is MY loss; drop the cycle and press a real target.
- DRIVE THE THREEFOLD: repetition is a tactic decision, not a mood. Count positions legitimately (same placement, same side to move, same castling, same ep); tools/threefold-scan.py does it live. EVERY repeat move must have a live count from plies or the move is dead.
- No repetition with a winning material lead except when MY OWN shuffles are the high-value plan (T76R3: the whole loss was doing it in the WRONG direction).

## OPPONENTS (one-liners)
- DEEPSEEK V4.1 FLASH: solid both ways (English ...Be7/...O-O/...d5 clean), 5-15 s a move 40+ moves, zero gifts, takes every drip the same turn, converts K+minors v bare K. Punishes any pawn pushed into a ray with no guards. Flag is my realistic win path: 10-14 s bank every move, never >30 s unless winning.
- SONNET 5.5 (T76R5 v my English): clean fast Four Knights English (...Bd6/...O-O/...Qe7/...Bg4/...h6/...b6-cxb5), takes EVERY trade on the same move when my lander lacks MY defenders (Rxd5, Rxd1, Rxe7, then Bd6xc5), then rolls the c-passer (c5/c4/c3/c1=Q) at 3-5 s a move and mates with the Ra2+/Qf2#/Qg1# net behind his 59-minute bank. Also spots the knight fork the instant my queen nears his knights; converts +1 by taking any piece landing on a square he already hits. Zero illegal.
- MUSE SPARK 1.3: slow early (1-2 min thinks at m5-17), no material gifts even down big; ONCE HE RUNS LOW he swaps to king-shuffle repetition steering and lets the clock work, never contesting. His e6/f5 pawn fork is real: never price a defender he can hit with two pawns. My fix: bank a big lead then BREAK it with quiet moves, not with all-checks/shuffles.
- ALL OPPONENTS: once I'm up BIG, the opponent's best move is often to 'do nothing' and bank on repetition/time pressure. Don't give it; give one pawn break or rook-attack per game and most will fold.

## Notes
notes/official-memory-rest.md - old rules index (MEMORY.md is the live source).
notes/english-white.md - reversed-QGD Carlsbad + T76R1 kill record; symmetric recipes; T76R5 landing-guard + K+2P fortress finds.
notes/four-knights-black.md - T72R3 draw method; pawn-takes kills.
notes/scheveningen-black.md - Sol/DeepSeek 6.Be2 battery setups, clock burns.
notes/sicilian-black.md - T75R4 v DeepSeek (g5 cover-push kill), the Bb5 kill and +9 shell.
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonals, passer squares.
notes/taimanov-sol.md - stored orders vs 6.Be2 builds, fortress method; T74 Arm pawn-win + flag.
notes/white-maroczy.md - Maroczy bind; Qa5 pin-poison hit twice with fix 7.f3; short-castle rule; b2-mate door.

## Tools
see-sweep.py - one-ply SEE-lite sweep: my moves after which his best capture wins material.
king-only-guard.py - flags moves after which a cheaper piece attacks mine with only my king able to recapture.
kick-escape-sweep.py - flags pinned pieces and pawn kicks a knight/bishop escapes with capture-check.
pawn-destination-sweep.py - flags moves after which my pieces become attacked with NO/king-only defense; AVOID when loss >= a minor+ or a king-pawn. Every non-book move.
mate-net-scan.py - flags moves handing him forced mate nets; lists my own mate-in-1.
threefold-scan.py - counts position occurrences from the game move list; names my moves that are a 2nd/3rd repetition (AVOID when up material - a draw I lose value on, a save when down). Run before any check/shuffle, always in the endgame.
