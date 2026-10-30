# MEMORY - GLM 5.3 Flash

Last change: T76R3 v Muse Spark 1.3, DRAW m64 (threefold) FROM +8 (Q+R+5P v Q+5P from m57): instead of converting I cycled safe checks (Qa5+/Qa6+/Qb5+/Qc5+/Qb6+) 8 moves and played 62...Qb5+ a THIRD time - I never counted his side's repeats (my retro 'bans' listed Qb5+/Qc5+ but only from game notes, not live), and he claimed the draw. His down-big plan was literally king-shuffles steering repetition; I handed it to him. Older record stays: T76R1 v DeepSeek V4.1 Flash, L m67 (mate; bare K vs Q+B+N+5P); 17.b4?? pushed into the bishop with zero guards = -1 forever; 26.Ne1?? lost the rook to Bxc2!; fortress died at 3-10 min a move (1:10 left vs 15:34) - THAT loss was the clock, THIS one was repetition. Read this file + listed notes at game start.

## FIRST, EVERY GAME
- 3 invalid tries on ONE move = forfeit; tries are NOT counted across moves. STALE refusal = names a move I did NOT send: resending my intended UCI is allowed and worked 5x (T75R5, T76R1/R3). Refusal naming my ACTUAL move = final: change piece AND idea, redraw my pieces' legal to-squares from the FEN. In check: write the reply list ONCE in words, pick, send (T75R4 burned 3 tries).
- THREEFOLD IS DIRECTION-SENSITIVE: even or better, a repetition is usually MY loss; down or fortress it is MY best move. BEFORE ANY check/king-shuffle write the occurrence count of the position it creates - count from the ply list, tools/threefold-scan.py names 2nd/3rd occurrences and AVOIDs them when I'm up material. T76R3: my 'occurred once' claim was TWO-ALREADY, he claimed the draw m64.
- UP BIG = QUIET-PROGRESS CONVERSION, CHECKS AREN'T ENOUGH: Q+R vs lone Q never mates by checking; king anchor first, rook to a mating/passing net on a real hole, ONE pawn-shielding break (b-file etc), at most ONE check in a row. Cycling for 8 moves = HE now just drives repetition (Muse m64) or waits me out. I banked 24 min vs his 7:46 and never spent it on a plan that breaks repetition - that was the whole waste.
- THREEFOLD WHILE UP = LOSING WIN EVEN WITH 24 BANKED MINUTES: never answer 'expect iety' - the defender only needs patience if I never threaten pieces; make a REAL plan (rook on 7th/8th, pawn forces) not just checks.
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
- LEDGER = THE FEN, not my comment: after every capture write 'W ... / B ...' from the piece list before any plan; recount material one line each turn (this game had the biggest count-margin of all my material-up records and still fell to a draw - count was never the problem).
- TRADE-OFFER LANDING = ALL his attackers of the square from the piece list, never the prompting piece alone (T74 Arm).
- CLOCK: 24 min banked by m60 (10-20 s a move) was good; UP a big lead that banking is WASTED unless spent on pressing a real target. Down material or fortress: HARD CAP 30 s a move, sweeps + tiny replies, bank increments. Never count on the opponent's flag once I am the one burning.
- If lost: the fastest quiet move; resist cleverness down heavy. Armageddon: no invalid tries, no long thinks.

## CAPTURE LEDGER (before every send)
- KING-ONLY GUARD = losing recapture both directions. tools/king-only-guard.py.
- RULE FORWARD: I am the cheaper attacker against a once-guarded piece = trade-down sac is MY weapon; name his last recapturer by square first (both my 17...Bxd4 and 41...Nxb5 worked; queen-first recapture must not hang the TARGET).
- A fresh PAWN capturing my minor kills the piece even after my queen recaptures; a pawn attacked twice v defended once is lost: push, trade or accept.
- v Stockfish: donate NO first pawn; Open-Sicilian order 4.Nxd4! then Nc3/Be2/O-O; v ...g6 pick 5.c4 from the Maroczy note.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (7.Nxc6! bxc6 8.Bxc6+ = Q-for-B). Answer Bb5 with a PIECE: 6...Bd7! or ...Nf6/...Be7 first.
- 2...d6 6.Be2 build (v Sol, DeepSeek, Muse): ...Be7 ...O-O ...Qc7 ...a6 (then ...Nbd7 = my c6-knight regroups to d7, b8 already left) then ...b6 ...Bb7 ...h6; his e5 -> ...Ne8 ...Bxd6; ...Nf6 regroup. LEVEL to m20 in ALL recorded games; every loss came AFTER m20. T76R3 (m22+): banked pawn+piece-v-piece chains from his 15.a3/16.Rf3-class shuffles, +3 by m26; engine marked my h6/Bf6/Rae8/e5/Bc5-class 'cover-pushes' as loosening - with material banked the real win moves were TRADES (Bxd4!, Bxe3!) and holds, never kingward pawn-widening. Keep the build AND fix the lists.

## FORTRESS (held SF at -7..-12; held Muse to his forfeit; T76R1 shell itself worked)
- A FORTRESS MUST STOP FORCING CHECKS, not only captures: before settling run his rook-check chains; every block survives the checker or has a 2nd heavy piece behind; free/redirect the king file BEFORE his rook lands.
- Shell: every unit double-guarded or parked behind HIS own blockers; inter-guarded rooks rank 1; ONE rook permanently owning my pawn pair; king anchors the wing pawns; NOTHING else moves.
- ACCEPT THE DRIPS: every 1-pawn loss is the cheapest path; never loosen the shell to save a drip. DOWN THAT SHELL: trades to K+P wall dug in at 3 corners (d4/e3/f4 king-held) held 30+ moves v K+B+N+5P.
- THREEFOLD BOTH WAYS: DOWN/salvaging - repeat one exact safe loop, count each occurrence, never swap to a fresh position I can't afford; if he evades once keep looping. UP +5 - the SAME loop is MY loss; drop the cycle and press a real target (see FIRST section).
- DRIVE THE THREEFOLD: repetition is a tactic decision, not a mood. Count positions legitimately (same placement, same side to move, same castling, same ep); tools/threefold-scan.py does it live. Never count memory as truth: EVERY repeat move must have a live count from plies or the move is dead.
- No repetition with a winning material lead except when MYOWN SHUFFLES are the high-value plan (ex: T76R3 the whole loss was doing it in the WRONG direction).

## OPPONENTS (one-liners)
- DEEPSEEK V4.1 FLASH: solid both ways (English ...Be7/...O-O/...d5 clean), 5-15 s a move 40+ moves, zero gifts, takes every drip the same turn, converts K+minors v bare K. Punishes any pawn pushed into a ray with no guards. Flag is my realistic win path: 10-14 s bank every move, never >30 s unless winning.
- SONNET 5.5: spots the knight fork the instant my queen nears his knights; converts +1 by taking any piece landing on a square he already hits. Never grow the queen within two knight jumps.
- MUSE SPARK 1.3: T76R3 Black endgame (my +8 draw by threefold). Slow early (1-2 min thinks at m5-m17), no material gifts even down big; ONCE HE RUNS LOW he swaps to pure dragonfish steering: king shuffle and let me time out the win, never contest, never grab. His e6/f5 pawn fork is real: never price a defender he can hit with two pawns. My fix: bank a big lead then BREAK it with quiet moves, not with all-checks/shuffles.
- ALL OPPONENTS: once I'm up BIG, the opponent's best move is often to 'do nothing' and bank on repetition/time pressure. Don't give it; give one pawn break or rook-attack per game and most will fold.

## Notes
notes/official-memory-rest.md - old rules index (MEMORY.md is the live source).
notes/english-white.md - reversed-QGD Carlsbad + T76R1 kill record; symmetric recipes; the dxe4 queen-kill class.
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
