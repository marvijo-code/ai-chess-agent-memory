# Pre-move scan & blunder catalogue (g1-g119)

## Before every move (final board)
1. Legality: paths clear; two units -> full name; O-O needs f8/g8 empty + knight off home; own piece blocking a queen line = illegal (g118 Qh5). A rejection = recheck, never guess.
2. COUNT MY GUARDS on the destination BEFORE the move: 0 of mine + his queen/bishop/rook/knight/king can take it = gift (g118 11.Bf4?? Qxf4, 12.Nd5?? cxd5, 13.Qxd5?? Nxd5; g119 20...Nxf2?? 24.Kxf2).
3. Knight sweep: his knights' 8 squares on my destination, before any queen move (g118 Qd5 was a knight square). His KING's square counts too (g119 20...Nxf2??).
4. PAWN first: never a piece where his pawn takes it (g109 13...Nc5?; g113 14.Nd5??; g118 12.Nd5??). No piece on f6/d6 while his e5-pawn stands (g115,g117). A defender his pawn can kick with tempo is no defender (g119 13...Nc5? 15.b4!).
5. Destination: his LAST move's attacks - rook files, bishop rays incl. parked (g105 Bc6; g108 Qxb7?? Bxb7). attacked+undefended -> save NOW; re-list guards after ANY trade.
6. Knight jump onto a covered square = piece for nothing: check BISHOP rays first, then pawns/knights/king. 'Attacks his queen' is no tempo (g116,g117). No recapture of mine = never.
7. Queen: hit -> moves THAT move; 'defended' never counts. No capture on a defended square, a standing bishop ray, or a square his KNIGHT attacks (g118 13.Qxd5?? Nxd5); count EVERY defender (g110).
8. Captures: name every recapturer + his 2nd attacker (g111 Rxc6?? Rxc6 = R for P; g116 ...Nd3?? Bxd3).
9. Blocked guard = NO guard (g112 13.Ba3?? Bxa3). Retreat needs a pawn/2nd guard; queen-only guard loses to Qx/Q-trade/Rx; king-only guard = no guard. Queen as the ONLY guard: a knight capture WITH CHECK wins Q for N (g119 16...Qd6?? 17.Nxe6+ Qxe6 18.Qxe6).
10. Pawn push: write the squares it ABANDONS (g111 21.c4?? left d4).
11. Mate nets: Qh2/Rh1; Qxg2#/Bb7 (g113); Qd1+ Be5+ Qh1# (g114); Rg7# (g117); Qxh2+ Kf1 Qh1# (g118). Scan HIS mates every ply when down.
12. A CHECK is not forcing: he may CAPTURE the checker (g115 18...Nc3+?? Qxc3; g119 24...Be3+?? Bxe3).
13. Down: keep queens; repetition; no piece-for-pawn; no zero-guard 'activity' move; keep blockaders home. Up: escort passers; promote; mate; stalemate-check; 5-10 s.
14. Equal = hold; routine <=15 s, cap 20 s; long thinks never prevented a blunder (g114-g119: 19-74 s on moves 8-22, every game blundered).

## Patterns
- SELF-BAN: a move my scan or note called bad is DEAD (g118 11.Bf4?? was flagged in my own note).
- Count MY defenders on the destination first, every single move; list parked bishops' rays.

## Key games
- g119 Caro 4.h4 h5 vs SF19 (DRAW): 10...cxd4?! 11.cxd5! exd5 12.e6! fxe6 13...Nc5? 15.b4! 16.Nxd4 (d4 unguarded since m10) 16...Qd6?? 17.Nxe6+ Qxe6 18.Qxe6 = Q for N; then Kg8/Kh7 shuttles -> threefold. 19-41 s/move.
- g118 Scotch vs Sonnet (0-1 m18): 7.Be2?? Qxe5; 11.Bf4?? Qxf4; 12.Nd5?? cxd5; 13.Qxd5?? Nxd5; Qxh2+/Qh1#. 38-74 s on moves 8-13.
- g117 Classical Caro vs Sol (0-1 m36, Rg7#): 17...Nxf4?? Bxf4; 20...Bf6?? exf6; keep the d5 blockader.
- g116 Caro Advance vs Sonnet (0-1 m24): 12.Nxf5 exf5 orphans d5; 15...Nd3?? Bxd3; 20...Rxc3?? bxc3; 22...Rd2?? Rxd2.
- g115 Classical Caro vs Sol (0-1, Qg7# m29): 18...Nc3+?? Qxc3; 21...Bf6?? exf6; 22...Qxf4?? Bxf4.
- g114 QGD Bxf6 vs Sol (0-1, Qh1# m27): 16.Bd5?? exd5; 21.Nd6?? Qxd6; 23.Qxd4?? Qxd4.
- g112 Caro Advance vs Sonnet (1-0 m58): 13...Bxa3! won a piece; 38...Rg2?? Kxg2.
