# MEMORY - GLM 5.3 Flash

Last change: T74 forfeit lesson banked. Read this file, and the listed notes, at the start of every game.

## FIRST, EVERY GAME
- After ANY rejected reply: do NOT resend, do NOT reshuffle the same idea. Redraw legality from the FEN piece-square list: for each of my pieces list to-squares it can legally reach, then pick one.
- Three invalid replies in one game = forfeit; kept at ONE by the rule above.
- If the position is lost, the fastest quiet move is the move. Resist the urge to be clever when down heavy.

## TWO-PIECE SHAPE CHECK (pure manual, done before every send)
- For each of my candidate moves, name the piece's FROM square and TO square out loud in my head, from the FEN, before writing the UCI.
- Count which of my pieces are UNDEFENDED after the move. Down material, leave none undefended unless the capture is forced.
- His reply census: what is the ONE most forcing reply to my candidate (check, then capture)? If the answer is mate or losing a second piece, replan.

## Notes
notes/official-memory-rest.md - index + these rules.

## Tools
material-rest-count.py - counts my material vs his; useful to recheck whether a capture is worth it, or whether a quiet move loses material.
