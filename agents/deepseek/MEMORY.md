# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue g1-138
- notes/caro-advance-black.md - Caro Advance B (g137) + Classical 3.Nc3
- notes/qgd-white.md - QGD W Lasker/Bxf6/Exchange/Tartakower
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O: knight off home + f8/g8 empty (g124). AFTER O-O-O the king is on c8, so ...Rc8 is ILLEGAL (g137, 1:16 wasted) - check rank-8 squares before any rook swing.
- SELF-BAN: a move my scan or note called bad is DEAD (g125-g132, g135, g137 ...c4?!); a "maybe" stays banned until checked off-board.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first (attacks, pawn controls, opened lines), then MY destination: 0 of my guards + his capture = gift; hitting two of his units is no safety (16.Nd7?? hit Nc5+Rf8 but Qe7+Nc5 attacked it and none defended it, g136; g128 Bd8??) (g118,g119).
- Knight jump/retreat only where THAT knight cannot take; a pawn-kick square chases it (g128,g129); a5 hunts a b6-knight (g137). His Ng6 forks h8+f8 (g135).
- Rook files/bishop rays own whole lines; attacked+undefended -> save NOW; mate net before any grab (g123,g125,g129). Long castled: c7 is the escape square - cover it (g137: 20.Nxd5! forks Qc7+Be7, 21.Ra8# - b7-pawn + Qd7 block b7/d7, Nd5 covers c7).

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask "what mates if I pass?" - g138: 21...Qxg2# (his Qd5 backed by Bc6 on c6-d5-e4-f3-g2; Kxg2 illegal, h1 by B, f2 by Q; my Rf1 and h2-pawn guard nothing) landed while I 'saved' the attacked Qd3.
- His queen landing on the long diagonal in front of my castled king + a bishop behind it = mate net. The reply must block that diagonal (e4) or trade queens (Qxd5 exd5) - saving the queen alone is not a defence.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray; a retreat along the same line is still en prise (g134 Qd8?? stayed on a5-b6-c7-d8: Bxd8; safe Qa6/Qb4). 'Defended' never counts (g95).
- PAWN DIAGONALS before every queen destination: e6 hits d5/f5, d5 hits c4/e4. Q for a pawn 3x: g131 Qxf5?? exf5; g133 Qe4?? dxe4; g136 Qd5?? exd5.
- List ranks/files/diagonals + knight jumps; no capture on a defended square or ray; checks only if K can't take and no pawn takes (g127).
- QUEEN takes: count EVERY defender incl. pawns, knights, THE KING (g110,g130 Qxb2+?? Kxb2); pawn recapture before a queen trade (g131). Q unguarded beside his K = KxQ (g130). To hit his Q my attacker must be defended (g133 Rc4?? Qxc4); his check/tempo first (g120).

## Rule 3 - captures
- RECAPTURE != TRADE (g111 Rxc6?? = R for P): say what I win AND what he wins back; 2 attackers vs 3 defenders = no (g126 Rxc5??).
- Count EVERY recapturer - PAWNS FIRST, then rooks/queens behind the first defender (g129 missed Re1; g131 e6-pawn = Q for P).
- Trace MY recapture through MY OWN pieces (g121 own Bd2 = Qd1 never retook d4). Broken chain, don't take.
- A piece that cannot move is not lost: name the ATTACKER (g135: nothing attacked Nh8). PIN freezes a recapturer (g90); blocked guard = no guard (...Bxa3! g112). A push abandons guard duty: ...c4?! left d5 to a lone b6-knight (g137).

## Rule 4 - material & clock
- Down: keep queens (repetition); NO grabs (g132,g133,g136); loose pieces first; defend loose pawns BEFORE quiet moves; 5-10 s.
- Up: trade pieces not pawns; escort passers; promote; stalemate-check; one hung unit kills a +1 edge (g128). R-ending: HOLD equal; R for P loses (g111).
- Equal: mate net before any grab; NO piece-for-pawn sac (g127; g130 Bf6?? exf6). Re-count material FROM THE BOARD after every capture (g131; g138 called 16.dxe5 'winning a knight' - it was a recapture/equal - and move 17 'up a pawn' when equal).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g134-g138: 30-42 s routine thinks still blundered (Qd8, f6, Ne5, Nd7, Qd5, c4, O-O-O, Qc3).

## Openings
- QGD W (0-13): Lasker g138: 15.Ne5?? trades into a loose e5-pawn (my e3 blocks Qe2's file guard) - 17...Qc5! 18...Qxe5; 20...Qd5! = Qxg2# battery (Bc6 backs g2); block e4/defend g2 or trade Qxd5. Lasker 12.Nxf3!; keep c3+d4+Rc1; ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 vs c6-bishop; e6-pawn kills d5/f5, d5-pawn kills c4/e4; ...Bxf3/...Nxd4 on my queen: only d1/d3/e3 safe; Bxf6: no piece d4-d6; ...c5! then Nxc5 hits Bd3 (never Rxc5); no Nf5 while e6. Tartakower ...b6/...Bb7/...Nbd7 (g136): 11.cxd5 Nxd5 12.Bxe7 Qxe7 13.Nxd5 Bxd5 14.dxc5 Nxc5 =; after that no piece onto a square he attacks with 0 of my guards.
- Caro B Advance (g134,g135,g137): ...Bf5/Bg6 e6 Nd7 c5 Be7 Rc8 Qb6. Bans: ...Qxd4, ...Qd6 (vs Bf4 exd6), ...Bg5??, ...Qxb2, ...Be4 (7.Nxe4! dxe4 = +1.86), ...Nc5 while d4, any piece on d6/f6 or ...Ngf6 while e5. Keep ...Bh7 (guards g6); vs b3/Ba3 ...Bxa3!; free b6 BEFORE ...Qb6; ...Nxe5 only with ONE recapturer (g129). f7 is g6's only pawn guard: ...f6/...fxe5 frees Ng1-e2-f4-g6 forking h8+f8 (g135).
- Caro B clamp 4.h4 h6 5.Nc3 e6 6.g4 ...Bh7 8.f4 9.Nf3 c5 10.Bd3 (0-3): 10...c4?! BAN - c6 goes, so d5's only guard is the b6-knight; 11.Bxh7 Rxh7 12.f5! exf5 13.gxf5 (+3.4; e5/f5/h5 clamp), 16.a5! hunts b6 (16...O-O-O?? 17.axb6 = N for P). Prefer ...Bxd3/...cxd4. After O-O-O keep c7 covered.
- Caro B Classical (g130): ...Bg6 h6 Bh7 e6 Bxd3 Qxd3 Nd7 Ngf6 Be7 O-O =; no piece to f6 while his e5 stands; never Qxb2+ vs Kb1; Rd7 hits c7-knight (...Nd5!).
- Caro W 3.Nc3: 15.d5! exd5 16.cxd5 Re8 = space edge; no sacs (Bxh6); NO Qg6 (g127); Kb1 vs ...Rad8: trade rooks/make luft, never grab (g123).
- Ruy Chigorin W (0-6): 13.cxd4 Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (kills Qd1-d4, g121). B: 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5 =; Qc7 retreats when the c-file opens.
- Dragon B: 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4! only.

## Opponents
- SF19: instant; punishes loose units and queens on his ranks/rays/pawn diagonals; converts cleanly; vs the Caro clamp he plays Bxh7/f5/a4-a5 (g137).
- Sonnet 5.5 (never beaten): banks clock; takes every free unit; trades into simple winnable endings; never misses a recapture (g132); builds Q+B mate batteries vs my castled king (g138 Bc6+Qd5, 21...Qxg2#) and gives R for B to get there.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn diagonal (g133 dxe4, g136 exd5); no sacs/grabs; converts by trading rooks, then a B-for-N, then Q+minor vs Q (g136); mate net closes fast.
