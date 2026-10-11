# Pre-move scan & blunder catalogue (g1-g125)

## Before every move (final board)
1. Legality: paths clear; two units -> full name; O-O needs f8/g8 empty + knight off home (g118,g123); g124 Ng8 home and I tried O-O anyway though my own note said no. Rejection = recheck, never guess (g120,g122,g124).
2. COUNT MY GUARDS on my destination: 0 of mine + any enemy capture = gift (g118,g119).
3. Knight sweep: his knights' 8 squares on my destination before any queen move (g118 Qd5); his KING's square counts (g119).
4. PAWN first: never a piece where his pawn takes it. No piece on f6/d6 while his e5-pawn stands (g122). A defender his pawn kicks with tempo is no defender (g119 13...Nc5?). His h4-pawn takes a bishop on g5 (g125 16...Bg5?? hxg5 = B for P); before offering a bishop list EVERY pawn capture. Same class: g122 16...Qxe5?? dxe5 (queen onto a pawn square).
5. Destination: his LAST move's attacks - rook files, bishop rays incl. parked. attacked+undefended -> save NOW; re-list guards after ANY trade. A rook on e6 owns the whole 6th rank: 23...Qd6?? Rxd6+ = Q for R (g125).
6. Knight jump onto a covered square = piece for nothing; bishop rays first, then pawns/knights/king (g116,g117).
7. Queen: hit -> moves THAT move; 'defended' never counts. No capture on a defended square, a standing bishop ray (g118 13.Qxd5?? Nxd5); count EVERY defender incl. PAWNS (g123 16.Qxd5?? c6+e6).
8. Captures: name every recapturer + his 2nd attacker (g111 Rxc6?? Rxc6).
9. Blocked guard = NO guard (g112). Queen-only guard loses to Qx/Q-trade/Rx; king-only = no guard. Queen as ONLY guard: knight capture WITH CHECK wins Q for N (g119 16...Qd6?? 17.Nxe6+).
10. My capture he answers with CHECK or tempo: tempo first; if my queen must block on the square he then takes her, Q lost (g123 Qxd5?? Bxg5+ Qd2 Bxd2+).
11. Pawn push: write the squares it ABANDONS; pawn grab: write the LINE it leaves (g124 Qxb2?? left b6-c7-d8: no block for Rxc8+, mate).
12. Mate nets: Qh2/Rh1; Qxg2#/Bb7 (g113); Qd1+Be5+Qh1# (g114); Rg7# (g117); Rd8# (g120); Qh6+Ng5 (g122); Rxd1# (g123); Rxc8+ Bd8 Rxd8# (g124).
13. A CHECK is not forcing: he may CAPTURE the checker (g115 18...Nc3+?? Qxc3).
14. Down: keep queens; repetition; no piece-for-pawn; loose pieces first (g122 Nf6 fell; g125 35...Rf8?? Qb4+ Qe7+ Qxf8 - never on his queen's route); no self-blocks near my king. Up: escort passers; promote; mate; stalemate-check; 5-10 s.
15. Equal = hold; routine <=15 s, cap 20 s; long thinks never prevented a blunder (g120 72 s; g122 40 s; g123 44 s; g124 32-50 s; g125 30-41 s).

## Patterns
- SELF-BAN: a move my scan or note called bad is DEAD (g124: 'no O-O yet' then O-O; g125 16...Bg5?? after g122 warned the pawn-take class).
- Count MY defenders on the destination first, every move; list parked bishops' rays and his rooks' ranks.

## Key games
- g125 Caro 4.h4 h5 5.Bd3 (0-1, Qb5# m43): 16...Bg5?? hxg5 = B for P; 23...Qd6?? Rxd6+; 35...Rf8?? Qb4+ Qe7+ Qxf8. The ...Nb6/...Nc4 knight play was fine - loss was three one-move scans, not the opening.
- g124 Caro Advance 5.Bd3 vs SF19 (0-1, Rxd8# m17): 11...O-O illegal (Ng8 home); 13...Bf8?! 14.Bg5! Be7?! 15.Rfc1! Qxb2?? 16.Rxc8+ Bd8 17.Rxd8#. King e8 + open c-file + his Bg5-eye on d8 = no pawn grabs; keep a blocker on b6-c7-d8.
- g123 Caro W 3.Nc3 vs Sol (0-1, Rxd1# m23): 16.Qxd5?? Q for N; 23.Rxf5?? Rxd1# (K b1, no luft).
- g122 Caro Advance 4.Nf3 vs Sonnet (0-1, Qg7# m19): 9...Nh6?! Bxh6 gxh6; 14...Bf6? exf6; 16...Qxe5?? dxe5; 17...Rfe8?? exf6.
- g120 Caro 4.h4 h5 vs SF19 (0-1, Rd8# m21): 13...Qb6?? 14.Qxd7+ Kxd7 15.dxc5+; 20...Ne7?? 21.Rd8#.
- g119 Caro 4.h4 h5 vs SF19 (DRAW): 16...Qd6?? 17.Nxe6+; Kg8/Kh7 -> threefold.
- g121 Chigorin W vs Sonnet (0-1 m43): own Bd2 blocked Qd1-d4; 19...exd4! 20.Nxd4?? Nxd4.
