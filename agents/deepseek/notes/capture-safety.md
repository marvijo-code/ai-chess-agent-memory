# Pre-move scan & blunder catalogue (g1-g122)

## Before every move (final board)
1. Legality: paths clear; two units -> full name; O-O needs f8/g8 empty + knight off home; own piece blocking a queen line = illegal (g118). Rejection = recheck, never guess (g120,g122).
2. COUNT MY GUARDS on the destination BEFORE the move: 0 of mine + any enemy queen/bishop/rook/knight/king = gift (g118 11.Bf4?? Qxf4; g119 20...Nxf2?? Kxf2).
3. Knight sweep: his knights' 8 squares on my destination before any queen move (g118 Qd5); his KING's square counts (g119).
4. PAWN first: never a piece where his pawn takes it (g109,g113). No piece on f6/d6 while his e5-pawn stands (g115,g117; g122 14...Bf6? exf6). A knight left on f6 in front of that pawn falls (g122 17...Rfe8?? exf6). A defender his pawn kicks with tempo is no defender (g119 13...Nc5? 15.b4!).
5. Destination: his LAST move's attacks - rook files, bishop rays incl. parked (g105,g108). attacked+undefended -> save NOW; re-list guards after ANY trade.
6. Knight jump onto a covered square = piece for nothing; bishop rays first, then pawns/knights/king. 'Attacks his queen' is no tempo (g116,g117).
7. Queen: hit -> moves THAT move; 'defended' never counts. No capture on a defended square, a standing bishop ray, or a knight square (g118 13.Qxd5?? Nxd5); count EVERY defender incl. the pawn that recaptures her (g122 16...Qxe5?? dxe5).
8. Captures: name every recapturer + his 2nd attacker (g111 Rxc6?? Rxc6; g116 ...Nd3?? Bxd3).
9. Blocked guard = NO guard (g112 13.Ba3?? Bxa3). Queen-only guard loses to Qx/Q-trade/Rx; king-only = no guard. Queen as ONLY guard: knight capture WITH CHECK wins Q for N (g119 16...Qd6?? 17.Nxe6+).
10. A queen trade may hide an INTERMEZZO: he checks/captures with tempo, then a discovered check, then a pawn takes my queen (g120 13...Qb6?? 14.Qxd7+ Kxd7 15.dxc5+ 16.cxb6). List HIS checks/captures before my recapture.
11. Pawn push: write the squares it ABANDONS (g111 21.c4?? left d4).
12. Mate nets: Qh2/Rh1; Qxg2#/Bb7 (g113); Qd1+ Be5+ Qh1# (g114); Rg7# (g117); Rd8# (g120); Qh6+Ng5 (g122 19.Qg7#).
13. A CHECK is not forcing: he may CAPTURE the checker (g115 18...Nc3+?? Qxc3).
14. Down: keep queens; repetition; no piece-for-pawn; move loose pieces (g122 Nf6 fell); no self-blocks near my king. Up: escort passers; promote; mate; stalemate-check; 5-10 s.
15. Equal = hold; routine <=15 s, cap 20 s; long thinks never prevented a blunder (g120 72 s Qb6??; g122 40 s Bf6? exf6).

## Patterns
- SELF-BAN: a move my scan or note called bad is DEAD (g118 11.Bf4??, g122 14...Bf6?).
- Count MY defenders on the destination first, every move; list parked bishops' rays.

## Key games
- g122 Caro Advance 4.Nf3 vs Sonnet (0-1, Qg7# m19): 9...Nh6?! Bxh6 gxh6; 11...O-O? Bxg6 hxg6; 13.Qd2 Qxh6 (h6 free); 14...Bf6? exf6; 16...Qxe5?? dxe5 (Q for N, d4 guarded e5); 17...Rfe8?? exf6.
- g120 Caro 4.h4 h5 vs SF19 (0-1, Rd8# m21): 13...Qb6?? 14.Qxd7+ Kxd7 15.dxc5+ 16.cxb6 = Q for P; 20...Ne7?? 21.Rd8#. Fix: 12...Nd7?! 13.Rd1! -> 12...Qd7!.
- g119 Caro 4.h4 h5 vs SF19 (DRAW): 10...cxd4?! 11.cxd5! exd5 12.e6!; 13...Nc5? 15.b4!; 16...Qd6?? 17.Nxe6+ Qxe6 18.Qxe6; Kg8/Kh7 shuttles -> threefold.
- g118 Scotch vs Sonnet (0-1 m18): 7.Be2?? Qxe5; 11.Bf4?? Qxf4; 12.Nd5?? cxd5; 13.Qxd5?? Nxd5.
- g117/g115 Classical Caro vs Sol (0-1 m36 Rg7# / m29 Qg7#): 17...Nxf4?? Bxf4; 20...Bf6??/21...Bf6?? exf6; 22...Qxf4?? Bxf4; 18...Nc3+?? Qxc3.
- g116 Caro Advance vs Sonnet (0-1 m24): 12.Nxf5 exf5 orphans d5; 15...Nd3?? Bxd3; 20...Rxc3?? bxc3; 22...Rd2?? Rxd2.
- g114 QGD Bxf6 vs Sol (0-1, Qh1# m27): 16.Bd5?? exd5; 21.Nd6?? Qxd6; 23.Qxd4?? Qxd4.
- g112 Caro Advance vs Sonnet (1-0 m58): 13...Bxa3! won a piece; 38...Rg2?? Kxg2.
