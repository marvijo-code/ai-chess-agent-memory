# Chess memory

## Move discipline
- Before choosing a move, scan the opponent's checks, captures, and pawn attacks. Repeat on the resulting position, including attacks on loose pieces elsewhere.
- Calculate the strongest defense to an attacking threat. A mate threat earns no compensation if a simple pawn move stops it and permits invasion.
- When a piece is attacked, check captures and counterthreats before retreating. Trace long-range defenders through recently vacated squares.
- Use more time at tactical turning points. Game 1 ended with almost six minutes unused despite a decisive missed pawn fork; game 2's comfortable clock does not justify rushing stronger opposition.

## Game 1: Black vs Stockfish 19, loss
- Symmetrical Four Knights: 1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4. After 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6, material is balanced. The counterattack on f3 enables this exchange sequence.
- After 10.Bc4 Be6 11.Bxe6, ...fxe6 was necessary and opened the f-file with tempo. After 14.c3, ...Ba5 was the only good move in postgame analysis. Improve earlier planning rather than rejecting forced responses.
- White Qb3 and Black Bb4: c3 followed by a bishop retreat exposes b7 to Qxb7. Calculate this before committing Ra8 to e8.
- 18...Qg6 was inaccurate. After 19.Bxb6 axb6 20.Qxc7 Rg5 21.g3, the mate threat was stopped; 21...h5 allowed 22.Rd8 Rxd8 23.Qxd8+. Assess d-file penetration and king safety before spending tempi on ...h5-h4.
- Pawn-fork warning: with my rook on b5 and White's pawn on c3, 33...Kd5 allowed 34.c4+, checking the king and attacking the rook. After ...Kc6 cxb5+, the rook was lost for a pawn. Check pawn pushes with check before centralizing the king.

## Game 2: Black vs DeepSeek V4.1 Flash, win
- Sound Chigorin Ruy Lopez setup: ...a6, ...Nf6, ...Be7, ...b5, ...O-O, ...d6, then 9...Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6. After 14.Nb3 a5 15.d5, ...Nb4 attacked Bc2. No Black moves received postgame marks; the decisive advantage came from White's 16.a3??.
- Tactical geometry: Qc7 defended c2 along the cleared c-file. After 16.a3 Nxc2, the knight captured a bishop and forked Ra1/Re1. White's 17.Qxc2 Qxc2 lost the queen. A pawn attack on the knight did not remove its tactical threat.
- Convert by taking safe material and removing counterplay: ...Qxb3 took a loose knight, ...dxc5 an exposed bishop, ...Bxd6 the advanced pawn, ...Bxc5 a rook, and ...Qxa2 the remaining rook.
- Finishing pattern in the played line: ...Bxf2+ with Ne4 protecting the bishop, ...Qa1+, and ...Rad8 activated the attack. After ...Qxb2+ Nxb2 Rd2+ Kf1, ...Ng3# checked the king and opened Bb7's diagonal toward g2. Bf2 covered e1/g1 and Rd2 covered e2. The queen sacrifice's success in this line does not establish that every king defense was forced.
- Opponent observation, one game only: DeepSeek continued with loose-piece moves after losing its queen. Recheck each capture concretely; do not assume future games will repeat this behavior.

## Note files
None.
