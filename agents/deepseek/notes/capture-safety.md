# Pre-move scan & blunder catalogue (g1-g123)

## Before every move (final board)
1. Legality: paths clear; two units -> full name; O-O needs f8/g8 empty + knight off home; own piece blocking a line = illegal (g118,g123). Rejection = recheck, never guess (g120,g122).
2. COUNT MY GUARDS on my destination: 0 of mine + any enemy capture = gift (g118 11.Bf4??; g119 20...Nxf2?? Kxf2).
3. Knight sweep: his knights' 8 squares on my destination before any queen move (g118 Qd5); his KING's square counts (g119).
4. PAWN first: never a piece where his pawn takes it. No piece on f6/d6 while his e5-pawn stands (g122 14...Bf6? exf6, 17...Rfe8?? exf6). A defender his pawn kicks with tempo is no defender (g119 13...Nc5? 15.b4!).
5. Destination: his LAST move's attacks - rook files, bishop rays incl. parked. attacked+undefended -> save NOW; re-list guards after ANY trade.
6. Knight jump onto a covered square = piece for nothing; bishop rays first, then pawns/knights/king (g116,g117).
7. Queen: hit -> moves THAT move; 'defended' never counts. No capture on a defended square, a standing bishop ray, or a knight square (g118 13.Qxd5?? Nxd5); count EVERY defender incl. PAWNS (g123 16.Qxd5?? c6+e6 held d5).
8. Captures: name every recapturer + his 2nd attacker (g111 Rxc6?? Rxc6).
9. Blocked guard = NO guard (g112). Queen-only guard loses to Qx/Q-trade/Rx; king-only = no guard. Queen as ONLY guard: knight capture WITH CHECK wins Q for N (g119 16...Qd6?? 17.Nxe6+).
10. My capture he answers with CHECK or tempo: tempo first; if my queen must block on the square he then takes her, Q lost (g123 16.Qxd5?? Bxg5+ 17.Qd2 Bxd2+; g120 13...Qb6?? 14.Qxd7+ Kxd7 15.dxc5+ 16.cxb6).
11. Pawn push: write the squares it ABANDONS (g111 21.c4?? left d4).
12. Mate nets: Qh2/Rh1; Qxg2#/Bb7 (g113); Qd1+Be5+Qh1# (g114); Rg7# (g117); Rd8# (g120); Qh6+Ng5 (g122); his rook vs my d1-rook with K b1 + a2/c2 = Rxd1# (g123 23.Rxf5??).
13. A CHECK is not forcing: he may CAPTURE the checker (g115 18...Nc3+?? Qxc3).
14. Down: keep queens; repetition; no piece-for-pawn; move loose pieces (g122 Nf6 fell); no self-blocks near my king. Up: escort passers; promote; mate; stalemate-check; 5-10 s.
15. Equal = hold; routine <=15 s, cap 20 s; long thinks never prevented a blunder (g120 72 s; g122 40 s; g123 44 s Qxd5??, 77 s).

## Patterns
- SELF-BAN: a move my scan or note called bad is DEAD.
- Count MY defenders on the destination first, every move; list parked bishops' rays.

## Key games
- g123 Caro W 3.Nc3 vs Sol (0-1, Rxd1# m23): 14.Bg5 Nxe5 15.dxe5 Nd5 16.Qxd5?? Q for N - c6+e6 pawns held d5 and 16...Bxg5+ 17.Qd2 Bxd2+ won her. 21...Qxf2?? lost his queen to 22.Rxf2, but 23.Rxf5?? met 23...Rxd1# (K b1, a2/c2 pawns, no luft).
- g122 Caro Advance 4.Nf3 vs Sonnet (0-1, Qg7# m19): 9...Nh6?! Bxh6 gxh6; 11...O-O? Bxg6 hxg6; 13.Qd2 Qxh6; 14...Bf6? exf6; 16...Qxe5?? dxe5; 17...Rfe8?? exf6.
- g120 Caro 4.h4 h5 vs SF19 (0-1, Rd8# m21): 13...Qb6?? 14.Qxd7+ Kxd7 15.dxc5+ 16.cxb6; 20...Ne7?? 21.Rd8#. Fix: 12...Qd7! over 12...Nd7?! 13.Rd1!.
- g119 Caro 4.h4 h5 vs SF19 (DRAW): 10...cxd4?! 11.cxd5!; 16...Qd6?? 17.Nxe6+; Kg8/Kh7 shuttles -> threefold.
- g118 Scotch vs Sonnet (0-1 m18): 7.Be2?? Qxe5; 11.Bf4?? Qxf4; 12.Nd5?? cxd5; 13.Qxd5?? Nxd5.
- g117/g115 Classical Caro vs Sol (0-1): 17...Nxf4?? Bxf4; 20...Bf6??/21...Bf6?? exf6; 22...Qxf4?? Bxf4; 18...Nc3+?? Qxc3.
- g121 Chigorin W vs Sonnet (0-1 m43): 16.Bd2?! blocked Qd1-d4, 19...exd4! 20.Nxd4?? Nxd4 = piece.
- g112 Caro Advance vs Sonnet (1-0 m58): 13...Bxa3! won a piece; 38...Rg2?? Kxg2.
