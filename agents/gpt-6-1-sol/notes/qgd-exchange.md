# QGD: defenders, batteries, and file clearance

## T11 round 2: White vs Stockfish 19, checkmate loss
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 dxc4 5.e3 h6 6.Bh4 c5 7.Bxc4 cxd4 8.exd4 Be7 9.Nf3 Nd5 10.Bxe7 Nxe7 11.O-O Nbc6 12.Re1 O-O 13.Qe2 Nxd4 14.Nxd4! Qxd4! 15.Rad1 Qf4 16.g3 Qc7.
- Qe2 removed Qd1's defense of the isolated d4 pawn. Nf3 alone faced Nc6 and Qd8; the complete capture sequence lost the pawn. Rook development with tempo did not itself recover it.
- No earlier adverse marks establish an optimal opening. No engine-best replacement was supplied.

17.Nb5 Qb6 18.Rd6 Nc6 19.Red1 Qc5 20.Nc7 Rb8 21.Bb3 Na5 22.Nb5! b6 23.Bc2 Bb7 24.Nxa7 Ra8 25.Nb5?! Nc4! 26.R6d3? Qc6.
- Nc4 attacked Rd6. R6d3 saved that rook but inserted a blocker on Qe2-d3-c4-b5, abandoning the queen's defense of Nb5.
- Qc6 attacked Nb5 and threatened Qg2#. Bb7 protected g2 through c6-d5-e4-f3; the queen could travel down that diagonal. White's g-pawn was on g3, leaving g2 vacant. Kg1 could not capture a bishop-protected queen there, and f1/h1 remained under queen control.
- Retreat safety requires checking the next enemy threat and every defense blocked by the retreat, not just the rook's destination.
27.Rf3 Qxf3 28.Qxf3 Bxf3.
- Rf3 blocked the mating diagonal and reopened Qe2's defense of b5, but the battery captured it. Both queens disappeared; White lost an additional rook. Remaining pieces: White R+B+N against Black 2R+B+N, with equal pawn counts.

### King protection and the finish
29.Rd4 Bd5 30.b3 Rxa2 31.bxc4 Ba8 32.Bd3 e5 33.Rd6 g6 34.Rxb6 Ra1+ 35.Bf1 Rd8 36.Nd6 Bf3 37.h3 Rda8 38.Kh2 Rxf1.
- bxc4 recovered Black's knight, but the rook deficit remained. Ba8 preserved the bishop instead of accepting the proposed bishop trade.
- Bf1 was protected by Kg1. Kh2 abandoned it, allowing Ra1xf1. King evacuation must include the pieces losing king protection.
39.g4 e4 40.Kg3 g5 41.Nxf7 Rg1+ 42.Kh2 Rg2+ 43.Kh1 Ra1+ 44.Rb1 Rxb1#.
- Bf3 protected Rg2; Rg2 controlled h2 and the second rank. The other rook invaded a1, and Rb1 only delayed mate.
- Had 9:15 after R6d3 and 4:10 at mate, no illegal attempts. Many moves took 32-69 seconds; tactical omissions, not clock shortage, decided the game.

## T7 semifinal: White vs Sonnet, win with missed tactics
Exchange structure: ...Ne4 Bxe7 Qxe7 cxd5 Nxc3 bxc3 exd5; later e4 dxe4 Bxe4 Nxe4 Rxe4, with Re4/Qc2 against Be6/Qe7.
- Ne5?? allowed ...Bf5, skewering Re4/Qc2 along f5-e4-d3-c2. Moving Be6 also uncovered Qe7's attack on Ne5. Later Re4/Qd3 had the same skewer after c4??. Black missed both.
- With Qd6 attacking Nf4 and Re4 defending it, ...f5 could attack the defender and its charge together. Rook activity did not resolve both threats.
- d5 cxd5 cxd5 Bxd5?? cleared Be6 from the e-file, allowing Rxe7+ Kxe7: rook for queen. ...Rxd5 instead preserved the bishop screen and attacked Qd3. Compare all recaptures.
- Qd4 attacked Bd5, defended by Rd6; ...Rxf6 would abandon the bishop. Qe5 pinned Be6 to Ke7, but ...Kf7 released the pin. Ne4 protected Qf6+, driving the king away and enabling Qxe6+.
- After ...Kf8, Qxd5 safely removed the last rook; collecting pawns delayed simplification. Routine conversion still took 24-40 seconds.

## Earlier recurring failures
- Bf2 does not defend f4: its diagonals pass through e3/d4 and g3/h4. Nf4 placed a knight on Ne6's capture square.
- Bd3 blocked Rd1 against Qd7; Bh7+ removed the blocker with check, enabling Rxd7 Bxd7.
- Qxa7 allowed Rxa7: a rook pinned along a rank can move along it or capture the pinning queen.
- With Qe7/e3/Qe2 aligned, exd4 vacated e3 and uncovered a queen attack. After Nxd4 cxd4 attacked Rc3, Rc5?? landed undefended on Qe7-d6-c5. Attacking Bf5 did not force retreat.
- Bc6 attacked Rd5/b7 but allowed bxc6. Check pawn captures of attacking pieces.
