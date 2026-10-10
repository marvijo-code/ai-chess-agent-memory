# Four Knights: attacked pieces, screens and checking defenses

## T18 final: Black vs Stockfish 19, checkmate loss
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.Nd5 O-O? 6.Bxc6! dxc6 7.Nxb4! Nxe4.
- Nd5 attacked Nc6, Bb4 and Nf6. Castling left the first two vulnerable: Bxc6 exchanged White's bishop for Nc6, then Nxb4 captured Black's bishop. Nxe4 recovered only a pawn. Black was a minor down for a pawn, not merely facing central tension.
- Distinguish 5.Nd5 from 5.O-O. Castling is not an automatic developing move when several pieces are attacked. Recalculate 5...Nxd5 and its continuations; no verified best replacement was supplied here.

8.Nd3 Re8 9.O-O Qd6 10.Re1 Bf5 11.Nh4 Bg6 12.Nxg6 Qxg6 13.h3 f5 14.Kh2 Re6 15.b4 Qf6 16.Qe2 Qh4 17.g3 Qg5 18.Rb1 Rg6 19.Nxe5 Re6 20.d4 Qf4?? 21.Bxf4 Nc3 22.Qf1 Nxb1.
- d2-d4 cleared Bc1-d2-e3-f4. Qf4 pinned g3 to Kh2 but landed on the bishop's newly opened ray. The last pawn move must trigger a fresh bishop scan before a queen destination is accepted.
- Nc3 forked Qe2/Rb1 and Nxb1 recovered a rook. The full sequence still exchanged Black's queen for a rook; counterplay did not repair the original queen loss. Sparse marks omitted Qf4's direct loss.
- Later ...f4/...Ne3 placed a knight defended by f4 on f2's capture square. fxe3 fxe3 traded knight for pawn. A protected knight is not immune to a cheaper capturer; evaluate the resulting passer before investing material.
- Rf2 was supported by e3/g3, but Qxe3 and Qxg3 eliminated both passers. Rook activity needs a concrete survival/promotion calculation.

Final net: Black Kh7/Rd4/Rf4, pawn g4; White Qg6/Ne5/Re1 after 53.Qg6+.
53...Kh8 54.Nf7+! Rxf7 55.Re8+ Rf8 56.Rxf8#.
- Qg6 controlled g7, g8 and h7. Nf7 checked h8 and forced Rf4 to f7; Re8+ then forced that rook to f8, where it was captured. Connected rooks did not supply a king escape or stop the deflection sequence.
- No invalid attempts; finished with 5:01. Qf4 took 46 seconds with 10:34 left. This was a capture-scan failure with ample time. Many 30-46-second quiet moves spent clock without preventing it.

## T17 final: uncastled ...Ne7 branch, mate loss
5.Nd5 Nxd5 6.exd5 Ne7 7.Nxe5 Nxd5 8.a3 Be7 9.Nxf7 Kxf7! 10.Qh5+ Ke6 11.O-O Nf6?? 12.Re1+ Ne4 13.Rxe4+ Kf6 14.Rf4+ Ke6 15.Qf5+ Kd6 16.Rd4#.
- Kxf7 was the only good move; Black had an extra knight for a pawn but an exposed king. No forced opening loss before Nf6 established.
- Nf6 attacked Qh5 but abandoned Nd5's e3 interposition and f4 control. Test every check before assuming a queen attack gains time. No best replacement supplied.
- Ne4 blocked Re1+ but was captured with check and no longer attacked Qh5. Refresh the relocated knight's actual attacks.
- At mate Rd4 covered d5, Bb5 c6, Qf5 c5/e5/e6; Black's c7/d7/Be7 blocked exits. Finished with 14:04: checking-defense failure, not clock shortage.

## T16: ...e4 branch, flag
5.Nd5 Nxd5 6.exd5 e4 7.Qe2 Qe7 8.dxc6 exf3 9.cxd7+ Bxd7! 10.Bxd7+ Kxd7! 11.Qxe7+ Bxe7 12.gxf3 Rae8 13.d4.
- Qe7 releases e4's pin. Exf3 attacks Qe2 but White can check first. Bb4 recaptures on e7 through c5/d6. Result: Black a pawn down, not proven lost.
- Actual start 450 seconds +10; e5/Nc6 consumed 198 seconds. An unbounded turn after d4 flagged despite 3:24 at the previous move. Include output in every deadline.

## Castled branch and other geometry
5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6?! 11.Bxe6 fxe6! 12.Qb3 Qe7.
- Qe7 guards Bb4 through d6/c5 and e6 vertically; Qd5 loses Bb4. Later queen chasing conceded pawns; no certified drawn rook ending.
- Kf7 can unpin Bf8: Rxf8+ Kxe7 captures Be7 while escaping check; Kxf8 is illegal when Be7 guards f8.
- Qe4 hits a8 through d5/c6/b7. Bc3 pins Rd4 to Qf6; Rd3?? cxd3 loses R.
- Qf2+ Kh2 Qf3?? gxf3 removes the queen's own pin. Rf4 screens Rf1 and guards f8; Re4 abandons both, allowing Rxf8#.
- Qxf5 exf5 clears e6 between Re2/Re8, allowing Rxe8+.
