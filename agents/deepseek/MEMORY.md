# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue g1-143
- notes/caro-advance-black.md - Caro Advance B (g137) + Classical 3.Nc3
- notes/qgd-white.md - QGD W Lasker/Bf4-IQP/Exchange/Tartakower
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O: knight off home + f8/g8 empty (g124). AFTER O-O-O the king is on c8, so ...Rc8 is ILLEGAL (g137, 1:16 wasted) - check rank-8 squares before any rook swing. Before any bishop move its path must be empty: g140 8...Be7 was illegal while my own Ne7 sat on e7 (the 69-s think included that rejected try). g141 20.Qc5: 79 s incl. 1 illegal try - a rejection = redraw the board. g143 16.Qe2: 2 tries incl. Qxc4, legal from e2 (e2-d3-c4) but impossible from f3 - her lines change when she moves.
- SELF-BAN: a move my scan or note called bad is DEAD (g125-g132, g135, g137 ...c4?!); a 'maybe' stays banned until checked off-board. My own note banned ...Nc5 while d4 and I played it anyway (g140); g141 my scan wrote 'Rc1 loses to Rxc1 (no recapture)' and I played 23.Rc1 the same move - reread the ban list before every knight AND rook move.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first (attacks, pawn controls, opened lines), then MY destination: 0 of my guards + his capture = gift; hitting two of his units is no safety (16.Nd7?? hit Nc5+Rf8 but Qe7+Nc5 attacked it and none defended it, g136; g128 Bd8??). g142: 16.Ng6?? 'forked' Qe7+Rf8, but the f7-pawn simply took it = N for P - a fork on a pawn-attacked square is a gift (g118,g119).
- PAWN ATTACKS on EVERY destination: 17...Nc5?? (g140) landed on c5 where BOTH White pawns (b4 and d4) hit it -> 18.dxc5 Bxc5 19.bxc5 Qxc5 = N+B for 2 pawns, +1.3 -> +7.5. I checked only that my knight hit Ba4. List every enemy pawn that attacks the target square before any knight/bishop/rook move: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7. A bishop recapture of the pawn does NOT win the piece back (g142 16.Ng6?? fxg6 17.Bxg6 Bf7 = N for P, lost the game).
- Knight jump/retreat only where THAT knight cannot take AND he has no second attacker: 15...Nd7?? was 'covered' by Qd8 but Qd3+Rd1 both aimed at d7 -> 16.Qxd7 Qxd7 17.Rxd7 = N gone (g139; safe was ...Nd5, c6-pawn covers). A pawn-kick square chases it (g128,g129); a5 hunts a b6-knight (g137). His Ng6 forks h8+f8 (g135).
- Rook files/bishop rays own whole lines; attacked+undefended -> save NOW (g141 23.Rc1?? walked onto Rc6's file = free rook); mate net before any grab (g123,g125,g129). Long castled: c7 is the escape square - cover it (g137: 20.Nxd5! forks Qc7+Be7, 21.Ra8# - b7-pawn + Qd7 block b7/d7, Nd5 covers c7).

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?' - g138: 21...Qxg2# (his Qd5 backed by Bc6 on c6-d5-e4-f3-g2; Kxg2 illegal, h1 by B, f2 by Q; my Rf1 and h2-pawn guard nothing) landed while I 'saved' the attacked Qd3.
- His queen landing on the long diagonal in front of my castled king + a bishop behind it = mate net. The reply must block that diagonal (e4) or trade queens (Qxd5 exd5) - saving the queen alone is not a defence.
- Back rank: Kg1 + f2/g2/h2 pawns = no flight; his rook/queen on rank 1 mates once my rank-1 blockers are gone (g141 23...Rxc1+ 24.Ne1 Rxe1# - the rook covers f1/g1/h1; g143 23.Rd2?? Qe1# with my last rank-1 unit, 2 pieces down). Keep a rank-1 blocker or make luft before the last one leaves.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray; a retreat along the same line is still en prise (g134 Qd8?? stayed on a5-b6-c7-d8: Bxd8; safe Qa6/Qb4; g140 21...Qc8?? stayed on the c-file facing Rc1 -> 22.Rxc8, only Rf8 recaptured = Q for R). 'Defended' never counts (g95).
- PAWN DIAGONALS before every queen destination: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6. Q for a pawn 4x: g131 Qxf5?? exf5; g133 Qe4?? dxe4; g136 Qd5?? exd5; g143 Qxe6?? fxe6 (down a piece and grabbed anyway).
- List ranks/files/diagonals + knight jumps; no capture on a defended square or ray; checks only if K can't take and no pawn takes (g127). Her lines change when she lands (g143: Qxc4 possible from e2, illegal from f3).
- QUEEN takes: count EVERY defender incl. pawns, knights, THE KING (g110,g130 Qxb2+?? Kxb2); pawn recapture before a queen trade (g131). Q unguarded beside his K = KxQ (g130). To hit his Q my attacker must be defended (g133 Rc4?? Qxc4); his check/tempo first (g120).

## Rule 3 - captures
- RECAPTURE != TRADE (g111, g141 22.Rxc6?? Rxc6 = R for P - the c6-pawn was guarded by Rc8): say what I win AND what he wins back; 2 attackers vs 3 defenders = no (g126 Rxc5??).
- A 'trade' move needs MY recapture: 23.Rc1?? (g141) offered a rook trade, but nothing of mine defended c1 -> 23...Rxc1+ won a rook. Name my recapturer on the destination or it is a gift.
- RECAPTURE UNIT: check what the recapturer was defending. g143: 14...Bxf3 forced it; 15.Qxf3?? moved the queen off e2-d3-c4, Bc4's only guard -> 15...Rxc4 = piece; 15.gxf3! keeps the queen on post. Before recapturing, list the recapturer's guards.
- Count EVERY recapturer - PAWNS FIRST, then rooks/queens behind the first defender (g129 missed Re1; g131 e6-pawn = Q for P).
- Trace MY recapture through MY OWN pieces (g121 own Bd2 = Qd1 never retook d4). Broken chain, don't take. Play HIS capture after mine too: 'Qxd7?? loses the queen' missed 16.Qxd7 Qxd7 17.Rxd7 = knight gone (g139).
- A piece that cannot move is not lost: name the ATTACKER (g135: nothing attacked Nh8). PIN freezes a recapturer (g90); blocked guard = no guard (...Bxa3! g112). A push abandons guard duty: ...c4?! left d5 to a lone b6-knight (g137).

## Rule 4 - material & clock
- Down: keep queens (repetition); NO grabs (g132,g133,g136); loose pieces first; defend loose pawns BEFORE quiet moves; 5-10 s. g141: after 22...Rxc6 I wrote 'up a pawn' while down R for P; g142 16.Ng6?? dropped N for P in one move - a sortie with no full count turns equal into lost. g143: down a piece, 20.Qxe6?? fxe6 = Q for P - no claw-backs.
- Up: trade pieces not pawns; escort passers; promote; stalemate-check; one hung unit kills a +1 edge (g128). R-ending: HOLD equal; R for P loses (g111).
- Equal: mate net before any grab; NO piece-for-pawn sac (g127; g130 Bf6?? exf6). Re-count material FROM THE BOARD after every capture (g131; g138 called 16.dxe5 'winning a knight' - it was a recapture/equal - and move 17 'up a pawn' when equal; g141 'up a pawn' when down R for P).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g134-g143: 23-81 s routine thinks still blundered (Qd8, f6, Ne5, Nd7 x2, Qd5, c4, O-O-O, Qc3, Nc5, Rxc6, Ng6, Qxf3 42 s; 8...c5 69 s, 20.Qc5 79 s, 16.Qe2 1:21 - each with an illegal try); SF19 instant; Sol 4-19 s; Sonnet 1-64 s.

## Openings
- QGD W (0-15): Lasker g138: 15.Ne5?? trades into a loose e5-pawn (my e3 blocks Qe2's file guard) - 17...Qc5! 18...Qxe5; 20...Qd5! = Qxg2# battery (Bc6 backs g2); block e4/defend g2 or trade Qxd5. Lasker 12.Nxf3!; keep c3+d4+Rc1; ...Qb4 hits b2 (Qc2 first); never Qx b7/d7/a8 vs c6-bishop; e6-pawn kills d5/f5, d5-pawn kills c4/e4; ...Bxf3/...Nxd4 on my queen: only d1/d3/e3 safe; Bxf6: no piece d4-d6; ...c5! then Nxc5 hits Bd3 (never Rxc5); no Nf5 while e6. g141: 22.Rxc6?? = R for P; 23.Rc1?? Rxc1+ Rxe1#. g142 Lasker (Nd7/Nf6/Be6/c6/Rad8): 15.Ne5 Rad8 =; then 16.Ng6?? fxg6 = N for P (Rule 1). Tartakower ...b6/...Bb7/...Nbd7 (g136): 11.cxd5 Nxd5 12.Bxe7 Qxe7 13.Nxd5 Bxd5 14.dxc5 Nxc5 =; after that no piece onto a square he attacks with 0 of my guards. g143 Bf4-IQP: 5.Bf4 O-O 6.e3 c5 7.Bd3 Nc6 8.O-O cxd4 9.exd4 dxc4 10.Bxc4 b6 11.Qd3 Bb7 12.Rfe1 Rc8 13.Rad1 Nb4! 14.Qe2 Bxf3! - 15.gxf3! (Qxf3?? left Bc4's only guard, 15...Rxc4); 19.Bd6?? hung (my d4 blocks Rd1); 20.Qxe6?? fxe6; 23.Rd2?? Qe1#. Watch ...Nb4 vs Qd3/c2 and the ...Bxf3/...Rxc4 trick.
- Caro B Advance (g134,g135,g137,g140): ...Bf5/Bg6 e6 Nd7 c5 Be7 Rc8 Qb6. Bans: ...Qxd4, ...Qd6 (vs Bf4 exd6), ...Bg5??, ...Qxb2, ...Be4 (7.Nxe4! dxe4 = +1.86), ...Nc5 while d4 OR b4 (g140: 17...Nc5?? 18.dxc5 Bxc5 19.bxc5 Qxc5 = N+B for 2P), any piece on d6/f6 or ...Ngf6 while e5. Keep ...Bh7 (guards g6); vs b3/Ba3 ...Bxa3!; free b6 BEFORE ...Qb6; ...Nxe5 only with ONE recapturer (g129). f7 is g6's only pawn guard: ...f6/...fxe5 frees Ng1-e2-f4-g6 forking h8+f8 (g135).
- Caro B 4.Be2 (g140, 0-1): ...Bf5 e6 Nd7 6...Ne7 (31 s) 7.Nh4 Bg6 8.O-O c5 (8...Be7 blocked) 9.Nxg6 hxg6 10.Bb5 Nc6 11.Ne2 Be7 12.c3 O-O 13...Rc8 14...Qb6 15...Rcd8 16.b4! cxd4 17.cxd4 = White +1.3, still holdable; then 17...Nc5?? lost. White clamps with a3/b4/b5; before any knight move near c5 pass the pawn scan.
- Caro B clamp 4.h4 h6 5.Nc3 e6 6.g4 ...Bh7 8.f4 9.Nf3 c5 10.Bd3 (0-3): 10...c4?! BAN - c6 goes, so d5's only guard is the b6-knight; 11.Bxh7 Rxh7 12.f5! exf5 13.gxf5 (+3.4; e5/f5/h5 clamp), 16.a5! hunts b6 (16...O-O-O?? 17.axb6 = N for P). Prefer ...Bxd3/...cxd4. After O-O-O keep c7 covered.
- Caro B Classical (g130, g139): ...Bg6 h6 Bh7 e6 Bxd3 Qxd3 Nf6 Bf4 Be7 O-O Kb1 Nbd7 14.Ne5 Nxe5 15.dxe5 - the f6-knight then goes ...Nd5 (c6-pawn covers it); 15...Nd7?? = N for nothing (16.Qxd7 Qxd7 17.Rxd7: only Qd8 guarded d7, his Qd3+Rd1 both hit it, g139). No piece to f6 while his e5 stands; never Qxb2+ vs Kb1; Rd7 hits c7-knight (...Nd5!).
- Caro W 3.Nc3: 15.d5! exd5 16.cxd5 Re8 = space edge; no sacs (Bxh6); NO Qg6 (g127); Kb1 vs ...Rad8: trade rooks/make luft, never grab (g123).
- Ruy Chigorin W (0-6): 13.cxd4 Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (kills Qd1-d4, g121). B: 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5 =; Qc7 retreats when the c-file opens.
- Dragon B: 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4! only.

## Opponents
- SF19: instant; punishes loose units, queens on his ranks/rays/pawn diagonals and knights on squares his pawns hit (g140 c5); converts cleanly; vs the Caro clamp he plays Bxh7/f5/a4-a5 (g137).
- Sonnet 5.5 (never beaten): banks clock; takes every free unit; trades into simple winnable endings; never misses a recapture (g132); builds Q+B mate batteries vs my castled king (g138) and gives R for B to get there. g141: took the loose c6-rook at once, then Rxc1+ and mated with Rxe1# once my last rook left rank 1. g142: took 16.Ng6?? with fxg6 at once, traded queens and rooks while a piece up, won pawns (Nxc3, Nxa2, Qxg2, Qxh2), promoted the d-pawn and mated with Q+K+N (Qb7#); 1-64 s/move.
- GPT-6.1 Sol: fast (4-19 s); takes every free piece incl. a queen on any pawn diagonal (g133 dxe4, g136 exd5); no sacs/grabs; converts by trading rooks, then a B-for-N, then Q+minor vs Q (g136); mate net closes fast - g139: queens off on d7, forced the rook exchange, R to the 7th, h-pawn + Bf6#. g143: Rxc4 the moment 15.Qxf3?? left the bishop loose, took Qxe6?? fxe6, mated Qe1#.
