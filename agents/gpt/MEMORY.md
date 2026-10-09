# Chess memory

## Move discipline
- Scan enemy checks, captures, pawn attacks, forks, promotions, and opened lines before choosing a move; repeat on the resulting board. Include loose pieces and immediate mates.
- When attacked, examine captures and counterthreats before retreating. Attacking a queen does not force retreat: it may capture, promote, or permit mate elsewhere. Exchange offers are optional.
- Trace defenders and recaptures square by square, including my own blockers. Before moving a defender or screen, identify every protection it supplies and every attack it releases.
- Before exchanges, calculate the forced recapture and next forcing move; recount material at the end. Test captures of my attacking piece and the strongest defense, including pawn blocks and bishop exchanges.
- Check is not protection: test captures of my queen and checking piece. Refresh pins after king moves. For a seventh-rank pawn, enumerate forward AND capture-promotions and the lines each clears.
- Verify movement geometry before calculating a line. Queenless positions still contain mates: scan checks and every king escape, including squares occupied by my pawns. Wins and sparse annotations do not validate moves.

## Clock and conversion
- Submit before expiry. Play familiar development, forced recaptures, and verified conversion quickly; reserve calculation for tactical turning points with a firm stopping point.
- Below 90 seconds with a 10-second increment, aim for 1-5 seconds on routine moves and generally stay below the increment.
- Q vs bare king: restrict the king, approach with my king, deliver protected mate. Before nonchecking moves verify an enemy legal move remains and my queen is safe. I have flagged in this ending.
- Recent losses had ample time. Spend calculation on concrete safety checks; long thinks without them failed. Simplify promptly once verified.

## Dragon: White vs DeepSeek
- T13 repeated the Yugoslav setup through 12...Nc4 13.Bxc4! Rxc4!; Nc4 attacked Qd2/Bb3. Then 14.h5 Nxh5 15.g4 Nf6 16.g5?! Ne8?! 17.Qh2 Rxd4?? 18.Qxh7#.
- After ...Nxh5, White's h-pawn was gone and Rh1 had a clear h-file. Nf6 guarded h7; ...Ne8 removed that defense. Qh2 threatened Qxh7#, protected by Rh1. Calculate captures, blocks, and king escapes before taking material elsewhere.
- g5 was inaccurate despite winning; no best replacement supplied. Qh2 took 25 seconds, mate 3 seconds; finished with 15:28 and no invalid attempts. Use the verified mate promptly.
- T12: h5 gxh5 Bh6?? abandoned Be3's defense of Nd4. ...Rxd4 Qxd4 Bxh6+ wins both minors for a rook. Black instead played ...Bxh6 Qxh6 Nxe4??, removing Nf6's h5/h7 defense; Rxh5 supported Qxh7#.

## Four Knights: Black vs Stockfish
- 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6 12.Qb3: Qe7 defends Bb4 via d6/c5 and e6 vertically; Qd5?? loses Bb4.
- T13 ...Rd4?! Re3 Bf4? Bc3! screened Qf6 with Rd4. ...Bxe3 fxe3 attacked that rook. ...Rd3?? allowed cxd3 and uncovered the queen attack. Imagined ...Rxc3 from d4 was illegal: rooks cannot capture diagonally. No best replacement supplied.
- ...Qxd3 behind Bc3 allowed Bxg7+ Kg8 Qxd3: the bishop cleared Qb3's attack with check. Rf7 protected Bg7. Calculate checking departures before placing a queen behind an enemy blocker.
- Rf4 screened Rf1 and could recapture on f8; ...Re4 abandoned both duties and allowed Rxf8#. ...Qe3+ Kh1 Qxc3 also ignored that mate. Kf6/Re7 allowed h4, protected Bg5+, and Bxe7: defense does not prevent a skewer.

## Central exchanges and blocked lines
- Preserve Bc2 before a3 against ...Nb4/...Nxc2. With ...Rac8/Qc7 and clear c3-c6, test ...Qxc2 Qxc2 Rxc2 before Ng3. Rc1 attacks Qc7 only after ALL c-file screens disappear.
- Recount central defenders after reroutes and exchanges. ...Rd8 Rxd8+ Nxd8 displaced Nc6 and exposed e5; Nd8 supplied no e4 recapture. ...Nd4 Nxd4 exd4 cleared the e-file for Re8+ Rxe8 Rxe8#; the pawn attack gave no tempo against check.
- Italian T12: ...d5 required e5!; ...Ne4 Nxe4 dxe4 Bxe4 followed. Be3 reinforced d4; Qe2 removed Qd1's d-pawn defense. My e5 pawn blocked Rd5xf5 until e6 fxe6 cleared it. Ng6+ Kg8 Ne7+ Kh7 Nxd5 won a rook while retaining the knight.
- T13 Chigorin: Bd3?? offered a bishop but Bd2 blocked Qd1xd3; ...Nxd3 won it outright. Verify the recapture path before trusting any offered exchange.

## Pawn shelter and promotion
- Caro-Kann T12: h5/Qg3 met ...g6? hxg6 fxg6, vacating f7 and forfeiting ...fxe6. e6! attacked Qd7; e7 then required ...Rfe8. Calculate central breakthroughs before changing the king's pawn shield.
- ...Rad8?? allowed exd8=N, capturing a rook and clearing e7; ...Qc7 Rxe8+ Kg7 Rg8# followed. Attacking the promoted knight did not answer the opened-file mate.
- A promotion threat does not force the blockader to move: another piece may capture its attacker. Verify destinations against ALL enemy pieces and pawns.

## Opponents
- Sonnet pressures central pawns and exploits unequal exchanges, but can misread blocked recaptures. Expect stalemate attempts and resistance until mate; verify offered trades.
- DeepSeek misses forks, captures, material counts, and mates. Search forcing wins while checking my own safety independently; it changed from ...gxh5 to ...Nxh5 in the Dragon.
- Stockfish takes exposed material and finds rook mates, capture-promotions, and counterattacks against pinned screens. Calculate its best reply before chasing its queen.

## Note files
- notes/accelerated-dragon.md - Capture geometry, pawn inventory, rook safety.
- notes/berlin-endgame.md - Open-file mate, queenless king safety.
- notes/caro-kann-advance.md - Capture-promotions, destination attacks, released pins.
- notes/deepseek.md - Dragon mate, Chigorin screens, material counts.
- notes/four-knights.md - Bishop defense, rook functions, skewers.
- notes/qgd-exchange.md - Knight forks, intermediate captures, blockers.
- notes/ruy-lopez.md - Italian queen win, checking forks, central defense.
- notes/sicilian-maroczy.md - Pinned defenders, unsafe retreats, promotion blockades.
