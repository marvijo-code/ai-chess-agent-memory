# Ruy Lopez: Chigorin safety and exchanges

## Shared structure
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6.

Count e4/d4 defenders after every reroute, exchange, and rook lift. With Bc2 facing ...Nb4, preserve the bishop before a3: ...Nxc2 can fork both rooks.

## T5 semifinal 2, game 1: Black vs Sonnet, checkmate loss
14.Nb3 Bb7 15.Bd3 Rac8 16.Be3 Rfe8? 17.Qd2?? d5 18.exd5 Nxd5! 19.dxe5?! Nxe3?? 20.Qxe3 Nxe5?? 21.Nxe5?! Bc5?! 22.Qxc5 Qxc5 23.Nxc5 Rxc5 24.Ng4.

### Blocked defender and failed liquidation
- ...Rfe8 was marked a mistake despite its plausible central purpose. White's Qd2 was a blunder, but ...Nxe3 squandered the opportunity; no engine-approved replacement was supplied.
- Before 20...Nxe5: White Kg1/Qe3/Ra1/Re1/Bd3/Nb3/Nf3, pawn e5; Black Kg8/Qc7/Rc8/Re8/Bb7/Be7/Nc6. Other pawns remained on their wings.
- ...Nc6xe5 was not safely supported by Re8: Be7 blocked e8-e5. After Nf3xe5, ...Qc7xe5 would allow Qe3xe5, and Re8 still could not recapture through Be7.
- ...Be7-c5 attacked Qe3 and finally uncovered Re8, but White captured the attacking bishop: Qxc5 Qxc5 Nb3xc5 Rc8xc5. Ng4 saved Ne5 from the two rooks.
- White then had 2R+B+N against 2R+B: a full knight advantage. Trading the remaining bishops did not restore equality. An activity narrative cannot replace the complete exchange count.

### Missed rook win, then last-rook giveaway
24...Rd8 25.Be4 Bxe4 26.Rxe4 h5 27.Ne3 Rd2 28.Rd1 Rxb2 29.a3 Rb3 30.Ra1 f5 31.Rf4 g6 32.Rb4 Rbc3 33.Rb3?? Rc1+?? 34.Rxc1! Rxc1+ 35.Kh2 Rb1 36.Rxb1.

- Before 33...Rc1+: White Kg1/Ra1/Rb3/Ne3, pawns a3 f2 g2 h3; Black Kg8/Rc3/Rc5, pawns a6 b5 f5 g6 h5.
- Rb3 was undefended and Rc3 could capture it directly with ...Rxb3. Ra1, Ne3, and a3 supplied no recapture on b3. Compare this capture before choosing a check.
- ...Rc3-c1+ instead permitted Ra1xc1 Rc5xc1+ Kh2. White retained Rb3/Ne3 against Rc1.
- ...Rc1-b1 attacked Rb3 but landed on that rook's capture line. b2 had been cleared by ...Rxb2; Rb3xb1 won the last rook outright. Black's king and pawns did not defend b1.
- ...Rb1 had no adverse move mark, yet its loss is explicit. Checks do not force favorable trades, and an attacked rook may capture its attacker.
- Familiar opening moves took 2-8 seconds. ...Nxe5 took 40 seconds, ...Qxc5 59, and ...Rc1+ 26. Finished with 14:06 and no illegal attempts: calculation quality, not clock pressure, caused the loss.

## T5 round 1: White vs Sonnet, checkmate loss
14.d5 Nb4 15.Bb1! a5! 16.Nf1 Bd7 17.a3 Na6! 18.Ng3 Nc5 19.Be3 Rac8 20.Bc2 Rfe8 21.Rc1 h6 22.b4 axb4 23.axb4! Na6! 24.Bd3 Nxb4?? 25.Rxc7 Rxc7 26.Bb1 Bf8 27.Qa4?? bxa4.

- Bd3 cleared the last c-file blocker and uncovered Rc1's attack on Qc7. ...Nxb4 attacked the bishop but ignored the queen loss.
- Qa4 attacked Nb4 but landed on the original b5 pawn's capture square. Black's a-pawn had disappeared in the b4 exchanges; b5 remained. No recapture existed on a4. Lost the queen with 14:30 remaining.
- Later Ne7+ Kf8 Nxc6 won a bishop by a fork, but did not validate the earlier defense.
- With Ra3 pinning Nb3 to Kf3, Ke4 released the pin without defending Nb3; ...Rxb3 took it. Later Be3 interposed against Rb3 but was undefended by Kg4; ...Rxe3 took the bishop.

## Earlier recurring lessons
- Nh4-f5 Bxf5 Ng3xf5 removed an e4 defender; Nc5/Nf6 then won e4. f3-f4 and Re3-g3 also abandoned e4.
- Nb3 overlooked ...axb3 from a4. Recheck advanced pawn attacks on destinations.
- Sonnet Game 4: e5 dxe5 Nxg7+ uncovered Bb1; Nxe8+ uncovered Rg3. Nxc7 exf4 exchanged queens and left an extra rook. Count both sides' captures.
- Game 4 promoted at move 58, then spent 30 seconds on Qe5+, 27 on Qc5, and 18 on Qxb4. Flagged with queen against bare king. Execute verified elementary mates promptly.
