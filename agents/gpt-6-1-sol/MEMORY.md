# Chess memory

## Move discipline
- Before choosing a move, scan enemy checks, captures, and pawn attacks. Repeat on the resulting position, including loose pieces elsewhere. Check destinations against advanced flank pawns.
- When attacked, examine captures and counterthreats before retreating. Trace sliding-piece defenders through vacated squares; friendly blockers interrupt protection.
- Recount central pawn defenders after knight reroutes, exchanges, and rook lifts. An outpost or attack is unsound if it abandons the center.
- Before offering exchanges, calculate the forced recapture and the opponent's next forcing move. Simplification can displace a defender and lose material.
- For contested captures, play the entire exchange sequence and tally material at the end. One supporting bishop does not make a knight safe against two attackers.
- Calculate the strongest defense to an attack. A mate threat earns no compensation if a simple pawn move stops it and permits invasion.
- Check is not protection: before a queen check, test king captures and every other capture of the queen. Protect promoted queens.
- Queenless positions still contain mating threats. Before king advances, scan knight checks and every escape square, including squares blocked by my own pawns.
- Move marks are incomplete. Unmarked moves and favorable results do not validate the play.

## Clock and conversion
- Submit a legal move before the clock expires; a forced win has no value after a flag.
- Decide familiar development, forced recaptures, and routine conversion quickly. Reserve calculation for tactical turning points, with a firm stopping point.
- Below 90 seconds with a 10-second increment, aim for 1 - 5 seconds on routine moves and generally stay below the increment. Avoid repeated 20 - 40-second searches in won positions.
- Game 4: about ten minutes at move 26, under three at move 44, and 28 seconds after move 67. Flagged after 67...Ka1 with queen against bare king; scored a draw because the bare king could not win on time. This forced Armageddon. Execute elementary mates quickly.
- Queen conversion: restrict the enemy king, approach with my king, and deliver a protected mate. Before nonchecking moves, verify an enemy legal move remains; avoid stalemate and queen captures.

## Ruy Lopez / central exchanges
- Opening sequences and examples: notes/ruy-lopez.md and notes/berlin-endgame.md. Play familiar development promptly.
- With Bc2 facing ...Nb4, preserve the bishop before a3 when ...Nxc2 is available. Attacking a knight does not cancel its fork.
- Rc1 against Qc7: moving Bc2 uncovers a queen attack only if the remaining c-file is clear. Check intervening knights and pawns.
- Nh4-f5, ...Bxf5, Ng3xf5 removes an e4 defender. Against ...Nc5 and ...Nf6, recount before further attacking maneuvers.
- Game 4: f3 supported e4; f4 removed that support. Re3 defended e4; Rg3 abandoned it against ...Re8 and both knights. ...Nxe4 could also fork Rg3/Bf2. This repeated Game 3's central-defense failure.
- Armageddon as Black: 17...Rd8?! 18.Rxd8+ Nxd8! displaced Nc6 and exposed e5 to 19.Nxe5. Assess that consequence before offering the rook exchange; the forced recapture was not the original error.
- Then 19...Nxe4?? 20.Nxe4 Bxe4 21.Bxe4 lost a piece. White's Ng3 and Bc2 both attacked e4; Black's Bb7 supported Nf6, but Nd8 supplied no recapture. Accept a pawn loss rather than force an unsound recovery.
- Draw odds favor stable equality, but exchanges must leave a tactically sound position.

## Tactical examples to retain
- Stockfish, Game 1: Qb3 against Bb4 means c3 and a bishop retreat can expose b7. Check before moving Ra8 away. A stopped ...Rg5 mate threat allowed Rd8 penetration; examine open-file entry before ...h5-h4.
- Stockfish, Game 1: king d5, rook b5, enemy pawn c3 permits c4+, checking the king and attacking the rook. Scan pawn checks before king centralization.
- DeepSeek, Game 2: ...Nb4 against Bc2 and rooks a1/e1 threatened ...Nxc2. Qc7 defended c2 along the cleared file, so Qxc2 Qxc2 lost White's queen.
- Sonnet, Game 3: Nb3 overlooked ...axb3 from a4. With Qd5/Re4, ...Qe6 allowed Rxe6! fxe6 Qxe6+, winning queen and pawn for rook.
- Sonnet, Game 3: ...Bd4+ allowed Qxd4 because d6 blocked Rd8's protection. After b8=Q, Qxg5+ allowed ...Kxg5; another queen did not excuse the error.
- Sonnet, Game 4: after e5 dxe5, Nxg7+ uncovered Bb1's check; Nxe8+ uncovered Rg3's check. After ...Bg7, Nxc7 exf4 exchanged queens and left an extra rook. Count both sides' captures before evaluating combinations.
- Extra material can convert through favorable exchanges and a passed pawn. In Game 4, Rxf6+ removed the bishop, knights were exchanged, and the h-pawn promoted. Complete the win promptly.
- Sonnet, Armageddon: 31.e4+ Kc4 32.Ne5#. My b5/c5 pawns blocked escapes; White's pawns covered b3/b4/d4/d5, b2 defended c3, and Ne5 covered d3. A king seeking counterplay still needs a safe escape map.

## Opponent observations
- Sonnet 5.5, three games: coherent Ruy Lopez development, pressure on loose central pawns, and exploitation of pawn attacks and unequal exchange counts. Earlier tactical errors enabled recoveries; do not depend on another blunder.
- In Game 4 Sonnet preserved its last pawn and sought stalemate or time trouble after my promotion. Expect resistance until mate.
- In Armageddon Sonnet immediately exploited the undefended e5 pawn, calculated the full e4 exchange, traded into knight-versus-pawns, and found a knight mate. Doubled pawns did not compensate for my tactical errors.

## Note files
- notes/ruy-lopez.md - Chigorin sequences, central defense, and conversion failures.
- notes/berlin-endgame.md - Armageddon rook exchanges, lost defenders, and knight mate.
