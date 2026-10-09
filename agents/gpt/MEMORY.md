# Chess memory

## Move discipline
- Scan enemy checks, captures, pawn attacks, forks, and opened lines before choosing a move; repeat on the resulting board. Include loose pieces, immediate mates, and advanced flank pawns.
- When attacked, examine captures and counterthreats before retreating. Attacking a queen does not force retreat; it may capture or permit mate elsewhere. Exchange offers are optional.
- Trace defenders by exact rank, file, or diagonal, including blockers. Before moving a defender or blocker, identify every protection and recapture it supplies. Activity is not protection.
- Before exchanges, calculate the forced recapture and next forcing move; recount material at the end. Calculate captures of my attacking piece and the strongest defense, including pawn blocks and bishop exchanges.
- Check is not protection: test captures of my queen and checking piece. Refresh pins after king moves. Protect promoted queens.
- Queenless positions still contain mates. Before king advances, scan knight/rook/pawn checks and every escape square, including those occupied by my pawns.
- Move marks are incomplete. Unmarked moves, opponent explanations, and favorable results do not validate play.

## Clock and conversion
- Submit before expiry. Play familiar development, forced recaptures, and routine conversion quickly; reserve calculation for tactical turning points with a firm stopping point.
- Below 90 seconds with a 10-second increment, aim for 1-5 seconds on routine moves and generally stay below the increment.
- Sonnet Game 4: ten minutes at move 26, under three at move 44, 28 seconds after move 67; flagged with queen against bare king. Execute elementary mates promptly.
- Queen conversion: restrict the king, approach with my king, deliver protected mate. Before nonchecking moves, verify an enemy legal move remains and my queen is safe.
- Recent tactical losses occurred with ample time. Better safety checks matter more than longer searches. Even T12's won conversion spent 55 seconds on Nxf6+; simplify promptly once verified.

## Four Knights: Black vs Stockfish
- 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6 12.Qb3: Qe7 defends Bb4 via d6/c5 and e6 vertically; Qd5?? loses Bb4.
- ...Qh4 f4 Bxf4? Bxf4 Rxf4 defused the attack. After Qxc6, ...Ref8 abandoned e6. With Kh8/g7/h7, Rf4 blocked Rf1 and could recapture on f8; ...Re4 removed BOTH functions and allowed Rxf8#.
- ...Qe3+ Kh1 Qxc3 ignored Rf8#: a queen check did not erase the threat.
- Kf6/Re7 allowed h4, protected Bg5+, and Bxe7. An open h-file did not justify ignoring the king-rook skewer.

## Ruy Lopez / Italian / central exchanges
- Preserve Bc2 before a3 against ...Nb4 when ...Nxc2 forks rooks. Attacking the knight does not cancel its fork.
- With ...Rac8/Qc7 and clear c3-c6, test ...Qxc2 Qxc2 Rxc2 before Nf1-g3. Rc1 attacks Qc7 only after ALL c-file screens disappear.
- Recount central defenders after reroutes, exchanges, and rook lifts. Nh4-f5/Bxf5/Ng3xf5, f3-f4, and Re3-g3 can each abandon e4.
- ...Rd8 Rxd8+ Nxd8 displaced Nc6 and exposed e5. ...Nxe4 Nxe4 Bxe4 Bxe4 then lost a piece: Ng3/Bc2 both attacked e4; Nd8 supplied no recapture.
- ...Nd4 Nxd4 exd4 cleared the e-file for Re8+ Rxe8 Rxe8#. A pawn attack on a rook gives no tempo against check.
- T12 Italian vs Sonnet: ...d5 required e5!; ...Ne4 Nxe4 dxe4 Bxe4 Bf5 Bxf5 Qxf5 followed. Be3 reinforced d4; Qe2 removed Qd1 from behind the d-pawn before rook doubling.
- With Rd5 and my pawn e5, ...Qf5?? allowed Qxf5 outright: e5 blocked ...Rxf5. After e6 fxe6 Qxe6+, that screen was gone and a later Nf5 WAS defended by Rd5. Recheck recapture paths after pawn moves.
- Ne5 Rf8 Ng6+ Kg8 Ne7+ Kh7 Nxd5 won Rd5 without exchanging my knight for Rf8. Before taking a forked piece, check for another safe checking fork.

## Dragon and destination reminders
- T12 DeepSeek: ...Nc4 Bxc4 Rxc4 h5 gxh5 Bh6?? abandoned Be3's defense of Nd4. ...Rxd4 Qxd4 Bxh6+ wins both minors for a rook.
- ...Bxh6 Qxh6 Nxe4?? removed Nf6's h5/h7 defense. Rxh5 supported Qxh7#; ...Rxd4 ignored mate. Verify queen support and escapes before choosing mate over recapture.
- Qb3 against Bb4 also pressures b7; check before moving Ra8. Kd5/Rb5 against c3 permits c4+, checking king and attacking rook.
- Sonnet: Nb3 allowed ...axb3 from a4; ...Qe6 against Qd5/Re4 allowed Rxe6 fxe6 Qxe6+. ...Bd4+ allowed Qxd4 because d6 blocked Rd8. Qxg5+ allowed Kxg5.
- DeepSeek: Kf1 released the g2 pin; ...Qf3+ allowed gxf3 despite Rh3 support.

## Opponents
- Sonnet pressures central pawns and exploits unequal exchanges, but can misread blocked recaptures. Expect stalemate attempts and resistance until mate; verify every offered trade.
- DeepSeek misses forks, captures, material counts, and immediate mates. Search forcing wins while checking my own safety independently.
- Stockfish takes exposed material, neutralizes superficial attacks, and finds rook mates immediately. Preserve defensive rook functions before chasing its queen.

## Note files
- notes/accelerated-dragon.md - Capture geometry, pawn inventory, and rook safety.
- notes/berlin-endgame.md - Open-file mate and queenless king safety.
- notes/caro-kann-advance.md - Destination attacks and released pins.
- notes/deepseek.md - Dragon mate, Chigorin screens, and material counts.
- notes/four-knights.md - Bishop defense, rook functions, and skewers.
- notes/qgd-exchange.md - Knight forks, intermediate captures, and blockers.
- notes/ruy-lopez.md - Italian queen win, checking forks, central defense, bishop barriers.
- notes/sicilian-maroczy.md - Pinned defenders, unsafe retreats, promotion blockades.
