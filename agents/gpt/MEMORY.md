# Chess memory

## Move discipline
- Start with the enemy's last move: identify direct/discovered attacks and changed pawn controls. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before queen/rook moves, enumerate enemy pawn/knight captures and trace sliding attacks through ALL blockers. Attacking a piece does not make my destination safe.
- Name defenders and recapturers. Before moving a defender/screen, list protections lost and lines opened. Refresh pins after king OR pinning-piece moves.
- Before automatic recaptures, inspect opened lines, stronger forcing captures and newly undefended pieces. Calculate the next forcing reply and recount material.
- Forks and mate threats do not force the expected defense: test enemy checks, captures, promotions, blocks and exchanges. A forked piece can escape with check.
- Verify actual pawn locations and BOTH forward/capture-promotions. Wins and sparse marks do not validate moves.
- Checks can be answered by capturing the checker, including with pawn or king. Enumerate king escapes, own occupied squares and pawn attacks even without queens.

## Clock and conversion
- Submit before expiry; budget output too. Book/routine moves 3-10 seconds; tactical turns usually 20-40. Set a turn deadline; never spend minutes on a routine king/rook move.
- Below 10 minutes, routine moves within the increment, tactical turns generally below 30 seconds. Below 90 seconds use 1-5 seconds. Fast recaptures still need an opened-line check.
- T15 flagged after spending 220 seconds on ...Ke5. The clock on the last submitted move is no protection against an unbounded next turn.
- Q vs bare king: restrict it, approach with king, deliver protected mate. Before nonchecks verify an enemy legal move remains and queen safety; I have flagged here.
- Choose verified simplification promptly; support an uncontested passer with king/minors. After king moves rescan mates; before pawn collection test enemy checks.
- Queen/rook batteries: queen moves can block or restore rook protection. Recheck the final board.

## Chigorin
- ...a5 vacates a6 for Nb4-a6-c5; d6 supports Nc5. Preserve Bb1; Ba2 reinforces d5 and frees Ra1. Rc1/Re1 permit ...Nd3's double-rook fork; Nc5 can screen doubled c-rooks.
- Be3?! screened Re1, permitting ...Ncxe4 Nxe4 Nxe4 to win e4. Bb1 drove the survivor away; Bg5 cleared the e-file. No verified opening replacement supplied.
- ...Nxd5?? Qxd5 Bxg5 Nxg5 left N for two pawns. ...Bc6 Qxd6 Qxd6 Nxd6 traded queens; Rxe5 restored pawn equality.
- Rxe8+ won a rook because Rd7 blocked Bc6-d7-e8. Ne7+ uncovered Bb1's check on Kh7 while attacking Bc6. Name exact recapturers and discovered checks.
- Rf7/Ne5/Bd3 vs Ke6/b5: Bc4+? bxc4; Nxc4? abandoned Rf7's sole guard, allowing Kxf7. After an unexpected checking-piece loss, save threatened material before recapturing.
- b4 axb3 e.p. Nxb3 Nxb3 removes the c-file screen. Test Rxc7 Rxc7 Bxb3 before Bxb3: wins Q for R. ...Qxc1 Bxc1 Rxc1 Qxc1 concedes Q+R for R+B.
- Black vs DeepSeek: ...a4 b4? axb3! e.p. axb3?! clears Ra8-a1; Bb1 blocks Re1's recapture. Qb2 attacks Ra1: retreat. Qa3 permits ...Rxa3.
- Bd3 supports h7 through e4/f5/g6 once Qf5 leaves; ...Kh8 allowed Qh7#.

## Maroczy: White vs Stockfish
- Qa5 pins Nc3 to Ke1. Qd1 recaptures d4 only with d2/d3 clear; f3 supports e4, Bd2 blocks Qxd4. Be3 alone leaves e4 vulnerable.
- Be3/b3 avoided the earlier c4 loss. After ...Ng4, assess bishop exchanges before routine rook development: Rfc1?! Nxe3! Qxe3! conceded the bishop pair.
- Kf3? exposed Be2 to ...Bg4+. ...h5 protected g4 against Kxg4. Nxe7?? attacked Bc8 but Bg4+ Kf4 Bxe2 won Be2; Rf7 support did not answer the skewer. ...h5 was itself marked a mistake.
- Kf4 vs Be6/Bd4 and rooks: Rxa7 allowed ...Rdf8+ Rf7 Rxf7+ Nf6 Rxf6#. Calculate checks and exits before pawn loot.
- Nxc5 dxc5 vacates d6 and creates a passer. Rxd4 cxd4 attacks Nc3; ...d3 attacks Be2. Calculate pawn recaptures/advances and the surviving rook's file before trades.

## Four Knights: Black vs Stockfish
- Bxe6 fxe6 Qb3: Qe7 guards Bb4 via d6/c5 and e6 vertically; Qd5 loses Bb4. ...Be6?! was inaccurate; required ...fxe6! did not certify the setup.
- ...Rad8/c3/Bd6/Qxb7/Rb8?! Qxc6! lost two pawns; queen-chasing did not repair it. ...Qh4/f4/...Bxf4 failed too: Bxf4 Rxf4 removed my bishop while White collected b7/c6.
- Qe4 R5f6?! Bxa7 Ra8? Qxa8+ loses a rook: e4-d5-c6-b7-a8 is clear, without a recapturer.
- Rb8/Rb1 vs Kf7: ...Qh4 threatens mate, but Qf3+ Bf6 R1b7# wins first. One rook controls escapes while its partner checks on the seventh.
- R1e7? Rxe7! Bxe7! Kf7! Rxf8+ Kxe7! reached R+3 vs R+4. Capturing the bishop escaped check; do not assume a checking rook must be captured. Keep active-rook resistance and meet deadlines.

## Dragon and forcing lines
- Yugoslav ...Nc4 attacks Qd2/Bb3; Bxc4! Rxc4! removes it before h5.
- ...Nxh5 g4 Nf6: Qh2 succeeded against errors, but T16 marked it ?!. After ...Rc8??, g5?? restored ...Nh5: g6 guards the blocker and g5 cannot capture h5. Test this defense; no verified best replacement supplied.
- With g4 still present, ...Nh5?? gxh5 gxh5 Qxh5 Bxd4 Qxh7#. Nf6 guards h7; Nh5 blocks the file. T16 ...Nxe4?? abandoned h7: Qxh7# before recapturing. A win does not validate g5.
- ...gxh5 Bh6 abandons Be3's guard of Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for rook.
- ...Nd4 Nxd4 exd4 clears Re8+ Rxe8 Rxe8#; a pawn attack supplies no tempo against check.

## Note files
- notes/accelerated-dragon.md - Pawn inventory and capture geometry.
- notes/berlin-endgame.md - Open-file mate and king safety.
- notes/caro-kann-advance.md - Promotions, destinations and pins.
- notes/deepseek.md - Dragon move orders and defensive blockers.
- notes/four-knights.md - Opening losses, liquidation and clock deadlines.
- notes/qgd-exchange.md - Forks, intermediate captures and blockers.
- notes/ruy-lopez.md - Chigorin screens, en passant and conversion.
- notes/sicilian-maroczy.md - Checking skewers, passers and rook mates.
