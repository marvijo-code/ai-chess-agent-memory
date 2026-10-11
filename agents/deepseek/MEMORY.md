# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue g1-147
- notes/caro-advance-black.md - Caro Advance B: Clamp + 4.Be2 + Classical 3.Nc3
- notes/qgd-white.md - QGD W Lasker/Bf4-IQP/Exchange/Tartakower/IQP-g146
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O needs knight off home + f8/g8 empty (g124). After O-O-O the king is on c8, so ...Rc8 is ILLEGAL (g137, 1:16 wasted). Before any bishop move its path AND destination must be empty (g140 8...Be7 illegal while my own Ne7 sat on e7; g145 19.Bc2 blocked by my own castled Rf1). After ONE rejection NEVER resend: redraw, list the move's squares, pick another idea (g144 20...Qxg6 twice, 1:43).
- SELF-BAN: a move my scan or note called bad is DEAD (g141 Rc1; g144 24...Qxe5 after my own note banned it 2 plies earlier). Reread the ban list before every knight, rook AND queen move.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first (attacks, pawn controls, opened lines), then MY destination: 0 of my guards + his capture = gift; hitting two of his units is no safety (g136 16.Nd7?? hit Nc5+Rf8 but Qe7+Nc5 owned it). g142 16.Ng6?? 'forked' Qe7+Rf8, f7-pawn took it = N for P (g118,g119); a bishop recapture of the pawn does NOT win the piece back.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7. g140 17...Nc5?? landed on c5 hit by BOTH White pawns b4 and d4 -> 18.dxc5 Bxc5 19.bxc5 = N+B for 2P.
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves, his attack lands. g145 18.e4?? kicked Nd5, the only screen on Be6-b3 (my Qb3) -> 18...Nf4! discovered Bxb3 AND hit Bd3 = Q for B. Queen + his bishop on one diagonal: move the QUEEN off that line first.
- PAWN PUSHES end guard duty AND can be screens: g135 9...f6? removed f7, g6's only pawn guard -> 10.Nf4! Ng6 forked h8+f8; g144 19...h6?? removed h7, the g6-knight's ONLY guard -> 20.Bxg6; g146 20.b3?? vacated b2, the last screen on Bf6-a1 -> 20...Bxa1!.
- Knight jump/retreat only where THAT knight cannot take AND his queen/rook own no line to the square: g139 15...Nd7?? 'covered' by Qd8 but Qd3+Rd1 hit d7 -> N gone; g146 17.Nc4?? 'defended' by Qd3 but Qd5 hit it and Rc8 sat behind: Qxc4 Qxc4 Rxc4 = N gone. A pawn-kick square chases it; a5 hunts a b6-knight (g137).
- Rook files/bishop rays own whole lines; attacked+undefended -> save NOW (g141 23.Rc1?? walked onto Rc6's file); mate net before any grab (g147 26...Nxd4?? grabbed while mate loomed). Long castled: c7 is the escape square - cover it (g137 20.Nxd5! forked Qc7+Be7, 21.Ra8#).

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?' - g138 21...Qxg2# (his Qd5 backed by Bc6 on c6-d5-e4-f3-g2; my Rf1 and h2-pawn guard nothing) landed while I 'saved' the attacked Qd3. g145 34.e5?? was the LAST screen on that same diagonal -> 34...Qxg2#. Never push/capture the last screen between his queen and my king.
- His queen landing in front of my castled king + a bishop behind it = mate net. The reply must block that diagonal (e4) or trade queens - saving the queen alone is not a defence.
- Back rank: Kg1 + f2/g2/h2 pawns = no flight; his rook/queen on rank 1 mates once my rank-1 blockers are gone (g141 23...Rxc1+ 24.Ne1 Rxe1#; g143 23.Rd2?? Qe1#; g146 26...Re1#). Keep a rank-1 blocker or make luft before the last one leaves.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray; a retreat along the same line is still en prise (g134 Qd8?? on a5-b6-c7-d8: Bxd8; g140 21...Qc8?? stayed on the c-file facing Rc1 -> 22.Rxc8). 'Defended' never counts (g95); if the queen AND another piece are attacked, the QUEEN moves first (g145 19.Bc2 'defended' her, 19...Bxb3 = Q for B). A queen as the sole guard of a piece his queen attacks loses it (g146 Qxc4).
- PAWN DIAGONALS before every queen destination: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6. Q for a pawn 5x: g131 Qxf5?? exf5; g133 Qe4?? dxe4; g136 Qd5?? exd5; g143 Qxe6?? fxe6; g144 24...Qxe5?? fxe5.
- List ranks/files/diagonals + knight jumps; no capture on a defended square or ray; checks only if K can't take and no pawn takes (g127). Her lines change when she lands (g143). To hit his Q my attacker must be defended (g133 Rc4?? Qxc4).
- QUEEN takes: count EVERY defender incl. pawns, knights, THE KING (g110,g130 Qxb2+?? Kxb2); pawn recapture before a queen trade.

## Rule 3 - captures
- RECAPTURE != TRADE: say what I win AND what he wins back (g141 22.Rxc6?? Rxc6 = R for P - the c6-pawn was guarded by Rc8); 2 attackers vs 3 defenders = no (g126). His queen takes my piece, my queen recaptures, his rook recaptures: queens off, my piece gone (g139 d7, g146 c4).
- A 'trade' move needs MY recapturer on the destination or it is a gift (g141 23.Rc1?? offered a rook trade, nothing of mine defended c1).
- RECAPTURE CHOICE - keep the recapturer's OTHER guards: g144 15...Bxf6? moved the e7-bishop off e7, c5's ONLY guard -> 16.Bxc5! Bxc3 17.bxc3 = White won a piece; ...Qxf6/...gxf6 keeps e7. g143 14...Bxf3! 15.Qxf3?? moved the queen off e2-d3-c4, Bc4's only guard -> 15...Rxc4; 15.gxf3! keeps her on post.
- Count EVERY recapturer - PAWNS FIRST, then rooks/queens behind the first defender (g129 missed Re1; g131 e6-pawn = Q for P). Trace MY recapture through MY OWN pieces (g121 own Bd2 = Qd1 never retook d4). Broken chain, don't take.
- A piece that cannot move is not lost: name the ATTACKER (g135: nothing attacked Nh8). PIN freezes a recapturer; blocked guard = no guard; a push abandons guard duty (g137 ...c4?! left d5 to a lone b6-knight).

## Rule 4 - material & clock
- Down: keep queens (repetition); NO grabs (g132-g147; g147 26...Nxd4?? grabbed a pawn with mate looming); loose pieces first; defend loose pawns BEFORE quiet moves; 5-10 s.
- Up: trade pieces not pawns; escort passers; promote; stalemate-check; one hung unit kills a +1 edge (g128). R-ending: HOLD equal; R for P loses (g111).
- Equal: mate net before any grab; NO piece-for-pawn sac (g127). Re-count material FROM THE BOARD after every capture (g131, g138).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g134-g147: 20-81 s routine thinks still blundered; g147 40-46 s on EVERY move 12-26, ended 7:08 v 19:39 - 8 min spent, still mated. SF19 instant; Sol 4-19 s; Sonnet 1-64 s.

## Openings
- Caro B Advance plan: ...Bf5/Bg6, ...e6, ...Nd7, ...c5, ...Be7, ...Rc8, ...Qb6. BANS: ...Qxd4, ...Qd6 (vs Bf4 exd6), ...Bg5??, ...Qxb2, ...Be4 (7.Nxe4! dxe4 = +1.86), ...Nc5 while d4 OR b4, any piece on d6/f6 or ...Ngf6 while e5, ...h6 while his bishop can hit a g6 piece, ...f6 while f7 is g6's only guard. Keep ...Bh7; vs b3/Ba3 ...Bxa3!; free b6 BEFORE ...Qb6; ...Nxe5 only with ONE recapturer (g129).
- Caro B 4.Be2 (0-3, g140,g144,g147): 3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 7.Nh4 Bg6 8.O-O c5 9.Nxg6 hxg6 - recapture ...hxg6 (g140,g147), NEVER ...Nxg6?! (g144: a knight on g6 is a target; 19.Bh5 then h6?? and 20.Bxg6 won it). White clamps with g4/f4 and breaks f5: g147 18...Bf8?! passive let 21.f5! win the exchange (f5+gxf5+exf5+Bxf5+Bxc8). COUNTER EARLY with ...f6/...Nc5/...a5/...b5 or central play, never a shuffle.
- Caro B clamp 4.h4 h6 5.Nc3 e6 6.g4 Bg6 7.h5 Bh7 8.f4 (0-3): 10...c4?! BAN - c6 goes, so d5's only guard is the b6-knight; 11.Bxh7 Rxh7 12.f5! exf5 13.gxf5 (+3.4); 16.a5! hunts b6. After O-O-O keep c7 covered; prefer ...Bxd3/...cxd4.
- Caro B Classical (g130, g139): ...Bxd3 Qxd3, ...Be7, O-O, Kb1, Nbd7, then 14.Ne5 Nxe5 15.dxe5: the f6-knight MUST go ...Nd5 (c6-pawn covers); 15...Nd7?? = N for nothing (Qd3 AND Rd1 hit d7). No piece to f6 while his e5 stands; never ...Qxb2+ vs Kb1.
- Caro W 3.Nc3: 15.d5! exd5 16.cxd5 Re8 = space edge; no sacs (Bxh6); NO Qg6 (g127); Kb1 vs ...Rad8: trade rooks/make luft, never grab (g123).
- QGD W (0-16): Lasker g138: 15.Ne5?? only trades; after dxe5 the e5-pawn hangs (my e3 blocks Qe2's file guard) -> ...Qc5/...Qxe5; 20...Qd5! = Qxg2# battery (Bc6 backs g2). Keep c3+d4+Rc1; ...Qb4 hits b2; never Qx b7/d7/a8 vs c6-bishop; e6-pawn kills d5/f5; ...Bxf3/...Nxd4 on my queen: only d1/d3/e3 safe; ...c5! then Nxc5 hits Bd3; no Nf5 while e6. g141: 22.Rxc6?? R for P; 23.Rc1?? Rxc1+ Rxe1#. g142 Lasker: 16.Ng6?? fxg6 = N for P. Tartakower g136: 11.cxd5 Nxd5 12.Bxe7 Qxe7 13.Nxd5 Bxd5 =. g145 Lasker blockade: the d5-knight SCREENS Be6-b3 (my Qb3); 18.e4?? Nf4! = Q for B - move the queen off b3 (Qc2) before any kick. g143 Bf4-IQP: 13...Nb4! hits Qd3; 14.Qe2 keeps the queen on the c4-guard; 14...Bxf3! 15.gxf3! (15.Qxf3?? Rxc4). g146 IQP: 13.Bxf6 Nxf6 14.Ne5 Nd5 15.Nxd5 Bxd5 16.Bxd5 Qxd5 - d4-pawn defends Ne5; 17.Nc4?? Qxc4 Qxc4 Rxc4.
- Ruy Chigorin W (0-6): 13.cxd4 Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (kills Qd1-d4, g121). B: 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5 =; Qc7 retreats when the c-file opens.
- Dragon B: 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4! only.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his ranks/rays/pawn diagonals and knights on pawn-hit squares (g140 c5). g144: took the c5-knight the moment Be7 left, took the g6 piece after h6, played exf6! at once. g147: after 18...Bf8?! it rolled g4/f4/f5 (19.Bb5 a6 20.Bd3 Nb6?! 21.f5! +4.96), won the exchange and then 25...f5 26.exf6 e.p. - the f6-pawn guarded g7, so my Bg7 block lost to 28.Qxg7#. Never shuffle passively vs a pawn clamp.
- Sonnet 5.5 (never beaten): banks clock; takes every free unit; trades into simple winnable endings; never misses a recapture (g132); builds Q+B mate batteries vs my castled king (g138) and gives R for B to get there. g141: took the loose c6-rook, then Rxc1+ and Rxe1# once my last rook left rank 1. g142: took 16.Ng6?? with fxg6, promoted, mated (Qb7#); 1-64 s/move. g145: ...Nf4 discovery won Q for B, then Qd4/Qxb3/Ne2+ (fork Kg1+Rc1)/Qxc2, mate Qxg2# the moment my screen pushed - never give her a screen, a discovery or a free unit.
- GPT-6.1 Sol: fast (4-19 s); takes every free piece incl. a queen on any pawn diagonal (g133 dxe4, g136 exd5) and any piece his queen hits when my queen is the only guard with his rook behind on the file (g146 17...Qxc4 Qxc4 Rxc4 = N for P); no sacs/grabs; converts by trading queens+rooks into R+B vs R; mate net closes fast (g139 R to 7th + Bf6#; g146 26...Re1# with Bf6 backing e1). g143: Rxc4 the moment 15.Qxf3?? left the bishop loose, then Qxe6?? fxe6, Qe1#.
