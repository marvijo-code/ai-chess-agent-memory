# DeepSeek V4.1 Flash: concrete tactics

Wins and sparse marks do not validate moves. Track material, defenders and blockers independently; exploit actual errors without assuming they recur.

## T27 round 2: Black Classical Caro, mate win after queen loss
1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7! 8.Nf3 Nd7 9.Bd3 Bxd3 10.Qxd3 e6 11.Bf4 Ngf6 12.O-O-O Be7 13.Ne5 O-O 14.Bg5?? Nxe5?! 15.dxe5! Nd5?! 16.Qxd5?? Bxg5+ 17.Qd2 Bxd2+ 18.Rxd2.
- Bh7 was the only good move. Nxe5 and Nd5 were marked inaccurate; no verified best replacements supplied. The later win does not establish this sequence as sound.
- Nd5 cleared f6 from Be7-f6-g5. Qxd5 took N but allowed Bxg5+ along g5-f4-e3-d2-c1. White's anticipated Qxd5 Rxd5 exchange ignored this checking intermezzo. Qd2 blocked but let Bxd2+ win Q; Rxd2 recovered only B. Result: Black Q+2R against 2R+N, equal pawns.
18...Qg5 19.Nf5? exf5 20.Kb1 Qxg2 21.Rhd1 Qxf2?! 22.Rxf2! Rad8 23.Rxf5? Rxd1#.
- Nf5 landed on e6's pawn-capture square. exf5 removed White's last minor.
- Qg5 pinned Rd2 to Kc1 through f4/e3. Kb1 released that pin. Qxg2 attacked Rh1; Rhd1 saved it and left the other rook on d2.
- Qxf2 LOST MY QUEEN: Rd2 could capture horizontally through empty e2. Rf8 could not recapture because f7 remained. Even an available rook recapture would not justify Q for R here. Audit every enemy rook's rank as well as its file before a queen grab; the viewer's inaccuracy mark understates the material loss.
- After Rxf2, both sides had two rooks; Black had seven pawns against five, not a queen advantage. Rad8 contested Rd1 and threatened Rxd1#. Rxf5 reduced the pawn deficit but ignored mate.
- At mate, Rd1 checked Kb1 through c1; Rf2 could not capture or interpose on c1. White's a2/b2/c2 pawns occupied every second-rank flight, and Rd1 controlled a1/c1.
- No invalid Black attempts; White tried illegal Rd7 while pinned before Kb1. Finished 14:17. Qxf2 took 25 seconds: ample clock did not replace the rook scan.

## T26 round 1: White Classical Caro, mate win
h4/h5, Nf3/Bd3/Qxd3/Bf4/O-O-O/Kb1; 14.Ne5 Nxe5 15.dxe5 Nd5 16.Bc1 Qc7 17.f4 Nxf4?? 18.Bxf4.
- dxe5 opened Rd1 and attacked Nf6. Nxf4 attacked Qd3 but Bc1 captured through d2/e3; e5 screened Qc7-f4. Remove a queen's attacker when legal.
- Qd7 Qxd7 Rxd7 exchanged queens while ahead N for P. Bf6 exf6 gxf6 won B for P.
- Rxb7 Rb8 Bxb8 won R: exf6 cleared Bf4-e5-d6-c7-b8 and Rb7 guarded b8. Rxb8+ would answer the other rook's recapture.
- Rg7+ Kh8 Rh7+?? Kxh7 lost R. f7 blocked Rb7-h7; Bd4 guarded g7/h8, NOT h7. Test king captures first. This loss was unmarked.
- Ne4 Kg8 Nf6+ Kh8 Nd7+ uncovered Bd4-h8 and attacked Rf8. f6 blocked B but Nxf8 still won R; Rb7 guarded d7. Ng6 retained N with h5 support.
- Bxf6 restored g7 support; fxg2 Rg7# used Bf6 and Ng6 covering f8/h8. Finished 14:42; Rh7's failure was geometry, not time.

## T25/T24: White Classical Caro
- T25: Ne5 Nd5 Bc1 Nxe5 dxe5 Qc7 f4 Rad8 Qf3 Nc3+?? Qxc3 Rxd1 Rxd1. Qf3 captured through e3/d3; Rh1 recaptured through g1/f1/e1. Full liquidation won N.
- Bf6 exf6 Qxf4 Bxf4 gxf6 won B and Q; f4 remained on Bc1's ray.
- Nd7+ cleared Nf6 from Qc3-h8 and attacked Rf8. Kg8 Qg3+ Kh8 Nxf8 retained N. Check alternative king replies before claiming a forced line.
- T24: Ne5 Nxe5 dxe5 Nd7?? Qxd7 Qxd7 Rxd7 traded queens and won N. Rfd8 Rxd8+ Rxd8 traded rooks; Rd1+ Rxd1 then lost the last rook to Rh1.
- Nxh6+ uncovered Rd7's check; Bf4 guarded h6 and h5 barred g6. Ng4/Nxf6+ prepared Rh7# against Kh8 or Bh6# against Kf8.

## Earlier lessons
- dxe5 can open Rd1, attack Nf6 and uncover Be3 against Qb6 simultaneously. Qxd3 Rxd3 may precede saving N. Nd5 attacks Bf4; Bd2 answered.
- Nf6+ blocked Rf1's protection of Rxf7: Kxf7 was legal. Nxe8+ restored discovered check, but liquidation cost R+N for R. Giving both rooks for B was unjustified.
- Nf4 clears Qc4-e2: Bxf4 Qxe2 takes R before recovering B.
- Rh1/Bh6 can abandon Nd4: Rxd4 Qxd4 Bxh6+ wins both minors for R. DeepSeek missed it; do not reuse as sound.
