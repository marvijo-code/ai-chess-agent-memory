# MEMORY - GLM 5.3 Flash

Last change: T74R5 (0-1 White v SF19, flag) - pawn-feed, doubt and clock lessons banked. Read this file and the listed notes at game start.

## FIRST, EVERY GAME
- 3 invalid tries on ONE move = forfeit; tries are NOT counted across moves (7 survived T74R5). After ANY rejected reply: do NOT resend or reshuffle the same idea. Redraw every my piece's legal to-squares from the FEN piece list, then pick by a DIFFERENT piece or square.
- DOUBT = SAFE MOVE. If my own verification of a greedy/centralizing move ends in "wait, is it safe?" (T74R5 m40: 40.Rc8?? dropped a free rook with the doubt written on my own move note), I send the verified-safe quiet move instead.
- When two of my rooks/knights/bishops share a rank or file, SEND UCI: SAN ambiguity (Rfd1, Rfe1, bare Rd1, Rb7) cost 4 invalid tries in T74R5; and always re-derive WHICH rook sits where after each rook move (f1->d1 fictions).
- Lost or worse: 10 s a move, hard think cap 60 s, trades and defense only. T74R5 flagged at 1:25 after 5:09 / 11:16 / 2:53 thinks on quiet moves. Recount material and eval from the FEN in one line each turn; my spoken numbers drift (-2 vs -7 confusion).
- After ANY rejected reply: do NOT resend, do NOT reshuffle the same idea. Redraw legality from the FEN piece-square list.
- If the position is lost, the fastest quiet move is the move. Resist the urge to be clever when down heavy.

## CAPTURE LEDGER (before every send)
- "If he takes it, I recapture" is bookkeeping, not defense: the capturer KIND decides. A fresh PAWN capturing my minor leaves the piece dead even after my queen recaptures (T74R5 11.Qe2 11...exd3! ate the d3-bishop; the recapture only got the pawn). A queen is never a second defender against a pawn capture that lands ON the target: move the target or remove the attacker.
- A pawn attacked twice v defended once is already lost (T74R5 9.Qf3? invited ...Nxd4 cxd4 dxe4 = two pawns, then exd3): choose push-away, trade or accept - never queen-defend it.
- v Stockfish, donate NO first pawn in the opening: 4.c3?? dxc3 = -1 forever with no attack, +9 by move 12, grind-loss. Clean recaptures only: 4.Nxd4!, then Nc3/Be2/O-O; against ...g6 pick 5.c4 from the Maroczy note - never a c3 gambit for air.

## Notes
notes/official-memory-rest.md - old rules index (MEMORY.md is the live source).
notes/english-white.md - reversed QGD/symmetric English recipes.
notes/four-knights-black.md - T72R3 draw method; pawn-takes kills.
notes/scheveningen-black.md - Sol/DeepSeek 6.Be2 battery setups, clock burns.
notes/sicilian-black.md - my Black Sicilian repertoire and losses.
notes/sveshnikov-black.md - T40R4 line; fresh-pawn diagonals, passer squares.
notes/taimanov-sol.md - stored orders vs 6.Be2 builds, fortress method.
notes/white-maroczy.md - Maroczy bind + T74R5 4.c3 open-Sicilian disaster.

## Tools
material-rest-count.py - counts my material vs his; recheck each capture's worth.
see-sweep.py - one-ply SEE-lite sweep: lists my moves after which his best capture wins material; his reply census and recapturer check that T74R5 lacked, with an AVOID line.
