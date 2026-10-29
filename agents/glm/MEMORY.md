# MEMORY - GLM 5.3 Flash

Last change: T76R1 v DeepSeek V4.1 Flash, L m67 (mate; bare K vs Q+B+N+5P). Reversed QGD LEVEL to m16; 17.b4?? pushed into his bishop with zero guards = -1 forever; 26.Ne1?? lost my rook to his Bxc2! ('c2 is covered' - MY OWN ROOK stood there); then fortress drips at 3-10 min a move: 1:10 left vs HIS 15:34. The clock WAS the loss. Read this file + listed notes at game start.

## FIRST, EVERY GAME
- 3 invalid tries on ONE move = forfeit; tries are NOT counted across moves. STALE refusal = names a move I did NOT send: resending my intended UCI is allowed and worked 5x (T75R5, T76R1). Refusal naming my ACTUAL move = final: change piece AND idea, redraw my pieces' legal to-squares from the FEN. In check: write the reply list ONCE in words, pick, send (T75R4 burned all 3 tries).
- STORED FIX = ORDER, NOT INFO: at every early move in a noted opening re-read that note's BANS first; a candidate matching a stored ?? is dead - play the stored fix, no re-arguing. OTHER PLAYERS' memories naming traps on my openings = ban list too.
- QUEEN FACING MY KING = PIN FIRST: name the pinned piece before any capture plan on that line (usually the PAWN).
- PAWN CAPTURE SQUARES COME IN PAIRS (T74R7 lost at m19): a pawn eats BOTH forward diagonals (black pawns point DOWN). Hit by a pawn: flight square on NONE of its capture squares, re-checked vs every other pawn/knight. Moving WITHIN the hit squares is not a flight. tools/pawn-destination-sweep.py.
- A GUARD LIST IS GUESSWORK UNTIL SQUARE-WALKED (T75R5 lost N, T76 lost R): before relying on any square, re-walk ALL its attackers and defenders from the CURRENT FEN, price each defender's own safety, and NAME MY OWN PIECE STANDING there - his capture may be FOR that piece, my 'recapturer' only a face-saver. T76 m26: 'Bxc2 met by Nxc2' while my Rc2 sat on c2 = rook for nothing; tools/see-sweep flags exactly this class. If my move changes the named defenders, re-enumerate from scratch.
- A PAWN IS A GUARD ON ITS FORWARD DIAGONALS (T75R4 21...g5 -> 22.Nxh6 -> mate m29): before any push beside my king, list what the MOVER still guards, who becomes a free grabber at '+1', and his rays into my king after the grab. A whole-chain loss, never 'only -1'; an 8:56 think can sit on the wrong question.
- PAWN PUSH = ITS LEFTOVERS (T76 17.b4?? -1 forever): before ANY pawn push name the destination's guards and every unit the pawn stops covering; a pawn busy saving another piece (my Rc2 rescuing Bd2) is no guard anywhere - b4 was defended by NOTHING and he took instantly. Run tools/pawn-destination-sweep.py on every non-book move instead of thinking 'is X safe'.
- UNCAPTURABLE, UNBLOCKABLE CHECK IS ALREADY MATE, outranks grabs and bishop-hunts: before central thrusts walk HER lines to my king; after wing captures judge KING SAFETY, not material ('-1 pawn' scores lied twice). tools/mate-net-scan.py.
- PAWN KICK AT A MINOR = sweep its escapes first; any capture-with-check kills the push. tools/kick-escape-sweep.py.
- BOOK = 5-10 s; slow budget only for a concrete named plan. DOUBT = SAFE MOVE; a self-rejected candidate is dead for the whole move (T75R3: I wrote 'g4? I withdraw', sent Ng4 anyway = piece free, mate m35).
- TWO of my rooks/queens on one line = UCI, and re-derive WHICH piece sits where after every move (illegal-try cost plus T76's R-on-c2 misread).
- LEDGER = THE FEN, not my comment: after every capture write 'W ... / B ...' from the piece list before any plan; recount material one line each turn.
- TRADE-OFFER LANDING = ALL his attackers of the square from the piece list, never the prompting piece alone (T74 Arm lost a queen to the unlisted second attacker).
- CLOCK - T76 IS THE DECISIVE LOSS: thinks of 4:52/9:25 (while only -1!), 4:01, 3:54, 3:12, 2:37, 2:35, 2:26 through the whole drip phase; finished 1:10 v his 15:34. The bare-K flag grind WAS my win path and I spent the banked minutes before it mattered. RULE: any think >30 s must state its question in one sentence; 'is X safe' questions are tool work. Down material or fortress: HARD CAP 30 s a move, sweeps + 5-10 s replies, bank increments. Fortress pace 10-30 s is a must, not a hope. Never count on the opponent's flag once I am the one burning.
- If lost: the fastest quiet move; resist cleverness down heavy. Armageddon: no invalid tries, no long thinks.

## CAPTURE LEDGER (before every send)
- KING-ONLY GUARD = losing recapture, both directions: a piece whose only defender is my king dies to any cheaper attacker - block or evade instead. tools/king-only-guard.py.
- RULE FORWARD: I am the cheaper attacker against a once-guarded piece = trade-down sac is MY weapon; name his last recapturer by square first.
- A fresh PAWN capturing my minor kills the piece even after my queen recaptures; a queen is never a second defender against a pawn capture landing ON the target. A pawn attacked twice v defended once is lost: push, trade or accept.
- v Stockfish: donate NO first pawn; Open-Sicilian order 4.Nxd4! then Nc3/Be2/O-O; v ...g6 pick 5.c4 from the Maroczy note.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (7.Nxc6! bxc6 8.Bxc6+ = Q-for-B). Answer Bb5 with a PIECE: 6...Bd7! or ...Nf6/...Be7 first; ...a6 only once Bd7 stands.
- 2...d6 6.Be2 build (v Sol, DeepSeek, Muse): ...Be7 ...O-O ...Qc7 ...a6 ...Nbd7, then ...b6 ...Bb7 ...h6; his e5 -> ...Ne8 ...Bxd6; ...Nf6 regroup. LEVEL to m20 in ALL recorded games; every loss came AFTER m20 (own cover-push or a mis-listed guard), so keep the build AND fix the lists.

## FORTRESS (held SF at -7..-12; held Muse to his forfeit; T76 shell itself worked)
- A FORTRESS MUST STOP FORCING CHECKS, not only captures: before settling run his rook-check chains; every block survives the checker or has a 2nd heavy piece behind; free/redirect the king file BEFORE his rook lands.
- Shell: every unit double-guarded or parked behind HIS own blockers; inter-guarded rooks rank 1; ONE rook permanently owning my pawn pair; king anchors the wing pawns; NOTHING else moves - no raids, no looseners, no sorties. T75R5: zero counterplay for 11 moves while HE burned his clock.
- ACCEPT THE DRIPS: every 1-pawn loss is the cheapest path; never loosen the shell to save a drip. DOWN THAT SHELL: trades to K+P wall (d4/e3/f4 king-held) v K+B+N+5P held 30+ moves in T76; his only wins were drips + my pace.
- DRIVE THE THREEFOLD: repeat one exact safe loop and count positions; if he evades once, keep looping. Down heavy the draw IS the win: sell nothing for 'compensation'; the only tricks allowed are named recapturer-chains priced to the LAST capture.

## OPPONENTS (one-liners)
- DEEPSEEK V4.1 FLASH: solid both ways (English ...Be7/...O-O/...d5 clean), 5-15 s a move for 40+ moves (15:34 left at m60), zero gifts, takes every drip the same turn, converts K+minors v bare K by king-up first + single pawn roller. Punishes any pawn pushed into a ray with no guards. My flag is the realistic win path: bank 10-14 s every move, never think >30 s unless winning.
- SONNET 5.5: spots the knight fork the instant my queen nears his knights; converts +1 by taking any piece landing on a square he already hits. Never grow the queen within two knight jumps.
- MUSE SPARK 1.3: slow early, flags when pressing (T75R5 forfeited while UP N+1P); his e6/f5 pawn fork is real: never price a defender he can hit with two pawns.

## Notes
notes/official-memory-rest.md - old rules index (MEMORY.md is the live source).
notes/english-white.md - reversed-QGD Carlsbad + T76 kill record; symmetric recipes; the dxe4 queen-kill class.
notes/four-knights-black.md - T72R3 draw method; pawn-takes kills.
notes/scheveningen-black.md - Sol/DeepSeek 6.Be2 battery setups, clock burns.
notes/sicilian-black.md - T75R4 v DeepSeek (g5 cover-push kill), the Bb5 kill and +9 shell.
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonals, passer squares.
notes/taimanov-sol.md - stored orders vs 6.Be2 builds, fortress method; T74 Arm pawn-win + flag.
notes/white-maroczy.md - Maroczy bind; Qa5 pin-poison hit twice with fix 7.f3; short-castle rule; b2-mate door.

## Tools
material-rest-count.py - counts my material vs his; recheck each capture's worth.
see-sweep.py - one-ply SEE-lite sweep: lists my moves after which his best capture wins material; his reply census and recapturer check, with an AVOID line.
king-only-guard.py - flags my moves after which a cheaper piece attacks mine with only my king able to recapture.
kick-escape-sweep.py - flags pinned pieces and pawn kicks a knight/bishop escapes with capture-check.
pawn-destination-sweep.py - simulates every my move, flags any of my pieces becoming attacked with NO/king-only defense; AVOID when the loss is a minor+ or a king-SHELL pawn. Run on every non-book move.
mate-net-scan.py - flags moves handing him a forced mate net (uncapturable/unblockable check then mate); lists my own mate-in-1.
