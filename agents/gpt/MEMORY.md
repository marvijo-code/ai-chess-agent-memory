# Chess memory

## Move discipline
- Start with the enemy's last move: identify direct/discovered attacks. Scan checks, captures, pawn attacks, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate enemy pawn/knight captures and sliding attacks. A recapture does not justify losing queen for minor.
- Name defenders and recapturers; trace paths through ALL blockers. Before moving a defender/screen, list protections lost and lines opened. Refresh pins after king OR pinning-piece moves.
- Calculate exchanges through the recapture AND next forcing reply; recount material. Test captures of attackers/checkers, blocks and bishop exchanges before crediting threats.
- Queen attacks and exchange offers do not force cooperation: the opponent may capture, check, promote or mate elsewhere.
- Verify actual pawn locations before reusing tactics. Scan forward AND capture-promotions. Sparse marks and wins do not validate moves.
- Queenless positions contain mates. Enumerate enemy checks and king escapes, including squares occupied by my pawns.

## Clock and conversion
- Submit before expiry. Play familiar development/forced recaptures quickly; reserve calculation for tactical turns with a firm stopping point.
- Below 90 seconds with 10-second increment, use 1-5 seconds routinely and generally stay below the increment.
- Q vs bare king: restrict it, approach with my king, deliver protected mate. Before nonchecks verify an enemy legal move remains and my queen is safe; I have flagged here.
- Long thinks do not replace safety checks. Select verified simplification promptly; use an uncontested passer when the enemy king cannot reach it.

## Chigorin: T14
- Black vs DeepSeek: d5 Nb4 Bb1 a5! a3 Na6! Nf1 Nc5. ...a5 vacates a6; d6 supports Nc5. ...Bd7?! was not certified by the win.
- Bxc5 Qxc5 retained d6's blockade. Nd4?? exd4 opened the e-file, but Re8 defended Be7; Qxd4 Qxd4 won an undefended queen. Verify actual recapturers before rejecting an offered knight.
- Qc5-d4 cleared Rc8's file: Bc2 Rxc2. Rc1 allowed Qxf2+ Kh1 Qxg2#, supported by Rc2. Check mating replies before trading an attacked rook.
- White vs Sonnet: preserve Bb1, then Ba2 reinforces d5 and frees Ra1. Qe2? and Qxb5? were mistakes despite ...Kh8??/...Bd8??; no best replacements supplied. Revise this pawn raid.
- With Rc1/Re1 and enemy Nc5, test ...Nd3's double-rook fork; Red1 removed it. Nd2-c4! attacked Bb6/d6. After ...Ba7, Nxd6 hit Rc8; ...Rd8 Nb5 forked Rc7/Ba7. Black's doubled rooks were screened by its own Nc5.
- ...Nxd5 Bxd5 Rb7 Bxb7 Rxd1+ Rxd1 followed by Bxc5 Bxc5 left R+B+N vs B. Nd6 Bxd6 Rxd6 simplified to R+B vs pawns; protect f5, restrict the king with g3/h4, advance b, then Ra8 supports Qh8#.

## Maroczy: White vs Stockfish
- Qa5 pins Nc3 to Ke1. Qd1 recaptures d4 only with d2/d3 clear; f3 supports e4, Bd2 blocks Qxd4. Be3 alone leaves e4 vulnerable.
- T14 Nb3/Qd8 avoided the earlier Qd2/Qc5+ pawn-loss line, not certified best. Nxc5 dxc5 vacated d6 and created the eventual c5 passer.
- Bxd4? Rxd4? Rfd1 Rhd8 Rxd4? cxd4 attacked Nc3; ...d3 attacked Be2. Before rook trades, calculate pawn recaptures, advances and the surviving rook's file.
- ...Ba4 attacked blockading Rd1; Be2 Bxd1 Bxd1 cost rook for bishop. Audit whether another piece can attack the blockader.
- Bd5 screened Rd8; c4 guarded it. Kxd2 pinned Bd5; ...bxc4 removed its guard. Ke2 allowed ...Rxd5. Recheck a screen after the enemy capture.
- Kh5/h7: h8=Q Rh2+ Kg6 Rxh8 skewered the promotion. Ka5/a4 vs ...Kc5: f4?? Ra8#; enemy king covered b4/b5/b6, my a4 occupied an escape. Passer pushes do not answer mate.

## Four Knights: Black vs Stockfish
- Nd5 Nxd5 exd5 e4 dxc6 exf3 Qxf3 dxc6 Bc4 Be6 Bxe6 fxe6 Qb3. Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5?? loses Bb4.
- Qh4/f4/Bxf4? Bxf4 Rxf4 removed my attacking bishop while White collected b7/c6. Repeating this plan did not repair it.
- Bc3 pinned Rd4 to Qf6; Bxe3 fxe3 attacked the screen. Rd3?? cxd3 lost it and exposed Qf6. Rooks cannot capture diagonally.
- Qxd3 behind Bc3 allowed Bxg7+ Kg8 Qxd3: the bishop cleared Qb3's line with check, supported by Rf7.
- Rf4 screened Rf1 and could recapture f8; Re4 abandoned both, allowing Rxf8#. Kf6/Re7 allowed protected Bg5+ and Bxe7.
- Qf2 pinned g2 to Kh2; Qf3?? removed its OWN pin and allowed gxf3. Later capturing a promoted queen ignored Rg1/Qg6/Qh6 mate.

## Dragon and other forcing lines
- Yugoslav ...Nc4 attacks Qd2/Bb3; Bxc4! Rxc4! removes it before h5.
- ...Nxh5 g4 Nf6 Qh2 Nh5?? gxh5 gxh5 Qxh5 Bxd4 Qxh7#. g4 can capture h5; g5 cannot. Nf6 guards h7; Nh5 only blocks it, ...Ne8 abandons it. Verify Qh2's path and Rh1's screens.
- ...gxh5 Bh6?? abandoned Be3's guard of Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for rook. Test strongest replies even when missed.
- Chigorin ...Rac8/Qc7: preserve Bc2 and test ...Qxc2 Qxc2 Rxc2 when c3-c6 clear. Bd2 can block Qd1's recapture on d3.
- ...Rd8 Rxd8+ Nxd8 displaced e5's defender. ...Nd4 Nxd4 exd4 cleared Re8+ Rxe8 Rxe8#; pawn attacks supply no tempo against check.
- Caro-Kann ...g6 hxg6 fxg6 vacated f7, allowing e6/e7 with tempo. ...Rad8?? allowed exd8=N; attacking that knight ignored rook mate.

## Note files
- notes/accelerated-dragon.md - Pawn inventory and capture geometry.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Dragon move order and Chigorin screens.
- notes/four-knights.md - Queen safety and rook functions.
- notes/qgd-exchange.md - Forks, intermediate captures and blockers.
- notes/ruy-lopez.md - Chigorin routes, forks and conversion.
- notes/sicilian-maroczy.md - Pinned defenders, passers and rook skewers.
