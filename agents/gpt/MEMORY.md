# Chess memory

## Move discipline
- Scan enemy checks, captures, pawn attacks, forks, promotions, opened lines, loose pieces and mates before choosing; repeat on the resulting board.
- When attacked, examine captures and counterthreats before retreating. Queen attacks and exchange offers do not force cooperation; the opponent may capture, promote or mate elsewhere.
- Trace defenders and recaptures square by square, including my own blockers. Before moving a defender or screen, identify every protection lost and attack released.
- Calculate exchanges through the forced recapture and next forcing move; recount material at the end. Test captures of attacking pieces and the strongest defense, including blocks and bishop exchanges.
- Check is not protection: test captures of my queen and checking piece. Refresh pins after king moves. Enumerate forward AND capture-promotions and the lines each clears.
- Verify movement geometry. Queenless positions still contain mates: scan checks and all king escapes, including squares occupied by my pawns. Wins and sparse annotations do not validate moves.
- Recheck pawn locations before reusing a tactical resource: move order can make a previously safe square capturable.

## Clock and conversion
- Submit before expiry. Play familiar development, forced recaptures and verified conversion quickly; reserve calculation for tactical turning points with a firm stopping point.
- Below 90 seconds with a 10-second increment, aim for 1-5 seconds on routine moves and generally stay below the increment.
- Q vs bare king: restrict the king, approach with my king, deliver protected mate. Before nonchecking moves verify an enemy legal move remains and my queen is safe. I have flagged here.
- Recent losses had ample time. Concrete safety checks matter more than long thinks. Simplify promptly once verified.

## Dragon: White vs DeepSeek
- Shared setup: Yugoslav through 12...Nc4 13.Bxc4! Rxc4! 14.h5. Nc4 attacked Qd2/Bb3; remove it before continuing the attack.
- T13 SF2G1: ...Nxh5 15.g4 Nf6 16.Qh2 Nh5?? 17.gxh5 gxh5 18.Qxh5 Bxd4 19.Qxh7#. Keeping g4 allowed capture of the h5 blocker. After g5, that pawn capture would be unavailable. Nh5 blocks the h-file; it does NOT defend h7.
- Qd2-h2 requires clear e2/f2/g2. With my h-pawn gone, Rh1 supports Qxh7 once intervening h-file blockers disappear. After Qxh5, Black must address mate before grabbing Nd4; do not assume all defenses fail.
- T13 round 3 instead used 16.g5?! Ne8?! 17.Qh2 Rxd4?? 18.Qxh7#. Nf6 guarded h7; ...Ne8 abandoned it. No best replacement for g5 was supplied; the later Qh2 move order is practical evidence, not certified best play.
- T12: ...gxh5 Bh6?? abandoned Be3's defense of Nd4; ...Rxd4 Qxd4 Bxh6+ wins both minors for a rook. Black chose ...Bxh6 Qxh6 Nxe4??, abandoning h5/h7; Rxh5 supported Qxh7#.

## Four Knights: Black vs Stockfish
- 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6 12.Qb3: Qe7 defends Bb4 through d6/c5 and e6 vertically; Qd5?? loses Bb4.
- T13 ...Rd4?! Re3 Bf4? Bc3! put Rd4 between Bc3 and Qf6. ...Bxe3 fxe3 attacked that screen. ...Rd3?? cxd3 lost it and exposed Qf6. Imagined ...Rxc3 from d4 was illegal: rooks cannot capture diagonally.
- ...Qxd3 behind Bc3 allowed Bxg7+ Kg8 Qxd3: checking departure cleared Qb3's attack. Rf7 protected Bg7. Calculate enemy blocker's checks before placing a queen behind it.
- Rf4 screened Rf1 and could recapture on f8; ...Re4 abandoned both duties, allowing Rxf8#. ...Qe3+ Kh1 Qxc3 also ignored mate. Kf6/Re7 allowed h4, protected Bg5+, and Bxe7: defense does not prevent a skewer.

## Central exchanges and blocked lines
- Preserve Bc2 before a3 against ...Nb4/...Nxc2. With ...Rac8/Qc7 and clear c3-c6, test ...Qxc2 Qxc2 Rxc2 before Ng3. Rc1 attacks Qc7 only after ALL screens disappear.
- Recount central defenders after exchanges. ...Rd8 Rxd8+ Nxd8 displaced Nc6 and exposed e5. ...Nd4 Nxd4 exd4 cleared the e-file for Re8+ Rxe8 Rxe8#; the pawn attack gave no tempo against check.
- Italian T12: ...d5 required e5!; ...Ne4 Nxe4 dxe4 Bxe4 followed. Be3 defended d4; Qe2 removed Qd1's defense. My e5 blocked Rd5xf5 until e6 fxe6 cleared it. Ng6+ Kg8 Ne7+ Kh7 Nxd5 won a rook while retaining the knight.
- T13 Chigorin: Bd3?? offered a bishop but Bd2 blocked Qd1xd3; ...Nxd3 won it outright. Trace the recapture path before trusting an exchange offer.

## Pawn shelter and promotion
- Caro-Kann T12: h5/Qg3 met ...g6? hxg6 fxg6, vacating f7 and forfeiting ...fxe6. e6! attacked Qd7; e7 required ...Rfe8. Calculate central breakthroughs before changing the king's pawn shield.
- ...Rad8?? allowed exd8=N, capturing a rook and clearing e7; ...Qc7 Rxe8+ Kg7 Rg8# followed. Attacking the promoted knight did not answer mate.
- A promotion threat need not move the blockader: another piece may capture its attacker. Check destinations against ALL enemy pieces and pawns.

## Opponents
- Sonnet pressures central pawns and exploits unequal exchanges, but misreads blocked recaptures. Expect stalemate attempts and resistance until mate; verify offered trades.
- DeepSeek misses captures, material counts and mates; reuses plans despite changed pawn locations. Search forcing wins while checking my own safety independently.
- Stockfish takes exposed material and finds rook mates, capture-promotions and counterattacks against pinned screens. Calculate its best reply before chasing its queen.

## Note files
- notes/accelerated-dragon.md - Capture geometry, pawn inventory, rook safety.
- notes/berlin-endgame.md - Open-file mate, queenless king safety.
- notes/caro-kann-advance.md - Capture-promotions, destination attacks, released pins.
- notes/deepseek.md - Dragon move order, mates, Chigorin screens.
- notes/four-knights.md - Bishop defense, rook functions, skewers.
- notes/qgd-exchange.md - Knight forks, intermediate captures, blockers.
- notes/ruy-lopez.md - Italian queen win, checking forks, central defense.
- notes/sicilian-maroczy.md - Pinned defenders, unsafe retreats, promotion blockades.
