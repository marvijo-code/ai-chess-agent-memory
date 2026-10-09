# Chess memory

## Move discipline
- Scan enemy checks, captures, pawn attacks, forks, promotions, and opened lines before choosing a move; repeat on the resulting board. Include loose pieces and immediate mates.
- When attacked, examine captures and counterthreats before retreating. Attacking a queen does not force retreat: it may capture, promote, or permit mate elsewhere. Exchange offers are optional.
- Trace defenders and recaptures by exact rank, file, or diagonal, including blockers. Before moving a defender or screen, identify every protection it supplies and every attack it releases.
- Before exchanges, calculate the forced recapture and next forcing move; recount material at the end. Test captures of my attacking piece and the strongest defense, including pawn blocks and bishop exchanges.
- Check is not protection: test captures of my queen and checking piece. Refresh pins after king moves. For a seventh-rank pawn, enumerate forward AND capture-promotions and the lines each clears.
- Queenless positions still contain mates. Before king advances, scan checks and every escape square, including squares occupied by my pawns. Sparse marks and favorable results do not validate play.

## Clock and conversion
- Submit before expiry. Play familiar development, forced recaptures, and verified conversion quickly; reserve calculation for tactical turning points with a firm stopping point.
- Below 90 seconds with a 10-second increment, aim for 1-5 seconds on routine moves and generally stay below the increment.
- Q vs bare king: restrict the king, approach with my king, deliver protected mate. Before nonchecking moves verify an enemy legal move remains and my queen is safe. I have flagged in this ending.
- Recent losses had ample time. Spend calculation on concrete safety checks; long thinks without them failed. Simplify promptly once verified.

## Four Knights: Black vs Stockfish
- 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6 12.Qb3: Qe7 defends Bb4 via d6/c5 and e6 vertically; Qd5?? loses Bb4.
- T13: after ...Rfd8/Re4, ...Rd4?! Re3 Bf4? Bc3! put Rd4 between Bc3 and Qf6. ...Bxe3 fxe3 removed my bishop and made e3 attack Rd4. Before grabbing a rook, calculate the pawn recapture and attacks on my remaining pieces.
- T13 ...Rd3?? vacated that queen screen and landed on c2's capture square: cxd3 lost the rook. Bxf6 Rxb3 was only one possible reply, not forced. Calculate ...Rxc3 Qxc3 Qxc3 bxc3 instead: this liquidation leaves equal rooks and six pawns each. No engine-best replacement for ...Bf4 was supplied.
- ...Qh4 f4 Bxf4? Bxf4 Rxf4 defused the attack. ...Ref8 abandoned e6. With Kh8/g7/h7, Rf4 blocked Rf1 and could recapture on f8; ...Re4 removed BOTH functions and allowed Rxf8#.
- ...Qe3+ Kh1 Qxc3 ignored Rf8#. Kf6/Re7 allowed h4, protected Bg5+, and Bxe7: a defended rook still loses the exchange to a king-rook skewer.

## Caro-Kann: pawn shelter and promotion
- T12: h5/Qg3 met ...g6? hxg6 fxg6, vacating f7 and forfeiting ...fxe6. e6! attacked Qd7; e7 then required ...Rfe8. Calculate central breakthroughs before changing the king's pawn shield.
- Qd5/Re6/Bg5/e7 against Kg8/Qg7/Re8/Ra8: ...Rad8?? allowed exd8=N, capturing the rook and clearing e7. ...Qc7 Rxe8+ Kg7 Rg8# followed. Attacking the promoted knight did not answer the opened-file mate.
- Earlier Qd6?? allowed c5xd6; Qe7?? allowed Nf5xe7+. A defended queen can still lose to a pawn or knight. ...f4+ abandoned Ne4 to Kxe4.

## Ruy Lopez / Italian / central exchanges
- Preserve Bc2 before a3 against ...Nb4/...Nxc2. With ...Rac8/Qc7 and clear c3-c6, test ...Qxc2 Qxc2 Rxc2 before Nf1-g3. Rc1 attacks Qc7 only after ALL c-file screens disappear.
- Recount central defenders after reroutes and exchanges. Nh4-f5/Bxf5/Ng3xf5, f3-f4, and Re3-g3 can abandon e4. ...Rd8 Rxd8+ Nxd8 displaced Nc6 and exposed e5; Nd8 supplied no e4 recapture.
- ...Nd4 Nxd4 exd4 cleared the e-file for Re8+ Rxe8 Rxe8#. A pawn attack on a rook gives no tempo against check.
- T12 Italian: ...d5 required e5!; ...Ne4 Nxe4 dxe4 Bxe4 followed. Be3 reinforced d4; Qe2 removed Qd1's d-pawn defense before rook doubling.
- Rd5 could not recapture Qxf5 through my e5 pawn. After e6 fxe6 Qxe6+, that screen vanished and Rd5 defended Nf5. Recheck paths after pawn moves.
- Ng6+ Kg8 Ne7+ Kh7 Nxd5 won Rd5 while retaining the knight. Before collecting a forked piece, check for another safe checking fork.

## Dragon and other recurring tactics
- T12: ...Nc4 Bxc4 Rxc4 h5 gxh5 Bh6?? abandoned Be3's defense of Nd4. ...Rxd4 Qxd4 Bxh6+ wins both minors for a rook.
- ...Bxh6 Qxh6 Nxe4?? removed Nf6's h5/h7 defense. Rxh5 supported Qxh7#; ...Rxd4 ignored mate. Verify queen support and escapes before choosing mate over recapture.
- A threatened promotion does not force the blockader to move: another piece may capture its attacker. Verify destinations against ALL enemy pieces and pawns.

## Opponents
- Sonnet pressures central pawns and exploits unequal exchanges, but can misread blocked recaptures. Expect stalemate attempts and resistance until mate; verify offered trades.
- DeepSeek misses forks, captures, material counts, and mates. Search forcing wins while checking my own safety independently.
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
