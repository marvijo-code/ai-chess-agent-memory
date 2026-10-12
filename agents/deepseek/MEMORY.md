# Chess memory

Notes:
- notes/capture-safety.md - scan + blunder catalogue g1-149
- notes/caro-advance-black.md - Caro Advance B: Clamp + 4.Be2 + Classical 3.Nc3
- notes/qgd-white.md - QGD W: Lasker/Bf4-IQP/Exchange/Tartakower/Bb4-IQP g149
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O needs knight off home + f8/g8 empty (g124). After O-O-O the king is on c8, so ...Rc8 is ILLEGAL (g137, 1:16 wasted). Before any bishop move its path AND destination must be empty (g140 8...Be7 illegal while my own Ne7 sat on e7; g148 ...Be7 illegal at move 9 with Ne7 still home; g145 19.Bc2 blocked by my own castled Rf1). After ONE rejection NEVER resend: redraw, write out every legal square of that piece, then choose (g144 20...Qxg6 twice, 1:43; g149 28.Qe3 rejected, 28.Qg2?? still a blunder - no real redraw).
- SELF-BAN: a move my scan or note called bad is DEAD (g141 Rc1; g144 24...Qxe5 after my own note banned it 2 plies earlier). Reread the ban list before every knight, rook AND queen move.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first (attacks, pawn controls, opened lines), then MY destination: 0 of my guards + his capture = gift; hitting two of his units is no safety (g136 16.Nd7??). g142 16.Ng6?? 'fork' taken by f7-pawn; a bishop recapture of the pawn does NOT win the piece back.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7. g140 17...Nc5?? landed on a square hit by BOTH b4 and d4 pawns -> 18.dxc5 Bxc5 19.bxc5.
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves, his attack lands. g145 18.e4?? kicked Nd5, the only screen on Be6-b3 (my Qb3) -> 18...Nf4! = Q for B. g148 17...Bg5?? traded the screen on his bishop's g5-d8 line to my queen -> 19.Bxd8.
- PAWN PUSHES end guard duty AND can be screens: g135 9...f6? removed f7, g6's only guard -> 10.Nf4!; g144 19...h6?? removed h7, the g6-knight's ONLY guard -> 20.Bxg6; g146 20.b3?? vacated b2, the last screen on Bf6-a1 -> 20...Bxa1!.
- Knights and rooks only where they are GUARDED: g139 15...Nd7?? (Qd3+Rd1 hit d7); g146 17.Nc4?? 'defended' by Qd3 but Rc8 sat behind: Qxc4 Qxc4 Rxc4 = N gone. g148 21...Rc7?? a rook 'generating activity' with NO guard -> 22.Rxc7 = R for P; g148 23...Nb7?? unguarded knight 'attacking' Ra7 -> 24.Rxb7. A rook on an open file must be defended.
- Rook files/bishop rays own whole lines; attacked+undefended -> save NOW (g141 23.Rc1?? walked onto Rc6's file); mate net before any grab (g147 26...Nxd4??). Long castled: c7 is the escape square - cover it.
- d4 under a battery: count HIS attackers and my recapturers every move - g149 12.Qd3?! then 12...Nxd4! 13.Nxd4 Qxd4 = N for N+pawn (SF takes on d4 the moment the chain is short).

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?' - g138 21...Qxg2# landed while I 'saved' my attacked queen; g145 34.e5?? was the LAST screen on that same diagonal -> 34...Qxg2#. Never push/capture the last screen between his queen and my king.
- His queen landing in front of my castled king + a bishop behind it = mate net. The reply must block that diagonal (e4) or trade queens - saving the queen alone is not a defence.
- Back rank: Kg1 + f2/g2/h2 pawns = no flight; his rook/queen on rank 1 mates once my rank-1 blockers are gone (g141 Rxc1+/Rxe1#; g143 Qe1#; g146 Re1#; g148 Rc8# with Ra7 sealing rank 7). Keep a rank-1 blocker or make luft before the last one leaves. g149 31.f3?? blocked Be4+ with an UNGUARDED pawn on a diagonal to my king -> 31...Bxf3#: a check-blocker must be defended.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray; a retreat along the same line is still en prise (g134 Qd8?? on a5-b6-c7-d8: Bxd8; g149 28.Qg2?? stayed on the g-file under Rg4 -> 28...Rxg2+ = Q for R). 'Defended' never counts (g95); if the queen AND another piece are attacked, the QUEEN moves first (g145 19.Bc2, 19...Bxb3 = Q for B). A queen as the sole guard of a piece his queen attacks loses it (g146 Qxc4; g149 14.Qg3?? left Bc4 unguarded -> 14...Qxc4).
- AFTER EVERY QUEEN MOVE write down what she no longer guards and re-list her lines from the new square.
- NEVER OFFER A 'TRADE' WHOSE RECAPTURE IS ILLEGAL OR LOSING: g148 17...Bg5?? - after 18.Bxg5 my recapture Qxg5 loses to Nxg5, so 19.Bxd8 took my queen = Q for B. Before any offer on a line to my queen, name the recapture and what it leaves standing on that line.
- PAWN DIAGONALS before every queen destination: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6. Q for a pawn 5x: g131 Qxf5?? exf5; g133 Qe4?? dxe4; g136 Qd5?? exd5; g143 Qxe6?? fxe6; g144 24...Qxe5?? fxe5.
- List ranks/files/diagonals + knight jumps; no capture on a defended square or ray; checks only if K can't take and no pawn takes (g127). Her lines change when she lands (g143). To hit his Q my attacker must be defended (g133 Rc4?? Qxc4).
- QUEEN takes: count EVERY defender incl. pawns, knights, THE KING (g110,g130 Qxb2+?? Kxb2); pawn recapture before a queen trade.

## Rule 3 - captures
- RECAPTURE != TRADE: say what I win AND what he wins back (g141 22.Rxc6?? Rxc6 = R for P); 2 attackers vs 3 defenders = no (g126). His queen takes my piece, my queen recaptures, his rook recaptures: queens off, my piece gone (g139 d7, g146 c4).
- A 'trade' move needs MY recapturer on the destination or it is a gift (g141 23.Rc1??).
- RECAPTURE CHOICE - keep the recapturer's OTHER guards: g144 15...Bxf6? moved the e7-bishop off e7, c5's ONLY guard -> 16.Bxc5! Bxc3 17.bxc3; ...Qxf6/...gxf6 keeps e7. g143 14...Bxf3! 15.Qxf3?? moved the queen off the c4-guard -> 15...Rxc4; 15.gxf3! keeps her on post.
- Count EVERY recapturer - PAWNS FIRST, then rooks/queens behind the first defender (g129 missed Re1; g131 e6-pawn = Q for P). Trace MY recapture through MY OWN pieces (g121 own Bd2 = Qd1 never retook d4). Broken chain, don't take.
- A piece that cannot move is not lost: name the ATTACKER. PIN freezes a recapturer; blocked guard = no guard; a push abandons guard duty.

## Rule 4 - material & clock
- Down: keep queens (repetition) only while they are SAFE; NO grabs (g132-g149; g147 26...Nxd4?? grabbed a pawn with mate looming; g148 18...bxa4 grabbed while my queen was already lost; g149 the queen chase lost Bc4 and then the queen); loose pieces first; defend loose pawns BEFORE quiet moves; 5-10 s.
- Up: trade pieces not pawns; escort passers; promote; stalemate-check; one hung unit kills a +1 edge (g128). R-ending: HOLD equal; R for P loses (g111).
- Equal: mate net before any grab; NO piece-for-pawn sac (g127). Re-count material FROM THE BOARD after every capture (g131, g138).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. g134-g149: 20-81 s routine thinks still blundered (g148 37 s on 15...Rc8, 38 s on 17...Bg5; g147 40-46 s every move; g149 30-37 s defending). SF19 instant; Sol 4-19 s; Sonnet 1-64 s.

## Openings
- QGD Bb4/5.Bg5 IQP (0-1, g149): 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Bb4 5.Bg5 O-O 6.e3 c5 7.Bxf6 Qxf6 8.Bd3 (16 plies), then ...cxd4/...dxc4/...Nc6/...Rd8. BANS: 12.Qd3?! (12...Nxd4! = N for N+P), 14.Qg3?? (she left c4 -> ...Qxc4), 28.Qg2?? (Rg4 on the g-file -> Rxg2+). Keep a second defender on c4 while the queen is the only one.
- Caro B Advance plan: ...Bf5/Bg6, ...e6, ...Nd7, ...c5, ...Be7, ...Rc8, ...Qb6. BANS: ...Qxd4, ...Qd6 (vs Bf4 exd6), ...Bg5??, ...Qxb2, ...Be4 (7.Nxe4! dxe4 = +1.86), ...Nc5 while d4 OR b4, any piece on d6/f6 or ...Ngf6 while e5, ...h6 while his bishop can hit a g6 piece, ...f6 while f7 is g6's only guard. Keep ...Bh7; vs b3/Ba3 ...Bxa3!; free b6 BEFORE ...Qb6; ...Nxe5 only with ONE recapturer (g129).
- Caro B 4.Be2 (0-4, g140,g144,g147,g148): 3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 7.Nh4 Bg6 8.O-O c5 9.Nxg6 hxg6 - recapture ...hxg6, NEVER ...Nxg6?! (a knight on g6 is a target, g144). g148 vs Sonnet (4.Nf3/5.Be2/6.O-O/7.c3/8.Nbd2/9.Nb3): my EARLY ...c5 at move 6 held the game level, with ...cxd4/...Nc6 (frees e7)/...Be7/...O-O/...Re8/...Rc8. Keep that counter against any clamp; never a shuffle (g147 18...Bf8?! let 21.f5! win the exchange). Then the g148 bans: ...Bg5 while his Bf4 sits on it and my queen is behind on g5-f6-e7-d8 (Rule 2); ...Rc7 undefended; ...Nb7 unguarded.
- Caro B clamp 4.h4 h6 5.Nc3 e6 6.g4 Bg6 7.h5 Bh7 8.f4 (0-3): 10...c4?! BAN - c6 goes, so d5's only guard is the b6-knight; 11.Bxh7 Rxh7 12.f5! exf5 13.gxf5 (+3.4); 16.a5! hunts b6. After O-O-O keep c7 covered; prefer ...Bxd3/...cxd4.
- Caro B Classical (g130, g139): ...Bxd3 Qxd3, ...Be7, O-O, Kb1, Nbd7, then 14.Ne5 Nxe5 15.dxe5: the f6-knight MUST go ...Nd5 (c6-pawn covers); 15...Nd7?? = N for nothing. No piece to f6 while his e5 stands; never ...Qxb2+ vs Kb1.
- Caro W 3.Nc3: 15.d5! exd5 16.cxd5 Re8 = space edge; no sacs (Bxh6); NO Qg6 (g127); Kb1 vs ...Rad8: trade rooks/make luft, never grab (g123).
- QGD W (0-17): Lasker g138: 15.Ne5?? only trades; after dxe5 the e5-pawn hangs (my e3 blocks Qe2's file guard) -> ...Qc5/...Qxe5; 20...Qd5! = Qxg2# battery (Bc6 backs g2). Keep c3+d4+Rc1; ...Qb4 hits b2; never Qx b7/d7/a8 vs c6-bishop; e6-pawn kills d5/f5; ...Bxf3/...Nxd4 on my queen: only d1/d3/e3 safe; ...c5! then Nxc5 hits Bd3; no Nf5 while e6. g141: 22.Rxc6?? R for P; 23.Rc1?? Rxc1+ Rxe1#. g142 Lasker: 16.Ng6?? fxg6 = N for P. Tartakower g136: never a piece on d7 (Qe7+Nc5 hit it) or d5 (e6-pawn). g145 Lasker blockade: the d5-knight SCREENS Be6-b3 (my Qb3); 18.e4?? Nf4! = Q for B - move the queen off b3 (Qc2) before any kick. g143 Bf4-IQP: 13...Nb4! hits Qd3; 14.Qe2 keeps the queen on the c4-guard; 14...Bxf3! 15.gxf3! (15.Qxf3?? Rxc4). g146 IQP: 13.Bxf6 Nxf6 14.Ne5 Nd5 (10 plies); 17.Nc4?? Qxc4 Qxc4 Rxc4 = N gone.
- Ruy Chigorin W (0-6): 13.cxd4 Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (kills Qd1-d4, g121). B: 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5 =; Qc7 retreats when the c-file opens.
- Dragon B: 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5.
- Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4! only.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his ranks/rays/pawn diagonals and knights on pawn-hit squares (g140 c5). g144: took the c5-knight the moment Be7 left, took the g6 piece after h6, played exf6! at once. g147: after 18...Bf8?! it rolled g4/f4/f5 (21.f5! +4.96), won the exchange, and 25...f5?? let exf6 e.p. strip a g7-guard. g149: as Black in the QGD it played ...Nxd4! the moment my d4 recapture chain was short, then took the unguarded c4-bishop with the queen and converted a piece up without a slip. Never shuffle passively vs a pawn clamp; never let a queen move leave a bishop unguarded.
- Sonnet 5.5 (never beaten): banks clock; takes every free unit; trades into simple winnable endings; never misses a recapture; builds Q+B mate batteries vs my castled king. g141 Rxc1+/Rxe1#; g142 fxg6 then Qb7#; g145 ...Nf4 discovery = Q for B then Qxg2#; g148: 18.Bxg5 when my recapture Qxg5 lost to Nxg5 (Q for B), then Rxc7 and Rxb7 took my two undefended pieces and Rc8# came. Never give her a screen, a discovery or a free unit; never offer a trade whose recapture is illegal.
- GPT-6.1 Sol: fast (4-19 s); takes every free piece incl. a queen on any pawn diagonal (g133 dxe4, g136 exd5) and any piece his queen hits when my queen is the only guard with his rook behind on the file (g146 17...Qxc4 Qxc4 Rxc4 = N for P); no sacs/grabs; converts by trading queens+rooks into R+B vs R; mate net closes fast (g139 R to 7th + Bf6#; g146 26...Re1#). g143: Rxc4 the moment 15.Qxf3?? left the bishop loose, then Qxe6?? fxe6, Qe1#.
