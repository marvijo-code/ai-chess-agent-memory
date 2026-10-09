# Chess memory

## Move discipline
- Start with the enemy's last move: identify all direct and discovered attacks. Scan checks, captures, pawn attacks, forks, promotions and mates; repeat on the proposed final board.
- Before EVERY queen move, enumerate enemy pawn and knight captures, then trace sliding attacks. A defended queen can still be lost for a pawn or minor. T13 final: ...Qf3?? g2xf3; Rf6 support only offered a recapture.
- Trace defenders and recaptures square by square, including own blockers. Before moving a defender or screen, identify every protection lost and line opened.
- Calculate exchanges through the forced recapture and next forcing reply; recount material at the end. Test captures of attacking pieces, blocks and bishop exchanges.
- Attacks on queens and exchange offers do not force cooperation: the opponent may capture, check, promote or mate elsewhere. Check is not protection; test captures of the checking piece.
- Refresh pins after king moves. Verify movement geometry and actual pawn locations before reusing tactics. Enumerate forward AND capture-promotions.
- Queenless positions still contain mates. Scan enemy checks and every king escape, including squares occupied by my pawns. Wins and sparse viewer marks do not validate moves.

## Clock and conversion
- Submit before expiry. Play familiar development and forced recaptures quickly; reserve calculation for tactical turning points with a firm stopping point.
- Below 90 seconds with 10-second increment, aim for 1-5 seconds on routine moves and generally stay below the increment.
- Q vs bare king: restrict it, approach with my king, deliver protected mate. Before nonchecks verify an enemy legal move remains and my queen is safe. I have flagged here.
- Recent losses had ample time, including over ten minutes at T13 final mate. Concrete safety checks matter more than long thinks; select verified simplification promptly.

## Four Knights: Black vs Stockfish
- Shared line: 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6 12.Qb3. Qe7 defends Bb4 via d6/c5 and e6 vertically; Qd5?? loses Bb4.
- T13 final: ...Rad8 c3 Bd6! Qxb7 Qh4 f4 Bxf4? Bxf4! Rxf4 Qxc6 Rxf1+ Rxf1. Bishop exchanges removed the h2 attack while White collected b7/c6, then a7. Count the pawn deficit and test the attack after exchanging its bishop; no best replacement for Bxf4 supplied.
- T13 round 1: ...Rd4 Re3 Bf4? Bc3! pinned Rd4 to Qf6. ...Bxe3 fxe3 attacked that screen; ...Rd3?? cxd3 lost it and exposed the queen. Imagined Rd4xc3 was illegal: rooks cannot capture diagonally.
- ...Qxd3 behind Bc3 allowed Bxg7+ Kg8 Qxd3. The checking bishop departure cleared Qb3's attack; Rf7 protected Bg7. Test enemy blocker's checks before placing a queen behind it.
- Rf4 screened Rf1 and could recapture on f8; ...Re4 abandoned both duties, allowing Rxf8#. ...Qe3+ Kh1 Qxc3 also ignored mate.
- Kf6/Re7 allowed h4, protected Bg5+, and Bxe7. A defended rook can still lose to a checking skewer.

## Dragon: White vs DeepSeek
- Yugoslav: 12...Nc4 attacks Qd2/Bb3; 13.Bxc4! Rxc4! removes it before 14.h5.
- T13: ...Nxh5 15.g4 Nf6 16.Qh2 Nh5?? 17.gxh5 gxh5 18.Qxh5 Bxd4 19.Qxh7#. Keeping g4 allowed capture of the h5 blocker; after g5 this capture is unavailable. Nh5 blocks the file but does not guard h7.
- Earlier 16.g5?! Ne8?! 17.Qh2 Rxd4?? 18.Qxh7#: Nf6 guarded h7; ...Ne8 abandoned it. Qh2 before g5 worked, but is not certified best preparation.
- Qd2-h2 requires clear e2/f2/g2. With my h-pawn gone, Rh1 supports Qxh7 after all h-file screens disappear. Answer mate threats before grabbing Nd4.
- ...gxh5 Bh6?? abandoned Be3's guard of Nd4: ...Rxd4 Qxd4 Bxh6+ wins both minors for rook. Calculate Black's strongest reply even when it misses it.

## Central exchanges and blockers
- Preserve Bc2 before a3 against ...Nb4/...Nxc2. With ...Rac8/Qc7 and clear c3-c6, test ...Qxc2 Qxc2 Rxc2 before Ng3. Rc1 reaches Qc7 only after ALL screens disappear.
- ...Rd8 Rxd8+ Nxd8 displaced Nc6 and exposed e5. ...Nd4 Nxd4 exd4 cleared the e-file for Re8+ Rxe8 Rxe8#; attacking a rook with the pawn supplied no tempo against check.
- Italian: ...d5 required e5!; ...Ne4 Nxe4 dxe4 Bxe4 followed. Be3 defended d4; Qe2 removed Qd1's guard. My e5 blocked Rd5xf5 until e6 fxe6 cleared it.
- Chigorin Bd3?? offered a bishop but Bd2 blocked Qd1xd3; ...Nxd3 won it outright. Name the recapturer and trace its path before trusting any exchange offer.

## Pawn shelter and promotion
- Caro-Kann: h5/Qg3 met ...g6? hxg6 fxg6, vacating f7 and losing ...fxe6. e6! attacked Qd7; e7 required ...Rfe8. Calculate central breakthroughs before changing the king's pawn shield.
- ...Rad8?? allowed exd8=N, capturing a rook and clearing e7; ...Qc7 Rxe8+ Kg7 Rg8# followed. Attacking the promoted knight did not answer mate.
- A promotion threat need not move the blockader: another piece may capture its attacker. Check destinations against ALL enemy pieces and pawns.

## Opponents
- Sonnet pressures central pawns but misreads blocked recaptures. Verify offered trades and expect stalemate attempts until mate.
- DeepSeek misses captures, material counts and mates; reuses plans despite changed pawn locations. Search forcing wins while checking my own safety.
- Stockfish takes exposed pawns and finds rook mates, capture-promotions and checking clearances. Calculate its best reply before chasing its queen.

## Note files
- notes/accelerated-dragon.md - Pawn inventory, capture geometry, rook safety.
- notes/berlin-endgame.md - Open-file mate, queenless king safety.
- notes/caro-kann-advance.md - Capture-promotions, destination attacks, pins.
- notes/deepseek.md - Dragon move order, mates, Chigorin screens.
- notes/four-knights.md - Bishop exchanges, queen safety, rook functions.
- notes/qgd-exchange.md - Knight forks, intermediate captures, blockers.
- notes/ruy-lopez.md - Central defense, checking forks, conversion.
- notes/sicilian-maroczy.md - Pinned defenders, retreats, promotion blockades.
