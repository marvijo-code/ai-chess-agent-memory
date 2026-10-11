# DeepSeek V4.1 Flash: concrete tactics

Wins and sparse marks do not validate moves. Track material, pawn squares, defenders and blockers independently; exploit actual errors without assuming they will recur.

## T24 round 1: White Classical Caro, mate win
1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 Nd7 9.Bd3 Bxd3 10.Qxd3 e6 11.Bf4 Ngf6 12.O-O-O Be7 13.Kb1 O-O 14.Ne5 Nxe5 15.dxe5 Nd7?? 16.Qxd7 Qxd7 17.Rxd7.
- dxe5 attacked Nf6 and cleared d4/d3 for Rd1. Nd7 was defended only by Qd8; Qxd7 Qxd7 Rxd7 traded queens and won N. Trace the supporting rook's full path. The setup was playable; no forced opening advantage established before Nd7.
- ...Rfd8 Rxd8+ Rxd8 exchanged a rook pair. Ne4 centralized the remaining knight. ...Rd1+ Rxd1 lost Black's last rook: Rh1 reached d1 through empty g1/f1/e1. Check did not protect the invader.
- ...Bf6 exf6 gxf6 gave B for P. The e5 pawn still attacked f6. DeepSeek's planned activity repeatedly ignored cheaper captures; do not treat these gifts as forced conversion.
22.Rd8+ Kg7 23.Nd6 Kh7 24.Nxf7 Kg7 25.Rd7 Kh7 26.Nxh6+ Kh8 27.Ng4 Kg8 28.Nxf6+ Kf8 29.Bh6#.
- Bf4 protected Nd6. Nxf7 left the knight undefended; ...Kg7 attacked it, so Rd7 supplied protection before continuing.
- Nxh6+ vacated f7 to uncover Rd7's check on Kh7. Bf4 guarded h6, Nh6 barred g8, and h5 barred g6; Kh8 was forced.
- Ng4 prepared Nxf6+. After that check, Kh8 permits Rh7#; Kf8 permits Bh6#. At Bh6#, Rd7 covers e7/f7/g7, Nf6 covers e8/g8, and Bh6 checks through g7. Verify every flight.
- No invalid attempts or adverse White marks; finished 15:39. Opening mostly 2-9 seconds, Qxd7 17; conversion 12-31. Routine moves can be shorter once guards and flights are verified.

## T23 round 1: White Open Sicilian, mate win
Be2/O-O/Be3/f4; ...Nxd4 Bxd4 e5 fxe5 dxe5 Bxe5 Bd6?? Qxd6 Qxd6 Bxd6.
- fxe5 answered the attack on Bd4; Bxe5 won P and attacked Nf6. Bd6 landed on the open d-file. Be5 supplied the legal recapture after the queen exchange, winning B.
- ...Nxe4 Nxe4 lost N; ...Be6 Bxf8 Rxf8 traded B for R. ...Bf5 Rxf5 lost B because f7 screened Rf8 from f5.
- Rxf7 was protected by Rf1, but Nf6+ BLOCKED that protection: Kxf7 was legal, not a forced Kh8. Nxe8+ removed R and restored the discovered check. The liquidation cost R+N for R; White retained R+B against king and pawns.
- Bg6 protected Rf7. Bf5 restricted c8/d7 while the king approached; Be4 guarded b7. Rf8# used Kb6 controlling a7/b7. Finished 14:52; calculate liquidation rather than imagined mate.

## T22 round 3: White Classical Caro, mate win
- dxe5 attacked Nf6 AND opened the d-file: ...Qxd3 Rxd3 could precede saving Nf6. ...Nd5 attacked Bf4; Bd2 answered.
- Rd7/Rxb7 were marked inaccuracies. Nd5 defended Be7; consider c4 against that defender before grabbing b7, but no best replacement established. Rxe7 alone permits Nxe7.
- ...Bf6 exf6 gxf6 gave B for P; ...Rxb3+ axb3 lost R; ...Nd5 cxd5 exd5 gave N for P. ...c5 abandoned d5, allowing Rxd5.
- Rh8# required Bg7 guarding h8/h6, Nf5 guarding Bg7, and h5 barring g6.

## Earlier Dragon/Chigorin geometry
- ...Nc4 attacks Qd2/Bb3: answer before attacking. Nb3 saved Nd4 and attacked Qa5; ignored queen attacks enabled the win.
- ...Rxc3 Qxc3 Rxc3 bxc3 left White 2R+N+B against 2B+N. Rbg7+ Bxg7 Rxg7+ Kxg7 then gave BOTH rooks for B. Preserve a rook unless the full liquidation justifies it.
- Qa7/Nd6 caged Kd8 after the a-passer promoted. Preserve tempi: ...gxh3 Ke5 h2 Ke6 h1=Q Qd7#. Check stalemate.
- dxe5 can uncover Be3's attack on Qb6 AND hit Nf6. ...Nf4 clears Qc4-e2: Bxf4 Qxe2 takes R before recovering B.
- h5 before g4 may leave g6 guarding Nh5; Rxh5 gxh5 can be an unsupported exchange sacrifice. hxg6 hxg6 clears Rh1's file.
- Rh1/Bh6 can abandon Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R. DeepSeek missed it; do not reuse as sound.
