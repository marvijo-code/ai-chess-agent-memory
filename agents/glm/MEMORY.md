# MEMORY - GLM 5.3 Flash

Last change: T74R7 W v DeepSeek V4.1 Flash, 1/2 threefold m40 (third place) - lost the queen to the e4-PAWN's second capture square (18.e4? dxe4, Qf3?? exf3 = Q-for-P at m19); defended -9 to a draw; new tool pawn-destination-sweep.py. Read this file and the listed notes at game start.

## FIRST, EVERY GAME
- 3 invalid tries on ONE move = forfeit; tries are NOT counted across moves (survived 19 in T74SF1G1 this way). After ANY rejection: if the refusal text is STALE (names a move I did not send) or my hand-check refutes its stated reason, resending the same UCI is allowed and was accepted; change piece and idea only after a refusal that names my ACTUAL move. Otherwise do NOT resend: redraw every my piece's legal to-squares from the FEN piece list and pick by a DIFFERENT piece or square.
- STORED FIX = ORDER, NOT INFO (T74SF1G2): white-maroczy.md already said 'FIX 7.f3!, never a bishop to d2/e3' and I played 7.Be3?? anyway. At every early move in a noted opening, re-list that note's BANS before choosing; a candidate matching a stored ?? is dead - no re-arguing, play the fix.
- QUEEN FACING MY KING ON A LINE = PIN FIRST: when any enemy queen faces my king, name the pinned piece before any capture plan on that diagonal; the answer is usually the PAWN, not another shield piece.
- PAWN CAPTURE SQUARES COME IN PAIRS (T74R7, the whole game lost at m19): a black pawn on e4 eats BOTH d3 and f3. After dxe4 hit my Qd3, my flight d3-f3 landed on the second square and ...exf3 ate the queen. When ANY enemy unit hits my queen, list its capture squares - for a PAWN, both forward diagonals; white pawns capture up, black pawns DOWN - and pick a flight square on NONE of them, then re-check that square against every other pawn and knight too. MOVING WITHIN THE HIT'S CAPTURE SQUARES IS NOT A FLIGHT. tools/pawn-destination-sweep.py.
- A PAWN 'GUARDED' ONLY BY A PIECE THE CAPTURING PAWN ALSO HITS IS NOT GUARDED (T74R7 18.e4?): ...dxe4 arrived WITH a queen hit on Qd3, so the pawn was never saved. Before a central push with my queen standing behind/next to it, ask what his capture does TO MY PROTECTOR, not just to the pawn.
- PAWN KICK AT A MINOR = SWEEP ITS ESCAPES FIRST (T74SF1G2): any capture-with-check kills the push. tools/kick-escape-sweep.py.
- KNOWN OPENING = BOOK 5-10 s: slow budget only for a CONCRETE pull with a named list, never for re-treading memorized setup.
- DOUBT = SAFE MOVE. If my own verification of a greedy/centralizing move ends in 'wait, is it safe?', send the verified-safe quiet move instead.
- TWO OF MY ROOKS/KNIGHTS/BISHOPS on one rank or file: send UCI (SAN ambiguity cost 4 tries in T74R5) and re-derive WHICH piece sits where after each of its moves.
- Lost or worse: 10 s a move, hard cap 60 s, trades and defense only; one 30 s checks/captures scan every few moves. Recount material and eval from the FEN in one line each turn; my spoken numbers drift. T74R7: down -9 I still burned 1:45-2:35 on FOUR moves (Nb5, b3, Rdd1, regroups) - there is nothing to think about after the list; the 10 s rule is for exactly this.
- If lost, the fastest quiet move is the move. Resist cleverness down heavy.

## CAPTURE LEDGER (before every send)
- KING-ONLY GUARD = LOSING RECAPTURE, both directions: a piece whose only defender is my king dies to ANY cheaper attacker. BEFORE every reply to a capture/check: if the landing square has no non-king recapturer, take a block or evasion instead. tools/king-only-guard.py flags it.
- RULE FORWARD: when I am the cheaper attacker against a once-guarded piece, the trade-down sac is MY weapon - name his last recapturer by square first.
- A fresh PAWN capturing my minor leaves the piece dead even after my queen recaptures. A queen is never a second defender against a pawn capture that lands ON the target: move the target or remove the attacker.
- A pawn attacked twice v defended once is already lost: push, trade or accept - never queen-defend it.
- v Stockfish, donate NO first pawn in the opening: never a c3 gambit for air. Open-Sicilian order 4.Nxd4!, then Nc3/Be2/O-O; against ...g6 pick 5.c4 from the Maroczy note.

## OPENING as Black
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? (7.Nxc6! bxc6 8.Bxc6+ = Q-for-B). Answer Bb5 with a PIECE: 6...Bd7! (7.Bxd7+ Qxd7, even), or ...Nf6/...Be7 first - ...a6 only once Bd7 stands.

## FORTRESS v ENGINE-CLASS OPPONENTS (drew SF at -7..-12; drew DeepSeek at -Q-for-P)
- Shell: double-guard every unit or park it behind HIS own pawn/blocker; inter-guarded rooks on rank 1; ONE rook permanently owning my pawn pair (Rb1 on b3->a4 in T74R7); king anchors the wing pawns (Kg2 on f2/h2/h3); NOTHING else moves: no raids, no pawn looseners, no bishop/knight sorties even as 'free tricks'.
- ACCEPT THE DRIPS: take every 1-pawn loss as the cheapest path; never loosen the shell to 'save' a drip.
- DRIVE THE THREEFOLD: repeat one exact safe loop (T74R7: Rg1/Qe6/Rgd1/Qf6) and count occurrences by position. If he evades the loop once (Qd6), KEEP LOOPING - the threefold still arrived at m40. Down heavy the draw IS the win: sell nothing for 'compensation'.
- Down heavy, the only 'tactics' are recapturer-chains priced to the LAST capture; refuse everything I cannot prove to the final board.

## Notes
notes/official-memory-rest.md - old rules index (MEMORY.md is the live source).
notes/english-white.md - reversed QGD/symmetric English recipes; T74R7 6.Bf4 Four-Knights line + the dxe4 queen kill.
notes/four-knights-black.md - T72R3 draw method; pawn-takes kills.
notes/scheveningen-black.md - Sol/DeepSeek 6.Be2 battery setups, clock burns.
notes/sicilian-black.md - my Black Sicilian repertoire, the Bb5 kill and +9 shell.
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonals, passer squares.
notes/taimanov-sol.md - stored orders vs 6.Be2 builds, fortress method.
notes/white-maroczy.md - Maroczy bind; the Qa5 pin-poison hit TWICE with fix 7.f3; short-castle rule; the b2-mate door.

## Tools
material-rest-count.py - counts my material vs his; recheck each capture's worth.
see-sweep.py - one-ply SEE-lite sweep: lists my moves after which his best capture wins material; his reply census and recapturer check, with an AVOID line.
king-only-guard.py - flags my moves after which a cheaper piece attacks mine with only my king able to recapture: the sac-trade-down blunder class.
kick-escape-sweep.py - flags my pinned pieces (enemy slider facing my king) and my pawn kicks a knight/bishop can escape with capture-check.
pawn-destination-sweep.py - flags my moves that leave a piece freshly capturable by an enemy PAWN (both diagonals): the dxe4-Qf3-exf3 queen-loss class.
