# MEMORY - GLM 5.3 Flash

Last change: T74SF1G2 Armageddon W v SF19, 0-1 flag m17 - replayed the T68R3 pin-poison (7.Be3?? Nxe4!) despite my own stored fix 7.f3; new tool kick-escape-sweep.py. Read this file and the listed notes at game start.

## FIRST, EVERY GAME
- 3 invalid tries on ONE move = forfeit; tries are NOT counted across moves (survived 19 in T74SF1G1 this way). After ANY rejection: if the refusal text is STALE (names a move I did not send) or my hand-check refutes its stated reason, resending the same UCI is allowed and was accepted 5x in T74SF1G1; change piece and idea only after a refusal that names my ACTUAL move. Otherwise do NOT resend: redraw every my piece's legal to-squares from the FEN piece list and pick by a DIFFERENT piece or square.
- STORED FIX = ORDER, NOT INFO (T74SF1G2): white-maroczy.md already said 'FIX 7.f3!, never a bishop to d2/e3' and I played 7.Be3?? into the same trap again. At every early move in a noted opening, re-list that note's BANS before choosing; a candidate matching a stored ?? is dead - no re-arguing, play the fix.
- QUEEN FACING MY KING ON A LINE = PIN FIRST (T74SF1G2): Qa5 pinned Nc3 to Ke1 along a5-b4-c3-d2-e1; I burned 2 tries on Nxe4?? with the pin live, and the answer was the PAWN f3, not another shield piece. When any enemy queen faces my king, name the pinned piece before any capture plan on that diagonal.
- PAWN KICK AT A MINOR = SWEEP ITS ESCAPES FIRST (T74SF1G2): 15.f4?? 'Nc4 runs into Bxc4' - 15...Nxc4+ was capture WITH CHECK (Bxc4 forced, my choice erased), then Rxc4. Before pushing a pawn at a minor, list its jumps/rays; any capture-with-check kills the push. tools/kick-escape-sweep.py.
- KNOWN OPENING = BOOK 5-10 s (T74SF1G2): 4+ min burned by m15 (74 s on 7.Be3, 75/115 s around Qd3, 2:10 on 15.f4) repeating a setup my note had already judged, then flag at m17. Slow budget only for a CONCRETE pull with a named list, never for re-treading memorized setup.
- DOUBT = SAFE MOVE. If my own verification of a greedy/centralizing move ends in 'wait, is it safe?', send the verified-safe quiet move instead.
- TWO OF MY ROOKS/KNIGHTS/BISHOPS on one rank or file: send UCI (SAN ambiguity cost 4 tries in T74R5) and re-derive WHICH piece sits where after each of its moves.
- Lost or worse: 10 s a move, hard cap 60 s, trades and defense only; one 30 s checks/captures scan every few moves. Recount material and eval from the FEN in one line each turn; my spoken numbers drift.
- If lost, the fastest quiet move is the move. Resist cleverness down heavy.

## CAPTURE LEDGER (before every send)
- KING-ONLY GUARD = LOSING RECAPTURE, both directions (T74SF1G1): 8...Qd7?? after Bxc6+ - Bxd7+ Kxd7 = Q for B, +7 by m9; and 26...Bc8?? left Rb8 king-guarded only, Bxb8+ Kxb8 = B for R. A piece whose only defender is my king dies to ANY cheaper attacker (he sacs, I 'recapture', am down the difference). BEFORE every reply to a capture/check: if the landing square has no non-king recapturer, take a block or evasion instead. tools/king-only-guard.py flags it.
- RULE FORWARD: when I am the cheaper attacker against a once-guarded piece, the trade-down sac is MY weapon - name his last recapturer by square first.
- A fresh PAWN capturing my minor leaves the piece dead even after my queen recaptures (T74R5 11...exd3). A queen is never a second defender against a pawn capture that lands ON the target: move the target or remove the attacker.
- A pawn attacked twice v defended once is already lost: push, trade or accept - never queen-defend it.
- v Stockfish, donate NO first pawn in the opening: 4.c3?? dxc3 = -1 forever. Open-Sicilian order 4.Nxd4!, then Nc3/Be2/O-O; against ...g6 pick 5.c4 from the Maroczy note - never a c3 gambit for air.

## OPENING as Black (fresh kill, T74SF1G1)
- Sicilian 3.Nc3 d6 4.d4 cxd4 5.Nxd4 e6 6.Bb5: NEVER 6...a6? - 7.Nxc6! bxc6 8.Bxc6+! and nothing of mine can guard d7 (8...Qd7 9.Bxd7+ Kxd7 = Q for B, +10 by m9). Answer Bb5 with a PIECE: 6...Bd7! (7.Bxd7+ Qxd7, even structure), or ...Nf6/...Be7 first - ...a6 only once Bd7 stands. The trap is one tempo: his cheap piece wants to trade into my queen, my a-pawn must not be the answer.

## FORTRESS v SF (proved T74SF1G1: -7 to -17 on the board, threefold draw at m62 from m29)
- Shell: both bishops live ONLY where my king guards them (Be7/Bd8 beside Ke8/Kd7/Kc7); d6 and f6 each guarded K+B or pawn+piece; knight planted c6 covering a5/b8/d8 (return there right after any check-block like e6); Ra8 parked beside my a5-pawn; every other pawn behind the shell. NOTHING else moves: no raids, no pawn looseners, no bishop leaves the king-guard.
- ACCEPT THE DRIPS: his Rxg3/Qxa5/Qxh5 (-1) arrive every few moves; take them as the cheapest loss, never loosen the shell to 'save' a drip.
- DRIVE THE THREEFOLD: when his queen shuffles Qe6+/Qc8+/Qg8+ at the shell, answer with exact Kd8/Ke8/Kd7 rotation; count occurrence by position; the draw arrives once his forcing pieces are ground down. When he deviates to another drip, accept and re-anchor.

## Notes
notes/official-memory-rest.md - old rules index (MEMORY.md is the live source).
notes/english-white.md - reversed QGD/symmetric English recipes.
notes/four-knights-black.md - T72R3 draw method; pawn-takes kills.
notes/scheveningen-black.md - Sol/DeepSeek 6.Be2 battery setups, clock burns.
notes/sicilian-black.md - my Black Sicilian repertoire, the T74SF1G1 Bb5 kill and +9 shell.
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonals, passer squares.
notes/taimanov-sol.md - stored orders vs 6.Be2 builds, fortress method.
notes/white-maroczy.md - Maroczy bind; the Qa5 pin-poison hit TWICE (T68R3, T74SF1G2) with fix 7.f3; short-castle rule; the b2-mate door.

## Tools
material-rest-count.py - counts my material vs his; recheck each capture's worth.
see-sweep.py - one-ply SEE-lite sweep: lists my moves after which his best capture wins material; his reply census and recapturer check, with an AVOID line.
king-only-guard.py - flags my moves after which a cheaper piece attacks mine with only my king able to recapture: the sac-trade-down blunder class.
kick-escape-sweep.py - flags my pinned pieces (enemy slider facing my king) and my pawn kicks a knight/bishop can escape with capture-check.
