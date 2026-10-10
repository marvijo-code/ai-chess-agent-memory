# Chess memory

## Move discipline
- Start with the enemy's last move: identify attacks and changed pawn controls. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate pawn/knight captures and trace sliding attacks through ALL blockers. An attacking purpose does not make a destination safe.
- Name exact defenders and recapturers. Before moving a defender/screen, list guards lost and lines opened. Refresh pins after king OR pinning-piece moves.
- Before automatic recaptures, inspect opened lines and stronger forcing captures; calculate the next forcing reply and recount material.
- Forks do not force retreat: test enemy checks, captures, promotions, blocks and exchanges. A forked piece can escape with check; an attacked queen can stay while its attacker is captured.
- Track actual pawn squares and BOTH forward/capture-promotions. Checks permit pawn/king captures. Enumerate king exits, own occupied squares and pawn attacks. Wins and sparse marks do not validate moves.

## Clock and conversion
- Submit before expiry; budget output too. Book/routine moves 3-10 seconds; tactical turns usually 20-40. Set a deadline, never minutes on routine king/rook moves.
- Below 10 minutes, routine moves within increment, tactical turns generally under 30 seconds. Below 90 seconds use 1-5 seconds; retain the opened-line check.
- T15 flagged after 220 seconds on ...Ke5: the last submitted clock does not protect an unbounded next turn.
- Q vs bare king: restrict, approach with king, protected mate. Before nonchecks verify queen safety and an enemy legal move; I have flagged here.
- Choose verified simplification promptly. Support passers with king/minors; before pawn loot test checks and exits. Moving a queen/screen can remove rook protection.

## Chigorin
- ...a5 vacates a6 for Nb4-a6-c5; d6 supports Nc5. Preserve Bb1; Ba2 supports d5 and frees Ra1. Rc1/Re1 permit ...Nd3's double-rook fork; Nc5 can screen doubled c-rooks.
- Be3 screens Re1 from e4. T16 Black: after Bc2-b3, only Nd2 guarded e4; ...Ncxe4 Nxe4 Nxe4 won a pawn. Rxe4 remained illegal through Be3. However 20...Nc5 was marked ??; no verified repair/refutation supplied.
- ...a4 b4 permits ...axb3 e.p. Recompute BOTH files and bishop diagonals after recapture. Bxb3 removes e4's bishop guard; axb3 can clear Ra8-a1 while Bb1 blocks Re1's recapture. Qa3 can allow ...Rxa3.
- T16 ...f5/e4 forked Qd3/Nf3. ...Bf6 then attacked Ra1 through e5-d4-c3-b2; ...Bxa1 won the exchange. Pawn clearance and en passant made this diagonal work.
- T16 Bc2 was undefended: Nd2 blocked Qe2-d2-c2, allowing ...Rxc2. Later ...Qxf3 WON Q: Rc2 pinned g2 to Kh2, making gxf3 illegal. Verify recapture legality before calling a queen capture an exchange.
- ...Nxd5?? Qxd5 Bxg5 Nxg5 left N for two pawns. Rd7 blocked Bc6's recapture of Rxe8+. Ne7+ uncovered Bb1's check while attacking Bc6.
- Rf7/Ne5/Bd3 vs Ke6/b5: Bc4+? bxc4; Nxc4? removed Rf7's sole guard, allowing Kxf7. Save threatened material before recapturing.
- b4 axb3 e.p. Nxb3 Nxb3 removes the c-file screen: test Rxc7 Rxc7 Bxb3 before Bxb3, winning Q for R. ...Qxc1 Bxc1 Rxc1 Qxc1 loses Q+R for R+B.
- Bd3 supports h7 after Qf5 leaves; ...Kh8 allowed Qh7#.

## Maroczy: White vs Stockfish
- Qa5 pins Nc3 to Ke1. Qd1 recaptures d4 only with d2/d3 clear; f3 supports e4. Bd2 blocks Qxd4; Be3 alone leaves e4 vulnerable.
- Be3/b3 avoided earlier c4 loss. Rfc1?! Nxe3! Qxe3! conceded the bishop pair: assess ...Ng4 exchanges before routine development.
- Kf3? exposed Be2 to ...Bg4+. ...h5 guarded g4 against Kxg4. Nxe7?? Bg4+ Kf4 Bxe2: the fork failed against a checking escape; Rf7 support was irrelevant. ...h5 itself was marked a mistake.
- Kf4 vs Be6/Bd4: Rxa7 allowed ...Rdf8+ Rf7 Rxf7+ Nf6 Rxf6#. Calculate checks/exits before loot.
- Nxc5 dxc5 creates a passer. Rxd4 cxd4 attacks Nc3; ...d3 attacks Be2. Calculate recaptures, advances and the surviving rook's file.

## Four Knights: Black vs Stockfish
- Bxe6 fxe6 Qb3: Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4. ...Be6?! was inaccurate; forced ...fxe6 did not certify it.
- ...Rad8/c3/Bd6/Qxb7/Rb8?! Qxc6 lost two pawns. Queen-chasing and ...Qh4/f4/...Bxf4 did not recover them.
- Qe4 R5f6?! Bxa7 Ra8? Qxa8+ loses R: e4-d5-c6-b7-a8 is clear, without a recapturer.
- Rb8/Rb1 vs Kf7: ...Qh4 threatens mate, but Qf3+ Bf6 R1b7# wins first.
- R1e7? Rxe7! Bxe7! Kf7! Rxf8+ Kxe7! reached R+3 vs R+4. A king can capture away from the checker; keep active resistance and meet deadlines.

## Dragon: White
- Yugoslav ...Nc4 attacks Qd2/Bb3; Bxc4! Rxc4! removes it before h5.
- ...Nxh5 g4 Nf6 Qh2?! Rc8?? g5??: g5 restored protected ...Nh5 because g6 guards h5 and g5 cannot capture it. No verified replacements supplied.
- With g4 present, ...Nh5?? gxh5 gxh5 Qxh5 Bxd4 Qxh7#. Nf6 guards h7; Nh5 only blocks. ...Nxe4 abandons h7: mate before recapturing.
- ...gxh5 Bh6 abandons Be3's guard of Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R.
- Accelerated Dragon, uncastled Rh8/...h5: Bh6?? Bxh6 Qxh6 Rxh6 loses Q. Trace h8-h7-h6 BEFORE offering the exchange.
- T16 recovery: Nf4xg6+ fxg6 Rxg6 cleared f7; Bb3 guarded g8 through c4/d5/e6/f7. ...Qf8?? Rg8+ Qxg8 Rxg8# used doubled rooks; Rh7 occupied h7. Recovery did not justify the queen loss.
- ...Nd4 Nxd4 exd4 clears Re8+ Rxe8 Rxe8#; a pawn attack supplies no tempo against check.

## Note files
- notes/accelerated-dragon.md - Rook capture geometry and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Dragon move orders and blockers.
- notes/four-knights.md - Opening losses, liquidation and deadlines.
- notes/qgd-exchange.md - Forks, intermediate captures and blockers.
- notes/ruy-lopez.md - Chigorin screens, en passant and pinned recaptures.
- notes/sicilian-maroczy.md - Checking skewers, passers and rook mates.
