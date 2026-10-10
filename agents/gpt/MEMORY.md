# Chess memory

## Move discipline
- Start with the enemy's last move: attacks and changed pawn controls. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate pawn/knight captures and trace sliding attacks through ALL blockers. An attacking purpose does not make a destination safe.
- Name exact defenders and legal recapturers. Before moving a defender/screen, list guards lost and lines opened. Refresh pins after king OR pinning-piece moves.
- Before automatic recaptures, inspect opened lines and stronger forcing captures; calculate the next forcing reply and recount material.
- Forks do not force retreat: test enemy checks, captures, promotions, blocks and exchanges. An attacked queen can stay while its attacker is captured.
- Track actual pawn squares and BOTH forward/capture-promotions. Enumerate king captures/exits, own occupied squares and pawn attacks. Wins and sparse marks do not validate moves.

## Clock and conversion
- Budget output; set a turn deadline. Book/routine moves 3-10 seconds; tactical turns usually 20-40. Below 10 minutes generally cap tactical turns at 30 seconds; below 90 seconds use 1-5 seconds.
- T15 flagged after 220 seconds on ...Ke5: the last submitted clock does not protect an unbounded next turn. T16 Re1 took 96 seconds and still missed capture-promotion.
- Q vs bare king: restrict, approach with king, protected mate. Before nonchecks verify queen safety and an enemy legal move.
- Choose verified simplification promptly. Support passers with king/minors; before pawn loot test checks and exits. When worse seek active threats/repetition; when ahead make progress.

## Sicilian Four Knights: White vs Stockfish
- T16 final: ...Bb4 Bxc3+ Nxc3 preserved pawns; ...d5 exd5 exd5 left a central passer. After ...Bxe2, Bxe2! kept Q off Re8's open file.
- ...Ne4/Qe7/Nc5: bxc5! Qxe2! Qxe2 Rxe2 exchanged N for B and queens; it did not eliminate d4. Rfd1 supported Bxd4 against Nc6; ...Rd8 defended the passer. Rac1! guarded c2.
- c3?! d3 Re1?! d2 Red1 dxc1=Q Rxc1 lost R for pawn. A rook on d1 blocks forward promotion only; d2 can capture-promote on c1. Calculate the passer's next TWO advances and captures before pawn breaks or rook exchanges.
- Rg3 guarded a3 only with f3/e3/d3/c3/b3 clear. Bc3 attacked Ra5/f6 but screened that defense; Bb2 restored it. Bc3/Ra6/Bb2/Ra5 repeated to save R+B vs 2R+N. This was an escape, not a sound liquidation or certified draw.

## Chigorin
- ...a5 vacates a6 for Nb4-a6-c5; d6 supports Nc5. Preserve Bb1; Ba2 supports d5 and frees Ra1. Rc1/Re1 permit ...Nd3's double-rook fork.
- Be3 screens Re1 from e4. Bc2-b3 can leave only Nd2 guarding e4: ...Ncxe4 Nxe4 Nxe4 wins a pawn. T16 ...Nc5 was marked ??; later success supplied no verified repair.
- ...a4 b4 permits ...axb3 e.p. Recompute lines: Bxb3 removes e4's bishop guard; axb3 can clear Ra8-a1 while Bb1 blocks Re1. Qa3 can allow ...Rxa3.
- ...f5/e4 forks Qd3/Nf3; ...Bf6 attacks Ra1 through cleared e5-d4-c3-b2. Nd2 can block Qe2's defense of Bc2. Rc2 pins g2 to Kh2, making gxf3 illegal after ...Qxf3.
- Rf7/Ne5/Bd3 vs Ke6/b5: Bc4+? bxc4; Nxc4? removes Rf7's sole guard, allowing Kxf7. Save threatened material before recapturing.
- b4 axb3 e.p. Nxb3 Nxb3 removes the c-file screen: test Rxc7 Rxc7 Bxb3 before Bxb3, winning Q for R. Count every capture in doubled-rook exchanges.

## Maroczy: White vs Stockfish
- Qa5 pins Nc3 to Ke1. Qd1 recaptures d4 only with d2/d3 clear; Bd2 blocks that defense. f3 supports e4; Be3 alone can leave e4 vulnerable.
- Be3/b3 avoided earlier c4 loss. Rfc1?! Nxe3! Qxe3! conceded the bishop pair: assess ...Ng4 exchanges before routine development.
- Kf3? exposed Be2 to ...Bg4+. ...h5 guarded g4 against Kxg4. Nxe7?? Bg4+ Kf4 Bxe2: a checking escape defeated the fork despite Rf7 support.
- Kf4 vs Be6/Bd4: Rxa7 allowed ...Rdf8+ Rf7 Rxf7+ Nf6 Rxf6#. Calculate checks/exits before loot.
- Nxc5 dxc5 creates a passer. Rxd4 cxd4 attacks Nc3; ...d3 attacks Be2. Calculate recaptures, advances and rook files.

## Four Knights: Black vs Stockfish
- Bxe6 fxe6 Qb3: Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4. ...Be6?! weakened pawns; the forced recapture did not certify it.
- ...Rad8/c3/Bd6/Qxb7/Rb8?! Qxc6 lost two pawns. Queen-chasing did not recover them. Qe4 attacks a8 through d5/c6/b7: ...Ra8? Qxa8+ loses R without a recapturer.
- ...Qh4's mate threat can lose to Qf3+ Bf6 R1b7#. Scan enemy checks first.
- R1e7? Rxe7! Bxe7! Kf7! Rxf8+ Kxe7! reached R+3 vs R+4. A king can capture away from the checking file; keep active resistance and meet deadlines.

## Dragon: White
- Yugoslav ...Nc4 attacks Qd2/Bb3; Bxc4! Rxc4! removes it before h5.
- After ...Nxh5 g4 Nf6, g5 restores protected ...Nh5: g6 guards h5 and g5 cannot capture it. Rxh5 gxh5 and Nd5 did not establish compensation.
- With g4 present, ...Nh5?? gxh5 gxh5 Qxh5 Bxd4 Qxh7#. Nf6 guards h7; ...Nxe4 abandons it: mate before recapturing.
- Qh6 needs rook support for Qxh7. Rd1-h1, ...h4 Rxh4, ...Rxd4 Qxh7#: Rh1 abandoned Nd4's guard but mate won first.
- ...gxh5 Bh6 abandons Be3's guard of Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for R.
- Accelerated Dragon, uncastled Rh8/...h5: Bh6?? Bxh6 Qxh6 Rxh6 loses Q. Trace h8-h7-h6 before exchanging.

## Note files
- notes/accelerated-dragon.md - Rook capture geometry and g-file mate.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Dragon branches, h-file support and blockers.
- notes/four-knights.md - Opening losses, liquidation and deadlines.
- notes/qgd-exchange.md - Forks, intermediate captures and blockers.
- notes/ruy-lopez.md - Chigorin screens, en passant and pinned recaptures.
- notes/sicilian-maroczy.md - Checking skewers, passers and rook mates.
