# Four Knights: defense before activity

## Shared opening
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4. Both pairs of knights disappear.
After ...Be6 Bxe6 fxe6 Qb3, Qe7 defends Bb4 via d6/c5 and e6 vertically. Qd5?? attacks Qb3 but permits Qxb4.

## T13 final: Black vs Stockfish 19, mate loss
10...Be6 11.Bxe6 fxe6! 12.Qb3 Qe7 13.d4 Rad8 14.c3 Bd6! 15.Qxb7 Qh4 16.f4 Bxf4? 17.Bxf4! Rxf4 18.Qxc6 Rxf1+ 19.Rxf1! Qe7.
- f4 interrupted Bd6-e5-f4-g3-h2. ...Bxf4 did not restore the mating battery: White exchanged bishops. Material stayed equal in pieces, but White had collected b7 and c6 and Qc6 attacked e6.
- This repeated an earlier failed ...Qh4/f4/...Bxf4 attack already recorded below. A familiar threat is not repaired preparation. Calculate the bishop exchange and ensuing pawn captures before committing; no best alternative to ...Bxf4 was supplied.
- ...Rxf1+ gave White's remaining rook the f-file. ...Rd6 attacked Qc6, but Qa8+ Rd8 Qxa7 forced the rook back and won another pawn. A queen attack can be answered with check and a capture elsewhere.

### Moving the pinning queen releases the pawn
After 30...Rf6 31.b4 Qf2+ 32.Kh2 Qf3?? 33.gxf3:
- White: Kh2, Qe4, Re1; pawns a5 b4 c3 d4 g2 h3. Black: Kg8, Qf2, Rf6; pawns c7 e6 g7 h6 before ...Qf3.
- Qf2 pinned g2 horizontally against Kh2. Moving the queen to f3 REMOVED the pin. The g2 pawn could now capture f3 legally.
- Rf6 supported Qf3, but a possible rook recapture would recover only a pawn. Attacking Qe4 and threatening c3 did not force a queen retreat.
- Before a queen move, enumerate enemy pawn captures of its destination on the RESULTING board. Refresh pins when the pinning piece moves, not only when the king moves.
- ...Qf3 took 38 seconds with over eleven minutes left. No invalid attempts; finished with 10:42. This was board verification failure, not time pressure.

### Promotion recapture ignores mate
33...Kf7 34.a6 e5 35.a7 Ra6 36.Qd5+ Kg6 37.Rg1+ Kh7 38.Qe4+ g6 39.a8=Q Rxa8 40.Qxg6+ Kh8 41.Qxh6#.
- ...e5 cleared the sixth rank for ...Ra6. Capturing the promoted queen removed one threat but ignored the forcing king attack.
- g2xf3 had opened the g-file for Rg1. That rook protected Qxg6+ and controlled g8; Qxh6 then covered h7/g7. Always scan checks and mate before an apparently automatic promotion recapture.

## T13 round 1: crossed attacks
13.d4 Rab8 14.Be3 Bd6 15.Rae1 Kh8 16.h3 e5 17.Bd2 Qf6 18.dxe5 Bxe5! 19.Bb4 Rfd8 20.Re4 Rd4?! 21.Re3 Bf4? 22.Bc3! Bxe3 23.fxe3 Rd3?? 24.cxd3.
- Rd4 screened Bc3's attack on Qf6. fxe3 attacked that rook; ...Rd3 lost it to cxd3 while exposing the queen. Imagined ...Rxc3 from d4 was illegal: rooks cannot capture diagonally.
- Black lost R+B for White's R, a bishop deficit. Prevent the crossed attacks before claiming a profitable exchange; no best replacement supplied.
24...Qg6 25.Rf7 Qxd3 26.Bxg7+! Kg8 27.Qxd3 Kxf7.
- Bc3 screened Qb3's attack on d3. Bxg7+ cleared it with check; Rf7 protected Bg7. Kxf7 recovered only the rook. Calculate an enemy blocker's checks before placing a queen behind it.

## T10 and earlier failures
- Kf6/Re7 allowed h4, protecting Bg5+ and enabling Bxe7. A defended rook still loses to a checking skewer. Later fxe5+ exd6+ cleared a rook checking file and removed Bd6.
- Rf4 screened Rf1 and could recapture on f8. ...Re4 abandoned both duties, allowing Rxf8#. ...Qe3+ Kh1 Qxc3 also ignored that mate.
- Qxf5 exf5 cleared e6 between Re2/Re8, allowing Rxe8+. Repetition escapes did not establish compensation.
- ...Qe1+ Rxe1 fxe3 Rxf8+ Bxf8 lost queen for rook: Ra1 had a clear path to e1.
- ...Rd1+ Kf2 Rd2+ Ke1 h6 Kxd2 lost the attacked rook. Creating luft did not answer its capture.
