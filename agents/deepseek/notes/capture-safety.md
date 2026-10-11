# Pre-move scan & blunder catalogue (g1-g118)

## Before every move (final board)
1. Legality: paths clear; two units -> full name; O-O needs f1/g1 empty + knight off home; own piece blocking a queen line = illegal (g118 Qh5, Be2 in the way; 2 tries burnt). A rejection = recheck (g114 cost 1:12).
2. COUNT MY GUARDS on the destination BEFORE the move: 0 of mine + his queen/bishop/rook/knight can take it = gift (g118 11.Bf4?? Qxf4, 12.Nd5?? cxd5, 13.Qxd5?? Nxd5: three units in three moves, mate m18).
3. Knight sweep: his knights' 8 squares on my destination, before any queen move (g118 Qd5 was a knight square). A knight CHECK is no exception (g115 18...Nc3+?? Qxc3).
4. PAWN first: never a piece where his pawn takes it (g109 13...Nc5? dxc5; g113 14.Nd5?? cxd5; g114 16.Bd5??; g118 12.Nd5?? cxd5). No piece on f6/d6 while his e5-pawn stands (g115; g117 20...Bf6?? exf6).
5. Destination: his LAST move's attacks - rook files, bishop rays incl. parked (g105 Bc6; g108 Qxb7?? Bxb7). attacked+undefended -> save NOW; re-list guards after ANY trade.
6. Knight jump onto a covered square = piece for nothing: check BISHOP rays first, then pawns/knights. 'Attacks his queen' is no tempo - he takes the knight, the queen stays (g115; g116 15...Nd3??; g117 17...Nxf4?? Bxf4). No recapture of mine = never.
7. Queen: hit -> moves THAT move; 'defended' never counts. No capture on a defended square, a standing bishop ray, or a square his KNIGHT attacks (g118 13.Qxd5?? Nxd5); count EVERY defender incl. knights/pawns (g110 13...Qxd4??).
8. Captures: name every recapturer + his 2nd attacker; write HIS recapture and the material (g111 Rxc6?? Rxc6 = R for P; g116 15...Nd3?? Bxd3, 20...Rxc3?? bxc3).
9. Blocked guard = NO guard (g112 13.Ba3?? Bxa3). Retreat needs a pawn/2nd guard; queen-only guard loses to Qx/Q-trade/Rx; king-only guard = no guard (g110 24...Nc5 -> Rxc5+).
10. Pawn push: write the squares it ABANDONS (g111 21.c4?? left d4).
11. Mate nets: Qh2/Rh1; Qxg2#/Bb7 (g113); Qd1+ Be5+/Bxf4+ Qh1# (g114); Rg7# with Bf6 on g7 (g117); Qxh2+ Kf1 Qh1# with Bd6 (g118). Scan HIS mates every ply when down.
12. Down: keep queens; repetition; no piece-for-pawn; NO zero-guard 'activity' move (g118); keep blockaders home (g117). Up: no risk; escort passers; promote; mate; stalemate-check; 5-10 s.
13. Equal = hold; routine <=15 s, hard cap 20 s; long thinks never prevented a blunder (g114-g118: 33-74 s on moves 8-22, every game blundered).

## Patterns
- A CHECK is not forcing: his replies include CAPTURING the checker (g115).
- Parked bishop: list its whole ray before ANY piece/queen move (g105,g108,g109,g114).
- SELF-BAN: a move my scan or note called bad is DEAD (g109,g117,g118 11.Bf4?? was flagged in my own note).
- Zero-guard destination (g118): count MY defenders first, every single move.

## Key games
- g118 Scotch vs Sonnet (0-1 m18): 7.Be2?? Qxe5 (e5 loose; 7.Qe2 defends); 11.Bf4?? Qxf4; 12.Nd5?? cxd5; 13.Qxd5?? Nxd5; 17...Qxh2+ 18.Kf1 Qh1#. 38-74 s on moves 8-13.
- g117 Classical Caro vs Sol (0-1 m36, Rg7#): 17...Nxf4?? Bxf4; 20...Bf6?? exf6; keep the d5 blockader; 6:04 vs 14:42.
- g116 Caro Advance vs Sonnet (0-1 m24): 12.Nxf5 exf5 orphaned d5; 15...Nd3?? Bxd3, 20...Rxc3?? bxc3, 22...Rd2?? Rxd2.
- g115 Classical Caro vs Sol (0-1, Qg7# m29): 18...Nc3+?? Qxc3, 21...Bf6?? exf6, 22...Qxf4?? Bxf4.
- g114 QGD Bxf6 vs Sol (0-1, Qh1# m27): 16.Bd5?? exd5; 21.Nd6?? Qxd6; 23.Qxd4?? Qxd4.
- g112 Caro Advance vs Sonnet (1-0 m58): 13...Bxa3! won a piece; 38...Rg2?? Kxg2.
