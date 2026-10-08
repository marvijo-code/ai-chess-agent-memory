# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan + blunder catalogue)
- notes/four-knights-black.md (games 3-4, b6-trap)
- notes/ruy-lopez-black.md
- notes/ruy-lopez-white.md (games 2, 5)

## Rule 1 - pre-move scan (all 5 losses; g4 alone had 4 misses)
Before submitting EVERY move:
1. Destination square: which enemy pawns/pieces attack it? If attacked and my piece is undefended -> reject (unless a forcing follow-up).
2. Captures: list EVERY recapturer (pawns count, queen behind counts); count material after the full exchange. Piece-for-pawn = -2; queen for N/B/pawn: never.
3. After the move: does it open a line (back rank, e-file, diagonal) to my king/queen, or leave a piece attacked next move?
4. Knight-fork scan: for each enemy knight, list its jumps that would attack 2 of my pieces: Nb3 hits a1+d2, Nc2 hits Ra1+Re1, Nf3+ hits Ke1+Qd2. Never move the queen onto such a square (g5: 26.Qd2?? ...Nb3! won the exchange; 27.Qxa5?? lost the queen for a pawn).
5. Legality/paths: my own pieces must not block the intended route, and pick the right rook (g5: 'Rad1' illegal - my Bb1 blocked the a1-rook; Red1 was legal). Illegal tries waste a try and clock.
Shapes seen: Bxd2??/Qxd2, Bxd4??/cxd4, Nxb2??/Bxb2 (piece for pawn); Qxe5??/Qxe5, Qxe4??/Rxe4, Qxa5??/Rxa5 (queen for lesser); Nf4??/Qxf4, Ne4??/Bxe4 (piece to an attacked square); Re8??/Qxe8# (rook to a queen-attacked square, undefended + back-rank mate).

## Rule 2 - time (600+10)
Opening <=10s, routine <=15s, max 3 decisions of 30-45s (g5: eight 30-45s thinks on moves 14-22 still ended in a blunder; long thinks don't fix tactics, the scan does). Dead-lost (down 2+): 5s moves, no tilt captures, keep the clock.

## Openings
- RL as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then Chigorin/Breyer; keep f7 covered; ...Nxb2 only if a rook already covers b2. notes/ruy-lopez-black.md.
- RL as White: Chigorin 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5! Nb4 15.Bb1 16.a3 Na6 17.Nf1 Bd7 18.Ng3 Nc5: then Bg5, Rd1/Red1, queen e2/e3 (not d2 while a knight can reach b3), f4 break. If ...Nb4 with the c-file open: 16.Rac1 or 16.Bb1, never 16.a3?? when only the queen guards c2 (g2: ...Nxc2!). notes/ruy-lopez-white.md.
- Four Knights 4.Bb5 Bb4: after 6.Nd5 Nxd5 7.exd5 Ne7, 8.Nxe5 wins the e5 pawn but only ~+0.5: answer 8...Nxd5/...d6/...c6, never 8...Bxd2??. If Nc4 hits b6: play ...b5. notes/four-knights-black.md.

## Opponents
- Stockfish 19 (ladder): ~0s/move, banks clock, takes every loose piece instantly, never blunders back. Every single move must pass the Rule 1 scan.
- Sonnet 5.5: fast, sound; stay ahead on clock.
- GPT-6.1 Sol: solid closed Ruy Lopez; punishes loose pieces and queen placement (finds ...Nb3 forks); keep everything defended, queen off fork squares. He blunders too (g5: 21...Nh7??, 22...Bxh4??) - punish calmly with Rd1/Qe2/f4, not queen shuffles.

## Principles
- Material first: no piece for a pawn, no queen for knight/bishop/pawn, no capture on a pawn- or queen-defended square.
- After a blunder: defend loose pieces, trade down, no panic captures; when dead-lost play fast and lose nothing more.
