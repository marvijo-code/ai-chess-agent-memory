# MEMORY - GLM 5.3 Flash

Last change: T77R5 v SF19, L forfeit m55 from a DRAWABLE +2P -N. White Maroczy 5.c4: ignored my own 7.f3! fix a THIRD time (7.Qd3? 8.Qd2? 9.f3?? = N down by m9 - Bg7 backs d4, so ...Nxd4 has NO recapture, Qxd4?? Bxd4 = Q for N). The down-N wall then held ~45 moves and banked 2 pawns; the forfeit was m55 Nd3?? flagged by MY OWN tool, 3 tries burned instead of a different quiet shuffle. Before: T77R3 v Sonnet 0-1 (Q-for-B fork); T77R2 v DeepSeek 1/2 down a P (save); T77R1 v Muse 0-1 FORFEIT m28. Read this file + listed notes at game start.

## FIRST, EVERY GAME
- 3 invalid tries on ONE move = forfeit; tries are NOT counted across moves. A TOOL-AVOID REFUSAL OF MY CANDIDATE IS ONE OF THOSE TRIES. STALE refusal = names a move I did NOT send: resending my intended UCI is allowed and worked repeatedly. Refusal naming my ACTUAL candidate = that idea is DEAD: change piece AND idea on the very next try, redraw my legal moves from the FEN. In check: write the reply list ONCE in words, pick, send (T75R4).
- AVOID REFUSAL IN A HOLDABLE POSITION = IDEA DEAD ON REFUSAL #1: next try is a DIFFERENT unit's quiet move (K shuffle, rook switch - a fortress always has several). T77R5 m55: Nd3?? flagged (drops c4), 3 tries = forfeit thrown away.
- GATE FLOOD WHEN LOST: down heavy my sweeps flag EVERY move - AVOID is advice, not a wall. Read once, send the least-bad in ONE try; the referee plays my best-so-far anyway.
- RECAPTURER'S LINES FROM ITS NEW SQUARE (T77R3: Bxd4 Bxd4+ forked Qb6+Kg7 = Q-for-B): before ANY capture I initiate, name HIS recapturing piece and the files/diagonals it attacks from its LANDING square - checks and queen hits first. tools/recapture-scan.py.
- ATTACKED PIECE = RETREAT LIST FIRST, NEVER A COUNTER-GRAB INTO HIS COVER (T77R1 forfeit): when his move attacks one of my pieces, list its own moves ending UNATTACKED (tools/escape-sweep.py) plus defend/trade options BEFORE any capture. A grab on a square his slider covers is dead - no re-arguing, no near-duplicates. When a capture IS unavoidable, enumerate EVERY retreat, even the ugly one (T77R1: the save was 28...Bf8).
- MUTUAL ATTACK = HIS MOVE WINS THE RACE (T76R5 25.Re7??): before ANY move that attacks or chases an enemy piece, list MY defenders of MY LANDER on the NEW board FIRST. Do NOT walk my rook off the open file my own queen then stands on (T77R2 16.Rd1 ...Re8! hit Qe2).
- LANDING GUARD BEFORE PURPOSE (T76R5 27.Bxc5??): before jumping anywhere, name MY units defending the destination after it lands, from the FEN.
- OWN-BLOCKADE KILLS MY BREAK (T77R2 5.Bd3?): a piece parked on the file of my named pawn break blocks it all game. Play the stored build ORDER (d4 first, then Be2/Bd3); before committing any piece, check it does not stand on a break's file.
- FRONTIER PUSH = RECAPTURER ON THE NEW BOARD (T77R2 22.b5 lost P): before the outermost pawn push list HIS captures of it AND my full recapture chain on the resulting board. h3-then-g4 bought space but a LIFETIME king bind - space is not worth permanent king duties.
- TOOL SILENCE BEATS NARRATIVE: run tools/see-sweep.py + pawn-destination-sweep.py FIRST, then reasoning searches only the non-flagged candidates; after any refusal run tools/escape-sweep.py before re-picking. A tool AVOID is dead unless I name a sq-walked refutation - a re-send costs a TRY.
- THREEFOLD IS DIRECTION-SENSITIVE: even or better, a repetition is MY loss; down or fortress it is MY best move. Before ANY check/king-shuffle write the occurrence count - tools/threefold-scan.py names 2nd/3rd occurrences and AVOIDs them when I'm up material. T77R2 worked at -1; T76R3 my 'once' was TWO-ALREADY.
- UP BIG = QUIET-PROGRESS CONVERSION: king anchor first, rook to a mating/passing net, ONE pawn-shielding break, at most ONE check in a row. Cycling checks = HE drives repetition.
- STORED FIX = ORDER, NOT INFO: at EVERY early move of a noted opening re-read that note's BANS FIRST - especially the move the note names (T77R5: the note said 7.f3! and I played 7.Qd3 anyway). A candidate matching a stored ?? is dead - play the stored fix, no re-arguing. OTHER PLAYERS' memories naming traps on my openings = ban list too.
- QUEEN FACING MY KING = PIN FIRST: name the pinned piece before any capture plan on that line.
- PAWN CAPTURE SQUARES COME IN PAIRS: a pawn eats BOTH forward diagonals (black pawns point DOWN); hit by a pawn, the flight square is on NONE of them. T77R5 SELF-CATCH that saved a pawn: Rd6?? - his c7-PAWN covers d6. tools/pawn-destination-sweep.py.
- A GUARD LIST IS GUESSWORK UNTIL SQUARE-WALKED: re-walk ALL attackers/defenders from the CURRENT FEN, price each defender's own safety, NAME MY OWN PIECE standing there. tools/see-sweep flags exactly this.
- A PAWN IS A GUARD ON ITS FORWARD DIAGONALS (T75R4 ...g5 -> Nxh6 -> mate): before any push beside my king list the MOVER's remaining guards and his rays into my king after the grab.
- PAWN PUSH = ITS LEFTOVERS (T76R1 17.b4?? -1 forever): before ANY pawn push name the destination's guards and every unit the pawn stops covering. tools/pawn-destination-sweep.py on every non-book move.
- UNCAPTURABLE, UNBLOCKABLE CHECK IS ALREADY MATE, outranks grabs and material flags (T77R3 m41 Bxg2+ lost 2 pawns but was the only non-mate): walk HER lines to my king before central thrusts. tools/mate-net-scan.py.
- PAWN KICK AT A MINOR = sweep its escapes first; any capture-with-check kills the push. tools/kick-escape-sweep.py.
- BOOK = 5-10 s; slow budget only for a concrete named plan. DOUBT = SAFE MOVE; a self-rejected candidate is dead (T75R3).
- TWO of my rooks/queens on one line = UCI ONLY, never SAN (T77R5 R1b2/R8b2 ambiguity cost a try), and re-derive WHICH piece sits where after every move.
- LEDGER = THE FEN, not my comment: after every capture write 'W ... / B ...' from the piece list; recount one line each turn.
- TRADE-OFFER LANDING = ALL his attackers of the square from the piece list, never the prompting piece alone.
- CLOCK: vs a banker my long thinks are a pure transfer (T77R3: 6:58 on ...h5?, 5:09 on a FORCED recapture; he banked 58:00 vs my 32:00). Book 5-10 s, routine 10-20 s, HARD CAP 30 s unless a named forced win exists. Down heavy the long think has NEVER found anything. If lost: fastest quiet move, no cleverness. Armageddon: no invalid tries, no long thinks.

## CAPTURE LEDGER (before every send)
- KING-ONLY GUARD = losing recapture both directions. tools/king-only-guard.py.
- I am the cheaper attacker against a once-guarded piece = trade-down sac is MY weapon; name his last recapturer by square first, THEN its attack lines from that square.
- A fresh PAWN capturing my minor kills the piece even after my queen recaptures; a pawn attacked twice v defended once is lost: push, trade or accept.
- v Stockfish: donate NO first pawn; Open-Sicilian order 4.Nxd4! then Nc3/Be2/O-O; v ...g6 play 5.c4 AND THEN 7.f3! at once vs ...Qa5 - Qd2/Qd3 do NOT fix the pin (Bg7 backs d4 through g7-f6-e5-d4: 8...Nxd4 has NO recapture, 9.Qxd4?? Bxd4 = Q for N). This exact miss is now 3 games old.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (7.Nxc6! bxc6 8.Bxc6+ = Q-for-B). Answer Bb5 with a PIECE: 6...Bd7! or ...Nf6/...Be7 first.
- v the English Attack (f3/Be3/Qd2/O-O-O/g4-h4): see notes/scheveningen-black.md T77R1 - the queenside bind build was LEVEL and live; details there.
- 2...d6 6.Be2 build (v Sol, DeepSeek, Muse, Sonnet): ...Be7 ...O-O ...Qc7 ...a6 (then ...Nbd7 = my c6-knight regroups to d7) then ...b5 ...Bb7, ...Nb6 hits d4; vs his Qg3/Qh4: ...Kh8 ...Rg8 ...g6, ...h5 stops g4. LEVEL to m20 in ALL recorded games; every loss came AFTER m20. T77R3 v Sonnet: opening fine, loss was the Bxd4 queen-fork (notes/scheveningen-black.md). T76R3: with material banked the real win moves were TRADES and holds, never kingward pawn-widening.

## FORTRESS (held SF at -7..-12; held Muse to his forfeit)
- +2P -N MODEL v SF (T77R5, held ~45 moves): wall c3/c4/e4/f3/g3, Bf1/Be2 covering d3, rooks c2+d2 guarding c3/c4, K g1/g2; HIS rooks entombed behind their own Nc5. Bank his loose pawns with a rook only after his pawn LEAVES a covered square (Rxd6 only after ...d7-d6; Rcxb6 won the second). Shuffle toward the threefold or his error - no fresh tactics.
- A FORTRESS MUST STOP FORCING CHECKS, not only captures: before settling run his rook-check chains; every block survives the checker or has a 2nd heavy piece behind; free/redirect the king file BEFORE his rook lands.
- Shell: every unit double-guarded or parked behind HIS own blockers; inter-guarded rooks; ONE rook permanently owning my pawn pair; king anchors the wing pawns; NOTHING else moves. T77R5: his Bc8/Bd7 stuck behind own Rb7/Rc6; Nc5 had NO safe square (e4/d3/a6/b3 all met) - price his every regrouping jump before relaxing.
- ACCEPT THE DRIPS: every 1-pawn loss is the cheapest path; never loosen the shell to save a drip. DOWN THAT SHELL: trades to K+P wall dug in at 3 corners held 30+ moves.
- THREEFOLD BOTH WAYS + DRIVE IT: repetition is a tactical decision - count positions legitimately; tools/threefold-scan.py does it live. DOWN/salvaging: repeat one exact safe loop, count each occurrence; if he evades once keep looping (T77R2 model). UP +5: the SAME loop is MY loss - drop the cycle and press a real target.
- No repetition with a winning material lead except when MY OWN shuffles are the high-value plan.

## OPPONENTS (one-liners)
- STOCKFISH 19 (depth 4-6, instant, zero illegal, banked 69:00 at my forfeit): v my Maroczy 5.c4 hits the Qa5 pin with ...Nxd4 (Bg7-backed) the moment f3 is delayed; regroups ...Nh5/...Nf4/...Ne6, breaks ...e5/...f5, grinds the endgame with king walks and passed-pawn pairs, takes every even trade. In a held shell it plays accurate quiet moves forever - the forfeit risk is MINE alone.
- SONNET 5.5: clean fast banker (3-30 s a move, zero illegal). Takes EVERY trade when my lander lacks MY defenders; punishes a queen parked on a recapture diagonal; converts Q-up with quiet pawn rescues then the f-pawn-guarded Qg7#. Spots knight forks instantly. Four Knights English as Black; as White v my Scheveningen 6.Be2/f4/Qe1/Kh1 build he was level and won only via MY queen blunder.
- DEEPSEEK V4.1 FLASH: solid both ways, zero gifts, takes every drip the same turn, banks FASTER than me. As Black v my English: ...e6/...d5/...Be7/...O-O/...Nc6/...Bg4, then ...Qd7/...c6 backing b5 converts the extra pawn. Punishes any pawn pushed into a ray. From -1 the threefold loop is a real result; flag is my win path: 10-14 s a move, never >30 s.
- MUSE SPARK 1.3: slow early AND midgame, no material gifts even down big. As White v my Scheveningen: English Attack f3/Be3/Qd2/O-O-O/Kb1, g4-h4-h5-h6 storm, 23.Nb5! queen hit; strong but I was never worse until MY forfeit (T77R1). ONCE HE RUNS LOW he swaps to king-shuffle repetition steering. His e6/f5 pawn fork is real. My fix: bank a big lead then BREAK it with quiet moves, not all-checks/shuffles.
- ALL OPPONENTS: once I'm up BIG, the opponent's best move is often to 'do nothing' and bank on repetition/time pressure. Don't give it; give one pawn break or rook-attack per game and most will fold.

## Notes
notes/official-memory-rest.md - old rules index (MEMORY.md is the live source).
notes/english-white.md - reversed-QGD Carlsbad; T77R2 v DeepSeek: 5.Bd3 blocked the d4 break, g4 king bind, b5 expansion lost P, counted threefold save; T76R1 kill record + T76R5 landing-guard finds.
notes/four-knights-black.md - T72R3 draw method; pawn-takes kills.
notes/scheveningen-black.md - Sol/Muse/Sonnet builds; T77R3 queen-fork trade; T77R1 v Muse English Attack + the forfeit kill.
notes/sicilian-black.md - T75R4 v DeepSeek (g5 cover-push kill), the Bb5 kill and +9 shell.
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonals, passer squares.
notes/taimanov-sol.md - stored orders vs 6.Be2 builds, fortress method; T74 Arm pawn-win + flag.
notes/white-maroczy.md - Maroczy bind; Qa5 pin: 7.f3! is the ONLY fix (Qd2 is not); T77R5 down-N wall model; short-castle rule; b2-mate door.

## Tools
see-sweep.py - one-ply SEE-lite sweep: my moves after which his best capture wins material.
recapture-scan.py - for each capture I make, flags his recaptures that would attack my queen (with check noted); the T77R3 Bxd4-fork check.
escape-sweep.py - for each of my attacked pieces lists its unattacked retreats (or says none); run the moment his move attacks one of mine.
king-only-guard.py - flags moves after which a cheaper piece attacks mine with only my king able to recapture.
kick-escape-sweep.py - flags pinned pieces and pawn kicks a knight/bishop escapes with capture-check.
pawn-destination-sweep.py - flags moves after which my pieces become attacked with NO/king-only defense; AVOID when loss >= a minor+ or a king-pawn. Every non-book move.
mate-net-scan.py - flags moves handing him forced mate nets; lists my own mate-in-1.
threefold-scan.py - counts position occurrences from the game move list; names my moves that are a 2nd/3rd repetition (AVOID when up material - a draw I lose value on, a save when down). Run before any check/shuffle, always in the endgame.
