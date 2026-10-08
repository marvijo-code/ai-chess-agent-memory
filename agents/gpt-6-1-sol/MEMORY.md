# Chess memory

## Move discipline
- Before choosing a move, scan the opponent's checks, captures, and pawn attacks. Repeat on the resulting position, including attacks on loose pieces elsewhere. Check every destination against enemy pawns, including advanced flank pawns.
- When a piece is attacked, examine captures and counterthreats before retreating. Trace long-range defenders through vacated squares; friendly blockers interrupt protection.
- Recount central pawn defenders after knight reroutes or exchanges. An attractive outpost can leave the center undefended.
- Calculate the strongest defense to an attacking threat. A mate threat earns no compensation if a simple pawn move stops it and permits invasion.
- Check is not protection: before any queen check, explicitly test ...KxQ and all other captures of the queen. After promotion, keep both queens safe unless sacrificing one has a concrete purpose.
- Clock: use quick decisions for familiar development, forced recaptures, and simple winning conversions; reserve longer calculation for tactical turning points. Game 1 left almost six minutes unused despite a decisive miss; game 3 spent heavily on middlegame maneuvering and finished with 21 seconds. More thinking helps only with a systematic threat scan.

## Game 1: Black vs Stockfish 19, loss
- Symmetrical Four Knights: 1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4. After 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6, material is balanced. The counterattack on f3 enables this exchange sequence.
- After 10.Bc4 Be6 11.Bxe6, ...fxe6 was necessary and opened the f-file with tempo. After 14.c3, ...Ba5 was the only good move in postgame analysis. Improve earlier planning rather than rejecting forced responses.
- White Qb3 and Black Bb4: c3 followed by a bishop retreat exposes b7 to Qxb7. Calculate this before committing Ra8 to e8.
- 18...Qg6 was inaccurate. After 19.Bxb6 axb6 20.Qxc7 Rg5 21.g3, the mate threat was stopped; 21...h5 allowed 22.Rd8 Rxd8 23.Qxd8+. Assess d-file penetration before spending tempi on ...h5-h4.
- With my rook on b5 and White's pawn on c3, 33...Kd5 allowed 34.c4+, checking the king and attacking the rook. Check pawn pushes with check before centralizing the king.

## Game 2: Black vs DeepSeek V4.1 Flash, win
- Sound Chigorin setup: ...a6, ...Nf6, ...Be7, ...b5, ...O-O, ...d6, then 9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6. After 14.Nb3 a5 15.d5, ...Nb4 attacked Bc2. No Black moves received postgame marks; White's 16.a3?? supplied the decisive advantage.
- Qc7 defended c2 along the cleared c-file. After 16.a3 Nxc2, the knight captured a bishop and forked Ra1/Re1. White's 17.Qxc2 Qxc2 lost the queen. A pawn attack on a knight does not remove its tactical threat.
- Convert by taking concretely safe loose material and removing counterplay. Do not assume an opponent will repeat its errors.
- Played mating pattern: ...Bxf2+ with Ne4 protecting the bishop, ...Qa1+, ...Rad8, then ...Qxb2+ Nxb2 Rd2+ Kf1 Ng3#. ...Ng3 opened Bb7's diagonal toward g2; Bf2 covered e1/g1 and Rd2 covered e2. This line does not prove every king defense was forced.

## Game 3: White vs Sonnet 5.5, win from a losing position
- Closed Ruy Lopez: after the Chigorin sequence above, 14.Nb3 a5 15.Be3 a4 16.Nbd2, then Nf1-g3 and Rc1 developed coherently. With Rc1 facing Qc7, 20.d5 Nb4 21.Bb1 uncovered an attack on the queen; only then 22.a3 drove the knight away. Preserve the bishop before playing a3 when ...Nxc2 is available.
- The kingside knight plan did not secure the center: after Nh4-f5, ...Bxf5 and Ng3xf5, e4 had only Bb1 defending it against Nc5 and Nf6. Black won it with ...Ncxe4 Bxe4 Nxe4. Recount defenders before committing to an outpost.
- Postgame marks: 28.Qg3? 29.Rcd1?! 30.Nh4? 31.Nf3?!. The sequence allowed central pawn losses and consumed time. Queen activity and rook pressure require concrete threats; do not assume they compensate for material.
- 34.Nd4 Qd7 35.Nb3?? overlooked Black's pawn on a4: ...axb3 won the knight. This obvious capture was absent from the supplied move marks; those marks are not an exhaustive error list. Scan pawn attacks on every proposed retreat square.
- Keep seeking concrete counterplay when behind. With Qd5 and Re4, 42...Qe6?? allowed 43.Rxe6! fxe6 44.Qxe6+, exchanging a rook for queen and pawn. Compare both rook and queen captures when offered a queen trade.
- 45...Bd4+?? allowed 46.Qxd4: Black's d6 pawn blocked Rd8's protection of the bishop. A checking piece can still be undefended.
- After 57.b8=Q, 58.Qxg5+?? allowed ...Kxg5 and unnecessarily lost one queen. Still winning is not a reason to skip capture checks. Convert queen endings by restricting the king, bringing up my king, and delivering a protected mate; avoid stalemate.
- Sonnet observation, one game only: exploited loose central pawns and the knight on b3, then missed rook captures of its queen, capture of its checking bishop, and an attacked rook. Its tactical errors supplied the recovery; the result does not validate my middlegame play.

## Note files
None.
