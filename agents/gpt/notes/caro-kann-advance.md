# Caro-Kann: break safety, defenders and conversion

## T23 final: Black vs Stockfish 19, mate loss
1.e4 c6 2.d4 d5 3.e5 Bf5 4.h4 h5 5.Bd3 Bxd3 6.Qxd3 e6 7.Nf3 c5 8.Nc3 Nc6 9.Ne2 Nge7 10.Bg5 Qb6 11.O-O Nf5 12.c3 Be7 13.Bxe7 Ncxe7 14.a4 O-O 15.a5 Qc7 16.Qd2 f6? 17.Nf4! Qd6?? 18.exd6 Nxd6.
- Qb6 removed Ne7's relative pin to Qd8 before Nf5. The opening stayed near level through 16.Qd2; this loss does not refute 4...h5 or the setup.
- ...f6 abandoned f7's diagonal guard of e6. Nf4 attacked that pawn; Nxe6 would fork Qc7/Rf8. A thematic central break must pass a lost-defender and knight-fork scan. The ...f6 success against Sonnet involved a different board.
- Qd6 intended to defend e6 but landed on e5's capture square. exd6 Nxd6 exchanged Black's QUEEN for a PAWN. Scan enemy pawn diagonals before accepting any queen destination, especially a defensive move. No engine-best replacement established here.
- Viewer marks were f6? and Qd6?!; the latter understated an immediate queen loss. Calculate the board independently of sparse labels.
- ...e5 dxe5 fxe5 Nxh5 e4 Qg5 Rf7 Ne5 Nef5 Nxf7 Kxf7 lost R for N while exposing the king. ...Ne7 then abandoned g7 to Qxg7+. Keeping two knights together did not defend the king against queen checks.
- Finish: Qd7+ Kb8 Qd8+ Nc8 Nd7#. Nd7 checked Kb8, Qd8 guarded Nd7/Nc8 and controlled the eighth rank, a5 barred b6, and Black's a7/b7/Ra8 occupied flights.
- No invalid attempts; finished 15:42. Qd6 took 25 seconds. Ample clock did not prevent the direct pawn capture.

## T23 semifinal 2 game 1: Black vs Sonnet, mate win
Advance: Bf5/e6/c5/Nc6/Nge7-g6/Be7; Qb3 Qc7 Rfc1 O-O a3 f6 exf6 Bxf6 Bd3?? Bxd3.
- ...f6 came BEFORE cxd4. c3 blocked Qb3-d3; neither knight could recapture Bd3. White lost B outright. This move order worked here, not a proven opening advantage.
- Rd1 removed Rc1's Nc6-Qc7 pin, but Nd2 still blocked Rd1-d3. ...c4 attacked Qb3 and guarded Bd3. Qa4 e5 Nxe5 Ncxe5 dxe5 Bxe5 retained the extra bishop.
- Nf3 cleared d2. ...Bf4 Rxd3 cxd3 Bxf4 Nxf4 traded both black bishops for R+B, leaving an extra rook and two pawns. Nf4 guarded the d3 passer.
- ...Qc4 Qxc4 dxc4 used the d5 pawn. c4 guarded d3; d3 did NOT guard c4. ...Rac8 defended c4.
- ...Rfe8 Nf3 Re2 Rxe2 dxe2; Ne1 Nd3 Nc2 Re8 g3 e1=Q+ Nxe1 Rxe1+ removed the blockader. Promotion need not survive if the rear rook's recapture is verified.
- Nd3 guarded f2/b2, not e2. ...Re2 Kf3 Rxf2+ saved the rook with check; ...Rxb2 kept it protected. ...b5 defended c4, which guarded Nd3.
- Rf2/Kf4/Ng4 against Kh3: Rh2#. Ng4 guarded h2 and Kf4 protected Ng4/barred g3/g4. No adverse marks; finished 12:55. Routine conversion should remain bounded.

## T23 round 3: Black vs Sonnet, mate loss
Same setup, but a3 cxd4 cxd4 f6 exf6 Bxf6 Ne5 Ngxe5 dxe5 Bxe5 Bc5 Rfe8?! Nf3 Bd6? Bxd6 Qxd6 Qxb7 Rab8?? Qxc6 Qxc6 Rxc6.
- Rc1 pinned Nc6 to Qc7, but Ng6 could capture e5. The liquidation won P; distinguish the knights.
- Bd6 drew Q away from b7. Qxb7 attacked Ra8/Nc6; Qd6 alone guarded Nc6. Rab8 chased Q but allowed an exchange losing N. Ra8 was guarded by Re8. Secure loose defenders before chasing Q; no verified best replacement supplied.
- e3 fxe3 dxe3 Rxd2 exd2 Rxd2 removed the passer despite ...Re1 support. ...Ra3+ Kf2 Rxh3?? gxh3 lost the last rook: g2 still attacked h3. Finished 11:35; capture scans, not clock shortage.

## Earlier geometry
- T22 final: ...e6-e5 left Qd8 alone guarding d5/Ne4; Qf6?? Rxd5. ...Nxc3 Rxe5 Qd6 bxc3 lost N despite Rc8: Qe3 guarded c3. ...Rce8 Rxe8 Rxe8 Qxe8+ Qxe8 Rxe8#; Ng5 barred f7/h7.
- Classical: h4 h6 h5 Bh7; Bd3 Bxd3 Qxd3 e6, Nd7/Ngf6/Be7/O-O. T22 Sonnet: c5 Bxf6 Bxf6 dxc5 Qc7 b4 a5 a3?? axb4 axb4 Ra1#. dxc5/b4 cleared Bf6-a1/b2; scan the final recapture board.
- Bg5 pins Ne7-Qd8: Nf5?? Bxd8. Qe8 guards Be7 AND b8: Qf7?? Rb8+ Bf8 pins B. Qxf4?? gxf4 loses Q to g3.
- Re6's departure opens Qd5-g8. Rad8?? exd8=N ignores capture-promotion. Kh1 releases Nd4's pin: Qe7?? Nxe7+.
