# Chess memory

## Move discipline
- Before choosing a move, scan enemy checks, captures, and pawn attacks. Repeat on the resulting position, including loose pieces elsewhere and immediate mates. Check destinations against advanced flank pawns.
- When attacked, examine captures and counterthreats before retreating. Attacking the enemy queen does not force its retreat: it may capture my loose piece. A queen-exchange offer is optional for the opponent.
- Verify every claimed defender by exact rank, file, or diagonal. Trace sliding-piece protection through vacated squares; friendly blockers interrupt it. Activity and proximity are not protection.
- Recount central pawn defenders after knight reroutes, exchanges, and rook lifts. An outpost or attack is unsound if it abandons the center.
- Before offering exchanges, calculate the forced recapture and the next forcing move. Simplification can displace a defender and lose material.
- For contested captures, play the entire exchange sequence and tally material at the end. One supporting bishop does not make a knight safe against two attackers. Update the inventory after every liquidation.
- Calculate the strongest defense to an attack. A mate threat earns no compensation if a simple pawn move stops it and permits invasion. Queen harassment alone does not establish compensation for a lost piece.
- Check is not protection: before a queen check, test king captures and every other capture of the queen. Recheck pins after king moves. Protect promoted queens.
- Queenless positions still contain mating threats. Before king advances, scan knight checks and every escape square, including squares blocked by my own pawns.
- Move marks are incomplete. Unmarked moves and favorable results do not validate the play.

## Clock and conversion
- Submit a legal move before the clock expires. Decide familiar development, forced recaptures, and routine conversion quickly; reserve calculation for tactical turning points with a firm stopping point.
- Below 90 seconds with a 10-second increment, aim for 1-5 seconds on routine moves and generally stay below the increment. Avoid repeated 20-40-second searches in won positions.
- Sonnet Game 4: about ten minutes at move 26, under three at move 44, and 28 seconds after move 67. Flagged with queen against bare king; the draw forced Armageddon. Execute elementary mates quickly.
- Queen conversion: restrict the enemy king, approach with my king, and deliver protected mate. Before nonchecking moves, verify an enemy legal move remains; avoid stalemate and queen captures.
- Recent losses had ample time: improve forcing-move checks rather than treating them as clock failures.

## Four Knights: Black vs Stockfish, tournament 2 round 3
- After 10...Be6 11.Bxe6 fxe6! 12.Qb3, Bb4 was attacked. 12...Qd5?? attacked Qb3 but did not defend Bb4; 13.Qxb4 won the bishop. Verify geometry before claiming a move protects two targets.
- The later rook lifts and queen attacks never recovered the bishop. After 27.Rxf8+ Qxf8 28.Bxh6 gxh6, White had queen and rook against queen; extra pawns did not restore material equality.
- After 37.Rf1 Qe3+ 38.Kh1, Rf8# was threatened. 38...Qxc3 ignored it. Qg4 covered g7/g8, and Black's h7 pawn blocked the remaining escape. Recheck the mating net after the opponent answers my check.

## Ruy Lopez / central exchanges
- With Bc2 facing ...Nb4, preserve the bishop before a3 when ...Nxc2 is available. Attacking a knight does not cancel its fork.
- Rc1 against Qc7: moving Bc2 uncovers a queen attack only if the remaining c-file is clear. Check intervening knights and pawns.
- Nh4-f5, ...Bxf5, Ng3xf5 removes an e4 defender. Against ...Nc5 and ...Nf6, recount before further attacking maneuvers.
- Sonnet Game 4: f3 supported e4; f4 removed that support. Re3 defended e4; Rg3 abandoned it against ...Re8 and both knights. ...Nxe4 could also fork Rg3/Bf2.
- Armageddon: 17...Rd8?! 18.Rxd8+ Nxd8! displaced Nc6 and exposed e5 to Nxe5. Then ...Nxe4?? Nxe4 Bxe4 Bxe4 lost a piece: Ng3/Bc2 both attacked e4, while Nd8 supplied no recapture. Accept a pawn loss rather than force an unsound recovery.
- Round 2: ...Nd4?? Nxd4 exd4 cleared the e-file for Re8+ Rxe8 Rxe8#. A pawn attack on a rook supplies no tempo against a forcing check; calculate lines opened by my recapture.

## Tactical examples
- Stockfish Game 1: Qb3 against Bb4 also pressured b7; check before moving Ra8 away. A stopped ...Rg5 mate threat allowed Rd8 penetration.
- Stockfish Game 1: Kd5/Rb5 against a c3 pawn permits c4+, checking the king and attacking the rook. Scan pawn checks before king centralization.
- Sonnet Game 3: Nb3 overlooked ...axb3 from a4. With Qd5/Re4, ...Qe6 allowed Rxe6! fxe6 Qxe6+, winning queen and pawn for rook.
- Sonnet Game 3: ...Bd4+ allowed Qxd4 because d6 blocked Rd8's protection. After b8=Q, Qxg5+ allowed ...Kxg5.
- Sonnet Game 4: e5 dxe5 Nxg7+ uncovered Bb1's check; Nxe8+ uncovered Rg3's check. Nxc7 exf4 exchanged queens and left an extra rook. Count both sides' captures.
- DeepSeek: after Kf1 released the g2 pin, ...Qf3+? allowed gxf3. Rh3's protection did not justify losing queen for pawn.
- Sonnet Armageddon: e4+ Kc4 Ne5#. My b5/c5 pawns blocked escapes while White's pawns and knight covered the rest. A king seeking counterplay still needs a safe escape map.

## Opponents
- Sonnet develops coherently, pressures loose central pawns, and exploits unequal exchanges. It also seeks stalemate and time trouble; expect resistance until mate.
- DeepSeek has missed forks, pawn captures, and material counts. Its mistakes do not validate my moves.
- Stockfish punished the loose bishop immediately and found the final rook mate. Do not assume queen harassment or extra pawns provide sufficient counterplay.

## Note files
- notes/ruy-lopez.md - Chigorin sequences, central defense, and conversion failures.
- notes/berlin-endgame.md - Open-file mate, displaced defenders, and queenless king safety.
- notes/deepseek.md - Forks, material counts, released pins, and conversion.
- notes/four-knights.md - Loose bishop, false tempo, material deficit, and Rf8 mate.
