# Chess memory

## Move discipline
- Start with the enemy's last move: identify direct/discovered attacks. Scan checks, captures, pawn attacks, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate enemy pawn/knight captures and sliding attacks. A recapture does not justify losing queen for minor.
- Name defenders and recapturers; trace ALL blockers. Before moving a defender/screen, list protections lost and lines opened. Refresh pins after king OR pinning-piece moves.
- Before an automatic recapture, inspect newly opened lines and stronger forcing captures. Calculate exchanges through the next forcing reply; recount material.
- Queen attacks do not force retreat: the opponent may capture, check, promote or mate elsewhere. Test captures of attackers/checkers, blocks and exchanges.
- Verify actual pawn locations. Scan forward AND capture-promotions. Wins and sparse marks do not validate moves.
- Queenless positions contain mates. Enumerate enemy checks and king escapes, including squares occupied by my pawns.

## Clock and conversion
- Submit before expiry. Play familiar development/verified recaptures quickly; reserve calculation for tactical turns with a firm stopping point.
- Below 90 seconds with 10-second increment, use 1-5 seconds routinely and generally stay below the increment.
- Q vs bare king: restrict it, approach with my king, deliver protected mate. Before nonchecks verify an enemy legal move remains and my queen is safe; I have flagged here.
- Select verified simplification promptly; use an uncontested passer. After each king move, rescan direct mates rather than follow a longer planned sequence.

## Chigorin: T14
- ...a5 vacates a6 for Nb4-a6-c5; d6 supports Nc5. Preserve Bb1, then Ba2 reinforces d5 and frees Ra1. ...Bd7?!, Qe2? and Qxb5? were not certified by wins.
- SF2 vs Sonnet: after ...a4, Be3?! was inaccurate; no replacement supplied. b4 axb3 e.p. Nxb3 Nxb3?? removed Nc5's c-file screen. Test Rxc7 Rxc7 Bxb3, winning Q for R, before automatic Bxb3??. ...Qxc1?? Bxc1 Rxc1 Qxc1 instead conceded Q+R for R+B.
- Qc7 attacked Bd7, guarded by Nf6. Nh5 Nxh5 Qxd7 exchanged my knight for that bishop. Qxb5 created an a-passer; a6 Nxa6 Qxa6 removed the remaining knight.
- Bd3/Qf5: once Qf5 leaves, Bd3 supports h7 through e4/f5/g6. ...Kh8 allowed direct Qh7#, bypassing the planned Qg6+ sequence.
- With Rc1/Re1 and enemy Nc5, test ...Nd3's double-rook fork; Red1 removed it. Nd2-c4 attacked Bb6/d6; Nxd6 hit Rc8, then ...Rd8 Nb5 forked Rc7/Ba7. Doubled rooks remained screened by Nc5.
- ...Nxd5 Bxd5 Rb7 Bxb7 won a rook. Trade remaining enemy pieces, protect f5, restrict the king with g3/h4, advance the distant passer; Ra8 supports Qh8#.
- Black vs DeepSeek: Bxc5 Qxc5 kept d6's blockade. Nd4?? exd4 Qxd4 Qxd4 won an undefended queen; Re8 defended Be7. Qc5-d4 cleared Rc8's file for ...Rxc2, then Qxf2+/Qxg2# with Rc2 support.

## Maroczy: White vs Stockfish
- Qa5 pins Nc3 to Ke1. Qd1 recaptures d4 only with d2/d3 clear; f3 supports e4, Bd2 blocks Qxd4. Be3 alone leaves e4 vulnerable.
- T14 Nb3/Qd8 avoided the earlier Qd2/Qc5+ pawn-loss line, not certified best. Nxc5 dxc5 vacated d6 and created the eventual c5 passer.
- Bxd4? Rxd4? Rfd1 Rhd8 Rxd4? cxd4 attacked Nc3; ...d3 attacked Be2. Before rook trades, calculate pawn recaptures, advances and the surviving rook's file.
- ...Ba4 attacked blockading Rd1; Be2 Bxd1 Bxd1 cost rook for bishop. Can another piece attack the blockader?
- Kxd2 relied on Bd5 screening Rd8; ...bxc4 removed its guard. Ke2 allowed ...Rxd5. Recheck screens after captures.
- Kh5/h7: h8=Q Rh2+ Kg6 Rxh8 skewered promotion. Ka5/a4 vs ...Kc5: f4?? Ra8#; my a4 occupied an escape. Passer pushes do not answer mate.

## Four Knights: Black vs Stockfish
- Nd5 Nxd5 exd5 e4 dxc6 exf3 Qxf3 dxc6 Bc4 Be6 Bxe6 fxe6 Qb3. Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5?? loses Bb4.
- Qh4/f4/Bxf4? Bxf4 Rxf4 removed my attacking bishop while White collected b7/c6. Repeating this plan did not repair it.
- Bc3 pinned Rd4 to Qf6; Bxe3 fxe3 attacked the screen. Rd3?? cxd3 lost it and exposed Qf6. Rooks cannot capture diagonally.
- Qxd3 behind Bc3 allowed Bxg7+ Kg8 Qxd3: the bishop cleared Qb3's line with check, supported by Rf7.
- Rf4 screened Rf1 and could recapture f8; Re4 abandoned both, allowing Rxf8#. Kf6/Re7 allowed protected Bg5+ and Bxe7.
- Qf2 pinned g2 to Kh2; Qf3?? removed its OWN pin and allowed gxf3. Capturing a promoted queen later ignored Rg1/Qg6/Qh6 mate.

## Dragon and other forcing lines
- Yugoslav ...Nc4 attacks Qd2/Bb3; Bxc4! Rxc4! removes it before h5.
- ...Nxh5 g4 Nf6 Qh2 Nh5?? gxh5 gxh5 Qxh5 Bxd4 Qxh7#. g4 can capture h5; g5 cannot. Nf6 guards h7; Nh5 only blocks it, ...Ne8 abandons it. Verify Qh2's path and Rh1's screens.
- ...gxh5 Bh6?? abandoned Be3's guard of Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for rook. Test strongest replies even when missed.
- ...Rac8/Qc7: preserve Bc2; test ...Qxc2 Qxc2 Rxc2 with c3-c6 clear. Bd2 can block Qd1's recapture on d3.
- ...Rd8 Rxd8+ Nxd8 displaced e5's defender. ...Nd4 Nxd4 exd4 cleared Re8+ Rxe8 Rxe8#; pawn attacks supply no tempo against check.
- Caro-Kann ...g6 hxg6 fxg6 vacated f7, allowing e6/e7 with tempo. ...Rad8?? allowed exd8=N; attacking that knight ignored rook mate.

## Note files
- notes/accelerated-dragon.md - Pawn inventory and capture geometry.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Dragon move order and Chigorin screens.
- notes/four-knights.md - Queen safety and rook functions.
- notes/qgd-exchange.md - Forks, intermediate captures and blockers.
- notes/ruy-lopez.md - Chigorin screens, forks and conversion.
- notes/sicilian-maroczy.md - Pinned defenders, passers and rook skewers.
