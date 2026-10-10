# Chess memory

## Move discipline
- Start with the enemy's last move: identify direct/discovered attacks. Scan checks, captures, pawn attacks, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate enemy pawn/knight captures and sliding attacks. Trace queen diagonals explicitly; attacking a piece does not make my destination safe.
- Name defenders and recapturers; trace ALL blockers. Before moving a defender/screen, list protections lost and lines opened. Refresh pins after king OR pinning-piece moves.
- Before automatic recaptures, inspect opened lines and stronger forcing captures. Calculate the next forcing reply and recount material.
- Queen attacks and mate threats do not force the expected defense: test enemy captures, checks, promotions, blocks and exchanges.
- Verify actual pawn locations; scan forward AND capture-promotions. Wins and sparse marks do not validate moves.
- Enumerate enemy checks and king escapes even without queens; include squares occupied by my pieces/pawns.

## Clock and conversion
- Submit before expiry. Play familiar development quickly; reserve calculation for tactical turns with a firm stopping point. Fast recaptures need an opened-line check.
- Below 90 seconds with 10-second increment, use 1-5 seconds routinely and generally stay below the increment.
- Q vs bare king: restrict it, approach with my king, deliver protected mate. Before nonchecks verify an enemy legal move remains and my queen is safe; I have flagged here.
- Select verified simplification promptly; use an uncontested passer. After king moves, rescan direct mates.
- Queen/rook batteries: moving my queen onto the rook's rank may block its protection; moving it away can restore that protection. Recheck the final board.

## Chigorin
- ...a5 vacates a6 for Nb4-a6-c5; d6 supports Nc5. Preserve Bb1; Ba2 reinforces d5 and frees Ra1. T14 ...Bd7, Be3 after ...a4, Qe2/Qxb5 had adverse marks; no best replacements supplied.
- b4 axb3 e.p. Nxb3 Nxb3 removes Nc5's c-file screen. Test Rxc7 Rxc7 Bxb3, winning Q for R, before Bxb3. ...Qxc1 Bxc1 Rxc1 Qxc1 concedes Q+R for R+B.
- T15 Black vs DeepSeek: ...a4 b4? axb3! e.p. axb3?! opens Ra8-a1. Bb1 blocks Re1's recapture; ...Rxa1 wins a rook. Qb2 attacks Ra1, so retreat; Qa3 then allows ...Rxa3. Verify the recapture before opening a file.
- Rc1/Re1 permit ...Nd3's double-rook fork. Nc5 can screen doubled rooks; do not assume an open c-file.
- Bd3 supports h7 through e4/f5/g6 once Qf5 leaves; ...Kh8 allowed Qh7#.
- Black vs DeepSeek: Bxc5 Qxc5 preserves d6's blockade. Nd4 exd4 Qxd4 Qxd4 wins an undefended queen; clearing Qc5 permits ...Rxc2 and Qxf2+/Qxg2# with Rc2 support.

## Maroczy: White vs Stockfish
- Qa5 pins Nc3 to Ke1. Qd1 recaptures d4 only with d2/d3 clear; f3 supports e4, Bd2 blocks Qxd4. Be3 alone leaves e4 vulnerable.
- T14 Nb3/Qd8 avoided the earlier Qd2/Qc5+ pawn-loss line, not certified best. Nxc5 dxc5 vacated d6 and created the c5 passer.
- Bxd4 Rxd4 Rfd1 Rhd8 Rxd4 cxd4 attacks Nc3; ...d3 attacks Be2. Before rook trades, calculate pawn recaptures, advances and the surviving rook's file.
- ...Ba4 attacks blockading Rd1; Be2 Bxd1 Bxd1 costs rook for bishop. Can another piece attack the blockader?
- Kxd2 relied on Bd5 screening Rd8; ...bxc4 removed its guard. Ke2 allowed ...Rxd5. Recheck screens after captures.
- Kh5/h7: h8=Q Rh2+ Kg6 Rxh8 skewers promotion. Ka5/a4 vs ...Kc5: f4 Ra8#; my a4 occupies an escape. Passer pushes do not answer mate.

## Four Knights: Black vs Stockfish
- Nd5 Nxd5 exd5 e4 dxc6 exf3 Qxf3 dxc6 Bc4 Be6 Bxe6 fxe6 Qb3. Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4.
- Repeated ...Qh4/f4/...Bxf4 failed: Bxf4 Rxf4 removes my attacking bishop while White collects b7/c6. T14 g3 Qxd4 recovered a pawn; this does not certify the line.
- T14 Qe4 R5f6?! Bxa7 Ra8? Qxa8+ loses a rook. Qe4-a8 runs through empty d5/c6/b7; Rf8-a8 has no recapturer. Attacking Ba7 supplies no protection.
- Rb8/Rb1 vs Kf7: ...Qh4 threatens mate, but Qf3+ Bf6 R1b7# wins first. A back-rank rook controls escapes while its partner checks on the seventh.
- Bc3 pins Rd4 to Qf6; fxe3 attacks the screen. Rd3 cxd3 loses it and exposes Qf6. Qxd3 behind Bc3 allows Bxg7+ Kg8 Qxd3, clearing Qb3's line with check.
- Rf4 screens Rf1 and can recapture f8; Re4 abandons both, allowing Rxf8#. Qf2 pins g2 to Kh2; Qf3 removes its OWN pin and allows gxf3.

## Dragon and other forcing lines
- Yugoslav ...Nc4 attacks Qd2/Bb3; Bxc4! Rxc4! removes it before h5.
- ...Nxh5 g4 Nf6 Qh2 Nh5 gxh5 gxh5 Qxh5 Bxd4 Qxh7#. g4 can capture h5; g5 cannot. Nf6 guards h7; Nh5 only blocks it, ...Ne8 abandons it. Verify Qh2's path and Rh1's screens.
- ...gxh5 Bh6 abandons Be3's guard of Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for rook. Test strongest replies even when missed.
- ...Rac8/Qc7: preserve Bc2; test ...Qxc2 Qxc2 Rxc2 with c3-c6 clear. Bd2 can block Qd1's recapture on d3.
- ...Rd8 Rxd8+ Nxd8 displaces e5's defender. ...Nd4 Nxd4 exd4 clears Re8+ Rxe8 Rxe8#; pawn attacks supply no tempo against check.
- Caro-Kann ...g6 hxg6 fxg6 vacates f7, allowing e6/e7 with tempo. ...Rad8 permits exd8=N; attacking that knight ignores rook mate.

## Note files
- notes/accelerated-dragon.md - Pawn inventory and capture geometry.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Dragon move order and Chigorin screens.
- notes/four-knights.md - Queen diagonals, rook safety and forcing checks.
- notes/qgd-exchange.md - Forks, intermediate captures and blockers.
- notes/ruy-lopez.md - Chigorin screens, en passant and conversion.
- notes/sicilian-maroczy.md - Pinned defenders, passers and rook skewers.
