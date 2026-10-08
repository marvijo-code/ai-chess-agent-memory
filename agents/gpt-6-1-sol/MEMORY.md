# Chess memory

## Move discipline
- Scan enemy checks, captures, and pawn attacks before choosing a move, then repeat on the resulting board. Include loose pieces, newly opened lines, and immediate mates. Check destinations against advanced flank pawns.
- When attacked, examine captures and counterthreats before retreating. Attacking the queen does not force retreat: it may capture a loose piece or allow another piece to deliver mate. Queen-exchange offers are optional.
- Verify defenders by exact rank, file, or diagonal, including blockers. Before moving a defender or blocker, identify every line and recapture it supplies. Activity is not protection.
- Recount central pawn defenders after knight reroutes, exchanges, and rook lifts. An outpost or attack is unsound if it abandons the center.
- Before exchanges, calculate the forced recapture and next forcing move. Play contested captures through to the end and update the material inventory. One bishop does not make a knight safe against two attackers.
- Calculate the strongest defense to an attack. A simple pawn block or bishop exchange may end a mate threat and permit invasion; queen harassment does not establish compensation.
- Check is not protection: test king captures and every other capture of my queen. Recheck pins after king moves. Protect promoted queens.
- Queenless positions still contain mating threats. Before king advances, scan knight checks and all escape squares, including those occupied by my pawns.
- Move marks are incomplete. Unmarked moves and favorable results do not validate the play.

## Clock and conversion
- Submit a legal move before the clock expires. Decide familiar development, forced recaptures, and routine conversion quickly; reserve calculation for tactical turning points with a firm stopping point.
- Below 90 seconds with a 10-second increment, aim for 1-5 seconds on routine moves and generally stay below the increment. Avoid repeated 20-40-second searches in won positions.
- Sonnet Game 4: about ten minutes at move 26, under three at move 44, and 28 seconds after move 67. Flagged with queen against bare king. Execute elementary mates quickly.
- Queen conversion: restrict the enemy king, approach with my king, and deliver protected mate. Before nonchecking moves, verify an enemy legal move remains; avoid stalemate and queen captures.
- Recent checkmate losses had ample time. Improve candidate-move safety checks; longer searches alone did not prevent tactical misses.

## Four Knights: Black vs Stockfish
- Shared sequence: 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6! 12.Qb3.
- Round 3: 12...Qd5?? attacked Qb3 but did not defend Bb4; 13.Qxb4 won the bishop. Semifinal: 12...Qe7 actually defended Bb4 along e7-d6-c5-b4 and e6 on the e-file. This repaired that specific error, not the whole opening.
- Semifinal: 13.d4 Rae8 14.c3 Bd6! 15.Qxb7 Qh4 16.f4 Bxf4? 17.Bxf4! Rxf4 18.Qxc6 Ref8 19.Qxe6+ Kh8. White's pawn block and bishop exchange defused the attack. Qxc6 attacked Re8; moving it to f8 abandoned e6, which fell with check.
- After 20.Qe2, Rf4 blocked White's Rf1 and could recapture on f8. 20...Re4 attacked the queen but removed BOTH functions: 21.Rxf8#. With Kh8 and pawns g7/h7, no escape remained. Reconstruct the board after rook lifts before claiming a tempo.
- Round 3: after 27.Rxf8+ Qxf8 28.Bxh6 gxh6, White had Q+R against Q; extra pawns did not restore equality. After 37.Rf1 Qe3+ 38.Kh1, 38...Qxc3 ignored Rf8#. Queen checks do not erase the threat after the king answers.

## Ruy Lopez / central exchanges
- With Bc2 facing ...Nb4, preserve the bishop before a3 when ...Nxc2 forks the rooks. Attacking a knight does not cancel its fork.
- Rc1 against Qc7: moving Bc2 uncovers a queen attack only if the remaining c-file is clear. Check intervening knights and pawns.
- Nh4-f5, ...Bxf5, Ng3xf5 removes an e4 defender. Against ...Nc5 and ...Nf6, recount before further attacking maneuvers.
- Sonnet Game 4: f3 supported e4; f4 removed that support. Re3 defended e4; Rg3 abandoned it against ...Re8 and both knights. ...Nxe4 could also fork Rg3/Bf2.
- Armageddon: ...Rd8 Rxd8+ Nxd8 displaced Nc6 and exposed e5. Then ...Nxe4?? Nxe4 Bxe4 Bxe4 lost a piece: Ng3/Bc2 both attacked e4, while Nd8 supplied no recapture. Accept a pawn loss rather than force an unsound recovery.
- Round 2: ...Nd4?? Nxd4 exd4 cleared the e-file for Re8+ Rxe8 Rxe8#. A pawn attack on a rook supplies no tempo against a forcing check.

## Tactical examples
- Stockfish: Qb3 against Bb4 also pressures b7; check before moving Ra8 away. Kd5/Rb5 against c3 permits c4+, checking the king and attacking the rook.
- Sonnet Game 3: Nb3 overlooked ...axb3 from a4. With Qd5/Re4, ...Qe6 allowed Rxe6! fxe6 Qxe6+, winning queen and pawn for rook.
- Sonnet Game 3: ...Bd4+ allowed Qxd4 because d6 blocked Rd8's protection. After b8=Q, Qxg5+ allowed ...Kxg5.
- Sonnet Game 4: e5 dxe5 Nxg7+ uncovered Bb1's check; Nxe8+ uncovered Rg3's check. Nxc7 exf4 exchanged queens and left an extra rook. Count both sides' captures.
- DeepSeek: after Kf1 released the g2 pin, ...Qf3+? allowed gxf3. Rh3's protection did not justify losing queen for pawn.
- Sonnet Armageddon: e4+ Kc4 Ne5#. My b5/c5 pawns blocked escapes; White's pawns and knight covered the rest.

## Opponents
- Sonnet pressures loose central pawns and exploits unequal exchanges. It seeks stalemate and time trouble; expect resistance until mate.
- DeepSeek has missed forks, pawn captures, and material counts. Its mistakes do not validate my moves.
- Stockfish takes exposed material, neutralizes superficial mate threats, and finds rook mates immediately. Verify defensive rook functions before chasing its queen.

## Note files
- notes/ruy-lopez.md - Chigorin sequences, central defense, and conversion failures.
- notes/berlin-endgame.md - Open-file mate, displaced defenders, and queenless king safety.
- notes/deepseek.md - Forks, material counts, released pins, and conversion.
- notes/four-knights.md - Bishop defense, failed kingside attack, and rook-move mating geometry.
