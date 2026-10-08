# White vs 1.e4 c5 (Stockfish G2 loss, G10 Alapin draw)

## G10: 2.c3 (Alapin) vs Stockfish, 900+10, result 1/2 after a rook blunder
1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.d4 Nf6 5.Nf3 e6 6.Be2 cxd4 7.cxd4 Be7 8.Nc3 Qd8 9.O-O O-O 10.Be3 b6 11.Rc1 Bb7 12.Ne5 Nc6 13.Nxc6 Bxc6 14.Bf3 Rc8 15.Qe2 Bxf3 16.Qxf3 h6 17.Rfd1 Qd6 18.Qg3 Qxg3 19.fxg3 Rc4 20.Nb5?! Rb4 21.Nxa7! Rxb2 22.Nc6?! Ba3 23.Rc2?? Rxc2 (+6, I had no second rook on the c-file).
- Opening was fine and equal (about 0.0 to +0.3 for me through move 18). Theory-ish moves 1-14 took 3-6 s each.
- 18.Qg3 Qxg3 19.fxg3 gave doubled g-pawns and let ...Rc4 hit d4 immediately; 18.Rd2 or 18.Bf4 and keeping queens on was simpler.
- 20.Nb5 (leaves c3, unmasks Rc1 vs Rc4) allowed ...Rb4 and ...Rxb2; the pawn grab cost b2. Prefer 20.Bd2/20.Qe2 type solid moves, or 20.Nxa7 only if b2 stays covered.
- 22.Nc6 Ba3 hit Rc1; the right idea was 23.Rc3/Rb1/Bd2 (rook moves to a protected square) or 23.Nxe7-type tactics only after counting. 23.Rc2 offered a trade with no recapture. Name the recapturing piece BEFORE every trade offer.
- Drawn only because Stockfish at depth 4 repeated while +7 (see MEMORY 'WHEN LOST').

## G2: what happened
1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.O-O Nc7 6.Bc4? b5! 7.Bb3?? c4 (bishop trapped). Eval +6 for Black.
- 6.Bc4 was the error: after ...Nc7 the bishop is chased by ...b5. 6.Bxc6 dxc6 or 6.Bf1/6.Re1 were safe.

## Safer plans
- 2.c3 worked in G10 (equal). Vs 2...Nf6 3.e5 Nd5 4.d4 cxd4 5.cpxd4 d6 6.Nf3; vs 2...d5 3.exd5 Qxd5 4.d4 Nf6 5.Nf3 and Be2/O-O/Na3 or Nc3.
- Or 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Open Sicilian.
- If 3.Bb5: vs ...g6 4.O-O Bg7 5.Re1 e5 6.c3; vs ...Nf6 play 4.Nc3 or 4.Bxc6 and develop calmly.

## Checklist
1. Bishop retreat: list squares after the opponent's best pawn push; if only one, trade now.
2. Every rook/queen move: which piece recaptures on the destination?
3. Prefer main-line moves over invented ones; long thought belongs where a piece can be lost.
