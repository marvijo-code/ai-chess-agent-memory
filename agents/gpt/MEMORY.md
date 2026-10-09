# Chess memory

## Move discipline
- Scan enemy checks, captures, pawn attacks, forks, promotions, and opened lines before choosing a move; repeat on the resulting board. Include loose pieces and immediate mates.
- When attacked, examine captures and counterthreats before retreating. Attacking a queen does not force retreat: it may capture, promote, or permit mate elsewhere. Exchange offers are optional.
- Trace defenders by exact rank, file, or diagonal, including blockers. Before moving a defender or blocker, identify every protection and recapture it supplies. Activity is not protection.
- Before exchanges, calculate the forced recapture and next forcing move; recount material at the end. Test captures of my attacking piece and the strongest defense, including pawn blocks and bishop exchanges.
- Check is not protection: test captures of my queen and checking piece. Refresh pins after king moves. Protect promoted pieces. For a seventh-rank pawn, enumerate forward AND capture-promotions and the lines each clears.
- Queenless positions still contain mates. Before king advances, scan checks and every escape square, including squares occupied by my pawns. Sparse move marks and favorable results do not validate play.

## Clock and conversion
- Submit before expiry. Play familiar development, forced recaptures, and verified conversion quickly; reserve calculation for tactical turning points with a firm stopping point.
- Below 90 seconds with a 10-second increment, aim for 1-5 seconds on routine moves and generally stay below the increment.
- Sonnet Game 4: flagged with queen against bare king. Restrict the king, approach with my king, deliver protected mate; before nonchecking moves verify an enemy legal move remains and my queen is safe.
- Recent losses had ample time. Use time for concrete safety checks. T12's won conversion still spent 55 seconds on Nxf6+; simplify promptly once verified.

## Caro-Kann: promotion and destination safety
- T12 final: h5/Qg3 met ...g6? hxg6 fxg6, vacating f7 and forfeiting ...fxe6. e6! attacked Qd7; e7 then required ...Rfe8. Calculate central breakthroughs before changing the king's pawn shield.
- With White Qd5/Re6/Bg5/e7 against Kg8/Qg7/Re8/Ra8, ...Rad8?? allowed exd8=N, capturing the rook and clearing e7: ...Qc7 Rxe8+ Kg7 Rg8#. Attacking the promoted knight did not answer the opened-file mate.
- Earlier Qd6?? allowed c5xd6; Qe7?? allowed Nf5xe7+. A defended queen destination can still lose queen for pawn or knight. ...f4+ abandoned Ne4 to Kxe4.

## Four Knights: Black vs Stockfish
- 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6 12.Qb3: Qe7 defends Bb4 via d6/c5 and e6 vertically; Qd5?? loses Bb4.
- ...Qh4 f4 Bxf4? Bxf4 Rxf4 defused the attack. ...Ref8 abandoned e6. With Kh8/g7/h7, Rf4 blocked Rf1 and could recapture on f8; ...Re4 removed BOTH functions and allowed Rxf8#.
- ...Qe3+ Kh1 Qxc3 ignored Rf8#. Kf6/Re7 allowed h4, protected Bg5+, and Bxe7; pursuing the h-file ignored the king-rook skewer.

## Ruy Lopez / Italian / central exchanges
- Preserve Bc2 before a3 against ...Nb4/...Nxc2. With ...Rac8/Qc7 and clear c3-c6, test ...Qxc2 Qxc2 Rxc2 before Nf1-g3. Rc1 attacks Qc7 only after ALL c-file screens disappear.
- Recount central defenders after reroutes and exchanges. Nh4-f5/Bxf5/Ng3xf5, f3-f4, and Re3-g3 can abandon e4. ...Rd8 Rxd8+ Nxd8 displaced Nc6 and exposed e5; Nd8 supplied no e4 recapture.
- ...Nd4 Nxd4 exd4 cleared the e-file for Re8+ Rxe8 Rxe8#. A pawn attack on a rook gives no tempo against check.
- T12 Italian: ...d5 required e5!; ...Ne4 Nxe4 dxe4 Bxe4 Bf5 Bxf5 Qxf5 followed. Be3 reinforced d4; Qe2 removed Qd1's d-pawn defense before rook doubling.
- Rd5 could not recapture Qxf5 through my e5 pawn. After e6 fxe6 Qxe6+, that screen vanished and Rd5 defended Nf5. Recheck paths after pawn moves.
- Ne5 Rf8 Ng6+ Kg8 Ne7+ Kh7 Nxd5 won Rd5 while retaining the knight. Before collecting a forked piece, check for another safe checking fork.

## Dragon and destination reminders
- T12 DeepSeek: ...Nc4 Bxc4 Rxc4 h5 gxh5 Bh6?? abandoned Be3's defense of Nd4. ...Rxd4 Qxd4 Bxh6+ wins both minors for a rook.
- ...Bxh6 Qxh6 Nxe4?? removed Nf6's h5/h7 defense. Rxh5 supported Qxh7#; ...Rxd4 ignored mate. Verify queen support and escapes before choosing mate over recapture.
- Qb3 against Bb4 also pressures b7; check before moving Ra8. Kd5/Rb5 against c3 permits c4+, checking king and attacking rook.
- Sonnet: Nb3 allowed ...axb3 from a4; ...Qe6 against Qd5/Re4 allowed Rxe6 fxe6 Qxe6+. ...Bd4+ allowed Qxd4 because d6 blocked Rd8. Qxg5+ allowed Kxg5.
- DeepSeek: Kf1 released the g2 pin; ...Qf3+ allowed gxf3 despite Rh3 support.

## Opponents
- Sonnet pressures central pawns and exploits unequal exchanges, but can misread blocked recaptures. Expect stalemate attempts and resistance until mate; verify offered trades.
- DeepSeek misses forks, captures, material counts, and mates. Search forcing wins while checking my own safety independently.
- Stockfish takes exposed material and finds rook mates and capture-promotions. Preserve defensive functions before chasing its queen.

## Note files
- notes/accelerated-dragon.md - Capture geometry, pawn inventory, rook safety.
- notes/berlin-endgame.md - Open-file mate, queenless king safety.
- notes/caro-kann-advance.md - Capture-promotions, destination attacks, released pins.
- notes/deepseek.md - Dragon mate, Chigorin screens, material counts.
- notes/four-knights.md - Bishop defense, rook functions, skewers.
- notes/qgd-exchange.md - Knight forks, intermediate captures, blockers.
- notes/ruy-lopez.md - Italian queen win, checking forks, central defense.
- notes/sicilian-maroczy.md - Pinned defenders, unsafe retreats, promotion blockades.
