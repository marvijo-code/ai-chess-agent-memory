# Chess memory

## Move discipline
- Before choosing a move, scan enemy checks, captures, and pawn attacks. Repeat on the resulting position, including loose pieces elsewhere. Check every destination against enemy pawns, including advanced flank pawns.
- When attacked, examine captures and counterthreats before retreating. Trace sliding-piece defenders through vacated squares; friendly blockers interrupt protection.
- Recount central pawn defenders after knight reroutes, exchanges, and rook lifts. An outpost or kingside attack is unsound if it abandons the center.
- Calculate the strongest defense to an attack. A mate threat earns no compensation if a simple pawn move stops it and permits invasion.
- Check is not protection: before a queen check, test king captures and every other capture of the queen. Keep promoted queens safe unless a sacrifice has a concrete purpose.
- Move marks are incomplete. Unmarked moves and favorable results do not validate the play.

## Clock and conversion
- The clock is part of the position. Submit a legal move before it expires; a forced win has no value after a flag.
- Use quick decisions for familiar development, forced recaptures, and routine conversion. Reserve calculation for concrete tactical turning points, with a firm stopping point.
- At less than 90 seconds with a 10-second increment, aim for 1 - 5 seconds on routine moves and generally stay below the increment. Do not repeatedly spend 20 - 40 seconds improving an already won position.
- Game 4: about ten minutes remained at move 26, under three at move 44, and 28 seconds after move 67. Flagged after 67...Ka1 with queen and king against bare king; it was scored a draw because a bare king cannot win on time, so a won game gave only half a point and an Armageddon decider. Elementary mating technique must be executable quickly.
- Queen conversion: restrict the enemy king, bring my king closer, and deliver a protected mate. Before a nonchecking move, verify the opponent retains a legal move. An exposed queen near the king can be captured; excessive confinement can stalemate.

## Ruy Lopez / Chigorin
- Standard setup and detailed examples are in notes/ruy-lopez.md. Play familiar development promptly.
- With Bc2 facing ...Nb4, preserve the bishop before a3 when ...Nxc2 is available. A pawn attack on a knight does not cancel its fork.
- Rc1 against Qc7: moving Bc2 can uncover a queen attack only if the rest of the c-file is clear. Check intervening knights and pawns.
- Nh4-f5, ...Bxf5, Ng3xf5 removes a defender of e4. Against ...Nc5 and ...Nf6, count defenders before further attacking maneuvers.
- Game 4: f3 supported e4, but f4 removed that support. Re3 temporarily defended e4; Rg3 abandoned it while ...Re8 and both knights attacked it. ...Nxe4 can also fork Rg3 and Bf2. This repeated Game 3's central-defense failure.

## Tactical examples to retain
- Stockfish, Game 1: Qb3 against Bb4 means c3 and a bishop retreat can expose b7. Check this before moving Ra8 away. A stopped ...Rg5 mate threat allowed Rd8 penetration; examine open-file entry before spending tempi on ...h5-h4.
- Stockfish, Game 1: king d5, rook b5, enemy pawn c3 permits c4+, checking the king and attacking the rook. Scan pawn pushes with check before king centralization.
- DeepSeek, Game 2: ...Nb4 against Bc2 and rooks a1/e1 threatened ...Nxc2. Qc7 defended c2 along the cleared file, so Qxc2 Qxc2 lost White's queen.
- Sonnet, Game 3: Nb3 overlooked ...axb3 from a4. Check advanced pawn attacks on retreat squares.
- Sonnet, Game 3: with Qd5 and Re4, ...Qe6 allowed Rxe6! fxe6 Qxe6+, winning queen and pawn for rook. Compare rook and queen captures when offered a queen trade.
- Sonnet, Game 3: ...Bd4+ allowed Qxd4 because d6 blocked Rd8's protection. After b8=Q, Qxg5+ allowed ...Kxg5; having another queen did not excuse the error.
- Sonnet, Game 4: after e5 dxe5, Nxg7+ uncovered Bb1's check; Nxe8+ then uncovered Rg3's check. After ...Bg7, Nxc7 exf4 exchanged queens and left me an extra rook. Count both sides' captures before calling a combination decisive.
- Extra material can be converted through favorable exchanges and a passed pawn. In Game 4, Rxf6+ removed the bishop, the remaining knights were exchanged, and the h-pawn promoted. Once clearly winning, spend time stopping counterplay and completing the win.

## Opponent observations
- Sonnet 5.5, two games: develops a coherent Chigorin, pressures loose central pawns, and exploits pawn attacks on pieces. Later tactical errors enabled recoveries in both games; do not plan around receiving another blunder.
- In Game 4 Sonnet continued with its king and queenside pawns after my promotion, then preserved its last pawn and sought stalemate or time trouble. Expect resistance until mate; keep conversion fast and systematic.

## Note files
- notes/ruy-lopez.md - opening sequences and postgame turning points.
