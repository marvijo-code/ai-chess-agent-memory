# DeepSeek V4.1 Flash: tactics and conversion

Shared Chigorin structure through 13...Nc6 is in notes/ruy-lopez.md. Opponent errors and wins do not validate my preceding play.

## Tournament 4, round 1: Black, checkmate win
14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.Rc1 Rfc8 18.Bb1 Qb7 19.Qe2 h6 20.Qxb5?? Qxb5.

- ...a5-a4 displaced Nb3. ...Rfc8 contested the open file while Ra8 supported a4. Bb1 uncovered Rc1's attack on Qc7; ...Qb7 removed the queen from that line and defended b5.
- Qxb5 lost White's undefended queen for a pawn; White had no recapture after ...Qxb5. Its explanation treated losing a queen as winning a pawn.
- No Black moves received marks. This does not establish opening optimality or excuse the later queen and knight losses.

21.Bc2 Nxd4 22.Nxd4 exd4 23.Bxd4 Be6 24.Ba7 Rxa7 25.Nf3 Rcc7 26.Rb1 d5 27.exd5 Nxd5 28.Red1 Rxc2 29.Rd2 Rxd2 30.Nxd2 Qd3 31.Re1 Qxd2 32.Kh2 Qxe1.

- Ba7 hung a bishop to Ra8. After White's rook left c1, Bc2 lacked protection and ...Rxc2 collected it. ...Rxd2 exchanged rooks to reduce counterplay.
- Qd3 attacked Rb1 along d3-c2-b1 and Nd2 down the d-file. Re1 saved the rook temporarily; ...Qxd2 then attacked it along d2-e1. White left it there and ...Qxe1 captured it.

### My unmarked capture failures
33.Kg3 Qe3+? 34.fxe3 Nxe3 35.Kf3 Nf5 36.b3 axb3 37.axb3 Bxb3 38.g4 Nh4+ 39.Kg3 Bd6+? 40.Kxh4.

- Qe3 was protected by Nd5, but f2xe3 still exchanged my queen for a pawn. Protection supplies a recapture; it does not prevent an unfavorable exchange. Scan enemy pawns before queen checks.
- Nh4 was protected by Be7 along e7-f6-g5-h4. ...Bd6+ removed that protection and Kg3 could capture the knight on h4. Reconstruct defenders after every move, including checking moves.
- Both losses were unnecessary giveaways; no forcing justification was established. Rook and two bishops still won against White's remaining pawns.
- ...Qe3+ took 53 seconds with over twelve minutes left. Calculation must explicitly test captures of the checking piece.

40...Kh7 41.g5 Ra4+ 42.Kh5 g6#.

- Ra4 controlled g4/h4, White's g5 pawn occupied g5, and Kh7 guarded g6/h6. The g6 pawn checked Kh5 and was protected by the king. This rook/pawn/king net finished the game.
- Finished with 11:04 and no illegal attempts. Familiar opening moves were quick, but several routine winning moves took 39-53 seconds.

## Tournament 3, round 1: Black, checkmate win
14.d5 Nb8 15.Nf1 Nbd7 16.Ng3 Nc5 17.Bg5 h6 18.Bxf6 Bxf6! 19.Nd2 Bd7 20.Nb3 Nxb3 21.Bxb3 Rac8 22.Qe2 a5 23.Rac1 Qb6?! 24.Qc2?? Rxc2 25.Bxc2.

- ...Nb8-d7-c5 regrouped actively; no mark proves it best. ...Bxf6 retained bishop pair and pawn structure.
- ...Qb6 cleared Rc8's file and pinned f2 to Kg1, but was inaccurate. White attempted illegal f4, then hung its queen on c2.
- ...Bg5 saved the bishop while attacking Rc1 along g5-f4-e3-d2-c1. ...Bxc1 won rook for bishop. Later Bd3 cleared c2 and exposed Rc1 to ...Rxc1.
- Nf6+ was capturable by Qf2 on the clear f-file. Finish ...Qf4+ g3 Qf2#: queen controlled the second rank/g3; Rc1 covered g1/h1. Finished with 14:09.

## Earlier recurring errors and useful patterns
- T2 third place: ...Nb4 Bb1 a5 a3 Na6 preserved the knight; ...Bxf6 was necessary. ...Na4? was still a mistake despite later Qxc3?? Qxc3, with Qc7 defending Nc3.
- ...Qxc1+ exploited Bb1 blocking Ra1's recapture; Qb2 forked Ra1/Bb1. Shorten routine conversion searches, which reached 31-54 seconds.
- T2 as White: Bb1 before a3 avoided ...Nxc2's rook fork. Ng3xf5 removed an e4 defender; Black's ...Nxd5?? exd5 lost Nf6 because Nc5 could not recapture. Its blunder did not validate my center defense.
- Earlier Black game: ...Nb3 forked Qd2/Ra1; Qxa5 Rxa5 lost White's queen. ...Qc2 forked Rd1/Be2.
- Kf1 released the g2 pin: ...Qf3+? gxf3 Rxf3+ lost my queen for a pawn despite Rh3 protection. Recheck pins and all captures before queen checks.
- ...Qd3 once took 3:11 while overwhelmingly ahead. Continue with verified captures and mating geometry promptly.
