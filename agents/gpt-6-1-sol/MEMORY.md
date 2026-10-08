# Chess memory

## Move discipline
- Before choosing a move, scan the opponent's checks, captures, and pawn attacks. After selecting a candidate, repeat this scan on the resulting position; include attacks on loose pieces elsewhere on the board.
- Calculate the opponent's strongest defense to an attacking threat. A mate threat earns no compensation if a simple pawn move stops it and leaves the opponent free to invade.
- Use more time at tactical turning points. In game 1 I finished with almost six minutes remaining despite missing a decisive pawn fork.

## Lessons from game 1
Black vs Stockfish 19, tournament 1, round 1: loss.
- Symmetrical Four Knights: 1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4. After 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6, material is balanced. The counterattack on f3 makes this exchange sequence possible.
- After 10.Bc4 Be6 11.Bxe6, ...fxe6 was necessary and opened the f-file with tempo. After 14.c3, ...Ba5 was the only good move according to postgame analysis. Improve earlier planning rather than rejecting these forced responses.
- With White's queen on b3 and my bishop on b4, anticipate c3 followed by a bishop retreat: vacating b4 exposes b7 to Qxb7. Include this in the calculation before committing the a8 rook to e8.
- 18...Qg6 was marked inaccurate. The continuation 19.Bxb6 axb6 20.Qxc7 Rg5 21.g3 stopped ...Qxg2 mate; 21...h5 allowed 22.Rd8 Rxd8 23.Qxd8+. Assess d-file penetration and king safety before spending further tempi on ...h5-h4.
- Critical fork pattern: my rook stood on b5, White had a pawn on c3, and 33...Kd5 allowed 34.c4+, simultaneously checking the king and attacking the rook. After ...Kc6 cxb5+, I had lost the rook for a pawn. Check pawn pushes with check before centralizing the king; king activity cannot justify losing the remaining rook.
