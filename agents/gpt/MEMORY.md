# Chess memory

## Move discipline
- Start with the enemy's last move: identify direct/discovered attacks. Scan checks, captures, pawn attacks, forks, promotions and mates; repeat on the proposed final board.
- Before every queen or rook move, enumerate enemy pawn/knight captures and trace sliding attacks. A defended queen still loses for a minor; a recapture does not restore its value.
- Name each defender and recapturer; trace its path through ALL blockers. Before moving a defender or screen, list protections lost and lines opened. Refresh pins after either king or pinning-piece moves.
- Calculate exchanges through the recapture AND next forcing reply; recount material. Test captures of attackers, blocks and bishop exchanges before crediting threats.
- Queen attacks and exchange offers do not force cooperation: the opponent may capture, check, promote or mate elsewhere. Test captures of checking pieces.
- Verify geometry and actual pawn locations before reusing tactics. Scan forward AND capture-promotions. Sparse viewer marks and wins do not validate moves.
- Queenless positions contain mates. Enumerate enemy checks and every king escape, including squares occupied by my pawns.

## Clock and conversion
- Submit before expiry. Familiar development and forced recaptures quickly; reserve calculation for tactical turning points with a firm stopping point.
- Below 90 seconds with 10-second increment, use 1-5 seconds on routine moves and generally stay below the increment.
- Q vs bare king: restrict it, approach with my king, deliver protected mate. Before nonchecks verify an enemy legal move remains and my queen is safe; I have flagged here.
- Recent losses ended with ample time. Long thinks do not replace concrete safety checks; select verified simplification promptly.

## Maroczy: White vs Stockfish
- Qa5 pins Nc3 to Ke1. Qd1 can recapture d4 only with d2/d3 clear. f3 supports e4; Bd2 blocks Qxd4. Be3 alone leaves e4 vulnerable.
- T14: 7.Nb3 Qd8 avoided the earlier pawn-losing Qd2/Qc5+ line; not certified best. 14.Nxc5 dxc5 removed Black's d-pawn, but its c5 pawn later became the passer.
- 19.Bxd4? Rxd4? 20.Rfd1 Rhd8 21.Rxd4? cxd4 attacked Nc3; ...d3 then attacked Be2. Trading rooks gave Black a protected passer and the remaining open-file rook. Calculate pawn recaptures and their next advance before claiming pressure is reduced; no best replacements supplied.
- ...Ba4 attacked the blockading Rd1. Be2 Bxd1 Bxd1 preserved the blockade but cost rook for bishop. A blockader that must surrender material is not a solved passer.
- Bd5 screened Rd8 and was guarded by c4. Kxd2 pinned Bd5 to my king; ...bxc4 removed its pawn guard. Ke2 released the pin but allowed ...Rxd5. Before capturing a passer, audit the screen's safety after the opponent's next capture.
- h8=Q with Kh5 allowed ...Rh2+ and ...Rxh8: promotion landed behind my king on the rook's checking file. Calculate checking skewers before promoting.
- Final Ka5 with my pawn a4, ...Kc5, f4?? Ra8#: b4/b5/b6 were controlled by Kc5 and a4 was occupied. A distant passer push did not answer the rook mate. Finished with 10:30; no illegal attempts.

## Four Knights: Black vs Stockfish
- 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6 12.Qb3. Qe7 defends Bb4 via d6/c5 and e6 vertically; Qd5?? loses Bb4.
- Qh4/f4/Bxf4? Bxf4 Rxf4 removed the attacking bishop while White collected b7/c6. Repeating this plan did not repair it; calculate exchanges before sacrificing pawns for an attack.
- Bc3 pinned Rd4 to Qf6; Bxe3 fxe3 attacked that screen. Rd3?? cxd3 lost it and exposed the queen. Rd4 cannot capture c3 diagonally.
- Qxd3 behind Bc3 allowed Bxg7+ Kg8 Qxd3: the bishop cleared Qb3's line with check, supported by Rf7.
- Rf4 screened Rf1 and could recapture f8; Re4 abandoned both, allowing Rxf8#. Kf6/Re7 allowed protected Bg5+ and Bxe7.
- T13 Qf2 pinned g2 to Kh2; Qf3?? removed its OWN pin and allowed gxf3. Rf6 support only offered a pawn recapture. Later capturing a promoted queen ignored Rg1/Qg6/Qh6 mate.

## Dragon: White vs DeepSeek
- Yugoslav: ...Nc4 attacks Qd2/Bb3; Bxc4! Rxc4! removes it before h5.
- ...Nxh5 g4 Nf6 Qh2 Nh5?? gxh5 gxh5 Qxh5 Bxd4 Qxh7#. With g4 still present I can capture the h5 blocker; after g5 I cannot. Nh5 blocks the file but does not guard h7.
- Nf6 guards h7; ...Ne8 abandons it. Qd2-h2 needs clear e2/f2/g2; Rh1 supports Qxh7 only after all h-file screens disappear.
- ...gxh5 Bh6?? abandoned Be3's guard of Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for rook. Test the strongest reply even when DeepSeek misses it.

## Blockers, shelter and promotion
- Chigorin: preserve Bc2 against ...Nb4/...Nxc2. With ...Rac8/Qc7 and clear c3-c6, test ...Qxc2 Qxc2 Rxc2. Rc1 reaches Qc7 only after ALL screens disappear.
- Bd3 offered a bishop but Bd2 blocked Qd1xd3; ...Nxd3 won it outright. Italian Be3 defended d4; Qe2 removed Qd1's guard.
- ...Rd8 Rxd8+ Nxd8 displaced e5's defender. ...Nd4 Nxd4 exd4 cleared the e-file for Re8+ Rxe8 Rxe8#; a pawn attack supplied no tempo against check.
- Caro-Kann ...g6 hxg6 fxg6 vacated f7 and allowed e6 with tempo, then e7. ...Rad8?? allowed exd8=N; attacking the promoted knight ignored rook mate.
- A promotion threat need not move its blockader: another piece can capture the attacker. Verify every destination against all enemy pieces.

## Note files
- notes/accelerated-dragon.md - Pawn inventory and capture geometry.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Dragon move order and Chigorin screens.
- notes/four-knights.md - Queen safety and rook functions.
- notes/qgd-exchange.md - Forks, intermediate captures and blockers.
- notes/ruy-lopez.md - Central defense and conversion.
- notes/sicilian-maroczy.md - Pinned defenders, passers and rook skewers.
