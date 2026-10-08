# Ruy Lopez: Chigorin safety and conversion

## Shared structure
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6.

Count e4/d4 defenders before knight reroutes and rook lifts. After d5 ...Nb4, save Bc2 before a3: ...Nxc2 can fork both rooks.

## T5 round 1: White vs Sonnet, checkmate loss
14.d5 Nb4 15.Bb1! a5! 16.Nf1 Bd7 17.a3 Na6! 18.Ng3 Nc5 19.Be3 Rac8 20.Bc2 Rfe8 21.Rc1 h6 22.b4 axb4 23.axb4! Na6! 24.Bd3 Nxb4?? 25.Rxc7 Rxc7 26.Bb1 Bf8 27.Qa4?? bxa4.

### Won queen, then overlooked an unmoved pawn
- Bb1 preserved the bishop before challenging Nb4. ...a5 supported Nb4; a3 induced ...Na6, then ...Nc5 renewed pressure on e4.
- After 23...Na6, the c-file between Rc1 and Qc7 was clear except for Bc2. Bd3 uncovered the attack. ...Nxb4 attacked Bd3 but ignored Rxc7, which won queen for rook after ...Rxc7.
- Before Qa4: White Kg1/Qd1/Re1/Bb1/Be3/Nf3/Ng3, pawns d5 e4 f2 g2 h3. Black Kg8/Rc7/Re8/Bd7/Bf8/Nb4/Nf6, pawns b5 d6 e5 f7 g7 h6.
- Qa4 attacked Nb4 but landed on b5's capture square. ...bxa4 won the queen outright. No White piece could recapture on a4. Black's a-pawn had disappeared in the earlier b4 exchanges; its original b-pawn was still on b5.
- White went from Q+R against 2R, with equal minor pieces, to a full rook deficit. Reject Qa4 by checking enemy pawn attacks before considering its activity. No best replacement was supplied.
- Qa4 took 25 seconds with 14:30 remaining. Time pressure did not cause the loss.

### Defensive opportunities and fresh losses
28.Bd2 Nc2 29.Bxc2 Rxc2 exchanged bishop for knight; 33...Nb3 34.Nxb3 axb3 exchanged knights. These were ordinary trades, despite opponent comments calling captures free. Maintain my own inventory.

44.fxe5 dxe5 45.d6 Bxd6 46.Rxd6 R2c6 47.Rxc6 Rxc6 left White B+N against R+B, with three pawns against four. 49...Bc6 50.Nf5 Rxe4? 51.Ne7+! Kf8! 52.Nxc6! won the bishop by a king/bishop fork. White then had B+N against R, with two pawns against four. The tactical resource worked; it does not prove the preceding defense was optimal.

54.Kf3 Rc4 55.Na5 Ra4 56.Nb3?! Ra3 57.Ke4 Rxb3:
- Ra3 pinned Nb3 to Kf3 along a3-b3-c3-d3-e3-f3.
- Ke4 released the pin but supplied no defense to b3. The rook simply captured the knight. Before moving a king away from a pinned piece, calculate the existing capture on that piece.

59...Ke6 60.Be3 Rxe3:
- White Kg4/Bf2, pawns g2/h3; Black Rb3/Ke6, pawns e5 f6 g6 h6.
- Be3 blocked the rook's third-rank line but was undefended: Kg4 did not cover e3. ...Rxe3 won the bishop directly. An interposition needs capture safety, not merely a useful blocking role.
- Finished with 5:33 and no illegal attempts. The decisive failures were destination checks and undefended pieces.

## Earlier games
- Black vs DeepSeek: 14.Nb3 a5 15.d5 Nb4 16.a3?? Nxc2 forked Ra1/Re1 after taking Bc2; Qxc2 Qxc2 lost White's queen along the clear c-file. This blunder did not validate all earlier Black play.
- White vs Sonnet Game 3: Bb1 before a3 preserved the bishop and uncovered Rc1's attack on Qc7. Later Nh4-f5, ...Bxf5, Ng3xf5 left e4 defended only by Bb1 against Nc5/Nf6; ...Ncxe4 Bxe4 Nxe4 won it. Nb3 later overlooked ...axb3 from a4.
- White vs Sonnet Game 4: f3 supported e4; f4 removed that defender. Re3 defended e4; Rg3 abandoned it against Re8/Nc5/Nf6. The rook lift remained unsound despite later opponent blunders.
- Game 4 recovery: e5 dxe5 Nxg7+ uncovered Bb1's check; Nxe8+ uncovered Rg3's check. Nxc7 exf4 exchanged queens and left an extra rook, not an extra queen.
- Game 4 promoted on move 58, then spent 30 seconds on Qe5+, 27 on Qc5, and 18 on Qxb4. Flagged with Kc4/Qb4 against Ka1. Execute elementary queen mates promptly while checking stalemate and queen captures.
