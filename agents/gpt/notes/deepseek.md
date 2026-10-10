# DeepSeek V4.1 Flash: concrete tactics

Wins, sparse marks and explanations do not validate moves. Track material, pawn squares, defenders and blockers independently.

## T23 round 1: White Open Sicilian, mate win
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Be7 7.O-O O-O 8.Be3 d6 9.f4 Nxd4 10.Bxd4 e5 11.fxe5 dxe5! 12.Bxe5 Bd6?? 13.Qxd6 Qxd6 14.Bxd6.
- fxe5 answered the attack on Bd4 without retreating. Bxe5 removed the recapturing pawn and attacked Nf6. The setup won a pawn, but no forced opening win was established; ...dxe5 was marked only good.
- ...Bd6 landed on the open d-file. Qxd6 used Be5's legal recapture: after Qxd6 Bxd6 both queens disappeared and Black lost a bishop. An enemy queen defending a piece may permit a favorable queen exchange; trace the entire sequence.
- ...Nxe4 Nxe4 lost N outright: Nc3 could capture e4. ...Be6 Bxf8 Rxf8 traded B for R. ...Bf5 Rxf5 lost the remaining B because f7 screened Rf8 from f5. DeepSeek repeatedly miscounted recaptures; exploit actual board errors, not an assumed pattern.
19.Raf1 h6 20.Rxf7 g6 21.Nf6+ Kxf7 22.Nxe8+ Kxe8 23.Bxg6+ Kd8 24.Rf7.
- Rxf7 was initially protected by Rf1. Nf6+ then occupied f6 and BLOCKED that protection, making Kxf7 legal. My claim that Kh8 was forced was false despite no adverse move marks.
- Nxe8+ removed Black's rook and vacated f6, restoring Rf1's discovered check on Kf7. After Kxe8, the liquidation had cost R+N for R; White retained R+B against bare king and pawns. Calculate this outcome before simplifying; do not call it a forced mating line.
- Bg6 protected Rf7. Bf5 controlled c8/d7 while Kf2-e3-d4-c5-b6 approached. gxh3 removed the passer. Be4 guarded b7; at Rf8#, Kb6 controlled a7/b7 and the rook controlled b8.
- No invalid attempts; finished 14:52. Critical Qxd6 took 25 seconds; routine conversion mostly 3-13. Be4/Kb6 took 27/20: safe king routes and guard checks need not become long shuffles.

## T22 round 3: White Classical Caro, mate win
- dxe5 attacked Nf6 AND cleared the d-file: ...Qxd3 Rxd3 could precede saving Nf6. ...Nd5 then attacked Bf4; Bd2 answered it.
- Rd7/Rxb7 were marked inaccuracies. Nd5 defended Be7; examine c4 against that defender before grabbing b7, but no engine-best replacement supplied. Rxe7 alone permits Nxe7.
- ...Bf6 exf6 gxf6 gave B for P. ...Rxb3+ axb3 lost R outright; ...Nd5 cxd5 exd5 gave N for P. Check and pawn support do not establish sacrifice soundness.
- ...c5 abandoned d5's guard, permitting Rxd5. Rh8# required Bg7 guarding h8/h6, Nf5 guarding Bg7, and h5 barring g6. Rd8 alone did not establish mate.

## T21 round 3: White Dragon, mate win
- ...Ne5 h4 h5 Bg5 Nc4 Bxc4 Rxc4! Kb1? Qa5?? Nb3! Rfc8?? Nxa5. Nb3 saved Nd4 and attacked Q; no queen win before the ignored attack established. No verified replacement for Kb1 supplied.
- ...Rxc3 Qxc3 Rxc3 bxc3 left White 2R+N+B against 2B+N: White lost Q+Nc3, Black Q+2R.
- Rbg7+ Bxg7 Rxg7+ Kxg7 gave BOTH rooks for B, leaving N+5P vs 4P. Preserve a rook unless the complete liquidation justifies it.
- The a-passer won the race. Qa7/Nd6 immobilized Kd8; preserve pawn tempi: ...gxh3 Ke5 h2 Ke6 h1=Q Qd7#. Avoid stalemate.

## Earlier Chigorin and Dragon geometry
- dxe5 can uncover Be3's attack on Qb6 AND hit Nf6. ...Nf4 clears Qc4-e2: Bxf4 Qxe2 takes R before recovering B.
- ...e2 bxa4 e1=Q# uses Qe5's guard. ...Nxe3 forks Q/B but Re1+ Kh2 Be5# can take precedence.
- ...Ne5 h4 Nc4 forks Qd2/Bb3: answer before attacking. g4 before h5 permits gxh5 after ...Nxh5; h5 first can leave g6 guarding Nh5, making Rxh5 gxh5 an unsupported exchange sacrifice.
- hxg6 hxg6 clears Rh1's file. Bxg7 Kxg7 Qh6+ Kg8 Qh7# worked after errors; Kg8 was not forced.
- Rh1 or Bh6 can abandon Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R. DeepSeek missed it; do not reuse as sound.
- Nf6 guards h7; ...Nxe4 can abandon mate defense. Test immediately without expecting repeated errors.
