# Caro-Kann Advance: resolve pins before counterattacking

## T4 semifinal 2, game 1: Black vs Stockfish 19
Checkmate loss with 10:10 remaining and no illegal attempts. Tactical calculation, not clock pressure, caused the loss.

1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6! 8.Nge2 Ne7 9.Na4 Ng6?! 10.Nxc5 Bxc5 11.dxc5! Nxe5 12.Nd4 Qa5+ 13.Bd2 Qxc5 14.Nxf5 exf5! 15.Bc3 Qd6? 16.Qe2! f6? 17.f4! d4 18.O-O-O Qc5?! 19.Rxd4 Qe7 20.fxe5 fxe5.

## Extra pawn did not justify delayed king safety
After 14...exf5, Black had Ke8/Qc5/Ra8/Rh8/Ne5 and pawns a7 c6 d5 f5 f7 g7 h7. White had Ke1/Qd1/Ra1/Rh1/Bd2 and pawns a2 b2 c2 f2 g2 h2: Black was a pawn ahead, with knight against bishop.

- ...bxc6 and ...exf5 were marked only good moves. ...Ng6 was inaccurate; its active destination alone did not establish opening quality.
- 15.Bc3 attacked Ne5 through d4. ...Qd6 defended the knight but was marked a mistake. No best replacement was supplied.
- 16.Qe2 added an e-file attack and pinned Ne5 absolutely to Ke8: e3/e4/e6/e7 were clear.
- ...f6 supplied a pawn defender but did not free the knight. White's f4 attacked Ne5, which could not legally retreat off the e-file while the pin remained.
- ...d4 attacked Bc3 and blocked its diagonal to e5, but did nothing to the Qe2/Ne5/Ke8 alignment. White did not need to retreat the bishop: O-O-O developed Rd1 against d4 and Qd6.
- ...Qc5 moved the queen off the d-file; Rxd4 removed the blocking pawn. ...Qe7 interposed the queen between knight and king, but did not save the attacked knight: fxe5 fxe5 traded it for a pawn.
- The recapture attacked Rd4, yet White could simply retreat. A tempo after losing a piece did not restore material.

Before supporting a pinned piece, test enemy pawn attacks and how the piece can escape. Before a counterattack on a bishop, calculate castling, captures, and moves that leave the bishop in place. Resolve the king pin and development problem rather than assuming harassment forces cooperation.

## Final rook attack allowed protected mate
21.Rdd1 e4 22.Qc4 Qc7 23.Qe6+ Kf8 24.Qxf5+ Kg8 25.Rhf1 Rf8 26.Qxf8#.

- ...e4 was supported by f5, but did not secure the king. Qc4-e6 entered through the now-empty d5 square; Qe6 checked along the open e-file. Qxf5+ removed the supporting pawn with check.
- Before ...Rf8, Black had Kg8/Qc7/Ra8/Rh8 and pawns a7 c6 e4 g7 h7. White had Qf5/Rd1/Rf1/Bc3 with Kc1.
- ...Rf8 was Ra8-f8: Rh8 could not cross its own king on g8. It attacked Qf5 along the clear f-file, but the queen could capture it.
- After Qxf8+, Rf1 protected Qf8 through empty f2-f7, so Kxf8 was illegal. Kg8 also blocked Rh8's capture of Qf8. Black's g7/h7 pawns and Rh8 occupied remaining nearby escape squares; an adjacent queen check could not be blocked.
- ...Rf8 took 30 seconds with ample time. Before attacking a queen with a rook, explicitly calculate the queen's capture and whether the king obstructs the other rook's defense.
