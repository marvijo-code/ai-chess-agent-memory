# DeepSeek V4.1 Flash: Chigorin tactics and conversion

## Tournament 2, round 1: White, checkmate win
Shared Chigorin through 13...Nc6, then:
14.Nf1 Bd7 15.Ng3 Rac8 16.Be3?! a5? 17.d5?! Nb4 18.Bb1 Rfe8 19.a3 Na6 20.Nh4 Nc5?! 21.Nhf5 Bxf5 22.Nxf5 Nxd5?? 23.exd5 Bf8.

- Be3 and d5 received inaccuracies despite the win. Development and space are reasons to consider moves, not proof they are best. No stronger alternatives were established by the supplied analysis.
- Preserve Bc2 before a3 when ...Nxc2 forks the rooks. Bb1 followed by a3 avoided the Game 2 failure.
- Ng3xf5 removed an e4 defender, repeating a familiar central-defense concern. Black's next blunder prevented this game from testing the plan fully.
- The knight capturing d5 came from f6. Nc5 could not recapture after exd5. Black lost a knight for a pawn and continued with incorrect material assumptions.

### C-file liquidation
24.Bc2 a4 25.Rc1 b4 26.axb4 Nd3 27.Bxd3 Qxc1 28.Qxc1 Rxc1 29.Rxc1.

- axb4 attacked Nc5. Its jump to d3 attacked Rc1 but allowed Bc2xd3, clearing the c-file between Rc1 and Qc7.
- Calculate through both rook recaptures. White finished with Rc1, Bd3, Be3 and Nf5 against Re8 and Bf8: two extra minor pieces, with five pawns each.
- The queen attack justified this concrete sequence; it does not make every bishop move on a blocked c-file a threat.

29...e4 30.Bc2 Re5 31.Ng3 Rxd5 32.Bxe4 Rc5 33.bxc5 dxc5 34.Bxc5 h6 35.Bxf8 Kxf8.

- Ng3 saved the attacked knight and defended e4, making Bxe4 safe after the rook left e5.
- Bxe4 attacked Rd5. ...Rc5 overlooked the b4 pawn; bxc5 won the rook. Pawn attack maps matter for rook retreats too.
- Bxc5 and Bxf8 removed Black's remaining central pawn and last piece. White retained rook, bishop and knight against pawns.

### Finish and clock
36.Ra1 f5 37.Bxf5 Kg8 38.Rxa4 Kf8 39.Ra7 Kg8 40.b4 h5 41.Nxh5 Kh8 42.Ra8#.

Ra8 checked along the eighth rank and covered g8; Bf5 covered h7; Black's g7 pawn blocked that escape. Look for coordinated mate before continuing a passer plan.

Finished with 13:04 from 15+10, avoiding the prior flag. Some routine conversion moves still consumed 26-34 seconds; shorten these when the safe move is clear.

## Earlier Game 5: Black, checkmate win
14.d5 Nb4 15.Bb1 a5! 16.a3 Na6! 17.Nf1 Bd7 18.Ng3 Nc5 19.Bg5 h6 20.Bh4?! Rfe8 21.Qd2? Nh7?? 22.Qc3?? Bxh4?? 23.Nxh4! g6 24.Rd1 Kg7 25.Qe3 Nf6 26.Qd2?? Nb3!.

- ...Rfe8 defended Be7, but that geometry did not validate ...Nh7 or ...Bxh4; both were marked blunders. Scan central captures and forcing replies.
- ...Nb3 forked Qd2/Ra1. 27.Qxa5 Rxa5 captured the queen: attacking a rook gains no tempo if that rook can take the queen.
- Later ...Qc2 attacked Rd1/Be2; Bd3 Qxd1+ won the rook. ...Nxg3+ captured a knight and uncovered Qd1's first-rank check.

### Released pin
With White Kg1/g2/h3 and Black Qg3, g2 was pinned along the g-file, so ...Rxh3 was safe from gxh3. After 42.Kf1, I played ...Qf3+? 43.gxf3 Rxf3+, losing queen for pawn. The king move released the pin; Rh3's protection of f3 did not justify the exchange. This error had no supplied mark.

Recheck the king's location before relying on a pin. Enumerate pawn captures before queen checks.

### Conversion failure to avoid
36...Qd3 took 3:11 while I had queen, two rooks, bishop and knight against rook and knight. After the queen loss, two rooks and bishop still won: ...b4 axb4 Rxa2 removed the last rook, then ...Rxb2+ Kg3 Rd3#.

DeepSeek repeatedly miscounts material and overlooks forks or pawn captures, but its errors do not validate my own moves. Use independent board geometry and finish promptly.
