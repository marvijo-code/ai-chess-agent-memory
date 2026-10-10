# Chess memory

## Move discipline
- Start with the enemy's last move: identify direct/discovered attacks and changed pawn controls. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate enemy pawn/knight captures and trace sliding attacks through ALL blockers. Attacking a piece does not make my destination safe.
- Name defenders and recapturers. Before moving a defender/screen, list protections lost and lines opened. Refresh pins after king OR pinning-piece moves.
- Before automatic recaptures, inspect opened lines, stronger forcing captures and newly undefended pieces. Calculate the next forcing reply and recount material.
- Forks and mate threats do not force the expected defense: test enemy checks, captures, promotions, blocks and exchanges first. A forked piece can escape with check.
- Verify actual pawn locations and BOTH forward/capture-promotions. Wins and sparse marks do not validate moves.
- Checks can be answered by capturing the checking piece, including with pawns or king. Enumerate king escapes even without queens; include own occupied squares and pawn attacks.

## Clock and conversion
- Submit before expiry. Familiar development quickly; reserve calculation for tactical turns with a firm stopping point. Fast recaptures still need an opened-line check.
- Below 90 seconds with 10-second increment, use 1-5 seconds routinely and generally stay below the increment.
- Q vs bare king: restrict it, approach with my king, deliver protected mate. Before nonchecks verify an enemy legal move remains and my queen is safe; I have flagged here.
- Choose verified simplification promptly, then support an uncontested passer with king/minor pieces. After king moves rescan mates; before pawn collection test enemy checks.
- Queen/rook batteries: queen moves can block or restore rook protection. Recheck the final board.

## Chigorin
- ...a5 vacates a6 for Nb4-a6-c5; d6 supports Nc5. Preserve Bb1; Ba2 reinforces d5 and frees Ra1. Rc1/Re1 permit ...Nd3's double-rook fork; Nc5 can screen doubled c-rooks.
- T15 semifinal White vs Sonnet: Be3?! screened Re1, permitting ...Ncxe4 Nxe4 Nxe4 to win e4. Bb1 drove the survivor away; Bg5 cleared the e-file. No best replacement for Be3 supplied.
- ...Nxd5?? Qxd5 Bxg5 Nxg5 left N for two pawns. ...Bc6 Qxd6 Qxd6 Nxd6 recovered d6 and traded queens. Later Rxe5 restored pawn equality.
- Rxe8+ won a rook because Rd7 blocked Bc6-d7-e8. Ne7+ uncovered Bb1's check on Kh7 while attacking Bc6. Name exact recapturers and test discovered checks.
- Conversion failure: Rf7/Ne5/Bd3 vs Ke6 and pawn b5: Bc4+? bxc4; Nxc4? abandoned Rf7's sole guard, allowing Kxf7. After a checking-piece loss, save other threatened material before recapturing. Ample clock and a winning position did not prevent this.
- b4 axb3 e.p. Nxb3 Nxb3 removes Nc5's c-file screen. Test Rxc7 Rxc7 Bxb3, winning Q for R, before Bxb3. ...Qxc1 Bxc1 Rxc1 Qxc1 concedes Q+R for R+B.
- Black vs DeepSeek: ...a4 b4? axb3! e.p. axb3?! clears Ra8-a1; Bb1 blocks Re1's recapture. After ...Rxa1, Qb2 attacks the rook; retreat. Qa3 permits ...Rxa3.
- Bd3 supports h7 through e4/f5/g6 once Qf5 leaves; ...Kh8 allowed Qh7#.

## Maroczy: White vs Stockfish
- Qa5 pins Nc3 to Ke1. Qd1 recaptures d4 only with d2/d3 clear; f3 supports e4, Bd2 blocks Qxd4. Be3 alone leaves e4 vulnerable.
- T15 Be3/b3 avoided the earlier c4-loss sequence. After ...Ng4, assess bishop exchanges before routine rook development: Rfc1?! Nxe3! Qxe3! conceded the bishop pair.
- Kf3? exposed Be2 to ...Bg4+. ...h5 protected g4 against Kxg4. Nxe7?? attacked Bc8 but Bg4+ Kf4 Bxe2 won my bishop; Rf7's support did not answer the skewer. ...h5 was itself marked a mistake.
- Kf4 vs Be6/Bd4 and rooks: Rxa7 allowed ...Rdf8+ Rf7 Rxf7+ Nf6 Rxf6#. Calculate checks and exits before pawn loot.
- Nxc5 dxc5 vacates d6 and creates a passer. Rxd4 cxd4 attacks Nc3; ...d3 attacks Be2. Calculate pawn recaptures/advances and the surviving rook's file before trades.

## Four Knights: Black vs Stockfish
- Nd5 Nxd5 exd5 e4 dxc6 exf3 Qxf3 dxc6 Bc4 Be6 Bxe6 fxe6 Qb3: Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4.
- Repeated ...Qh4/f4/...Bxf4 failed: Bxf4 Rxf4 removes my attacking bishop while White collects b7/c6.
- Qe4 R5f6?! Bxa7 Ra8? Qxa8+ loses a rook: e4-d5-c6-b7-a8 is clear, without a recapturer.
- Rb8/Rb1 vs Kf7: ...Qh4 threatens mate, but Qf3+ Bf6 R1b7# wins first. One rook controls escapes while its partner checks on the seventh.

## Dragon and forcing lines
- Yugoslav ...Nc4 attacks Qd2/Bb3; Bxc4! Rxc4! removes it before h5.
- ...Nxh5 g4 Nf6 Qh2 Nh5 gxh5 gxh5 Qxh5 Bxd4 Qxh7#. g4 can capture h5; g5 cannot. Nf6 guards h7; Nh5 only blocks it. Verify Qh2's path and Rh1's screens.
- ...gxh5 Bh6 abandons Be3's guard of Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for rook.
- ...Nd4 Nxd4 exd4 clears Re8+ Rxe8 Rxe8#; a pawn attack supplies no tempo against check.

## Note files
- notes/accelerated-dragon.md - Pawn inventory and capture geometry.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Dragon move order and Chigorin screens.
- notes/four-knights.md - Queen diagonals, rook safety and forcing checks.
- notes/qgd-exchange.md - Forks, intermediate captures and blockers.
- notes/ruy-lopez.md - Chigorin screens, en passant and conversion.
- notes/sicilian-maroczy.md - Checking skewers, passers and rook mates.
