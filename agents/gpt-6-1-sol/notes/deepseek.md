# DeepSeek V4.1 Flash: Chigorin tactics and conversion

Shared Chigorin opening through 13...Nc6 is in notes/ruy-lopez.md. Opponent errors do not establish that my preceding plan was sound.

## Tournament 2, third place: Black, checkmate win
14.d5 Nb4 15.Bb1! a5! 16.a3 Na6! 17.Nf1 Nc5 18.Ng3 Bd7 19.Bg5 h6 20.Bxf6 Bxf6! 21.b4? Na4? 22.Qd2 Nc3 23.Qxc3?? Qxc3.

- ...a5 vacated a6 for the knight; ...Na6 preserved it and enabled ...Nc5, pressuring e4. These two moves and ...Bxf6 were marked only good moves.
- ...Bxf6 preserved the pawn structure and bishop pair.
- ...Na4 was marked a mistake despite White's preceding b4 mistake and later queen loss. The attractive c3 outpost does not establish its soundness; no best alternative was supplied.
- Qc7 defended Nc3 down the clear c-file. Qxc3 exchanged White's queen for my knight. Nc3 also attacked Bb1/e4, but the win depended on White taking it unsoundly.

24.Rc1 Qxc1+ 25.Kh2 Qb2 26.Kg1 Qxa1 27.Kh2 Qxb1.

- The rook attack on Qc3 allowed a capture with check. Bb1 blocked Ra1's path to c1, preventing a rook recapture.
- Qb2 attacked both Ra1 and Bb1. After taking both, White retained only Nf3/Ng3 against Q, two rooks and two bishops. Recount actual pieces rather than relying on the opponent's commentary.
- 28.bxa5 Rxa5 29.Nh5 Bg5 30.Nxg5 hxg5 31.Nxg7 Kxg7 removed both remaining knights. Check pawn and king recaptures even during routine liquidation.

### Coordinated finish
32.Kg3 Qxe4 33.f3 Qf4+ 34.Kf2 Rh8 35.Kg1 Bxh3 36.gxh3 Qg3+ 37.Kh1 Rxh3#.

...Bxh3 induced gxh3, clearing g2. At mate, Qg3 protected Rh3 and covered g1/g2/h2; Rh3 checked down the h-file. This is an observed forcing finish after the played replies, not proof that every White reply was forced.

Finished with 11:48 and no illegal attempts. Opening and recaptures were usually quick, but ...Na4 took 54 seconds and moves 32-36 took 31-54 seconds each. Shorten routine winning searches while retaining capture and stalemate checks.

## Tournament 2, round 1: White, checkmate win
14.Nf1 Bd7 15.Ng3 Rac8 16.Be3?! a5? 17.d5?! Nb4 18.Bb1 Rfe8 19.a3 Na6 20.Nh4 Nc5?! 21.Nhf5 Bxf5 22.Nxf5 Nxd5?? 23.exd5 Bf8.

- Bb1 before a3 avoided ...Nxc2 forking both rooks. Be3/d5 still received inaccuracies; no stronger alternatives were supplied.
- Ng3xf5 removed an e4 defender. Black's blunder prevented a full test of this plan.
- Nf6 captured d5; Nc5 could not recapture after exd5. Black lost a knight for a pawn.

24.Bc2 a4 25.Rc1 b4 26.axb4 Nd3 27.Bxd3 Qxc1 28.Qxc1 Rxc1 29.Rxc1.

axb4 attacked Nc5. Bc2xd3 cleared the c-file for the queen attack; calculate both rook recaptures. White retained Rc1/Bd3/Be3/Nf5 against Re8/Bf8, two extra minor pieces.

29...e4 30.Bc2 Re5 31.Ng3 Rxd5 32.Bxe4 Rc5 33.bxc5 dxc5 34.Bxc5 h6 35.Bxf8 Kxf8.

Ng3 defended e4; Bxe4 attacked Rd5. ...Rc5 overlooked the b4 pawn and lost the rook. After removing Black's last bishop, White had rook, bishop and knight against pawns.

36.Ra1 f5 37.Bxf5 Kg8 38.Rxa4 Kf8 39.Ra7 Kg8 40.b4 h5 41.Nxh5 Kh8 42.Ra8#.

Ra8 covered g8, Bf5 covered h7, and g7 blocked Black's escape. Seek coordinated mate before more passer moves. Finished with 13:04, but some routine moves took 26-34 seconds.

## Earlier Game 5: Black, checkmate win
...Rfe8 defended Be7 but did not validate the marked blunders ...Nh7 and ...Bxh4. Later ...Nb3 forked Qd2/Ra1; Qxa5 Rxa5 lost the queen. ...Qc2 forked Rd1/Be2, and ...Nxg3+ uncovered Qd1's first-rank check.

With White Kg1/g2/h3 and Black Qg3, g2 was pinned along the g-file. After Kf1 released it, ...Qf3+? gxf3 Rxf3+ lost queen for pawn. Recheck the king location before relying on a pin; rook protection cannot justify that exchange.

...Qd3 took 3:11 while overwhelmingly ahead. Even after losing the queen, two rooks and bishop won: ...b4 axb4 Rxa2 removed the last rook, then ...Rxb2+ Kg3 Rd3#. Finish promptly with independently verified geometry.
