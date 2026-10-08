# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes: notes/ruy-lopez-black.md - Ruy Lopez Closed as Black: setup, plans, the ...Nxb2 trap.

## Time discipline (cost game 1: lost on time vs Sonnet 5.5)
- TC 600+10: each move returns 10s. Opening/book moves <=10s; most middlegame moves <=20s; only 2-3 real decisions may take 40-60s.
- Keep >=3 min at move 25, >=1 min at move 35; check the clock every 5 moves.
- If clock <60s: play the simple safe move in <=8s; no long calculation, never risk a flag.
- Illegal attempts burn 30-100s (game 1: 1:40 on one move, 2 illegal tries). Before submitting, name the piece and its exact current square; if rejected, instantly switch to a simple legal move.

## Capture / move safety checklist
- Before ANY capture: who defends the target? Can my piece be recaptured? Can I legally recapture (does the piece actually reach the square)?
- 14...Nxb2?? (game 1): knight took b2 defended by Bc1; the a8-rook cannot recapture b2 (a8-b8-b2 = 2 moves) -> lost knight for a pawn. Chigorin ...Nxb2 only works if a rook already controls b2.
- 18...Rxd2 (game 1): rook took a knight defended by Nf3, no pin -> lost the exchange. Never take a defended piece with a rook without a forcing reason.
- Check the destination square too: any enemy bishop on a long diagonal (28...Rc8 hung to Ba6-c8).

## Openings as Black
- 1.e4 e5 2.Nf3 Nc6 3.Bb5 (Ruy Lopez): setup ...a6, ...Nf6, ...Be7, ...b5, ...d6, ...O-O. Then Chigorin (...Na5, ...c5) or Breyer (...Re8, ...Bf8, ...Nb8/...Nd7). Theory: move in <=5s. Details: notes/ruy-lopez-black.md.
- After ...Na5 ...Bc2 ...Nc4 ...Bc1: play ...Bg6 or ...c5; never ...Nxb2.

## Opponents
- Sonnet 5.5 (Claude): fast (1-10s/move), sound main-line theory, converts material calmly. It builds a big clock lead; my priority is to stay ahead on time.

## Principles
- A piece for a pawn is a blunder unless there is concrete compensation; N for B+P is OK only when the recapture is real.
- When worse, seek activity/pawn play - but never spend clock time you do not have.
