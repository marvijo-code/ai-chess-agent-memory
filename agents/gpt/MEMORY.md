# Chess memory

## Move discipline
- Start with the enemy's last move: identify direct/discovered attacks. Scan checks, captures, pawn attacks, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate enemy pawn/knight captures and trace sliding attacks. A defended queen still loses for a minor; recapturing does not restore its value.
- Name defenders and recapturers; trace paths through ALL blockers. Before moving a defender/screen, list protections lost and lines opened. Refresh pins after king OR pinning-piece moves.
- Calculate exchanges through the recapture AND next forcing reply; recount material. Test captures of attackers/checkers, blocks and bishop exchanges before crediting threats.
- Queen attacks and exchange offers do not force cooperation: the opponent may capture, check, promote or mate elsewhere.
- Verify geometry and actual pawn locations before reusing tactics. Scan forward AND capture-promotions. Sparse marks and wins do not validate moves.
- Queenless positions contain mates. Enumerate enemy checks and every king escape, including squares occupied by my pawns.

## Clock and conversion
- Submit before expiry. Play familiar development/forced recaptures quickly; reserve calculation for tactical turns with a firm stopping point.
- Below 90 seconds with 10-second increment, use 1-5 seconds routinely and generally stay below the increment.
- Q vs bare king: restrict it, approach with my king, deliver protected mate. Before nonchecks verify an enemy legal move remains and my queen is safe; I have flagged here.
- Recent losses ended with ample time. Long thinks do not replace safety checks; select verified simplification promptly.

## Chigorin: Black vs DeepSeek
- T14: 14.d5 Nb4 15.Bb1 a5! 16.a3 Na6! 17.Nf1 Nc5. ...a5 vacates a6 for retreat; d6 supports Nc5. 18...Bd7?!: the win does not certify this development choice.
- Bxc5 Qxc5 retained d6's blockade and guarded d4. Nd4?? exd4 opened the e-file, but Re8 defended Be7; Qxd4 Qxd4 won an undefended queen. Verify the opponent's actual recapturers before rejecting an offered knight.
- Qc5-d4 cleared Rc8's file: Bc2 Rxc2 won the bishop. With Qd4/Rc2, Rc1 allowed Qxf2+ Kh1 Qxg2#; Rc2 protected both queen captures. Check mating replies before trading an attacked rook.

## Maroczy: White vs Stockfish
- Qa5 pins Nc3 to Ke1. Qd1 recaptures d4 only with d2/d3 clear; f3 supports e4, Bd2 blocks Qxd4. Be3 alone leaves e4 vulnerable.
- T14 7.Nb3 Qd8 avoided the earlier Qd2/Qc5+ pawn-loss line; not certified best. Nxc5 dxc5 vacated d6 and created the eventual c5 passer.
- Bxd4? Rxd4? Rfd1 Rhd8 Rxd4? cxd4 attacked Nc3; ...d3 attacked Be2. Before rook trades, calculate pawn recaptures, advances and the surviving rook's file.
- ...Ba4 attacked blockading Rd1; Be2 Bxd1 Bxd1 cost rook for bishop. A blockade requiring material surrender is not solved.
- Bd5 screened Rd8 and c4 guarded it. Kxd2 pinned Bd5; ...bxc4 removed its guard. Ke2 allowed ...Rxd5. Audit a screen after the enemy's next capture.
- Kh5/h7: h8=Q Rh2+ Kg6 Rxh8 skewered the promotion behind my king. Final Ka5 with a4, ...Kc5, f4?? Ra8#: Kc5 covered b4/b5/b6 and a4 occupied an escape. Passer pushes do not answer mate.

## Four Knights: Black vs Stockfish
- 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6 12.Qb3. Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5?? loses Bb4.
- Qh4/f4/Bxf4? Bxf4 Rxf4 removed my attacking bishop while White collected b7/c6. Repeating this plan did not repair it; calculate exchanges before sacrificing pawns.
- Bc3 pinned Rd4 to Qf6; Bxe3 fxe3 attacked the screen. Rd3?? cxd3 lost it and exposed Qf6. Rd4 cannot capture c3 diagonally.
- Qxd3 behind Bc3 allowed Bxg7+ Kg8 Qxd3: the bishop cleared Qb3's line with check, supported by Rf7.
- Rf4 screened Rf1 and could recapture f8; Re4 abandoned both, allowing Rxf8#. Kf6/Re7 allowed protected Bg5+ and Bxe7.
- Qf2 pinned g2 to Kh2; Qf3?? removed its OWN pin and allowed gxf3. Rf6 support only offered a pawn recapture. Later taking a promoted queen ignored Rg1/Qg6/Qh6 mate.

## Dragon: White vs DeepSeek
- Yugoslav ...Nc4 attacks Qd2/Bb3; Bxc4! Rxc4! removes it before h5.
- ...Nxh5 g4 Nf6 Qh2 Nh5?? gxh5 gxh5 Qxh5 Bxd4 Qxh7#. g4 can capture the h5 blocker; after g5 it cannot. Nh5 blocks the file but does not guard h7.
- Nf6 guards h7; ...Ne8 abandons it. Qd2-h2 needs clear e2/f2/g2; Rh1 supports Qxh7 only after all h-file screens disappear.
- ...gxh5 Bh6?? abandoned Be3's guard of Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for rook. Test the strongest reply even when DeepSeek misses it.

## Blockers, shelter and promotion
- Chigorin: preserve Bc2 against ...Nb4/...Nxc2. With ...Rac8/Qc7 and clear c3-c6, test ...Qxc2 Qxc2 Rxc2. Rc1 reaches Qc7 only after ALL screens disappear.
- Bd3 offered a bishop but Bd2 blocked Qd1xd3; ...Nxd3 won it. Italian Be3 guarded d4; Qe2 removed Qd1's guard.
- ...Rd8 Rxd8+ Nxd8 displaced e5's defender. ...Nd4 Nxd4 exd4 cleared the e-file for Re8+ Rxe8 Rxe8#; a pawn attack supplied no tempo against check.
- Caro-Kann ...g6 hxg6 fxg6 vacated f7, allowing e6 with tempo then e7. ...Rad8?? allowed exd8=N; attacking that knight ignored rook mate.
- A promotion threat need not move its blockader: another piece can capture the attacker. Verify every destination against all enemy pieces.

## Note files
- notes/accelerated-dragon.md - Pawn inventory and capture geometry.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Dragon move order and Chigorin screens.
- notes/four-knights.md - Queen safety and rook functions.
- notes/qgd-exchange.md - Forks, intermediate captures and blockers.
- notes/ruy-lopez.md - Chigorin routes, recaptures and conversion.
- notes/sicilian-maroczy.md - Pinned defenders, passers and rook skewers.
