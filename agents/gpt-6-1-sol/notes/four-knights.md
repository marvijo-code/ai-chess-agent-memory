# Four Knights: defense before activity

## Shared ...Bb4 opening
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4. Both pairs of knights disappear.

After ...Be6 Bxe6 fxe6 Qb3, Qe7 defends Bb4 along e7-d6-c5-b4 and e6 vertically. Qd5?? merely attacks Qb3 and permits Qxb4.

## T5 round 3: Black vs Stockfish 19, repetition draw
13.d4 Rad8 14.c3 Bd6! 15.Qxb7 Qh4 16.f4 Rf6?! 17.g3 Qh3 18.Qxc6 Rh6 19.Qg2 Qf5 20.Bd2 Rg6 21.b3?! h5 22.b4 h4 23.Rae1 h3?! 24.Qe4.

- f4 blocks Bd6's mating diagonal. g3 attacks Qh4; Qg2 defends h2 and offers Qxh3 followed by ...Rxh3. The queen-and-rook battery did not force mate.
- Rf6 defended e6; Rh6 abandoned that defense. White collected b7/c6 while answering the attack. Avoid assuming threats compensate for lost pawns and defensive functions.
- With Rg6/Qg2, g3 is constrained on the g-file. ...h3 stopped attacking g3, let the queen leave for e4, and left h3 blocked by White's h2 pawn. Its proximity to the king did not establish a decisive threat.
- ...Rf6 and ...h3 were marked inaccuracies. No best replacements were supplied; the draw does not validate this continuation.

24...Qg4 25.a4 Re8 26.Qd3 Qh5 27.c4 Rg4 28.Re2 Qf5 29.Rf3 g5 30.Qxf5 exf5 31.Rxe8+ Kg7.

- Re8 stood behind e6, with White's Re2 on the same file. The forced queen recapture ...exf5 removed the sole blocker and allowed Rxe8+, losing a rook outright.
- Before ...Qf5, inspect the queen exchange and resulting e-file. Opening that file benefited White's rook; it did not activate mine safely. Prevent the geometry before the forced recapture.

39.Rh5 Rc6 40.Reg5+ Kf6 41.Rh6+ Kxg5 42.Rxc6.
- Kxg5 captured one White rook, but Rxc6 then captured Black's last rook. White retained a rook against none; material balance was not restored.
- White promoted g8=Q and eventually repeated with Q+R against king and pawns. Survival was practical fortune, not a theoretical draw or adequate compensation.
- Engine searches were depth 4. Do not generalize this repetition behavior to stronger Stockfish settings.
- Finished with 10:46 and no illegal attempts. Several middlegame moves took 33-54 seconds; ample time did not make the attack sound. Familiar opening moves took 2-7 seconds.

## T4 round 3: bishop trap and later mate
Different opening: 4...Nd4 5.Nxe5 Qe7 6.f4 Nxb5 7.Nxb5 d6 8.Nf3 Qxe4+ 9.Qe2 Qxe2+ 10.Kxe2 Kd8, guarding c7.

After 27.Rg1, Black Kd7/Re8/Rg8/Bh6, pawns a7 b7 c7 d6 f7 h5; White Kd3/Rf5/Rg1/Bd4, pawns a2 b2 c2 d5 h4.
- 27...Rgf8?? occupied Bh6's escape square. 28.Rf6! Bf4 29.Rxf4 won the bishop; f7 blocked Rf8's apparent recapture. Other bishop retreats were attacked. Calculate forcing attacks before occupying a friendly piece's retreat square.
- ...c5 dxc6+ was en passant, removing c5 and checking Kd7.
- Bc5+ followed by Bxf8 skewered king and rook.
- Rg2+ Kh8 Rh4# sealed the g-file and checked on h. Black's h2 pawn blocked Rh1 from helping.

## Earlier failures and repetition escapes
- ...Qh4 f4 Bxf4? Bxf4 Rxf4 Qxc6 Ref8 Qxe6+ Kh8 Qe2 Re4 Rxf8#: Rf4 blocked Rf1 and could recapture on f8; Re4 removed both functions. g7/h7 denied escapes.
- ...Qh4 f4 c5 Qxa7 cxd4 Qxd4 e5? Qc4+ Kh8 Be3 exf4 Rf3 Qe1+? Rxe1 fxe3 Rxf8+ Bxf8: Ra1 could capture Qe1 through clear b1/c1/d1. White retained Q+R against R+B; repetition did not establish compensation.
- Another line lost a rook after ...Rd1+ Kf2 Rd2+ Ke1 h6 Kxd2. Luft ignored the attacked rook. The eventual bishop-and-a-pawn repetition did not prove a theoretical draw; a8 is light.
- Rxf8+ Qxf8 Bxh6 gxh6 left White Q+R against Q. Rf1 Qe3+ Kh1 Qxc3 ignored Rf8#. Reassess the threat after the king answers a queen check.
