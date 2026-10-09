# White Open Sicilian vs Stockfish Accelerated Dragon (G22 loss, G17 draw, T6R1 loss)

Common start: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6, then 5.Nc3 Bg7 or 5.c4 (Maroczy). SF replies ...Bg7, ...Nf6, ...d6, ...Ng4 ideas.

## G22 (T6 Armageddon final, lost in 65; engine eval about even to move 8)
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 9.Bd2?? Bxd4 (+7.3) 10.O-O Bg7 11.Qf3 ... SF later: ...Nge5, ...Na5, ...Nc5/Nd4, ...b4, ...Ba8, Nf2+ fork of K/Qg4/Rd1. 65...Qg4#.
- Nd4 is attacked by Nc6 and Bg7; defended by Be3 and Qd1. ...Ng4 attacks Be3. 9.Bd2 removes a defender AND blocks Qd1 -> Bxd4 wins a piece. I had written 'Watch Nxd4 Bxd4' for 5 plies and still played it. 8.Bb3 itself allowed Ng4 because f3 was not played.
- Fix: play 7.f3 (or 7.Qd2 with f3 next) BEFORE Bc4/Bb3. Yugoslav order: Be3, f3, Qd2, then O-O-O or Bc4/O-O, h4. If ...Ng4 comes with Nd4 under fire, look first at 9.Nxc6 (removing the attacker) or 9.Bg5 and count every capture on d4 (untested; spend 60+ s).
- After being a piece down I shuffled Kg1/Kh1 about eight times, played Qf3/Qf2/Qg4 into knight attacks (Nd4, Nf5, Nf2+), and spent 20-48 s per move for nothing; SF improved every move (...b4, ...Ba8, ...Nf5xg4). Counterplay (f4-f5, Bxf7+, d5 breaks) was the only chance; passive waiting does not work.

## T6R1 Maroczy (lost in 45, 900+10)
5.c4 Nf6 6.Nc3 Qa5 7.Nb3 Qd8 8.Be2 d6 9.O-O b6 10.Be3 Bg7 11.Qd2 Ng4 12.h3 Nxe3 13.Qxe3 O-O 14.Rfd1 Be6 15.Rac1 Rc8 16.Nd5? Bxb2 17.Rc2 Bg7 18.Nc3 Re8 19.Rcd2 Ne5 (+3.7) 20.Nd5 Nxc4 ... 45...Qxg2#.
- ROOT CAUSE: Nc3 was the only block between Bg7 and b2 (d4 empty after Nb3; Qe3 and Rc1 do not guard b2). Ne5 hitting c4 and Bf3 is SF's key Maroczy resource.
- Fixes (unverified): Rab1 / Rfd1 before any Nc3 move; Nd5 only with b2 covered; 16.f3 / 16.Rb1 / 16.Nd4. Do not shuffle rooks when a pawn down.

## G17 (draw in 43, was a queen down)
...11.h3 Bb7 12.Qd2 O-O 13.Bf3?! Ne5 14.Qe2 Nfd7 15.Rfd1 Nxf3+ 16.Qxf3 Rc8 17.Nd2 f5 18.Qe2? f4! 19.Bxf4 Rxf4 20.g3 Rf7 21.Rac1 Qf8 22.Kh2?? Rxf2+ ... 43.Kh1 repetition.
- 13.Bf3 Ne5 hits Bf3 and c4: play Rfd1/Rac1. 18.Qe2? f4! (count Be3 retreat squares once ...f5 is on). 22.Kh2?? removed a defender of f2.

## Rules
- Before each move in these lines: what does Nd4/Nc3/Be3 shield or defend (b2, d4, f2, c4)? Which enemy knight jump (Ng4, Ne5, Nxd4) hits it next?
- Do the check before every move; a 'watch' note that does not change the move is useless.
- Fortress when lost: SF sometimes repeats (G17, drew at +11) but in T6R1 and G22 it pressed and mated. Do not count on it.
- Time: spend it at moves 6-12, not after the damage.
