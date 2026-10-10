# Chess memory

## Move discipline
- Start with the enemy's last move: identify direct/discovered attacks and changed pawn controls. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate enemy pawn/knight captures and sliding attacks. Trace queen diagonals explicitly; attacking a piece does not make my destination safe.
- Name defenders and recapturers; trace ALL blockers. Before moving a defender/screen, list protections lost and lines opened. Refresh pins after king OR pinning-piece moves.
- Before automatic recaptures, inspect opened lines and stronger forcing captures. Calculate the next forcing reply and recount material.
- Forks, queen attacks and mate threats do not force the expected defense: test enemy checks, captures, promotions, blocks and exchanges FIRST. A forked piece can escape with check and win something else.
- Verify actual pawn locations; scan forward AND capture-promotions. Wins and sparse marks do not validate moves.
- Enumerate enemy checks and king escapes even without queens. Include my occupied squares and attacks by pawns; king activity requires safe exits.

## Clock and conversion
- Submit before expiry. Play familiar development quickly; reserve calculation for tactical turns with a firm stopping point. Fast recaptures need an opened-line check.
- Below 90 seconds with 10-second increment, use 1-5 seconds routinely and generally stay below the increment.
- Q vs bare king: restrict it, approach with my king, deliver protected mate. Before nonchecks verify an enemy legal move remains and my queen is safe; I have flagged here.
- Select verified simplification promptly; use an uncontested passer. After king moves, rescan direct mates. Before collecting pawns with an active rook, test enemy rook checks against my king.
- Queen/rook batteries: queen moves can block or restore rook protection. Recheck the final board.

## Chigorin
- ...a5 vacates a6 for Nb4-a6-c5; d6 supports Nc5. Preserve Bb1; Ba2 reinforces d5 and frees Ra1. Earlier Be3/Qe2/Qxb5 had adverse marks; no best replacements supplied.
- b4 axb3 e.p. Nxb3 Nxb3 removes Nc5's c-file screen. Test Rxc7 Rxc7 Bxb3, winning Q for R, before Bxb3. ...Qxc1 Bxc1 Rxc1 Qxc1 concedes Q+R for R+B.
- T15 Black vs DeepSeek: ...a4 b4? axb3! e.p. axb3?! opens Ra8-a1. Bb1 blocks Re1's recapture; ...Rxa1 wins a rook. Qb2 attacks Ra1, so retreat; Qa3 then allows ...Rxa3.
- Rc1/Re1 permit ...Nd3's double-rook fork. Nc5 can screen doubled rooks; do not assume an open c-file.
- Bd3 supports h7 through e4/f5/g6 once Qf5 leaves; ...Kh8 allowed Qh7#.
- Bxc5 Qxc5 preserves d6's blockade. Nd4 exd4 Qxd4 Qxd4 wins an undefended queen; clearing Qc5 permits ...Rxc2 and protected Qxf2+/Qxg2#.

## Maroczy: White vs Stockfish
- Qa5 pins Nc3 to Ke1. Qd1 recaptures d4 only with d2/d3 clear; f3 supports e4, Bd2 blocks Qxd4. Be3 alone leaves e4 vulnerable.
- T15: 9.Be3 and 13.b3 avoided the earlier c4-loss sequence. After ...Ng4, assess exchanges before routine development: Rfc1?! Nxe3! Qxe3! conceded the bishop pair. No best replacement supplied.
- T15 Kf3? exposed Be2 to ...Bg4+. ...h5 protected g4 against Kxg4. Nxe7?? attacked Bc8, but Bg4+ Kf4 Bxe2 won my bishop. Rf7's support of Ne7 did not answer the skewer; ...h5 was itself marked a mistake, so the loss was not forced beforehand.
- T15 Kf4 vs Be6/Bd4 and rooks: Rxa7 allowed ...Rdf8+ Rf7 Rxf7+ Nf6 Rxf6#. Pawn loot did not answer the king's confinement; calculate checks and exits before grabbing.
- Nxc5 dxc5 vacates d6 and creates a c5 passer. Bxd4 Rxd4 Rfd1 Rhd8 Rxd4 cxd4 attacks Nc3; ...d3 attacks Be2. Calculate pawn recaptures, advances and the surviving rook's file before trades.
- ...Ba4 attacks blockading Rd1; Be2 Bxd1 Bxd1 costs rook for bishop. Kxd2 relied on Bd5 screening Rd8; ...bxc4 removed its guard, then ...Rxd5 won it.
- Kh5/h7: h8=Q Rh2+ Kg6 Rxh8 skewers promotion. Ka5/a4 vs ...Kc5: f4 Ra8#; my a4 occupies an escape.

## Four Knights: Black vs Stockfish
- Nd5 Nxd5 exd5 e4 dxc6 exf3 Qxf3 dxc6 Bc4 Be6 Bxe6 fxe6 Qb3. Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4.
- Repeated ...Qh4/f4/...Bxf4 failed: Bxf4 Rxf4 removes my attacking bishop while White collects b7/c6. T14 g3 Qxd4 recovered a pawn, not proof of the line.
- Qe4 R5f6?! Bxa7 Ra8? Qxa8+ loses a rook: e4-d5-c6-b7-a8 is clear, and Ra8 has no recapturer.
- Rb8/Rb1 vs Kf7: ...Qh4 threatens mate, but Qf3+ Bf6 R1b7# wins first. One rook controls escapes while its partner checks on the seventh.
- Bc3 pins Rd4 to Qf6; fxe3 attacks the screen. Rd3 cxd3 loses it and exposes Qf6. Qxd3 behind Bc3 allows Bxg7+ Kg8 Qxd3, clearing Qb3's line with check.
- Rf4 screens Rf1 and can recapture f8; Re4 abandons both, allowing Rxf8#. Qf2 pins g2 to Kh2; Qf3 removes its OWN pin and allows gxf3.

## Dragon and other forcing lines
- Yugoslav ...Nc4 attacks Qd2/Bb3; Bxc4! Rxc4! removes it before h5.
- ...Nxh5 g4 Nf6 Qh2 Nh5 gxh5 gxh5 Qxh5 Bxd4 Qxh7#. g4 can capture h5; g5 cannot. Nf6 guards h7; Nh5 only blocks it, ...Ne8 abandons it. Verify Qh2's path and Rh1's screens.
- ...gxh5 Bh6 abandons Be3's guard of Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for rook.
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
- notes/sicilian-maroczy.md - Checking skewers, passers and rook mates.
