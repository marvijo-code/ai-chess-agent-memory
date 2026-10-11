# Pre-move scan & blunder catalogue (g1-g117)

## Before every move (final board)
1. Legality: paths clear; two units -> full name; O-O needs f1/g1 empty + knight off home; re-read after captures; a rejection = recheck (g114 cost 1:12).
2. Knight sweep: his knights' 8 squares on my destination, before any queen move. A knight CHECK is no exception (g115 18...Nc3+?? Qxc3).
3. PAWN first: never a piece where his pawn takes it (g109 13...Nc5? dxc5; g113 14.Nd5?? cxd5; g114 16.Bd5?? exd5). No piece on f6/d6 while his e5-pawn stands (g115; g117 20...Bf6?? exf6).
4. Destination: his LAST move's attacks - rook files, bishop rays incl. parked (g105 Bc6; g108 Qxb7?? Bxb7). attacked+undefended -> save NOW; re-list guards after ANY trade.
5. Knight jump onto a covered square = piece for nothing: check BISHOP rays first, then pawns/knights. 'Attacks his queen' is no tempo - he takes the knight, the queen stays (g115 18...Nc3+??; g116 15...Nd3??; g117 17...Nxf4?? Bxf4, c1-d2-e3-f4). No recapture of mine = never.
6. Queen: hit -> moves THAT move; 'defended' never counts. No capture on a defended square or standing bishop ray; count EVERY defender incl. knights/pawns (g110 13...Qxd4??; g114 23.Qxd4??; g115 22...Qxf4??). Queen check only if his king CANNOT take (g106).
7. Captures: name every recapturer + his 2nd attacker; write HIS recapture and material (g111 Rxc6?? Rxc6 = R for P). Count EVERY defender: g116 15...Nd3?? Bxd3, 20...Rxc3?? bxc3, 22...Rd2?? Rxd2.
8. Blocked guard = NO guard (g112 13.Ba3?? Bxa3: a2/b3 blocked both recaptures).
9. Retreat needs a pawn/2nd guard; queen-only guard loses to Qx/Q-trade/Rx; king-only guard = no guard (g110 24...Nc5 -> Rxc5+).
10. Pawn push: write the squares it ABANDONS (g111 21.c4?? left d4).
11. Mate nets: Qh2/Rh1; Qxg2# with Bb7 (g113); Qd1+ Be5+/Bxf4+ then Qh1# (g114); Rg7# with Bf6 guarding g7 and Ng6 covering f8/h8 (g117 m36). Scan HIS mates every ply when down.
12. Down: keep queens; repetition; no piece-for-pawn; keep blockaders home (g117 Nd5 jumped for a fake tempo). Up: no risk; escort passers; promote; mate; stalemate-check; 5-10 s.
13. Equal = hold; routine <=15 s, hard cap 20 s; long thinks never prevented a blunder (g114-g117: 33-49 s on moves 10-22, still blundered).

## Patterns
- A CHECK is not forcing: his replies include CAPTURING the checker (g115).
- Queen on an attacked square moves THAT move; 'defended' never counts (g41,g94,g95,g100).
- Parked bishop: list its whole ray before ANY piece/queen move (g105,g108,g109,g114).
- SELF-BAN: a move my scan or note called bad is DEAD (g98,g103,g105,g108,g109,g111,g115,g117).
- Knight-hit-on-queen onto a covered square: 3rd repeat (g115,g116,g117) - always list the landing square's guards (bishop rays first).

## Key games
- g117 Classical Caro vs Sol (0-1 m36, Rg7#): 17...Nxf4?? Bxf4 lost a knight (Bc1 ray c1-d2-e3-f4, no recapture); Nd5 was the blockader - keep it; 20...Bf6?? exf6 B for P; 33-49 s on 14-22; ended 6:04 vs 14:42.
- g116 Caro Advance vs Sonnet (0-1 m24): 12.Nxf5 exf5 orphaned d5 -> 15.Qxd5; 15...Nd3?? Bxd3, 20...Rxc3?? bxc3, 22...Rd2?? Rxd2.
- g115 Classical Caro vs Sol (0-1, Qg7# m29): 18...Nc3+?? Qxc3, 21...Bf6?? exf6, 22...Qxf4?? 23.Bxf4.
- g114 QGD Bxf6 vs Sol (0-1, Qh1# m27): 16.Bd5?? exd5; 21.Nd6?? Qxd6; 23.Qxd4?? Qxd4.
- g112 Caro Advance vs Sonnet (1-0 m58): 13...Bxa3! won a piece (a2/b3 blocked recaptures); 38...Rg2?? Kxg2.
