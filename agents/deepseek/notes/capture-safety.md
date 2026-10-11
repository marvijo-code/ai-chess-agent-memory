# Pre-move scan & blunder catalogue (g1-g116)

## Before every move (final board)
1. Legality: paths clear; two units -> full name; O-O needs f1/g1 empty + knight off home; re-read after captures; a rejection = recheck (g114 cost 1:12).
2. Knight sweep: his knights' 8 squares on my destination, before any queen move. A knight CHECK is no exception (g115 18...Nc3+?? Qxc3: b2-pawn attacks c3, Qf3 covers rank 3).
3. PAWN first: never a piece where his pawn takes it (g109 13...Nc5? dxc5; g113 14.Nd5?? cxd5; g114 16.Bd5?? exd5; g115 21...Bf6?? exf6). No piece on f6/d6 while his e5-pawn stands.
4. Destination: his LAST move's attacks - rook files, bishop rays incl. parked (g105 Bc6; g108 Qxb7?? Bxb7). attacked+undefended -> save NOW; re-list guards after ANY trade.
5. Queen: hit -> moves THAT move; 'defended' never counts. No capture on a defended square or standing bishop ray; count EVERY defender incl. knights/pawns (g110 13...Qxd4??; g114 23.Qxd4??; g115 22...Qxf4??). Queen check only if his king CANNOT take (g106).
6. Captures: name every recapturer + his 2nd attacker; write HIS recapture and material (g111 Rxc6?? Rxc6 = R for P). Count EVERY defender of the target, not just the piece I attack: g116 15...Nd3?? Bxd3 (no recapture), 20...Rxc3?? bxc3 (R for P), 22...Rd2?? Rxd2.
7. Blocked guard = NO guard (g112 13.Ba3?? Bxa3: a2/b3 blocked both recaptures).
8. Retreat needs a pawn/2nd guard; queen-only guard loses to Qx/Q-trade/Rx; king-only guard = no guard (g110 24...Nc5 -> Rxc5+).
9. Pawn push: write the squares it ABANDONS (g111 21.c4?? left d4).
10. Mate nets: Qh2/Rh1; Qxg2# (g101,g102); Qd1+ Rf1 Qxf1# (g108); Bb7 battery: Qxg2/h1# (g113,g114). Scan HIS mates every ply when down.
11. Down: keep queens; repetition; no claw-back grabs. Up: no risk (g112 38...Rg2?? Kxg2); escort passers; promote; mate; stalemate-check; 5-10 s.
12. IQP: count attackers/defenders of d4 before moving a guard (g114 14...Nxd4! won P). Equal = hold; routine <=15 s; long thinks never prevented a blunder (g106-g116).

## Patterns
- A CHECK is not forcing: his replies include CAPTURING the checker (g115 b2 attacks c3, waived - 19.Qxc3).
- Queen on an attacked square moves THAT move; 'defended' never counts (g41,g94,g95,g100).
- Parked bishop: list its whole ray before ANY piece/queen move (g105,g108,g109,g114).
- SELF-BAN: a move my scan or note called bad is DEAD (g98,g103,g105,g108,g109,g111,g115).
- A piece attacked must flee PAWN-SAFE, not merely 'strong'; his bishop's ray counts too (g116 Nd3??).

## Key games
- g116 Caro Advance vs Sonnet (0-1 m24): 12.Nxf5 exf5 orphaned d5 -> 15.Qxd5; 15...Nd3?? Bxd3, 20...Rxc3?? bxc3, 22...Rd2?? Rxd2; ended 8:30 vs 13:08.
- g115 Classical Caro vs Sol (0-1, Qg7# m29): equal to m18; 18...Nc3+?? Qxc3, 21...Bf6?? exf6, 22...Qxf4?? 23.Bxf4. 43-45 s/move 14-22.
- g114 QGD Bxf6 vs Sol (0-1, Qh1# m27): 14...Nxd4! won P after 14.Qe2?!; 16.Bd5?? exd5; 21.Nd6?? Qxd6; 23.Qxd4?? Qxd4; Be5+/Bxf4+/Qh1#; 11:16 vs 15:10.
- g112 Caro Advance vs Sonnet (1-0 m58): 13...Bxa3! won a piece (a2/b3 blocked recaptures); 38...Rg2?? Kxg2.
