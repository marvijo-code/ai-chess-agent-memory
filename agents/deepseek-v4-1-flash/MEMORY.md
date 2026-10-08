# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan + blunder catalogue)
- notes/four-knights-black.md (games 3-4, b6-trap)
- notes/ruy-lopez-black.md
- notes/ruy-lopez-white.md

## Rule 1 - pre-move scan (all 4 losses; g4 alone had 4 misses)
Before submitting EVERY move:
1. Destination square: which enemy pawns/pieces attack it? If attacked and my piece is undefended -> reject (unless a forcing follow-up).
2. Captures: list EVERY recapturer (pawns count, queen behind counts); count material after the full exchange. Piece-for-pawn = -2; queen for N/B = -3/-6: never.
3. After the move: does it open a line (back rank, e-file, diagonal) to my king/queen, or leave a piece attacked next move?
Shapes seen: Bxd2??/Qxd2, Bxd4??/cxd4, Nxb2??/Bxb2 (piece for pawn); Qxe5??/Qxe5, Qxe4??/Rxe4 (queen for lesser); Nf4??/Qxf4, Ne4??/Bxe4 (piece to an attacked square); Re8??/Qxe8# (rook to a queen-attacked square, undefended + back-rank mate).

## Rule 2 - time (600+10)
Opening <=10s, routine <=15s, max 2-3 decisions of 30-45s. g4: 45s on the blunder move -> long thinks don't fix tactics, the scan does. Dead-lost (down 2+): 5s moves, no tilt captures, keep the clock.

## Openings
- RL as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then Chigorin/Breyer; keep f7 covered; ...Nxb2 only if a rook already covers b2. notes/ruy-lopez-black.md.
- RL as White: Chigorin 9.h3 Na5 10.Bc2 c5; at 15...Nb4 play 16.Rac1 or 16.Bb1 (16.a3?? ...Nxc2, Qc7 defends c2). notes/ruy-lopez-white.md.
- Four Knights 4.Bb5 Bb4: after 6.Nd5 Nxd5 7.exd5 Ne7, 8.Nxe5 wins the e5 pawn but only ~+0.5: answer 8...Nxd5/...d6/...c6, never 8...Bxd2??. If Nc4 hits b6: play ...b5. notes/four-knights-black.md.

## Opponents
- Stockfish 19 (ladder): ~0s/move, banks clock, takes every loose piece instantly, never blunders back. Every single move must pass the Rule 1 scan.
- Sonnet 5.5: fast, sound; stay ahead on clock. GPT-6.1 Sol: punishes hanging pieces; keep everything defended.

## Principles
- Material first: no piece for a pawn, no queen for knight/bishop, no capture on a pawn- or queen-defended square.
- After a blunder: defend loose pieces, trade down, no panic captures; when dead-lost play fast and lose nothing more.
