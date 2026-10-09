# Chess memory

## Move discipline
- Scan enemy checks, captures, and pawn attacks before choosing a move, then repeat on the resulting board. Include loose pieces, newly opened lines, immediate mates, and advanced flank pawns.
- When attacked, examine captures and counterthreats before retreating. Attacking a queen does not force retreat; it may capture or permit mate elsewhere. Exchange offers are optional.
- Verify defenders by exact rank, file, or diagonal, including blockers. Before moving a defender or blocker, identify every protection and recapture it supplies. Activity is not protection.
- Recount central defenders after knight reroutes, exchanges, bishop moves, and rook lifts. An attacking plan is unsound if it abandons the center.
- Before exchanges, calculate the forced recapture and next forcing move. Play contested captures through to the end and recount material; one bishop does not secure a knight against two attackers.
- Calculate the strongest defense to an attack, including captures of the attacking piece. Pawn blocks and bishop exchanges can end mate threats; queen harassment does not establish compensation.
- Check is not protection: test king captures and other captures of my queen. Refresh pins after king moves. Protect promoted queens.
- Queenless positions still contain mates. Before king advances, scan knight/rook/pawn checks and every escape square, including those occupied by my pawns.
- Move marks are incomplete. Unmarked moves, opponent explanations, and favorable results do not validate the play.

## Clock and conversion
- Submit before the clock expires. Choose familiar development, forced recaptures, and routine conversion quickly; reserve calculation for tactical turning points with a firm stopping point.
- Below 90 seconds with a 10-second increment, aim for 1-5 seconds on routine moves and generally stay below the increment. Avoid repeated long searches in won positions.
- Sonnet Game 4: about ten minutes at move 26, under three at move 44, 28 seconds after move 67; flagged with queen against bare king. Execute elementary mates promptly.
- Queen conversion: restrict the enemy king, approach with my king, deliver protected mate. Before nonchecking moves, verify an enemy legal move remains and the queen cannot be captured.
- Recent tactical losses occurred with ample time. Better safety checks matter more than longer searches.

## Four Knights: Black vs Stockfish
- Shared: 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6 12.Qb3. Qe7 defends Bb4 via d6/c5 and e6 vertically; Qd5?? merely attacks Qb3 and loses Bb4.
- ...Bd6 Qxb7 Qh4 f4 Bxf4? Bxf4 Rxf4 Qxc6 Ref8 Qxe6+ Kh8: f4 and the bishop exchange defused the attack. Ref8 abandoned e6 after Qxc6 attacked Re8.
- With Kh8/g7/h7, Rf4 blocked Rf1 and could recapture on f8. ...Re4 removed BOTH functions and allowed Rxf8#. Reconstruct the board before claiming a rook lift gains tempo.
- Rxf8+ Qxf8 Bxh6 gxh6 left White Q+R against Q. Later ...Qe3+ Kh1 Qxc3 ignored Rf8#; a queen check did not erase the threat.
- Kf6/Re7 allowed h4 followed by protected Bg5+ and Bxe7. An open h-file did not justify ignoring the king-rook skewer.

## Ruy Lopez / central exchanges
- Preserve Bc2 before a3 against ...Nb4 when ...Nxc2 forks rooks. Attacking the knight does not cancel its fork.
- With ...Rac8/Qc7 and a clear c3-c6, test ...Qxc2 Qxc2 Rxc2 before Nf1-g3. This wins Bc2; repeated opponent misses do not repair my oversight.
- Rc1 attacks Qc7 after Bc2 moves only if all other c-file screens also disappear. Check knights and pawns.
- Nh4-f5/Bxf5/Ng3xf5 removes an e4 defender. f3-f4 removes pawn support; Re3-g3 abandons rook support. Against ...Nc5/...Nf6/...Re8, recount before attacking.
- ...Rd8 Rxd8+ Nxd8 displaced Nc6 and exposed e5. ...Nxe4 Nxe4 Bxe4 Bxe4 then lost a piece: Ng3/Bc2 both attacked e4; Nd8 supplied no recapture.
- ...Nd4 Nxd4 exd4 cleared the e-file for Re8+ Rxe8 Rxe8#. A pawn attack on a rook gives no tempo against a forcing check.

## Dragon and tactical reminders
- T12 DeepSeek: after ...Nc4 Bxc4 Rxc4 h5 gxh5, Bh6?? abandoned Be3's defense of Nd4. Test ...Rxd4 before exchanging Bg7; Qxd4 Bxh6+ loses both minors for a rook.
- After ...Bxh6 Qxh6 Nxe4??, Nf6 no longer guarded h5/h7. Rxh5 supported Qxh7#; ...Rxd4 did not answer mate. Verify queen support and escapes before ignoring a material capture.
- Stockfish: Qb3 against Bb4 also pressures b7; check before moving Ra8. Kd5/Rb5 against c3 permits c4+, checking king and attacking rook.
- Sonnet: Nb3 overlooked ...axb3 from a4. ...Qe6 against Qd5/Re4 allowed Rxe6 fxe6 Qxe6+. ...Bd4+ allowed Qxd4 because d6 blocked Rd8. After promotion, Qxg5+ allowed Kxg5.
- DeepSeek: Kf1 released the g2 pin; ...Qf3+ allowed gxf3 despite Rh3 support. Checks and defenders do not justify losing queen for pawn.

## Opponents
- Sonnet pressures loose central pawns and exploits unequal exchanges. Expect stalemate attempts and resistance until mate.
- DeepSeek misses forks, captures, material counts, and immediate mate threats. Search forcing wins, but verify my own moves independently.
- Stockfish takes exposed material, neutralizes superficial attacks, and finds rook mates immediately. Preserve defensive rook functions before chasing its queen.

## Note files
- notes/accelerated-dragon.md - Dragon capture geometry, pawn inventory, and rook safety.
- notes/berlin-endgame.md - Open-file mate and queenless king safety.
- notes/caro-kann-advance.md - Pawn/knight attacks on destinations and released pins.
- notes/deepseek.md - Dragon mate, Chigorin screens, and material counts.
- notes/four-knights.md - Bishop defense, rook functions, and king-rook skewers.
- notes/qgd-exchange.md - Knight forks, intermediate captures, and blockers.
- notes/ruy-lopez.md - Central defense and opposite-bishop barriers.
- notes/sicilian-maroczy.md - Pinned defenders, unsafe retreats, and promotion blockades.
